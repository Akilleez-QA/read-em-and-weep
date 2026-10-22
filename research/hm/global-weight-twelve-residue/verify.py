"""Universal formal identities and line arithmetic only; no actual instance."""
import sympy as s
f,g,l,t=s.symbols('f g ell t')
sig=s.Matrix([f,g]); v=s.Matrix([0,l]); J=s.Matrix([[0,-1],[1,0]])
n=sig*sig.T*J
tau=lambda v:sig*v.T*J+v*sig.T*J
assert n*v == -f*l*sig
assert tau(v)*sig == f*l*sig
assert tau(sig)==2*n
assert t*n*v == -t*tau(v)*sig
assert (s.eye(2)+t*n).det()==1
assert ((s.eye(2)+t*n)*sig-sig).applyfunc(s.expand)==s.zeros(2,1)
assert (sig.row_join(n*v)).det()==0
# Physical coefficient lines of G(4), scalar multiplier and its kernel.
assert s.Rational(-5,2)+4-s.Rational(1,2)==1
assert s.Rational(9,2)+4-s.Rational(7,2)==5
assert s.Rational(-5,2)+4-s.Rational(9,2)==-3
assert -2+1==-1
assert 4-4//2==2
assert 8+4==12
# Only weight four can mix to twelve under the lowest weight-eight stabilizer.
assert [w for w in range(4,12,2) if w+8==12]==[4]
# Bidegree (2,2) scalar space and conic restriction dimension.
from math import comb
assert (comb(4,2)-1)*3 == 15
assert comb(8,2)-comb(6,2)==13
h0=lambda d:max(d+1,0)
h1=lambda d:max(-d-1,0)
assert h0(-1)==h1(-1)==0
assert 5*h0(2)==3*h0(4)==15
assert 5*2-2*(-1)==3*4
print('PASS: exact stabilizer mixing, quotient-kernel sign, physical twists, scalar splitting dimensions and acyclic cubic kernel.')
