#!/usr/bin/env python3
"""Independent rank-one image review. Exact characters; no author-code imports."""
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
def envelope(s):return add(chi(s,3),h0(s,1),h0(s,-1))
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

def independent_rank_three():
 # Exhaustive coefficient families in rank three: 1+1+1, 1+2, or 3.
 out=set()
 for es in combinations_with_replacement(range(-6,7,2),3):
  if sum(es)in range(6,19,2):out.add(tuple((e,'1')for e in es))
 for e in range(-6,7,2):
  for f in range(-5,6,2):
   for n in('W',"W'"):
    if e+2*f in range(6,19,2):out.add(tuple(sorted(((e,'1'),(f,n)))))
 for e in range(-6,7,2):
  for n in('A','V'):
   if 3*e in range(6,19,2):out.add(((e,n),))
 return sorted(out)
def targets(N):
 out=[]
 for index,Q in enumerate(QS,1):
  okay=True
  for block,multiplicity in Counter(N).items():
   e,n=block
   bound=sum(hom(e,n,f-(0 if MUT=='target-twist'else 2),m)for f,m in Q)
   if bound<(1 if MUT=='ignore-multiplicity'else multiplicity):okay=False
  if okay:out.append(index)
 return out

def run():
 for item in json.loads((ROOT/'INPUTS.json').read_text()):
  name=Path(item['file']).name;raw=(ROOT/item['file']).read_bytes()
  require(hashlib.sha256(raw).hexdigest()==item['sha256']==('0'*64 if MUT=='source-hash'else HASHES[name]),'complete frozen original '+name)
  require(len(raw)==item['bytes'],'original byte count')
 for n in NAMES:
  require(CHAR[n][0]==q(DIM[n])and CHAR[n][1]==q(DIM[n]*(-1)**PAR[n]),'physical dimension and central sign')
  for m in NAMES:require(inner(CHAR[n],CHAR[m])==q(n==m),'character orthogonality')
 require(CHAR['A']==symmetric(2)and CHAR['V']!=CHAR['A'],'physical marking')
 require(E(3)==representation(**{"W'":1,'T6':2}),'actual unequal E cubic Euler')
 require(show(Qstar(4))=={'1':-1,'A':-1,'D':1,'P':1,'V':2},'actual dual quartic Euler')
 require(line(-5)==mul(-1,CHAR['S4']),'negative scalar quotient contributes -S4, not zero')
 max_source=max(1-e for source in SOURCES.values()for e,n in source)
 require(max_source==9,'sharp rank-one image saturation bound')
 image_degrees=[e for e in range(10)if e%2==1 and coeff(symmetric(e),'T6')>0 and any(any(hom(e,'1',1-f,n)>0 for f,n in source)for source in SOURCES.values())]
 require(image_degrees==[9],'complete odd line-image degree domain leaves only nine')
 eligible=[label for label,source in SOURCES.items()if any(hom(9,'1',1-e,n)>0 for e,n in source)]
 require(eligible==['D'],'rank-one O9 image requires D, not source Z')
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
 require(len(ledger)==31 and sum(any(x[2])for x in ledger)==24,'complete thirty-one-row ramified ledger')
 require(c3s==[-2,0,2,4,6,8,10],'complete c3 range')
 require(min(c3s)+8-2*6==-6,'intrinsic rank-three ordinary lower bound')
 domain=independent_rank_three()
 if MUT=='omit-case':domain=domain[:-1]
 alternate=sorted(set(s for d in range(6,19,2)for s in ordinary_shapes(3,d,6)))
 require(domain==alternate and len(domain)==53,'complete rank-three domain by independent coefficient families and ordinary partitions')
 C=((-7 if MUT=='scalar-quotient-twist'else -8,'1'),)
 require(rank(C)==1 and degree(C)==-8,'genuine rank-one quotient is O(-8)')
 require(envelope(C)==mul(-1,CHAR['S4']),'all negative scalar quotient section terms included')
 records=[];lows=[];highs=[]
 for N in domain:
  B=tuple(sorted(N+C));d=degree(B)
  require(rank(N)==3 and rank(B)==4 and degree(N)==d+8,'rank and degree of genuine complementary kernel')
  require(all(-6<=e<=6 for e,n in N),'proved N slope window')
  ext=add(*(tensor(CHAR[n],symmetric(-e-10))for e,n in N if e+8<=-2))
  require(ext==ZERO,'ordinary H1(N(8)) vanishes, hence equivariant extension splits')
  margin=sub(add(envelope(N),envelope(C)),E(3));ts=targets(N)
  passing=genuine(margin)and bool(ts)
  row={'N':display(N),'B':display(B),'c3':d,'section_margin':show(margin),'Q_targets':ts,'passes':passing}
  records.append(row)
  if not passing:continue
  rows=[x for x in ledger if x[3][2]==d]
  require(bool(rows),'every admitted kernel has numerical rows')
  if d<=0:
   require(d in(-2,0)and all(x[2][0]==x[2][1]==0 for x in rows),'only lower defects vanish in low branch')
   a=-24 if d==-2 else -30
   require(all(x[0]==a for x in rows),'lower endpoint degree')
   endpoints=sorted(shapes(5,a,-4))
   require(endpoints==ordinary_shapes(5,a,-4),'two complete endpoint domains agree')
   require(len(endpoints)==(13 if d==-2 else 46),'rank-five endpoint domain counts')
   bottom={t:sub(E(t),add(chi(B,t),chi(B,t-2),chi(B,t-4)))for t in(3,4)}
   survivors3=[s for s in endpoints if chi(s,3)==bottom[3]]
   survivors=[s for s in survivors3 if chi(s,4)==bottom[4]]
   require(not survivors3 and not survivors,'all seven low cases already fail cubic Euler alone')
   lows.append(dict(row,a=a,endpoint_domain=[display(s)for s in endpoints],chi_endpoint_3=show(bottom[3]),chi_endpoint_4=show(bottom[4]),cubic_survivors=[],joint_survivors=[],degree_rows=rows))
  else:
   require(all(x[2][2]==0 for x in rows),'upper defect vanishes only after positive c3 restriction')
   dual=tuple((-e,n)for e,n in B)
   q4=E(4)if MUT=='upper-source-swap'else Qstar(4)
   z4=sub(q4,chi(dual,1 if MUT=='upper-quotient-twist'else 2))
   target=h0(dual,2 if MUT=='upper-derivative-twist'else 0)
   source_v=coeff(z4,'V');target_v=coeff(target,'V')
   require(source_v==1 and target_v==0,'nine exact physical-V upper excesses')
   highs.append(dict(row,chi_Z4=show(z4),H0_B_dual=show(target),V_source=source_v,V_target=target_v,V_margin=source_v-target_v,degree_rows=rows))
 require(len(lows)==7 and len(highs)==9 and sum(x['passes']for x in records)==16,'complete fifty-three to sixteen to seven plus nine reduction')
 require(any(x[2][2]==12 for row in lows for x in row['degree_rows']),'ramified upper low-degree rows retained')
 require(any(any(x[2][:2])for row in highs for x in row['degree_rows']),'positive lower defects retained in upper obstruction')
 # The universal top-section kernel has strictly negative degree and zero internal derivative.
 cap=-3 if MUT=='weaken-top-bound'else -4
 require(cap+(-1 if MUT=='weaken-top-bound'else -2)-(-4)<0,'strict slope gap for maps K -> (Z/K)(-2)')
 require(DIM['V']*(-4)==-12,'forced horizontal top V summand has negative degree')
 for x in highs:require(x['V_source']==x['chi_Z4'].get('V',0)and x['V_target']==x['H0_B_dual'].get('V',0)and x['V_margin']==1,'reported multiplicities match exact characters')
 return {'status':'PASS','claim':'Conditional rank-one restricted-image exclusion, including direct derivation of O(9) and source D. Integration with other image-rank exclusions is separate.','checks':CHECKS,'counts':[53,16,7,9],'domain':records,'low_exclusions':lows,'upper_exclusions':highs,'complete_ledger_rows':31,'positive_ledger_rows':24,'top_kernel_degree':-12,'quartic_endpoint_test_essential':False,'global_zero_defects_assumed':False,'actual_instance_evaluations':0,'historical_enumerations':0,'complete_profile_claim':False}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
