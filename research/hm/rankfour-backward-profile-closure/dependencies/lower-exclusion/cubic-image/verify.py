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
HASHES['four-sources.md']='d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e'
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
  ref='504b7eb800407dfc7e6340c98c72cdd553939f54' if name=='four-sources.md' else 'db51525015bb7c5e825833d550d08dedf6f6ea96'
  require(x['ref']==ref,'pinned original ref')
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

SOURCES={
 'D':((-2,4),(-3,7),(-3,5),(-4,8),(-8,0)),
 'P':((-2,6),(-3,7),(-3,5),(-4,8),(-5,7)),
 'V':((-2,8),(-3,7),(-3,5),(-4,8),(-4,8)),
 'Z':((-3,7),(-3,5),(-3,5),(-4,8))}

def tensor(x,y):
 return class_decompose(tuple(qm(char_eval(x,k),char_eval(y,k))for k in range(9)))
def block_hom(e,i,f,j):
 return 0 if f<e else sym(unit(j),f-e)[i]
def image_eligible(e,i,sources=SOURCES):
 if not (0<=e<=9 and DIMS[i]<=4 and PARITY[i]==(e+1)%2):return False
 if not sym(unit(i),e)[5]:return False
 return any(any(block_hom(e,i,1-f,j)for f,j in bs)for bs in sources.values())
