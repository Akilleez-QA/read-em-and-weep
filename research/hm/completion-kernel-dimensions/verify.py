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

H=ca(lift(V),lift(W,-1)); U=lift(Wp,-1); source=ca(U,lift(A))
G=[cm(U,power(H,3+i,True)) for i in range(3)]
O3=ca(power(H,3),cs(-1,H))
EQ4=ca(cm(G[0],O3),cs(-1,cm(G[1],ca(power(H,2),cs(-1,unit)))),cm(G[2],H))
N=ca(cm(source,EQ4),cs(-1,cm(power(source,2,True),O3)))
sp2=ca(cm(power(G[0],2),H),cs(-1,cm(G[1],G[0])))
param=vmul(vadd(one,D),D)
for n,c in [('EQ4',EQ4),('N',N),('sp2',sp2)]: print(n,c[0],decomp(c[:9]), 'even',decomp(plus(c)),inner(param,plus(c)))
K=vadd(plus(N),plus(sp2),A,D)
print('K',K[0],decomp(K),inner(param,K))
assert all(inner(r,s)==z(int(i==j)) for i,r in enumerate(irreps) for j,s in enumerate(irreps))
assert power(H,5,True)==unit and power(U,2,True)==unit
assert N[0]==z(2050) and sp2[0]==z(850)
assert decomp(plus(N))==[14,0,0,55,45,72,0,86,0]
assert decomp(plus(sp2))==[9,0,0,22,25,27,0,36,0]
assert K[0]==z(1478) and inner(param,K)==z(738)
assert decomp(K)==[23,0,0,78,70,99,0,123,0]
ambient=vadd(vscale(38,one),vscale(123,A),vscale(118,V),vscale(162,P),vscale(200,D))
image=vadd(ambient,vscale(-1,K))
assert decomp(image)==[15,0,0,45,48,63,0,77,0]
assert image[0]==z(931) and inner(param,image)==z(465)
ambiguity=plus(cm(source,source,power(H,2)))
assert ambiguity[0]==z(189) and inner(param,ambiguity)==z(95)
full=vadd(K,ambiguity)
assert decomp(full)==[29,0,0,90,79,109,0,139,0]
assert full[0]==z(1667) and inner(param,full)==z(833)
assert 1203-738==465 and 738+95==833
print('PASS: exact abstract characters, determinant lines, kernel, image and completion torsor dimensions; no actual coefficient or matrix evaluation.')
source4=plus(cm(source,source,power(H,4)))
cochain=vadd(ambient,source4)
constraints=vadd(cochain,vscale(-1,full))
print('source4',source4[0],decomp(source4),inner(param,source4))
print('full cochain constraints',constraints[0],decomp(constraints),inner(param,constraints))
assert source4[0]==z(878) and inner(param,source4)==z(440)
assert inner(param,cochain)==z(1643)
assert constraints[0]==z(1620) and inner(param,constraints)==z(810)
class_image=vadd(A,D)
class_middle=vadd(K,vscale(-1,class_image))
class_full=vadd(full,vscale(-1,class_image))
assert inner(param,class_image)==z(4)
assert decomp(class_middle)==[23,0,0,77,70,99,0,122,0]
assert class_middle[0]==z(1470) and inner(param,class_middle)==z(734)
assert class_full[0]==z(1659) and inner(param,class_full)==z(829)
print('PASS: class variation family4; nonempty class-fixed middle/full fibers734/829.')
assert decomp(source4)==[15,0,0,46,41,58,0,74,0]
assert decomp(constraints)==[24,0,0,79,80,111,0,135,0]
assert decomp(class_full)==[29,0,0,89,79,109,0,138,0]
