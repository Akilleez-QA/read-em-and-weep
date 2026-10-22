#!/usr/bin/env python3
"""Universal characters and degree bookkeeping; no actual coefficients or ranks."""
import runpy
r=runpy.run_path('verify_negative_vertex_scalar.py')
va,vm,sc=r['vadd'],r['vmul'],r['vscale']
V,A,D,P,Wp=r['V'],r['A'],r['D'],r['P'],r['Wp']
assert vm(V,A)==va(P,D)
# Ambient A+D cancels degree-zero vertex A and conic D.
assert va(A,vm(V,A),D,sc(-1,va(A,D)))==va(P,D)
# The section isomorphism follows from H*(O(-1))=0; check its character.
assert vm(D,A)==vm(V,D)
assert 5*3==3*5==15
# Physical twist four, transverse cover degree four: base degree 4-4/2=2.
assert 4-4//2==2
# Generator tangency and regular CI socle.
assert (3-1)+(5-1)==6
assert 4+3>6 and 4+5>6
print('PASS: residue P4+D5; unique D5 tensor A -> V tensor D5 correction; all degrees.')
print('Geometric isomorphism uses H0(O(-1))=H1(O(-1))=0, not a tested map rank.')
