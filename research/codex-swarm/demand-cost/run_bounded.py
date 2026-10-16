"""Replay producer and tests under inherited per-process resource limits."""
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def limits():
    resource.setrlimit(resource.RLIMIT_AS, (256*1024**2,256*1024**2))
    resource.setrlimit(resource.RLIMIT_CPU, (15,15))


def main():
    commands = [
        [sys.executable,'-B',str(HERE/'preflight.py')],
        [sys.executable,'-B','-m','unittest','discover','-s',str(HERE),'-p','test_producer.py','-v'],
        [sys.executable,'-O','-B','-m','unittest','discover','-s',str(HERE),'-p','test_producer.py','-v'],
    ]
    runs = []
    for i,cmd in enumerate(commands):
        start = time.monotonic()
        proc = subprocess.run(cmd,cwd=REPO,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                              timeout=25,preexec_fn=limits)
        elapsed = time.monotonic()-start
        if proc.returncode or len(proc.stdout)+len(proc.stderr)>2_000_000:
            raise RuntimeError('bounded replay failed: '+proc.stderr.decode(errors='replace')[:2000])
        if i == 0 and proc.stdout != (HERE/'request-report.json').read_bytes():
            raise RuntimeError('report is not byte reproducible')
        if i:
            (HERE/('tests-optimized.log' if i == 2 else 'tests-normal.log')).write_bytes(proc.stderr)
        runs.append({'command':cmd, 'exit_status':proc.returncode,'wall_seconds':round(elapsed,6),
                     'stdout_sha256':hashlib.sha256(proc.stdout).hexdigest(),
                     'stderr_sha256':hashlib.sha256(proc.stderr).hexdigest()})
    receipt = {'schema':'co01-bounded-replay-v1','runs':runs,
        'limits':{'per_process_address_space_bytes':256*1024**2,'per_process_cpu_seconds':15,
                  'per_command_wall_seconds':25},
        'child_maxrss_kib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        'rss_metric':'Linux wait4 maximum resident size of an individual terminated child; not aggregate live RSS',
        'physical_source_evaluated':False,'execution_release':False}
    (HERE/'run-receipt.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps(receipt,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
