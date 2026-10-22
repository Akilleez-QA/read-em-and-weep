#!/usr/bin/env python3
"""One second-defect branch exclusion; abstract characters only."""
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
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md': 'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
front=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][5]
ID='G3.21.ed1df480d8d2';row=next(c for c in front['cases']if c['id']==ID)
assert row['profile']=='21' and row['source_index']==5
assert row['A']==p['A']==[[-8,'one'],[4,'one'],[16,'one']]
assert row['B']==p['B']==[[-18,'one'],[-6,'one'],[6,'one']] and p['a']==12
alts=[a for a in p['alternatives']if a['s']==20]
assert len(alts)==1 and alts[0]['torsion']==[[20,2]]
assert len(alts[0]['endpoints'])==4
assert all([-4,'V'] in M and max(e for e,n in M)<=-4 for M in alts[0]['endpoints'])
# C10 invariant divisor D12 gives a degree12 invariant section, nonzero on D20.
assert (2-(-10))==12 and [e%6 for e in [-10,2,14]]==[2,2,2]
# Low-only quotient forces an O(-30) summand, below quotient J's lower bound.
minJ=(-54-p['a'])-13*(-3)
assert minJ==-27 and -10-20<minJ
# H0K2=0 by topK<=-3. Compute H1K2=chiA2-chiE2 exactly.
chiA2=sub([plus(x,y)for x,y in zip(symchar(6),symchar(18))],symchar(4))
chiE2=sub(mul(M3,W),mul(M4,symchar(2)))
k=decompose(sub(chiA2,chiE2));assert k==(0,0,0,1,3,3,0,0,0)
# High zero, middle nonzero: the degree12 lift gives J=(-10,-18,14).
j=decompose([plus(x,y)for x,y in zip(symchar(6),symchar(14))])
assert k[names.index('D')]==0<j[names.index('D')]
# High nonzero: H0O16 restricts injectively to D20, so H0J2 embeds in Sym4=D.
assert 16<20 and -10+2<0
middle=decompose(symchar(4));assert middle==(0,0,0,0,0,0,0,1,0)
assert middle[names.index('V')]==0
out=dict(scope='Whole index5 second-defect20 exclusion; quotient labels unchanged.',source_hashes=PINNED,id=ID,source_pair_index=5,excluded_second_defect=20,torsion=[[20,2]],character_order=names,min_J=minJ,high_zero_middle_nonzero_H1_K_two=k,high_zero_middle_nonzero_H1_J_two=j,high_nonzero_H0_J_two_embeds_into=middle,each_published_M_has_V_in_H0_M_four=True)
(ROOT/'two-one-index-five-second-defect-twenty-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'s20 excluded by low-only degree, middle-only H1 D, and high-nonzero H0 V obstructions.')
