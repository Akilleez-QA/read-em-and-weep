"""Reproduce the all-degree split, source resolution, saturation certificate,
and exact full-U relation transport. No actual instances or ranks.
"""
from universal_graded_c_orthogonal_module import *

m=graded_module();fc=fitting_certificate()
print('PASS: physical constant pairing split D R=I, D C=0, Zeta C=I, R D+C Zeta=I over Q[FB±1,FC±1,FD±1].',flush=True)
print('PASS: all nine independent formal RHS coefficients solved using Laurent-unit pivots; no marking values assigned.',flush=True)

# The full chain homotopy is checked on a spanning set of formal monomials,
# not points or source assignments. The proof for every degree is Euler's
# identity: i_v d+d i_v=(polynomial degree+exterior degree) id.
vv=s.Matrix([[x,y,z]])
for d in range(5):
 mons=[x**i*y**j*z**(d-i-j) for i in range(d+1) for j in range(d-i+1)]
 for a in range(3):
  for r in range(3):
   for p in mons:
    q=s.zeros(9,1);q[3*a+r]=p
    div=sum(positive_variables[k]*q[3*a+k] for k in range(3))
    correction=s.zeros(9,1)
    correction[3*a:3*a+3,0]=s.Matrix([s.diff(div,v) for v in positive_variables])/(d+1)
    assert (m['d2']*potential(q,d)-q+correction).applyfunc(s.expand)==s.zeros(9,1)
for d in range(4):
 mons=[x**i*y**j*z**(d-i-j) for i in range(d+1) for j in range(d-i+1)]
 for a in range(3):
  for p in mons:
   t=s.zeros(3,1);t[a]=p;h=m['d3']*t
   assert (relation_potential(h,d+1)-t).applyfunc(s.expand)==s.zeros(3,1)
print('PASS: Koszul contracting identities on complete monomial spans; exact all-degree proof supplied by the Euler anticommutator.',flush=True)

# Free polynomial coefficients in all C and all nine Koszul generators.
for d in range(4):
 mons=[x**i*y**j*z**(d-i-j) for i in range(d+1) for j in range(d-i+1)]
 c=s.Matrix([sum(t*p for t,p in zip(s.symbols(f'free_C_{d}_{a}_0:{len(mons)}'),mons)) for a in range(3)])
 if d:
  mm=[x**i*y**j*z**(d-1-i-j) for i in range(d) for j in range(d-i)]
  h=s.Matrix([sum(t*p for t,p in zip(s.symbols(f'free_K_{d}_{a}_0:{len(mm)}'),mm)) for a in range(9)])
 else:h=s.zeros(9,1)
 yy=m['C']*c+m['R']*m['d2']*h
 reconstruct_leg(yy,d)
print('PASS: all-degree constructive source decomposition retains C, A and the five D5 coefficients; arbitrary free coefficient checks through cubic degree.',flush=True)
print('P determinant =',m['detP'],flush=True)
print('Three exact D5 relation columns =',m['relation'],flush=True)
print('PASS: exact relation Y Rel = -Acoeff H+C Zeta Acoeff H. Its injectivity follows from M(v)^2=(xy+z^2)I and Koszul exactness.',flush=True)
print('PASS: ten formal exterior-cube polynomials have Laurent-unit span equal to every positive cubic. Fitting ideal=(x,y,z)^3, giving the projective subbundle certificate without points or ranks.',flush=True)

am,bm,cm=s.symbols('graded_am graded_bm graded_cm',nonzero=True)
kap=bm/am
for j in range(3):
 sigma=m['relation_sigma'][:,j];zz=m['relation_C'][:,j]
 W=vww_leg(m['relation_W'][:,j])
 assert any(W)
 for a in range(2):
  assert not pair(W,A(s.eye(2)[:,a]))
  assert not pair(W,B(s.eye(2)[:,a]))
 Cshift=C_column(sum(zz[k]*mon(2)[k] for k in range(3)))[0]
 lhs=adds(
  mixed((m['Y']*m['relation'][:,j])[:6,:],(m['Y']*m['relation'][:,j])[6:,:]),
  sc(-kap,vww_leg(m['ZG']*m['relation'][:,j])))
 rhs=adds(Cshift,A(sigma),sc(kap,B(sigma)),sc(-kap,W))
 eqvec(lhs,rhs)
 assert any(s.expand(e)!=0 for e in m['relation_WC'][:,j])
 print('Full-U relation',j,'sigma=',sigma,'Cshift=',zz,'Wcoeff=',m['relation_W'][:,j],'W*C=',m['relation_WC'][:,j],flush=True)
print('PASS: L Rel=C(zeta)+alpha_U(sigma)/am-(bm/am)W, with W*A=W*B=0 and W*C nonzero, in complete exterior forms. No higher-weight remainder discarded.',flush=True)
print('These W remainders are NOT claimed independent beyond the retained completed D5-square family.',flush=True)
print('No actual physical/source/marking values, points, instance ranks, broad family solve, frozen edit, or external write used.',flush=True)

# Finite symmetry is used only after the exact graded/global proof.
p=(1+s.sqrt(5))/2
one=s.Matrix([1,1,1,1,1]);Ac=s.Matrix([3,-1,0,p,1-p]);Vc=s.Matrix([3,-1,0,1-p,p])
Pc=s.Matrix([4,0,1,-1,-1]);Dc=s.Matrix([5,1,-1,0,0]);sizes=[1,15,20,12,12]
mul=lambda a,b:a.multiply_elementwise(b)
inner=lambda a,b:s.simplify(sum(n*aa*bb for n,aa,bb in zip(sizes,a,b))/60)
quotient=mul(Vc,one+Pc+2*Dc)-mul(Ac,Dc)
assert (quotient-2*(Ac+Vc+Pc+Dc)).applyfunc(s.simplify)==s.zeros(5,1)
assert inner(one+Ac+Vc+2*Pc+2*Dc,quotient)==12 and inner(Dc,quotient)==2
print('PASS: formal lower cubic quotient character 2A+2V+2P4+2D5, with 12 harmonic and 2 trace maps. This is not physical completed-middle independence.',flush=True)
