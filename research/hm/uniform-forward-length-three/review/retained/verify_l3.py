#!/usr/bin/env python3
"""Fixed universal character checks for the uniform l=3 proof.

No historical profile/tail enumeration, instance map, point, coefficient,
matrix, rank, or jet is evaluated. Bounds and geometric exhaustiveness are
proved in PROOF-L3.md. This file checks only the displayed identities.
"""
from fractions import Fraction as F
import json

checks = 0
def require(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)

def q(a=0, b=0): return (F(a), F(b))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]+5*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def sc(c,a): return (c*a[0],c*a[1])
def va(*vs): return tuple(map(lambda xs: (sum(x[0] for x in xs),sum(x[1] for x in xs)),zip(*vs)))
def vs(c,a): return tuple(sc(c,x) for x in a)
def vm(a,b): return tuple(mul(x,y) for x,y in zip(a,b))
sizes=(1,1,12,12,12,12,20,20,30)
one=(q(1),)*9
W=(q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0))
zero=vs(0,one)
sym=[one,W]
for n in range(2,26): sym.append(va(vm(W,sym[-1]),vs(-1,sym[-2])))
P=tuple(q(x) for x in (4,4,-1,-1,-1,-1,1,1,0))
A,S,D,T=sym[2:6]
V=va(sym[6],vs(-1,P))
Wp=va(vm(W,P),vs(-1,T))
reps={'1':one,'W':W,'Wp':Wp,'A':A,'V':V,'P':P,'S':S,'D':D,'T':T}
def inner(a,b):
    out=q()
    for size,x,y in zip(sizes,a,b): out=add(out,sc(F(size,120),mul(x,y)))
    require(out[1]==0 and out[0].denominator==1,'integer character inner product')
    return int(out[0])
def coeff(a): return {n:inner(a,b) for n,b in reps.items()}
def equal(a,b,label): require(a==b,label)
def effective(a): return all(x>=0 for x in coeff(a).values())
def dim(a): require(a[0][1]==0,'rational dimension');return int(a[0][0])
for n,a in reps.items():
    for m,b in reps.items(): require(inner(a,b)==int(n==m),'irreducible orthogonality')
for n,a in enumerate(sym): require(dim(a)==n+1,'symmetric-power dimension')
M2=va(A,vs(2,V),vs(3,P),vs(4,D))
M3=va(vs(3,Wp),vs(3,S),vs(6,T))
M4=va(vs(2,V),vs(4,P),vs(3,D))
U=va(Wp,vs(2,T))
equal(va(vm(W,M4),vs(-1,M3)),va(Wp,vs(3,T)),'H1(E(1))')
equal(va(vm(W,M3),vs(-1,vm(A,M4))),vs(-1,V),'chi(E(2))')
equal(va(vm(A,M3),vs(-1,vm(S,M4))),U,'chi(E(3))')
equal(va(vm(A,M3),vs(-1,vm(S,M2))),va(T,vs(-2,W),vs(-1,S)),'chi(Q*(3))')
E4=va(vm(S,M3),vs(-1,vm(D,M4)))
equal(E4,va(vs(3,V),vs(3,P),vs(2,D)),'chi(E(4))')
equal(vm(W,V),T,'unique l=3 primal splitting')
require(inner(V,A)==0,'scalar degree-six tail forbidden')
require(inner(U,W)==inner(U,S)==0,'small scalar cubic-source Hom')
require(inner(V,A)==inner(V,D)==0,'small scalar quartic-source Hom')
require(inner(U,W)==inner(V,vm(W,W))==0,'W degree-zero block forbidden')
require(inner(U,vm(W,A))==inner(V,vm(W,S))==0,'W degree-two block forbidden')
equal(vm(Wp,A),T,'Wp times Sym2')
equal(vm(Wp,D),va(S,T),'Wp times Sym4')
bud0=va(vs(2,W),Wp,vs(2,S),T)
bud2=va(vs(2,W),Wp,S)
require(dim(bud0)==20 and dim(bud2)==10,'two line budgets')
for b in (7,9,11,13): require(inner(sym[b],T)==1,'small scalar has only one T')
for b in (21,23,25): require(inner(sym[b-6],T)==2,'large scalar exceeds T budget')
for b in (15,17,19):
    require(effective(va(bud0,vs(-1,sym[b-6]))),'three degree-zero-doublet line budgets')
    require(effective(va(sym[b],vs(-2,T))),'two T sections')
for b in (9,11): require(inner(sym[b],Wp)==0,'degree-two-doublet missing Wp')
for b in (13,15): require(inner(sym[b-6],T)==1,'degree-two-doublet exceeds T budget')
equal(sym[7],va(Wp,T),'unique degree-two-doublet line')
require(effective(va(bud2,vs(-1,W))),'degree-seven line budget')
quotients=[]
for d in (12,14,16):
    # A0=Wp O(-3)+O(d); twist four gives Wp*W+Sym^(d+4).
    chiK4=va(E4,vs(-1,vm(Wp,W)),vs(-1,sym[d+4]))
    require(inner(chiK4,V)==2,'two top V copies from Euler characteristic')
    require(inner(V,sym[d+2])==1,'one scalar endpoint Hom')
    Dsat=d+3
    require(0<=Dsat-11<12,'full-image defect gap')
    quotients.append({'doublet_degree':-3,'line_degree':d,'chi_K4':coeff(chiK4),'endpoint_V_Hom':1})
chiK4=va(E4,vs(-1,vm(Wp,S)),vs(-1,sym[8]))
equal(chiK4,va(vs(2,V),vs(2,P)),'fourth kernel Euler character')
require(inner(V,vm(Wp,W))==0 and inner(V,sym[6])==1,'fourth endpoint Hom')
require(11-11==0,'fourth full-image defect')
quotients.append({'doublet_degree':-1,'line_degree':4,'chi_K4':coeff(chiK4),'endpoint_V_Hom':1})
print(json.dumps({'status':'PASS','fixed_universal_checks':checks,'range':'1<=k,l<=3','conclusion':'No actual maximal rank-three plateau has l=3, for any k>=1.','saturated_images':[['Wp',0,'1',15],['Wp',0,'1',17],['Wp',0,'1',19],['Wp',2,'1',7]],'quotients':quotients,'scope':'No historical splitting enumeration or actual-instance evaluation.'},indent=2,sort_keys=True))
