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
 'EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md':'9f01d086401ee7ee850d3c9181c0486734bcc5c5791c552410895ae4ba742fbf',
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
  for n in range(10):
   v=sym(unit(i),n)
   require(genuine(v),'genuine symmetric power')
   require(dim(v)==DIMS[i]*(n+1),'symmetric power dimension')
   require(all(not c or PARITY[j]==(PARITY[i]+n)%2 for j,c in enumerate(v)),'symmetric power parity')
   expected=tuple(qm(CHARS[i][k],qsym(n,x))for k,x in enumerate(TRACES))
   require(tuple(char_eval(v,k)for k in range(9))==expected,'McKay vs exact class product')

BLOCKS=tuple((e,i)for e in range(-2,7)for i in range(9)if DIMS[i]<=4 and PARITY[i]==e%2)
def enumerate_blocks():
 out=set()
 def rec(bs,start,r,d):
  if r==4:
   if d==0:out.add(tuple(bs))
   return
  for j in range(start,len(BLOCKS)):
   e,i=BLOCKS[j]
   if r+DIMS[i]<=4:rec(bs+[(e,i)],j,r+DIMS[i],d+e*DIMS[i])
 rec([],0,0,0)
 return out

def decompose_degree(rank,par):
 reps=[i for i in range(9)if PARITY[i]==par and DIMS[i]<=rank]
 out=[]
 # Independent bounded multiplicity-product method at a fixed degree.
 for ms in product(*(range(rank//DIMS[i]+1)for i in reps)):
  if sum(m*DIMS[i]for i,m in zip(reps,ms))==rank:
   out.append(tuple(i for i,m in zip(reps,ms)for _ in range(m)))
 return out

def enumerate_ordinary_degrees():
 out=set()
 for degrees in combinations_with_replacement(range(-2,7),4):
  if sum(degrees)!=0:continue
  counts=Counter(degrees);keys=sorted(counts)
  choices=[decompose_degree(counts[e],e%2)for e in keys]
  for reps in product(*choices):
   out.add(tuple(sorted((e,i)for e,rr in zip(keys,reps)for i in rr)))
 return out

def derive():
 ninputs=authenticate();character_controls()
 M2=vec(A=1,V=2,P=3,D=4);M3=vec(**{"W'":3,'S4':3,'T6':6});M4=vec(V=2,P=4,D=3)
 H=sub(sub(times_w(M3),M2),M4)
 require(H==vec(A=2,V=2,P=2,D=2) and dim(H)==30,'actual ambient character')
 actual_h1=sub(times_w(M4),M3)
 require(actual_h1==vec(**{"W'":1,'T6':3}),'actual H1(E1)')
 U=vec(**{"W'":1,'T6':2})
 source_options=[('A',vec(A=1)),('V',vec(V=1)),('3*1',vec(**{'1':3}))]
 source_survivors=[(name,sub(actual_h1,times_w(v)))for name,v in source_options if genuine(sub(actual_h1,times_w(v)))]
 require(source_survivors==[('V',U)],'three-deficit source selection')
 require(not genuine(sub(actual_h1,vec(S4=1))),'O(-6) source alternative rejected')
 require(2*min(DIMS[i]for i in range(9)if PARITY[i])>3,'no degree-5 source block')
 E=tuple([(-3,7)]+[(-3,5)]*2+[(-4,8)])
 require(sum(DIMS[i]for _,i in E)==17 and sum(e*DIMS[i]for e,i in E)==-54,'Z rank and degree')
 require(h1(E,1)==actual_h1 and h0(E,3)==U and h1(E,3)==ZERO,'Z cohomology')

 ranks=[5+4*i for i in range(7)];cs=[-16+8*i for i in range(6)]
 fs=[-30]
 for c in cs:fs.append(fs[-1]+c)
 require(ranks==[5,9,13,17,21,25,29],'plateau ranks')
 require(fs==[-30,-46,-54,-54,-46,-30,-6],'plateau degrees')
 # Exact symbolic affine coefficient vectors ordered
 # [constant, a, c1, delta1,...,delta5], avoiding numeric sampling.
 def padd(*xs):return tuple(sum(x[i]for x in xs)for i in range(8))
 def pscale(x,n):return tuple(n*y for y in x)
 def basis(i):return tuple(int(j==i)for j in range(8))
 ps=[basis(2)]
 for i in range(5):ps.append(padd(ps[-1],pscale(basis(0),8),basis(3+i)))
 pf3=padd(basis(1),*ps[:3]);pb=padd(basis(1),*ps)
 identity=padd(basis(1),pb,pscale(pf3,-2))
 require(identity==(72,0,0,1,2,3,2,1),'symbolic endpoint degree identity')
 require(-2*54+identity[0]==-36,'endpoint identity constant')
 require(list(identity[3:])==[1,2,3,2,1],'endpoint defect weights')
 require(-6*5-6==-36 and all(w>0 for w in [1,2,3,2,1]),'endpoint equality closes defects')
 require(-46-9*(-5)==-1 and -54-13*(-4)==-2,'F1 and F2 excesses')
 require(0-3*(-2)==6,'forced upper slope from lower slope and degree zero')
 # Check all ordinary partitions of tiny deficits without assuming parity.
 def deficits(n,total):
  return [ds for ds in combinations_with_replacement(range(total+1),n)if sum(ds)==total]
 f1=deficits(9,1);f2=deficits(13,2)
 require(f1==[(0,)*8+(1,)],'F1 ordinary splitting')
 require(set(f2)=={(0,)*12+(2,),(0,)*11+(1,1)},'F2 ordinary splittings')
 require([dim(sym(unit(0),d-2)) if d>=2 else 0 for d in [1,2,3]]==[0,1,2],'line cohomology')

 candidates=enumerate_blocks();second=enumerate_ordinary_degrees()
 require(candidates==second,'independent abstract candidate enumeration')
 require(len(candidates)==20,'twenty new rank-four candidates')
 target_w=add(U,vec(W=1));target_wp=add(U,vec(**{"W'":1}))
 survivor=((-2,0),(-1,7),(4,0))
 results=[];survivors=[]
 for bs in sorted(candidates):
  ch=h0(bs,3)
  require(h1(bs,1)==ZERO,'forced H1B1 window')
  require(dim(ch)==16,'candidate cubic sections')
  require(class_decompose(class_h0(bs,3))==ch,'candidate class-character independent check')
  keep=ch in (target_w,target_wp)
  if keep:survivors.append(bs)
  results.append({'blocks':shape(bs),'h0_B3':pretty(ch),'cubic_condition':keep})
 require(survivors==[survivor],'unique cubic survivor')
 require(h0(survivor,3)==target_w,'survivor exact cubic character')
 require(h1(survivor,4)==ZERO,'survivor H1B4')
 residual=sub(chi(E,4),chi(survivor,4))
 require(residual==vec(V=2,P=2,A=-1),'exact F2 degree-four Euler residual')
 require(dim(residual)==11,'ordinary Euler dimension residual')
 for corr in (ZERO,unit(0)):
  require(add(residual,corr)[2]==-1 and not genuine(add(residual,corr)),'negative A survives all H1 corrections')

 # Fail-closed contract mutations check required facts, not geometry.
 def accept_contract(c):
  return (c['ranks']==ranks and c['degrees']==fs and c['weights']==[1,2,3,2,1]
   and c['lower']==-2 and c['upper']==6 and c['source_h1']==list(actual_h1)
   and c['source']==list(U) and c['parity']==list(PARITY)
   and c['candidate_keys']==[list(map(list,x))for x in sorted(second)]
   and c['survivors']==[list(map(list,survivor))] and c['residual']==list(residual)
   and c['h1_corrections']==[list(ZERO),list(unit(0))])
 contract={'ranks':ranks,'degrees':fs,'weights':[1,2,3,2,1],'lower':-2,'upper':6,
  'source_h1':list(actual_h1),'source':list(U),'parity':list(PARITY),
  'candidate_keys':[list(map(list,x))for x in sorted(second)],'survivors':[list(map(list,survivor))],
  'residual':list(residual),'h1_corrections':[list(ZERO),list(unit(0))]}
 require(accept_contract(contract),'base contract acceptance')
 mutations=[]
 for key in contract:
  c=json.loads(json.dumps(contract))
  if isinstance(c[key],int):c[key]+=1
  else:c[key]=c[key][:-1]
  require(not accept_contract(c),'reject changed '+key);mutations.append(key)
 output={'status':'PASS','scope':'Excludes only actual generic-rank-four maximal plateau (3,3), conditional on pinned actual geometry.',
  'authenticated_originals':ninputs,'source_deficit_survivor':{'R3':'V','R14':pretty(U)},
  'endpoint_degrees':[-30,-6],'plateau_ranks':ranks,'plateau_degrees':fs,
  'quotient_degrees':cs,'determinant_defects':[0]*5,
  'rank_four_slope_window':[-2,6],'new_abstract_candidate_count':len(candidates),
  'cubic_survivor':shape(survivor),'cubic_survivor_character':pretty(target_w),
  'F2_twist4_Euler':pretty(residual),'possible_F2_twist4_H1':[{}, {'1':1}],
  'remaining_genuine_candidates':0,'mutation_controls':mutations,
  'checks':checks}
 return output,results

if __name__=='__main__':
 output,candidates=derive()
 # Output files are independently compared by the caller; no silent rewrite.
 if (ROOT/'CANDIDATES.json').exists():
  require(json.loads((ROOT/'CANDIDATES.json').read_text())==candidates,'candidate artifact consistency')
 print(json.dumps(output,indent=2,sort_keys=True))
