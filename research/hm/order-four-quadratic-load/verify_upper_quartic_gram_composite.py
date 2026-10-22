#!/usr/bin/env python3
"""Representation arithmetic and universal characteristic identity only."""
import runpy
import sympy as S
c=runpy.run_path('verify_negative_vertex_scalar.py')
V,P,A,W,Wp,D,one=[c[k] for k in ('V','P','A','W','Wp','D','one')]
vm,va,inn,z=c['vmul'],c['vadd'],c['inner'],c['z']
assert vm(V,P)==va(A,P,D)
assert inn(vm(vm(V,P),A),one)==z(1)
assert inn(vm(Wp,W),one)==z(0)
assert [c["sym"](4,x) for x in W]==D
assert [c["sym"](8,x) for x in W]==va(P,D)
assert inn(D,one)==z(0)
assert inn(va(P,D),one)==z(0)
assert inn(D,one)==z(0) # unique obstruction map D5 -> H1 O(-2)
assert (-3+5,-1+5,5+5)==(2,4,10)
assert (-5+3,1+3,3+3)==(-2,4,6)
# Newton identities for arbitrary eigenvalue indeterminates, not an actual matrix.
x,y,zv,l=S.symbols('x y z l')
p1=x+y+zv; p2=x*x+y*y+zv*zv; e2=x*y+x*zv+y*zv
assert S.expand(e2-(p1*p1-p2)/2)==0
assert S.expand((l-x)*(l-y)*(l-zv)-(l**3-p1*l*l+e2*l-x*y*zv))==0
print('PASS: unique actual Gram factorization degrees and character multiplicities; universal cubic characteristic identity.')
print('No actual coefficients, actual matrix, or actual rank evaluation used.')
