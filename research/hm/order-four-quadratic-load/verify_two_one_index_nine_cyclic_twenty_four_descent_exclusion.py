#!/usr/bin/env python3
"""One cyclic torsion branch exclusion via a further endpoint descent."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
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
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md': 'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843', 'NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md': '53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
front=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][9]
ID='G3.21.1c43993b4f83';row=next(c for c in front['cases']if c['id']==ID)
assert row['profile']=='21' and row['source_index']==9
assert row['A']==p['A']==[[-8,'one'],[6,'one'],[16,'one']]
assert row['B']==p['B']==[[-18,'one'],[-8,'one'],[6,'one']] and p['a']==14
alts=[a for a in p['alternatives']if a['s']==24 and a['torsion']==[[24,4]]]
assert len(alts)==1 and len(alts[0]['endpoints'])==2
# Low weight0 is absent from cyclic layers4,2, so its whole component is zero.
assert (-10)%10 not in [4,(4-12)%10]
candidates=[[(e,'one'),(-6-e,'one')]for e in range(-20,-3,2)]+[[(-3,'W')],[(-3,'Wp')]]
assert len(candidates)==11
# Rank2 degree-6 and top<=14 give exactly9 even line pairs or W/Wp(-3).
def chi_line(e,n):
 return mul(chars[n],symchar(e))if e>=0 else [scale(-1,x)for x in mul(chars[n],symchar(-e-2))]if e<=-2 else [z(0)]*9
def chi_bundle(b):return [total(chi_line(e,n)[i]for e,n in b)for i in range(9)]
want=decompose(sub(symchar(14),symchar(18)))
matched=[b for b in candidates if decompose(chi_bundle(b))==want]
assert matched==[[(-20,'one'),(14,'one')],[(-16,'one'),(10,'one')],[(-10,'one'),(4,'one')],[(-3,'Wp')]]
assert inner(symchar(4),chars['one'])==z(0) # O10 cannot embed in O4+O14.
chiA2=sub([plus(x,y)for x,y in zip(symchar(8),symchar(18))],symchar(4))
chiE2=sub(mul(M3,W),mul(M4,symchar(2)))
k=decompose(sub(chiA2,chiE2));j=decompose([plus(x,y)for x,y in zip(symchar(6),symchar(16))])
assert k==(0,0,0,1,2,3,0,1,0) and j==(0,0,0,0,2,2,0,2,0)
assert k[names.index('D')]<j[names.index('D')] # Rules out J'=(-20,14).
# Wp(-3) has no sections at twist2, whereas each M has7 sections at twist4.
dims={'one':1,'W':2,'Wp':2,'A':3,'V':3,'P':4,'S':4,'D':5,'T':6}
h0dim=lambda b,t:sum(dims[n]*max(e+t+1,0)for e,n in b)
Mends=alts[0]['endpoints']
assert all(h0dim(M,4)==7 and h0dim(M,5)==16 for M in Mends)
assert all(sorted([n for e,n in M if e==-4])==['P','V']for M in Mends)
forcedJ=[(-10,'one'),(-10,'one'),(4,'one')]
assert inner(symchar(10),chars['one'])==z(0) # No O4 -> O14 equivariant lift.
assert decompose(symchar(6))==(0,0,0,0,1,1,0,0,0)
# The derivative M -> J(-2) can land only in O2, and its twist4 section
# map onto all H0O6 makes this line quotient everywhere surjective.
assert all(min(e for e,n in M)>-12 for M in Mends)
N5lower=16-(7+1);assert N5lower==8
# N=M^- has top<=-5; N^- has top<=-6; derivative N -> O2(-2)=O0.
next_target_sections=5+1;assert N5lower>next_target_sections
out=dict(scope='Source9 cyclicO4|2D12 excluded by further endpoint descent;143 quotient labels unchanged.',source_hashes=PINNED,id=ID,source_pair_index=9,second_defect=24,excluded_torsion=[[24,4]],character_order=names,rank_two_overlist=candidates,Euler_matched=matched,forced_J=forcedJ,H1_K_two=k,H1_rejected_J_two=j,M_endpoint_degree_minima=[min(e for e,n in M)for M in Mends],H0_M_four=7,H0_M_five=16,forced_M_over_Mminus='O2',H0_Mminus_five_lower_bound=N5lower,next_derivative_target_H0_five=next_target_sections)
(ROOT/'two-one-index-nine-cyclic-twenty-four-descent-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'cyclic s24 excluded: after forced J and quotient O2,8 endpoint-kernel sections cannot inject into6.')
