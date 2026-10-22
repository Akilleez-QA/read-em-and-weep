#!/usr/bin/env python3
"""Universal character and dimension checks, with no HM coefficient evaluation."""
from fractions import Fraction as F

def z(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def seq_sum(xs):
    out=z(0)
    for x in xs: out=add(out,x)
    return out
# SU2 traces on the nine conjugacy classes of the abstract binary A5.
phi=z(F(1,2),F(1,2)); phip=z(F(1,2),F(-1,2))
tr=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
assert sum(sizes)==120

def sym(n,x):
    if n==0:return z(1)
    a,b=z(1),x
    for _ in range(2,n+1): a,b=b,sub(mul(x,b),a)
    return b

def inner(a,b):return scale(F(1,120),seq_sum(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
def vadd(*args):return [seq_sum(v) for v in zip(*args)]
def vmul(a,b):return [mul(x,y) for x,y in zip(a,b)]
def vscale(k,a):return [scale(k,x) for x in a]

one=[z(1)]*9; W=tr; A=[sym(2,x) for x in tr]
S=[sym(3,x) for x in tr]; D=[sym(4,x) for x in tr]; T=[sym(5,x) for x in tr]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=[sub(sym(6,x),p) for x,p in zip(tr,P)]
Wp=[sub(mul(w,p),t) for w,p,t in zip(W,P,T)]

from itertools import combinations_with_replacement
names=('one','W','Wp','A','V','P','S','D','T')
reps={n:globals()[n] for n in names}
assert sum(int(R[0][0])**2 for R in reps.values())==120
for n,R in reps.items():
 for m,U in reps.items(): assert inner(R,U)==z(int(n==m))
def dec(x):
 values={n:inner(R,x) for n,R in reps.items()}
 assert all(v[1]==0 and v[0].denominator==1 for v in values.values())
 return {n:int(v[0]) for n,v in values.items() if v[0]}
def genuine(x):return all(v>=0 for v in dec(x).values())
def chi(X,t):
 out=vscale(0,one)
 for e,n in X:
  d=e+t
  if d==-1:continue
  out=vadd(out,vscale(1 if d>=0 else -1,vmul(reps[n],[sym(d if d>=0 else -d-2,w)for w in W])))
 return out
def h0(X,t):return chi([(e,n)for e,n in X if e+t>=0],t)
M2=vadd(A,vscale(2,V),vscale(3,P),vscale(4,D))
M3=vadd(vscale(3,Wp),vscale(3,S),vscale(6,T))
M4=vadd(vscale(2,V),vscale(4,P),vscale(3,D))
def chiE(t):return vadd(vmul(M3,[sym(t-1,w)for w in W]),vscale(-1,vmul(M4,[sym(t,w)for w in W])))
assert chiE(2)==vscale(-1,V)
assert chiE(3)==vadd(Wp,vscale(2,T))
def c2(X):return vadd(chi(X,2),V)
def c3(X):return vadd(h0(X,1),chi(X,3),vscale(-1,chiE(3)))
def candidates(a):
 # Every ordinary summand is >=-10; rank three gives maximum a+20.
 upper=a+20
 out=[]
 for es in combinations_with_replacement(range(-10,upper+1,2),3):
  if sum(es)==a:out.append([(e,'one')for e in es])
 for n in ('W','Wp'):
  for e in range(-9,upper+1,2):
   f=a-2*e
   if -10<=f<=upper and f%2==0:out.append([(e,n),(f,'one')])
 if a%6==0:
  out += [[(a//3,n)]for n in ('A','V')]
 return [X for X in out if h0(X,1)[0][0]>=2-a]
expected8=[
 [(-10,'one'),(-6,'one'),(8,'one')],
 [(-8,'one'),(-8,'one'),(8,'one')],
 [(-10,'one'),(-8,'one'),(10,'one')],
 [(-10,'one'),(-10,'one'),(12,'one')],
 [(-9,'W'),(10,'one')],[(-9,'Wp'),(10,'one')]]
key=lambda X:tuple(X)
assert set(map(key,candidates(-8)))==set(map(key,expected8))
expected_char8=[{'Wp':-1,'S':2,'T':-1},{'W':1,'Wp':-1},{'W':2,'S':1,'T':-1},{'W':1,'S':2,'T':-1},{'W':2,'S':1,'T':-1},{'W':2,'S':1,'T':-1}]
assert [dec(c3(X))for X in expected8]==expected_char8
assert all(not genuine(c3(X))for X in candidates(-8))
expected6=[
 [(-10,'one'),(-8,'one'),(12,'one')],
 [(-9,'W'),(12,'one')],[(-9,'Wp'),(12,'one')]]
all6=candidates(-6)
assert len(all6)==15
survivors=[X for X in all6 if genuine(c2(X)) and genuine(c3(X))]
assert survivors==expected6
certs={(-10,-10,14):(2,'P'),(-10,-6,10):(3,'T'),(-10,-4,8):(2,'one'),(-10,-2,6):(3,'T'),(-10,0,4):(3,'T'),(-10,2,2):(2,'P'),(-8,-8,10):(2,'D'),(-8,-6,8):(3,'Wp'),(-8,-4,6):(2,'one'),(-6,-6,6):(2,'A')}
for es,(which,n)in certs.items():assert dec((c2 if which==2 else c3)([(e,'one')for e in es])).get(n,0)<0
for n in ('W','Wp'):assert dec(c3([(-7,n),(8,'one')])).get('Wp',0)<0
assert inner(one,M2)==z(0)
assert [sym(12,w)for w in W]==vadd(one,A,P,D)
print('PASS: invariant degree-twelve multiplier and absence of trivial H1(Q*).')
eligible=[]
for j in range(14,43):
 for n,R in reps.items():
  dim=R[0][0]
  if R[1]!=z((-1)**j*dim) or (j-1)*dim>41:continue
  contribution=vmul(R,[sym(j-2,w)for w in W])
  if genuine(vadd(M2,vscale(-1,contribution))):
   eligible.append((j,n))
   assert inner(one,vmul(R,[sym(j-14,w)for w in W]))==z(0)
assert eligible==[(16,'one'),(17,'W'),(18,'one'),(19,'W'),(20,'one'),(28,'one'),(30,'one')]
print('PASS: six degree-minus-eight candidates excluded by C3.')
print('PASS: fifteen degree-minus-six candidates reduce to three, each containing O(12).')
print('PASS: seven conservative eligible Q* blocks, all with zero G-Hom to O(-14).')
print('Only exact universal character arithmetic; no selected actual-instance evaluation.')

# All invariant effective divisor degrees <=22; orbit multiplicities retained.
invariant={12*i+20*j for i in range(2)for j in range(2)if 12*i+20*j<=22}
assert invariant=={0,12,20}
second=[]
for a in range(-4,7,2):
 b=-6-a
 for defect in sorted(invariant):
  if defect<=14-2*a:second.append((a,b,defect,-36+2*a+defect))
assert second==[(-4,-2,0,-44),(-4,-2,12,-32),(-4,-2,20,-24),(-2,-4,0,-40),(-2,-4,12,-28),(0,-6,0,-36),(0,-6,12,-24),(2,-8,0,-32),(4,-10,0,-28),(6,-12,0,-24)]
print('PASS: exact remaining second-dual defect table, including the twenty-point branch.')
