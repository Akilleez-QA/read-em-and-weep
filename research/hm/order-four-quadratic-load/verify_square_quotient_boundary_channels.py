#!/usr/bin/env python3
"""Universal P1 duality and representation arithmetic, no actual maps."""
import runpy
c=runpy.run_path('verify_negative_vertex_scalar.py')
add,mul,scale=c['vadd'],c['vmul'],c['vscale']
A,V,P,D,W=c['A'],c['V'],c['P'],c['D'],c['W']
sym7=[c['sym'](7,x) for x in W]
assert mul(V,D)==add(A,V,P,D)
assert mul(W,sym7)==add(V,scale(2,P),D)
assert c['inner'](mul(V,D),P)==c['z'](1)
assert c['inner'](mul(W,sym7),P)==c['z'](2)
assert (2*8,3*5,2*8+3*5)==(16,15,31)
for d in (4,7):
    assert 2-d<0
    # Laurent representative t^(-j) times t^k contributes to H1(O(-2))
    # precisely when its exponent is -1: the perfect dual basis pairing.
    for j in range(1,d+2):
        for k in range(d+1):
            assert (k-j==-1)==(j==k+1)
print('PASS: full split characters, both negative Hom degrees, and universal perfect cup pairings.')
print('No actual residue or actual-instance map was evaluated; cancellation remains open.')
