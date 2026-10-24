#!/usr/bin/env python3
"""Independent lower-image review. Exact characters; no author-code imports."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from collections import Counter
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parent
MUT=sys.argv[1] if len(sys.argv)>1 else ''
CHECKS=0
def require(x,msg):
 global CHECKS
 CHECKS+=1
 if not x:raise RuntimeError(msg)
def q(a,b=0):return F(a),F(b)
def qa(x,y):return x[0]+y[0],x[1]+y[1]
def qs(k,x):return k*x[0],k*x[1]
def qm(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def qr(x,y):return qa(x,qs(-1,y))
SIZES=(1,1,12,12,12,12,20,20,30)
TRACE=(q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0))
NAMES=('1','W','A','S4','D','T6','P',"W'",'V')
DIM=dict(zip(NAMES,(1,2,3,4,5,6,4,2,3)))
PAR=dict(zip(NAMES,(0,1,0,1,0,1,0,1,0)))
ZERO=(q(0),)*9
def add(*args):return tuple((sum(x[i][0]for x in args),sum(x[i][1]for x in args))for i in range(9))
def mul(k,x):return tuple(qs(k,v)for v in x)
def sub(x,y):return add(x,mul(-1,y))
@lru_cache(None)
def tensor(x,y):return tuple(qm(a,b)for a,b in zip(x,y))
@lru_cache(None)
def symmetric(n):
 old,now=ZERO,(q(1),)*9
 for _ in range(n):old,now=now,sub(tensor(TRACE,now),old)
 return now
CHAR={n:symmetric(i)for i,n in enumerate(NAMES[:6])}
CHAR['P']=tuple(q(x)for x in(4,4,-1,-1,-1,-1,1,1,0))
CHAR['V']=sub(symmetric(6),CHAR['P'])
CHAR["W'"]=sub(tensor(TRACE,CHAR['P']),CHAR['T6'])
if MUT=='physical-marking':CHAR['A'],CHAR['V']=CHAR['V'],CHAR['A']
def inner(x,y):
 result=q(0)
 for size,a,b in zip(SIZES,x,y):result=qa(result,qs(F(size,120),qm(a,b)))
 return result
@lru_cache(None)
def dec(x):
 ans=[]
 for n in NAMES:
  a,b=inner(x,CHAR[n]);require(b==0 and a.denominator==1,'integral class decomposition')
  ans.append(int(a))
 return tuple(ans)
def coeff(x,n):return dec(x)[NAMES.index(n)]
def show(x):return {n:v for n,v in zip(NAMES,dec(x))if v}
def representation(**kw):return add(*(mul(k,CHAR[n])for n,k in kw.items()))
@lru_cache(None)
def line(n):
 if n>=0:return symmetric(n)
 if n==-1 or MUT=='omit-H1':return ZERO
 return mul(-1,symmetric(-n-2))
@lru_cache(None)
def chi(shape,t):return add(*(tensor(CHAR[n],line(e+t))for e,n in shape))
@lru_cache(None)
def h0(shape,t):return add(*(tensor(CHAR[n],symmetric(e+t))for e,n in shape if e+t>=0))
def h0dim(shape,t):return sum(DIM[n]*(e+t+1)for e,n in shape if e+t>=0)
def degree(shape):return sum(e*DIM[n]for e,n in shape)
def rank(shape):return sum(DIM[n]for e,n in shape)
def display(shape):return [{'degree':e,'coefficient':n}for e,n in shape]
@lru_cache(None)
def hom(e,n,f,m):
 exponent=f-e
 if MUT=='maps-vs-sections':exponent=f+e
 if exponent<0:return 0
 return coeff(tensor(CHAR[m],symmetric(exponent)),n)
M2=representation(A=1,V=2,P=3,D=4)
M3=representation(**{"W'":3,'S4':3,'T6':6})
M4=representation(V=2,P=4,D=3)
H=representation(A=2,V=2,P=2,D=2)
def E(t):return sub(tensor(M3,line(t-1)),tensor(M2 if MUT=='source-dual-swap'else M4,line(t)))
def Qstar(t):return sub(tensor(M3,line(t-1)),tensor(M2,line(t)))
SOURCES={
'D':((-2,'D'),(-3,"W'"),(-3,'T6'),(-4,'V'),(-8,'1')),
'P':((-2,'P'),(-3,"W'"),(-3,'T6'),(-4,'V'),(-5,"W'")),
'V':((-2,'V'),(-3,"W'"),(-3,'T6'),(-4,'V'),(-4,'V')),
'Z':((-3,"W'"),(-3,'T6'),(-3,'T6'),(-4,'V'))}
HASHES={
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md':'0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2',
'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md':'868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c',
'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md':'783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71',
'four-sources.md':'d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e',
'EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md':'9f01d086401ee7ee850d3c9181c0486734bcc5c5791c552410895ae4ba742fbf'}
QS=(
 ((3,'T6'),(4,'V'),(6,'1'),(6,'A')),
 ((3,'T6'),(4,'V'),(5,'W'),(7,'W')),
 ((3,'T6'),(4,'V'),(5,'W'),(6,'1'),(8,'1')),
 ((3,'T6'),(4,'V'),(4,'1'),(6,'1'),(7,'W')),
 ((3,'T6'),(4,'V'),(4,'1'),(6,'1'),(6,'1'),(8,'1')))
def genuine(x):return all(v>=0 for v in dec(x))
@lru_cache(None)
def envelope(s):return add(chi(s,3),h0(s,1),ZERO if MUT=='omit-second-backstep'else h0(s,-1))
def shapes(r,d,cap):
 lo=d-(r-1)*cap
 blocks=[(e,n)for e in range(lo,cap+1)for n in NAMES if DIM[n]<=r and PAR[n]==e%2]
 for length in range(1,r+1):
  for s in combinations_with_replacement(blocks,length):
   if rank(s)==r and degree(s)==d:yield s

@lru_cache(None)
def coefficient_shapes(r,p):
 allowed=[n for n in NAMES if DIM[n]<=r and PAR[n]==p]
 out=[]
 def rec(i,left,current):
  if i==len(allowed):
   if left==0:out.append(tuple(current))
   return
  n=allowed[i]
  for k in range(left//DIM[n]+1):rec(i+1,left-k*DIM[n],current+[n]*k)
 rec(0,r,[])
 return out
@lru_cache(None)
def ordinary_shapes(r,d,cap):
 lo=d-(r-1)*cap
 out=[]
 for degrees in combinations_with_replacement(range(lo,cap+1),r):
  if sum(degrees)!=d:continue
  choices=[]
  for e,count in sorted(Counter(degrees).items()):
   choices.append([tuple((e,n)for n in ns)for ns in coefficient_shapes(count,e%2)])
  for pieces in product(*choices):out.append(tuple(sorted(sum(pieces,()))))
 return sorted(set(out))

def run():
 for item in json.loads((ROOT/'INPUTS.json').read_text()):
  name=Path(item['file']).name;raw=(ROOT/item['file']).read_bytes()
  require(hashlib.sha256(raw).hexdigest()==item['sha256']==('0'*64 if MUT=='source-hash'else HASHES[name]),'complete immutable source: '+name)
  require(len(raw)==item['bytes'],'original source bytes')
  require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob_sha1'],'original source Git blob')
 for n in NAMES:
  require(CHAR[n][0]==q(DIM[n])and CHAR[n][1]==q(DIM[n]*(-1)**PAR[n]),'physical dimensions and central signs')
  for m in NAMES:require(inner(CHAR[n],CHAR[m])==q(n==m),'character orthogonality')
 require(CHAR['A']==symmetric(2)and CHAR['A']!=CHAR['V'],'physical A/V distinction')
 require(E(3)==representation(**{"W'":1,'T6':2}),'actual E cubic Euler')
 require(Qstar(3)==representation(T6=1,W=-2,S4=-1),'actual unequal Qstar cubic Euler')
 require(sub(sub(tensor(TRACE,M3),M2),M4)==H and H[0]==q(30),'actual ambient thirty-space')
 for source in SOURCES.values():
  require(rank(source)==17 and degree(source)==-54,'four source ranks and degrees')
  for t in range(-2,6):require(chi(source,t)==E(t),'four source Euler classes')
 # Import the five necessary dual types as a theorem, not historical re-enumeration.
 for shape in QS:
  dual=tuple((-e,n)for e,n in shape)
  require(rank(dual)==13 and degree(dual)==-54 and h0(dual,2)==ZERO,'five imported dual types and persistence')
  for t in range(-2,6):require(chi(dual,t)==Qstar(t),'five imported dual types match actual presentation')
 require(max(e for s in QS for e,n in s)==8,'actual Q maximum degree eight')
 # Complete necessary degree ledger, derived anew without source enumeration.
 sem={12*x+20*y+30*z for x in range(4)for y in range(3)for z in range(2)if 12*x+20*y+30*z<=40}
 if MUT=='global-zero-defects':sem={0}
 ledger=[]
 for a in range(-60,-19,2):
  for b in range(-48,-35,2):
   for ds in product(sem,repeat=3):
    if a+3*b!=-168+ds[0]+2*ds[1]+3*ds[2]:continue
    num=-78-a-2*ds[0]-ds[1]
    if num%6:continue
    cs=[num//3]
    for delta in ds:cs.append(cs[-1]+8+delta)
    ledger.append((a,b,tuple(ds),tuple(cs)))
 ledger.sort();c3s=sorted({x[3][2]for x in ledger})
 require(len(ledger)==31 and sum(any(x[2])for x in ledger)==24,'all positive-defect degree rows retained')
 require(c3s==[-2,0,2,4,6,8,10],'complete first-quotient degree values')
 blocks=[]
 for e in range(10):
  for n in NAMES:
   if DIM[n]>4 or PAR[n]!=(e+1)%2 or coeff(tensor(CHAR[n],symmetric(e)),'T6')==0:continue
   if any(any(hom(e,n,1-f,m)>0 for f,m in s)for s in ([SOURCES['Z']]if MUT=='source-Z-only'else SOURCES.values())):blocks.append((e,n))
 require(len(blocks)==14,'complete source/target image blocks')
 image_lists={}
 for r in(2,3):
  images=[]
  for length in range(1,r+1):
   for s in combinations_with_replacement(blocks,length):
    if rank(s)!=r:continue
    if not any(all(any(hom(e,n,1-f,m)>0 for f,m in source)for e,n in s)for source in SOURCES.values()):continue
    if any(s.count(block)>coeff(tensor(CHAR[block[1]],symmetric(block[0])),'T6')for block in set(s)):continue
    images.append(s)
  image_lists[r]=images
 require(len(image_lists[2])==4 and len(image_lists[3])==7,'complete low-image source domains')
 top2=max(sum(sorted([1-e for e,n in s for _ in range(DIM[n])],reverse=True)[:2])for s in SOURCES.values())
 require(top2==14,'ambient rank-two saturation degree bound')
 cap3=3+6-min(c3s)
 require(cap3==11,'rank-three saturation bound uses line kernel and ledger, not full annihilator identification')
 sat_images={2:[s for s in image_lists[2]if degree(s)<=top2],3:[s for s in image_lists[3]if degree(s)<=cap3]}
 require(sat_images[2]==[((2,"W'"),),((4,"W'"),),((6,"W'"),)],'three rank-two saturated image candidates')
 require(sat_images[3]==[((1,'V'),),((3,'V'),)],'two rank-three saturated image candidates')
 for r in(2,3):
  for s in sat_images[r]:require(0<=(top2 if r==2 else cap3)-degree(s)<12,'all remaining low images have zero invariant saturation torsion')
 # Kernel N in 0 -> N -> B -> C=S*(1) -> 0 embeds in Q(-2).
 cases=[];domains=[]
 for r in(2,3):
  for S in sat_images[r]:
   C=tuple((1-e,n)for e,n in S);h=0 if MUT=='full-annihilator-identification'else 4-r
   require(rank(C)+h==4,'lower image quotient needs its complementary kernel')
   degrees=[c-degree(C)for c in c3s]
   lo=min(degrees)-(h-1)*6
   ns=[]
   for d in degrees:
    if d>6*h:continue
    ns.extend(shapes(h,d,6))
   ns=sorted(set(ns));prefilter=len(ns);eligible=[]
   alternative=sorted(set(z for d in degrees if d<=6*h for z in ordinary_shapes(h,d,6)))
   require({tuple(sorted(x))for x in ns}==set(alternative),'independent complete N ordinary-degree domain')
   for N in ns:
    require(all(lo<=e<=6 for e,n in N),'derived complete N slope window')
    margin=sub(add(envelope(N),envelope(C)),E(3))
    if not (margin[0][0]>=0 if MUT=='dimensions-only'else genuine(margin)):continue
    qgood=[]
    for j,Q in enumerate(QS):
     if all(sum(hom(e,n,f-(1 if MUT=='dual-target-twist'else 2),m)for f,m in Q)>=(1 if MUT=='drop-target-multiplicity'else N.count((e,n)))for e,n in set(N)):qgood.append(j+1)
    if not qgood:continue
    # Actual equivariant Ext is invariants of ordinary H1(N tensor C*).
    ext=add(*(tensor(tensor(CHAR[n],CHAR[m]),symmetric(-e-f-1))for e,n in N for f,m in S if e+f-1<=-2))
    require((ext[0][0] if MUT=='ordinary-Ext-zero'else coeff(ext,'1'))==0,'equivariant extension splits only after invariant Ext calculation')
    B=tuple(sorted(N+C));c3=degree(B);lr=[row for row in ledger if row[3][2]==c3]
    require(lr and rank(B)==4,'actual first quotient has correct degree/rank')
    row={'image':display(S),'N':display(N),'C':display(C),'B':display(B),'c3':c3,'Q_types':qgood,'section_margin':show(margin),'ordinary_Ext':show(ext),'equivariant_Ext_dimension':coeff(ext,'1'),'ledger_rows':[{'a':a,'b':b,'defects':ds,'graded_degrees':cs}for a,b,ds,cs in lr]}
    eligible.append(row);cases.append((S,N,B,lr,row))
   domains.append({'image':display(S),'N_min_degree':lo,'N_max_degree':6,'initial_shapes':prefilter,'all_N_shapes':[display(z)for z in ns],'survivor_count':len(eligible),'survivors':eligible})
 require([d['survivor_count']for d in domains]==[9,6,3,3,2],'complete section-and-target kernel lists')
 require(len(cases)==23,'all twenty-three split preliminary cases')
 require(show(sub(add(envelope(((2,'1'),)),envelope(((0,'V'),))),E(3)))=={'W':1,'S4':2,'T6':1},'exact two-backstep envelope retains both section contributions')
 # Only low c3 cases can be removed using forced lower unramifiedness.
 final=[];eliminated=[]
 for S,N,B,lr,row in cases:
  c3=degree(B)
  if c3>0:final.append(row);continue
  require(c3 in(-2,0),'only two low degrees occur')
  require(all((not any(ds))if MUT=='low-branch-all-zero'else ds[0]==ds[1]==0 for a,b,ds,cs in lr),'low degree forces only lower two derivatives unramified')
  require(len({a for a,b,ds,cs in lr})==1,'unique lower endpoint degree in low branch')
  a=lr[0][0];es=list(shapes(5,a,-4))
  require({tuple(sorted(x))for x in es}==set(ordinary_shapes(5,a,-4)),'independent complete lower endpoint ordinary-degree domain')
  def bottom(t):return sub(E(t),add(*(chi(B,t-j)for j in(0,2,4))))
  good=[s for s in es if all(chi(s,t)==bottom(t)for t in((3,)if MUT=='omit-quartic'else(3,4)))]
  homs=[]
  for s in good:
   value=sum(hom(e,n,f-(4 if MUT=='endpoint-derivative-twist'else 6),m)for e,n in s for f,m in B)
   homs.append(value);require(value==0,'low-case endpoint derivative Hom vanishes')
  eliminated.append({'image':display(S),'N':display(N),'c3':c3,'lower_endpoint_degree':a,'endpoint_domain_count':len(es),'chi_endpoint_3':show(bottom(3)),'chi_endpoint_4':show(bottom(4)),'endpoint_survivors':[display(s)for s in good],'endpoint_Hom_dimensions':homs})
 require(len(final)==13 and len(eliminated)==10,'thirteen remaining necessary B cases, ten removed low cases')
 require(sum(len(x['image'])==1 and x['image'][0]['coefficient']=='V' for x in final)==3,'three rank-three cases')
 # Actual inverse-image filtrations split each determinant defect into two
 # invariant torsion lengths, without splitting the lower bundle extensions.
 case_rows=[];torsion_rows=[]
 for case in final:
  S=tuple((z['degree'],z['coefficient'])for z in case['image'])
  N=tuple((z['degree'],z['coefficient'])for z in case['N'])
  r=rank(S);h=rank(N);p=r-degree(S);n=degree(N)
  for row in case['ledger_rows']:
   d1,d2,d3=row['defects'];cs=row['graded_degrees']
   require(d3==0,'all surviving lower-image cases force only upper defect zero')
   case_rows.append({'image':case['image'],'N':case['N'],**row})
   def parts(delta):
    if MUT=='force-torsion-into-N':return [(delta,0)]
    allowed=range(0,delta+1,2)if MUT=='allow-even-torsion'else sorted(sem)
    return [(x,delta-x)for x in allowed if delta-x in allowed]
   for (nu1,tau1),(nu2,tau2)in product(parts(d1),parts(d2)):
    require(all(x in sem for x in(nu1,tau1,nu2,tau2)),'each subquotient torsion length is an invariant effective divisor')
    shift=1 if MUT=='inverse-image-twist'else 2
    nd=(n-2*shift*h-nu1-nu2,n-shift*h-nu2,n)
    cd=(p-2*shift*r-tau1-tau2,p-shift*r-tau2,p)
    require(tuple(nd[i]+cd[i]for i in range(3))==tuple(cs[:3]),'inverse-image degree additivity reproduces full graded degrees')
    require(nu1+tau1==d1 and nu2+tau2==d2,'snake-lemma torsion lengths add')
    torsion_rows.append({'image':case['image'],'N':case['N'],**row,'nu':[nu1,nu2],'tau':[tau1,tau2],'N_degrees':nd,'C_degrees':cd})
 require(len(case_rows)==50 and sum(any(x['defects'])for x in case_rows)==37,'complete fifty case-degree rows retain thirty-seven positive defects')
 require(len(torsion_rows)==96 and sum(any(x['defects'])for x in torsion_rows)==83,'complete ninety-six torsion partitions retain eighty-three positive defects')
 return {'status':'PASS','scope':'Necessary lower-image and split first-quotient classification only; no full (3,1) exclusion.','checks':CHECKS,'original_sources':6,'ledger_rows':31,'positive_defect_rows':24,'c3_values':c3s,'rank_two_saturation_degree_bound':top2,'rank_three_saturation_degree_bound':cap3,'raw_rank_two_images':[display(s)for s in image_lists[2]],'raw_rank_three_images':[display(s)for s in image_lists[3]],'kernel_domains':domains,'preliminary_split_case_count':len(cases),'eliminated_low_cases':eliminated,'final_necessary_cases':final,'final_case_count':13,'case_degree_rows':case_rows,'case_degree_row_count':len(case_rows),'torsion_partition_rows':torsion_rows,'torsion_partition_row_count':len(torsion_rows),'nontrivial_ordinary_Ext_cases':[row for S,N,B,lr,row in cases if row['ordinary_Ext']],'actual_instance_evaluations':0,'historical_enumerations':0,'full_image_annihilator_equated_to_lower_image':False,'globally_zero_defects_assumed':False}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
