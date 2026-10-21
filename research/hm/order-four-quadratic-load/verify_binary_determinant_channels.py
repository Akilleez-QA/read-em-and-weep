#!/usr/bin/env python3
"""Universal representation checks, not a Horrocks--Mumford matrix evaluation."""
import sympy as s
n=4
E=s.zeros(5); H=s.diag(4,2,0,-2,-4)
for i in range(1,5): E[i-1,i]=i
G=s.zeros(5)
for i in range(5): G[i,4-i]=s.Rational((-1)**i,s.binomial(4,i))
assert G==G.T and G.det()!=0
for M in [E,H]:
    assert M.T*G+G*M==s.zeros(5)
    assert (G*M).rank()==4
# Every nonzero sl2 element over C is conjugate up to nonzero scale to E or H.
# Its Sym4 action therefore yields an alternating form of rank4, not rank2.
assert [6-2*i for i in range(7) if (6-2*i)%5==0]==[0]
# The unique degree-six rotation-invariant monomial is x^3*y^3.
# In the four-dimensional A5 module, restricted to D5, neither character
# trivial nor reflection-sign occurs: characters are4,-1,0 on 1,r!=1,sr^k.
assert (4+4*(-1)+5*0)//10==0
phi=(1+s.sqrt(5))/2; phip=(1-s.sqrt(5))/2
sizes=[1,15,20,12,12]
V=[3,-1,0,phi,phip]; A=[3,-1,0,phip,phi]
D4=[4,0,1,-1,-1]; D5=[5,1,-1,0,0]
Sym8=[9,1,0,-1,-1]
assert all(s.simplify(x-y-z)==0 for x,y,z in zip(Sym8,D4,D5))
assert s.simplify(sum(n*x*y for n,x,y in zip(sizes,Sym8,V))/60)==0
assert s.simplify(sum(n*x*y for n,x,y in zip(sizes,Sym8,A))/60)==0
print('PASS: annihilator sl2 alternating forms have rank4 in both nonzero conjugacy types.')
print('PASS: Sym8 has no three-dimensional constituent; D5 has no sign in4.')
print('PASS: order-five invariant binary sextic is proportional to x^3 y^3.')
print('LIMIT: universal checks only; no actual bundle coefficients or ranks evaluated.')
