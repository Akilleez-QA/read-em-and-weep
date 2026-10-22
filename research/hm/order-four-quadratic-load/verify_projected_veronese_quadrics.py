#!/usr/bin/env python3
"""Universal A5 character and Chern checks; no actual HM matrix evaluations."""
import sympy as s
p=(1+s.sqrt(5))/2; pp=1-p
V=[3,-1,0,p,pp]; A=[3,-1,0,pp,p]; U=[4,0,1,-1,-1]; D=[5,1,-1,0,0]
one=[1]*5; L=[x+y for x,y in zip(V,U)]; square=[0,0,2,4,3]
S2=[s.simplify((L[i]**2+L[square[i]])/2) for i in range(5)]
S6=[]
for c in V:
 h=[s.Integer(1)]
 for k in range(1,7):
  h.append(s.simplify(c*h[k-1]-(c*h[k-2] if k>=2 else 0)+(h[k-3] if k>=3 else 0)))
 S6.append(h[6])
for i in range(5):
 assert s.simplify(S2[i]-(2+A[i]+2*U[i]+3*D[i]))==0
 assert s.simplify(S6[i]-(2+V[i]+2*U[i]+3*D[i]))==0
 assert s.simplify(A[i]*L[i]-(V[i]+2*U[i]+2*D[i]))==0
H=s.symbols('H')
N=s.series((1+3*H)**7/(1+H)**3,H,0,3).removeO().expand()
assert N==1+18*H+132*H**2
virtual=s.series((1-18*H+132*H**2)/(1-6*H)**3,H,0,3).removeO().expand()
assert virtual==1+24*H**2
cycles=[(a,b,c,d,e) for a in range(5) for b in range(3) for c in range(3) for d in range(2) for e in range(2) if 6*a+10*b+12*c+15*d+20*e==24]
assert cycles==[(0,0,2,0,0),(2,0,1,0,0),(4,0,0,0,0)]
print('PASS: forced A quadratic kernel and V cokernel; no matching-channel rank assumption.')
print('PASS: forced net linear multiples representation V+2*4+2*5.')
print('PASS: conormal virtual Chern class 1+24H^2.')
print('PASS: conditional length24 orbit cycles: 4Z6, 2Z6+Z12, or2Z12.')
print('LIMIT: orbit geometry, finite degeneracy, and actual ranks are not inferred by this script.')
