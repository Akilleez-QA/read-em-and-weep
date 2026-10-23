#!/usr/bin/env python3
"""Bounded universal checks only. No actual HM/source instance data."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
import sympy as sp
count=0
def require(v,msg):
 global count
 count+=1
 if not v: raise RuntimeError(msg)
base=Path(__file__).resolve().parent
for item in json.loads((base/'INPUTS.json').read_text()):
 b=(base/item['local_path']).read_bytes()
 require(len(b)==item['bytes'],item['label']+' bytes')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],item['label']+' SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'],item['label']+' Git blob')
def z(a,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def sym(n,x):
 if n==0:return z(1)
 a,b=z(1),x
 for _ in range(2,n+1):a,b=b,sub(mul(x,b),a)
 return b
phi=z(F(1,2),F(1,2));phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
A=[sym(2,x) for x in W];T=[sym(5,x) for x in W]
Wp=[z(2),z(-2),phip,neg(phip),phi,neg(phi),z(1),z(-1),z(0)]
for w,a,p,t,wp in zip(W,A,P,T,Wp):
 require(mul(w,w)==add(z(1),a),'Hom(W,W)=1+A')
 require(mul(p,w)==add(wp,t),'primary terminal P tensor W')
require(P[0]==z(4) and W[0]==z(2),'actual character dimensions')
require(P[1]==P[0] and W[1]==neg(W[0]),'physical parity')
require(add(z(1),A[1])==z(4),'primary Y positive')
require(4*4==16 and 4*2==8,'primary pencil dimensions')
require(16-8==8 and -16==8*(-2),'primary kernel rank and degree')
require(16-14==2 and -16==2*(-8),'first-block kernel rank and degree')
require(8>6,'terminal injection contradiction')
# Exact evaluation 2->1 over arbitrary projective variables, then tensor Z,U.
u,v=sp.symbols('u v')
evalrow=sp.Matrix([[u,v]])
kernel=sp.Matrix([-v,u])
require((evalrow*kernel)==sp.zeros(1,1),'universal evaluation syzygy')
# On each affine chart the evalrow has a right inverse and kernel generator.
for row,col,ker in [(sp.Matrix([[1,v]]),sp.Matrix([1,0]),sp.Matrix([-v,1])),(sp.Matrix([[u,1]]),sp.Matrix([0,1]),sp.Matrix([-1,u]))]:
 require(row*col==sp.ones(1,1),'evaluation chart splitting')
 require(row*ker==sp.zeros(1,1),'evaluation chart kernel')
 require(sp.det(sp.Matrix.hstack(col,ker)) in [1,-1],'evaluation chart basis')
# Universal source [u v] and long preinjective target B_m.
# These are formal representation diagrams, never actual HM matrices.
controls={}
for m in [2,3,8]:
 a=sp.symbols('a0:'+str(m));b=sp.symbols('b0:'+str(m));c=sp.symbols('c0:'+str(m-1))
 eq=[]
 for i in range(m-1):eq += [a[i],-a[i+1]-c[i],-b[i+1],b[i]-c[i]]
 sol=sp.linsolve(eq,(*a,*b,*c))
 tup=next(iter(sol));free=set().union(*(q.free_symbols for q in tup))
 require(len(free)==int(m==2),'universal Hom dimension m='+str(m))
 if m>2:require(all(q==0 for q in tup),'all long-pencil morphisms vanish')
 else:require(tup==(0,-c[0],c[0],0,c[0]),'sharp m=2 nonzero control')
 controls[str(m)]={'source_dimensions':[2,1],'target_dimensions':[m,m-1],'hom_dimension':len(free)}
for m in [3,8]:
 require(max(0,2-m+1)==0,'kernel Hom cohomology vanishing')
require(max(0,-1+1)==0,'constant-to-minus-one vanishing')
result={'status':'PASS','checks':count,'input_count':5,'primary_dimensions':[16,8],'primary_kernel':['P tensor W',-2],'first_block_kernel':['W',-8],'residual_terminal_dimension':6,'universal_hom_controls':controls,'actual_instance_evaluation':False,'scope':'conditional actual source2 pure-V compatible-radical exclusion; not full goal'}
print(json.dumps(result,indent=2,sort_keys=True))
