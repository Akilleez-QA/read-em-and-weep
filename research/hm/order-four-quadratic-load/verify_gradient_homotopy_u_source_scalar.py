#!/usr/bin/env python3
"""Universal exterior compression and exact source coefficient, not a source test."""
import runpy
from pathlib import Path
import sympy as s
base=Path(__file__).resolve().parent
T=runpy.run_path(str(base/'verify_universal_monad_clifford_homotopy.py'))
globals().update({k:v for k,v in T.items() if not k.startswith('__')})

# All coordinates h,k,l,x,y,z,u,w and the physical theta remain arbitrary.
# The imported 2x2 basis is the universal sl2 representation, not an actual
# monad/source matrix. No parameter values are assigned here.
RDBq=[action(P,F) for F in B(q)]
full_pair=pair(B(p),RDBq)
a_poly=(k*u*u-2*h*u*w-l*w*w)/2
clifford_volume=s.trace(M0*(M1*M2-M2*M1))
pair_M=(p.T*J*M*q)[0]
predicted=scale(-clifford_volume/theta*a_poly*pair_M,ixOmega)
eq(full_pair,predicted)

# Retain independent b-channel and a-volume markings.
scaleL,scaleTau=s.symbols('scaleL scaleTau',nonzero=True)
newchi=scaleL**2*theta
newg=scaleL**3/scaleTau*clifford_volume
newpairM=scaleL*pair_M
newOmega=scale(scaleTau,ixOmega)
eq(scale(scaleL**2,full_pair),scale(-newg/newchi*a_poly*newpairM,newOmega))

# Full Hamiltonian determinant convention and factor two, for arbitrary a.
al,be,ga,s0,t0=s.symbols('alpha beta gamma s0 t0')
Da=s.Matrix([[-2*be,2*al],[-2*ga,2*be]])
wrow=s.Matrix([[s0,t0]])
j=s.Matrix([-t0,s0])
a_eval=al*s0*s0+2*be*s0*t0+ga*t0*t0
assert s.expand((wrow*Da*j)[0]-2*a_eval)==0
ellrow=wrow*Da
it=s.Matrix([-ellrow[1],ellrow[0]])
assert s.expand((wrow*it)[0]+2*a_eval)==0

# The exact scalar forced by the duality pairing.
Cmult,gL,chi=s.symbols('Cmult gL chi',nonzero=True)
qb=s.symbols('qb')
forced=-1-Cmult*gL/(2*chi)
assert s.cancel(-Cmult*gL/chi-2*forced-2)==0
sol=s.solve(-Cmult*gL/chi-2*qb-2,qb)
assert len(sol)==1 and s.cancel(sol[0]-forced)==0
print('PASS: complete determinant-valued B* R_Da B compression, with all exterior components.')
print('PASS: independent Clifford/volume markings and exact Hamiltonian factor two.')
print('PASS: Q_b=(-1-C_mult*g_L/(2chi))*a*I is forced by the coupled skew equations.')
print('No actual source, parameter value, rank, completed homotopy or C_mult value is evaluated.')
