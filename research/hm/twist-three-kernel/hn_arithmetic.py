from fractions import Fraction as F
from itertools import product
P=[]
for r in range(1,13):
 for a in range(1,10):
  if (a-2*r)%5:continue
  low=F((r-1)*a*a,2*r)
  c=2*r*(r-1)%5
  while c<low:c+=5
  P.append((r,a,F(a,r),F(a*a,2)-c,c))
def walk(R,A,prev,seq):
 if R==A==0:
  if len(seq)>1:
   yield seq
  return
 for p in P:
  r,a,s,*_=p
  if r<=R and a<=A and s>prev:
   yield from walk(R-r,A-a,s,seq+[p])
rows=list(walk(12,9,F(0),[]))
print('HN numeric profiles',len(rows))
for seq in sorted(rows,key=lambda s:sum(p[3] for p in s),reverse=True):
 print([(p[0],p[1],p[4]) for p in seq], 'ch2 upper',sum(p[3] for p in seq),'t upper',sum(p[3] for p in seq)-F(3,2))
