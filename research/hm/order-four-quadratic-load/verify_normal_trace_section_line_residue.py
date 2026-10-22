"""Universal algebra checks only; actual geometric inputs remain cited in the proof."""
import sympy as s
f,g,p,v1,v2,w1,w2,t=s.symbols('f g p v1 v2 w1 w2 t')
a=-f*w2-g*w1
b=2*f*w1
c=-2*g*w2
assert s.expand(f*f*c-2*f*g*a-g*g*b)==0
assert s.expand(c-2*w2*(-g))==0
assert s.expand(-2*a-(2*w2*f+2*w1*g))==0
assert s.expand(-b-(-2*w1*f))==0
# Determinant pairing transported to the Hilbert--Burch kernel.
assert s.expand(v1*(2*w2)/2+v2*(-2*w1)/2-(v1*w2-v2*w1))==0
R=g*v1+f*v2
Rp=(g+p*f)*v1+f*(v2+p*v1)
assert s.expand(Rp*g*g-R*(g+p*f)**2+f*f*(2*p*g*v2+p*p*R))==0
assert s.expand(((g*(v1+f*t)+f*(v2+g*t))-R)/2-f*g*t)==0
assert s.expand(f*(v2+g*t)-g*(v1+f*t)-(f*v2-g*v1))==0
# Universal generalized fractions: cancellation realizes the residue transformation.
assert s.cancel((f*g*t)/(f*f*g*g)-t/(f*g))==0
# Degree and line factors, not an actual-instance evaluation.
assert 2*3+2*5-2==14
assert 3+5+6==14
assert 14+8>14
assert -6//2-1==-4
assert -1-1==-2
# On P1: H1(O(-4)) dual is H0(O(2)); final trace is H1(O(-2)).
assert -(-4)-2==2
assert -(-2)-2==0
print('PASS: universal square duality, nonsplit transition, section-line residue, and degree/line checks')
