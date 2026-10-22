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
for chi in (W,Wp,A,V,P,S,D,T): assert inner(chi,chi)==z(1)
assert inner(A,V)==z(0)
# Characters of Gamma x physical C2, stored by evaluation at epsilon=+1,-1.
irreps=[one,W,Wp,A,V,P,S,D,T]
names=['1','W','U','A','V','P','S','D','T']
def ca(*cs):return vadd(*cs)
def cm(*cs):
 r=one+one
 for c in cs:r=vmul(r,c)
 return r
def cs(k,c):return vscale(k,c)
def lift(c,parity=1):return c+vscale(parity,c)
unit=lift(one)
def adams(c,k):
 out=[]
 for eps in [1,-1]:
  for t in tr:
   # trace(g^k) = Sym^k(trace g)-Sym^(k-2)(trace g)
   tk=sub(sym(k,t),sym(k-2,t)) if k>=2 else t
   j=tr.index(tk)
   out.append(c[j+(0 if eps**k==1 else 9)])
 return out
def power(c,n,exterior=False):
 vals=[unit]
 for j in range(1,n+1):
  vals.append(cs(F(1,j),ca(*[cs((-1)**(k-1) if exterior else 1,cm(vals[j-k],adams(c,k))) for k in range(1,j+1)])))
 return vals[n]
def plus(c):return vscale(F(1,2),vadd(c[:9],c[9:]))
def decomp(c):
 out=[inner(c,r) for r in irreps]
 assert all(y==0 and x.denominator==1 and x>=0 for x,y in out),out
 return [int(x) for x,y in out]
H=ca(lift(V),lift(W,-1)); U=lift(Wp)
G=[cm(U,power(H,3+i,True)) for i in range(3)]
C=[cm(power(G[0],2),power(H,3)),cm(G[1],G[0],power(H,2)),cm(ca(power(G[1],2,True),cm(G[2],G[0])),H),cm(G[2],G[1])]
R=ca(C[0],cs(-1,C[1]),C[2],cs(-1,C[3]))
param=vmul(vadd(one,D),D)
assert decomp(param)==[1,0,0,1,1,2,0,3,0]
B=vmul(Wp,V)
vertex=vmul(vmul(B,B),D)
K=vadd(plus(R),vscale(-1,vertex))
for name,c in zip(['C0','C1','C2','C3','R+','vertex+','kernel+'],list(map(plus,C))+[plus(R),vertex,K]):
 print(name,'dimension',c[0], 'multiplicities',decomp(c),'family',inner(param,c))
assert plus(R)[0]==z(2409) and vertex[0]==z(180) and K[0]==z(2229)
assert R[0]==z(4755)
print('PASS: bounded exact character arithmetic; no actual HM evaluations.')
expected=[[59,0,0,188,181,249,0,308,0],[27,0,0,72,79,97,0,124,0],[7,0,0,7,18,10,0,17,0],[1,0,0,0,2,0,0,1,0],[38,0,0,123,118,162,0,200,0],[3,0,0,9,9,12,0,15,0],[35,0,0,114,109,150,0,185,0]]
chars=list(map(plus,C))+[plus(R),vertex,K]
assert list(map(decomp,chars))==expected
assert [inner(param,c) for c in chars]==list(map(z,[1850,744,103,6,1203,90,1113]))
assert 1850-1203==647 and 1850-90==1760 and 1760-744+103-6==1113
negative=vscale(F(1,2),vadd(R[:9],vscale(-1,R[9:])))
assert negative[0]==z(2346) and inner(param,negative)==z(0)
# Verify the full irreducible table, source symmetric power, and determinants.
assert all(inner(r,s)==z(int(i==j)) for i,r in enumerate(irreps) for j,s in enumerate(irreps))
assert sum(int(r[0][0])**2 for r in irreps)==120
assert plus(power(lift(A),2))==vadd(one,D)
assert plus(power(lift(Wp),2,True))==one
assert power(H,5,True)==unit
print('PASS: all printed claims are asserted; complete table orthogonality and determinant checks pass.')
assert plus(power(lift(Wp),2))==V
assert plus(power(lift(V),2))==vadd(one,D)
assert all(inner(r,negative)==z(0) for r in [one,A,V,P,D])
