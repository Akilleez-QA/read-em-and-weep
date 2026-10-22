#!/usr/bin/env python3
"""Universal character and bundle-degree arithmetic only."""
import runpy
r=runpy.run_path('verify_negative_vertex_scalar.py')
assert r['vmul'](r['V'],r['S'])==r['vadd'](r['Wp'],r['S'],r['T'])
assert r['vmul'](r['V'],r['W'])==r['T']
rank_e,deg_e=17,-54
rank_k,rank_k2=rank_e-3,rank_e-6
assert (rank_k,rank_k2)==(14,11)
deg_k_case1=deg_e-3*(-2)
assert deg_k_case1==-48
assert deg_k_case1+4*rank_k==8>0
deg_k_case2=deg_e
deg_k2=deg_k_case2-3*(-2)
assert deg_k2==-48
assert deg_k2+5*rank_k2==7>3
assert 1+3<5 and 0+4<5
print('PASS: both rank-three pairing images contradict the next one or two persistent derivative steps.')
print('No actual map or rank was evaluated; saturation and section-surjectivity are geometric inputs proved in the note.')
