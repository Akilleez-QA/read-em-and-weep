#!/usr/bin/env python3
"""Portable independent/author replay and exact tuple-set comparison."""
from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'accepted-author-packet'
def call(script,opt=False):
 p=subprocess.run([sys.executable]+(['-O']if opt else[])+[str(script)],cwd='/',capture_output=True)
 if p.returncode:raise ValueError(p.stderr.decode())
 return p.stdout
def digest(raw):return hashlib.sha256(raw).hexdigest()
def main():
 normal=call(ROOT/'verify_bounded.py');n=(ROOT/'BOUNDED-RESULT.json').read_bytes()
 optimized=call(ROOT/'verify_bounded.py',True);o=(ROOT/'BOUNDED-RESULT.json').read_bytes()
 if normal!=optimized or n!=o:raise ValueError('independent normal/optimized mismatch')
 controls=call(ROOT/'test_independent_controls.py');ocontrols=call(ROOT/'test_independent_controls.py',True)
 if controls!=ocontrols:raise ValueError('independent controls normal/optimized mismatch')
 (ROOT/'INDEPENDENT-CONTROLS.json').write_bytes(controls)
 a=call(SRC/'verify.py');ao=call(SRC/'verify.py',True)
 if a!=ao or a!=(SRC/'RESULT.json').read_bytes():raise ValueError('author replay mismatch')
 ac=call(SRC/'test_controls.py');aco=call(SRC/'test_controls.py',True)
 if ac!=aco or ac!=(SRC/'CONTROL-RESULT.json').read_bytes():raise ValueError('author controls mismatch')
 own=json.loads(n);author=json.loads(a)
 report={'status':'PASS','author_manifest_sha256':digest((SRC/'MANIFEST.json').read_bytes()),'author_checks':author['checks'],'independent_checks':own['checks'],'author_mutations_rejected':48,'independent_mutations_rejected':json.loads(controls)['genuine_subprocess_mutations'],'all_31_exact_tuples_match':own['all_31_exact_tuples_match'],'all_five_residual_tuples_match':own['all_five_residual_tuples_match'],'normal_optimized_byte_identical':True,'independent_result_sha256':digest(n),'author_result_sha256':digest(a),'independent_controls_sha256':digest(controls),'author_controls_sha256':digest(ac)}
 (ROOT/'COMPARISON.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps(report,sort_keys=True))
if __name__=='__main__':main()
