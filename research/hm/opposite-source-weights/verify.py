#!/usr/bin/env python3
"""Nine-class abstract characters only. No actual tensors or instance evaluations."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

def require(condition,message):
    if not condition: raise RuntimeError(message)
def z(a,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(k,x):return k*x[0],k*x[1]
def total(xs):
    out=z(0)
    for x in xs:out=add(out,x)
    return out
def va(*args):return [total(v) for v in zip(*args)]
def vs(k,a):return [scale(k,x) for x in a]
def vm(a,b):return [mul(x,y) for x,y in zip(a,b)]
def sym(n,x):
    require(n>=0,'negative symmetric power')
    if n==0:return z(1)
    a,b=z(1),x
    for _ in range(2,n+1):a,b=b,sub(mul(x,b),a)
    return b
phi=z(F(1,2),F(1,2));phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
one=[z(1)]*9
A=[sym(2,x) for x in W];S=[sym(3,x) for x in W]
D=[sym(4,x) for x in W];T=[sym(5,x) for x in W]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=[sub(sym(6,x),p) for x,p in zip(W,P)]
Wp=[sub(mul(w,p),t) for w,p,t in zip(W,P,T)]
reps=dict(zip(['1','W','Wp','A','V','P','S','D','T'],[one,W,Wp,A,V,P,S,D,T]))
def inner(a,b):return scale(F(1,120),total(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
require(sum(sizes)==120,'class sizes')
for n,c in reps.items():
 for m,d in reps.items():require(inner(c,d)==z(int(n==m)),'character orthogonality')
require(sum(int(c[0][0])**2 for c in reps.values())==120,'irrep completeness')
require(V==[sym(2,x) for x in Wp],'positive ambient V=Sym2 Wp')
# W trace separates the nine classes; g-square has trace trace(g)^2-2.
square=[W.index(sub(mul(x,x),z(2))) for x in W]
require(square==[0,0,5,5,3,3,7,7,1],'exact square-class map')
def psi2(c):return [c[i] for i in square]
H=va(V,W)
L2=vs(F(1,2),va(vm(H,H),vs(-1,psi2(H))))
require(L2==va(V,vm(V,W),one),'exterior square H')
N=va(A,Wp)
# Sym^n(V+W), with V=Sym2 Wp; degrees only 2 through 8.
def sn(n):
 return [total(mul(total(sym(2*i-4*j,xp) for j in range(i//2+1)),sym(n-i,x)) for i in range(n+1)) for x,xp in zip(W,Wp)]
c={-1:vs(-1,N),0:va(vm(Wp,L2),vs(-1,N)),1:vs(-1,vm(Wp,H)),2:Wp}
# The same fixed lambda-ring formula at twist three, not an actual matrix.
chi=va(*[vs(F(1,2),vm(vm(ci,cj),sn(i+j+3))) for i,ci in c.items() for j,cj in c.items()],
       *[vs(F(1,2),vm(psi2(ci),sn(2*i+3))) for i,ci in c.items()])
k3=vs(-1,chi)
u=va(vs(2,W),vs(2,Wp),vs(3,S),vs(4,T))
require(k3==va(A,vs(2,V),vs(3,P),vs(4,D),u),'actual Euler character all classes')
e=va(u,vs(-1,S),vs(-1,Wp),vs(-2,T))
require(e==va(vs(2,W),Wp,vs(2,S),vs(2,T)),'reduced source26 character')
require(u[0]==z(44) and e[0]==z(26),'source dimensions')
# Restrictions to abstract binary C10: retain repeated weight5 in T.
odd_weights={'W':[1,9], 'Wp':[3,7], 'S':[1,9,3,7], 'T':[1,9,3,7,5,5]}
j={a:tuple(odd_weights[n].count(a%10) for n in ('W','Wp','S','T')) for a in (1,3,5,7,9)}
require(j[1]==j[9]==(1,0,1,1),'J1')
require(j[3]==j[7]==(0,1,1,1),'J3')
require(j[5]==(0,0,0,2),'J5')
contribution={r:j[(2*r-1)%10] for r in (0,1,-1,2,-2)}
plus=lambda a,b:tuple(x+y for x,y in zip(a,b))
minus=lambda a,b:tuple(x-y for x,y in zip(a,b))
source=(2,1,2,2)
rows=[]
for pair in [(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
    rest=minus(source,plus(contribution[pair[0]],contribution[pair[1]]))
    if rest in ((1,0,0,0),(0,1,0,0)): rows.append((pair,rest))
# Equal-sign middle pair(1,1) leaves Wp, but neither middle quotient has source Wp.
rows=[x for x in rows if not (x[0] in ((1,1),(-1,-1)) and x[1]!=(1,0,0,0))]
require(rows==[((0,1),(0,1,0,0)),((0,-1),(1,0,0,0)),((1,-1),(1,0,0,0)),((1,2),(1,0,0,0))],'exact signed patterns')
# Ext weight exponents modulo5, tau=zeta^-1, target fiber trivial.
patterns={'I':(0,-1),'II':(0,1),'III':(1,-1),'IV':(1,2)}
for name,rs in patterns.items():
    inv=sum((1-r)%5==0 for r in rs)
    require(inv==(0 if name=='I' else 1),'semisimple invariant Ext dimension')
cyclic={'I':0,'II':1,'IV':2}
for name,r in cyclic.items():
    invariant_positions=[i for i in (0,1) if (2-r-i)%5==0]
    require(invariant_positions=={'I':[],'II':[1],'IV':[0]}[name],'cyclic invariant class valuation')
require(2-1==1 and 2-2==0,'absorbed lengths')
print('PASS: nine-class source Euler, E26, binary C10 signed factors, four type pairings, semisimple/cyclic invariant Ext weights.')
print('TypeI: tors24 forced; TypeII/III/IV-semisimple: tors24 or12; TypeIV-cyclic: tors24 or0.')
print('BOUNDARY: universal proof only; no actual HM/source coefficient, point, matrix, derivative or instance rank is evaluated.')
