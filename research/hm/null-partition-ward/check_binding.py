"""Immutable input and exact eight-branch controls; never imports production."""
from pathlib import Path
import hashlib,json
from fractions import Fraction
ROOT=Path(__file__).resolve().parent
PINS={'PROOF.md': '42189fa11cb6c6165dc6678429b31b27c429bd87024fe9a7161209b06deb9a1c', 'branches.json': '335c9568efc9d15d0f94833e6d6635768724cab106b2e9e8ee5e83250e89cb9f', 'PROVENANCE.json': '6516755154125f088e994d372b61628955f5456a62528cce59f95d3cf3734305', 'dependencies/source-adjoint.md': 'c4c45e748e4b7c22aff75c6d05772ec35d3902c7210924dcfad618b2890e8cec', 'dependencies/current-curl.md': '2ba896e7243a1a7da41fe92dc963c4e4af27d485ad948733b791c69e94d37450', 'dependencies/hpl.md': '42139f79c0d0e901e6edd8386df174c0732ac040a033c7f002fa9fbc54c5ff98', 'dependencies/outer-weight.md': 'dbd691a2d547a51f2821da19461ba0a740a54495ac77d90cbf5b908a270b933f', 'dependencies/regular-prism.md': 'e5243ab12b64dbbe5b36067997f8389a894cf27da669dc55b3eb9c96c8fdaea6'}
for name,digest in PINS.items():
    if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
        raise RuntimeError('input pin mismatch: '+name)
branches=json.loads((ROOT/'branches.json').read_text())
expected=[]
for pair,other in [([0,1],[2,3]),([2,3],[0,1])]:
    a,b=pair
    for axis,current,edge,num in [(a,['L',b],'jk',1),(b,['L',a],'jk',-1),(b,['U',a],'ij',1),(a,['U',b],'ij',-1)]:
        expected.append(dict(pair=pair,scalar_pair=other,axis=axis,current=current,edge=edge,coefficient=[num,2]))
if branches!=expected: raise RuntimeError('eight branch contract mismatch')
# Gather exact raw-scalar/current coefficients by derivative axis, before HPL.
actual={d:{} for d in range(4)}
for e in branches:
    key=(tuple(e['scalar_pair']),e['edge'],tuple(e['current']))
    actual[e['axis']][key]=Fraction(*e['coefficient'])
for pair,other in [([0,1],[2,3]),([2,3],[0,1])]:
    a,b=pair; q=tuple(other)
    za={(q,'jk',('L',b)):Fraction(1,2),(q,'ij',('U',b)):Fraction(-1,2)}
    zb={(q,'jk',('L',a)):Fraction(-1,2),(q,'ij',('U',a)):Fraction(1,2)}
    if actual[a]!=za or actual[b]!=zb: raise RuntimeError('Z endpoint gathering mismatch')
print('PASS: immutable predecessor excerpts and exact eight-branch/Z binding; source meaning remains a written conditional proof')
