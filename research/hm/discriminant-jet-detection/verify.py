#!/usr/bin/env python3
"""Bounded universal cubic identities only; no actual HM/source data."""
import sympy as s
x,y,z,u,v=s.symbols('x y z u v')
Delta=y*y-x*z
box=lambda f:s.diff(f,y,2)-4*s.diff(f,x,z)
assert box(Delta)==6
monomials=[x**i*y**j*z**(3-i-j) for i in range(4) for j in range(4-i)]
assert len(monomials)==10
for L in (x,y,z):
    assert s.expand(box(Delta*L)-10*L)==0
for f in monomials:
    L=box(f)/10
    H=s.expand(f-Delta*L)
    assert s.expand(box(H))==0
    assert s.expand(H+Delta*L-f)==0
    assert s.expand((f-H).subs({x:u*u,y:u*v,z:v*v}))==0
    assert s.expand(H-Delta*box(H)/10-H)==0
# Infinitesimal SL2 equivariance on universal cubics, in this convention.
E=lambda f:2*y*s.diff(f,x)+z*s.diff(f,y)
F=lambda f:x*s.diff(f,y)+2*y*s.diff(f,z)
assert s.expand(E(Delta))==s.expand(F(Delta))==0
for f in monomials:
    assert s.expand(box(E(f))-E(box(f)))==0
    assert s.expand(box(F(f))-F(box(f)))==0
# The restriction contains every binary sextic monomial: exponents 2i+j.
assert {2*i+j for i in range(4) for j in range(4-i)}==set(range(7))
# Every binary quadratic is the restriction of one unique linear form.
assert [L.subs({x:u*u,y:u*v,z:v*v}) for L in (x,y,z)]==[u*u,u*v,v*v]
# Dimensions below are imported representation multiplicities from pinned PR696,
# not newly computed actual maps or ranks.
target=(1,2,2,2); cubic_input=(3,3,3,4); normal_input=(1,1,1,1)
whole=sum(a*b for a,b in zip(target,cubic_input))
normal=sum(a*b for a,b in zip(target,normal_input))
assert (whole,normal,whole-normal)==(23,7,16)
assert 10==7+3 and 3<4
print('PASS: Box(Delta)=6; Box(Delta L)=10L; ten universal cubic decompositions.')
print('PASS: harmonic projection, square restriction, linear normal reconstruction; dimensions 23=16+7.')
print('No actual HM/source value, selected direction, matrix or derivative evaluated.')
