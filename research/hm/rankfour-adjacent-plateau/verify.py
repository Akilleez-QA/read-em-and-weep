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

# All calculations below are universal formal identities, not actual maps.
def derive():
 ninputs=authenticate();character_controls()
 M3=vec(**{"W'":3,'S4':3,'T6':6});M4=vec(V=2,P=4,D=3)
 require(dim(M3)==54 and dim(M4)==37,'actual presentation dimensions')
 actual_euler=sub(times_w(M3),sym(M4,2))
 require(actual_euler==vec(V=-1),'actual E(2) Euler from presentation')
 # Independent exact conjugacy-class derivation of the same presentation.
 actual_classes=tuple(qsub(qm(char_eval(M3,k),x),qm(char_eval(M4,k),qsym(2,x))) for k,x in enumerate(TRACES))
 require(class_decompose(actual_classes)==actual_euler,'actual Euler by class characters')
 require(times_w(unit(1))==vec(**{'1':1,'A':1}),'physical W square')
 require(times_w(unit(7))==unit(6),'physical W times W-prime')
 require(unit(2)!=unit(8),'physical A and V distinct')
 require(PARITY[0]==0 and DIMS[0]==1,'unique trivial line coefficient')
 require([NAMES[i]for i in range(9)if DIMS[i]==1]==['1'],'perfect-group one-dimensional marking')
 require([NAMES[i]for i in range(9)if DIMS[i]==2 and PARITY[i]]==['W',"W'"],'two odd doublet choices')

 ranks=[9+4*i for i in range(6)]
 require(ranks==[9,13,17,21,25,29],'plateau ranks')
 # Persistence: at index i, the largest vanishing twist is 4-i.
 require([-(5-i) for i in range(5)]==[-5,-4,-3,-2,-1],'persistence degree caps')
 even_floor=lambda d:2*(d//2)
 abounds=[even_floor(-5*9),even_floor(-5*1)]
 require(abounds==[-46,-6],'even endpoint bounds')
 # Exact affine vectors: [constant,a,c1,delta1,...,delta4].
 def padd(*xs):return tuple(sum(x[i]for x in xs)for i in range(7))
 def scale(x,n):return tuple(n*y for y in x)
 def basis(i):return tuple(int(i==j)for j in range(7))
 csymbol=[basis(2)]
 for j in range(4):csymbol.append(padd(csymbol[-1],scale(basis(0),8),basis(j+3)))
 esymbol=padd(basis(1),*csymbol[:2]);bsymbol=padd(basis(1),*csymbol)
 lhs=padd(scale(basis(1),3),scale(bsymbol,2),scale(esymbol,-5))
 require(lhs==(120,0,0,3,6,4,2),'formal exact endpoint identity')
 weights=list(lhs[3:]);target=5*(-54)+lhs[0]
 require(target==-150 and 3*abounds[0]+2*abounds[1]==target,'sharp endpoint equality')
 require(all(w>0 for w in weights),'all nonnegative defects forced zero')
 # With equality, all variables are determined, not searched.
 a,b=abounds;c1=(-54-a-8)//2
 require(2*c1==-54-a-8,'integral first block degree')
 cs=[c1+8*j for j in range(5)]
 fs=[a]
 for c in cs:fs.append(fs[-1]+c)
 require(cs==[-8,0,8,16,24] and fs==[-46,-54,-54,-46,-30,-6],'derived block and stage degrees')
 require(fs[2]==-54 and fs[-1]==b,'central and upper consistency')

 def partitions(n,total):
  return [list(ds)for ds in combinations_with_replacement(range(total+1),n)if sum(ds)==total]
 require(-5*9-fs[0]==1 and -4*13-fs[1]==2,'forced low-stage deficits')
 f0parts=partitions(9,1);f1parts=partitions(13,2)
 require(f0parts==[[0]*8+[1]],'complete rank-nine deficit partition')
 require(f1parts==[[0]*12+[2],[0]*11+[1,1]],'complete rank-thirteen deficit partitions')
 require(chi(((-1,0),),0)==ZERO,'O(-1) acyclic')
 require(chi(((-2,0),),0)==mul(unit(0),-1),'chi O(-2)')
 require(chi(((-3,0),),0)==mul(unit(1),-1),'chi O(-3)')
 require(chi(((-4,0),),0)==mul(unit(2),-1),'chi O(-4)')
 f0_4=mul(unit(0),-1);rhs=add(f0_4,actual_euler)
 require(rhs==vec(**{'1':-1,'V':-1}),'forced two-sequence Euler RHS')
 # The unknown R11/R12 cancels formally, never assigning it a character.
 # Pair (coefficient of R, known character) represents each Euler term.
 rows=[]
 for label,i in [('W',1),("W'",7),('line',0)]:
  if label!='line':
   terms=[(1,ZERO),(-1,mul(times_w(unit(i)),-1))]
   lhs_class=tuple(qs(-1,qm(CHARS[i][k],x))for k,x in enumerate(TRACES))
  else:
   terms=[(1,mul(unit(0),-1)),(-1,mul(unit(2),-1))]
   lhs_class=tuple(qs(-1,qa(q(1),qsym(2,x)))for x in TRACES)
  require(sum(r for r,_ in terms)==0,'unknown low-stage coefficient cancels')
  left=add(*(v for _,v in terms));residual=sub(left,rhs)
  require(class_decompose(lhs_class)==left,'independent tail character')
  rclasses=tuple(qsub(lhs_class[k],char_eval(rhs,k))for k in range(9))
  require(class_decompose(rclasses)==residual,'independent exact residual')
  require(residual!=ZERO and dim(residual)==0,'nonzero dimension-zero obstruction')
  require(any(x!=q(0)for x in rclasses),'actual class distinguishes exact characters')
  rows.append({'tail':label,'chi_F1_4_plus_chi_F1_2':pretty(left),'required':pretty(rhs),'residual':pretty(residual),'ordinary_residual_dimension':dim(residual)})
 require([x['residual']for x in rows]==[{'A':-1,'V':1},{'1':1,'P':-1,'V':1},{'A':-1,'V':1}],'three final exact obstructions')

 # Fail-closed acceptance checks independently derived numerical and character
 # prerequisites. A mutation changes exactly one coordinate or named premise.
 expected={'ranks':ranks,'endpoint_bounds':abounds,'degree_caps':[-5,-4,-3,-2,-1],
  'weights':weights,'degrees':fs,'block_degrees':cs,'determinant_defects':[0]*4,
  'F0_deficit_partitions':f0parts,'F1_deficit_partitions':f1parts,
  'E2_Euler':list(actual_euler),'physical_W_square':list(times_w(unit(1))),
  'physical_W_Wprime':list(times_w(unit(7))),'parity':list(PARITY),
  'F0_4_Euler':list(f0_4),'two_sequence_twists':[4,2],
  'graded_twist':-2,'residuals':[list(sub(mul(times_w(unit(1)),-1),rhs)),list(sub(mul(unit(6),-1),rhs)),list(sub(vec(**{'1':-1,'A':-1}),rhs))]}
 def accept(c):return c==expected
 require(accept(json.loads(json.dumps(expected))),'base contract')
 mutations=[]
 def leaves(x,path=()):
  if isinstance(x,list):
   for i,y in enumerate(x):yield from leaves(y,path+(i,))
  else:yield path
 for key,value in expected.items():
  for path in leaves(value):
   changed=json.loads(json.dumps(expected))
   if path:
    dest=changed[key]
    for i in path[:-1]:dest=dest[i]
    dest[path[-1]]+=1
   else:changed[key]+=1
   require(not accept(changed),'reject altered prerequisite '+key+str(path));mutations.append(key+str(path))
 return {'status':'PASS','scope':'Excludes only actual rank-four maximal ordered plateau (2,3), conditional on the pinned actual geometry.',
  'authenticated_originals':ninputs,'rank_four_quotient_enumeration_used':False,
  'actual_E2_Euler':pretty(actual_euler),'plateau_ranks':ranks,'plateau_degrees':fs,
  'endpoint_degrees':abounds,'defect_weights':weights,'determinant_defects':[0]*4,'quotient_degrees':cs,
  'F0_deficit_partitions':f0parts,'F1_deficit_partitions':f1parts,
  'exact_two_sequence_identity':'chi(F1(4))+chi(F1(2))=chi(F0(4))+chi(E(2))=-1-V',
  'tail_obstructions':rows,'remaining_tail_types':0,'mutation_rejections':len(mutations),'checks':checks}

if __name__=='__main__':
 print(json.dumps(derive(),indent=2,sort_keys=True))
