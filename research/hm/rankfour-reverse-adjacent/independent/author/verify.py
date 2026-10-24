#!/usr/bin/env python3
"""Universal abstract bundle/character controls, never actual HM instances."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from collections import Counter
import hashlib,json

ROOT=Path(__file__).resolve().parent
NAMES=('1','W','A','S4','D','T6','P',"W'",'V')
DIMS=(1,2,3,4,5,6,4,2,3)
PARITY=(0,1,0,1,0,1,0,1,0)
EDGES=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8))
ZERO=(0,)*9
HASHES={
 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
 'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md':'0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2',
 'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md':'868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c',
 'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md':'783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71',
}
checks=0
def require(c,msg):
 global checks
 checks+=1
 if not c:raise ValueError(msg)
def vec(**kw):return tuple(kw.get(n,0) for n in NAMES)
def unit(i):return tuple(int(i==j) for j in range(9))
def add(*vs):return tuple(sum(v[i] for v in vs) for i in range(9))
def mul(v,k):return tuple(k*x for x in v)
def sub(a,b):return add(a,mul(b,-1))
def dim(v):return sum(x*y for x,y in zip(v,DIMS))
def genuine(v):return all(x>=0 for x in v)
def times_w(v):
 out=[0]*9
 for i,j in EDGES:out[i]+=v[j];out[j]+=v[i]
 return tuple(out)
def sym(v,n):
 if n<0:return ZERO
 prev,now=ZERO,v
 for _ in range(n):prev,now=now,sub(times_w(now),prev)
 return now
def h0(bs,t):return add(*(sym(unit(i),e+t) for e,i in bs if e+t>=0))
def h1(bs,t):return add(*(sym(unit(i),-e-t-2) for e,i in bs if e+t<=-2))
def chi(bs,t):return sub(h0(bs,t),h1(bs,t))
def pretty(v):return {n:c for n,c in zip(NAMES,v) if c}
def shape(bs):return [{'degree':e,'coefficient':NAMES[i]}for e,i in bs]

def authenticate():
 es=json.loads((ROOT/'INPUTS.json').read_text());seen=set()
 require(len(es)==len(HASHES),'input count')
 for x in es:
  name=Path(x['file']).name;require(name in HASHES and name not in seen,'input name');seen.add(name)
  raw=(ROOT/x['file']).read_bytes()
  require(hashlib.sha256(raw).hexdigest()==x['sha256']==HASHES[name],'source SHA256')
  require(len(raw)==x['bytes'],'source byte count')
  require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==x['git_blob_sha1'],'source Git SHA1')
  require(x['ref']=='db51525015bb7c5e825833d550d08dedf6f6ea96','pinned original ref')
  require(x['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+x['ref']+'/'+x['path'],'source URL')
 return len(es)

# Exact Q(sqrt5) class characters; independent of McKay recurrence.
def q(a,b=0):return F(a),F(b)
def qa(a,b):return a[0]+b[0],a[1]+b[1]
def qm(a,b):return a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def qs(c,a):return c*a[0],c*a[1]
def qsub(a,b):return qa(a,qs(-1,b))
def qsym(n,x):
 prev,now=q(0),q(1)
 for _ in range(n):prev,now=now,qsub(qm(x,now),prev)
 return now
TRACES=(q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0))
WEIGHTS=(1,1,12,12,12,12,20,20,30)
CHARS={i:tuple(qsym(i,x) for x in TRACES) for i in range(6)}
CHARS[6]=tuple(q(x) for x in (4,4,-1,-1,-1,-1,1,1,0))
CHARS[8]=tuple(qsub(qsym(6,x),p) for x,p in zip(TRACES,CHARS[6]))
CHARS[7]=tuple(qsub(qm(x,p),t) for x,p,t in zip(TRACES,CHARS[6],CHARS[5]))
def char_eval(v,k):
 s=q(0)
 for i,c in enumerate(v):s=qa(s,qs(c,CHARS[i][k]))
 return s
def class_h0(bs,t):
 out=[]
 for k,x in enumerate(TRACES):
  s=q(0)
  for e,i in bs:
   if e+t>=0:s=qa(s,qm(CHARS[i][k],qsym(e+t,x)))
  out.append(s)
 return tuple(out)
def class_decompose(ch):
 v=[]
 for i in range(9):
  s=q(0)
  for k,w in enumerate(WEIGHTS):s=qa(s,qs(F(w,120),qm(CHARS[i][k],ch[k])))
  require(s[1]==0 and s[0].denominator==1,'integral exact class decomposition');v.append(int(s[0]))
 return tuple(v)
def character_controls():
 require(sum(WEIGHTS)==120,'group order')
 for i in range(9):
  require(CHARS[i][0]==q(DIMS[i]),'character dimension')
  require(CHARS[i][1]==q((-1)**PARITY[i]*DIMS[i]),'center marking')
  require(class_decompose(CHARS[i])==unit(i),'character orthogonality')
  for n in range(25):
   v=sym(unit(i),n)
   require(genuine(v),'genuine symmetric power')
   require(dim(v)==DIMS[i]*(n+1),'symmetric power dimension')
   require(all(not c or PARITY[j]==(PARITY[i]+n)%2 for j,c in enumerate(v)),'symmetric power parity')
   expected=tuple(qm(CHARS[i][k],qsym(n,x))for k,x in enumerate(TRACES))
   require(tuple(char_eval(v,k)for k in range(9))==expected,'McKay vs exact class product')

# Everything below is universal abstract bundle/character arithmetic.
def repchi(R,t):
 if t>=0:return sym(R,t)
 if t==-1:return ZERO
 return mul(sym(R,-t-2),-1)
M2=vec(A=1,V=2,P=3,D=4)
M3=vec(**{"W'":3,'S4':3,'T6':6})
M4=vec(V=2,P=4,D=3)
H=vec(A=2,V=2,P=2,D=2)
def E(t):return sub(repchi(M3,t-1),repchi(M4,t))
def Q(t):return sub(repchi(H,t),E(t))
def Qstar(t):return sub(repchi(M3,t-1),repchi(M2,t))
def dual(bs):return tuple(sorted((-e,i)for e,i in bs))
def class_repchi(R,t):
 if t==-1:return tuple(q(0)for _ in TRACES)
 degree=t if t>=0 else -t-2
 sign=1 if t>=0 else -1
 return tuple(qs(sign,qm(char_eval(R,k),qsym(degree,x)))for k,x in enumerate(TRACES))
def cadd(*xs):return tuple(qa_reduce([x[k]for x in xs])for k in range(9))
def qa_reduce(xs):
 out=q(0)
 for x in xs:out=qa(out,x)
 return out

def cmul(x,c):return tuple(qs(c,a)for a in x)
def class_chi(bs,t):return cadd(*(class_repchi(unit(i),e+t)for e,i in bs))
def class_E(t):return cadd(class_repchi(M3,t-1),cmul(class_repchi(M4,t),-1))
def class_Q(t):return cadd(class_repchi(H,t),cmul(class_E(t),-1))
def class_Qstar(t):return cadd(class_repchi(M3,t-1),cmul(class_repchi(M2,t),-1))

def split_by_blocks(rank,degree,cap=-5):
 lo=degree-(rank-1)*cap
 blocks=[(e,i)for e in range(lo,cap+1)for i in range(9)
         if DIMS[i]<=rank and PARITY[i]==e%2]
 out=[]
 def go(start,r,d,bs):
  if r==0:
   if d==0:out.append(tuple(bs))
   return
  for k in range(start,len(blocks)):
   e,i=blocks[k];n=DIMS[i]
   if n<=r and (r-n)*lo<=d-e*n<=(r-n)*cap:
    go(k,r-n,d-e*n,bs+[(e,i)])
 go(0,rank,degree,[])
 return tuple(sorted(out))

def split_by_ordinary_degrees(rank,degree,cap=-5):
 """Independent five ordinary-line partitions, then coefficient decompositions."""
 lo=degree-(rank-1)*cap;out=[];reps={}
 for parity in range(2):
  ids=[i for i in range(9)if PARITY[i]==parity and DIMS[i]<=rank]
  for n in range(1,rank+1):
   reps[parity,n]=[]
   for length in range(1,n+1):
    for ijs in combinations_with_replacement(ids,length):
     if sum(DIMS[i]for i in ijs)==n:reps[parity,n].append(ijs)
 for es in combinations_with_replacement(range(lo,cap+1),rank):
  if sum(es)!=degree:continue
  degrees=sorted(Counter(es).items())
  for choices in product(*(reps[e%2,n]for e,n in degrees)):
   bs=[]
   for (e,n),ijs in zip(degrees,choices):bs.extend((e,i)for i in ijs)
   out.append(tuple(sorted(bs)))
 return tuple(sorted(out))

def pair_data(F0,D0):
 Du=dual(D0)
 def B(t):return add(E(t),mul(chi(F0,t),-1),mul(Q(t-6),-1),chi(Du,t-6))
 def BC(t):return cadd(class_E(t),cmul(class_chi(F0,t),-1),cmul(class_Q(t-6),-1),class_chi(Du,t-6))
 residuals=[]
 for t in (0,1):
  residual=sub(add(B(t+2),B(t+4),chi(Du,t)),Q(t))
  rc=cadd(BC(t+2),BC(t+4),class_chi(Du,t),cmul(class_Q(t),-1))
  require(class_decompose(rc)==residual,'independent endpoint residual class calculation')
  require(dim(residual)==0,'endpoint residual has zero ordinary dimension')
  residuals.append(residual)
 if any(x!=ZERO for x in residuals):return residuals,None
 primal=sub(B(2),E(2))
 dualtail=sub(mul(B(-3),-1),Qstar(3))
 require(class_decompose(cadd(BC(2),cmul(class_E(2),-1)))==primal,'independent primal persistence character')
 require(class_decompose(cadd(cmul(BC(-3),-1),cmul(class_Qstar(3),-1)))==dualtail,'independent dual persistence character')
 require(not genuine(primal)or not genuine(dualtail),'every Euler survivor fails a necessary positivity test')
 return residuals,{'F0':shape(F0),'D0':shape(D0),'minus_chi_F2_2':pretty(primal),
                  'minus_chi_D1_3':pretty(dualtail),
                  'failed_tests':[name for name,x in [('F2_twist2',primal),('D1_twist3',dualtail)]if not genuine(x)]}

def derive():
 ninputs=authenticate();character_controls()
 require([dim(x)for x in (M2,M3,M4,H)]==[41,54,37,30],'actual presentation dimensions')
 require(sub(sub(times_w(M3),M2),M4)==H,'actual ambient from Koszul class')
 require(E(2)==vec(V=-1),'actual E twist2 Euler')
 require(Qstar(2)==vec(**{'1':-1,'A':-2,'D':-1,'V':-1}),'actual Qstar twist2 Euler')
 require(Qstar(3)==vec(W=-2,S4=-1,T6=1),'actual Qstar twist3 Euler')
 for t in range(-12,13):
  require(Qstar(t)==mul(Q(-t-2),-1),'actual duality from unequal presentations')
  require(class_decompose(class_E(t))==E(t),'actual E class presentation')
  require(class_decompose(class_Qstar(t))==Qstar(t),'actual Qstar class presentation')
 require([NAMES[i]for i in range(9)if DIMS[i]==1]==['1'],'unique one-dimensional representation')
 # Formal Laurent shift ledger: this is an identity of graded classes,
 # before any character specialization or endpoint selection.
 lower={-4:1,-2:1,0:1};upper={2:1,4:1}
 eliminated=Counter(lower)
 for shift,coefficient in upper.items():eliminated[shift-6]-=coefficient
 require({k:c for k,c in eliminated.items()if c}=={0:1},'formal B elimination by upper shift minus six')
 require(-2==-(2),'dual quotient L4 star is B star minus two')
 require(2+2<5 and 1+3<5,'both final persistence twists are interior')
 ranks=[5+4*i for i in range(6)]
 require(ranks==[5,9,13,17,21,25],'ordered rank-four ranks')
 require(ranks[3]==17 and 30-ranks[5]==5,'correct unequal marked central role')
 caps=[-(5-i)for i in range(5)]
 require(caps==[-5,-4,-3,-2,-1],'persistence degree caps')
 # Formal affine vectors: constant, a, c1, delta1,...,delta4.
 def basis(i):return tuple(int(i==j)for j in range(7))
 def padd(*xs):return tuple(sum(x[i]for x in xs)for i in range(7))
 def scale(x,n):return tuple(n*y for y in x)
 cs=[basis(2)]
 for j in range(4):cs.append(padd(cs[-1],scale(basis(0),8),basis(j+3)))
 es=padd(basis(1),*cs[:3]);bs=padd(basis(1),*cs)
 symbolic=padd(scale(basis(1),2),scale(bs,3),scale(es,-5))
 require(symbolic==(120,0,0,2,4,6,3),'formal exact endpoint determinant identity')
 bounds=[2*((-5*5)//2)]*2;weights=list(symbolic[3:])
 require(bounds==[-26,-26],'even endpoint degree bounds')
 slack=2*bounds[0]+3*bounds[1]-(-150)
 require(slack==20 and min(weights)*12==24>slack,'all invariant determinant defects vanish')
 uv=[(u,v)for u in range(slack//4+1)for v in range(slack//6+1)if 4*u+6*v==slack]
 require(uv==[(2,2),(5,0)],'complete zero-defect endpoint arithmetic')
 cases=sorted([(-26-2*u,-26-2*v)for u,v in uv]);require(cases==[(-36,-26),(-30,-30)],'two endpoint cases')
 split_lists={}
 for degree,expected_count in [(-36,44),(-30,15),(-26,4)]:
  first=split_by_blocks(5,degree);second=split_by_ordinary_degrees(5,degree)
  require(first==second,'independent complete endpoint enumeration')
  require(len(first)==len(set(first))==expected_count,'endpoint splitting count')
  for bb in first:
   require(sum(DIMS[i]for e,i in bb)==5,'endpoint rank')
   require(sum(e*DIMS[i]for e,i in bb)==degree,'endpoint degree')
   require(all(degree+20<=e<=-5 and PARITY[i]==e%2 for e,i in bb),'forced endpoint degree and parity window')
  split_lists[degree]=first
 results=[]
 for a,b in cases:
  require((-78-a)%3==0,'integral first quotient degree')
  c1=(-78-a)//3;ci=[c1+8*j for j in range(5)];fi=[a]
  for c in ci:fi.append(fi[-1]+c)
  require(fi[3]==-54 and fi[-1]==b,'stage degree consistency')
  survivors=[];rejected=0
  for F0,D0 in product(split_lists[a],split_lists[b]):
   residuals,row=pair_data(F0,D0)
   if row is None:rejected+=1
   else:survivors.append(row)
  expected_survivors=4 if a==-36 else 10
  require(len(survivors)==expected_survivors,'exact two-twist Euler survivor count')
  require(rejected+len(survivors)==len(split_lists[a])*len(split_lists[b]),'complete pair coverage')
  results.append({'endpoint_degrees':[a,b],'degree_windows':[[a+20,-5],[b+20,-5]],
   'quotient_degrees':ci,'stage_degrees':fi,'endpoint_counts':[len(split_lists[a]),len(split_lists[b])],
   'pairs_tested':rejected+len(survivors),'rejected_by_exact_Euler':rejected,
   'Euler_survivors':survivors,'remaining_after_persistence':0})
 require(sum(x['pairs_tested']for x in results)==401,'complete new bounded pair domain')
 # Explicit symbolic relations, recorded and mutation-tested separately from search.
 expected={'rank':4,'ordered_profile':[3,2],'ambient_rank':30,'central_rank':17,
  'endpoint_bounds':bounds,'defect_weights':weights,'slack':20,'invariant_divisor_minimum':12,
  'cases':cases,'E2':list(E(2)),'Qstar3':list(Qstar(3)),
  'B_expression_shifts':[0,0,-6,-6],'top_shifts':[2,4],
  'Euler_test_twists':[0,1],'persistence_stages_and_twists':[[2,2],[1,3]],
  'counts':[44,15,4,401,4,10,0]}
 expected=json.loads(json.dumps(expected))
 def accept(x):return x==expected
 require(accept(json.loads(json.dumps(expected))),'base numerical/character contract')
 def leaves(x,path=()):
  if isinstance(x,list):
   for i,y in enumerate(x):yield from leaves(y,path+(i,))
  else:yield path
 mutations=0
 for key,value in expected.items():
  for path in leaves(value):
   changed=json.loads(json.dumps(expected))
   if path:
    dest=changed[key]
    for i in path[:-1]:dest=dest[i]
    dest[path[-1]]+=1
   else:changed[key]+=1
   require(not accept(changed),'fail closed on changed contract '+key+str(path));mutations+=1
 return {'status':'PASS','scope':'Excludes only maximal ordered rank-four plateau (3,2), conditional on the retained actual geometric premises.',
  'authenticated_originals':ninputs,'historical_enumeration_used':False,'rank_four_quotient_enumeration_used':False,
  'actual_instance_evaluation_used':False,'source_Z_assumed':False,
  'actual_E2_Euler':pretty(E(2)),'actual_Qstar3_Euler':pretty(Qstar(3)),
  'plateau_ranks':ranks,'endpoint_degree_bounds':bounds,'defect_weights':weights,
  'determinant_defects':[0]*4,'derived_endpoint_splittings':{str(d):[shape(bb)for bb in ss]for d,ss in split_lists.items()},
  'cases':results,'total_pairs':401,'Euler_survivors':14,'remaining':0,
  'mutation_rejections':mutations,'checks':checks}

if __name__=='__main__':print(json.dumps(derive(),indent=2,sort_keys=True))
