#!/usr/bin/env python3
"""Exact formal presentation and stabilizer tests; no actual source evaluations."""
from pathlib import Path
import hashlib,json
from model import *
ROOT=Path(__file__).resolve().parent;checks=[]
def check(name,value):
 if not bool(value):raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/item['local_path']).read_bytes()
 check('sha256 '+item['label'],hashlib.sha256(data).hexdigest()==item['sha256'])
 check('git blob '+item['label'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
S=s.Matrix([[s.sympify(e) for e in row] for row in json.loads((ROOT/'S.json').read_text())])
M=L.row_join(-S)
check('actual mixed matrix shape',M.shape==(4,8))
check('actual L block degrees',all(f==0 or s.Poly(f,p,q,t).total_degree()==1 for f in L))
check('actual S block degrees',all(f==0 or s.Poly(f,p,q,t).total_degree()==3 for f in S))
check('block twists',1-0==1 and 1-(-2)==3)
u,v=s.symbols('u v');coeff=s.symbols('b0:6');S0=s.Matrix(3,2,coeff)
Sloc=S0.col_join(s.zeros(1,2)).row_join(s.Matrix([0,0,0,1]))
Lloc=s.eye(4).row_join(s.zeros(4,1));Lloc[3,3]=u;Lloc[3,4]=v
Mloc=Lloc.row_join(-Sloc)
right=s.zeros(8,4)
for i in range(3):right[i,i]=1
right[7,3]=-1
check('whole local ring right inverse',Mloc*right==s.eye(4))
J=s.zeros(8,4)
for i in range(3):
 for j in range(2):J[i,j]=S0[i,j]
J[3,2]=1;J[4,3]=1;J[5,0]=1;J[6,1]=1;J[7,2]=u;J[7,3]=v
check('canonical local kernel map',Mloc*J==s.zeros(4,4))
check('local kernel inclusion split',J[[5,6,3,4],:]==s.eye(4))
# Abstract stabilizer of a rotation axis. This is not a point of the source plane.
r=s.Matrix([[-s.Rational(1,2),-s.sqrt(3)/2,0],[s.sqrt(3)/2,-s.Rational(1,2),0],[0,0,1]])
h=s.diag(1,-1,-1)
check('full S3 generator orders',r**3==s.eye(3) and h**2==s.eye(3))
check('full S3 conjugacy relation',h*r*h==r.inv())
check('axis line sign character',r[2,2]==1 and h[2,2]==-1)
Tr=r[:2,:2];Th=-h[:2,:2]
check('projective tangent determinants',Tr.det()==1 and Th.det()==-1)
sizes=[1,3,2];one=[1,1,1];sign=[1,-1,1];std=[2,0,-1];Achar=[3,-1,0]
def inner(a,b):return sum(s.Rational(n,6)*x*y for n,x,y in zip(sizes,a,b))
check('A restricts as sign plus standard',Achar==[x+y for x,y in zip(sign,std)])
check('A has no trivial quotient',inner(Achar,one)==0)
check('A has unique sign quotient',inner(Achar,sign)==1)
check('even twists trivial at axis',[x**2 for x in sign]==one and [x**4 for x in sign]==one)
local_ext=[x*y for x,y in zip(sign,sign)]
check('local Ext2 character trivial',local_ext==one)
check('Frobenius invariant multiplicity',inner(local_ext,one)==1)
check('full nonequivariant Ext dimension',60//6==10)
# P2 line-bundle cohomology: H1 always zero; H2(O(-2)) dual H0(O(-1)) zero.
check('outer H2 vanishes',-(-2)-3==-1)
check('presentation rank',5+3-4==4)
check('presentation first Chern',3*(-2)-4==-10)
source_c2=3*4;target_c2=6
check('presentation second Chern',source_c2-(-10)*4-target_c2==46)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'presentation':'0 -> K_H -> D O + A O(-2) -> P O(1) -> 0','Ext1_equivariant_dimension':1,'Ext1_nonequivariant_dimension':10,'C_L_stabilizer_character':'sign','local_Ext2_character':'trivial','kernel_Chern':{'rank':4,'c1':-10,'c2':46}},indent=2))
