#!/usr/bin/env python3
"""Universal certificates only; no actual source instance is constructed."""
import hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
    if not condition: raise RuntimeError(name)
    checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/item['local_path']).read_bytes()
    check(item['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==item['sha256'])
    check(item['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'])
# All formal quadratic monomials, not any evaluated direction.
x,y=s.symbols('x y')
quad=[x*x,x*y,y*y]; quart=[x**4,x**3*y,x*x*y*y,x*y**3,y**4]
M=s.Matrix([[s.Poly(a*b,x,y).coeff_monomial(v) for a in quad for b in quad] for v in quart])
check('complete multiplication has rank five',M.rank()==5)
check('complete multiplication kernel has dimension four',len(M.nullspace())==4)
check('displayed five monomial products span',M[:,[0,1,2,5,8]].det()==1)
mu=s.symbols('mu',nonzero=True)
# Coordinates below are solely the abstract exact sequence (6): K plus I2.
H=s.zeros(5,33); H[:,28:33]=mu*s.eye(5)
R=s.zeros(33,5); R[28:33,:]=s.eye(5)/mu
P=R*H; K=s.eye(33)-P
check('formal section identity',H*R==s.eye(5))
check('canonical projector idempotent',P*P==P)
check('complement projector idempotent',K*K==K)
check('orthogonal projectors',P*K==s.zeros(33) and K*P==s.zeros(33))
check('homotopy kills complement',H*K==s.zeros(5,33))
check('projector fixes marked quartic',P*R==R)
check('projector independent of scalar',P.diff(mu)==s.zeros(33))
check('projector image dimension',P.rank()==5)
check('projector kernel dimension',33-P.rank()==28)
check('kernel homotopy dimension',37-9==28)
# Characters use ordered irreps A,V,P,D; direct sums, not embeddings.
dim=s.Matrix([3,3,4,5]); N2=s.Matrix([1,2,3,4]); N4=s.Matrix([0,2,4,3])
imQ=s.Matrix([0,2,3,3]); imh=s.Matrix([0,0,1,1]); kerh=N4-imh; D=s.Matrix([0,0,0,1])
check('source dimension and unique A',int(dim.dot(N2))==41 and N2[0]==1)
check('target and homotopy dimensions',int(dim.dot(N4))==37 and int(dim.dot(imh))==9)
check('image Q dimension',int(dim.dot(imQ))==33)
check('complement character equality',imQ-kerh==D)
check('kernel character dimension',int(dim.dot(kerh))==28)
check('remaining D multiplicity exactly two',kerh[3]==2)
print(json.dumps({'status':'PASS','checks':len(checks),'passed':checks,'scope':'Universal multiplication and exact-sequence normal forms; actual-map premises are proved in the text from authenticated pins.'},indent=2))
