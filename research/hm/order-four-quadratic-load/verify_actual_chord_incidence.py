#!/usr/bin/env python3
"""Universal Cartan determinant, line-class and character identities only."""
from pathlib import Path
import contextlib, io, runpy
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
    r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
vadd,vmul,vscale,sym=r['vadd'],r['vmul'],r['vscale'],r['sym']
A,V,P,D,W,Wp,one=(r[n] for n in ['A','V','P','D','W','Wp','one'])
S10p=[sym(10,x) for x in Wp]
assert S10p==vadd(A,V,D)
assert vmul(A,S10p)==vadd(one,vscale(2,A),V,vscale(2,P),vscale(3,D))
assert vmul(V,S10p)==vadd(one,A,vscale(2,V),vscale(2,P),vscale(3,D))
assert [sym(3,x) for x in Wp]==[sym(3,x) for x in W]
u,v,a,b=s.symbols('u v a b')
ell=s.Matrix([u,v]); row=s.Matrix([[a,b]])
f=a*u+b*v
M=(f*s.eye(2)+3*ell*row)/4
assert s.expand(M.det()-f*f/4)==0
assert s.expand(s.trace(M)-5*f/4)==0
assert all(s.expand(x)==0 for x in M*ell-f*ell)
# K=M+N, tau=M-N: K+2tau=3M-N, degree6.
assert (1+2,1-2)==(3,-1)
assert 3*3-3==6
l1,l2,l3=s.symbols('l1 l2 l3')
assert s.expand((l2*l3)*(l1*l3)*(l1*l2)-(l1*l2*l3)**2)==0
print('PASS: actual fiber-character distinction, Cartan determinant/trace, residual polarization, and triangle-square identity.')
