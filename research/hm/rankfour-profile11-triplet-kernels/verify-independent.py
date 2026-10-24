#!/usr/bin/env python3
"""Independent exact universal-character checks; no actual-instance data/search.

Uses the full real character table and class inner products, NOT characters.py
or its McKay adjacency recurrence. All symmetric powers use the determinant-one
trace recurrence. Atom inspection is individual only (9 irreps, 5 <= j <= 14).
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
PIN = {
 'PROOF.md': '4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a',
 'inputs/low-top.md': 'c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af',
 'inputs/top-four.md': '56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0',
}
checks = 0

def require(ok, label):
 global checks
 checks += 1
 if not ok:
  raise AssertionError(label)

# Exact a+b sqrt(5).
def q(a, b=0): return (F(a), F(b))
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0], -x[1])
def sub(x, y): return add(x, neg(y))
def mul(x, y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(n, x): return (n*x[0], n*x[1])

a, b = q(F(1,2), F(1,2)), q(F(1,2), F(-1,2))
# Classes: 1, -1, trace a, -a, b, -b, 1, -1, 0.
sizes = (1, 1, 12, 12, 12, 12, 20, 20, 30)
names = ('one', 'W', 'A', 'S', 'D', 'T', 'V', 'P', 'Wp')
raw = (
 (1,1,1,1,1,1,1,1,1),
 (2,-2,a,neg(a),b,neg(b),1,-1,0),
 (3,3,a,a,b,b,0,0,-1),
 (4,-4,1,-1,1,-1,-1,1,0),
 (5,5,0,0,0,0,-1,-1,1),
 (6,-6,-1,1,-1,1,0,0,0),
 (3,3,b,b,a,a,0,0,-1),
 (4,4,-1,-1,-1,-1,1,1,0),
 (2,-2,b,neg(b),a,neg(a),1,-1,0),
)
char = {r: tuple(v if isinstance(v, tuple) else q(v) for v in row)
        for r,row in zip(names,raw)}
dim = {r: int(char[r][0][0]) for r in names}
parity = {r: 0 if char[r][1] == q(dim[r]) else 1 for r in names}

def inner(x, y):
 z = q(0)
 for size, xi, yi in zip(sizes, x, y): z = add(z, scale(F(size,120), mul(xi, yi)))
 return z

require(sum(sizes)==120, 'class sizes')
require(sum(d*d for d in dim.values())==120, 'complete dimensions')
for r in names:
 for s in names:
  require(inner(char[r],char[s])==q(int(r==s)), 'character orthogonality '+r+','+s)
for r,n in [('one',0),('W',1),('A',2),('S',3),('D',4),('T',5)]:
 require(parity[r]==n%2, 'physical parity '+r)

sym = [char['one'],char['W']]
for n in range(2,12):
 sym.append(tuple(sub(mul(t,x),y) for t,x,y in zip(char['W'],sym[-1],sym[-2])))

def decompose(row):
 out = {}
 for r in names:
  v=inner(row,char[r])
  require(v[1]==0 and v[0].denominator==1, 'integral exact character inner product')
  if v[0]: out[r]=int(v[0])
 return out

def product(r,n):
 if n<0: return {}
 out=decompose(tuple(mul(x,y) for x,y in zip(char[r],sym[n])))
 require(all(v>=0 for v in out.values()), 'genuine product')
 require(sum(dim[s]*v for s,v in out.items())==dim[r]*(n+1), 'product dimension')
 return out

def plus(*reps):
 out={}
 for rep in reps:
  for r,n in rep.items(): out[r]=out.get(r,0)+n
 return {r:n for r,n in out.items() if n}
def minus(rep): return {r:-n for r,n in rep.items()}
def contains(rep,budget): return all(n<=budget.get(r,0) for r,n in rep.items())
def h0(blocks,t): return plus(*(product(r,e+t) for r,e in blocks))
def euler(blocks,t):
 out={}
 for r,e in blocks:
  d=e+t
  term=product(r,d) if d>=0 else minus(product(r,-d-2)) if d<=-2 else {}
  out=plus(out,term)
 return out

def rank_degree(blocks):
 return (sum(dim[r] for r,e in blocks),sum(dim[r]*e for r,e in blocks))

E=[('D',-2),('Wp',-3),('T',-3),('V',-4),('one',-8)]
Aq=[('A',4),('one',-8)]
E0=E[:-1]
M2={'A':1,'V':2,'P':3,'D':4}; M3={'Wp':3,'S':3,'T':6}
require(h0(Aq,0)=={'A':1,'V':1,'P':1,'D':1}, 'quotient H0')
require(h0(Aq,1)=={'Wp':1,'S':1,'T':2}, 'quotient twist-one H0')
require(contains(h0(Aq,0),M2) and contains(h0(Aq,1),M3), 'actual section gates')
require(h0(Aq,2)=={'V':1,'P':2,'D':2}, 'quartic derivative target')
require(euler(E,3)=={'Wp':1,'T':2}, 'source cubic Euler')
require(euler(E,4)=={'V':3,'P':3,'D':2}, 'source quartic Euler')
require(plus(euler(E,3),minus(euler(Aq,3)))=={'T':-1}, 'kernel cubic Euler')
require(plus(euler(E,4),minus(euler(Aq,4)))=={'V':1,'P':1}, 'kernel quartic Euler')
require(product('S',1)=={'A':1,'D':1}, 'cubic coefficient W product')

expected6={('T',5):({'T':1},{}), ('V',6):({'T':1},{'V':1}),
           ('Wp',7):({'T':1},{'P':1}), ('one',10):({'T':1},{'D':1})}
expected10={
 ('S',5):({'S':1},{}), ('T',5):({'T':1},{}),
 ('D',6):({'S':1,'T':1},{'D':1}), ('V',6):({'T':1},{'V':1}),
 ('Wp',7):({'T':1},{'P':1}), ('one',8):({'S':1},{'A':1}),
 ('W',9):({'S':1,'T':1},{'A':1,'D':1}),
 ('Wp',9):({'S':1,'T':1},{'D':1,'V':1}),
 ('one',10):({'T':1},{'D':1}),
 ('one',14):({'S':1,'T':1},{'D':1,'P':1}),
}
atom_reports={}
for title,budget,cost,expected in [('six',{'T':1},6,expected6),('ten',{'S':1,'T':1},10,expected10)]:
 atoms={}
 for j in range(5,15):
  for r in names:
   if parity[r]!=j%2 or (j-4)*dim[r]>cost: continue
   first=product(r,j-5)
   if contains(first,budget): atoms[(r,j)]=(first,product(r,j-6))
 require(atoms==expected, title+' complete individual atom table')
 atom_reports[title]=[{ 'irrep':r,'j':j,'H1_twist3':x,'H1_twist4':y}
                      for (r,j),(x,y) in atoms.items()]
# These are set filters on individual universal atoms, NOT tuple construction.
require([key for key,(x,y) in expected10.items() if y.get('A',0)]==[('one',8),('W',9)], 'only A-supplying atoms')
require([key for key,(x,y) in expected6.items() if y.get('D',0)]==[('one',10)], 'only residual T atom supplying D')
require(plus({'V':1,'P':1},expected6[('V',6)][1])=={'V':2,'P':1}, 'excluded R4 V multiplicity')
require(not contains({'V':2,'P':1},h0(Aq,2)), 'near-top injection excludes V(-6) atom')

K=[
 [('V',-4),('P',-4),('T',-5)],
 [('V',-4),('P',-4),('P',-4),('Wp',-7)],
 [('V',-4),('P',-4),('D',-4),('one',-10)],
 [('S',-3),('V',-4),('P',-4),('W',-9)],
 [('S',-3),('V',-4),('P',-4),('one',-8),('one',-10)],
]
require(rank_degree(E)==(17,-54) and rank_degree(Aq)==(4,4), 'source and quotient ranks/degrees')
for i,k in enumerate(K,1):
 require(rank_degree(k)==(13,-58), 'K'+str(i)+' rank/degree')
 require(euler(k,3)=={'T':-1} and euler(k,4)=={'V':1,'P':1}, 'K'+str(i)+' Euler check')
require(product('one',8)=={'P':1,'D':1}, 'Sym8 and V-row quotient Hom')
for n in range(5): require(product('one',n).get('V',0)==0, 'V rank-one Hom vanishing degree '+str(n))
require(product('one',11)=={'W':1,'S':1,'T':1}, 'Sym11 and Wp-row quotient Hom')
require(product('one',8).get('P',0)==1, 'possible P row')
require(product('one',9).get('T',0)==1, 'possible T row')
require(2-(-4)-(-4)==10<12, 'V maximal-minor degree')
require(4-(-4)==8<12 and 4-(-5)==9<12, 'nonzero scalar row divisor bounds')
require(all(e>-10 for k in K[:2] for r,e in k), 'K1/K2 negative projection vanishes')
# Fixed source Hom into O(-8), scalar contraction multiplicity.
require([product(r,-8-e).get('one',0) for r,e in E]==[0,0,0,0,1], 'unique negative quotient row')
# Capacity is symbolic: odd h1+h2=11 forces (h1-h2)^2 >= 1.
require((11**2+1)//2==61, 'two-column minimum squares')
require(-58-2==-60 and -60>-61, 'rank-eleven endpoint contradiction')
require(13-3==10 and -58-3*2==-64, 'full-image kernel rank/degree')
require(rank_degree(E0)==(16,-46), 'E0 rank/degree')
require((-46)-(-58)==3*4, 'E0/K positive quotient degree')

for filename,wanted in PIN.items():
 require(hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==wanted, 'immutable input '+filename)
print(json.dumps({'status':'PASS','assertions':checks,'method':'Full exact character table; individual atoms only; symbolic two-column capacity',
                  'pinned_sha256':PIN,'individual_atom_tables':atom_reports},indent=2))
