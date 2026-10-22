#!/usr/bin/env python3
import sympy as s
u,v=s.symbols('u v')
f=sum(s.Symbol(f'f{i}')*u**i*v**(3-i) for i in range(4))
g=sum(s.Symbol(f'g{i}')*u**i*v**(5-i) for i in range(6))
def tr2(p,r):
 return s.diff(p,u,2)*s.diff(r,v,2)-2*s.diff(p,u,v)*s.diff(r,u,v)+s.diff(p,v,2)*s.diff(r,u,2)
def B(p,r,m,n):
 return tr2(p,r)/(2*(2*m-1)*(2*n-1)*(2*m+2*n-1))
M=tr2(f,g); df=tr2(f,f)/2; dg=tr2(g,g)/2
error=B(f*g,f*g,4,4)-B(f*f,g*g,3,5)+2*f*g*M/112-f*f*dg/144-g*g*df/20
assert s.expand(error)==0
assert s.Rational(1,240)+s.Rational(1,210)==s.Rational(1,112)
assert s.Rational(1,36)+s.Rational(2,90)==s.Rational(1,20)
assert s.Rational(1,400)+s.Rational(2,450)==s.Rational(1,144)
print('PASS: universal harmonic square-zero correction (1/112, -1/20, 1/144), with every cubic/quintic coefficient an independent symbol.')
print('No actual HM/source coefficient or rank evaluation.')
