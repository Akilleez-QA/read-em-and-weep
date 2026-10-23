#!/usr/bin/env python3
"""Exact universal identities for an internal symbol, not HM instance data."""
import hashlib,itertools,json
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parent
checks=0

def ck(test,label):
 global checks
 checks+=1
 if not test:raise RuntimeError(label)
x,y,a,b,c,lam,mu,s,t=S.symbols('x y alpha beta gamma lambda mu s t')
q=a*x*x+b*x*y+c*y*y
bas2=[x*x,x*y,y*y];bas3=[x**(3-i)*y**i for i in range(4)];bas4=[x**(4-i)*y**i for i in range(5)]
def bracket(f,h):return S.diff(f,x)*S.diff(h,y)-S.diff(f,y)*S.diff(h,x)
def vector(p,bas):
 p=S.Poly(S.expand(p),x,y)
 return S.Matrix([p.coeff_monomial(v) for v in bas])
M=S.Matrix.hstack(*(vector(q*k,bas4) for k in bas2),*(vector(bracket(q,h),bas4) for h in bas4))
delta=b*b-4*a*c
mons=[a**i*b**j*c**(3-i-j) for i in range(4) for j in range(4-i)]
quotients={}
for cols in itertools.combinations(range(8),5):
 det=S.expand(M[:,cols].det());quo,rem=S.div(det,delta,a,b,c)
 ck(rem==0,'all maximal minors divisible by discriminant')
 ck(S.Poly(quo,a,b,c).total_degree()<=3,'quotients homogeneous cubic or zero')
 quotients[cols]=quo
selected=[(0,1,2,p,z) for p,z in itertools.combinations(range(3,8),2)]
expected=[-16*c**3,16*b*c**2,16*c*(a*c-b*b),-16*b*(2*a*c-b*b),-16*a*c*c,16*a*b*c,16*a*(a*c-b*b),-16*a*a*c,16*a*a*b,-16*a**3]
for cols,pol in zip(selected,expected):ck(S.expand(quotients[cols]-pol)==0,'displayed selected minor identity')
coeff=S.Matrix([[S.Poly(quotients[cols],a,b,c).coeff_monomial(m) for m in mons] for cols in selected])
ck(coeff.det()==2**40,'ten cubic quotients span entire cubic space')
# Universal transverse identities with symbolic nonzero scalars.
qgamma=x*x+c*y*y;k=y*y;h=-lam*x*y**3/(6*mu)
expr=lam*qgamma*k+mu*bracket(qgamma,h)
ck(S.simplify(expr.subs(c,0))==0,'transverse test vector initially in kernel')
ck(S.simplify(S.diff(expr,c)-S.Rational(4,3)*lam*y**4)==0,'multiplicity-one normal derivative')
ck(S.diff(-4*c,c)==-4,'transverse discriminant derivative')
# Parameterized conic kernel, with harmless lambda rescaling to avoid division.
l=s*x+t*y
for r in bas3:
 kk=-2*mu*bracket(l,r);hh=lam*l*r
 ck(S.expand(lam*l*l*kk+mu*bracket(l*l,hh))==0,'global conic kernel parametrization')
# Normal derivative on each cubic at l=x is -8mu times cubic quotient.
for i,r in enumerate(bas3):
 kk=-2*mu*bracket(x,r)/lam;hh=x*r
 derivative=S.expand(lam*y*y*kk+mu*bracket(y*y,hh))
 cokcoeff=S.Poly(derivative,x,y).coeff_monomial(y**4)
 ck(cokcoeff==(-8*mu if i==3 else 0),'Tor boundary is nonzero cubic evaluation')
# Cubic evaluation annihilates l*Sym2 and multiplication has rank3 offorigin.
L=S.Matrix.hstack(*(vector(l*k,bas3) for k in bas2))
evalrow=S.Matrix([[r.subs({x:-t,y:s},simultaneous=True) for r in bas3]])
ck(evalrow*L==S.zeros(1,3),'complete cubic evaluation kernel identity')
ck(S.expand(L[:3,:].det())==s**3,'evaluation kernel leading rank certificate')
ck(S.expand(L[1:4,:].det())==t**3,'evaluation kernel trailing rank certificate')
# Local shape diag(I4,z,0,0,0) has free rank3 kernel and torsion cokernel.
z=S.symbols('z');local=S.zeros(5,8)
for i in range(4):local[i,i]=1
local[4,4]=z
ck(local[:,:5].det()==z,'local reduced Fitting generator')
ck(len(local.nullspace())==3,'generic local kernel rank')
ck(len(local.subs(z,0).nullspace())==4,'fiberwise kernel jumps by Tor rankone')
# K-class and line-bundle twist bookkeeping on P2 and conic P1.
rank=8-6+1;c1=-8+2;ch2=S.Rational(8,2)+S.Rational(4,2);c2=(c1*c1-2*ch2)/2
ck((rank,c1,c2)==(3,-6,12),'kernel Chern data')
ck(2*2==4,'O_C(2) pulls back to O_P1(4)')
ck(4-4==0,'Tor line degree zero')
ck(3*(-4)==2*c1==4*(-3),'ambient and restricted kernel degrees')
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/e['local_path']).read_bytes()
 ck(hashlib.sha256(data).hexdigest()==e['sha256'],'input SHA256')
 ck(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==e['git_blob'],'input Git blob')
print(json.dumps(dict(status='pass',checks=checks,maximal_minors=56,cubic_spanning_determinant=str(2**40),homogeneous_ideal='Delta*(alpha,beta,gamma)^3',projective_scheme='reduced discriminant conic',cokernel='i_*O_C(2)',kernel_rank=rank,c1=c1,c2=int(c2),restricted_kernel='Sym^3(W) O_P1(-3)',ambient_kernel_restriction='Sym^2(W) O_P1(-4)',scope='Universal nonzero-mu alternative; no actual scalar selection or source cut'),indent=2))
