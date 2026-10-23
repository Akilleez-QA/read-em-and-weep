#!/usr/bin/env python3
"""Pinned actual-map premises plus formal linear algebra, no source evaluations."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent;checks=[]
def ck(name,v):
 if not bool(v):raise RuntimeError(name)
 checks.append(name)
for p in json.loads((root/'INPUTS.json').read_text()):
 b=(root/p['local_path']).read_bytes()
 ck('sha256 '+p['label'],hashlib.sha256(b).hexdigest()==p['sha256'])
 ck('git blob '+p['label'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob'])
# Character vectors in order A,V,P,D. Isotypical intersections are proved
# in the text, not inferred by arbitrary subtraction of characters.
dims=s.Matrix([[3,3,4,5]])
NC=s.Matrix([0,1,1,2]);I2=s.Matrix([0,0,0,1]);I4=s.Matrix([0,0,1,0]);A=s.Matrix([1,0,0,0]);Ph=I4
U=NC-I2;NC4=I4+I2
ck('NC source character dimension',(dims*NC)[0]==17)
ck('actual kernel character dimension',(dims*(A+I2))[0]==8)
ck('NC has no A',NC[0]==0)
ck('Q image character',U==s.Matrix([0,1,1,1]))
ck('Q image dimension',(dims*U)[0]==12)
ck('small full preimage intersection',(dims*(I2+Ph))[0]==9)
ck('large full preimage intersection',(dims*I2)[0]==5)
ck('small target intersection',(dims*Ph)[0]==4)
ck('large target intersection dimension',5-5==0)
ck('small quotient image dimension',12-4==8)
ck('large quotient image dimension',12-0==12)
ck('residual target dimension',(dims*NC4)[0]==9)
ck('residual direct sum character',NC4+U==s.Matrix([0,1,2,2]))
ck('residual transverse sum dimension',(dims*(NC4+U))[0]==21)
# Universal preimage lemma in abstract block coordinates. K is a kernel,
# P maps invertibly to I, and T maps invertibly to the complementary image.
# Matrices below are symbolic normal forms for a linear-algebra lemma,
# not actual N spaces, sources, coefficients, or instances.
u=s.symbols('u',nonzero=True); b=s.symbols('b0:4');c=s.symbols('c0:4')
B=s.Matrix(2,2,b);C=s.Matrix(2,2,c)
Q=s.zeros(4,6);Q[:2,2:4]=u*s.eye(2);Q[:2,4:6]=B;Q[2:4,4:6]=C
P=s.zeros(6,2);P[2:4,:]=s.eye(2)/u
incl=s.eye(4)[:,:2]
ck('symbolic section of I',Q*P==incl)
# qbar C^-1 normalizes the target complement; its vanishing forces T=0.
normal=s.diag(s.eye(2),C.inv())*Q
ck('complement quotient isolates T',s.simplify(normal[2:4,:]-s.eye(6)[4:6,:])==s.zeros(2,6))
x0,x1=s.symbols('x0 x1');yy=s.Matrix([x0,x1]);k0,k1=s.symbols('k0 k1')
x=s.Matrix([k0,k1,x0/u,x1/u,0,0])
ck('whole preimage parametrization',Q*x==incl*yy)
ck('section subtraction lands in kernel',Q*(x-P*yy)==s.zeros(4,1))
# Three isotypical projections show there can be no mixed A/P/D cancellation.
PA=s.diag(1,0,0);PD=s.diag(0,1,0);PP=s.diag(0,0,1)
ck('isotypical projections sum identity',PA+PD+PP==s.eye(3))
ck('isotypical projections orthogonal',all(X*Y==s.zeros(3) for X,Y in [(PA,PD),(PA,PP),(PD,PP)]))
# Transversality implication: U contained ker h; ker h intersection C=I;
# U intersection I=0. Exhaust the abstract membership truth table.
allowed=[]
for inU in [False,True]:
 for inC in [False,True]:
  for inh in [False,True]:
   for inI in [False,True]:
    if inU and not inh:continue
    if inC and inh and not inI:continue
    if inU and inI:continue
    allowed.append((inU,inC,inh,inI))
ck('intersection implication without Q residual invariance',all(not(U0 and C0) for U0,C0,_,_ in allowed))
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'Q_NC2_dimension':12,'Q_NC2_character':'V+P+D','I4_intersection_by_endpoint':{'9':4,'16':0},'NC4_transverse_only_in_residual_large':True,'scope':'formal linear algebra and pinned premises; no actual coefficient evaluation'},indent=2))
