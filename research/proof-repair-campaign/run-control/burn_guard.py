#!/usr/bin/env python3
"""Bounded POSIX process-group runner; sampled RSS is not a hard memory cap."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import sys
import time

PS_TIMEOUT = 0.5
TERM_GRACE = 0.5
KILL_GRACE = 2.0


def digest(path):
    path = Path(path).resolve(strict=True)
    if not path.is_file():
        raise ValueError(f"not a regular file: {path}")
    h = hashlib.sha256()
    with path.open("rb") as src:
        for block in iter(lambda: src.read(1024 * 1024), b""):
            h.update(block)
    return {"path": str(path), "sha256": h.hexdigest(), "bytes": path.stat().st_size}


def write_receipt(path, data):
    # The caller exclusively reserved this receipt before starting any child.
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("x", encoding="utf-8") as out:
        json.dump(data, out, indent=2, sort_keys=True, allow_nan=False)
        out.write("\n")
    os.replace(temporary, path)


def group_sample(pgid, timeout=PS_TIMEOUT):
    # Darwin -g selects this group; Linux numeric -g selects this session.
    # Both were created with the same id. Filter explicitly by group below.
    # No command strings or environment are requested.
    result = subprocess.run(
        ["/bin/ps", "-g", str(pgid), "-o", "pid=,pgid=,rss=,stat="],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        timeout=timeout, check=True, text=True,
    )
    members = []
    leader_state = None
    for line in result.stdout.splitlines():
        fields = line.split()
        if len(fields) != 4:
            raise RuntimeError("unrecognized ps output")
        pid, group, kib = map(int, fields[:3])
        if pid == pgid:
            if group != pgid:
                raise RuntimeError("leader left its created process group")
            leader_state = fields[3]
        if group == pgid and not fields[3].startswith("Z"):
            members.append({"pid": pid, "rss_bytes": kib * 1024})
    if leader_state is None:
        raise RuntimeError("unreaped leader missing from ps snapshot")
    return members, leader_state.startswith("Z")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--stdout", type=Path, required=True)
    parser.add_argument("--stderr", type=Path, required=True)
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--cpu-seconds", type=int, default=60)
    parser.add_argument("--wall-seconds", type=float, default=75.0)
    parser.add_argument("--rss-bytes", type=int, default=1536 * 1024 * 1024)
    parser.add_argument("--sample-interval", type=float, default=0.1)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    receipt = args.receipt.absolute()
    data = {
        "schema": 1, "status": "invalid_configuration", "command": command,
        "cwd": os.getcwd(), "platform": sys.platform,
        "command_sha256": hashlib.sha256(json.dumps(command).encode()).hexdigest(),
        "enforcement": {
            "address_space_limit_enforced": False,
            "cpu": "RLIMIT_CPU inherited per process; not aggregate group CPU",
            "rss": "sampled sum of resident bytes in the created process group",
            "rss_guaranteed_overshoot_bound_bytes": None,
            "rss_overshoot_note": "No finite byte bound between samples or during scheduler delay.",
            "wall": "monotonic watchdog; scheduler and ps latency can delay detection",
            "ps_timeout_seconds": PS_TIMEOUT, "term_grace_seconds": TERM_GRACE,
            "kill_grace_seconds": KILL_GRACE,
            "containment": "Children must stay in the created group; this is not a sandbox.",
        },
        "samples": 0, "sampled_group_peak_rss_bytes": 0,
        "observed_rss_overshoot_bytes": 0, "child_cpu_seconds": None,
        "child_peak_rss_bytes": None, "child_returncode": None,
        "cleanup_complete": True, "signals_sent": [], "cpu_limit_applied": False,
    }
    # Exclusive reservation makes completed and failed receipts non-overwritable.
    try:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        with receipt.open("x", encoding="utf-8") as out:
            out.write("{}\n")
    except OSError as exc:
        print(f"cannot reserve receipt: {exc}", file=sys.stderr)
        return 2
    try:
        if sys.platform not in ("darwin", "linux") or not hasattr(os, "wait4"):
            raise ValueError("supported platforms are Darwin and Linux with wait4")
        if not command:
            raise ValueError("command is required after --")
        if args.cpu_seconds <= 0 or args.rss_bytes <= 0:
            raise ValueError("CPU and RSS limits must be positive integers")
        if not math.isfinite(args.wall_seconds) or args.wall_seconds <= 0:
            raise ValueError("wall limit must be finite and positive")
        if not math.isfinite(args.sample_interval) or not 0 < args.sample_interval <= 1:
            raise ValueError("sample interval must be finite and in (0, 1]")
        paths = [receipt.resolve(), args.stdout.resolve(), args.stderr.resolve()]
        if len(set(paths)) != 3:
            raise ValueError("receipt, stdout and stderr paths must be distinct")
        if args.stdout.exists() or args.stderr.exists():
            raise ValueError("stdout and stderr paths must not already exist")
        executable = shutil.which(command[0])
        if executable is None:
            raise ValueError("command executable not found")
        artifacts = {str(Path(p).resolve()): digest(p) for p in args.input}
        for argument in command[1:]:
            candidate = Path(argument)
            try:
                if candidate.is_file():
                    artifacts[str(candidate.resolve())] = digest(candidate)
            except OSError:
                pass  # Inline command text need not be a valid filesystem name.
        data["artifacts"] = {
            "supervisor": digest(__file__), "executable": digest(executable),
            "inputs": list(artifacts.values()),
        }
        data["limits"] = {
            "cpu_soft_seconds": args.cpu_seconds, "cpu_hard_seconds": args.cpu_seconds,
            "wall_seconds": args.wall_seconds, "rss_bytes": args.rss_bytes,
            "sample_interval_seconds": args.sample_interval,
        }
    except (ValueError, OSError) as exc:
        data["error"] = str(exc)
        write_receipt(receipt, data)
        return 2

    process = None
    usage = None
    requested_signal = []
    started = time.monotonic()
    old_handlers = {}

    def request_stop(signum, _frame):
        requested_signal.append(signum)

    def signal_group(signum):
        # pgid comes ONLY from our own start_new_session child, never the CLI.
        # The leader is deliberately unreaped until ALL group signals finish,
        # reserving its PID and preventing a recycled-PGID signal race.
        try:
            os.killpg(process.pid, signum)
            data["signals_sent"].append(signal.Signals(signum).name)
        except ProcessLookupError:
            pass

    def observe(timeout=PS_TIMEOUT):
        members, leader_exited = group_sample(process.pid, timeout)
        rss = sum(member["rss_bytes"] for member in members)
        data["samples"] += 1
        if rss > data["sampled_group_peak_rss_bytes"]:
            data["sampled_group_peak_rss_bytes"] = rss
            data["peak_group_members"] = members
        data["observed_rss_overshoot_bytes"] = max(0, data["sampled_group_peak_rss_bytes"] - args.rss_bytes)
        return members, rss, leader_exited

    def cleanup():
        # Even a successful leader is not allowed to leave a running group.
        for signum, grace in ((signal.SIGTERM, TERM_GRACE), (signal.SIGKILL, KILL_GRACE)):
            signal_group(signum)
            deadline = time.monotonic() + grace
            while time.monotonic() < deadline:
                try:
                    members, _, leader_exited = observe(min(PS_TIMEOUT, max(0.01, deadline - time.monotonic())))
                    if not members and leader_exited:
                        return True
                except (OSError, ValueError, RuntimeError, subprocess.SubprocessError):
                    pass  # Continue to KILL when the monitor cannot confirm exit.
                time.sleep(min(0.05, max(0, deadline - time.monotonic())))
        return False

    try:
        for signum in (signal.SIGINT, signal.SIGTERM):
            old_handlers[signum] = signal.signal(signum, request_stop)
        # An inherited ignored SIGCHLD could auto-reap and lose our PID anchor.
        old_handlers[signal.SIGCHLD] = signal.signal(signal.SIGCHLD, signal.SIG_DFL)
        for path in (args.stdout, args.stderr):
            path.parent.mkdir(parents=True, exist_ok=True)
        with args.stdout.open("xb") as out, args.stderr.open("xb") as err:
            data["status"] = "starting"
            write_receipt(receipt, data)
            process = subprocess.Popen(
                command, stdout=out, stderr=err, start_new_session=True,
                preexec_fn=lambda: resource.setrlimit(resource.RLIMIT_CPU, (args.cpu_seconds, args.cpu_seconds)),
            )
            data["pid"] = process.pid
            data["process_group"] = process.pid
            data["cpu_limit_applied"] = True
            data["status"] = "running"
            write_receipt(receipt, data)
            while True:
                if requested_signal:
                    data["status"] = "interrupted"
                    data["requested_signal"] = requested_signal[0]
                    break
                if time.monotonic() - started >= args.wall_seconds:
                    data["status"] = "wall_limit"
                    break
                members, rss, leader_exited = observe()
                if rss > args.rss_bytes:
                    data["status"] = "rss_limit"
                    break
                if leader_exited:
                    if members:
                        data["status"] = "lingering_group"
                    else:
                        data["status"] = "exited_group_empty"
                    break
                time.sleep(min(args.sample_interval, max(0, args.wall_seconds - (time.monotonic() - started))))
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        data["status"] = "monitor_error" if process is not None else "launch_error"
        data["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        if process is not None:
            if data["status"] != "exited_group_empty":
                data["cleanup_complete"] = cleanup()
                if not data["cleanup_complete"]:
                    data["prior_status"] = data["status"]
                    data["status"] = "cleanup_incomplete"
            # No group signal is sent after this reaping operation.
            pid, status, usage_result = os.wait4(process.pid, os.WNOHANG)
            if pid:
                process.returncode = os.waitstatus_to_exitcode(status)
                usage = usage_result
            elif data["cleanup_complete"]:
                data["cleanup_complete"] = False
                data["prior_status"] = data["status"]
                data["status"] = "cleanup_incomplete"
            data["child_returncode"] = process.returncode
            if data["status"] == "exited_group_empty":
                data["status"] = "success" if process.returncode == 0 else "child_failed"
                if process.returncode == -signal.SIGXCPU or (
                    process.returncode == -signal.SIGKILL and usage is not None
                    and usage.ru_utime + usage.ru_stime >= args.cpu_seconds - 0.05
                ):
                    data["status"] = "cpu_limit"
                    data["cpu_status_basis"] = "exit signal and child rusage; not a group CPU measurement"
        if usage is not None:
            data["child_cpu_seconds"] = usage.ru_utime + usage.ru_stime
            data["child_cpu_scope"] = "wait4 direct child rusage, including descendants it waited for"
            data["child_peak_rss_bytes"] = int(usage.ru_maxrss * (1 if sys.platform == "darwin" else 1024))
        data["runtime_seconds"] = time.monotonic() - started
        data["wall_overshoot_seconds"] = max(0, data["runtime_seconds"] - args.wall_seconds)
        for signum, handler in old_handlers.items():
            signal.signal(signum, handler)
        try:
            data["input_hashes_unchanged"] = all(
                digest(item["path"])["sha256"] == item["sha256"]
                for item in data["artifacts"]["inputs"]
            )
        except (OSError, ValueError):
            data["input_hashes_unchanged"] = False
        if not data["input_hashes_unchanged"]:
            data["prior_status"] = data["status"]
            data["status"] = "input_changed"
        write_receipt(receipt, data)
    return 0 if data["status"] == "success" else 1


if __name__ == "__main__":
    sys.exit(main())
