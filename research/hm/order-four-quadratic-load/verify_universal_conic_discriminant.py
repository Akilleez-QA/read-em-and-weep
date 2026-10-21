#!/usr/bin/env python3
"""Universal symmetric determinant and balanced jets; no HM evaluation."""
import sympy as s
x,y,z,a,b,c=s.symbols('x y z a b c')
M=s.Matrix([[x,a,b],[a,y,c],[b,c,z]])
f=s.expand(M.det())
assert f==x*y*z+2*a*b*c-x*c*c-y*b*b-z*a*a
adj=M.adjugate()
for v,expected in [(x,adj[0,0]),(y,adj[1,1]),(z,adj[2,2]),(a,2*adj[0,1]),(b,2*adj[0,2]),(c,2*adj[1,2])]:
    assert s.expand(s.diff(f,v)-expected)==0
u,v,w=s.symbols('u v w')
assert s.expand(f.subs({x:u*u,y:v*v,z:w*w,a:u*v,b:u*w,c:v*w}))==0
for g in [s.diff(f,t) for t in (x,y,z,a,b,c)]:
    assert s.expand(g.subs({x:u*u,y:v*v,z:w*w,a:u*v,b:u*w,c:v*w}))==0
layers=[3*(m+1)*max(9-2*m,0) for m in range(7)]
assert layers==[27,42,45,36,15,0,0]
assert (sum(layers[::2]),sum(layers[1::2]))==(87,78)
print('PASS: universal determinant gradient equals symmetric minor ideal')
print('PASS: rank-one Veronese parameterization lies in singular scheme')
print('PASS: balanced normal layers 27,42,45,36,15; parity totals87,78')
print('LIMIT: actual pencil isomorphism requires the companion representation proof')
