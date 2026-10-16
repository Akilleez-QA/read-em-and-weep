#!/usr/bin/env python3
"""Run only the producer's exact abstract controls, bounded in both modes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from run_formal import bounds

HERE=Path(__file__).resolve().parent
if __name__=='__main__':
    results=[]
    for optimized in(False,True):
        command=[sys.executable,'-B']+(['-O']if optimized else[])+['-m','unittest','discover','-s',str(HERE),'-p','test_compiler.py','-v']
        start=time.monotonic();p=subprocess.run(command,capture_output=True,timeout=60,preexec_fn=bounds)
        results.append({'optimized':optimized,'exit_code':p.returncode,'elapsed_seconds':round(time.monotonic()-start,6),'stdout':p.stdout.decode(),'stderr':p.stderr.decode(),'physical_source_evaluated':False})
        if p.returncode:break
    out={'schema':'sc01-producer-controls-v1','commands':results,'address_space_cap_bytes':512*1024*1024,'wall_timeout_seconds_per_command':60,'code_sha256':{f:hashlib.sha256((HERE/f).read_bytes()).hexdigest()for f in('compiler.py','test_compiler.py','run_controls.py')},'physical_source_evaluated':False,'execution_release':False}
    (HERE/'controls-receipt.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'normal_and_optimized_pass':len(results)==2 and all(r['exit_code']==0 for r in results),'tests_per_mode':13,'physical_source_evaluated':False}))
    if len(results)!=2 or any(r['exit_code']for r in results):raise SystemExit(1)
