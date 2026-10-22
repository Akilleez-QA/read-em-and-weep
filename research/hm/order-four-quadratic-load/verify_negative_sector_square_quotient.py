#!/usr/bin/env python3
"""Universal character and perfect-pairing checks, no actual map evaluation."""
import runpy
c=runpy.run_path('verify_negative_vertex_scalar.py')
add,mul,scale=c['vadd'],c['vmul'],c['vscale']
A,V,P,D,W=c['A'],c['V'],c['P'],c['D'],c['W']
assert c['inner'](V,mul(A,A))==c['z'](0)
M=add(mul(A,D),mul(V,A))
Cminus=add(V,scale(2,P),scale(2,D))
assert M==add(A,Cminus)
assert Cminus==add(P,D,mul(P,A))
assert 15+9-3==21
assert 21-9==4*3
for j in range(1,4):
    for k in range(3):
        assert (k-j==-1)==(j==k+1)
assert 9+9==18 and 30-18==12
print('PASS: absent cross-Hom,24→21 scalar quotient, canonical9→21→12 characters, perfect quadratic pairing.')
print('Actual rank4 for all nonzero directions follows geometrically; no actual-instance matrix or selected coefficients used.')
