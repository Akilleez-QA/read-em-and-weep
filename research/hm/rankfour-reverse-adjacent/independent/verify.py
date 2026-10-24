#!/usr/bin/env python3
"""Independent intrinsic endpoint test. Exact class arithmetic; no author imports."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
from collections import Counter
import json, hashlib, sys
ROOT=Path(__file__).resolve().parent
MUT=sys.argv[1] if len(sys.argv)>1 else ''
CHECKS=0
SOURCE_HASHES={
 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
 'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md':'0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2',
 'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md':'868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c',
 'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md':'783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71',
}

def check(ok,label):
 global CHECKS
 CHECKS+=1
 if not ok: raise RuntimeError(label)

def q(a,b=0):return F(a),F(b)
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def times(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(a,x):return a*x[0],a*x[1]
def minus(x,y):return plus(x,scale(-1,y))
def sym(n,x):
 old,now=q(0),q(1)
 for _ in range(n):old,now=now,minus(times(x,now),old)
 return now
TRACES=(q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0))
SIZES=(1,1,12,12,12,12,20,20,30)
NAMES=('1','W','A','S4','D','T6','P',"W'",'V')
DIMS=(1,2,3,4,5,6,4,2,3)
PARITY=(0,1,0,1,0,1,0,1,0)
ZERO=(q(0),)*9

def add(*cs):return tuple((sum(c[j][0] for c in cs),sum(c[j][1] for c in cs))for j in range(9))
def mult(k,c):return tuple(scale(k,x)for x in c)
def sub(c,d):return add(c,mult(-1,d))
def tensor(c,d):return tuple(times(x,y)for x,y in zip(c,d))
C={n:tuple(sym(i,x)for x in TRACES)for i,n in enumerate(NAMES[:6])}
C['P']=tuple(q(a)for a in(4,4,-1,-1,-1,-1,1,1,0))
C['V']=sub(tuple(sym(6,x)for x in TRACES),C['P'])
C["W'"]=sub(tensor(C['W'],C['P']),C['T6'])
if MUT=='physical-marking':C['V'],C['A']=C['A'],C['V']

def inner(c,d):
 out=q(0)
 for j in range(9):out=plus(out,scale(F(SIZES[j],120),times(c[j],d[j])))
 return out
@lru_cache(None)
def decompose(c):
 out=[]
 for n in NAMES:
  a,b=inner(c,C[n]);check(b==0 and a.denominator==1,'integral exact class multiplicity')
  out.append(int(a))
 return tuple(out)
def rep(**kw):return add(*(mult(v,C[k])for k,v in kw.items()))
def show(c):return {n:v for n,v in zip(NAMES,decompose(c))if v}
def positive(c):return all(x>=0 for x in decompose(c))
@lru_cache(None)
def line(t):
 if t>=0:return tuple(sym(t,x)for x in TRACES)
 if t==-1:return ZERO
 if MUT=='omit-H1':return ZERO
 return mult(-1,tuple(sym(-t-2,x)for x in TRACES))
@lru_cache(None)
def chi(shape,t):return add(*(tensor(C[n],line(e+t))for e,n in shape))
def dual(shape):return tuple((-e,n)for e,n in shape)
def shape_json(shape):return [{'degree':e,'irrep':n}for e,n in shape]

# Independent enumeration: partition the ordinary five line-degree deficits,
# then decompose the coefficient at each repeated degree into irreducibles.
def integer_partitions(total,slots,minimum=0):
 if slots==0:
  if total==0:yield ()
  return
 for a in range(minimum,total//slots+1):
  for rest in integer_partitions(total-a,slots-1,a):yield (a,)+rest
@lru_cache(None)
def coefficient_types(rank,parity):
 allowed=[n for n,d,p in zip(NAMES,DIMS,PARITY)if d<=rank and p==parity]
 out=[]
 def go(k,left,row):
  if k==len(allowed):
   if left==0:out.append(tuple(row))
   return
  n=allowed[k];d=DIMS[NAMES.index(n)]
  for copies in range(left//d+1):go(k+1,left-copies*d,row+[n]*copies)
 go(0,rank,[])
 return tuple(out)

def endpoint_shapes(degree):
 deficit=-25-degree
 out=[]
 for ordinary in integer_partitions(deficit,5):
  choices=[]
  for delta,multiplicity in sorted(Counter(ordinary).items()):
   e=-5-delta
   parity=(e+(MUT=='endpoint-parity'))%2
   choices.append([tuple((e,n)for n in rs)for rs in coefficient_types(multiplicity,parity)])
  for pieces in product(*choices):out.append(tuple(sorted(sum(pieces,()))))
 check(len(out)==len(set(out)),'endpoint shapes are unique')
 for s in out:
  check(sum(DIMS[NAMES.index(n)]for e,n in s)==5,'endpoint rank')
  check(sum(e*DIMS[NAMES.index(n)]for e,n in s)==degree,'endpoint degree')
  check(all(degree+20<=e<=-5 and PARITY[NAMES.index(n)]==e%2 for e,n in s),'intrinsic endpoint bounds and parity')
 return sorted(out)

M3=rep(**{"W'":3,'S4':3,'T6':6})
M4=rep(V=2,P=4,D=3)
M2=rep(A=1,V=2,P=3,D=4)
H=rep(A=2,V=2,P=2,D=2)
@lru_cache(None)
def E(t):return sub(tensor(M3,line(t-1)),tensor(M4,line(t)))
@lru_cache(None)
def Qstar(t):return sub(tensor(M3,line(t-1)),tensor(M2,line(t)))
@lru_cache(None)
def Q(t):return sub(tensor(H,line(t)),E(t))


def derive():
 sources=json.loads((ROOT/'INPUTS.json').read_text())
 check(len(sources)==4 and {Path(z['file']).name for z in sources}==set(SOURCE_HASHES),'four complete fixed source names')
 for item in sources:
  raw=(ROOT/item['file']).read_bytes()
  name=Path(item['file']).name
  check(item['sha256']==SOURCE_HASHES[name],'fixed immutable source hash')
  check(item['ref']=='db51525015bb7c5e825833d550d08dedf6f6ea96','fixed original commit')
  check(item['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+item['ref']+'/'+item['path'],'verified source URL')
  digest=item['sha256'] if MUT!='source-hash' else '0'*64
  check(hashlib.sha256(raw).hexdigest()==digest,'source SHA256')
  check(len(raw)==item['bytes'],'source byte count')
  check(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob_sha1'],'source Git blob')
 check(sum(SIZES)==120 and sum(x*x for x in DIMS)==120,'group and complete irreducible dimensions')
 for i,n in enumerate(NAMES):
  check(C[n][0]==q(DIMS[i]) and C[n][1]==q(DIMS[i]*(-1)**PARITY[i]),'dimension and central sign')
  for j,m in enumerate(NAMES):check(inner(C[n],C[m])==q(i==j),'character orthogonality')
 check(C['A']==tuple(sym(2,x)for x in TRACES)and C['A']!=C['V'],'fixed physical A=Sym2 W, not V')
 check(tensor(C['W'],C['W'])==add(C['1'],C['A']),'physical W square')
 check(tensor(C['W'],C["W'"])==C['P'],'physical W W-prime')
 check(sub(sub(tensor(C['W'],M3),M2),M4)==H,'actual ambient Koszul character')
 check(M3[0]==q(54)and M4[0]==q(37)and M2[0]==q(41),'actual presentation dimensions not swapped')
 check(E(2)==mult(-1,C['V']),'direct actual chi E(2)')
 check(Qstar(3)==rep(T6=1,W=-2,S4=-1),'direct actual chi Qstar(3)')
 for t in range(-18,13):check(Q(t)==mult(-1,Qstar(-t-2)),'ambient quotient and actual dual presentation agree')
 check(line(-2)==mult(-1,C['1'])and line(-3)==mult(-1,C['W']),'line H1 corrections')
 # Affine polynomial identity in 1,a,c1,delta1,...,delta4, independently derived.
 unit=lambda i:tuple(int(i==j)for j in range(7))
 padd=lambda *ps:tuple(sum(p[j]for p in ps)for j in range(7))
 pscale=lambda k,p:tuple(k*x for x in p)
 cs=[unit(2)]
 for j in range(4):cs.append(padd(cs[-1],pscale(8,unit(0)),unit(j+3)))
 es=padd(unit(1),*cs[:3]);bs=padd(unit(1),*cs)
 endpoint_identity=padd(pscale(2,unit(1)),pscale(3,bs),pscale(-5,es))
 weights=[2,4,6,3]
 if MUT=='defect-weight':weights[0]=1
 check(endpoint_identity==(120,0,0,*weights),'symbolic rank4 ordered(3,2) endpoint identity')
 bound=2*((-5*5)//2)
 check(bound==-26,'rank-five persistence and determinant parity')
 slack=2*bound+3*bound-(-150)
 check(slack==20 and min(weights)*12>slack,'invariant-divisor gap forces every defect zero')
 # Complete solutions to 4u+6v=20, since both degree endpoints are even.
 endpoints=[(-26-2*u,-26-2*v)for u in range(slack//4+1)for v in range(slack//6+1)if 4*u+6*v==slack]
 endpoints.sort()
 check(endpoints==[(-36,-26),(-30,-30)],'all endpoint alternatives')
 # Laurent-polynomial formal K-class, not a test of Euler faithfulness.
 lower=Counter({-4:1,-2:1,0:1})
 upper=Counter({2:1,4:1})
 shift=-5 if MUT=='K-twist' else -6
 cancel=Counter(lower)
 for e,c in upper.items():cancel[e+shift]-=c
 check({e:c for e,c in cancel.items()if c}=={0:1},'exact graded K-class eliminates other four blocks')
 # Dual sequence: D2/D1=L4*=B*(-2), so twist3 produces B*(1).
 dual_twist=-1 if MUT=='dual-twist'else -2
 check(dual_twist+3==1 and -(dual_twist+3)-2==-3,'dual quotient and Serre twist')
 rows=[]
 for a,b in endpoints:
  c1=(-54-a-24)//3
  degrees=[c1+8*i for i in range(5)]
  check(a+sum(degrees[:3])==-54 and a+sum(degrees)==b,'central E and endpoint degree sums')
  aa=endpoint_shapes(a);dd=endpoint_shapes(b)
  check((len(aa),len(dd))==({-36:(44,4),-30:(15,15)}[a]),'independent complete endpoint counts')
  survivors=[]
  for f,d in product(aa,dd):
   def B(t):
    source=Qstar(t)if MUT=='source-dual-swap'else E(t)
    return add(source,mult(-1,chi(f,t)),mult(-1,Q(t-6)),chi(dual(d),t-6))
   residuals=[sub(add(B(t+2),B(t+4),chi(dual(d),t)),Q(t))for t in(0,1)]
   passes=all(r==ZERO for r in residuals)
   if MUT=='dimensions-only':passes=all(r[0]==q(0)for r in residuals)
   if not passes:continue
   f2tail=sub(B(2),E(2))
   d1tail=sub(mult(-1,B(-3)),Qstar(3))
   # In fact each tail separately must be genuine by vanishing at i+d=4.
   necessary=[positive(f2tail),positive(d1tail)]
   survivors.append({'F0':shape_json(f),'D0':shape_json(d),'minus_chi_F2_2':show(f2tail),'minus_chi_D1_3':show(d1tail),'genuine':necessary})
  check(len(survivors)==(4 if a==-36 else 10),'exact two-Euler necessary survivor count')
  check(not any(all(x['genuine'])for x in survivors),'every necessary survivor violates persistence positivity')
  rows.append({'endpoints':[a,b],'graded_degrees':degrees,'ordinary_endpoint_degree_windows':[[a+20,-5],[b+20,-5]],'endpoint_counts':[len(aa),len(dd)],'initial_pairs':len(aa)*len(dd),'Euler_survivors':survivors,'survivor_count':len(survivors),'remaining_pairs':0})
 out={'status':'PASS','scope':'Conditional exclusion only of ordered maximal generic-rank-four plateau (3,2).',
      'method':'Independent ordinary-deficit partitions and exact conjugacy-class arithmetic, no author-code imports.',
      'plateau_ranks':[5,9,13,17,21,25],'central_index':3,'dual_central_index':2,
      'defect_weights':weights,'endpoint_bound':bound,'slack':slack,'minimum_positive_defect_cost':min(weights)*12,
      'K_identity':'[B]=[E]-[F0]-[Q(-6)]+[D0*(-6)]','Euler_tests':'chi(B(t+2))+chi(B(t+4))+chi(D0*(t))=chi(Q(t)), t=0,1, necessary only',
      'necessary_positivity':['-chi F2(2)=chi B(2)-chi E(2)','-chi D1(3)=-chi B(-3)-chi Q*(3)'],
      'cases':rows,'checks':CHECKS,'actual_instance_evaluations':0,'historical_enumerations':0,'source_Z_assumed':False}
 return out
if __name__=='__main__':print(json.dumps(derive(),indent=2,sort_keys=True))
