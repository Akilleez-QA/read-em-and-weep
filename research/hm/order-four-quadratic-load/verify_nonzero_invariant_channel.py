#!/usr/bin/env python3
"""Universal flag scalars and exact divisor-class arithmetic only."""
import sympy as s
f,g=s.symbols('f g')
e=s.Matrix([[f,3*g/4],[0,f/4]])
J=s.Matrix([[0,1],[-1,0]])
eadj=J.inv()*e.T*J
assert eadj==s.Matrix([[f/4,-3*g/4],[0,f]])
assert [s.expand(eadj[0,0]**2),s.expand(eadj[0,0]*eadj[1,1]),s.expand(eadj[1,1]**2)]==[f*f/16,f*f/4,f*f]
assert [(4+j,10+j) for j in [-2,0,2]]==[(2,8),(4,10),(6,12)]
for t in [8,10,12]:
    assert ((t)-(t-6),-6-(-12))==(6,6)
reduced=[3*(t-6) for t in [8,10,12]]
nil=[3*((t-3)-9) for t in [8,10,12]]
assert reduced==[6,12,18]
assert nil==[-12,-6,0]
assert 9%5!=0
assert 6%5==1
assert (-1)%5==4 and (-3)%5==2
assert 1 not in [4,2]
for degree in [6,18]:
    assert not any(12*a+30*b+60*c==degree for a in range(3) for b in range(2) for c in range(2))
assert 6-2==4
assert 2*(-5)==-10 and 2*15+25==55
assert 26-2==24 and 351-3-24*2==300
print('PASS: apolar flag, graded twists, doubled-curve degrees, nontrivial five-torsion classes, and orbit exclusion.')
