#!/usr/bin/env python3
"""Portable universal character and bundle audit; no actual map is evaluated."""
from fractions import Fraction as Q
from math import comb, ceil
from itertools import combinations_with_replacement, product
from collections import Counter
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parent
NAMES=('1','W','A','S4','D5','T6','P4',"W'",'V')
DIMS=(1,2,3,4,5,6,4,2,3)
PARITY=(0,1,0,1,0,1,0,1,0)
WEIGHTS=(1,1,12,12,12,12,20,20,30)
CHECKS=0
SOURCE_HASHES={
 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
 'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md':'0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2',
 'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md':'868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c',
 'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md':'783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71'}

def check(cond,label):
 global CHECKS
 CHECKS+=1
 if not cond: raise AssertionError(label)
def q(a,b=0):return (Q(a),Q(b))
def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(x,a):return (a*x[0],a*x[1])
def times(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def power(x,n):
 r=q(1)
 for _ in range(n):r=times(r,x)
 return r
def total(xs):
 r=q(0)
 for x in xs:r=plus(r,x)
 return r
X=(q(2),q(-2),q(Q(1,2),Q(1,2)),q(Q(-1,2),Q(-1,2)),q(Q(1,2),Q(-1,2)),q(Q(-1,2),Q(1,2)),q(1),q(-1),q(0))
# Closed binomial polynomial, not a McKay or symmetric-power recurrence.
def sym_at(n,x):
 if n<0:return q(0)
 return total(scale(power(x,n-2*k),(-1)**k*comb(n-k,k)) for k in range(n//2+1))
CHARS=[tuple(sym_at(i,x) for x in X) for i in range(6)]
CHARS.append(tuple(q(z) for z in (4,4,-1,-1,-1,-1,1,1,0)))
CHARS.append(tuple(plus(times(x,p),scale(t,-1)) for x,p,t in zip(X,CHARS[6],CHARS[5])))
CHARS.append(tuple(plus(sym_at(6,x),scale(p,-1)) for x,p in zip(X,CHARS[6])))
ZERO=(0,)*9

def u(i):return tuple(int(i==j) for j in range(9))
def v(**kw):return tuple(kw.get(n,0) for n in NAMES)
def add(*vs):return tuple(sum(x[i] for x in vs) for i in range(9))
def neg(x):return tuple(-a for a in x)
def sub(x,y):return add(x,neg(y))
def dim(x):return sum(a*b for a,b in zip(x,DIMS))
def genuine(x):return all(a>=0 for a in x)
def evalv(v):return tuple(total(scale(CHARS[i][j],v[i]) for i in range(9)) for j in range(9))
def decompose(ch):
 out=[]
 for i in range(9):
  z=total(scale(times(ch[j],CHARS[i][j]),Q(WEIGHTS[j],120)) for j in range(9))
  check(z[1]==0 and z[0].denominator==1,'integral character decomposition')
  out.append(int(z[0]))
 return tuple(out)
CACHE={}
def tensor_sym(coeff,n):
 key=(coeff,n)
 if key not in CACHE:
  cc=evalv(coeff)
  CACHE[key]=decompose(tuple(times(cc[j],sym_at(n,X[j])) for j in range(9)))
 return CACHE[key]
def h0(B,t):return add(*(tensor_sym(u(i),e+t) for e,i in B if e+t>=0))
def h1(B,t):return add(*(tensor_sym(u(i),-e-t-2) for e,i in B if e+t<=-2))
def chi(B,t):return sub(h0(B,t),h1(B,t))
def show(x):return {n:a for n,a in zip(NAMES,x) if a}
def shape(B):return [{'degree':e,'coefficient':NAMES[i]} for e,i in B]

# Enumerate ordinary four-line degree multisets, then decorate each degree.
def decorations(r,parity):
 ids=[i for i in range(9) if PARITY[i]==parity and DIMS[i]<=r]
 for ms in product(*(range(r//DIMS[i]+1) for i in ids)):
  if sum(m*DIMS[i] for i,m in zip(ids,ms))==r:
   yield tuple(i for i,m in zip(ids,ms) for _ in range(m))
def candidates(degree):
 out=set()
 for ds in combinations_with_replacement(range(-4,degree+13),4):
  if sum(ds)!=degree:continue
  counts=Counter(ds);levels=sorted(counts)
  for dec in product(*(tuple(decorations(counts[e],e%2)) for e in levels)):
   out.add(tuple((e,i) for e,ii in zip(levels,dec) for i in ii))
 return out
# A separate rank-budget recursion cross-checks completeness and endpoints.
def candidates_by_blocks(degree):
 blocks=[(e,i) for e in range(-4,degree+13) for i in range(9) if DIMS[i]<=4 and PARITY[i]==e%2]
 out=set()
 def rec(start,B,r,d):
  if r==4:
   if d==degree:out.add(tuple(B))
   return
  for j in range(start,len(blocks)):
   e,i=blocks[j]
   if r+DIMS[i]<=4:rec(j,B+[(e,i)],r+DIMS[i],d+e*DIMS[i])
 rec(0,[],0,0)
 return out

def authenticate():
 rows=json.loads((ROOT/'INPUTS.json').read_text())
 check(len(rows)==4 and {Path(z['file']).name for z in rows}==set(SOURCE_HASHES),'complete source registry')
 for z in rows:
  name=Path(z['file']).name;raw=(ROOT/z['file']).read_bytes()
  check(hashlib.sha256(raw).hexdigest()==z['sha256']==SOURCE_HASHES[name],'source SHA256')
  check(len(raw)==z['bytes'],'source byte count')
  check(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==z['git_blob_sha1'],'source Git blob')
  check(z['ref']=='db51525015bb7c5e825833d550d08dedf6f6ea96','immutable source ref')
  check(z['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+z['ref']+'/'+z['path'],'source URL')
 return len(rows)

def audit():
 authenticated=authenticate()
 for i,c in enumerate(CHARS):
  check(c[0]==q(DIMS[i]),'dimension fixed')
  check(c[1]==q((-1)**PARITY[i]*DIMS[i]),'central parity fixed')
  check(decompose(c)==u(i),'orthonormal class characters')
 check(sum(d*d for d in DIMS)==120 and sum(WEIGHTS)==120,'group-order controls')
 for i in range(9):
  for n in range(25):
   s=tensor_sym(u(i),n)
   check(dim(s)==DIMS[i]*(n+1) and genuine(s),'symmetric-product dimension/genuineness')
   check(all(not a or PARITY[j]==(PARITY[i]+n)%2 for j,a in enumerate(s)),'product parity')
 check(tensor_sym(u(0),2)==u(2),'fixed W gives A, not V')
 check(tensor_sym(u(8),1)==u(5),'fixed V times W is T6')
 check(tensor_sym(u(7),1)==u(6),'fixed W-prime times W is P4')
 M2=v(A=1,V=2,P4=3,D5=4);M3=v(**{"W'":3,'S4':3,'T6':6});M4=v(V=2,P4=4,D5=3)
 H=sub(sub(tensor_sym(M3,1),M2),M4)
 check(H==v(A=2,V=2,P4=2,D5=2),'actual ambient character')
 actual_h1=sub(tensor_sym(M4,1),M3)
 check(actual_h1==v(**{"W'":1,'T6':3}),'actual H1E1')
 # New, direct deficit-three argument, not the historical 28-type search.
 R4_options=[v(**{'1':3}),u(2),u(8)]
 good=[r for r in R4_options if genuine(sub(actual_h1,tensor_sym(r,1)))]
 check(good==[u(8)],'rank-three degree-four source coefficient')
 check(not genuine(sub(actual_h1,u(3))),'degree-six source line rejected')
 E=((-4,8),(-3,5),(-3,5),(-3,7))
 U=v(**{"W'":1,'T6':2})
 check(h0(E,3)==U and h1(E,3)==ZERO,'source cubic data')
 for t in range(-2,9):
  presentation=sub(tensor_sym(M3,t-1) if t>=1 else neg(tensor_sym(M3,-t-1)) if t<=-1 else ZERO,
                   tensor_sym(M4,t) if t>=0 else neg(tensor_sym(M4,-t-2)) if t<=-2 else ZERO)
  check(chi(E,t)==presentation,'source split vs actual presentation Euler')
 # Endpoint defects are effective invariant divisors; every positive value >=12.
 budget=3*(-52)+(-4)-(-168)
 check(budget==8 and all(w*min(12,20,30)>budget for w in (3,2,1)),'every possible positive weighted defect exceeds budget8')
 lower_a=ceil(Q(-168+4,3))
 check(lower_a==-54,'endpoint lower bound derived from b<=-4')
 endpoints=[(a,-168-3*a) for a in range(lower_a,-51) if a%2==0 and -168-3*a<=-4]
 check(endpoints==[(-54,-6),(-52,-12)],'complete even endpoint domain')
 rows=[];summaries=[]
 for a,b in endpoints:
  degree=-54-a; domain=candidates(degree)
  check(domain==candidates_by_blocks(degree),'two independent complete domain enumerations')
  check(len(domain)==(37 if degree==-2 else 50),'complete necessary domain count')
  check(((-4,0),(-4,0),(-4,0),(degree+12,0)) in domain,'upper slope endpoint is included')
  cubic=[];quartic=[];full=[]
  for B in sorted(domain):
   check(all(e>=-4 and e<=degree+12 and PARITY[i]==e%2 for e,i in B),'necessary slope and parity domain')
   check(sum(DIMS[i] for e,i in B)==4 and sum(e*DIMS[i] for e,i in B)==degree,'rank-degree domain')
   check(h1(B,3)==ZERO and h1(B,4)==ZERO,'cubic/quartic B tails vanish')
   Xc=sub(h0(B,3),U)
   cubic_ok=Xc in ([ZERO] if a==-52 else [u(1),u(7)])
   if not cubic_ok:continue
   cubic.append(B)
   r4=sub(chi(E,4),chi(B,4))
   corrections=[ZERO] if a==-52 else [ZERO,u(0)]
   quartic_ok=any(genuine(add(r4,c)) for c in corrections)
   detail={'endpoint_degrees':[a,b],'B':shape(B),'cubic_excess':show(Xc),'F0_twist4_Euler':show(r4),'quartic_pass':quartic_ok}
   if quartic_ok:
    quartic.append(B)
    # Difference RHS - LHS of H=E+B(2)+B(4)+B(6)+O(-b).
    residuals={str(t):add(chi(E,t),chi(B,t+2),chi(B,t+4),chi(B,t+6),tensor_sym(u(0),t-b),neg(tensor_sym(H,t))) for t in range(5)}
    check(all(dim(z)==0 for z in residuals.values()),'Euler residual has zero ordinary dimension')
    detail['full_Euler_residuals']={t:show(z) for t,z in residuals.items()}
    detail['H1_E_twist0']=show(h1(E,0))
    detail['H1_B_twist2']=show(h1(B,2))
    check(residuals['0']!=ZERO,'full Euler twist0 excludes survivor')
    if residuals['0']==ZERO:full.append(B)
   rows.append(detail)
  summaries.append({'endpoint_degrees':[a,b],'B_degree':degree,'slope_window':[-4,degree+12],
                    'domain_count':len(domain),'cubic_count':len(cubic),'quartic_count':len(quartic),'full_Euler_survivors':len(full)})
 check(sum(x['quartic_count'] for x in summaries)==4,'exactly four cubic/quartic survivors')
 # These controls exercise errors that scalar rank/degree checks cannot see.
 check(sum(x['cubic_count'] for x in summaries)>4,'quartic filter is active')
 check(chi(E,0)!=h0(E,0),'omitting source H1 is detected')
 check(h1(((-4,0),),2)==u(0) and chi(((-4,0),),2)==neg(u(0)),'negative degree B(2) tail sign control')
 check(H!=v(A=4,V=0,P4=2,D5=2),'fixed representation marking cannot be collapsed')
 return {'status':'PASS','scope':'Necessary universal data exclude only actual generic-rank-four maximal plateau (1,3).',
         'authenticated_sources':authenticated,'ambient_character':show(H),'endpoint_cases':summaries,'cubic_candidates':rows,'checks':CHECKS,
         'method':'Independent exact conjugacy-class arithmetic using closed binomial symmetric polynomials; independent ordinary-line and irreducible-block candidate enumerations.'}

if __name__=='__main__':
 out=audit()
 print(json.dumps(out,indent=2,sort_keys=True))
