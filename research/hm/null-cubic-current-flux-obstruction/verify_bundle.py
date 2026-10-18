#!/usr/bin/env python3
"""Verify exact packet inventory, hashes, premise pins, and reproduced audit logs."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
PINS={
 'dependencies/RESULT.md':'2b07d868ec9c1fc5e38503623a8556ff7b3c71e3df76c3550385560602584db5',
 'dependencies/REVIEW.md':'ea986247cc484155f86fc2b016fc88477a85e74f7a7e094d2ff6680652e0afaf',
 'dependencies/author-RESULT.md':'dfcfd7882e546a423f4607920d1625d06eb71c2bcad33768d5033c70ddd980ad',
 'certificate.json':'bed968ee298ec44da1373f118450e38a53a3c3a0e681e7f71a7712e4e0ec7784',
}
def require(condition,message):
 if not condition:raise RuntimeError(message)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest={}
for line in (ROOT/'SHA256SUMS').read_text().splitlines():
 require(re.fullmatch(r'[0-9a-f]{64}  \./[^\n]+',line) is not None,'Malformed hash manifest')
 h,n=line.split('  ',1);n=n[2:]
 require(n not in manifest and not Path(n).is_absolute() and '..' not in Path(n).parts,'Unsafe or duplicated inventory entry')
 manifest[n]=h
all_files={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
require(all_files==set(manifest)|{'SHA256SUMS'},'Exact inventory mismatch')
require(not any(p.is_symlink() for p in ROOT.rglob('*')),'Symlink in packet')
for name,h in manifest.items():require(digest(ROOT/name)==h,'Hash mismatch: '+name)
for name,h in PINS.items():require(manifest.get(name)==h,'Premise pin mismatch: '+name)
source_pins=(ROOT/'SOURCE-PINS.md').read_text()
for h in PINS.values():require(h in source_pins,'Missing documentary pin')
for p in ROOT.rglob('*'):
 if p.is_file():
  data=p.read_bytes()
  require(re.search(rb'/(?:workspace|home|tmp)/',data) is None,'Machine-local path in packet: '+p.name)
  require(b'dream'+b'_notes' not in data and b'agent'+b'_notes' not in data,'Private note marker in packet')
logs=[json.loads((ROOT/n).read_text()) for n in ('audit-normal.json','audit-optimized.json','audit-other-cwd.json')]
require(logs[0]==logs[1]==logs[2],'Audit logs disagree')
expected={'verdict':'PASS','row_embedding_rank':144,'columns':96,'image_rank':94,'augmented_rank':95,'certificate_support':8,'certificate_pairing_N':'1','certificate_pairing_M2':'1/8'}
require(all(logs[0].get(k)==v for k,v in expected.items()),'Unexpected audit result')
with tempfile.TemporaryDirectory(prefix='cubic-flux-verify-') as other:
 for flags,cwd in (([],ROOT),(['-O'],ROOT),([],Path(other))):
  result=subprocess.run([sys.executable,'-B',*flags,str(ROOT/'audit_check.py')],cwd=cwd,text=True,capture_output=True,check=True)
  require(json.loads(result.stdout)==logs[0],'Reproduced audit differs from saved log')
require((ROOT/'author-normal.txt').read_bytes()==(ROOT/'author-optimized.txt').read_bytes(),'Author run logs disagree')
print(json.dumps({'verdict':'PASS','manifest_files':len(manifest),'exact_inventory':True,'all_hashes':True,'source_pins':True,'public_path_scan':'clean','reproduced_audits':['normal','optimized','other working directory'],'author_logs_identical':True},indent=2))
