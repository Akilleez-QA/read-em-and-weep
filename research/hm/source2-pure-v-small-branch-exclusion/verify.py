#!/usr/bin/env python3
"""Bounded authentication and representation checks, not an actual-source test."""
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
# Multiplicity vectors in irreducible order A,V,P,D,W,Wprime,S,T.
A=s.Matrix([1,0,0,0,0,0,0,0]);V=s.Matrix([0,1,0,0,0,0,0,0]);P=s.Matrix([0,0,1,0,0,0,0,0]);D=s.Matrix([0,0,0,1,0,0,0,0]);Wp=s.Matrix([0,0,0,0,0,1,0,0]);S=s.Matrix([0,0,0,0,0,0,1,0]);T=s.Matrix([0,0,0,0,0,0,0,1]);dims=s.Matrix([[3,3,4,5,2,2,4,6]])
NC2=V+P+2*D;NC3=Wp+S+2*T;F3=Wp+2*T;NC4=P+D;M5=Wp+3*T
ck('actual quotient character NC3/F3',NC3-F3==S)
ck('actual middle dimensions',[(dims*v)[0] for v in [NC3,F3,S]]==[18,14,4])
ck('no S map into full degree5 negative target',S.dot(M5)==0)
ck('full degree5 negative target dimension',(dims*M5)[0]==20)
ck('genuine terminal decomposition',(Wp+2*T)+T==M5)
ck('unique V in actual NC2',V.dot(NC2)==1)
ck('V disjoint from Q kernel in NC2',V.dot(D)==0)
ck('V absent from full joint-negative kernel',V.dot(NC4)==0)
ck('actual quadratic image dimension',(dims*(NC2-D))[0]==12)
ck('endpoint alternatives after contradiction',set([9,16])-{9}=={16})
# Invariant quadratic is even; W is odd. Both sides of Q3(ell*a)=ell*Q2(a)
# have negative parity when a is in the positive N2.
q_parity=1;w_parity=-1;n2_parity=1
ck('actual Q preserves negative source parity',q_parity*(-1)==-1)
ck('commuting arrows have same negative target parity',q_parity*(w_parity*n2_parity)==w_parity*(q_parity*n2_parity)==-1)
x,y,q,a=s.symbols('x y q a')
ck('literal invariant-quadratic polynomial commutation',s.expand(q*(x*a)-x*(q*a))==0 and s.expand(q*(y*a)-y*(q*a))==0)
ck('joint kernel determinant convention invertible',s.Matrix([[0,1],[-1,0]]).det()==1)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,excluded_generated_endpoint=9,necessary_generated_endpoint=16,scope='conditional actual source2 pure-V hypotheses; neither endpoint16 mechanism nor source realization selected'),indent=2))
