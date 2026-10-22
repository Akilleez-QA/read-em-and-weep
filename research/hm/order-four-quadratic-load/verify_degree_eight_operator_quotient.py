#!/usr/bin/env python3
import sympy as s
f,g,k,r,p=s.symbols('f g k r p')
N=s.Matrix([[f*g,-f*f],[g*g,-f*g]])
K=s.Matrix([[k,0],[r,-k]])
P=s.Matrix([[1,0],[p,1]])
assert s.expand(s.trace(N*K)-2*f*g*k+f*f*r)==0
assert s.simplify(P*K*P.inv()-s.Matrix([[k,0],[r+2*p*k,-k]]))==s.zeros(2)
assert K*s.Matrix([f,g])==s.Matrix([k*f,r*f-k*g])
assert s.Rational(9,2)+4-s.Rational(3,2)==7
assert -s.Rational(5,2)+4-s.Rational(5,2)==-1
assert -7+4-1==-4
rankE,degE=6+4,6*(-1)+4*7
rankJ,degJ=3+1,3*(-4)+4
assert (rankE-rankJ,degE-degJ)==(6,30)
assert 4*(7+1)==32
assert 3*3-5==4
assert 6+30==32+4==36
print('PASS: actual graded bundle twists, conjugation factor2, square-ideal map, and quotient dimensions32,36,4.')
print('No actual source coefficient or rank evaluation; extension nonvanishing and global comparison are geometric inputs.')
