#!/usr/bin/env python3
"""Bound this source-free formal compiler/tests by 60s CPU and512MiB AS."""
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
import hashlib

HERE=Path(__file__).resolve().parent

def bounds():
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
    resource.setrlimit(resource.RLIMIT_CPU,(59,59))

if __name__=='__main__':
    start=time.monotonic()
    with(HERE/'compiled-template.json').open('wb')as output:
        result=subprocess.run([sys.executable,'-B',str(HERE/'compiler.py')],stdout=output,stderr=subprocess.PIPE,timeout=60,preexec_fn=bounds)
    raw=(HERE/'compiled-template.json').read_bytes()
    receipt={'exit_code':result.returncode,'elapsed_seconds':round(time.monotonic()-start,6),'peak_child_rss_bytes':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss*1024,'address_space_cap_bytes':512*1024*1024,'cpu_cap_seconds':59,'wall_timeout_seconds':60,'output_bytes':len(raw),'output_sha256':hashlib.sha256(raw).hexdigest(),'stderr':result.stderr.decode()[:8000],'physical_source_evaluated':False,'execution_release':False}
    (HERE/'formal-run-receipt.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps(receipt,sort_keys=True))
    if result.returncode:raise SystemExit(result.returncode)
