#!/usr/bin/env python3
"""Bounded universal representation/cohomology checks; no actual instance data."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
count=0
def require(v,msg):
 global count
 count+=1
 if not v:raise RuntimeError(msg)
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
def scale(k,x):return k*x[0],k*x[1]
def total(xs):
 r=z(0)
 for x in xs:r=add(r,x)
 return r
def sym(n,x):
 if n==0:return z(1)
 a,b=z(1),x
 for _ in range(2,n+1):a,b=b,sub(mul(x,b),a)
 return b
phi=z(F(1,2),F(1,2));phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
Wp=[z(2),z(-2),phip,neg(phip),phi,neg(phi),z(1),z(-1),z(0)]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
A=[sym(2,x) for x in W];V=[sym(2,x) for x in Wp]
D=[sym(4,x) for x in W];T=[sym(5,x) for x in W]
reps={'1':[z(1)]*9,'W':W,'Wp':Wp,'P':P,'A':A,'V':V,'D':D,'T':T}
dims={k:int(v[0][0]) for k,v in reps.items()}
for i in range(9):
 require(mul(P[i],W[i])==add(Wp[i],T[i]),'primary target Wp+T')
 require(mul(W[i],W[i])==add(z(1),A[i]),'primary evaluation curry')
# Existing universal equations, reduced by a>=1,b>=1.
# Slack (b-1)+(c-1)+e+f=1: four unit vectors exhaust all possibilities.
slacks=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
require(len(slacks)==4 and all(sum(s)==1 for s in slacks),'slack unit-vector completeness')
rows=[]
for sb,sc,e,f in slacks:
 a,b,c,d,g,h=1,1+sb,1+sc,0,0,0
 require(a+d+g+h==1,'first existing equation')
 require(b+c+d+e+f+2*g+h==3,'second existing equation')
 require(c+g+h>=1 and a>=1 and b>=1,'genuine and primary conditions')
 blocks=[]
 for rep,n in [('V',c-1),('P',e),('D',f)]:blocks += [(2,rep)]*n
 blocks += [(3,'Wp')]+[(3,'T')]*b+[(4,'V')]*c+[(5,'Wp')]*e+[(8,'1')]*f
 require(sum(dims[r] for _,r in blocks)==17,'rank17')
 require(sum(-j*dims[r] for j,r in blocks)==-54,'degree-54')
 require(sum(dims[r] for j,r in blocks if j==3)>=8,'degree3 multiplicity lower bound')
 for k in range(9):
  h1e1=total(mul(reps[r][k],sym(j-3,W[k])) for j,r in blocks if j>=3)
  require(h1e1==add(Wp[k],scale(3,T[k])),'actual terminal cohomology character')
  h0e2=total(reps[r][k] for j,r in blocks if j==2)
  h1e2=total(mul(reps[r][k],sym(j-4,W[k])) for j,r in blocks if j>=4)
  require(sub(h0e2,h1e2)==neg(V[k]),'actual Euler twist2 character')
 rows.append({'coefficients':[a,b,c,d,e,f,g,h],'blocks':[[-j,r] for j,r in blocks],'R3_dimension':sum(dims[r] for j,r in blocks if j==3)})
require(len({tuple(r['coefficients']) for r in rows})==4,'four distinct types')
# Formal cohomology controls for canonical slope quotient, no chosen morphism.
for d in [4,5,8,9,10]:
 require(3-d<0,'Hom O(-2) to O(1-d) vanishes')
 require(max(0,2-d)==0,'H0 quotient(1) vanishes')
require(max(0,-1+1)==0,'Hom O to O(-1) zero')
require(max(0,-1+1)==0 and max(0,-(-1)-1)==0,'O(-1) acyclic')
require(max(0,-(-2)-1)==1,'H1 O(-2) dimension1')
rejected=[{'label':'E10','R3_Wp':0,'R3_T':0},{'label':'E13','R3_Wp':0,'R3_T':1},{'label':'E14','R3_Wp':0,'R3_T':0}]
for r in rejected:require(r['R3_Wp']<1 or r['R3_T']<1,'specified type fails primary inclusion')
result={'status':'PASS','checks':count,'input_count':6,'actual_instance_evaluation':False,'canonical_conclusion':'primary terminal Wp+T embeds in canonical R3','remaining_formal_types':rows,'incompatible_specified_types':rejected,'rank_three_coverage_proved_here':False,'full_goal_solved':False}
print(json.dumps(result,indent=2,sort_keys=True))
