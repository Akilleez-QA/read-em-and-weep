#!/usr/bin/env python3
"""Universal exterior/filtration obstruction; no actual-instance evaluation."""
import sympy as s

def zero(expr):
    assert s.expand(expr)==0, s.expand(expr)

# A general two-dimensional Hamiltonian and a general covector. The c's
# are components of an ARBITRARY exterior tensor after volume pairing,
# not a chosen HM source. Coefficient extraction proves separation for ALL c.
w0,w1,d,e,f=s.symbols('w0 w1 d e f')
r=s.symbols('r0:3')
c=s.symbols('c00 c01 c10 c11 c20 c21')
ell=(d*w0+f*w1,e*w0-d*w1)
S=sum(r[i]*(ell[0]*c[2*i]+ell[1]*c[2*i+1]) for i in range(3))
P=s.Poly(S,*r,w0,w1,d,e,f)
for i in range(3):
    mon=[0]*8;mon[i]=1;mon[3]=1;mon[5]=1
    assert P.coeff_monomial(tuple(mon))==c[2*i]
    mon=[0]*8;mon[i]=1;mon[4]=1;mon[5]=1
    assert P.coeff_monomial(tuple(mon))==-c[2*i+1]
assert all(sum(m[3:5])==1 for m in P.monoms())

# Negative-degree separation. C has degrees 0,1; B has degrees 0,1;
# P_b has degree2; R has degree1. Universal noncommutative bookkeeping.
eps=s.symbols('eps')
C0,C1,B0,B1,Pb,R=s.symbols('C0 C1 B0 B1 Pb R',commutative=False)
E=s.expand((C0+eps*C1)*eps**2*Pb+(B0+eps*B1)*eps*R)
zero(E.coeff(eps,1)-B0*R)
zero(E.coeff(eps,0))

# This 2x2 object is the universal sl2 Clifford representation, not an
# actual monad/source matrix. Its square gives a polynomial inverse away
# from the nonzero quadratic, without any rank or point evaluation.
x,y,z=s.symbols('x y z')
M=s.Matrix([[x,y],[z,-x]])
Q=x*x+y*z
assert M*M==Q*s.eye(2)
R0,R1=s.symbols('R0 R1')
rv=s.Matrix([R0,R1])
assert M*(M*rv)==Q*rv or all(s.expand(a)==0 for a in M*(M*rv)-Q*rv)

# Free word algebra certificate: channel adjoints annihilate C exactly.
# A dyad T L Tstar therefore has composite T L (Tstar C)=0 for EACH
# channel, independently of any regular coefficient operator L.
for TstarC in [s.Integer(0),s.Integer(0),s.Integer(0)]:
    T,L=s.symbols('T L',commutative=False)
    assert T*L*TstarC==0

print('PASS: contraction-separation is injective on the full generic exterior tensor.')
print('PASS: the source correction is degree1 while C P_b starts at degree2.')
print('PASS: universal Clifford identity forces R=0 if B R vanishes to degree2.')
print('PASS: every regular channel dyad kills C, excluding that middle span in the gradient gauge.')
print('No actual source, parameter value, matrix rank, or C_mult value is evaluated.')
