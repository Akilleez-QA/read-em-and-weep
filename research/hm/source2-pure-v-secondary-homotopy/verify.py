#!/usr/bin/env python3
"""Universal symbolic diagnostics only; no actual source data evaluated."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def ck(name,value):
 if not value: raise RuntimeError(name)
 checks.append(name)
def zero(M): return all(s.expand(x)==0 for x in M)
for item in json.loads((root/'INPUTS.json').read_text()):
 data=(root/item['local_path']).read_bytes()
 ck('sha256 '+item['local_path'],hashlib.sha256(data).hexdigest()==item['sha256'])
 ck('git_blob '+item['local_path'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
# Synthetic one-dimensional stand-ins A,D,B_D,B_P and B_D,B_P,C.
# All displayed parameters remain independent indeterminates.
a,b,l,m,n,p,q,t=s.symbols('a b l m n p q t')
Q=s.Matrix([[0,0,1,0],[0,0,0,1],[0,0,0,0]])
h=s.Matrix([[0,0,0],[1,0,0],[0,0,0],[0,0,1]])
T=s.Matrix([[a,0,m,n],[b,l,p,q],[0,0,l,0]])
j2=h*Q;j4=Q*h
ck('square-zero endpoints',zero(j2*j2) and zero(j4*j4))
ck('negative intertwining',zero(j4*T-T*j2))
ck('annihilating homotopy',zero(j2*h) and zero(h*j4))
K0=h*T;K1=T*h
ck('same-direction chain identities',zero(Q*K0-K1*Q) and zero(T*K0-K1*T))
ck('formal chain identity',zero((Q+t*T)*K0-K1*(Q+t*T)))
ck('secondary kernel channels',K0[:,:2]==s.Matrix([[0,0],[a,0],[0,0],[0,0]]))
ck('secondary cokernel zero',K1[2,:]==s.zeros(1,3))
u=s.Matrix([0,0,-a,-b]);x=s.Matrix([1,0,0,0])
ck('first correction',zero(Q*u+T*x))
ck('original second factorization sign',zero(j4*T*u+T*K0*x))
ck('nonzero second scalar product',s.expand((T*u)[2]+l*a)==0)
# Universal ordinary quadratic multiplication; do not specialize direction.
u,v,w=s.symbols('u v w');xx,yy=s.symbols('x y');aa=u*xx**2+v*xx*yy+w*yy**2
def mult(k):
 return s.Matrix([[s.expand(aa*xx**(k-j)*yy**j).coeff(xx,k+2-i).coeff(yy,i) for j in range(k+1)] for i in range(k+3)])
M2=mult(2);M4=mult(4)
M22=s.Matrix([[s.expand(aa**2*xx**(2-j)*yy**j).coeff(xx,6-i).coeff(yy,i) for j in range(3)] for i in range(7)])
ck('universal a times a equals a squared',zero(M4*M2-M22))
ck('leading three-row minor',s.expand(M2[:3,:].det()-u**3)==0)
ck('trailing three-row minor',s.expand(M2[2:,:].det()-w**3)==0)
ck('middle three-row minor on u=w=0',s.expand(M2[1:4,:].det().subs({u:0,w:0})-v**3)==0)
# The A5 character table certifies the unique A tensor A -> D channel.
r=s.sqrt(5);sizes=[1,15,20,12,12];A=[3,-1,0,(1+r)/2,(1-r)/2];D=[5,1,-1,0,0]
ck('unique multiplication D channel',s.simplify(sum(z*a*a*d for z,a,d in zip(sizes,A,D))/60)==1)
H=s.symbols('H')
ck('rank-two quotient Chern classes',s.series((1-H)**-3,H,0,3).removeO()==1+3*H+6*H**2)
print(json.dumps({'status':'pass','checks':checks,'count':len(checks),'scope':'universal symbolic and synthetic only; conditional pure-V branch; no source cut'},indent=2))
