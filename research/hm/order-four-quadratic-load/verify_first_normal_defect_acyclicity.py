#!/usr/bin/env python3
"""Universal characters and LES arithmetic, not evaluation of an actual map."""
import runpy
r=runpy.run_path('verify_negative_vertex_scalar.py')
one=r['one']; z=r['z']; add=r['vadd']; inner=r['inner']
assert inner(one,add(r['V'],r['W']))==z(0)
assert inner(one,add(one,r['V']))==z(1)
assert inner(one,add(one,one,r['V']))==z(2)
# Established geometric input: the bracket induces an isomorphism of lines.
h1_j_inv=h1_g_inv=1
proved_isomorphism_dimension=1
h2_j_inv=h2_g_inv=h0_g_inv=0
assert h1_j_inv-proved_isomorphism_dimension==0  # H0 M(-2)^G
assert h1_g_inv-proved_isomorphism_dimension+h2_j_inv==0  # H1 M(-2)^G
print('PASS: invariant line characters and exact-sequence dimensions give H0/H1 M(-2)^G=0.')
print('The nonzero bracket is a geometric input, not inferred from dimensions or tested on an actual matrix.')
