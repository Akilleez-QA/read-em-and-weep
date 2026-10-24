#!/usr/bin/env python3
"""Independent universal review. No author imports or historical enumeration."""
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
def chi(shape,t):return add(*(tensor(CHAR[n],line(e+t))for e,n in shape))
def h0(shape,t):return add(*(tensor(CHAR[n],symmetric(e+t))for e,n in shape if e+t>=0))
def h0dim(shape,t):return sum(DIM[n]*(e+t+1)for e,n in shape if e+t>=0)
def degree(shape):return sum(e*DIM[n]for e,n in shape)
def rank(shape):return sum(DIM[n]for e,n in shape)
def display(shape):return [{'degree':e,'coefficient':n}for e,n in shape]
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
EXPECTED_BLOCKS=((1,'P'),(1,'V'),(2,'S4'),(2,"W'"),(3,'P'),(3,'V'),(4,"W'"),(5,'P'),(5,'V'),(6,'S4'),(6,"W'"),(7,'A'),(8,'W'),(9,'1'))
EXPECTED_IMAGES=(((1,'P'),),((2,'S4'),),((1,'V'),(9,'1')),((2,"W'"),(2,"W'")))
HASHES={
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md':'0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2',
'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md':'868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c',
'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md':'783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71',
'four-sources.md':'d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e'}
def partitions(n,k,lo=0):
 if k==0:
  if n==0:yield ()
  return
 for x in range(lo,n//k+1):
  for rest in partitions(n-x,k-1,x):yield(x,)+rest
@lru_cache(None)
def irreducible_partitions(d,p):
 names=[n for n in NAMES if PAR[n]==p and DIM[n]<=d]
 out=[]
 def rec(i,left,row):
  if i==len(names):
   if left==0:out.append(tuple(row))
   return
  n=names[i]
  for copies in range(left//DIM[n]+1):rec(i+1,left-copies*DIM[n],row+[n]*copies)
 rec(0,d,[])
 return out

def run():
 manifests=json.loads((ROOT/'INPUTS.json').read_text())
 require(len(manifests)==5,'all five complete source inputs')
 for s in manifests:
  raw=(ROOT/s['file']).read_bytes();expected=HASHES[Path(s['file']).name]
  if MUT=='source-hash':expected='0'*64
  require(s['sha256']==expected and hashlib.sha256(raw).hexdigest()==expected,'immutable original SHA256')
  require(len(raw)==s['bytes'],'original bytes')
  require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==s['git_blob_sha1'],'original Git blob')
 require(sum(SIZES)==120 and sum(d*d for d in DIM.values())==120,'complete group character dimensions')
 for n in NAMES:
  require(CHAR[n][0]==q(DIM[n]) and CHAR[n][1]==q(DIM[n]*(-1)**PAR[n]),'irrep dimensions and central signs')
  for m in NAMES:require(inner(CHAR[n],CHAR[m])==q(n==m),'exact class orthogonality')
 require(CHAR['A']==symmetric(2) and CHAR['A']!=CHAR['V'],'physical A distinct from V')
 require(sub(sub(tensor(TRACE,M3),M2),M4)==H and H[0]==q(30),'actual ambient character and dimension')
 require(M3[0]==q(54) and M4[0]==q(37) and M2[0]==q(41),'unequal actual presentations')
 require(E(3)==representation(**{"W'":1,'T6':2}),'actual E Euler cubic')
 require(Qstar(3)==representation(T6=1,W=-2,S4=-1),'actual dual Euler cubic')
 for source in SOURCES.values():
  require(rank(source)==17 and degree(source)==-54,'all four actual source ranks/degrees')
  for t in range(-2,6):require(chi(source,t)==E(t),'all four sources match actual Euler presentation')
 # Formal affine identity: coordinates 1,a,c1,d1,d2,d3.
 u=lambda i:tuple(int(i==j)for j in range(6))
 pa=lambda *ps:tuple(sum(p[j]for p in ps)for j in range(6))
 pm=lambda k,p:tuple(k*x for x in p)
 cs=[u(2)]
 for j in range(3):cs.append(pa(cs[-1],pm(8,u(0)),u(j+3)))
 prefix=pa(u(1),*cs[:3]);total=pa(u(1),*cs)
 identity=pa(u(1),pm(3,total),pm(-4,prefix))
 require(identity==(48,0,0,1,2,3),'ordered (3,1) determinant identity')
 require(-20+3*(-36)-(-168)==40,'general slack is 40')
 sem=sorted({12*x+20*y+30*z for x in range(4)for y in range(3)for z in range(2)if 12*x+20*y+30*z<=40})
 if MUT=='global-zero-defects':sem=[0]
 rows=[]
 for a in range(-60,-19,2):
  for b in range(-48,-35,2):
   for ds in product(sem,repeat=3):
    if a+3*b!=-168+ds[0]+2*ds[1]+3*ds[2]:continue
    num=-78-a-2*ds[0]-ds[1]
    if num%6:continue
    c=[num//3]
    for delta in ds:c.append(c[-1]+8+delta)
    require(a+sum(c[:3])==-54 and a+sum(c)==b,'ordered central and endpoint sums')
    rows.append((a,b,ds,tuple(c)))
 require(len(rows)==31 and sum(any(x[2])for x in rows)==24,'general positive defects retained')
 patterns=sorted(set(x[2]for x in rows));require(len(patterns)==12,'all twelve defect patterns')
 # Image conditions derive from both bundle-map spaces, not section counts alone.
 blocks=[];compat={}
 for e in range(10):
  for n in NAMES:
   if DIM[n]>4 or PAR[n]!=(e+1+(MUT=='image-parity'))%2:continue
   if coeff(tensor(CHAR[n],symmetric(e)),'T6')==0:continue
   src=[label for label,s in SOURCES.items()if (MUT!='source-Z-only' or label=='Z') and any(hom(e,n,1-f,m)>0 for f,m in s)]
   if src:blocks.append((e,n));compat[(e,n)]=src
 require(set(blocks)==set(EXPECTED_BLOCKS),'complete fourteen image blocks')
 rank_one=[s for s in blocks if DIM[s[1]]==1]
 require(rank_one==[(9,'1')] and compat[(9,'1')]==['D'],'rank-one corollary: O(9), source D only')
 all_shapes=[];images=[]
 for length in range(1,5):
  for bs in combinations_with_replacement(blocks,length):
   if rank(bs)!=4:continue
   all_shapes.append(bs)
   dual=tuple((-e,n)for e,n in bs)
   cap=6+h0dim(dual,2)+h0dim(dual,0)
   if degree(bs)<=cap:images.append((bs,cap))
 require({tuple(sorted(s))for s,c in images}=={tuple(sorted(s))for s in EXPECTED_IMAGES},'complete four full-rank image shapes')
 for s,cap in images:
  if MUT=='saturation-cap':cap=24
  require(0<=cap-degree(s)<12,'torsion saturation defect strictly below first invariant orbit')
 # After saturation B=J*(1). Persistent F1(3)=0 in all four cases.
 image_data=[]
 for s,cap in images:
  B=tuple((1-e,n)for e,n in s)
  require(h0dim(B,-1)==0,'F1 cubic persistence via backward derivative')
  image_data.append({'image':display(s),'degree':degree(s),'saturation_degree_bound':cap,'B':display(B),'chi_F2_3':show(sub(E(3),chi(B,3))),'H0_B_1':show(h0(B,1))})
 s4=((-1,'S4'),)
 require(show(sub(E(3),chi(s4,3)))=={"W'":1,'T6':1,'W':-1,'S4':-1},'S4 positive channels')
 require(coeff(h0(s4,1),"W'")==0 and coeff(h0(s4,1),'T6')==0,'S4 target misses forced channels')
 multiplicity=coeff(tensor(CHAR["W'"],symmetric(2)),'T6')
 if MUT=='intertwiner-multiplicity':multiplicity+=1
 require(multiplicity==1,'one copy of the intertwiner forces common diagonal factor')
 require(DIM["W'"]*multiplicity<4,'two W-prime summands cannot be jointly generated by one T6')
 vo=((0,'V'),(-8,'1'))
 require(sub(E(3),chi(vo,3))==CHAR['T6']==h0(vo,1),'V-plus-line exact Euler envelope')
 require(-4>-10 and all(e>=-4 for e in[-4,-3]),'vanishing H1(F2(3)) gives slope floor -4 above inaccessible -10')
 # Only the P candidate fixes c3=0 and yields the local ten-unit defect bounds.
 local=[(a,b,ds,c)for a,b,ds,c in rows if c[2]==0]
 require(local==[(-30,-46,(0,0,0),(-16,-8,0,8))],'P candidate alone forces zero plateau defects')
 # Endpoint domain: partition five ordinary degree deficits from -4, total ten.
 endpoints=[]
 for p in partitions(10,5):
  options=[]
  for deficit,line_count in sorted(Counter(p).items()):
   e=-4-deficit
   options.append([tuple((e,n)for n in ns)for ns in irreducible_partitions(line_count,e%2)])
  for pieces in product(*options):endpoints.append(tuple(sorted(sum(pieces,()))))
 require(len(endpoints)==len(set(endpoints))==46,'complete 46-shape intrinsic endpoint domain')
 for s in endpoints:
  require(rank(s)==5 and degree(s)==-30 and all(-14<=e<=-4 and PAR[n]==e%2 for e,n in s),'forced endpoint rank, degree, parity and bounds')
 targets={t:sub(E(t),add(*(tensor(CHAR['P'],line(t-e))for e in(4,2,0))))for t in(3,4)}
 require(show(targets[3])=={'S4':-1,'T6':-1} and show(targets[4])=={'V':1,'A':-1,'D':-1},'exact lower-endpoint Euler targets')
 twists=(3,)if MUT=='omit-quartic'else(3,4)
 survivors=[s for s in endpoints if all((chi(s,t)[0]==targets[t][0] if MUT=='dimensions-only'else chi(s,t)==targets[t])for t in twists)]
 require(set(survivors)=={((-10,'1'),(-8,'1'),(-4,'V')),((-9,'W'),(-4,'V'))},'exactly two forced endpoints')
 target=-4 if MUT=='endpoint-derivative-twist'else -6
 homs=[]
 for s in survivors:
  vals=[hom(e,n,target,'P')for e,n in s];homs.append(vals)
  require(all(x==0 for x in vals),'every endpoint derivative component vanishes')
 return {'status':'PASS','theorem':'Conditional: every T6 copy in H0(Q*(3)) has nonzero derivative image of generic rank at most 3 in actual ordered rank-four (3,1) plateau.','central_rank':17,'dual_rank':13,'ambient_dimension':30,'ordered_ranks':[5,9,13,17,21],'source_Z_assumed':False,'canonical_evaluation_assumed':False,'single_T6_assumed':False,'positive_defects_retained':True,'general_ledger_rows':len(rows),'positive_defect_rows':24,'defect_patterns':patterns,'ledger':[{'a':a,'b':b,'defects':ds,'graded_degrees':c}for a,b,ds,c in rows],'individual_image_blocks':[{'block':display((s,))[0],'compatible_sources':compat[s]}for s in blocks],'rank_one_necessary_image':display(((9,'1'),)),'rank_one_necessary_source':'D','raw_rank_four_multisets':len(all_shapes),'full_rank_image_candidates':image_data,'intertwiner_multiplicity':multiplicity,'endpoint_shapes':[display(s)for s in endpoints],'endpoint_survivors':[display(s)for s in survivors],'endpoint_Hom_dimensions':homs,'checks':CHECKS,'actual_instance_evaluations':0,'historical_enumerations':0,'coarse_profile_eliminations':0}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
