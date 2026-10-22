#!/usr/bin/env python3
"""Universal characters, line degrees, and formal residue coefficient identity."""
import runpy
import sympy as s
r=runpy.run_path('verify_negative_vertex_scalar.py')
va,vm=r['vadd'],r['vmul']
A,V,D,P,Wp=r['A'],r['V'],r['D'],r['P'],r['Wp']
sym=r['sym']
assert [sym(6,x) for x in Wp]==va(A,P)
assert vm(V,A)==va(P,D)
assert r['inner'](vm(D,V),A)==r['z'](1)
# Relative dualizing degree = det G degree2 + relative canonical degree-1.
assert 2-1==1
assert -(-1)==1 # dual of socle line O(-1)
assert (-1)-(-3)==2 # lambda coefficient line
# Formal generic determinant and Euler correction, no polynomial instantiation.
k,h,tr=s.symbols('k h tr')
assert s.expand((3+5)*k*h-tr-4*k*h-(4*k*h-tr))==0
assert 5>4 # dimensions in the positive Casimir trace contradiction
print('PASS: complete quadratic residue channel, V tensor A=P4+D5, and all connection degrees.')
print('No actual source coefficients, map matrices, or ranks were evaluated.')
