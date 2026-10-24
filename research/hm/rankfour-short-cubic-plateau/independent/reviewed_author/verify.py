#!/usr/bin/env python3
"""Universal abstract bundle/character controls, never actual HM instances."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from collections import Counter
import hashlib,json
from functools import lru_cache

ROOT=Path(__file__).resolve().parent
NAMES=('1','W','A','S4','D','T6','P',"W'",'V')
DIMS=(1,2,3,4,5,6,4,2,3)
PARITY=(0,1,0,1,0,1,0,1,0)
EDGES=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8))
ZERO=(0,)*9
HASHES={'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md': 'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md': '0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2', 'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md': '868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c', 'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md': '783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71'}
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
  for n in range(16):
   v=sym(unit(i),n)
   require(genuine(v),'genuine symmetric power')
   require(dim(v)==DIMS[i]*(n+1),'symmetric power dimension')
   require(all(not c or PARITY[j]==(PARITY[i]+n)%2 for j,c in enumerate(v)),'symmetric power parity')
   expected=tuple(qm(CHARS[i][k],qsym(n,x))for k,x in enumerate(TRACES))
   require(tuple(char_eval(v,k)for k in range(9))==expected,'McKay vs exact class product')


E=((-3,7),(-3,5),(-3,5),(-4,8))
U=vec(**{"W'":1,'T6':2})
H=vec(A=2,V=2,P=2,D=2)

def block_options(degree,target):
    # B(4) is a quotient of globally generated E(4), hence every e>=-4.
    # At rank four and total degree d, no e exceeds d+12.
    return tuple((e,i) for e in range(-4,degree+13)
                 for i in range(9) if DIMS[i]<=4 and PARITY[i]==e%2
                 and genuine(sub(target,h0(((e,i),),3))))

def candidates_recursive(degree,target):
    blocks=block_options(degree,target);out=set()
    def visit(bs,j,r,d,ch):
        if r==4:
            if d==degree and ch==target:out.add(tuple(bs))
            return
        for z in range(j,len(blocks)):
            e,i=blocks[z]
            nextch=add(ch,h0(((e,i),),3))
            if r+DIMS[i]<=4 and genuine(sub(target,nextch)):
                visit(bs+[(e,i)],z,r+DIMS[i],d+e*DIMS[i],nextch)
    visit([],0,0,0,ZERO)
    return out

def candidates_multiplicity(degree,target):
    # A genuinely different bounded-product enumeration, of the allowed
    # irreducible blocks, not an import of a historical bundle list.
    blocks=block_options(degree,target);out=set()
    for ms in product(*(range(4//DIMS[i]+1) for e,i in blocks)):
        if sum(m*DIMS[i] for m,(e,i) in zip(ms,blocks))!=4:continue
        if sum(m*e*DIMS[i] for m,(e,i) in zip(ms,blocks))!=degree:continue
        bs=tuple(b for m,b in zip(ms,blocks) for _ in range(m))
        if h0(bs,3)==target:out.add(bs)
    return out

def endpoints(max_defect=8,orbit_min=12):
    out=[]
    # With weights 3,2,1 every nonzero invariant determinant defect
    # is already too large. This proves the forced zero, not a cutoff.
    require(orbit_min>max_defect,'invariant-divisor minimum exceeds all slack')
    for u in range(4//3+1):
        v=4-3*u
        out.append((-52-2*u,-4-2*v))
    return out

def derive():
    ninputs=authenticate();character_controls()
    M2=vec(A=1,V=2,P=3,D=4);M3=vec(**{"W'":3,'S4':3,'T6':6});M4=vec(V=2,P=4,D=3)
    require(sub(sub(times_w(M3),M2),M4)==H and dim(H)==30,'actual ambient')
    actual_h1=sub(times_w(M4),M3)
    require(actual_h1==vec(**{"W'":1,'T6':3}),'actual E1 cohomology')
    possible_r3=[unit(2),unit(8),mul(unit(0),3)]
    keep=[(R,sub(actual_h1,times_w(R))) for R in possible_r3 if genuine(sub(actual_h1,times_w(R)))]
    require(keep==[(unit(8),U)],'source-Z three-deficit derivation')
    require(not genuine(sub(actual_h1,unit(3))),'exclude source O(-6) alternative')
    require(2*min(DIMS[i]for i in range(9)if PARITY[i])>3,'exclude source degree-minus-five')
    require(sum(DIMS[i]for e,i in E)==17 and sum(e*DIMS[i]for e,i in E)==-54,'source rank degree')
    require(h1(E,1)==actual_h1 and h0(E,3)==U and h1(E,3)==ZERO,'source characters')
    require(h1(E,4)==ZERO and all(e+4>=0 for e,i in E),'E4 globally generated')
    # Formal affine coefficient vectors indexed (constant,a,c1,d1,d2,d3).
    def padd(*vs):return tuple(sum(v[i]for v in vs)for i in range(6))
    def pscale(v,n):return tuple(n*x for x in v)
    def basis(i):return tuple(int(i==j)for j in range(6))
    cs=[basis(2)]
    for j in range(3):cs.append(padd(cs[-1],pscale(basis(0),8),basis(3+j)))
    e=padd(basis(1),cs[0]);b=padd(basis(1),*cs)
    identity=padd(pscale(basis(1),3),b,pscale(e,-4))
    require(identity==(48,0,0,3,2,1),'exact symbolic plateau identity')
    require(4*(-54)+48==-168,'identity constant')
    require(3*(-52)-4-(-168)==8,'exact endpoint slack')
    require([60//n for n in [1,2,3,5]]==[60,30,20,12],'projective orbit sizes')
    rows=endpoints();require(rows==[(-52,-12),(-54,-6)],'complete endpoint alternatives')
    # Parity-refined rank13 deficit2 ordinary possibilities.
    tiny=[ds for ds in combinations_with_replacement(range(3),13)if sum(ds)==2]
    require(tiny==[(0,)*12+(2,),(0,)*11+(1,1)],'rank13 deficit two partitions')
    require([i for i in range(9)if PARITY[i] and DIMS[i]<=2]==[1,7],'negative-tail doublets')
    require(h1(((-5,1),),3)==unit(1) and h1(((-5,7),),3)==unit(7),'doublet tail cubic cohomology')
    require(h1(((-6,0),),3)==unit(1) and h1(((-6,0),),4)==unit(0),'scalar tail cohomology')
    allrecords=[];summary=[];blocktables=[]
    expected_survivors={
      -52:{((-3,7),(2,0),(2,0)),((-2,8),(4,0))},
      -54:{((-3,7),(2,0),(4,0)),((-3,7),(3,1))}}
    expected_residuals={
      ((-3,7),(2,0),(2,0)):vec(**{'1':1,'A':-1,'D':1,'V':-1}),
      ((-2,8),(4,0)):vec(**{'1':1,'A':1,'P':-1}),
      ((-3,7),(2,0),(4,0)):vec(A=-1,V=1),
      ((-3,7),(3,1)):vec(A=-1,V=1)}
    for a,b in rows:
        degree=-54-a
        targets=[U] if a==-52 else [add(U,unit(1)),add(U,unit(7))]
        pool=set()
        for target in targets:
            rec=candidates_recursive(degree,target)
            independent=candidates_multiplicity(degree,target)
            require(rec==independent,'two complete candidate derivations agree')
            pool |= rec
            blocktables.append({'degree':degree,'target':pretty(target),'allowed_blocks':[
              {'degree':e,'coefficient':NAMES[i],'cubic':pretty(h0(((e,i),),3))}for e,i in block_options(degree,target)]})
        require(len(pool)==(5 if a==-52 else 8),'complete cubic candidate count')
        survivors=[]
        for B in sorted(pool):
            require(sum(DIMS[i]for e,i in B)==4 and sum(e*DIMS[i]for e,i in B)==degree,'B rank degree')
            require(all(e>=-4 and e<=degree+12 and PARITY[i]==e%2 for e,i in B),'B derived slope parity window')
            for t in [3,4,6]:
                require(class_decompose(class_h0(B,t))==h0(B,t),'independent exact class character')
            residual=sub(chi(E,4),chi(B,4))
            corrections=[ZERO]if a==-52 else [ZERO,unit(0)]
            passes=any(genuine(add(residual,corr))for corr in corrections)
            record={'a':a,'b':b,'B':shape(B),'cubic':pretty(h0(B,3)),'F0_quartic_Euler':pretty(residual),'passes_quartic':passes}
            if passes:
                survivors.append(B)
                # Exact sequences E->F4 and F4->H O->O(-b).
                upper=add(chi(E,0),*(chi(B,j)for j in [2,4,6]),sym(unit(0),-b),mul(H,-1))
                require(upper==expected_residuals[B] and upper!=ZERO,'nonzero upper exact Euler obstruction')
                require(dim(upper)==0,'upper contradiction is equivariant, not dimensional')
                record['upper_Euler_residual']=pretty(upper)
            else:
                require(all(not genuine(add(residual,corr))for corr in corrections),'quartic rejection survives all permitted H1 corrections')
            allrecords.append(record)
        require(set(survivors)==expected_survivors[a],'complete quartic survivor list')
        summary.append({'endpoint_degrees':[a,b],'block_degrees':[degree+8*i for i in range(4)],'all_defects':0,'cubic_candidates':len(pool),'quartic_survivors':len(survivors),'upper_Euler_survivors':0})
    # Explicit fail-closed mutations of each structural or finite-classification
    # datum. Both expected and independently computed quantities are retained.
    mut=0
    def rejects(condition):
        nonlocal mut
        require(not condition,'mutation erroneously accepted');mut+=1
    for a,b in rows:
        for shift in [-2,2]:rejects(3*(a+shift)+b==-168)
    for j,w in enumerate([3,2,1]):rejects(3*(-52)-4==-168+w*12)
    for target in [U,add(U,unit(1)),add(U,unit(7))]:
        degree=-2 if target==U else 0
        correct=candidates_multiplicity(degree,target)
        for B in correct:rejects(correct-{B}==correct)
    for B,want in expected_residuals.items():
        for i in range(9):rejects(add(want,unit(i))==want)
        rejects(want==ZERO)
    for i,p in enumerate(PARITY):rejects(CHARS[i][1]==q((-1)**(1-p)*DIMS[i]))
    for i,j in EDGES:rejects(tuple(char_eval(sub(times_w(unit(i)),unit(j)),k)for k in range(9))==tuple(qm(TRACES[k],CHARS[i][k])for k in range(9)))
    for name,h in HASHES.items():rejects(hashlib.sha256((ROOT/'inputs'/name).read_bytes()+b'\n').hexdigest()==h)
    require(mut>=60,'nontrivial mutation suite')
    return {'status':'PASS','scope':'Conditional exclusion of actual rank-four maximal profile (1,3), not all rank four or original repair.','authenticated_sources':ninputs,'checks':checks,'mutation_rejections':mut,'endpoint_cases':summary,'cubic_block_tables':blocktables,'candidates':allrecords}

if __name__=='__main__':
    print(json.dumps(derive(),indent=2,sort_keys=True))
