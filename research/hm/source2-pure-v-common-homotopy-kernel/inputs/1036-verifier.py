#!/usr/bin/env python3
"""Whole-orbit symbolic ideal-power and conic-divisibility certificate."""
from model import *
from pathlib import Path
from itertools import permutations,combinations_with_replacement
import hashlib,json
root=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not value:raise RuntimeError(name)
 checks.append(name)
for item in json.loads((root/'INPUTS.json').read_text()):
 data=(root/item['local_path']).read_bytes()
 ck('sha256 '+item['local_path'],hashlib.sha256(data).hexdigest()==item['sha256'])
 ck('git_blob '+item['local_path'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
def detpoly(mat):
 out=s.Poly(0,p,q,t,extension=z)
 for perm in permutations(range(mat.rows)):
  term=s.Poly((-1)**sum(perm[i]>perm[j] for i in range(mat.rows) for j in range(i+1,mat.rows)),p,q,t,extension=z)
  for row,col in enumerate(perm):term*=s.Poly(mat[row,col],p,q,t,extension=z)
  out+=term
 return out.as_expr()
B=s.Matrix.hstack(*[Pi*cv(a*a*x**(2-i)*y**i,6) for i in range(3)])
N=s.Matrix([[(-1)**i*detpoly(B[[j for j in range(4) if j!=i],:]) for i in range(4)]])
ck('determinant cokernel map',all(s.expand(f)==0 for f in N*B))
F1=(N*L*R1).applyfunc(s.expand);F2=(N*L*R2).applyfunc(s.expand)
ck('homogeneous nonic rows',all(s.Poly(f,p,q,t).is_homogeneous and s.Poly(f,p,q,t).total_degree()==9 for F in [F1,F2] for f in F))
cP=Pi*cv(a**3,6)
I5=[s.expand(f.subs(p,1)) for f in cP]
I3=[s.expand(detpoly(L[:,[j for j in range(5) if j!=i]]).subs(p,1)) for i in range(5)]
expected5=[q*q+5*t**3+t+2*z,q*t*t-q,t**4-s.Rational(2,5)*z*t**3+s.Rational(2,5)*z*t-1]
expected3=[q*q+s.Rational(27,2)*t**5+s.Rational(27,10)*z*t**4+6*t**3-3*z*t*t-s.Rational(11,2)*t-s.Rational(57,10)*z,q*t**4-q,t**6+s.Rational(2,3)*z*t**5+t**4-t*t-s.Rational(2,3)*z*t-1]
def quotient_length(gb):
 leads=[poly.LM(order=gb.order).exponents for poly in gb.polys]
 bq=min(i for i,j in leads if j==0);bt=min(j for i,j in leads if i==0)
 return sum(not any(a<=i and b<=j for a,b in leads) for i in range(bq) for j in range(bt))
for label,gens,power,expected,expectedlen,powerlen,ratio,witnessmon,witness in [('C5',I5,3,expected5,6,36,s.Rational(-1,2),q**4*t,s.Rational(-512,9)),('C3',I3,2,expected3,10,30,s.Rational(1,2),q*q*t**3,s.Rational(6656,3)*z)]:
 gb=s.groebner(gens,q,t,extension=z)
 ck(label+' exact reduced base basis',list(gb)==expected)
 ck(label+' whole orbit affine length',quotient_length(gb)==expectedlen)
 powers=[s.prod(tup) for tup in combinations_with_replacement(list(gb),power)]
 gp=s.groebner(powers,q,t,extension=z)
 ck(label+' ideal-power length',quotient_length(gp)==powerlen)
 rems=[[s.expand(gp.reduce(s.expand(f.subs(p,1)))[1]) for f in F] for F in [F1,F2]]
 for i,(r1,r2) in enumerate(zip(*rems)):ck(label+' full remainder relation '+str(i),s.expand(r2-ratio*r1)==0)
 ck(label+' nonzero coefficient witness',s.simplify(s.Poly(rems[0][0],q,t).coeff_monomial(witnessmon)-witness)==0)
 ck(label+' rank-three line nonzero jet',any(s.expand(r1-r2)!=0 for r1,r2 in zip(*rems)))
# Formal square-family pullback, with no point selected.
u,v=s.symbols('u v')
f12=-2*u**12-s.Rational(44,5)*z*u**10*v**2+66*u**8*v**4+s.Rational(88,5)*z*u**6*v**6+66*u**4*v**8-s.Rational(44,5)*z*u**2*v**10-2*v**12
Vpol=[sum(vec[i]*x**(6-i)*y**i for i in range(7)) for vec in Pi.nullspace()]
wr=s.expand(s.Matrix([[s.diff(f.subs(y,1),x,k) for f in Vpol] for k in range(3)]).det())
wr=s.Poly(wr,x).homogenize(y).as_expr()
ck('Wronskian invariant normalization',s.expand(wr.subs({x:u,y:v})-f12)==0)
ck('square-factor zero-point symplectic normalization',s.expand(f12.subs({u:-v,v:u}, simultaneous=True)-f12)==0)
fs=[]
for F in [F1,F2]:
 fs.append([s.rem(s.Poly(s.expand(f.subs({p:1,q:2*v,t:v*v})),v,extension=z),s.Poly(f12.subs(u,1),v,extension=z)).as_expr() for f in F])
ck('R1 entire conic divisor',all(f==0 for f in fs[0]))
ck('R2 nonzero conic remainder witness',s.Poly(fs[1][0],v).coeff_monomial(v**10)==s.Rational(13539328,45))
lines=[s.Matrix([1,2]),s.Matrix([1,-2]),s.Matrix([1,0]),s.Matrix([1,-1])]
for i in range(4):
 for j in range(i+1,4):ck('distinct coefficient lines '+str(i)+','+str(j),s.Matrix.hstack(lines[i],lines[j]).det()!=0)
print(json.dumps(dict(status='pass',count=len(checks),checks=checks,jet_lines={'ell5':'[1:2]','ell3':'[1:-2]','ellDelta':'[1:0]','rank_three':'[1:-1]'},scope='universal coefficient-line placement; no actual gate coefficients selected'),indent=2))
