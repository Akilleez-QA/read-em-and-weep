"""Hard-bounded artificial JC HPL controls only; no actual source descriptions."""
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
import unittest
HERE=Path(__file__).resolve().parent
LIMIT=512*1024*1024

def child():
    resource.setrlimit(resource.RLIMIT_AS,(LIMIT,LIMIT));resource.setrlimit(resource.RLIMIT_CPU,(59,59))
    start=time.monotonic();suite=unittest.defaultTestLoader.discover(str(HERE),pattern='test_lift.py')
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({'success':result.wasSuccessful(),'tests':result.testsRun,'seconds':time.monotonic()-start,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'optimized':not __debug__,
        'actual_source_descriptions_constructed':False,'actual_fibers_enumerated':False,'physical_source_evaluated':False}))
    return 0 if result.wasSuccessful()else 1

def main():
    if '--child'in sys.argv:return child()
    receipt={'schema':'full-lift-domain-controls-v1','hard_address_space_bytes':LIMIT,
        'hard_cpu_seconds':59,'parent_wall_timeout_seconds':60,'physical_source_evaluated':False,'runs':[]}
    for flags in((),('-O',)):
        command=[sys.executable,'-B',*flags,str(Path(__file__).resolve()),'--child'];start=time.monotonic()
        out=subprocess.run(command,cwd=HERE,text=True,capture_output=True,timeout=60);elapsed=time.monotonic()-start
        if elapsed>=60:raise RuntimeError('wall deadline exceeded')
        if out.returncode:raise RuntimeError(out.stdout+out.stderr)
        run=json.loads(out.stdout);run['parent_elapsed_seconds']=elapsed
        run['command']=['python','-B',*flags,'run_controls.py','--child'];receipt['runs'].append(run)
        (HERE/('controls-optimized.log'if flags else'controls-normal.log')).write_text(out.stderr)
    (HERE/'controls-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2));return 0

if __name__=='__main__':raise SystemExit(main())
