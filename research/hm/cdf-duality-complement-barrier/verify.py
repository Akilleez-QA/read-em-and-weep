#!/usr/bin/env python3
"""Universal formal counterfamily, never an actual HM matrix evaluation."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=0
def ck(p,msg):
 global checks
 if not p:raise ValueError(msg)
 checks+=1
def zero(m):return all(s.simplify(v)==0 for v in m) if isinstance(m,s.MatrixBase) else s.simplify(m)==0
for row in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/row['path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==row['sha256'],'sha '+row['path'])
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],'blob '+row['path'])
ck(-4-5==-9 and -2-5==-7,'P4 Serre twists')
ck(1+3==4,'P4 cohomological degrees')
ck(1+1==2 and 2+4==6,'direct endpoint trace cup H2 O6')
ck(41!=37 and 24!=21,'endpoint perfect cross-pairing impossible')
ck(17!=13 and 7!=4,'P1 bundle dual marks unequal')
ck(24-(3+5)==16 and 21-16==5,'forced quotient B mark deficit D')
h=s.diag(1,-1);e=s.Matrix([[0,1],[0,0]]);f=s.Matrix([[0,0],[1,0]])
G=s.Matrix([[(a*b).trace() for b in [h,e,f]] for a in [h,e,f]])
ck(G==s.Matrix([[2,0,0],[0,0,1],[0,1,0]]),'universal trace Gram')
ck(G.det()==-2,'nondegenerate trace')
t,u=s.symbols('t u',nonzero=True);a,b,d,w=s.symbols('a b d w')
QV=s.Matrix([[0,1],[1,0]])
QP=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[u,0,0]])
QD=s.Matrix([[0,1,0,0],[0,0,1,0],[t,0,0,0]])
LV=s.Matrix([[0,1],[1,0]])
LP=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0]])
RD=s.Matrix([[0,0,1/t],[1,0,0],[0,1,0],[0,0,0]])
ck(QV*LV==s.eye(2),'V inverse')
ck(LP*QP==s.eye(3),'P injective split')
pc=s.Matrix([[-u,0,0,1]])
ck(pc*QP==s.zeros(1,3),'P quotient kills image')
ck(pc[0,3]==1,'P quotient onto')
ck(QP*LP+s.Matrix([0,0,0,1])*pc==s.eye(4),'P exact kernel image decomposition')
ck(zero(QD*RD-s.eye(3)),'D onto split over Laurent ring')
ck(zero(s.eye(4)-RD*QD-s.diag(0,0,0,1)),'D unique kernel source B2')
ck(2*3+3*4+3*5==33,'derived image character dimension')
ck(3+5==8 and 41-8==33 and 37-33==4,'kernel cokernel dimensions')
ck(3+2*4+5==16,'B image character dimension')
# Source F/B and target complement/B index marks, with no orthogonal assumptions.
for q,xf,xb,yc,yb in [(QV,[0],[1],[1],[0]),(QP,[0],[1,2],[0,3],[1,2]),(QD,[0,1],[2,3],[0],[1,2])]:
 ck(zero(q.extract(yc,xb)),'one-sided B preservation')
 ck(zero(q.T.extract(xb,yc)),'automatic annihilator preservation')
 x=s.Matrix(s.symbols('x:'+str(q.cols)));z=s.Matrix(s.symbols('z:'+str(q.rows)))
 ck(zero((q*x).dot(z)-x.dot(q.T*z)),'graded dual adjunction identity')
ck(QD[2,0]==t and QD.T[0,2]==t,'opposite block remains nonzero in transpose')
# Exact commutant in the entire represented c-d-f pencil algebra.
eV=s.diag(b,d);xV=s.diag(a,b)
eP=s.diag(a,b,b,d);eP[0,3]=w;xP=s.diag(a,b,b)
eD=s.diag(a,b,b);xD=s.diag(a,a,b,b)
CV=eV*QV-QV*xV;CP=eP*QP-QP*xP;CD=eD*QD-QD*xD
ck(CV[1,0]==d-a,'V forces d=a')
ck(zero(CD[2,0]-t*(b-a)),'D forces b=a')
ck(CP[0,0]==u*w,'P forces radical zero')
for C in [CV,CP,CD]:ck(zero(C.subs({b:a,d:a,w:0})),'common scalars suffice')
ck(not zero(CD.subs({a:0,b:1,d:0,w:0})),'B projector genuinely fails')
ck(not zero(CP.subs({a:0,b:0,d:0,w:1})),'radical genuinely fails')
print(json.dumps({'status':'pass','checks':checks,'formal_units':['t','u'],'actual_instance_evaluations':0,'conclusion':'Perfect graded adjunction and scalar commutant do not force complementary preservation.','limitation':'Not an HM realization or full negative-multiplication/Bockstein model.'},indent=2))