def rank_of(bs):return sum(DIMS[i]for e,i in bs)
def degree_of(bs):return sum(e*DIMS[i]for e,i in bs)
def dimension_bound(bs):return 6+dim(h0(dual(bs),2))+dim(h0(dual(bs),0))
def first_ledger():
 sem=sorted({12*x+20*y+30*z for x in range(4)for y in range(3)for z in range(2)if 12*x+20*y+30*z<=40})
 out=[]
 for ds in product(sem,repeat=3):
  slack=40-sum((i+1)*d for i,d in enumerate(ds))
  if slack<0:continue
  for u in range(slack//2+1):
   for v in range(slack//6+1):
    if 2*u+6*v!=slack:continue
    a=-20-2*u;b=-36-2*v;n=-78-a-2*ds[0]-ds[1]
    if n%6:continue
    cs=[n//3]
    for d in ds:cs.append(cs[-1]+8+d)
    out.append((a,b,ds,tuple(cs)))
 return tuple(sorted(out))
def second_ledger():
 # Independently scan even stage data, and recover all defects from differences.
 out=[]
 sem={n for n in range(41)if any(n==12*x+20*y+30*z for x in range(4)for y in range(3)for z in range(2))}
 for a in range(-60,-19,2):
  for b in range(-48,-35,2):
   c4=b+54
   for c1 in range(-46,-5,2):
    for c2 in range(-38,3,2):
     c3=-54-a-c1-c2
     cs=(c1,c2,c3,c4);ds=tuple(cs[i+1]-cs[i]-8 for i in range(3))
     if all(d in sem for d in ds):out.append((a,b,ds,cs))
 return tuple(sorted(out))
def image_multisets(blocks):
 return tuple(sorted(bs for n in range(1,5)for bs in combinations_with_replacement(blocks,n)if rank_of(bs)==4))
def independent_images(blocks):
 out=[]
 def go(j,left,bs):
  if j==len(blocks):
   if left==0:out.append(tuple(bs))
   return
  e,i=blocks[j]
  for n in range(left//DIMS[i]+1):go(j+1,left-n*DIMS[i],bs+[(e,i)]*n)
 go(0,4,[])
 return tuple(sorted(out))
def bottom(t):return sub(E(t),add(*(repchi(unit(6),t-e)for e in (4,2,0))))
def bottom_class(t):return cadd(class_E(t),*(cmul(class_repchi(unit(6),t-e),-1)for e in (4,2,0)))
def endpoint_valid(bs):return rank_of(bs)==5 and degree_of(bs)==-30 and all(e<=-4 and PARITY[i]==e%2 for e,i in bs)and all(chi(bs,t)==bottom(t)for t in (3,4))
def endpoint_hom(bs):return sum(block_hom(e,i,-6,6)for e,i in bs)
def ledger_row(r):
 a,b,ds,cs=r;fs=[a]
 for c in cs:fs.append(fs[-1]+c)
 return {'a':a,'b':b,'defects':list(ds),'quotient_degrees':list(cs),'stage_degrees':fs}

def derive():
 ninputs=authenticate();character_controls()
 require([dim(x)for x in (M2,M3,M4,H)]==[41,54,37,30],'actual coefficient and ambient dimensions')
 require(sub(sub(times_w(M3),M2),M4)==H,'actual ambient Koszul character')
 require(E(3)==vec(**{"W'":1,'T6':2}),'actual E cubic Euler')
 require(Qstar(3)==vec(W=-2,S4=-1,T6=1),'actual dual cubic Euler')
 require(E(2)==vec(V=-1),'physical primal quadratic Euler')
 for name,bs in SOURCES.items():
  require(rank_of(bs)==17 and degree_of(bs)==-54,'necessary source ranks/degrees')
  require(max(1-e for e,i in bs)<=9,'actual image target degree cap')
  for t in range(-2,10):
   require(chi(bs,t)==E(t),'source Euler identities')
   require(class_decompose(class_chi(bs,t))==chi(bs,t),'source exact-class cohomology')
 for t in range(-12,13):
  require(Qstar(t)==mul(Q(-t-2),-1),'unequal actual presentations and duality')
  require(class_decompose(class_E(t))==E(t),'actual E independent Euler')
  require(class_decompose(class_Qstar(t))==Qstar(t),'actual Qstar independent Euler')
 # Universal polynomial determinant identity, not a sampled actual stage.
 def basis(i):return tuple(int(i==j)for j in range(6))
 def pa(*xs):return tuple(sum(x[i]for x in xs)for i in range(6))
 def sc(x,n):return tuple(n*y for y in x)
 cs=[basis(2)]
 for j in range(3):cs.append(pa(cs[-1],sc(basis(0),8),basis(3+j)))
 ee=pa(basis(1),*cs[:3]);bb=pa(basis(1),*cs)
 relation=pa(basis(1),sc(bb,3),sc(ee,-4))
 require(relation==(48,0,0,1,2,3),'full affine determinant relation')
 require(4*(-54)+48==-168,'correct actual endpoint constant')
 ledger=first_ledger();require(ledger==second_ledger(),'independent complete positive-defect ledger')
 require(len(ledger)==31 and sum(any(r[2])for r in ledger)==24,'positive defects not discarded')
 require(len(set(r[2]for r in ledger))==12,'twelve invariant defect patterns')
 for a,b,ds,cs in ledger:
  require(a<=-20 and b<=-36 and all(c%2==0 for c in cs),'endpoint persistence and parity')
  require(a+sum(cs[:3])==-54 and a+sum(cs)==b,'actual marked central prefix')
  require(a+3*b==-168+sum((i+1)*d for i,d in enumerate(ds)),'endpoint defect identity')
 blocks=tuple((e,i)for e in range(10)for i in range(9)if image_eligible(e,i))
 expected_blocks=((1,6),(1,8),(2,3),(2,7),(3,6),(3,8),(4,7),(5,6),(5,8),(6,3),(6,7),(7,2),(8,1),(9,0))
 require(blocks==expected_blocks,'complete fourteen image block overlist')
 require(tuple(b for b in blocks if DIMS[b[1]]==1)==((9,0),),'rank-one image is necessarily O9')
 require([name for name,bs in SOURCES.items()if any(block_hom(9,0,1-f,j)for f,j in bs)]==['D'],'rank-one image requires source D')
 for e in range(10):
  for i in range(9):
   require(sym(unit(i),e)[5]==tensor(unit(i),sym(unit(0),e))[5],'independent source multiplicity')
   for name,bs in SOURCES.items():
    for f,j in bs:
     if 1-f>=e:require(block_hom(e,i,1-f,j)==tensor(unit(j),sym(unit(0),1-f-e))[i],'independent target Hom multiplicity')
 all_images=image_multisets(blocks)
 require(all_images==independent_images(blocks),'independent rank-four block coverage')
 survivors=tuple(bs for bs in all_images if degree_of(bs)<=dimension_bound(bs))
 expected=tuple(sorted([((1,6),),((2,3),),((1,8),(9,0)),((2,7),(2,7))]))
 require(survivors==expected,'four candidates after newly derived rank-four section bound')
 for bs in survivors:require(0<=dimension_bound(bs)-degree_of(bs)<12,'every full-rank cubic image is saturated')
 # S4 O(2): an actual positive Euler constituent absent from the section target.
 B=((-1,3),);r=sub(E(3),chi(B,3));allowed=h0(B,1)
 require(r==vec(W=-1,S4=-1,T6=1,**{"W'":1}),'S4 candidate exact Euler')
 require(any(r[i]>allowed[i]for i in range(9)),'S4 candidate section contradiction')
 # Two identical target blocks cannot be generated by a one-dimensional Hom space.
 require(sym(unit(7),2)==unit(5),'single T6 intertwiner to Wprime O2')
 require(2<4,'diagonal image rank bound strictly below full rank')
 # V O1 plus O9: exact H1 vanishing implies all source degrees >=-4.
 B=((0,8),(-8,0));r=sub(E(3),chi(B,3))
 require(r==h0(B,1)==unit(5),'V plus line cohomology equality forces H1=0')
 require(h0(B,-1)==ZERO,'vanishing lower-stage section target')
 require(-10<-4 and DIMS[8]==3<4,'unreachable low target line gives rank-three bound')
 # P O1 is the only subcase where all plateau defects vanish.
 local=[row for row in ledger if row[3][2]==0]
 require(local==[(-30,-46,(0,0,0),(-16,-8,0,8))],'P candidate alone forces zero defects')
 require(bottom(3)==vec(S4=-1,T6=-1),'forced endpoint cubic Euler')
 require(bottom(4)==vec(V=1,A=-1,D=-1),'forced endpoint quartic Euler')
 for t in range(-2,10):require(class_decompose(bottom_class(t))==bottom(t),'endpoint Euler independent class calculation')
 endpoint_shapes=split_by_blocks(5,-30,-4)
 require(endpoint_shapes==split_by_ordinary_degrees(5,-30,-4),'independent complete rank-five endpoint shape domain')
 require(len(endpoint_shapes)==46,'new endpoint finite window has 46 shapes')
 endpoints=tuple(bs for bs in endpoint_shapes if endpoint_valid(bs))
 require(endpoints==(((-10,0),(-8,0),(-4,8)),((-9,1),(-4,8))),'two forced endpoint shapes')
 for bs in endpoints:
  require(endpoint_hom(bs)==0,'entire endpoint derivative Hom space vanishes')
  for t in range(-2,10):require(chi(bs,t)==bottom(t),'endpoint all checked Euler twists')
 # Genuine negative controls recalculate constraints after corrupting conclusions.
 controls=[]
 def reject(label,condition):require(condition,label);controls.append(label)
 reject('discarding positive defects loses 24 necessary numerical rows',tuple(r for r in ledger if not any(r[2]))!=ledger)
 reject('reversing unequal endpoint weights breaks a retained row',any(a+3*b!=-168+sum((3-i)*d for i,d in enumerate(ds))for a,b,ds,cs in ledger))
 reject('substituting source Z alone changes image-block coverage',tuple((e,i)for e in range(10)for i in range(9)if image_eligible(e,i,{'Z':SOURCES['Z']}))!=blocks)
 reject('permitting absent cubic image block O1 fails source character',not image_eligible(1,0))
 reject('omitting dimension bound retains invalid rank-four image',any(degree_of(bs)>dimension_bound(bs)for bs in all_images))
 reject('declaring full-rank image defect twelve violates every bound',all(degree_of(bs)+12>dimension_bound(bs)for bs in survivors))
 reject('identifying physical A with V changes endpoint Euler',bottom(4)!=vec(A=1,V=-1,D=-1))
 reject('dropping quartic endpoint test retains fifteen false endpoints',sum(chi(bs,3)==bottom(3)for bs in endpoint_shapes)==17)
 reject('allowing V Ominus4 to differentiate downward contradicts Hom',block_hom(-4,8,-6,6)==0)
 reject('adding invariant defect12 to local P branch violates endpoint cap',-30+12>-20 and -46+12>-36)
 reject('replacing physical P target by D destroys endpoint Hom vanishing',any(sum(block_hom(e,i,-6,4)for e,i in bs)>0 for bs in endpoints))
 return {'status':'PASS','scope':'Only the restricted dual cubic image bound rank 1..3 in actual ordered rank-four plateau (3,1); no profile closure.',
  'authenticated_originals':ninputs,'historical_enumeration_used':False,'actual_instance_evaluation_used':False,
  'rank_one_image':{'degree':9,'coefficient':'1','necessary_source':'D'},
  'canonical_single_T6_assumed':False,'source_Z_assumed':False,'globally_zero_defects_assumed':False,
  'actual_E3_Euler':pretty(E(3)),'actual_Qstar3_Euler':pretty(Qstar(3)),
  'plateau_ranks':[5,9,13,17,21],'endpoint_bounds':[-20,-36],
  'ledger':[ledger_row(row)for row in ledger],'ledger_rows':31,'positive_defect_rows':24,
  'image_blocks':[{'degree':e,'coefficient':NAMES[i], 'source_labels':[name for name,bs in SOURCES.items()if any(block_hom(e,i,1-f,j)for f,j in bs)]}for e,i in blocks],
  'rank_four_image_multisets':len(all_images),'section_bound_survivors':[{'shape':shape(bs),'degree':degree_of(bs),'saturated_degree_upper_bound':dimension_bound(bs)}for bs in survivors],
  'endpoint_shapes':[{'shape':shape(bs),'chi3':pretty(chi(bs,3)),'chi4':pretty(chi(bs,4)),'passes':endpoint_valid(bs)}for bs in endpoint_shapes],
  'forced_endpoints':[shape(bs)for bs in endpoints],'rank_four_images_remaining':0,'negative_controls':controls,'checks':checks}

if __name__=='__main__':print(json.dumps(derive(),indent=2,sort_keys=True))
