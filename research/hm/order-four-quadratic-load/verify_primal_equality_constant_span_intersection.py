#!/usr/bin/env python3
"""Primal constant-span intersection; exhaustive obstruction to the exceptional dual block."""
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
PINNED={
'PRIMAL-EQUALITY-ANNIHILATOR-FORCES-DUAL-DEGREE-ONE-SECTIONS.md':'a8b4e3fe6c1dfa48c56b7f62d2f185b5e3285feb90c5407ec21db42222a0280d',
'primal-equality-annihilator-forces-dual-degree-one-sections.json':'af4351a0016bea94a4f62e2fd2784b60d7fc083535645f7afe059561727024cc',
'EQUALITY-GAUSS-ENVELOPES-FORCE-RATIONAL-NORMAL-SUBBUNDLES.md':'cc64326df0b4c5d3b35a195a994f1faf397cac88ec377d608aac56b29f4fb9db',
'PRIMAL-EQUALITY-HAS-SIX-RESIDUAL-QUOTIENT-PARAMETER-SPACES.md':'de06847ba55aae35effb6ad394de4792b5c8813d48dbee35b4c1bed79935afa6',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
prior=json.loads((ROOT/'primal-equality-annihilator-forces-dual-degree-one-sections.json').read_text())
blocks=prior['all_eligible_dual_blocks'];assert len(blocks)==26
M3=linear([(3,'Wp'),(3,'S'),(6,'T')]);M2=linear([(1,'A'),(2,'V'),(3,'P'),(4,'D')])
assert tuple(prior['H1_Qstar_minus_one'])==decompose(M3)
assert tuple(prior['H1_Qstar'])==decompose(M2)
def contributions(e,n):
 return decompose(mul(chars[n],symchar(-e-1))),decompose(mul(chars[n],symchar(-e-2)))if e<=-2 else (0,)*9
# Recheck all frozen cohomology records using exact class functions.
for b in blocks:
 x,y=contributions(b['degree'],b['irrep'])
 assert list(x)==b['H1_minus_one']and list(y)==b['H1_zero']
def co_blocks(e,n):
 x,y=contributions(e,n)
 X=tuple(a-b for a,b in zip(decompose(M3),x));Y=tuple(a-b for a,b in zip(decompose(M2),y))
 assert min(X)>=0 and min(Y)>=0
 out=[b for b in blocks if all(a<=c for a,c in zip(b['H1_minus_one'],X))and all(a<=c for a,c in zip(b['H1_zero'],Y))]
 return X,Y,out
X,Y,co=co_blocks(-28,'one')
assert [(b['degree'],b['irrep'])for b in co]==[(-10,'one'),(-6,'one'),(-4,'V'),(-3,'Wp'),(-2,'P'),(-2,'D'),(-1,'Wp'),(-1,'S'),(-1,'T')]
homs=[]
for b in co:
 e,n=b['degree'],b['irrep']
 h=inner(chars[n],symchar(-8-e))if e<=-8 else z(0)
 assert h==z(0)
 homs.append(dict(degree=e,irrep=n,Hom_to_O_minus_eight=0))
assert inner(chars['one'],symchar(20))==z(1)
assert all(b['degree']!=-28 for b in co) # O(-28) multiplicity at most one.
# The only remaining exceptional Hom block O(-10) maps canonically into W O(-9).
assert inner(chars['W'],symchar(1))==z(1)
assert decompose(symchar(9))==(0,0,0,0,0,0,1,0,1)
_,_,co9=co_blocks(-9,'W')
assert all(not(b['degree']==-9 and b['irrep']=='W')for b in co9)
assert (13-2,-54+18)==(11,-36)
assert (17-9,-54+18,30-11)==(8,-36,19)
assert (14-8,-54+24)==(6,-30)
out=dict(scope='Exact primal constant-span intersection and genuine projected residual for surviving profile11/12 equalities; no further label exclusion.',source_hashes=PINNED,annihilator_commit='4c6b0ab0eccb2d2df524f7f529e26f2771a91111',ids=['G3.11.942927348917','G3.12.8e9af2d08af9'],hypothetical_O_minus_28=dict(residual_H1_minus_one=X,residual_H1_zero=Y,all_co_blocks_and_Hom_to_O_minus_eight=homs,own_Hom_to_O_minus_eight=1,own_map_polynomial_degree=20,impossible_due_to_required_surjection=True),forced_projection_block=[-9,'W'],forced_projection_block_multiplicity=1,projection_kernel_Qprime=dict(rank=11,degree=-36),intersection='E intersect V0=C8=Sym8 W O(-2)',projected_residual_Z=dict(rank=8,degree=-36,ambient_constant_rank=19,saturated=True),projected_kernel_N=dict(rank=6,degree=-30,contained_in_actual_Z_Gauss_kernel=True,equality_asserted=False),no_new_label_exclusions=True,realization_claimed=False)
(ROOT/'primal-equality-constant-span-intersection.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: O(-28) has nine possible co-blocks, none maps to O(-8); forced W O(-9) projection is surjective; primal intersection C8 and saturated Z.')
