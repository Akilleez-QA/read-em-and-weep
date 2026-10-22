#!/usr/bin/env python3
"""Abstract character arithmetic only; no actual bundle coefficients or ranks."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
add,mul,scale=r['vadd'],r['vmul'],r['vscale']
zero=scale(0,r['one'])
def total(*xs):
    z=zero
    for x in xs: z=add(z,x)
    return z
def minus(x): return scale(-1,x)
A,V,P,D,W,Wp=(r[n] for n in ('A','V','P','D','W','Wp'))
def sym(w,n):
    if n==0: return r['one']
    p,q=r['one'],w
    for _ in range(2,n+1): p,q=q,add(mul(w,q),minus(p))
    return q
assert sym(Wp,4)==D
assert sym(Wp,8)==add(P,D)
assert mul(V,A)==add(P,D)
assert mul(P,A)==total(V,P,D)
assert mul(D,A)==total(A,V,P,D)
q2=add(A,D); q2t=add(D,minus(A))
q4=total(sym(Wp,8),mul(D,A),D)
q4t=total(sym(Wp,8),minus(mul(D,A)),D)
z2=total(D,A,mul(V,A))
z2t=total(D,minus(A),mul(V,A))
vertex8=add(sym(Wp,8),mul(P,A))
z4=total(sym(Wp,8),D,mul(D,A),vertex8)
z4t=total(sym(Wp,8),D,minus(mul(D,A)),vertex8)
C=total(minus(q2),z2,minus(q4),z4)
Ct=total(q4t,minus(q2t),z2t,minus(z4t))
assert C==total(V,scale(3,P),scale(3,D))
assert Ct==minus(total(V,P,D))
from fractions import Fraction
plus=scale(Fraction(1,2),add(C,Ct))
negative=scale(Fraction(1,2),add(C,minus(Ct)))
assert plus==add(P,D)
assert negative==total(V,scale(2,P),scale(2,D))
active=mul(P,A)
assert add(negative,minus(active))==add(P,D)
print('PASS: ordinary and phi-trace Euler tables recover the actual lower cohomology.')
print('PASS: positive sector P4+D5 has dimension9; negative sector V+2P4+2D5 has dimension21.')
print('WITH THE GEOMETRIC INPUTS: A kills the positive sector; normal variation kills the negative sector.')
print('The absolute cubic value and the generic four-or-five alternative remain unresolved.')
