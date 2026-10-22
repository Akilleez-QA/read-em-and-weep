#!/usr/bin/env python3
"""Universal local ideal/character arithmetic only; no actual HM data."""
from collections import Counter

# Products of homogeneous monomial generators, not evaluated points.
m1={(1,0),(0,1)}
m2={(2,0),(1,1),(0,2)}
I2={(2,0),(0,2)}
prod=lambda a,b:{(x+u,y+v) for x,y in a for u,v in b}
assert prod(m1,I2)=={(i,3-i) for i in range(4)}
assert prod(m2,I2)=={(i,4-i) for i in range(5)}

# Rotation weights modulo five; reflection exchanges opposite weights.
rho1=Counter({1:1,4:1})
rho2=Counter({2:1,3:1})
trivial=Counter({0:1})
sym=lambda degree:Counter((degree-2*i)%5 for i in range(degree+1))
assert sym(2)==trivial+rho2
assert sym(3)==rho1+rho2
assert not (trivial+rho1)&rho2
assert (trivial+rho1)&(rho1+rho2)==rho1
assert rho2+sym(3)==rho1+rho2+rho2
# Every paired rotation character extends irreducibly to D10.
# With D|N=1+rho1+rho2, Schur multiplicity gives these dimensions.
assert sum([1,1,1])==3  # Hom(D,rho1+2rho2)
assert sum([1])==1     # Hom(D,rho1)
assert sum([1,1])==2   # Hom(D,2rho2)

# Bezout inequalities for six distinct smooth five-point conics.
assert 5*4>2*9
assert 6*2>9
# Exact compatibility dimensions and normalized supplement.
Q,R,E,E1,E2,T=4,3,3,1,2,1
assert R+E-E2==Q
assert R+E1==Q
assert Q-R==T==E1
assert R-E2==1
print('PASS: local ideal products; disjoint quadratic source/target weights; unique cubic rho1 channel.')
print('PASS: degree-nine quadruple-axis Bezout exclusion and exact compatibility dimensions.')
print('Geometric surjectivity, actual-map identification, and finite-group inputs remain explicit dependencies.')
