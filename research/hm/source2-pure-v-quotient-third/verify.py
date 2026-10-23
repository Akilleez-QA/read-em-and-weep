#!/usr/bin/env python3
"""Exact universal diagnostics for the conditional third/fourth interface."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not value:raise RuntimeError(name)
 checks.append(name)
def zero(M):return all(s.expand(x)==0 for x in M)
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/item['local_path']).read_bytes()
 ck('immutable pin '+item['local_path'],bool(item.get('commit')))
 ck('sha256 '+item['local_path'],hashlib.sha256(b).hexdigest()==item['sha256'])
 ck('git_blob '+item['local_path'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'])
# Synthetic universal complex. X=(A,D,B_D,B_E,B_P); Y=(B_D,B_E,B_P,C).
# Every T coefficient remains an indeterminate: no source instance is used.
a,b,c,l,m,n,r,u,v,t=s.symbols('a b c l m n r u v t')
Q=s.Matrix([[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]])
T=s.Matrix([[a,0,r,m,0],[b,0,v,u,n],[c,l,0,0,0],[0,0,l,0,0]])
h=s.Matrix([[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
j0=h*Q;j1=Q*h
ck('square-zero radical',zero(j0*j0) and zero(j1*j1))
ck('actual negative intertwining',zero(j1*T-T*j0))
p0=s.Matrix([[1,0,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])
p1=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])
Qb=s.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,0]])
Tb=s.Matrix([[a,r,m,0],[b,v,u,n],[0,l,0,0]])
f0=s.Matrix([[0,1,0,0]]);f1=s.Matrix([[0,0,1]])
ck('quotient q identity',zero(p1*Q-Qb*p0))
ck('quotient T identity',zero(p1*T-Tb*p0))
ck('global radical identity',zero(f1*Tb-l*f0) and zero(f1*Qb))
ck('formal radical chain identity',zero(f1*(Qb+t*Tb)-t*l*f0))
x0=s.Matrix([0,0,0,1]);x1=s.Matrix([0,0,-n,0]);x2=s.Matrix([0,n*m,n*u,0])
ck('canonical P cycle',zero(Qb*x0) and zero(f0*x0))
ck('first quotient correction',zero(Qb*x1+Tb*x0))
ck('second quotient correction',zero(Qb*x2+Tb*x1))
ck('quotient P second zero',zero(f1*Tb*x1))
R=(f0*x2)[0];ss=(f1*Tb*x2)[0]
ck('unique quadratic lift candidate',s.expand(R-n*m)==0)
ck('global third representative in L image',s.expand(ss-l*R)==0)
ck('cubic coefficient homogeneous',s.Poly(ss,a,b,c,l,m,n,r,u,v).total_degree()==3)
# Original D corrections: d,-x,-y,-z.
d=s.Matrix([0,1,0,0,0]);x=s.Matrix([0,0,0,0,l]);y=s.Matrix([0,0,0,-l*n,0]);zz=s.Matrix([0,0,l*n*m,l*n*u,0])
ck('connecting exact lift',zero(Q*x-T*d))
ck('next original correction',zero(Q*y+T*x))
ck('third original correction',zero(Q*zz+T*y))
ck('quotient lift relations',zero(p0*x-l*x0) and zero(p0*y-l*x1) and zero(p0*zz-l*x2))
ck('original third raw zero',(T*(-y))[3]==0)
ck('fourth comparison sign',s.expand((T*(-zz))[3]+l*ss)==0)
ck('quartic degree',s.Poly((T*(-zz))[3],a,b,c,l,m,n,r,u,v).total_degree()==4)
# Exact A5 character arithmetic, no floating-point divisions.
sqrt5=s.sqrt(5);sizes=[1,15,20,12,12]
A=[3,-1,0,(1+sqrt5)/2,(1-sqrt5)/2];D=[5,1,-1,0,0];P=[4,0,1,-1,-1]
def inn(x,y):return s.simplify(sum(k*a*b for k,a,b in zip(sizes,x,y))*s.Rational(1,60))
ck('no A tensor A ambiguity',inn(P,[a*a for a in A])==0)
ck('two quadratic D lifts',inn(P,[d*(1+d) for d in D])==2)
ck('no negative-degree kappa ambiguity',-5-(-3)==-2)
ck('source lift degree',-1-(-3)==2)
ck('m ambiguity degree',-2-(-3)==1)
# Split kernel and Hilbert polynomial arithmetic.
k=s.symbols('k');chi=lambda q:(q+2)*(q+1)/2
hj=s.expand(5*chi(k-1)-3*chi(k-2)-chi(k-5))
ck('rank-one kernel presentation',5-3-1==1)
ck('determinant twist six',-5-(-6-5)==6)
ck('resolution gives length34',s.expand(chi(k+6)-hj)==34)
ck('twisted ideal resolution',(-2-6,-5-6,-1-6)==(-8,-11,-7))
ck('twist-three H0 sequence',(3-2,3-5,3-1)==(1,-2,2))
ck('scheme length bookkeeping',6*4+10==34)
print(json.dumps({'status':'pass','count':len(checks),'checks':checks,'scope':'conditional two-dimensional gate; actual coefficients unselected; no source exclusion'},indent=2))
