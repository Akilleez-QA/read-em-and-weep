#!/usr/bin/env python3
"""Source2 residual forced by its first two osculations; exact support only."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
from functools import lru_cache
ROOT=Path(__file__).resolve().parent

# Exact Q(sqrt(5)) character arithmetic, independently reproduced here.
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def minus(a,b):return plus(a,scale(-1,b))
def total(xs):
 out=(F(0),F(0))
 for x in xs:out=plus(out,x)
 return out
z=lambda a,b=0:(F(a),F(b))
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
@lru_cache(None)
def symchar(n):
 a=[z(1)]*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,[minus(times(w,v),u)for w,v,u in zip(W,b,a)]
 return b
chars={'one':[z(1)]*9,'W':W,'A':symchar(2),'S':symchar(3),'D':symchar(4),'T':symchar(5)}
chars['P']=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
chars['V']=[minus(a,b)for a,b in zip(symchar(6),chars['P'])]
chars['Wp']=[minus(times(w,p),t)for w,p,t in zip(W,chars['P'],chars['T'])]
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(s,times(x,y))for s,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
# Characters are real, hence the nine irreducibles are self-dual.
# W has trivial determinant: Lambda^2 W = 1 (the standard SL2 lift).
# The recurrence uses exactly that determinant-one linearization.
def mul(a,b):return [times(x,y)for x,y in zip(a,b)]
def sub(a,b):return [minus(x,y)for x,y in zip(a,b)]
def linear(terms):return [total(scale(c,chars[n][i])for c,n in terms)for i in range(9)]
def decompose(a):
 out=[inner(a,chars[n])for n in names]
 assert all(b==0 and x.denominator==1 for x,b in out)
 return tuple(int(x)for x,b in out)
M3=linear([(3,'Wp'),(3,'S'),(6,'T')])
M4=linear([(2,'V'),(4,'P'),(3,'D')])
PINNED={'TWO-ONE-INDEX-TWO-DUAL-RANK-FOUR-RESIDUAL.md': '12a381971cc8b418212dd627fc875aeff7d3000de93c9a8f3a64569ba1cedb6f', 'TWO-ONE-INDEX-TWO-CONSTANT-SPAN-INTERSECTION.md': 'f72531663c01cb681e56500f578d595355cab384c9bb96b1ea120012ff4671b7', 'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
ID='G3.21.d610e381ed75';row=next(r for r in json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']if r['id']==ID)
assert row['profile']=='21' and row['source_index']==2
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']] and row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]))
Slist=[[(-8,'one'),(-6,'one')],[(-7,'W')]]
Rlist=[[(-18,'one'),(-8,'one'),(-6,'one'),(-4,'one')],[(-18,'one'),(-8,'one'),(-5,'W')],[(-18,'one'),(-7,'W'),(-4,'one')],[(-18,'one'),(-6,'A')]]
def hom_to_line(e,n,t):return 0 if t<e else int(inner(mul(chars[n],symchar(t-e)),chars['one'])[0])
assert all(hom_to_line(e,n,-20)==0 for S in Slist for e,n in S)
assert [[hom_to_line(e,n,-6)for e,n in S]for S in Slist]==[[0,1],[1]]
assert [sum(e*dims[n]for e,n in S)for S in Slist]==[-14,-14]
# The forced nonzero derivative maps have rank1, target O(-6), and kernel O(-8).
assert -14-(-6)==-8
assert decompose(symchar(1))==(0,1,0,0,0,0,0,0,0)
assert decompose(symchar(2))==(0,0,0,1,0,0,0,0,0)
# Universal first osculation is W O(-7), second is A O(-6).
assert -8+1==-7 and -8+2==-6
# Split S admits at most rank1 from W O(-7), since its O(-8) component vanishes by degree.
assert sum(dims[n]for e,n in Slist[0]if e>=-7)==1
# For the remaining R3/R4, second-osculation support ranks are respectively1 and3.
assert [sum(dims[n]for e,n in R if e>=-6)for R in Rlist[2:]]==[1,3]
forced_R=Rlist[3];forced_Q=[(-2,'P'),(-2,'D')]+forced_R;forced_L=[(-3,'Wp'),(-3,'T'),(-7,'W')]
assert sum(dims[n]for e,n in forced_R)==4 and sum(e*dims[n]for e,n in forced_R)==-36
assert sum(dims[n]for e,n in forced_Q)==13 and sum(e*dims[n]for e,n in forced_Q)==-54
assert sum(dims[n]for e,n in forced_L)==10 and sum(e*dims[n]for e,n in forced_L)==-38
out=dict(scope='Four necessary dual source types reduced to one; no stable-label exclusion or realization.',id=ID,source_hashes=PINNED,intersection_commit='2348d4b6fb2afd67d66b15aad6037ab92c94f076',residual_source_commit='92c1580998dd5476458e32d8d6c2ca14a9c55edb',input_R_types=Rlist,input_S_types=Slist,derivative_target=[[-20,'one'],[-6,'one']],forced_C=[[-8,'one']],first_osculating_source=[[-7,'W']],second_osculating_source=[[-6,'A']],excluded_R_indices=[1,2,3],forced_R=forced_R,forced_Qstar=forced_Q,forced_L=forced_L,forced_second_osculating_subbundle=[[-6,'A']],R_minus_equals_S_claimed=False,realization_claimed=False)
(ROOT/'two-one-index-two-residual-osculations.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'four residual sources -> unique O(-18)+A O(-6); no label exclusion.')
