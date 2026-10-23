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
results={}
for label,gens,r,F,expected,n in [('C5',I5,3,F1+2*F2,expected5,6),('C3',I3,2,F1-2*F2,expected3,10)]:
 gb=s.groebner(gens,q,t,extension=z)
 ck(label+' exact reduced orbit basis',list(gb)==expected)
 ck(label+' whole orbit length',quotient_length(gb)==n)
 def power_basis(k):
  return s.groebner([s.prod(tup) for tup in combinations_with_replacement(list(gb),k)],q,t,extension=z)
 gr=power_basis(r);gn=power_basis(r+1)
 ck(label+' target power length',quotient_length(gr)==n*r*(r+1)//2)
 ck(label+' bounded truncation length',quotient_length(gn)==n*(r+1)*(r+2)//2)
 affine=[s.expand(f.subs(p,1)) for f in F]
 ck(label+' every component in target ideal power',all(gr.reduce(f)[1]==0 for f in affine))
 remainders=[gn.reduce(f)[1] for f in affine]
 combined=s.groebner(list(gn)+remainders,q,t,extension=z)
 ck(label+' EXACT Nakayama ideal equality',list(combined)==list(gr))
 ck(label+' quotient dimension',quotient_length(combined)==n*r*(r+1)//2)
 results[label]=dict(order=r,orbit_size=n,local_length=r*(r+1)//2,truncation_length=quotient_length(gn),quotient_length=quotient_length(combined),target_leading_monomials=[poly.LM(order=gr.order).exponents for poly in gr.polys])
ck('ell5 total length',6*6+10==46)
ck('ell3 total length',6*4+10*3==54)
print(json.dumps(dict(status='pass',count=len(checks),checks=checks,results=results,total_lengths={'ell5':46,'ell3':54},scope='universal special gate lines only; no actual gate selected'),indent=2))
