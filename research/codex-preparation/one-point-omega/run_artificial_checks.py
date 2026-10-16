"""Replay artificial/static controls only; never dispatch the physical body."""
from pathlib import Path
import hashlib
import json
import os
import re
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def frozen():
    paths = [HERE/n for n in ('bounded_exact.py', 'prepare_omega.py', 'test_artificial.py',
                              'run_artificial_checks.py', 'spec.json', 'source-pins.json')]
    paths += sorted((HERE/'sources').glob('*'))
    return {str(p.relative_to(HERE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def limits():
    resource.setrlimit(resource.RLIMIT_AS, (268435456, 268435456))
    resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
    resource.setrlimit(resource.RLIMIT_FSIZE, (65536, 65536))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def main():
    resource.setrlimit(resource.RLIMIT_AS, (268435456, 268435456))
    resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    before = frozen()
    receipt = dict(schema='one-point-omega-artificial-controls-v1', status='RUNNING',
                   limits_per_child=dict(address_space_bytes=268435456, CPU_seconds=15, wall_seconds=20),
                   parent_limits=dict(address_space_bytes=268435456, CPU_seconds=15),
                   max_simultaneous_processes=2,
                   workers_launched=0, actual_source_evaluated=False,
                   actual_point_or_denominator_values_evaluated=False,
                   source_metadata_and_hashes_only=True, execution_release=False,
                   before=before, runs=[])
    failed = False
    for optimized in (False, True):
        command = [sys.executable, '-I', '-B']+(['-O'] if optimized else [])+[str(HERE/'test_artificial.py'), '-v']
        start = time.monotonic()
        try:
            done = subprocess.run(command, timeout=20, preexec_fn=limits, capture_output=True,
                                  env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=''))
            raw = done.stdout+done.stderr
            code = done.returncode
        except subprocess.TimeoutExpired as exc:
            raw = (exc.stdout or b'')+(exc.stderr or b'')+b'\nWALL TIMEOUT\n'
            code = 124
        if len(raw) > 65536:
            raise RuntimeError('bounded control output exceeded cap')
        name = 'controls-optimized.log' if optimized else 'controls-normal.log'
        (HERE/name).write_bytes(raw)
        counts = re.findall(rb'Ran (\d+) tests?', raw)
        passed = code == 0 and counts == [b'13'] and frozen() == before
        receipt['runs'].append(dict(optimized=optimized, returncode=code, tests=13 if counts == [b'13'] else None,
                                    pass_=passed, seconds=round(time.monotonic()-start, 4),
                                    log=name, log_sha256=hashlib.sha256(raw).hexdigest()))
        failed |= not passed
        if failed:
            break
    receipt['after'] = frozen()
    receipt['status'] = 'FAILED' if failed else '13 artificial/static controls PASS per mode'
    (HERE/'controls-receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(receipt['status'])
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
