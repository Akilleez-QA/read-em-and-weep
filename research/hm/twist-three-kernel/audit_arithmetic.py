"""Independent finite HN audit: unordered combinations, then strict slope order."""
from fractions import Fraction as F
from itertools import combinations
P=[(r,b) for r in range(1,13) for b in range(1,10) if (b-2*r)%5==0]
profiles=[]
for n in range(2,10):
 for p in combinations(P,n):
  if sum(r for r,b in p)!=12 or sum(b for r,b in p)!=9: continue
  s=sorted(p,key=lambda x:F(x[1],x[0]))
  if len({F(b,r) for r,b in s})<n: continue
  c=[]
  for r,b in s:
   k=2*r*(r-1)%5
   while 2*r*k<(r-1)*b*b:k+=5
   c.append(k)
  u=sum(F(b*b,2)-k for (r,b),k in zip(s,c))
  profiles.append((s,c,u))
assert len(profiles)==15
positive=[(s,c,u) for s,c,u in profiles if s[0][1]>1 and u>F(3,2)]
assert len(positive)==2
for s,c,u in positive:print(s,c,'ch2 max',u,'t max',u-F(3,2))
assert 9**4-3*9**2*42+42**2+2*9*72==-585
print('Independent checks passed; 15 profiles, two positive-defect candidates, h4=-585.')
