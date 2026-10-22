#!/usr/bin/env python3
"""Universal identity and representation arithmetic; no actual-instance data."""
import sympy as s
import runpy
f,g,p,u,v=s.symbols('f g p u v')
r=f*u+g*v
rp=r+2*p*f*v
assert s.expand(rp*g*g-r*(g+p*f)**2+f*f*(2*p*g*u+p*p*r))==0
P=s.Matrix([[1,0],[p,1]])
R=s.Matrix([[r,-2*f*v],[2*g*u,-r]])
assert s.expand((P*R*P.inv())[0,0]-rp)==0
assert (8-2*5,2-2*(-5))==(-2,12)
assert (-2-6,12-6)==(-8,6)
assert (7-1,7*6-12)==(6,30)
assert 3*7+3*5==36
c=runpy.run_path('verify_negative_vertex_scalar.py')
add,mul,scale=c['vadd'],c['vmul'],c['vscale']
A,V,P4,D=c['A'],c['V'],c['P'],c['D']
Wp6=add(A,P4); W6=add(V,P4)
assert c['inner'](Wp6,W6)==c['z'](1)
lhs=add(mul(A,W6),mul(V,D))
rhs=add(add(A,scale(2,V)),add(scale(3,P4),scale(3,D)))
assert lhs==rhs
print('PASS: universal r/g² transition, line degrees, rank/degree, and full36-dimensional character.')
print('Geometric inputs: actual regular-pair gluing, uniform CI, and the proven quintic evaluation sequence.')
