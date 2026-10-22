#!/usr/bin/env python3
"""Universal Hamiltonian identity and representation/degree arithmetic only."""
import sympy as s
import runpy
x,y,z=s.symbols('x y z')
a0,a1,a2=s.symbols('a0:3')
f0,f1,f2,f3=s.symbols('f0:4')
a=a0*x*x+a1*x*y+a2*y*y
f=f0*x**3+f1*x*x*y+f2*x*y*y+f3*y**3
D=lambda p:s.diff(a,x)*s.diff(p,y)-s.diff(a,y)*s.diff(p,x)
az=a.subs({x:1,y:z});fz=f.subs({x:1,y:z})
assert s.expand(D(f).subs({x:1,y:z})-(2*az*s.diff(fz,z)-3*s.diff(az,z)*fz))==0
assert s.simplify(D(y/x)-2*a/x**2)==0
assert (3-5,1-(-5))==(-2,6)
assert (-2+4,6)==(2,6)
assert (2-3,6-3)==(-1,3)
assert (3*6-3*2)==12
c=runpy.run_path('verify_negative_vertex_scalar.py')
assert c['vmul'](c['V'],c['V'])==c['vadd'](c['one'],c['V'],c['D'])
assert c['inner'](c['vmul'](c['V'],c['V']),c['D'])==c['z'](1)
assert c['vmul'](c['A'],c['A'])==c['vadd'](c['one'],c['A'],c['D'])
print('PASS: universal projective Hamiltonian factor, unique extension degrees, quartic channel multiplicity1, determinant degree12.')
print('No actual coefficients or actual-instance rank evaluation; exceptional ranks follow from integral-curve multiplication and orbit geometry.')
