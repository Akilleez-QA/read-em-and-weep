"""Universal full-source factorization, not only lower C-source quotienting."""
from universal_q_middle_completion_transport import *
c=graded_module()['C']*s.Matrix(s.symbols('q_source_factor_c0:3'))
g=s.Matrix(s.symbols('q_source_factor_g0:12'))
ell=sum(a*v for a,v in zip(s.symbols('q_source_factor_ell0:3'),positive))
cf=mixed(c[:6,:],c[6:,:])
for a in range(2):
 assert not pair(cf,B(s.eye(2)[:,a]))
assert homogeneous_partner(ell*c,1)['Z']==s.zeros(6,1)
assert homogeneous_partner(quadratic*c,2)['Z']==s.zeros(6,1)
print('PASS: constant C-source pairing with Bsource is identically zero; all positive-polynomial C-source Euler partners therefore vanish.',flush=True)
# Prove the pair-factor identity from complete legs, with every c,g,ell free.
kap=s.symbols('q_source_factor_kappa')
a=homogeneous_partner(ell*g,1);b=homogeneous_partner(quadratic*g,2)
la=adds(a['Y'],sc(-kap,vww_leg(a['Z'])))
lb=adds(b['Y'],sc(-kap,vww_leg(b['Z'])))
H=sc(s.Rational(1,2),adds(sc(ell,lb),sc(quadratic,la)))
# B=ell*sym(c,g); linearity of the exported constructor gives
# 1/2*sym(ell*c,L2(qg))+1/2*sym(L1(ell*g),q*c)=sym(c,H).
# No arbitrary nonclosed eta is scalar-paired: tensor coefficient identity is
# checked in every exterior-component pair before using its closed action.
for a in range(2):
 for ia in set(cf[a])|set(la[a])|set(lb[a])|set(H[a]):
  for bidx in range(2):
   for ib in set(cf[bidx])|set(la[bidx])|set(lb[bidx])|set(H[bidx]):
    lhs=(ell*cf[a].get(ia,0)*lb[bidx].get(ib,0)+ell*lb[a].get(ia,0)*cf[bidx].get(ib,0)+quadratic*la[a].get(ia,0)*cf[bidx].get(ib,0)+quadratic*cf[a].get(ia,0)*la[bidx].get(ib,0))/4
    rhs=(cf[a].get(ia,0)*H[bidx].get(ib,0)+H[a].get(ia,0)*cf[bidx].get(ib,0))/2
    assert s.expand(lhs-rhs)==0
print('PASS: every C-source factor in qB stays a literal full-source factor in the ENTIRE chosen completion, including both higher weights; no lower-only quotient is used.',flush=True)
print('The complete qB family may therefore descend from12 to the nine-dimensional mixed quotient by constant C sources, modulo the actual full-source homotopy with its endpoints.',flush=True)
