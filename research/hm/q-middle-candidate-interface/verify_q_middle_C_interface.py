"""Entire 234-coefficient q-middle C interface, no instance or rank tests."""
from universal_q_middle_C_interface import *
BB=s.zeros(12)
for i in range(12):
 for j in range(i,12):
  BB[i,j]=BB[j,i]=sum(c*v for c,v in zip(s.symbols(f'Cinterface_free_B_{i}_{j}_0:3'),positive))
record=q_middle_C_interface(BB)
print('PASS: all234 free coefficients have exact zero-WW D3 after subtracting the canonical q full-U quotient; the VWW-to-mixed Koszul conversion is literal.',flush=True)
am,bm,cm,kAt=s.symbols('qmi_am qmi_bm qmi_cm qmi_kAt',nonzero=True)
kap=bm/am
Ccols=[C_column(sp)[0] for sp in mon(2)]
N=[adds(record['quotient_Y'][i],sc(-kap,vww_leg(record['quotient_Z'][:,i]))) for i in range(3)]
rem=[adds(record['D3'][i],sc(kap,vww_leg(record['G5'][:,i]))) for i in range(3)]
for i in range(3):
 lhs=sc(kAt*cm/kap,record['action'](Ccols[i],am,bm))
 rhs=sc(kAt*cm,adds(sc(quadratic/kap,N[i]),rem[i]))
 eqvec(lhs,rhs)
 for a in range(2):
  aa=adds(sc(am,A(s.eye(2)[:,a])),sc(bm,B(s.eye(2)[:,a])))
  assert not pair(N[i],aa)
  assert not pair(rem[i],aa)
print('PASS: exact complete C residual with all am,bm,cm,kAt factors and all234 coefficients; canonical N and D3+kappa*G5 both annihilate the entire U arrow.',flush=True)
for i in range(3):
 for j in range(3):
  delta=s.expand(scalar_pairing(rem[i],Ccols[j])-scalar_pairing(rem[j],Ccols[i]))
  expected=quadratic*record['C_C_anomaly_factor'][i,j]
  assert s.expand(delta-expected)==0,(i,j,delta-expected)
  n_delta=s.expand(scalar_pairing(N[i],Ccols[j])-scalar_pairing(N[j],Ccols[i]))
  assert s.expand(n_delta+kap*record['C_C_anomaly_factor'][i,j])==0
print('PASS: C,C skew defect of D3+kappa*G5 is q*(ZN_C-ZN_C^t), canceled exactly by q/kappa*N; no separate cochain closure is asserted.',flush=True)
print('The source/division interface is available; source extension errors are returned, not solved. No actual coefficients, points, ranks, frozen edits or external writes.',flush=True)
