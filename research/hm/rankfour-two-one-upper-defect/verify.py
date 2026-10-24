#!/usr/bin/env python3
"""Universal abstract bundle/character controls, never actual HM instances."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from collections import Counter
from functools import lru_cache
import hashlib,json

ROOT=Path(__file__).resolve().parent
NAMES=('1','W','A','S4','D','T6','P',"W'",'V')
DIMS=(1,2,3,4,5,6,4,2,3)
PARITY=(0,1,0,1,0,1,0,1,0)
EDGES=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8))
ZERO=(0,)*9
HASHES={
 'four-sources.md':'d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e',
 'RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md':'efc9ca4ea3348429be704d27096ba8ceec00de522ee5159bcfdf33972ecd7d22',
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
@lru_cache(None)
def sym(v,n):
 if n<0:return ZERO
 prev,now=ZERO,v
 for _ in range(n):prev,now=now,sub(times_w(now),prev)
 return now
def h0(bs,t):return add(*(sym(unit(i),e+t) for e,i in bs if e+t>=0))
def h1(bs,t):return add(*(sym(unit(i),-e-t-2) for e,i in bs if e+t<=-2))
@lru_cache(None)
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
  require(x['ref']==('504b7eb800407dfc7e6340c98c72cdd553939f54' if name=='four-sources.md' else 'db51525015bb7c5e825833d550d08dedf6f6ea96'),'pinned original ref')
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
@lru_cache(None)
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

def bounded_splits(rank,degree,lo,hi):
 blocks=[(e,i)for e in range(lo,hi+1)for i in range(9)if DIMS[i]<=rank and PARITY[i]==e%2]
 out=[]
 def rec(start,r,d,bs):
  if r==0:
   if d==0:out.append(tuple(bs))
   return
  for j in range(start,len(blocks)):
   e,i=blocks[j];n=DIMS[i]
   if n<=r and (r-n)*lo<=d-e*n<=(r-n)*hi:rec(j,r-n,d-e*n,bs+[(e,i)])
 rec(0,rank,degree,[])
 return tuple(sorted(out))

@lru_cache(None)
def coefficient_types(n,parity):
 ids=[i for i in range(9)if PARITY[i]==parity and DIMS[i]<=n];out=[]
 def rec(pos,r,ls):
  if r==0:out.append(tuple(ls));return
  for j in range(pos,len(ids)):
   i=ids[j]
   if DIMS[i]<=r:rec(j,r-DIMS[i],ls+[i])
 rec(0,n,[])
 return tuple(out)
def independent_splits(rank,degree,lo,hi):
 """First partition ordinary degrees; independently decompose equal-degree fibers."""
 parts=[]
 def part(r,d,low,ls):
  if r==0:
   if d==0:parts.append(tuple(ls))
   return
  for e in range(low,min(hi,d//r)+1):
   if (r-1)*e<=d-e<=(r-1)*hi:part(r-1,d-e,e,ls+[e])
 part(rank,degree,lo,[]);out=[]
 for es in parts:
  groups=sorted(Counter(es).items())
  for choices in product(*(coefficient_types(n,e%2)for e,n in groups)):
   out.append(tuple(sorted((e,i)for (e,n),ijs in zip(groups,choices)for i in ijs)))
 return tuple(sorted(out))
def signature(bs,offset=0):return chi(bs,offset)+chi(bs,offset+1)
def homdim(source,target):
 return sum(sym(unit(j),f-e)[i]for e,i in source for f,j in target if f>=e)
def twist(bs,t):return tuple(sorted((e+t,i)for e,i in bs))
def quotient_blocks(endpoint,selected):
 x=list(endpoint)
 for block in selected:x.remove(block)
 return tuple(x)

@lru_cache(None)
def tors_atom(n,r,t):return sub(repchi(unit(0),r+t),repchi(unit(0),r+t-n))
@lru_cache(None)
def torsion(desc,t):return add(*(tors_atom(n,r,t)for n,r in desc))
def horizontal_witnesses(endpoint,target):
 out=[]
 for j,block in enumerate(endpoint):
  internal=twist(endpoint[:j]+endpoint[j+1:],-2)
  if homdim((block,),target)==0 and homdim((block,),internal)==0:
   out.append({'subbundle':shape((block,)),'outer_Hom_dimension':0,'internal_Hom_dimension':0})
 return out

def derive():
 authenticate();character_controls()
 require([dim(x)for x in(M2,M3,M4,H)]==[41,54,37,30],'actual unequal presentations')
 require(sub(sub(times_w(M3),M2),M4)==H,'actual constant representation')
 require(E(1)==vec(T6=-3,**{"W'":-1}),'actual E twist one')
 require(Qstar(1)==vec(W=-1,S4=-2,T6=-3),'actual dual twist one')
 require(Qstar(2)==vec(**{'1':-1,'A':-2,'D':-1,'V':-1}),'actual dual twist two')
 for t in range(-14,15):require(Qstar(t)==mul(Q(-t-2),-1),'actual duality')
 require([9+4*i for i in range(4)]==[9,13,17,21],'ordered two-one ranks')
 # Formal coefficients: 1,a,c1,d1,d2.
 def ba(i):return tuple(int(i==j)for j in range(5))
 def pa(*xs):return tuple(sum(x[i]for x in xs)for i in range(5))
 def sc(x,k):return tuple(k*v for v in x)
 cs=[ba(2)]
 for j in range(2):cs.append(pa(cs[-1],sc(ba(0),8),ba(j+3)))
 ee=pa(ba(1),*cs[:2]);bb=pa(ba(1),*cs)
 require(pa(ba(1),sc(bb,2),sc(ee,-3))==(24,0,0,1,2),'a+2b=3E+24+d1+2d2')
 require(-28+2*(-28)-(-138)==54,'ordered endpoint slack54')
 sem=sorted({12*x+20*y+30*z for x in range(5)for y in range(3)for z in range(2)if 12*x+20*y+30*z<=54})
 cases=[];all_numerical=[]
 for d1,d2 in product(sem,repeat=2):
  for u in range(28):
   for v in range(14):
    if 2*u+4*v+d1+2*d2!=54:continue
    a,b=-28-2*u,-28-2*v;c1=(-62-a-d1)//2
    if c1%2:continue
    d=c1+8+d1;row=(a,b,d1,d2,d);all_numerical.append(row)
    require(a+2*c1+8+d1==-54 and b==-54+d+8+d2,'central degree and upper quotient degree')
    if d2>=20:cases.append(row)
 require(sorted({x[3]for x in all_numerical})==[0,12,20,24],'all possible upper defects')
 expected=[(-30,-34,0,20,-8),(-34,-32,0,20,-6),(-38,-30,0,20,-4),(-42,-28,0,20,-2),(-30,-30,0,24,-8),(-34,-28,0,24,-6),(-30,-28,12,20,-2)]
 require(cases==expected,'complete seven high-defect degree cases')
 # Composition-factor overlists include nonreduced orbit modules.
 T={0:[()],12:[((12,r),)for r in range(0,10,2)],20:[((20,r),)for r in range(0,6,2)],24:[((12,r),(12,s))for r in range(0,10,2)for s in range(r,10,2)]}
 require([len(T[n])for n in(0,12,20,24)]==[1,5,3,15],'all stabilizer-character composition multisets')
 for n,descs in T.items():
  for ds in descs:
   for t in range(-8,9):
    vv=torsion(ds,t)
    require(genuine(vv)and dim(vv)==n,'torsion positivity and length')
    require(all(not x or PARITY[i]==t%2 for i,x in enumerate(vv)),'torsion center parity')
    require(torsion(ds,t+1)==sub(times_w(vv),torsion(ds,t-1)),'torsion Euler recurrence')
 for n,period in((12,10),(20,6),(30,4)):
  for r in range(0,period,2):
   for t in(-2,-1,0,1,2):require(tors_atom(n,r+period,t)==tors_atom(n,r,t),'stabilizer-character periodicity')
 # Universal K0 shift ledger, keeping every torsion sign.
 lower_B=Counter({0:1,-2:1});upper_B=Counter({2:1})
 shifted_B=Counter({e-2:c for e,c in upper_B.items()})+Counter({e-4:c for e,c in upper_B.items()})
 require(lower_B==shifted_B,'upper-shift elimination cancels both lower B terms')
 require(sorted([2-2,2-4])==[-2,0],'retained upper torsion shifts')
 H1E1=vec(T6=3,**{"W'":1});negative=[]
 for j in range(3,23):
  for i in range(9):
   if DIMS[i]<=4 and PARITY[i]==j%2 and genuine(sub(H1E1,sym(unit(i),j-3))):negative.append((-j,i))
 require(negative==[(-3,7),(-4,6),(-4,8),(-5,7),(-8,0),(-9,1),(-10,0)],'fresh rank-four quotient negative-block bound')
 endpoints={};Bs={}
 for a,b,d1,d2,d in cases:
  for dg in(a,b):
   if dg in endpoints:continue
   lo=dg+24;xs=bounded_splits(9,dg,lo,-3);ys=independent_splits(9,dg,lo,-3)
   require(xs==ys,'independent endpoint splitting domain')
   idx={}
   for z in xs:
    require(sum(DIMS[i]for e,i in z)==9 and sum(e*DIMS[i]for e,i in z)==dg,'endpoint rank and degree')
    idx.setdefault(signature(z),[]).append(z)
   endpoints[dg]=(xs,idx)
  if d not in Bs:
   xs=bounded_splits(4,d,-10,d+30);ys=independent_splits(4,d,-10,d+30)
   require(xs==ys,'independent quotient splitting domain')
   keep=[]
   for B in xs:
    tests=[sub(H1E1,h1(B,1)),sub(mul(Qstar(1),-1),h0(B,-1))]
    tests += [sub(sub(chi(B,t),E(t)),h1(B,t-2))for t in(-2,-1,0,1)]
    if all(genuine(x)for x in tests):keep.append(B)
   Bs[d]=(xs,keep)
 summary=[];horizontal=[];survivors=[];allexact=[]
 for a,b,d1,d2,d in cases:
  count=0;surv=[]
  for B in Bs[d][1]:
   Fs=[];Ds=[]
   for T1 in T[d1]:
    target=tuple(add(sub(E(t),add(chi(B,t),chi(B,t-2))),torsion(T1,t))[i]for t in(0,1)for i in range(9))
    for F0 in endpoints[a][1].get(target,[]):Fs.append((F0,T1))
   for T2 in T[d2]:
    Pdu=sub(sub(mul(chi(B,-2),-1),torsion(T2,-2)),Qstar(2))
    if not genuine(Pdu):continue
    target=tuple(add(Qstar(t),chi(B,-t),torsion(T2,-t))[i]for t in(0,1)for i in range(9))
    for D0 in endpoints[b][1].get(target,[]):Ds.append((D0,T2))
   for F0,T1 in Fs:
    for D0,T2 in Ds:
     count+=1;row=(a,b,d1,d2,d,F0,D0,B,T1,T2);allexact.append(row)
     fw=horizontal_witnesses(F0,twist(B,-4));dw=horizontal_witnesses(D0,twist(dual(B),-4))
     if fw or dw:horizontal.append({'case':[a,b,d1,d2,d],'F0':shape(F0),'D0':shape(D0),'B':shape(B),'T1':T1,'T2':T2,'primal':fw,'dual':dw})
     else:surv.append(row);survivors.append(row)
  summary.append({'case':[a,b,d1,d2,d],'F0_domain':len(endpoints[a][0]),'D0_domain':len(endpoints[b][0]),'B_domain':len(Bs[d][0]),'B_positive_domain':len(Bs[d][1]),'exact_positive_survivors':count,'horizontal_survivors':len(surv)})
 require(len(survivors)==5,'five high-defect residual tuples')
 # Direct literal boundary, independent of lists produced by exploration.
 f20=((-5,7),(-4,8),(-3,3));d20=((-8,0),(-3,5),(-3,7))
 b20a=((-8,0),(-8,0),(4,0),(6,0));b20b=((-8,0),(-8,0),(5,1))
 f24a=((-6,0),(-3,1),(-3,5));f24b=((-4,2),(-3,5));d24=((-6,0),(-3,5),(-3,7));b24=((-8,0),(-8,0),(2,0),(6,0))
 ffinal=((-4,8),(-3,5));bfinal=((-8,0),(-3,7),(6,0))
 literal={(-34,-32,0,20,-6,f20,d20,b20a,(),((20,2),)),(-34,-32,0,20,-6,f20,d20,b20b,(),((20,2),)),
 (-30,-30,0,24,-8,f24a,d24,b24,(),((12,4),(12,6))),(-30,-30,0,24,-8,f24b,d24,b24,(),((12,4),(12,6))),
 (-30,-30,0,24,-8,ffinal,ffinal,bfinal,(),((12,2),(12,4)))}
 require(set(survivors)==literal,'complete literal five-row boundary')
 for row in survivors:
  a,b,d1,d2,d,F0,D0,B,T1,T2=row
  for t in range(-12,13):
   require(chi(F0,t)==add(sub(E(t),add(chi(B,t),chi(B,t-2))),torsion(T1,t)),'all-twist lower exact identity')
   require(chi(D0,t)==add(Qstar(t),chi(B,-t),torsion(T2,-t)),'all-twist upper exact identity')
   require(sub(chi(F0,t),add(chi(dual(D0),t-2),chi(dual(D0),t-4)))==add(sub(E(t),add(Q(t-2),Q(t-4))),torsion(T1,t),torsion(T2,t),torsion(T2,t-2)),'all-twist torsion-retaining elimination')
 # Four-source theorem is used ONLY for this one cohomology consequence.
 source_splittings=[((-2,4),(-3,7),(-3,5),(-4,8),(-8,0)),((-2,6),(-3,7),(-3,5),(-4,8),(-5,7)),((-2,8),(-3,7),(-3,5),(-4,8),(-4,8)),((-3,7),(-3,5),(-3,5),(-4,8))]
 allowed_h1=[h1(x,3)for x in source_splittings]
 require(allowed_h1==[unit(3),unit(7),ZERO,ZERO],'actual four-source cubic H1 consequence')
 source_rejected=[];final=[]
 for row in survivors:
  B=row[7];allowed=[j for j,ch in enumerate(allowed_h1)if genuine(sub(ch,h1(B,3)))]
  if allowed:final.append((row,allowed))
  else:source_rejected.append({'case':list(row[:5]),'B':shape(B),'H1_B_twist3':pretty(h1(B,3))})
 require(len(source_rejected)==4 and len(final)==1,'four cubic quotient contradictions, one remaining tuple')
 require(final[0][0][5]==ffinal and final[0][0][7]==bfinal and final[0][1]==[0],'remaining tuple forces actual D source')
 require(homdim(ffinal,twist(quotient_blocks(bfinal,((6,0),)),-4))==0,'endpoint derivative can reach only scalar O2')
 require(sum(DIMS[i]for e,i in ffinal)==9 and sum(e*DIMS[i]for e,i in ffinal)==-30,'last endpoint rank and degree')
 require([n for n in range(12,31)if 9*(n-9)<=30]==[12],'rank-one degree bound and three-step persistence force span12')
 n,r=12,9;ss=n-r;weight=n*(30-r*ss);ws=[ss*j if j<r else r*(n-j)for j in range(1,n)]
 require(weight==36 and ws==[3,6,9,12,15,18,21,24,27,18,9],'complete rank-one required weights')
 possible=[]
 def defects_rec(pos,left,vals):
  if pos==11:
   if left==0:possible.append(tuple(vals))
   return
  for dd in sem:
   if ws[pos]*dd<=left:defects_rec(pos+1,left-ws[pos]*dd,vals+[dd])
 defects_rec(0,weight,[])
 require(possible==[(12,0,0,0,0,0,0,0,0,0,0)],'only first complete-flag defect is12')
 deltas=possible[0];numerator=-n*(n-1)-sum((n-j)*deltas[j-1]for j in range(1,n))
 require(numerator%n==0,'integral initial complete-flag degree')
 lines=[numerator//n]
 for dd in deltas:lines.append(lines[-1]+2+dd)
 require(lines==[-22,-8,-6,-4,-2,0,2,4,6,8,10,12],'forced complete-flag line degrees')
 require(sum(lines[:9])==-30 and sum(lines[:10])==-22 and sum(lines[:11])==-12 and sum(lines)==0,'first two forward endpoint degrees')
 require(-12>-2*11,'rank11 second forward transform violates actual E twist-one vanishing')
 span_character=add(*(repchi(unit(0),e)for e in lines))
 require(span_character==vec(A=1,D=1,P=1),'optional pinned invariant constant-span character')
 require(genuine(sub(H,span_character)),'constant-span character alone is not a contradiction')
 return {'status':'PASS','theorem':'In an actual ordered maximal rank-four (2,1) plateau, the upper derivative defect delta2 is 0 or 12.',
  'scope':'This does not exclude the (2,1) profile or change the remaining coarse-bin count.',
  'input_originals':6,'numerical_cases_all':len(all_numerical),'high_defect_cases':summary,
  'torsion_composition_factor_counts':{str(n):len(T[n])for n in T},'exact_positive_count':len(allexact),
  'horizontal_rejection_count':len(horizontal),'horizontal_rejections':horizontal,
  'five_residual_tuples':[{'case':list(x[:5]),'F0':shape(x[5]),'D0':shape(x[6]),'B':shape(x[7]),'T1':x[8],'T2':x[9]}for x in survivors],
  'source_cubic_rejections':source_rejected,'rank_one_final':{'span':12,'rank':9,'degree':-30,'required_weight':36,'defects':deltas,'line_degrees':lines,'second_forward_rank':11,'second_forward_degree':-12,'required_degree_cap':-22,'span_character':pretty(span_character)},'checks':checks}
if __name__=='__main__':print(json.dumps(derive(),indent=2,sort_keys=True))
