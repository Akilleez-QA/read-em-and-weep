#!/usr/bin/env python3
"""Universal polynomial identities only; no HM instance is selected."""
import sympy as S
s,t=S.symbols('s t')
q=[s*s,s*t,t*t]
def D(f): return S.Matrix([-S.diff(f,t),S.diff(f,s)])
assert S.simplify(q[0]*D(q[2])+q[2]*D(q[0])-2*q[1]*D(q[1])) == S.zeros(2,1)
u,v,w=S.symbols('u v w')
a=u*s*s+v*s*t+w*t*t
assert S.simplify(D(a*a)-2*a*D(a)) == S.zeros(2,1)
x=S.Matrix(S.symbols('x0:3')); z=S.Matrix(S.symbols('z0:3'))
K=x*(x.dot(z))-x.dot(x)*z
assert S.expand(x.dot(K)) == 0
trace=S.Matrix([S.expand(sum(S.diff(k,xi,2) for xi in x)/2) for k in K])
assert trace == -2*z
assert 1+1+2+2 == 6 and 1+2+2 == 5 and 5-2 == 3
print('PASS: Hamiltonian quartic factorization and trace-removing contraction-kernel identity.')
print('This is a representative normalization, not a nonzero cubic obstruction certificate.')
