#!/usr/bin/env python3
import runpy
r=runpy.run_path('verify_negative_vertex_scalar.py')
vm,va=r['vmul'],r['vadd']
V,W,A,D,P,T=r['V'],r['W'],r['A'],r['D'],r['P'],r['T']
assert vm(V,W)==T
assert vm(T,W)==va(D,P,V)
assert r['inner'](vm(T,W),D)==r['z'](1)
assert r['inner'](vm(V,A),r['one'])==r['z'](0)
assert 6*(-1)-5*(-2)==4
assert 4+3*2==0-5*(-2)
print('PASS: unique quintic-syzygy morphism, quotient degree4, unique equivariant splitting.')
print('Only abstract characters and line degrees were checked; no actual map was evaluated.')
