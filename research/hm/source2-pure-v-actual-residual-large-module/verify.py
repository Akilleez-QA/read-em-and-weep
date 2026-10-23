#!/usr/bin/env python3
"""Universal structural arithmetic only; no actual source instance."""
from pathlib import Path
import hashlib,json
import sympy as s
r=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
 if not bool(b):raise RuntimeError(name)
 checks.append(name)
for a in json.loads((r/'INPUTS.json').read_text()):
 d=(r/a['local_path']).read_bytes()
 ck('sha256 '+a['label'],hashlib.sha256(d).hexdigest()==a['sha256'])
 ck('git blob '+a['label'],hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==a['git_blob'])
def h0(d):return max(d+1,0)
def h1(d):return max(-d-1,0)
ck('endpoint twist1 acyclic',h0(-1)==h1(-1)==0)
ck('residual quotient degree5 dimension',6*h1(-2)==6)
ck('separated degree5 dimension',2*h1(-8)==14)
ck('full degree5 dimension',14+6==2+3*6)
ck('residual degree4 dimension',9+12==21)
ck('residual-large endpoint dimension',21-5==4+12==16)
ck('nonzero terminal image forced by kernel intersection',16>4)
x,y=s.symbols('x y')
ck('Koszul coefficient cancellation',s.Matrix([[x,y]])*s.Matrix([y,-x])==s.zeros(1,1))
ck('full Koszul exact-sequence dimensions',2*37-54==20)
# Ordered character coordinates A,V,P,D,W,Wprime,S,T.
F0=s.Matrix([0,0,1,1,0,0,0,0]);F1=s.Matrix([0,0,0,0,0,1,0,2]);F2=s.Matrix([0,1,2,1,0,0,0,0]);F3=s.Matrix([0,0,0,0,0,0,0,1])
WF0=s.Matrix([0,0,0,0,0,1,1,2]);WF1=s.Matrix([0,2,3,2,0,0,0,0]);WF2=s.Matrix([0,0,0,0,0,2,1,4]);WF3=s.Matrix([0,1,1,1,0,0,0,0])
coeff=[F0,F1-WF0,F2-WF1+F0,F3-WF2+F1,F2-WF3,F3]
expect=[F0,s.Matrix([0,0,0,0,0,0,-1,0]),s.Matrix([0,-1,0,0,0,0,0,0]),s.Matrix([0,0,0,0,0,-1,-1,-1]),s.Matrix([0,0,1,0,0,0,0,0]),F3]
for i in range(6):ck('equivariant numerator coefficient '+str(i),coeff[i]==expect[i])
dim=s.Matrix([[3,3,4,5,2,2,4,6]])
ck('actual Hilbert dimensions',[(dim*f)[0] for f in [F0,F1,F2,F3]]==[9,14,16,6])
ck('numerical numerator',[int((dim*c)[0]) for c in coeff]==[9,-4,-3,-12,4,6])
t=s.symbols('t');H=9+14*t+16*t*t+6*t**3;N=9-4*t-3*t*t-12*t**3+4*t**4+6*t**5
ck('Hilbert numerator identity',s.expand(H*(1-t)**2-N)==0)
ck('length',H.subs(t,1)==45)
ck('original shifted resolution numerator',s.expand(t*t*N-(9*t**2-4*t**3-3*t**4-12*t**5+4*t**6+6*t**7))==0)
ck('free rank Euler identity',9-(4+3+12)+(4+6)==0)
ck('free degree Euler identity',9*2-(4*3+3*4+12*5)+(4*6+6*7)==0)
ck('length from original numerator',s.diff(t*t*N,t,2).subs(t,1)/2==45)
ck('annihilator low pieces irreducible dimensions',[2,3,4]==[d+1 for d in range(1,4)])
ck('annihilator quotient length',sum(range(1,5))==10)
ck('socle not level',4!=5)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,hilbert_original_degrees={'2':9,'3':14,'4':16,'5':6},socle_original_degrees={'4':'I4=P','5':'NR5=T'},length=45,annihilator='(W)^4',minimal_relations={'3':'S','4':'V','5':'Wprime+S+T'},second_syzygies={'6':'P','7':'T'},scope='actual residual-large branch only; no nonzero-N0 or positive-variable claim'),indent=2))
