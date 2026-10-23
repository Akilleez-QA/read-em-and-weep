"""Literal bridge to all eight existing q-completed physical legs.

Checks lower reduction AND full-U source shifts, not equivalence of arbitrary
completions after dropping the q-middle.
"""
from universal_q_middle_completion_transport import *
from universal_q_orthogonal_leg_completion import q_orthogonal_legs,theta,q as actual_q0

raw=q_orthogonal_legs();G=s.Matrix.hstack(*[s.Matrix.vstack(*leg['Y']) for leg in raw])
ZG=s.Matrix.hstack(*[leg['Z'] for leg in raw]);R0=s.Matrix.vstack(*[leg['R0'] for leg in raw])
parts=[reconstruct_q_leg(G[:,j],1) for j in range(8)]
change=s.Matrix.hstack(*[p['A_new'].col_join(p['D5']) for p in parts])
As=s.Matrix.hstack(*[p['A'] for p in parts]);Cs=s.Matrix.hstack(*[p['C'] for p in parts])
base=standard_q_orthogonal_legs();module=graded_module()
assert (G-base*change-module['Acoeff']*As-module['C']*Cs).applyfunc(s.expand)==s.zeros(12,8)
assert (change[:3,:]-R0.T/theta).applyfunc(s.expand)==s.zeros(3,8)
baseZ=s.Matrix.hstack(*[homogeneous_partner(base[:,j],1)['Z'] for j in range(8)])
sigma=s.Matrix([[sum((u,w)[r]*As[2*r+a,j] for r in range(2)) for j in range(8)] for a in range(2)])
assert (ZG-baseZ*change+s.Matrix.vstack(*[Mi*sigma for Mi in Ms])).applyfunc(s.expand)==s.zeros(6,8)
print('PASS: all8 existing physical q legs exactly equal the graded standard8 plus retained A/C source shifts; actual theta retained.',flush=True)
print('PASS: all8 VWW partners transport by Zraw=Zstandard*change-B(sigma), so completed legs differ by alpha_U(sigma)/am+C(Cs).',flush=True)

K=s.zeros(8)
for i in range(8):
 for j in range(i,8):
  K[i,j]=K[j,i]=sum(c*v for c,v in zip(s.symbols(f'actual_q8_free_K_{i}_{j}_0:3'),positive))
result=q_cubic_lift(G*K*G.T,qpolynomial=actual_q0,known_defect=G*K*R0)
assert (result['exact']+actual_q0*result['correction']-G*K*G.T).applyfunc(s.expand)==s.zeros(12)
print('PASS: all108 free K coefficients in the actual raw8 basis have T=T_exact+q0 B with exact C annihilation and symmetric linear physical B.',flush=True)
print('This is a lower-middle identity only; existing N, divided arrow, C,C anomaly and actual higher companions are neither deleted nor identified with another completion.',flush=True)
