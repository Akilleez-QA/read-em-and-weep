#!/usr/bin/env python3
"""Universal transvectants and representation identities, not actual HM entries."""
from pathlib import Path
import contextlib, io, runpy
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
    r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
vadd,vmul,inner,z,sym=r['vadd'],r['vmul'],r['inner'],r['z'],r['sym']
A,V,P,D,W,T,one=(r[n] for n in ['A','V','P','D','W','T','one'])
assert vmul(T,W)==vadd([sym(6,x) for x in W],D)
assert inner(vmul(T,W),one)==z(0)
assert [sym(10,x) for x in W]==vadd(A,V,D)
assert inner(vmul(A,D),vadd(A,V,D))==z(3)
x,y,u,v,a,b,c,d=s.symbols('x y u v a b c d')
ell=u*x+v*y
w1=a*x+b*y;w2=c*x+d*y
f=ell**3*w1;g=ell**3*w2
tr=s.diff(f,x,2)*s.diff(g,y,2)-2*s.diff(f,x,y)*s.diff(g,x,y)+s.diff(f,y,2)*s.diff(g,x,2)
assert s.expand(tr+18*(u*b-v*a)*(u*d-v*c)*ell**4)==0
print('PASS: high-channel Hom vanishing, exact universal second transvectant, and remaining 3-to-3 representation dimensions.')
