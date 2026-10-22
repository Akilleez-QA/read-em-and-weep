"""Full exterior identity with every six-space coefficient and polar symbol free."""
from universal_source_balance_helpers import *
K=s.Matrix(6,6,s.symbols('identity_K0:36'))
rv=s.symbols('polar0:3');rf={(i,):rv[i] for i in range(3)}
ps=s.Matrix(s.symbols('source0:2'))
def FI(K,F):
 out=[{},{}]
 for i in [3,4]:out=adds(out,putp(K*getp(F,(i,)),(i,)))
 return out

def starI(K,F):
 out=[{},{}]
 for i in [3,4]:out=adds(out,putY(up*adj6(K)*low*getY(F,(i,)),(i,)))
 return out

def LI(K,rf,F):
 v=adds(FI(K,[wedge(rf,f) for f in F]),sc(-1,[wedge(rf,f) for f in starI(K,F)]))
 return [contract(coords,f) for f in v]
cs2=s.symbols('form2_0:20');cs3=s.symbols('form3_0:20')
Z2=[dict(zip(combinations(range(5),2),cs2[10*j:10*j+10])) for j in range(2)]
Z3=[dict(zip(combinations(range(5),3),cs3[10*j:10*j+10])) for j in range(2)]
eq(pair(FI(K,Z3),Z2),pair(Z3,starI(K,Z2)))
print('PASS: full determinant adjoint has the identity-W plus sign.',flush=True)
YL=s.Matrix.vstack(M0,M1,M2)
E=s.Matrix.hstack(*[getp([wedge(rf,{(i,):s.eye(6)[2*i+j,c] for i in range(3)}) for j in range(2)]) for c in range(6)])
Y=(E*up*adj6(K)*low*YL-K*E*YL)*ps
jp=contract(coords,omega)
right=[contract(coords,wedge(f,jp)) for f in putp(Y)]
actual=LI(K,rf,B(ps))
eqvec(actual,right)
zero_matrix(getp(actual))
assert all(f.get((3,4),0)==0 for f in actual)
eqvec(LI(K,rf,A(ps)),[{},{}])
print('PASS: full U VV and WW coefficients vanish, while all36-symbol mixed coefficients match the exact Y formula.')
print('PASS: A input is annihilated. No mixed-U, c-companion or fourth-value vanishing is claimed.')
# Complete operator formula, not merely its two source restrictions.
R=K*E-E*up*adj6(K)*low
raw=[{},{}]
for i in (3,4):raw=adds(raw,putp(R*getY(Z2,(i,)),(i,)))
all_output=[contract(coords,f) for f in raw]
eqvec(LI(K,rf,Z2),all_output)
zero_matrix(getp(all_output)-R*(u*getY(Z2,(3,))+w*getY(Z2,(4,))))
closed=[contract(coords,f) for f in Z3]
vv=putp(getp(closed)); vp=[x,y,z,0,0]
ivvv=s.Matrix([contract(vp,f).get((i,),0) for i in range(3) for f in vv])
zero_matrix(u*getY(closed,(3,))+w*getY(closed,(4,))-ivvv)
zero_matrix(getp(LI(K,rf,closed))-R*ivvv)
print('PASS: the complete20-input operator factors through the mixed sector, and its principal action on every closed input is R i_v(F_VV).')
