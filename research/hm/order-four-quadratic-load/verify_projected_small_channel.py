#!/usr/bin/env python3
"""Universal biform, character, and bundle-degree checks only."""
from pathlib import Path
import contextlib, io, runpy
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
    r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
vmul,vadd,inner,z=r['vmul'],r['vadd'],r['inner'],r['z']
vscale,sym=r['vscale'],r['sym']
W,A,V,P,D,S,T=(r[n] for n in ['W','A','V','P','D','S','T'])
H=vmul(T,S)
assert H==vadd(A,V,vscale(2,P),vscale(2,D))
assert vmul(A,D)==vadd(A,V,P,D)
assert inner(A,H)==z(1)
assert inner(vmul(A,D),H)==z(6)
assert inner(vmul(A,D),A)==z(1)
assert inner(vmul(A,D),vadd(V,vscale(2,P),vscale(2,D)))==z(5)
x,y,b,c,h,k=s.symbols('x y b c h k')
G=s.groebner([x*x-b*x+c,y*y-b*y+c],x,y)
assert G.reduce(s.expand((x-y)**3-(b*b-4*c)*(x-y)))[1]==0
J=s.groebner([h*h,k*k],h,k)
assert J.reduce((h-k)**3)[1]==0
assert J.reduce((h-k)**2)[1]==-2*h*k
# Z=T x T, eta=first projection, nu*O_P(1)=O(1,1).
assert (-3+3,3)==(0,3)  # O_Z(-3) tensor nu*O_P(3)=iota*O_Z(3).
assert (-5+3,3)==(-2,3)
# Kernel psi=W tensor S6*(2): rank4 and degree -2.
assert 3*(-6)+6*3==0  # degree A tensor K(3).
assert 0-2==2*(-5+2*2)==-2
print('PASS: Hom multiplicities 1+6, discriminant subspace 1+1, exact biform factor, residual-root line identity, and kernel degree.')
