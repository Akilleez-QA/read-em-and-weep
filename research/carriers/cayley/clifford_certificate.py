#!/usr/bin/env python3
"""Exact Clifford identity for the rank-seven projection; not an Atiyah test."""
import sympy as s
from itertools import product

def wedge(j):
    m=s.zeros(8)
    for mask in range(8):
        if not mask & (1<<j):
            m[mask | (1<<j),mask]=(-1)**((mask & ((1<<j)-1)).bit_count())
    return m
P=s.diag(*[(-1)**i.bit_count() for i in range(8)])
L=[wedge(j) for j in range(3)]; I=[m.T for m in L]
t,*z=s.symbols('t x1 x2 x3 y1 y2 y3')
x=z[:3];y=z[3:]
C=t*P
for j in range(3): C+=x[j]*L[j]+y[j]*I[j]
assert (C*C-(t*t+sum(x[j]*y[j] for j in range(3)))*s.eye(8)).applyfunc(s.expand)==s.zeros(8)
A,B,D,E,U,V,W=s.symbols('A B D E U V W')
N=C.subs({t:W,x[0]:-4*A,y[0]:E,x[1]:B,y[1]:D,x[2]:-(U+W),y[2]:V+W})
q=4*A*E-B*D+U*V+U*W+V*W
assert (N*N+q*s.eye(8)).applyfunc(s.expand)==s.zeros(8)
blocks=[N.diff(v) for v in [A,B,D,E,U,V,W]]
assert s.Matrix.vstack(*blocks).rank()==8
print('PASS: Clifford matrix squares to -q0 I8; common kernel of all seven coefficient matrices is zero.')
