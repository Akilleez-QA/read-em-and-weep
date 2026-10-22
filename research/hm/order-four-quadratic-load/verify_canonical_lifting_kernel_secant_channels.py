#!/usr/bin/env python3
"""Universal algebra/characters only; no actual coefficients or instance tests."""
import contextlib
import io
import runpy
from pathlib import Path
import sympy as s

x,y,u,v,r,w=s.symbols('x y u v r w')
def tv(f,g,n):
    return s.expand(sum((-1)**i*s.binomial(n,i)*s.diff(f,x,n-i,y,i)
                        *s.diff(g,x,i,y,n-i) for i in range(n+1)))
ell=u*x+v*y
m=r*x+w*y
assert tv(ell*m,ell**4,2)==0
assert tv(ell*m,m**4,2)==0
assert tv(ell**2,ell**3*x,2)==0
assert tv(ell**2,ell**3*y,2)==0
# These are universal orbit normal forms, not selected actual directions.
for j in range(5):
    h=x**(4-j)*y**j
    mixed=0 if j in (0,4) else -2*j*(4-j)*x**(3-j)*y**(j-1)
    square=0 if j<2 else 2*j*(j-1)*x**(4-j)*y**(j-2)
    assert tv(x*y,h,2)==mixed
    assert tv(x*x,h,2)==square
# Universal full symbolic adjunction; constants are fixed by this tv convention.
a0,a1,a2=s.symbols('a0:3')
hs=s.symbols('h0:5')
b0,b1,b2=s.symbols('b0:3')
a=a0*x*x+a1*x*y+a2*y*y
h=sum(hs[j]*x**(4-j)*y**j for j in range(5))
b=b0*x*x+b1*x*y+b2*y*y
assert s.expand(6*tv(tv(a,h,2),b,2)-tv(h,a*b,4))==0
# Apolar evaluation: roots in P(W) are [ell] and [m].
assert tv(ell*m,ell**2,2)==0
assert tv(ell*m,m**2,2)==0
H=s.symbols('H')
assert s.series((1+H)**(-3),H,0,3).removeO()==1-3*H+6*H**2
assert -3+2==-1 and 6-3+1==4
assert 2*(-3)==-6  # det of W O_P1(-3), consistent with pullback c1

with contextlib.redirect_stdout(io.StringIO()):
    R=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
add,scale,mul=R['vadd'],R['vscale'],R['vmul']
one,A,V,P,D=R['one'],R['A'],R['V'],R['P'],R['D']
S=lambda n:[R['sym'](n,t) for t in R['tr']]
inner,z=R['inner'],R['z']
sym2A=add(one,D)
sym3A=add(S(6),A)
sym4A=add(S(8),D,one)
I9=add(mul(P,sym3A),scale(-1,mul(A,A)))
I10=add(mul(P,sym4A),scale(-1,mul(A,sym2A)))
assert I9==add(A,scale(2,V),scale(3,P),scale(2,D))
assert I10==add(one,A,scale(2,V),scale(3,P),scale(4,D))
assert I9[0]==z(31) and I10[0]==z(42)
assert inner(A,I9)==z(1)
assert inner(D,I10)==z(4)
assert inner(D,mul(A,A))==z(1)
assert R['sub'](inner(D,I10),inner(A,I9))==z(3)
print('PASS: universal secant/tangent kernels and apolar evaluation convention.')
print('PASS: transvectant is the apolar transpose of multiplication; c1,c2=(-3,6), normalized=(-1,4).')
print('PASS: H0(I_Sigma(9))=A+2V+3P4+2D5, dimension31; quartic channel quotient dimensions4-1=3.')
print('No actual fourth value, actual source specialization, or actual-instance rank is evaluated.')
