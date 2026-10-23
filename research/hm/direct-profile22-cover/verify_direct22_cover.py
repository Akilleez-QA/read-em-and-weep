"""Standalone exact abstract profile-(2,2) quotient cover.

No imported proof scripts, records, JSON frontier, actual coefficients, points,
maps, matrices or numerical ranks. Inputs are the proved four source bundles,
actual Euler presentations and universally necessary inequalities in PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, hashlib, itertools

ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,label):
    global checks
    checks+=1
    if not ok: raise RuntimeError(label)
def q(a,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def mul(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(n,x):return n*x[0],n*x[1]
def plus(*xs):
    r=q(0)
    for x in xs:r=add(r,x)
    return r
def cp(a,b):return tuple(mul(x,y) for x,y in zip(a,b))
def cs(n,a):return tuple(scale(n,x) for x in a)
def ca(*xs):return tuple(plus(*t) for t in zip(*xs))
phi=q(F(1,2),F(1,2));phip=q(F(1,2),F(-1,2))
tr=(q(2),q(-2),phi,neg(phi),phip,neg(phip),q(1),q(-1),q(0))
weights=(1,1,12,12,12,12,20,20,30)
@lru_cache(None)
def sym(n):
    require(n>=0,'nonnegative symmetric power')
    if n==0:return (q(1),)*9
    if n==1:return tr
    return ca(cp(tr,sym(n-1)),cs(-1,sym(n-2)))
R={ 'one':sym(0),'W':tr,'A':sym(2),'S':sym(3),'D':sym(4),'T':sym(5),
   'P':tuple(q(x) for x in (4,4,-1,-1,-1,-1,1,1,0)) }
R['V']=ca(sym(6),cs(-1,R['P']))
R['Wp']=ca(cp(tr,R['P']),cs(-1,R['T']))
names=('one','W','Wp','A','V','P','S','D','T')
dims={n:int(R[n][0][0]) for n in names}
def inner(a,b):return scale(F(1,120),plus(*(scale(w,mul(x,y)) for w,x,y in zip(weights,a,b))))
def vector(c):
    out=[]
    for n in names:
        a,b=inner(R[n],c)
        require(b==0 and a.denominator==1,'integral exact character')
        out.append(int(a))
    return tuple(out)
zero=(0,)*9
def va(*vs):return tuple(sum(x) for x in zip(*vs)) if vs else zero
def vs(a,b):return tuple(x-y for x,y in zip(a,b))
def unit(n,c=1):return tuple(c if k==n else 0 for k in names)
@lru_cache(None)
def prod(n,d):return vector(cp(R[n],sym(d)))
def chi(bundle,t=0,h0=False):
    out=[]
    for e,n in bundle:
        d=e+t
        if d>=0:out.append(prod(n,d))
        elif not h0 and d<=-2:out.append(tuple(-v for v in prod(n,-d-2)))
    return va(*out)
def degree(B):return sum(e*dims[n] for e,n in B)
def rank(B):return sum(dims[n] for e,n in B)
def shift(B,t):return [(e+t,n) for e,n in B]
def hom(n,e,B):return sum(prod(m,d-e)[names.index(n)] for d,m in B if d>=e)
def parity(n,j):return R[n][1][0]==(-1)**j*R[n][0][0]
for n in names:
    for m in names:require(inner(R[n],R[m])==q(int(n==m)),'orthonormal irreducibles')

# Source names D,P,V,Z denote necessary source types, not occurrences.
sources={
    'D':[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-8,'one')],
    'P':[(-2,'P'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-5,'Wp')],
    'V':[(-2,'V'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-4,'V')],
    'Z':[(-3,'Wp'),(-3,'T'),(-3,'T'),(-4,'V')],
}
M3=[(-1,'Wp')]*3+[(-1,'S')]*3+[(-1,'T')]*6
M4=[(0,'V')]*2+[(0,'P')]*4+[(0,'D')]*3
M2=[(0,'A')]+[(0,'V')]*2+[(0,'P')]*3+[(0,'D')]*4
def euler_E(t):return vs(chi(M3,t),chi(M4,t))
def euler_Qstar(t):return vs(chi(M3,t),chi(M2,t))
def effective(v):return min(v)>=0
def h1(B,t):return vs(chi(B,t,True),chi(B,t))
for E in sources.values():
    require(rank(E)==17 and degree(E)==-54,'source rank and degree')
    require(min(e for e,n in E)>=-8,'source globally generated at twist8')
    for t in range(6):require(chi(E,t)==euler_E(t),'actual source Euler presentation')
four={(1+u,1+v,e,f) for u,v,e,f in itertools.product(range(2),repeat=4) if u+v+e+f==1}
require(four=={(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)},'four source tuple substitution')

def shape_domain(lo=-8,hi=20):
    lines=[(e,'one') for e in range(lo,hi+1) if e%2==0]
    out=list(itertools.combinations_with_replacement(lines,3))
    out += [tuple(sorted(((e,n),L))) for e in range(lo,hi+1) if e%2 for n in ('W','Wp') for L in lines]
    out += [((e,n),) for e in range(lo,hi+1) if e%2==0 for n in ('A','V')]
    return out

def necessary_cover(check_h1=True,primal_endpoint=True,dual_endpoint=True,second_twist=1,lo=-8,hi=20):
    out=set()
    stages=[set() for _ in range(6)]
    for A in shape_domain(lo,hi):
        a=degree(A)
        if a not in (-2,0,2,4):continue
        B=tuple((-e-2,n) for e,n in A)
        pair=(tuple(sorted(A)),tuple(sorted(B)))
        stages[0].add(pair)
        if not any(
            all(any(hom(n,d,[(e,m)]) for d,n in E) for e,m in A)
            and effective(vs(chi(A,2,True),chi(E,2,True)))
            and (not check_h1 or effective(vs(h1(E,2),h1(A,2))))
            for E in sources.values()
        ):continue
        stages[1].add(pair)
        if not effective(vs(chi(A,2),euler_E(2))) or not effective(vs(chi(B,2),euler_Qstar(2))):continue
        stages[2].add(pair)
        if not effective(vs(va(chi(A,3),chi(A,second_twist)),euler_E(3))) or not effective(vs(va(chi(B,3),chi(B,second_twist)),euler_Qstar(3))):continue
        stages[3].add(pair)
        # a=-2 may retain s'=12: no dual endpoint test there.
        if primal_endpoint and a<=2 and not effective(vs(va(chi(A,0,True),chi(A,2),chi(A,4)),euler_E(4))):continue
        stages[4].add(pair)
        # a=4 may retain s=12: no primal endpoint test there.
        if dual_endpoint and a>=0 and not effective(vs(va(chi(B,0,True),chi(B,2),chi(B,4)),euler_Qstar(4))):continue
        stages[5].add(pair)
        out.add(pair)
    return out,stages

expected={
    (((-8,'one'),(2,'one'),(6,'one')),((-8,'one'),(-4,'one'),(6,'one'))),
    (((-8,'one'),(4,'one'),(6,'one')),((-8,'one'),(-6,'one'),(6,'one'))),
    (((-8,'one'),(5,'W')),((-7,'W'),(6,'one'))),
}
survivors,stages=necessary_cover()
require(survivors==expected,'complete necessary cover equals three explicit pairs')
for A,B in survivors:
    a=degree(A);b=degree(B)
    require(a in (0,2) and b==-6-a,'terminal pair degree')
    require(2*a+4<12 and 8-2*a<12,'both second defects vanish for terminal pairs')

# Counterfactual controls are witnesses to indispensable implications, not new
# conclusions about actual maps. No asserts are removed by optimized Python.
mutation_controls=[]
def rejects(label,predicate):
    require(predicate,label)
    mutation_controls.append(label)
without_h1,_=necessary_cover(check_h1=False)
rejects('omitting H1 quotient condition changes exact cover',without_h1!=expected)
rejects('seven-W obstruction reappears without H1 condition',(((-7,'W'),(16,'one')),((-18,'one'),(5,'W'))) in without_h1)
rejects('double-octic obstruction reappears without H1 condition',(((-8,'one'),(-8,'one'),(14,'one')),((-16,'one'),(6,'one'),(6,'one'))) in without_h1)
without_endpoints,_=necessary_cover(primal_endpoint=False,dual_endpoint=False)
rejects('omitting endpoint inequalities changes exact cover',without_endpoints!=expected)
wrong_twist,_=necessary_cover(second_twist=2)
rejects('incorrect cotangent twist changes exact cover',wrong_twist!=expected)
rejects('missing terminal pair fails exact equality',set(sorted(survivors)[:-1])!=expected)
larger,_=necessary_cover(lo=-10,hi=26)
require(larger==expected,'safe wider-domain cross-check')
wrong_expected=set(expected)
wrong_expected.remove((((-8,'one'),(5,'W')),((-7,'W'),(6,'one'))))
wrong_expected.add((((-8,'one'),(5,'Wp')),((-7,'Wp'),(6,'one'))))
rejects('swapping physically marked doublets fails exact equality',survivors!=wrong_expected)

result={
    'status':'pass','checks':checks,'mutation_controls':mutation_controls,
    'source_types':['D','P','V','Z'],'intrinsic_A_window':[-8,20],
    'degree_A':[-2,0,2,4],
    'survivors':[{'A':A,'B':B} for A,B in sorted(survivors)],
    'scope':'Necessary abstract equivariant quotient cover only, conditional on the pinned actual four-source theorem and maximal profile (2,2). Not a realization, actual rank computation or standalone global SF bound.',
}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

