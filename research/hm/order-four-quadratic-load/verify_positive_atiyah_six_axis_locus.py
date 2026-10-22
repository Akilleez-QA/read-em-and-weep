#!/usr/bin/env python3
"""Universal representation and Hilbert checks only."""
import runpy
import sympy as s
r=runpy.run_path('verify_negative_vertex_scalar.py')
va,vm=r['vadd'],r['vmul']
A,V,D,P,one=r['A'],r['V'],r['D'],r['P'],r['one']
assert vm(V,A)==va(P,D)
assert vm(D,A)==va(A,V,P,D)
# Sym²(A) via character identity (A tensor A)=1+A+D.
assert vm(A,A)==va(one,A,D)
for X in [one,A,va(one,D)]:
    assert r['inner'](V,X)==r['z'](0)
n=s.symbols('n')
chi=lambda k:s.expand((k+2)*(k+1)/2)
length=s.expand(chi(n)-4*chi(n-3)+3*chi(n-4))
assert length==6
# C5 eigenweight multiplicities, independent of any map.
weights={'A':[0,1,4], 'V':[0,2,3], 'P4':[1,2,3,4]}
assert weights['A'].count(0)==weights['V'].count(0)==1
assert weights['P4'].count(0)==0
print('PASS: kernel-character exclusion, determinantal length6, and six C5 fixed axes.')
print('No actual map matrix, rank, coefficient, or parameter scan was evaluated.')
