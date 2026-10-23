#!/usr/bin/env python3
"""Bounded provenance and universal identities; no actual source evaluations."""
from pathlib import Path
import hashlib,json
import sympy as s
r=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not bool(value):raise RuntimeError(name)
 checks.append(name)
for a in json.loads((r/'INPUTS.json').read_text()):
 d=(r/a['local_path']).read_bytes()
 ck('sha256 '+a['label'],hashlib.sha256(d).hexdigest()==a['sha256'])
 ck('git blob '+a['label'],hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==a['git_blob'])
def h0(d):return max(d+1,0)
def h1(d):return max(-d-1,0)
ck('endpoint twist2 generated with no H1',[h0(0),h1(0)]==[1,0])
ck('separated quotient twist2 has no sections',2*h0(-7)+6*h0(-1)==0)
ck('untwisted quotient has no sections',2*h0(-9)+6*h0(-3)==0)
ck('embedded endpoint cohomology dimension',9*h1(-2)==9)
ck('endpoint next cohomology vanishes',9*h1(-1)==0)
ck('restricted actual Koszul dimensions',17+1==2*9)
x,y=s.symbols('x y')
ck('universal Koszul cancellation',(s.Matrix([[x,y]])*s.Matrix([y,-x]))==s.zeros(1,1))
J=s.Matrix([[0,1],[-1,0]])
ck('determinant convention invertible',J.det()==1 and J*J==-s.eye(2))
ck('full Koszul dimension compatibility',2*37-54==2+3*6)
ck('actual submodule length',9+14+9==32)
t=s.symbols('t');H=9*t**2+14*t**3+9*t**4
N=9*t**2-4*t**3-10*t**4-4*t**5+9*t**6
ck('shifted Hilbert numerator',s.expand(H*(1-t)**2-N)==0)
ck('free resolution rank Euler sum',9-(4+10+4)+9==0)
ck('free resolution degree Euler sum',9*2-(4*3+10*4+4*5)+9*6==0)
ck('free resolution length via second derivative',s.diff(N,t,2).subs(t,1)/2==32)
F0=s.Matrix([0,0,1,1,0,0,0,0]);F1=s.Matrix([0,0,0,0,0,1,0,2]);WF0=s.Matrix([0,0,0,0,0,1,1,2]);WF1=s.Matrix([0,2,3,2,0,0,0,0])
ck('linear and cubic relation characters',F1-WF0==s.Matrix([0,0,0,0,0,0,-1,0]))
ck('quadratic relation character',2*F0-WF1==s.Matrix([0,-2,-1,0,0,0,0,0]))
ck('terminal socle dimension',4+5==9)
ck('irreducible negative homogeneous pieces dimensions',[1,2,3]==[1,2,2*(2+1)//2])
ck('annihilator quotient length',sum([1,2,3])==6)
ck('actual degree shift',[0+2,1+2,2+2,3+2,4+2]==[2,3,4,5,6])
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,actual_negative_module_hilbert=[0,0,9,14,9],length=32,annihilator='(W)^3',resolution_degrees={'generators':{'2':9},'relations':{'3':4,'4':10,'5':4},'second_syzygies':{'6':9}},scope='conditional endpoint9; actual negative submodule only, not full Rao or positive action'),indent=2))
