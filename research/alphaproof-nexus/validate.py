#!/usr/bin/env python3
"""Offline pin check; explicit opt-in, one-file Lean check in a prepared checkout.

Python 3.10+, standard library only. This is a resource guard, NOT a sandbox.
Never installs, fetches, invokes Lake, or executes an upstream helper script.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import stat
import subprocess
import sys
import tempfile


PACKAGE_DIR = Path(__file__).resolve().parent
REPOSITORY = "https://github.com/google-deepmind/alphaproof-nexus-results"
COMMIT = "0647711a71183c1ea492ad60860776617ce1ea88"
TOOLCHAIN = "leanprover/lean4:v4.27.0"
TARGET = "APNOutputs/AICollaborator/AlgebraicGeometry/hilbert_functions_5.lean"
DEPENDENCIES = {
    "formal_conjectures": "7862bf6a6976c26acb086b6b2cec12ad1d92ce5d",
    "mathlib": "a3a10db0e9d66acbebf76c5e6a135066525ac900",
    "plausible": "009dc1e6f2feb2c96c081537d80a0905b2c6498f",
    "LeanSearchClient": "5ce7f0a355f522a952a3d678d696bd563bb4fd28",
    "importGraph": "8f497d55985a189cea8020d9dc51260af1e41ad2",
    "proofwidgets": "c04225ee7c0585effbd933662b3151f01b600e40",
    "aesop": "cb837cc26236ada03c81837bebe0acd9c70ced7d",
    "Qq": "bd58c9efe2086d56ca361807014141a860ddbf8c",
    "batteries": "b25b36a7caf8e237e7d1e6121543078a06777c8a",
    "Cli": "55c37290ff6186e2e965d68cf853a57c0702db82",
}
FILES = {
    TARGET: "d654c3dbdb006712418b30e8c43d1de45d32ba1a5c7d514033e47066f7b2ef26",
    "lean-toolchain": "d55ca0039a5479db5b38919d005b2c427b89b3be4f0184a20f2f4eae931f5bdb",
    "lake-manifest.json": "d5f3544a12eb2b6ae6913524e16b0e62cad4ca279d0cfa89e4d4bd5c467bffd5",
}
MAX_OUTPUT = 4 * 1024 * 1024


class ValidationError(Exception):
    """A prerequisite failed; no success receipt may be issued."""


def expected_pins() -> dict:
    return {
        "schema_version": 1, "repository": REPOSITORY, "commit": COMMIT,
        "lean_toolchain": TOOLCHAIN, "dependencies": DEPENDENCIES.copy(),
        "files": FILES.copy(),
    }


def unique_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> dict:
    if path.stat().st_size > 65536:
        raise ValidationError(f"Oversized JSON file: {path}")
    try:
        result = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (ValueError, UnicodeError) as exc:
        raise ValidationError(f"Invalid JSON: {path}") from exc
    if not isinstance(result, dict):
        raise ValidationError(f"Expected a JSON object: {path}")
    return result


def canonical(path: Path) -> Path:
    """Require an existing canonical path: no hidden symlink traversal."""
    absolute = path.absolute()
    resolved = absolute.resolve(strict=True)
    if resolved != absolute:
        raise ValidationError(f"Use a canonical path without symlinks or '..': {path}")
    return resolved


def confined(root: Path, relative: str, *, directory: bool = False) -> Path:
    pure = PurePosixPath(relative)
    if (not relative or pure.is_absolute() or str(pure) != relative
            or ".." in pure.parts or "\\" in relative or "\x00" in relative):
        raise ValidationError(f"Unsafe relative path: {relative!r}")
    path = root
    for part in pure.parts:
        path = path / part
        if path.is_symlink():
            raise ValidationError(f"Symlink rejected: {path}")
    if not path.resolve(strict=True).is_relative_to(root):
        raise ValidationError(f"Path escapes checkout: {path}")
    mode = path.stat().st_mode
    if not (stat.S_ISDIR(mode) if directory else stat.S_ISREG(mode)):
        raise ValidationError(f"Expected a {'directory' if directory else 'regular file'}: {path}")
    return path


def check_pins(path: Path) -> dict:
    path = canonical(path)
    if not path.is_file():
        raise ValidationError("Pins must be a regular file")
    pins = read_json(path)
    if pins != expected_pins() or type(pins.get("schema_version")) is not int:
        raise ValidationError("pins.json differs from the reviewed release pins embedded in validate.py")
    return pins


def clean_environment() -> dict[str, str]:
    # No inherited LEAN_PATH, ELAN_*, LD_*, DYLD_*, GIT_* or Python variables.
    return {
        "PATH": os.defpath, "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
        "LEAN_NUM_THREADS": "1", "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull,
        "GIT_TERMINAL_PROMPT": "0", "GIT_NO_LAZY_FETCH": "1",
        "GIT_OPTIONAL_LOCKS": "0",
    }


def resource_guard(memory_mib: int):
    if os.name != "posix":
        raise ValidationError("--run requires POSIX resource limits and process groups")
    try:
        import resource
        address_limit = resource.RLIMIT_AS
    except (ImportError, AttributeError) as exc:
        raise ValidationError("POSIX address-space memory limit is unavailable") from exc

    def apply_limits():
        def lower(kind, requested):
            _, hard = resource.getrlimit(kind)
            limit = requested if hard == resource.RLIM_INFINITY else min(requested, hard)
            resource.setrlimit(kind, (limit, limit))
        lower(address_limit, memory_mib * 1024 * 1024)
        lower(resource.RLIMIT_FSIZE, MAX_OUTPUT * 2)
        lower(resource.RLIMIT_CORE, 0)

    return apply_limits


def run_process(argv: list[str], *, cwd: Path, env: dict[str, str],
                timeout: float, memory_mib: int) -> str:
    if not isinstance(argv, list) or not argv or not Path(argv[0]).is_absolute():
        raise ValidationError("Subprocess requires a list and an absolute executable path")
    if not math.isfinite(timeout) or timeout <= 0 or memory_mib <= 0:
        raise ValidationError("Invalid process resource limits")
    # Spool output rather than leaving a descendant holding a PIPE open.
    with tempfile.TemporaryFile() as output:
        with subprocess.Popen(
            argv, cwd=str(cwd), env=env, stdin=subprocess.DEVNULL,
            stdout=output, stderr=subprocess.STDOUT, shell=False,
            start_new_session=True, preexec_fn=resource_guard(memory_mib),
        ) as process:
            try:
                returncode = process.wait(timeout=timeout)
            except subprocess.TimeoutExpired as exc:
                raise ValidationError(f"Process timed out after {timeout:g} seconds") from exc
            finally:
                # Clean up descendants too, including after a successful leader exit.
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.wait()
        output.seek(0)
        raw = output.read(MAX_OUTPUT + 1)
    if len(raw) > MAX_OUTPUT:
        raise ValidationError("Process output exceeded the 4 MiB reporting limit")
    text = raw.decode("utf-8", errors="replace")
    if returncode != 0:
        raise ValidationError(f"Process exited {returncode}: {text[-12000:]}")
    return text


def native_executable(path: Path) -> Path:
    path = canonical(path)
    if not path.is_file() or not os.access(path, os.X_OK):
        raise ValidationError(f"Missing executable: {path}")
    with path.open("rb") as source:
        magic = source.read(4)
    if magic not in (b"\x7fELF", b"\xfe\xed\xfa\xce", b"\xce\xfa\xed\xfe",
                     b"\xfe\xed\xfa\xcf", b"\xcf\xfa\xed\xfe", b"\xca\xfe\xba\xbe",
                     b"\xbe\xba\xfe\xca"):
        raise ValidationError(f"Expected an installed native binary, not a wrapper script: {path}")
    return path


def git_read(git: Path, root: Path, args: list[str]) -> str:
    argv = [str(git), "--no-replace-objects", "--no-optional-locks",
            "-c", "core.fsmonitor=false", "-c", f"core.hooksPath={os.devnull}"]
    for protocol in ("", "file.", "http.", "https.", "ssh.", "git.", "ext."):
        argv += ["-c", f"protocol.{protocol}allow=never"]
    argv += ["-C", str(root), *args]
    return run_process(argv, cwd=root, env=clean_environment(), timeout=30, memory_mib=4096)


def git_blob_hash(path: Path) -> str:
    digest = hashlib.sha1(usedforsecurity=False)
    digest.update(f"blob {path.stat().st_size}\0".encode("ascii"))
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_checkout(root: Path, revision: str, git: Path) -> None:
    # A standalone checkout only; no external worktree metadata or submodules.
    confined(root, ".git", directory=True)
    if git_read(git, root, ["rev-parse", "--show-toplevel"]).strip() != str(root):
        raise ValidationError(f"Not the checkout root: {root}")
    if git_read(git, root, ["rev-parse", "--verify", "HEAD^{commit}"]).strip() != revision:
        raise ValidationError(f"Wrong HEAD: {root}; expected {revision}")
    tree = git_read(git, root, ["ls-tree", "-r", "-z", "--full-tree", "HEAD"])
    expected = {}
    for record in tree.split("\0"):
        if not record:
            continue
        metadata, relative = record.split("\t", 1)
        mode, kind, oid = metadata.split()
        if kind != "blob" or mode not in ("100644", "100755"):
            raise ValidationError(f"Symlink or submodule in tracked tree: {relative}")
        path = confined(root, relative)
        actual_mode = "100755" if path.stat().st_mode & 0o111 else "100644"
        if actual_mode != mode or git_blob_hash(path) != oid:
            raise ValidationError(f"Dirty tracked file: {path}")
        expected[relative] = (mode, oid, "0")
    if not expected:
        raise ValidationError(f"Empty tracked source tree: {root}")
    index = {}
    for record in git_read(git, root, ["ls-files", "--stage", "--full-name", "-z"]).split("\0"):
        if record:
            metadata, relative = record.split("\t", 1)
            if relative in index:
                raise ValidationError(f"Unmerged index entry: {relative}")
            index[relative] = tuple(metadata.split())
    if index != expected:
        raise ValidationError(f"Staged changes or unmerged index: {root}")


def check_sources(root: Path) -> dict:
    for relative, expected in FILES.items():
        path = confined(root, relative)
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValidationError(f"Pinned source digest mismatch: {relative}")
    if confined(root, "lean-toolchain").read_text().strip() != TOOLCHAIN:
        raise ValidationError("Wrong lean-toolchain")
    lock = read_json(confined(root, "lake-manifest.json"))
    if lock.get("packagesDir") != ".lake/packages" or lock.get("lakeDir") != ".lake":
        raise ValidationError("Unexpected dependency directory in lockfile")
    packages = lock.get("packages", [])
    if (not isinstance(packages, list) or len(packages) != len(DEPENDENCIES)
            or any(p.get("type") != "git" or p.get("subDir") is not None for p in packages)
            or {p.get("name"): p.get("rev") for p in packages} != DEPENDENCIES):
        raise ValidationError("Dependency revisions differ from the reviewed lockfile")
    return lock


def artifact_paths(root: Path) -> list[Path]:
    paths = []
    # This single source imports Mathlib only, never formal_conjectures.
    for name in ("mathlib", *(n for n in DEPENDENCIES if n not in ("mathlib", "formal_conjectures"))):
        relative = f".lake/packages/{name}/.lake/build/lib/lean"
        candidate = root / relative
        if not candidate.exists() and not candidate.is_symlink():
            continue  # Any genuinely required missing import fails the Lean check.
        directory = confined(root, relative, directory=True)
        for current, dirs, files in os.walk(directory, followlinks=False):
            for entry in dirs + files:
                item = Path(current) / entry
                if item.is_symlink():
                    raise ValidationError(f"Symlink in compiled import path: {item}")
        paths.append(directory)
    mathlib = confined(root, ".lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean")
    if mathlib.stat().st_size == 0:
        raise ValidationError("Empty Mathlib.olean; prepare trusted dependency artifacts first")
    return paths


def check_lean(lean: Path, *, cwd: Path, env: dict, memory_mib: int) -> tuple[Path, str, str]:
    if not lean.is_absolute() or lean.name != "lean" or lean.parent.name != "bin":
        raise ValidationError("--lean must name the absolute native TOOLCHAIN/bin/lean, not an elan shim")
    if lean.parent.parent.name not in ("leanprover--lean4---v4.27.0", "lean-4.27.0-linux",
                                        "lean-4.27.0-linux_aarch64", "lean-4.27.0-darwin",
                                        "lean-4.27.0-darwin_aarch64"):
        raise ValidationError("Unrecognized toolchain directory; use the installed Lean 4.27.0 directory")
    lean = native_executable(lean)
    prefix = lean.parent.parent
    confined(prefix, "lib/lean/Init.olean")
    version = run_process([str(lean), "--version"], cwd=cwd, env=env, timeout=10, memory_mib=memory_mib)
    if not re.search(r"\bLean \(version 4\.27\.0(?:,|\))", version):
        raise ValidationError(f"Compiler version mismatch: {version.strip()}")
    reported = run_process([str(lean), "--print-prefix"], cwd=cwd, env=env, timeout=10, memory_mib=memory_mib)
    if reported.strip() != str(prefix):
        raise ValidationError("Compiler prefix does not match the explicit toolchain directory")
    return lean, version.strip(), reported.strip()


def parse_axioms(output: str) -> list[str]:
    match = re.search(r"'?P5'?\s+depends on axioms:\s*\[([^]]*)\]", output)
    if not match:
        raise ValidationError("Lean did not produce the expected #print axioms P5 report")
    axioms = [name.strip() for name in match.group(1).split(",") if name.strip()]
    if not set(axioms) <= {"propext", "Classical.choice", "Quot.sound"}:
        raise ValidationError(f"Unexpected P5 axioms: {axioms}")
    return axioms


def run_validation(checkout: Path, lean: Path, timeout: float, memory_mib: int) -> dict:
    if not 1 <= timeout <= 3600 or not math.isfinite(timeout):
        raise ValidationError("--timeout must be between 1 and 3600 seconds")
    if not 512 <= memory_mib <= 32768:
        raise ValidationError("--memory-mib must be between 512 and 32768")
    resource_guard(memory_mib)  # Refuse unsupported platforms before any subprocess.
    root = canonical(checkout)
    if root.is_relative_to(PACKAGE_DIR) or PACKAGE_DIR.is_relative_to(root):
        raise ValidationError("Use a separate prepared checkout, outside this integration directory")
    git_location = shutil.which("git", path=os.defpath)
    if not git_location:
        raise ValidationError("An already-installed Git executable is required")
    git = native_executable(Path(git_location))
    verify_checkout(root, COMMIT, git)
    check_sources(root)
    dependencies = []
    for name, revision in DEPENDENCIES.items():
        directory = confined(root, f".lake/packages/{name}", directory=True)
        verify_checkout(directory, revision, git)
        dependencies.append((directory, revision))
    imports = artifact_paths(root)
    with tempfile.TemporaryDirectory(prefix="nexus-p5-check-") as temporary:
        work = Path(temporary).resolve()
        env = clean_environment()
        env.update(HOME=str(work), TMPDIR=str(work), LEAN_PATH=os.pathsep.join(map(str, imports)))
        compiler, compiler_version, compiler_prefix = check_lean(
            lean, cwd=work, env=env, memory_mib=memory_mib)
        source = work / "hilbert_functions_5.lean"
        source.write_bytes(confined(root, TARGET).read_bytes() + b"\n#print axioms P5\n")
        output = run_process([str(compiler), str(source)], cwd=work, env=env,
                             timeout=timeout, memory_mib=memory_mib)
        axioms = parse_axioms(output)
    # Catch tracked-source mutations during the check; never repair them silently.
    verify_checkout(root, COMMIT, git)
    for directory, revision in dependencies:
        verify_checkout(directory, revision, git)
    return {"local_compilation": "passed", "target": TARGET, "axioms": axioms,
            "lean_output": output, "upstream_ci": "not_checked_by_this_tool",
            "release_pins": expected_pins(), "checkout": str(root),
            "compiler": {"path": str(compiler), "observed_version": compiler_version,
                         "observed_prefix": compiler_prefix},
            "compiler_exit_code": 0, "import_paths": list(map(str, imports)),
            "resource_limits": {"proof_timeout_seconds": timeout, "memory_mib": memory_mib},
            "artifact_trust": "compiler and prebuilt dependency artifacts are user-trusted, not certified"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pins", type=Path, default=PACKAGE_DIR / "pins.json")
    parser.add_argument("--run", action="store_true", help="explicitly compile only P5 in a prepared checkout")
    parser.add_argument("--checkout", type=Path, help="separate, already prepared upstream checkout")
    parser.add_argument("--lean", type=Path, help="absolute native Lean 4.27.0 TOOLCHAIN/bin/lean")
    parser.add_argument("--timeout", type=float, default=300, help="compiler wall seconds, 1–3600 (default 300)")
    parser.add_argument("--memory-mib", type=int, default=4096, help="POSIX address-space MiB, 512–32768")
    args = parser.parse_args(argv)
    try:
        check_pins(args.pins)
        if not args.run:
            result = {"pins": "passed", "local_compilation": "not_run", "target": TARGET,
                      "checkout_checked": False, "dependencies_checked": False,
                      "upstream_ci": "not_checked_by_this_tool",
                      "next_step": "Only in a trusted, prepared isolated checkout: --run --checkout PATH --lean TOOLCHAIN/bin/lean",
                      "network_or_install_actions": "none"}
        else:
            if args.checkout is None or args.lean is None:
                raise ValidationError("--run requires both --checkout and --lean; no installation is attempted")
            result = run_validation(args.checkout, args.lean, args.timeout, args.memory_mib)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except (ValidationError, OSError, ValueError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "failed", "local_compilation": "not_certified", "error": str(exc)}, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
