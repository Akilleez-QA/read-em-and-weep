#!/usr/bin/env python3
"""Universal exact Euler-character check. No actual coefficients or ranks.

Actual geometric inputs: the equivariant normalized HM monad K-class,
H1(End_0 F)=End_0(U), and H0=H3=H4=0. U=V+W is ambient.
"""
from fractions import Fraction as F
from pathlib import Path
import json

def z(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def total(values):
    result=z(0)
    for x in values: result=add(result,x)
    return result

def va(*xs): return [total(v) for v in zip(*xs)]
def vs(k,x): return [scale(k,a) for a in x]
def vm(x,y): return [mul(a,b) for a,b in zip(x,y)]
def sym(n,x):
    a,b=z(1),x
    if n==0: return a
    for k in range(2,n+1): a,b=b,sub(mul(x,b),a)
    return b

phi=z(F(1,2),F(1,2)); phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
one=[z(1)]*9; A=[sym(2,x) for x in W]; S=[sym(3,x) for x in W]
D=[sym(4,x) for x in W]; T=[sym(5,x) for x in W]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=va([sym(6,x) for x in W],vs(-1,P)); Wp=va(vm(W,P),vs(-1,T))
irreps={'1':one,'W':W,'Wp':Wp,'A':A,'V':V,'P':P,'S':S,'D':D,'T':T}
def inner(x,y): return scale(F(1,120),total(scale(k,mul(a,b)) for k,a,b in zip(sizes,x,y)))
def decompose(x):
    out={}
    for name,y in irreps.items():
        r=inner(x,y)
        assert r[1]==0 and r[0].denominator==1
        if r[0]: out[name]=int(r[0])
    reconstructed=va(*[vs(m,irreps[n]) for n,m in out.items()]) if out else [z(0)]*9
    assert reconstructed==x
    return out
for n,x in irreps.items():
    for m,y in irreps.items(): assert inner(x,y)==z(n==m)
# Determine power maps from the faithful SU2 trace, independently of the
# ambient symmetric-power formula used by the original project verifier.
def trace_power(x,k):
    a,b=z(2),x
    if k==0: return a
    for j in range(2,k+1): a,b=b,sub(mul(x,b),a)
    return b
power_maps={k:[W.index(trace_power(x,k)) for x in W] for k in range(1,6)}
def adams(x,k): return [x[j] for j in power_maps[k]]
def symmetric_powers(x,n):
    result=[one]
    for k in range(1,n+1):
        result.append(vs(F(1,k),va(*[vm(adams(x,j),result[k-j]) for j in range(1,k+1)])))
    return result
U=va(V,W); N=va(A,Wp)
Lambda2U=vs(F(1,2),va(vm(U,U),vs(-1,adams(U,2))))
assert Lambda2U==va(V,vm(V,W),one)
O=symmetric_powers(U,5)
# Separate direct-sum/symmetric-square formula for an independent check.
def symmetric_three(n,x): return total(sym(2*n-4*j,x) for j in range(n//2+1))
for n in range(6):
    direct=[total(mul(symmetric_three(j,xp),sym(n-j,x)) for j in range(n+1)) for x,xp in zip(W,Wp)]
    assert O[n]==direct
Fc={-1:vs(-1,N),0:va(vm(Wp,Lambda2U),vs(-1,N)),1:vs(-1,vm(Wp,U)),2:Wp}
chi=vs(-1,one)
for i,ci in Fc.items():
    for j,cj in Fc.items():
        twist=1+i+j
        assert -1<=twist<=5
        if twist>=0: chi=va(chi,vm(vm(ci,cj),O[twist]))
H1=va(vm(U,U),vs(-1,one))
H2=va(chi,H1)
assert H1[0]==z(24) and chi[0]==z(-22)
assert H2==W and H2!=Wp
report={'scope':'Exact representation-ring Euler computation; no actual coefficients or ranks.',
        'ambient_U':'V+W','monad_N':'A+Wp','monad_middle_representation':'Wp',
        'H1_B0':decompose(H1),'chi_B0':decompose(chi),'H2_B0':decompose(H2),
        'ambient_symmetric_powers_independently_cross_checked':True,
        'power_maps':power_maps}
Path(__file__).with_name('h2_B0_character.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
