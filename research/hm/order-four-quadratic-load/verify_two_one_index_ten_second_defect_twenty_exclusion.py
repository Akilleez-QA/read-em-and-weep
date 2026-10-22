#!/usr/bin/env python3
"""One second-defect exclusion from a complete seven-item rank-two overlist."""
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
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][10]
ID='G3.21.d41783aef00b';row=next(c for c in front['cases']if c['id']==ID)
assert row['profile']=='21' and row['source_index']==10
assert row['A']==p['A']==[[-8,'one'],[9,'Wp']]
assert row['B']==p['B']==[[-11,'Wp'],[6,'one']] and p['a']==10
assert [a['torsion']for a in p['alternatives']if a['s']==20]==[[[20,0]],[[20,2]]]
assert (-10)%6==2 and sorted([(7-1)%6,(7+1)%6])==[0,2]
# Degree -6 rank2, max<=7: five even line pairs, or W/Wp at odd degree -3.
linepairs=[[(e,'one'),(-6-e,'one')]for e in range(-12,-3,2)]
candidates=linepairs+[[(-3,'W')],[(-3,'Wp')]]
assert len(candidates)==7 and all(e<=f<=7 for [(e,_),(f,_) ]in linepairs)
def chi_line(e,n):
 return mul(chars[n],symchar(e))if e>=0 else [scale(-1,x)for x in mul(chars[n],symchar(-e-2))]if e<=-2 else [z(0)]*9
def chi_bundle(bundle):return [total(chi_line(e,n)[i]for e,n in bundle)for i in range(9)]
records=[]
for top in [0,2]:
 # chi(T_top)=Sym(top)+Sym(18-top), by its reduced divisor exact sequence.
 want=decompose(sub(sub(mul(chars['Wp'],symchar(7)),symchar(top)),symchar(18-top)))
 matched=[b for b in candidates if decompose(chi_bundle(b))==want]
 if top==0:
  assert matched==[[(-10,'one'),(4,'one')],[(-3,'Wp')]]
  # O4 cannot embed into WpO7, as its Hom invariants vanish.
  hom=inner(mul(chars['Wp'],symchar(3)),chars['one']);assert hom==z(0)
  forced=[(-3,'Wp')];bound=0
 else:
  assert matched==[[(-6,'one'),(0,'one')]]
  forced=matched[0];bound=3
 records.append(dict(top=top,chi_Jprime=want,Euler_matched=matched,forced_Jprime=forced,H0_J_two=bound))
minJ=-54-p['a']-13*(-3);assert minJ==-25 and -30<minJ
chiM4=11*5-48-2*p['a']+20;assert chiM4==7>max(r['H0_J_two']for r in records)
out=dict(scope='Whole index10 second-defect20 exclusion;143 quotient labels unchanged.',source_hashes=PINNED,id=ID,source_pair_index=10,excluded_second_defect=20,character_order=names,complete_rank_two_overlist=candidates,alternatives=records,min_J=minJ,H0_M_four_lower_bound=chiM4)
(ROOT/'two-one-index-ten-second-defect-twenty-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'both s20 alternatives excluded: at least7 M sections versus0 or3 J sections.')
