"""Free-symbol full-U and product-rule checks with all derivatives retained."""
from universal_q_middle_completion_transport import *

# Arbitrary positive-linear mixed leg and arbitrary positive quadratic scalar.
yy=s.Matrix([sum(c*v for c,v in zip(s.symbols(f'free_linear_leg_{i}_0:3'),positive)) for i in range(12)])
mons=(x*x,x*y,x*z,y*y,y*z,z*z)
p=sum(c*v for c,v in zip(s.symbols('free_multiplier0:6'),mons))
base=homogeneous_partner(yy,1)
product=homogeneous_partner(p*yy,3)
term=coefficient_gradient_partner(p,base['rB'])
assert (product['Z']-p*base['Z']-(term-2*p*base['Z'])/3).applyfunc(s.expand)==s.zeros(6,1)
print('PASS: all36 linear-leg and6 multiplier coefficients free: Z3(pY)-pZ1(Y)=(J grad(p) rY-2pZ1(Y))/3.',flush=True)

# q times an entirely free constant mixed leg has a nonzero linear partner
# containing grad(q), not a factor q. No actual constant is selected.
g=s.Matrix(s.symbols('free_constant_mixed_leg0:12'))
qleg=homogeneous_partner(quadratic*g,2)
raw=mixed(g[:6,:],g[6:,:])
r0=s.Matrix([[scalar_pairing(raw,B(s.eye(2)[:,j])) for j in range(2)]])
assert (qleg['Z']-coefficient_gradient_partner(quadratic,r0)/2).applyfunc(s.expand)==s.zeros(6,1)
assert any(s.expand(e)!=0 for e in qleg['Z'])
check_degree(qleg['Z'],1)
print('PASS: Z2(qg)=p(J grad(q) r_g/2) is a nonzero positive-linear partner; it is not q-divisible.',flush=True)

# The derivative of a free linear coefficient cannot be suppressed.
ell=sum(c*v for c,v in zip(s.symbols('free_linear_scalar0:3'),positive))
linear=homogeneous_partner(ell*g,1)
assert (linear['Z']-coefficient_gradient_partner(ell,r0)).applyfunc(s.expand)==s.zeros(6,1)
print('PASS: Z1(ell g)=p(J grad(ell) r_g), retaining the scalar/K derivative term.',flush=True)

# Each paired transvection is full-U balanced independently. Therefore the
# symmetric sum in q_linear_middle_completion has exactly lower qB and
# keeps both grad(q) and every derivative of B in its higher companions.
am,bm=s.symbols('transport_am transport_bm',nonzero=True)
ly=adds(base['Y'],sc(-bm/am,vww_leg(base['Z'])))
lq=adds(qleg['Y'],sc(-bm/am,vww_leg(qleg['Z'])))
for a in range(2):
 alpha=adds(sc(am,A(s.eye(2)[:,a])),sc(bm,B(s.eye(2)[:,a])))
 assert not pair(ly,alpha) and not pair(lq,alpha)
print('PASS: arbitrary degree-one and q-times-constant degree-two legs balance the entire U arrow with independent am,bm.',flush=True)
print('The qB completion retains grad(q), coefficient derivatives, T2/T4 and their C residuals. It is not identified with another completion or a pure q-cochain.',flush=True)
print('No actual coefficient/point/marking assignments, rank calls, broad source solves, frozen changes or external writes.',flush=True)

# Exercise the exported qB constructor on the entire symmetric-linear space,
# with all234 independent formal coefficients, not a chosen instance.
BB=s.zeros(12)
for i in range(12):
 for j in range(i,12):
  BB[i,j]=BB[j,i]=sum(c*v for c,v in zip(s.symbols(f'free_qmiddle_B_{i}_{j}_0:3'),positive))
completed=q_linear_middle_completion(BB)
for a in range(2):
 alpha=adds(sc(am,A(s.eye(2)[:,a])),sc(bm,B(s.eye(2)[:,a])))
 eqvec(completed['action'](alpha,am,bm),[{},{}])
print('PASS: exported qB completion balances both entire U columns with all234 symmetric-linear middle coefficients free.',flush=True)
