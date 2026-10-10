"""Exact rank-seven Segre tangent and automorphism-orbit certificate (QQ)."""
import sympy as s
from itertools import product
from collections import defaultdict
from pathlib import Path
bits=list(product(range(2),repeat=4)); z=s.symbols('z0:16')
A=z[0];E=z[15];B=sum(z[i] for i,b in enumerate(bits) if sum(b)==1);D=sum(z[i] for i,b in enumerate(bits) if sum(b)==3)
U=z[3]+z[12];V=z[5]+z[10];W=z[6]+z[9]
q=4*A*E-B*D+U*V+U*W+V*W
Q=s.hessian(q,z)
K=s.Matrix.hstack(*Q.nullspace())
# Every Segre monomial restriction is indexed by a vector in {0,1,2}^4.
# In each fiber, differences against one reference monomial give an exact I_2 basis.
fibers=defaultdict(list)
for i in range(16):
 for j in range(i,16):
  fibers[tuple(bits[i][k]+bits[j][k] for k in range(4))].append((i,j))
basis=[]
for pairs in fibers.values():
 i,j=pairs[0]
 for k,l in pairs[1:]: basis.append(z[k]*z[l]-z[i]*z[j])
assert len(fibers)==81 and len(basis)==55
Hs=[s.hessian(f,z) for f in basis]
upper=lambda M:s.Matrix([M[i,j] for i in range(M.rows) for j in range(i,M.cols)])
T=s.Matrix.hstack(*(upper(K.T*H*K) for H in Hs))
print('I2 dimension:',len(basis));print('Q rank:',Q.rank());print('K:',K)
print('Tangent restriction matrix shape:',T.shape)
print('Tangent restriction rank:',T.rank());print('Affine tangent dimension:',55-T.rank());print('Projective tangent dimension:',54-T.rank())
# An explicit nonzero maximal minor makes the calculation independently reproducible.
_,pc=T.rref(); _,pr=T[:,list(pc)].T.rref()
print('Restriction pivot columns:',pc);print('Restriction pivot rows:',pr)
print('Restriction full-rank minor determinant:',T.extract(pr,pc).det())
# The natural infinitesimal sl_2 action in each tensor factor, using column vectors.
gens=[]; names=[]
for a in range(4):
 for name,g in [('E',s.Matrix([[0,1],[0,0]])),('F',s.Matrix([[0,0],[1,0]])),('H',s.diag(1,-1))]:
  R=s.zeros(16)
  for j,b in enumerate(bits):
   for k in range(2):
    c=list(b);c[a]=k
    R[bits.index(tuple(c)),j]=g[k,b[a]]
  gens.append(R);names.append(str(a+1)+name)
O=s.Matrix.hstack(*(upper(R.T*Q+Q*R) for R in gens))
Oplus=O.row_join(upper(Q))
print('Orbit affine tangent rank (sl2^4):',O.rank())
print('Orbit tangent plus scalar rank:',Oplus.rank())
print('Infinitesimal stabilizer basis in order',names,':',O.nullspace())
print('Projective stabilizer equations basis (last entry scalar):',Oplus.nullspace())
assert T.rank()==45
assert O.rank()==9 and Oplus.rank()==10
assert all(sum((gens[3*a+i] for a in range(4)),s.zeros(16)).T*Q + Q*sum((gens[3*a+i] for a in range(4)),s.zeros(16))==s.zeros(16) for i in range(3))
print('All exact assertions passed.')
