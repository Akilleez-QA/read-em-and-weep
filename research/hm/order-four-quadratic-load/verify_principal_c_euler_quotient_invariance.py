"""Universal necessity of the C-only principal quotient under general Euler completion."""
from universal_source_balance_helpers import *
ks=s.Matrix(6,6,s.symbols('free_K0:36')); qs=s.symbols('free_q0:5')
q4=sum(qs[i]*u**(4-i)*w**i for i in range(5));K=q4*ks
zero_matrix(getp(fullT(K,4,Cx))-K*getp(Cx))
print('PASS: arbitrary negative-quartic six-space Euler symbols have c-VV exactly K C_VV, in low bidegree(0,5).',flush=True)
r0,r1=s.symbols('r0 r1');rr=s.Matrix([r0,r1]);lam=s.Matrix([[-r1,r0]])
Mv=M.subs({x:r0*r0,y:-r1*r1,z:-r0*r1},simultaneous=True)
assert Mv==rr*lam
bs=s.symbols('beta0:4');beta=sum(bs[i]*r0**(3-i)*r1**i for i in range(4))
spinY=rr*beta
recovered=s.expand((s.diff(spinY[0],r0)+s.diff(spinY[1],r1))/5)
assert recovered==beta
uu=s.Matrix([-s.diff(beta,r1),s.diff(beta,r0)])/3
zero_matrix(Mv*uu-spinY)
print('PASS: full binary-cubic spin source has canonical regular quadratic lift, without choosing a point.',flush=True)
l0,l1=s.symbols('ambiguity0:2');amb=l0*r0+l1*r1
zero_matrix(Mv*(rr*amb))
# Complete source ambiguity: every quadratic vector in ker M is r times a linear form.
cs=s.symbols('kernel0:6');z=s.Matrix([sum(cs[3*j+i]*r0**(2-i)*r1**i for i in range(3)) for j in range(2)])
eqs=s.Poly(s.expand((lam*z)[0]),r0,r1).coeffs()
sol=s.solve(eqs,cs,dict=True)[0]
zk=z.subs(sol,simultaneous=True)
q=(s.diff(zk[0],r0)+s.diff(zk[1],r1))/3
zero_matrix(zk-rr*q)
# An arbitrary actual Cartan row changes by F times that same scalar.
ar=s.Matrix(1,2,s.symbols('cartan_row0:2'));F=(ar*rr)[0]
assert s.expand((ar*(uu+rr*amb))[0]-(ar*uu)[0]-F*amb)==0
print('PASS: all quadratic source choices differ by r times a linear form, so the Cartan quotient changes only by a multiple of F.',flush=True)
print('No U screen, source-only normalization constraint, actual coefficient, or curve division has been used.')
