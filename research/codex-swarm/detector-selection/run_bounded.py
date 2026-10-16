#!/usr/bin/env python3
"""Enforce process-group RSS, wall and output bounds for the constant runner."""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
LIMIT_RSS=512*1024*1024
LIMIT_WALL=59.0
LIMIT_OUTPUT=2_000_000


def group_rss(group):
    total=0
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():continue
        try:
            stat=(path/'stat').read_text()
            tail=stat[stat.rfind(')')+2:].split()
            if int(tail[2])!=group:continue
            for line in(path/'status').read_text().splitlines():
                if line.startswith('VmRSS:'):total+=int(line.split()[1])*1024;break
        except(FileNotFoundError,ProcessLookupError,PermissionError):continue
    return total


def main():
    target=HERE/'selection.json';start=time.monotonic();peak=0;failure=None
    with target.open('wb')as output:
        child=subprocess.Popen([sys.executable,'-B',str(HERE/'select_detectors.py')],stdout=output,stderr=subprocess.PIPE,start_new_session=True)
        while child.poll()is None:
            elapsed=time.monotonic()-start;rss=group_rss(child.pid);peak=max(peak,rss)
            if elapsed>LIMIT_WALL:failure='wall cap'
            elif rss>LIMIT_RSS:failure='aggregate process-group RSS cap'
            elif target.stat().st_size>LIMIT_OUTPUT:failure='output cap'
            if failure:
                os.killpg(child.pid,signal.SIGKILL);break
            time.sleep(0.02)
        _,stderr=child.communicate()
    # A child can exit between watchdog samples; recheck final wall/output.
    if failure is None and time.monotonic()-start>LIMIT_WALL:failure='final wall cap'
    if failure is None and target.stat().st_size>LIMIT_OUTPUT:failure='final output cap'
    status='success'if child.returncode==0 and failure is None else'failed'
    receipt={'status':status,'exit_code':child.returncode,'failure':failure,'elapsed_seconds':round(time.monotonic()-start,6),'peak_sampled_group_rss_bytes':peak,'rss_sampling_seconds':0.02,'rss_cap_bytes':LIMIT_RSS,'wall_cap_seconds':LIMIT_WALL,'output_bytes':target.stat().st_size,'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'stderr':stderr.decode(errors='replace')[:8000],'physical_source_evaluated':False,'obstruction':'undecided','code_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in(HERE/'extract_constants.js',HERE/'select_detectors.py',Path(__file__))}}
    encoded=json.dumps(receipt,indent=2,sort_keys=True)+'\n'
    (HERE/'run-receipt.json').write_text(encoded);sys.stdout.write(encoded)
    if status!='success':raise SystemExit(2)

if __name__=='__main__':main()
