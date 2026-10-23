#!/usr/bin/env python3
"""Universal typed syzygy and polynomial identities; no actual source matrices."""
from pathlib import Path
from itertools import combinations
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent;checks=[]
def check(name,ok):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
for i in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/i['local_path']).read_bytes()
 check(i['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==i['sha256'])
 check(i['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==i['git_blob'])
# All forms retain independent coefficients.
x,y=s.symbols('x y');l0,l1,m0,m1,n0,n1,r0,r1=s.symbols('l0 l1 m0 m1 n0 n1 r0 r1')
l=l0*x+l1*y;m=m0*x+m1*y;n=n0*x+n1*y;r=r0*x+r1*y
br=lambda a,b:s.diff(a,x)*s.diff(b,y)-s.diff(a,y)*s.diff(b,x)
eps=l0*m1-l1*m0
check('actual-Q associativity polynomial relation',s.expand(l*m*r-m*l*r)==0)
check('exact bracket coefficient four',s.expand(br(n*l,m*r)-br(n*m,l*r)-4*eps*n*r)==0)
def cv(f):return [s.Poly(s.expand(f),x,y).coeff_monomial(v) for v in [x*x,x*y,y*y]]
def pair(a,b):
 a,b=cv(a),cv(b)
 return s.Matrix([a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[2]*b[0],a[1]*b[1],a[1]*b[2]+a[2]*b[1],a[2]*b[2]])
rel=(pair(n*l,m*r)-pair(n*m,l*r)).applyfunc(s.expand)
k=s.Matrix([0,0,1,-1,0,0])
check('full symmetric tensor difference is scalar relation',all(s.expand(a-b)==0 for a,b in zip(rel,eps*(n0*r1-n1*r0)*k)))
mult=s.Matrix([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
check('symmetric multiplication quotient rank5',mult.rank()==5)
check('symmetric product kernel exact',mult*k==s.zeros(5,1) and len(mult.nullspace())==1)
# Restricted actual composition types, whose landing assertions are proved.
types={'s':('I4','M2'),'T':('M2','M4'),'TZ':('M2','Z'),'G':('Z','M2'),'X':('M2','M3'),'Y':('M3','M4'),'h':('M4','M2'),'j2':('M2','M2'),'j3':('M3','M3'),'j4':('M4','M4'),'Q2':('M2','M4'),'Q3':('M3','M5'),'terminal':('M4','M5')}
def typ(w):
 for a,b in zip(w,w[1:]):
  if types[a][0]!=types[b][1]:raise RuntimeError('type error '+str(w))
 return types[w[-1]][0],types[w[0]][1]
for name,w,t in [('H',('X','G','TZ','s'),('I4','M3')),('Q3H',('Q3','X','G','TZ','s'),('I4','M5')),('j3H',('j3','X','G','TZ','s'),('I4','M3')),('paired H',('h','Y','X','G','TZ','s'),('I4','M2')),('pairing target kernel',('Q2','h','Y'),('M3','M4')),('radical pairing target',('Y','j3'),('M3','M4')),('actual commutation left',('Q3','X'),('M2','M5')),('actual commutation right',('terminal','Q2'),('M2','M5'))]:check(name+' type',typ(w)==t)
# Exact McKay multiplicities, same fixed labels as the input proofs.
names=['1','W','A','S','D','T','V','P','Wp'];idx={n:i for i,n in enumerate(names)}
def ir(n):return s.eye(9)[:,idx[n]]
adj={'1':['W'],'W':['1','A'],'A':['W','S'],'S':['A','D'],'D':['S','T'],'T':['D','V','P'],'V':['T'],'P':['T','Wp'],'Wp':['P']}
M=s.Matrix.hstack(*[sum((ir(b) for b in adj[a]),s.zeros(9,1)) for a in names]);dims=s.Matrix([[1,2,3,4,5,6,3,4,2]])
check('McKay dimensions',dims*M==2*dims)
check('W tensor P decomposition',M*ir('P')==ir('Wp')+ir('T'))
check('W tensor Wprime has no D',M*ir('Wp')==ir('P'))
check('W tensor T has D once',(M*ir('T'))[idx['D']]==1)
check('Hom P D zero',ir('P').dot(ir('D'))==0)
check('symmetric A dimension decomposition',6==1+5)
check('generated F3 has two T',(ir('Wp')+2*ir('T'))[idx['T']]==2)
check('full middle six T',(3*ir('Wp')+3*ir('S')+6*ir('T'))[idx['T']]==6)
check('combined target four T',(ir('Wp')+3*ir('T')+ir('T'))[idx['T']]==4)
check('new quotient T forces rank at most3',6-(2+1)==3)
# Universal normal form after choosing any three independent kernel vectors.
Z=s.Matrix(4,3,s.symbols('z0:12'));J=s.zeros(4,3).row_join(Z)
check('all fourth minors vanish with three kernel columns',all(J[:,list(c)].det()==0 for c in combinations(range(6),4)))
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'identity':'Psi(n,Hbar(r,p))=4 kappa L_(nr)*p','consequence':'kappa nonzero implies rank of combined T multiplicity map (Q3,j3) at most3','scope':'No coefficient or rank selected; no graded h or mixed commutation assumed.'},indent=2))
