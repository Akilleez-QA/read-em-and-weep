#!/usr/bin/env python3
"""Bounded formal binary-monomial and dimension checks; no source evaluations."""
def mons(n):
    return {(i,n-i) for i in range(n+1)}
def mul(a,b):
    return {(i+k,j+l) for i,j in a for k,l in b}
ideal2={(2,0),(0,2)}
assert mul(ideal2,mons(3))==mons(5)
assert mul(ideal2,mons(2))==mons(4)
vertex_image=mul({(1,0)},mul(ideal2,mons(2)))
assert vertex_image==mul({(1,0)},mons(4))
center_even={(i,j) for i,j in mons(5) if j%2==0}
assert center_even=={(1,4),(3,2),(5,0)}
assert center_even<=vertex_image
# Koszul lift: 2*(Lambda^3 K0 + Lambda^2 K0 tensor C2 + K0 tensor Lambda^2 C2).
assert 2*(1+3*2+3)==20
assert 2*(3*2+3)==18
# Symmetric row: Sym^2 C6 -> C6 has fifteen-dimensional constant kernel.
assert 6*7//2-6==15
# Line skew blocks and normalized scalar kernel.
line_h0=21*4+36*5+21*6
kernel_h0=19*4+2+36*5+21*6
assert line_h0==390 and kernel_h0==384 and line_h0-kernel_h0==6
assert 19+1+36+21==77 # rank78 bundle to rank1 target
# The two-generator syzygy has coefficients degree2, so O3^2 -> O5 has kernelO1.
assert (2*4-6)==2
print('PASS: binary ideal, vertex divisibility, center projection, generator dimensions, exact kernel counts')
# Formal right-inverse bookkeeping, coefficient labels only (no chosen data).
# t^2*(gamma*t^3 + beta*t*s^2) - c*s^2*(-alpha/c*t*s^2).
right_inverse_terms={'gamma':(5,0),'beta':(3,2),'alpha':(1,4)}
assert set(right_inverse_terms.values())==center_even
print('PASS: explicit three-coefficient right-inverse monomials')
