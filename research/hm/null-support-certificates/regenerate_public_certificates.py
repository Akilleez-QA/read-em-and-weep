"""Regenerate only finite-label/AST certificates; never run physical checkers."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parent

def run(name,output=None):
    result=subprocess.run([sys.executable,str(ROOT/name)],cwd=ROOT,check=True,capture_output=bool(output),text=True)
    if output:(ROOT/output).write_text(result.stdout)

def main():
    run('lower_selected_kernel_denominators.py','selected-full-owner-kernel-lowering.json')
    from preflight_selected_coefficient_support import PIN,COMPILER
    for name,expected in [('selected-full-owner-kernel-lowering.json',PIN),('lower_selected_kernel_denominators.py',COMPILER)]:
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=expected:raise RuntimeError('Public release binding changed: '+name)
    run('preflight_legal_mask_sector.py','legal-mask-sector-support.json')
    run('derive_legal_mask_gap_patterns.py','legal-mask-gap-patterns.json')
    run('preflight_primary_carrier_sector.py')
    run('preflight_permuted_standard_sector.py')
    run('lower_exceptional_carrier_sector.py')
    run('inventory_permuted_standard_slices.py')
    bridge=ROOT/'primary-carrier-full-domain-partition.json'
    doc=json.loads(bridge.read_text())
    doc['certificates_sha256']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in doc['certificates_sha256']}
    bridge.write_text(json.dumps(doc,sort_keys=True,indent=2)+'\n')
    print('Public certificates regenerated; physical execution remains disabled.')
if __name__=='__main__':main()
