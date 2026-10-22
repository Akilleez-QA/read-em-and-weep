#!/usr/bin/env python3
"""Complete universal sl2 identities and marking weights; no actual source."""
import sympy as s

def mat(tag):
    a,b,c=s.symbols(tag+'0 '+tag+'1 '+tag+'2')
    return s.Matrix([[a,b],[c,-a]])
def zero(M):
    if isinstance(M,s.MatrixBase):
        assert all(s.expand(x)==0 for x in M), M
    else:assert s.expand(M)==0, M
X,Y,Z=mat('x'),mat('y'),mat('z')
I=s.eye(2)
zero(X*Y+Y*X-s.trace(X*Y)*I)
g=s.trace(X*(Y*Z-Z*Y))
zero(g+s.trace(Y*(X*Z-Z*X)))
zero(g+s.trace(X*(Z*Y-Y*Z)))
zero(X*Y*Z-(s.trace(X*Y)*Z-s.trace(X*Z)*Y+s.trace(Y*Z)*X)/2-g*I/4)
# Nonzero is checked as a universal polynomial, not at a numerical tuple.
assert g!=0
# The trace-pairing characterization of the commutator is the exact
# cross-product coefficient: tr([X,Y]Z)/2=g/2.
zero(s.trace((X*Y-Y*X)*Z)/2-g/2)

C,chi,gL,t,scaleL,nu,am,bm=s.symbols('C chi gL t s nu am bm',nonzero=True)
ratio=am/bm
newC=t/scaleL*C
newchi=scaleL**2*chi
newg=scaleL**3/t*gL
zero(newC*(am/t)/(bm/scaleL)-C*ratio)
zero(s.cancel(newC*newg/newchi-C*gL/chi))
zero(s.cancel((C/nu)*gL/(chi/nu)-C*gL/chi))
print('PASS: full universal quadratic, cubic, alternating and commutator trace identities.')
print('PASS: factors 1/2 and 1/4 retained in the marked Fierz formula.')
print('PASS: C_mult*g_L/chi is invariant under independent a/b-channel and q0 rescalings.')
print('No actual source, point, differential rank, or value of the residual scalar is evaluated.')
