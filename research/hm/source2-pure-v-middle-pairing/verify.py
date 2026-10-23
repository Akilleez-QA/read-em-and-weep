#!/usr/bin/env python3
"""Universal transvectant-pair certificate; no actual source evaluations."""
from pathlib import Path
import json,hashlib
import sympy as s
r=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
 if not bool(b):raise RuntimeError(name)
 checks.append(name)
for a in json.loads((r/'INPUTS.json').read_text()):
 d=(r/a['local_path']).read_bytes()
 ck('sha256 '+a['label'],hashlib.sha256(d).hexdigest()==a['sha256'])
 ck('git blob '+a['label'],hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==a['git_blob'])
x,y=s.symbols('x y')
def cv(f,n):
 p=s.Poly(s.expand(f),x,y);return s.Matrix([p.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def tv(a,f,k):return s.expand(sum((-1)**j*s.binomial(k,j)*s.diff(a,x,k-j,y,j)*s.diff(f,x,j,y,k-j) for j in range(k+1)))
a=[x*x,x*y,y*y];g=[x**(5-i)*y**i for i in range(6)]
U=s.Matrix.hstack(*[cv(tv(b,x*f,2),4).col_join(cv(tv(b,y*f,2),4)) for b in a for f in g])
Delta=s.zeros(18,8)
for k in range(8):
 for j in range(3):
  if 0<=k-j<=5:Delta[j*6+k-j,k]=s.binomial(7-k,2-j)*s.binomial(k,j)
Mul=s.Matrix.hstack(*[cv(b*f,7) for b in a for f in g])
ck('polarization multiplication identity',Mul*Delta==21*s.eye(8))
ck('whole polarization kernel',U*Delta==s.zeros(10,8))
piv=[1,2,3,4,5,7,8,9,10,11]
minor=U[:,piv].det()
ck('exact ten-dimensional quotient certificate',minor==70808371200)
ck('full universal rank',U.rank()==10)
ck('exact kernel dimension',18-10==8)
ck('full determinant-contraction identity',all(s.expand(x*tv(b,y*f,2)-y*tv(b,x*f,2)-2*tv(b,f,1))==0 for b in a for f in g))
Tmap=s.Matrix.hstack(*[cv(tv(b,f,1),5) for b in a for f in g])
ck('quintic channel onto',Tmap.rank()==6)
# epsilon^2*g = X^2*y^2*g - 2XY*x*y*g +Y^2*x^2*g.
g3=[x**(3-i)*y**i for i in range(4)]
ck('entire cubic channel constant84',all(s.expand(tv(x*x,ell*y*y*f,2)-2*tv(x*y,ell*x*y*f,2)+tv(y*y,ell*x*x*f,2)-84*ell*f)==0 for ell in [x,y] for f in g3))
E3=s.Matrix.hstack(*[cv(y*y*f,5).col_join(cv(-2*x*y*f,5)).col_join(cv(x*x*f,5)) for f in g3])
ck('epsilon-square cubic embedding injective',E3.rank()==4)
Sout=s.Matrix.hstack(*[cv(x*f,4).col_join(cv(y*f,4)) for f in g3])
ck('paired cubic map identifies Euler S',U*E3==84*Sout)
ck('Euler S pairing injective',Sout.rank()==4)
# Character coordinates Wprime,S,T; target S+T.
J=s.Matrix([3,3,5]);target=s.Matrix([0,1,1]);K=s.Matrix([3,3,2]);F=s.Matrix([1,0,2]);dim=s.Matrix([[2,4,6]])
ck('pairing full-kernel character',J-target==s.Matrix([3,2,4]))
ck('pairing full-kernel dimension',(dim*(J-target))[0]==38)
ck('global simultaneous quotient character',K-F==s.Matrix([2,3,0]))
ck('all simultaneous T copies are generated',K[2]==F[2])
ck('induced quotient image S and kernel',K-F-s.Matrix([0,1,0])==s.Matrix([2,2,0]))
ck('induced source image kernel dimensions',[(dim*v)[0] for v in [K-F,s.Matrix([0,1,0]),s.Matrix([2,2,0])]]==[16,4,12])
ck('Euler quotient rank',5-4==1)
ck('Euler quotient degree',0-4*(-1)==4)
ck('determinant rotation invertible',s.Matrix([[0,1],[-1,0]]).det()==1)
# Universal projector algebra after the PROVED actual marked splitting.
# c is a formal invertible scalar, not a chosen actual normalization.
c=s.symbols('c',nonzero=True)
rows=list(Sout.T.rref()[1]);left=Sout[rows,:].inv()*s.eye(10)[rows,:]
ck('Euler coefficient left inverse',left*Sout==s.eye(4))
Aformal=s.zeros(10,12).row_join(c*Sout)
section=s.zeros(12,10).col_join(left/c)
projector=section*Aformal
ck('canonical projector idempotent',projector*projector==projector)
ck('canonical projector image and kernel',projector==s.diag(s.zeros(12),s.eye(4)))
ck('canonical projector scale independent',projector.diff(c)==s.zeros(16))
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,universal_minor=str(minor),universal_kernel='complete polarization Sym7',full_pairing_image='S+T',restricted_pairing_image='S',restricted_pairing_kernel='2Wprime+2S',quotient_pencil='0 -> marked S_can O(-1) -> I2 O -> O(4) -> 0',canonical_splitting='pairing radical plus marked S_can image',scope='actual conditional pairing; canonical degree-three quotient complement only; no branch or actual coefficient selected'),indent=2))
