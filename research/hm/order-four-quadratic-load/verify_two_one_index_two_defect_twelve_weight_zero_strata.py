#!/usr/bin/env python3
"""Three scalar strata of one torsion alternative and same-endpoint section pruning."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
ROOT=Path(__file__).resolve().parent

# Exact Q(sqrt(5)) character arithmetic, independently reproduced here.
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def minus(a,b):return plus(a,scale(-1,b))
def total(xs):
 out=(F(0),F(0))
 for x in xs:out=plus(out,x)
 return out
z=lambda a,b=0:(F(a),F(b))
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def symchar(n):
 a=[z(1)]*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,[minus(times(w,v),u)for w,v,u in zip(W,b,a)]
 return b
chars={'one':[z(1)]*9,'W':W,'A':symchar(2),'S':symchar(3),'D':symchar(4),'T':symchar(5)}
chars['P']=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
chars['V']=[minus(a,b)for a,b in zip(symchar(6),chars['P'])]
chars['Wp']=[minus(times(w,p),t)for w,p,t in zip(W,chars['P'],chars['T'])]
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(s,times(x,y))for s,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
# Characters are real, hence the nine irreducibles are self-dual.
# W has trivial determinant: Lambda^2 W = 1 (the standard SL2 lift).
# The recurrence uses exactly that determinant-one linearization.
def mul(a,b):return [times(x,y)for x,y in zip(a,b)]
def sub(a,b):return [minus(x,y)for x,y in zip(a,b)]
def linear(terms):return [total(scale(c,chars[n][i])for c,n in terms)for i in range(9)]
def decompose(a):
 out=[inner(a,chars[n])for n in names]
 assert all(b==0 and x.denominator==1 for x,b in out)
 return tuple(int(x)for x,b in out)
M3=linear([(3,'Wp'),(3,'S'),(6,'T')])
M4=linear([(2,'V'),(4,'P'),(3,'D')])
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md': 'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843', 'NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md': '53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08', 'NEGATIVE-GAUSS-FLAGS-HAVE-A-FINITE-DEGREE-ENVELOPE.md': '90aa42a0eded9cd3118d086a4ebf82ce98ff4e4c3682e1baaea61e5928f94088'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
rows=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][2]
ID='G3.21.d610e381ed75';row=next(r for r in rows if r['id']==ID)
assert row['profile']=='21' and row['source_index']==2
assert row['A']==p['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==p['B']==[[-18,'one'],[-4,'one'],[6,'one']]
alts=[a for a in p['alternatives']if a['s']==12 and a['torsion']==[[12,0]]]
assert len(alts)==1 and len(alts[0]['endpoints'])==8
Ms=alts[0]['endpoints'];C=[-10,0,14];assert [e%10 for e in C]==[0,0,4]
# No invariant global low-to-middle lift, and one-dimensional extension group.
assert inner(symchar(10),chars['one'])==z(0)
assert inner(symchar(0),chars['one'])==z(1) # H1O(-2)=1.
strata={'low_only':[(-22,'one'),(0,'one'),(14,'one')],
        'middle_only':[(-12,'one'),(-10,'one'),(14,'one')],
        'mixed':[(-11,'W'),(14,'one')]}
dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]))
def h0(b,t):
 return decompose([total(mul(chars[n],symchar(e+t))[i]for e,n in b if e+t>=0)for i in range(9)])
assert all(sum(dims[n]for e,n in J)==3 and sum(e*dims[n]for e,n in J)==-8 for J in strata.values())
assert -48-2*p['a']+12==-56
for M in Ms:assert sum(dims[n]for e,n in M)==11 and sum(e*dims[n]for e,n in M)==-56 and max(e for e,n in M)<=-4
regimes=[];removed=[]
for name,J in strata.items():
 target=tuple(sum(h0(J,t)[i]for t in [4,2,0])for i in range(9))
 assert target[0]==(1 if name=='low_only'else 0)
 lam=sorted([e for e,n in J for _ in range(dims[n])],reverse=True)
 heights=[(a,11-a,0)for a in range(6,12)] # All endpoint first ranks<=2.
 capacity=max(sum(h*d-h*(h+1)for h,d in zip(v,lam))for v in heights)
 assert capacity>=-56
 surviving=[]
 for index,M in enumerate(Ms):
  source=h0(M,6);difference=tuple(a-b for a,b in zip(target,source))
  if min(difference)<0:removed.append(dict(stratum=name,published_endpoint_index=index,M=M,H0_M_six=source,target=target,difference=difference))
  else:surviving.append(index)
 regimes.append(dict(stratum=name,J=J,twist_six_target=target,maximal_endpoint_degree_capacity=capacity,remaining_endpoint_indices=surviving))
assert {x['published_endpoint_index']for x in removed}=={3,4,5,7}
assert len(removed)==8 and all(x['difference'][0]==-1 for x in removed)
assert all([-6,'one']in Ms[i]for i in [3,4,5,7])
out=dict(scope='Three actual-image scalar strata; eight same-stratum/endpoint combinations pruned, no torsion-branch or quotient-label exclusion.',source_hashes=PINNED,id=ID,source_pair_index=2,second_defect=12,torsion=[[12,0]],character_order=names,strata=regimes,removed_combinations=removed,initial_combinations=24,remaining_combinations=16,realization_claimed=False)
(ROOT/'two-one-index-two-defect-twelve-weight-zero-strata.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'weight0 torsion has3 actual-kernel scalar strata;24 abstract combinations reduced to16, no branch exclusion.')
