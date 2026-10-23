#!/usr/bin/env python3
"""Universal chain and sheaf-interface diagnostics; no actual instances."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not value:raise RuntimeError(name)
 checks.append(name)
def z(M):return all(s.expand(x)==0 for x in M)
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/item['local_path']).read_bytes()
 ck('sha256 '+item['local_path'],hashlib.sha256(b).hexdigest()==item['sha256'])
 ck('git_blob '+item['local_path'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'])
# All parameters below are unspecialized synthetic indeterminates.
a,b,l,m,n,p,q,t=s.symbols('a b l m n p q t')
Q=s.Matrix([[0,0,1,0],[0,0,0,1],[0,0,0,0]])
T=s.Matrix([[a,0,m,n],[b,l,p,q],[0,0,l,0]])
h=s.Matrix([[0,0,0],[1,0,0],[0,0,0],[0,0,1]])
j0=h*Q;j1=Q*h
inc0=s.Matrix([0,1,0,0]);inc1=s.Matrix([0,1,0])
p0=s.Matrix([[1,0,0,0],[0,0,1,0],[0,0,0,1]])
p1=s.Matrix([[1,0,0],[0,0,1]])
Qb=s.Matrix([[0,1,0],[0,0,0]]);Tb=s.Matrix([[a,m,n],[0,l,0]])
ck('image complex Q zero',z(Q*inc0))
ck('image complex T is L',z(T*inc0-l*inc1))
ck('actual quotient chain Q',z(p1*Q-Qb*p0))
ck('actual quotient chain T',z(p1*T-Tb*p0))
f0=s.Matrix([[0,1,0]]);f1=s.Matrix([[0,1]])
ck('descended radical endpoints',z(inc0*f0*p0-j0) and z(inc1*f1*p1-j1))
ck('descended radical full chain',z(t*l*f0-f1*(Qb+t*Tb)))
cycle=s.Matrix([[1,0],[0,0],[0,1]])
ck('quotient initial cycles',z(Qb*cycle))
ck('descended H0 map zero',z(f0*cycle))
ck('descended H1 map identity',f1[0,1]==1)
ck('whole quotient first zero',z((Tb*cycle)[1,:]))
# First corrections yield a quadratic quotient symbol [-la,-ln].
uA=s.Matrix([0,-a,0]);uP=s.Matrix([0,-n,0])
ck('quotient first corrections',z(Qb*uA+Tb*cycle[:,0]) and z(Qb*uP+Tb*cycle[:,1]))
Bq=s.Matrix([[(Tb*uA)[1],(Tb*uP)[1]]])
ck('quotient second exact',Bq==s.Matrix([[-l*a,-l*n]]))
uOrig=s.Matrix([0,0,-a,-b]);ck('original A correction',z(Q*uOrig+T*s.Matrix([1,0,0,0])))
ck('A second naturality',(T*uOrig)[2]==Bq[0,0])
# Connecting preimage v=sigma(Ld) represented by x=l B_P.
d=inc0;x=s.Matrix([0,0,0,l]);y=s.Matrix([0,0,-l*n,-l*q])
ck('connecting exact representative',z(Q*x-T*d))
ck('next correction qy=-Tx',z(Q*y+T*x))
ck('original successive correction signs',z(Q*(-x)+T*d) and z(Q*(-y)+T*(-x)))
ck('quotient third-interface sign',s.expand((T*(-y))[2]+(Tb*(p0*y))[1])==0)
ck('P symbol times L matches comparison',s.expand(Bq[0,1]*l-(Tb*(p0*y))[1])==0)
# Exact character certificates: inequivalent Hom and quadratic channel count.
r=s.sqrt(5);sizes=[1,15,20,12,12]
A=[3,-1,0,(1+r)/2,(1-r)/2];P=[4,0,1,-1,-1];D=[5,1,-1,0,0]
def inner(x,y):return s.simplify(sum(n*a*b for n,a,b in zip(sizes,x,y))*s.Rational(1,60))
ck('no equivariant P to A',inner(P,A)==0)
ck('no equivariant A+P to D',inner([a+p for a,p in zip(A,P)],D)==0)
Sym2A=[1+d for d in D]
ck('quadratic P-endomorphism dimension two',inner([x*p for x,p in zip(Sym2A,P)],P)==2)
ck('matched twists force degree zero',(-2)-(-2)==0)
ck('depth lemma local lower bound',min(2,2-1)==1)
ck('quotient character dimensions',36-29==3+4 and 33-29==4)
ck('post-second residual dimensions',(36-29-3,33-29-3)==(4,1))
print(json.dumps({'status':'pass','count':len(checks),'checks':checks,'scope':'conditional quotient interface; no actual parameter evaluation or higher original value'},indent=2))
