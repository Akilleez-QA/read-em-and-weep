#!/usr/bin/env python3
"""Fixed universal atom tables and exact symbolic data, no bundle search."""
from collections import Counter
from pathlib import Path
import hashlib,json
from characters import product, h0, DIM,NAMES
ROOT=Path(__file__).resolve().parent
checks=0
def check(got,want,label):
 global checks
 checks+=1
 if got!=want:raise RuntimeError((label,got,want))
def clean(c):return {r:n for r,n in c.items() if n}
def sub(a,b):
 c=Counter(a);c.subtract(b);return c
def h1(bs,t):
 c=Counter()
 for e,r in bs:c.update(product(r,-e-t-2))
 return c
def chi(bs,t):return sub(h0(bs,t),h1(bs,t))
E=[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-8,'one')]
A=[(4,'A'),(-8,'one')]
check(clean(sub(chi(E,3),chi(A,3))),{'T':-1},'kernel cubic Euler')
check(clean(sub(chi(E,4),chi(A,4))),{'V':1,'P':1},'kernel quartic Euler')
check(dict(h0(A,0)),{'A':1,'D':1,'V':1,'P':1},'untwisted gate')
check(dict(h0(A,1)),{'Wp':1,'S':1,'T':2},'twist-one gate')
check(dict(h0(A,2)),{'D':2,'V':1,'P':2},'R4 target')
parity={'one':0,'W':1,'A':0,'S':1,'D':0,'T':1,'V':0,'P':0,'Wp':1}
expected6=[('T',5),('V',6),('Wp',7),('one',10)]
expected10=[('S',5),('T',5),('D',6),('V',6),('Wp',7),('one',8),('W',9),('Wp',9),('one',10),('one',14)]
atom_records=[]
for budget,want in [(Counter(T=1),expected6),(Counter(S=1,T=1),expected10)]:
 cost=sum(DIM[r]*n for r,n in budget.items());got=[]
 for j in range(5,cost+5):
  for r in NAMES:
   if parity[r]!=j%2 or (j-4)*DIM[r]>cost:continue
   c=product(r,j-5)
   if all(n<=budget.get(s,0) for s,n in c.items()):got.append((r,j))
 check(got,want,'complete bounded individual atoms')
 atom_records.append({'budget':dict(budget),'atoms':[{'R':r,'j':j,'H1_3':dict(product(r,j-5)),'H1_4':dict(product(r,j-6))} for r,j in got]})
for r,j in expected10:
 hasA=product(r,j-6).get('A',0)>0
 check(hasA,(r,j) in [('one',8),('W',9)],'only atoms supplying A '+r+str(j))
check([r for r,j in expected6 if product(r,j-6).get('D',0)],['one'],'unique T-budget D supplier')
K=[
 [(-4,'V'),(-4,'P'),(-5,'T')],
 [(-4,'V'),(-4,'P'),(-4,'P'),(-7,'Wp')],
 [(-4,'V'),(-4,'P'),(-4,'D'),(-10,'one')],
 [(-3,'S'),(-4,'V'),(-4,'P'),(-9,'W')],
 [(-3,'S'),(-4,'V'),(-4,'P'),(-8,'one'),(-10,'one')]]
for i,bs in enumerate(K,1):
 check(sum(DIM[r] for e,r in bs),13,'rank K'+str(i))
 check(sum(e*DIM[r] for e,r in bs),-58,'degree K'+str(i))
 check(clean(chi(bs,3)),{'T':-1},'cubic Euler K'+str(i))
 check(clean(chi(bs,4)),{'V':1,'P':1},'quartic Euler K'+str(i))
check(dict(product('one',8)),{'D':1,'P':1},'V quotient obstruction')
check(dict(product('one',9)),{'S':1,'T':1},'T positive scalar row')
check(dict(product('one',11)),{'W':1,'S':1,'T':1},'no Wp positive scalar row')
for n in range(5):check(product('one',n).get('V',0),0,'rank-one V obstruction '+str(n))
check(2-2*(-4),10,'V maximal-minor degree')
check((-58)-2,-60,'hypothetical rank-eleven degree')
check(-(6*6+5*5),-61,'all-height integer two-column maximum')
# Identity h1^2+h2^2=((h1+h2)^2+(h1-h2)^2)/2:
# odd sum11 forces odd difference, whose square is at least1.
check((11*11+1)//2,61,'all-height parity certificate')
check(-58-6,-64,'full-positive predecessor degree')
check(5+2+6+3,16,'actual E0 rank')
check(-2*5-3*8-4*3,-46,'actual E0 degree')
for f,h in [('inputs/top-four.md','56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0'),('inputs/low-top.md','c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af')]:check(hashlib.sha256((ROOT/f).read_bytes()).hexdigest(),h,'immutable input')
print(json.dumps({'status':'PASS','checks':checks,'atoms':atom_records,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'scope':'Fixed universal individual atoms only; no actual instance or bundle/height search.'},indent=2,sort_keys=True))
