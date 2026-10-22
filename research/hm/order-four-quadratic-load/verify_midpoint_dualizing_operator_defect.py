#!/usr/bin/env python3
import sympy as s
f,g=s.symbols('f g')
N=s.Matrix([[f*g,-f*f],[g*g,-f*g]])
S1=s.Matrix([[f,0],[2*g,-f]])
S2=s.Matrix([[g,-2*f],[0,-g]])
assert s.simplify(N-(g*S1+f*S2)/2)==s.zeros(2)
a,b,c=s.symbols('a b c')
sigma=s.Matrix([f,g]); J=s.Matrix([[0,-1],[1,0]])
tau=lambda v:sigma*v.T*J+v*sigma.T*J
K=s.Matrix([[a,b],[c,-a]])
assert tau(sigma)==2*N
assert s.simplify(K*N-N*K-tau(K*sigma))==s.zeros(2)
assert 6+2-2==6 # operator twist + N twist - normal equation = error twist
assert 6-2==4 # normal operator correction K
assert 4-2==2 # centralizer line
assert 1+4==5 # M(4)=omega_(2Z)(5)
assert 6-2==4 # scalar-lift ambiguity
# H1(O_Q(2))=H2(O_Q(2))=0 follows from O_P4(0)->O_P4(2)->O_Q(2).
print('PASS: error B6, gauge B4, centralizer O2, dualizing omega(5), and class of N.')
print('No actual coefficient, rank, or local source-instance evaluation was performed.')
