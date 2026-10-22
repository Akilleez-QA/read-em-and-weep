"""Universal presentation kernel; no monad coefficients or instance ranks."""
import sympy as s
r=s.Matrix(s.symbols('r0:3')); a,b,c,d,e=s.symbols('a b c d e')
H=s.Matrix([[a,b,c],[b,d,e],[c,e,-a-d]])
K=s.Matrix(3,3,s.symbols('k0:9'))
def B(v):return s.Matrix(3,3,lambda i,j:sum(s.LeviCivita(i,j,k)*v[k] for k in range(3)))
def zero(M):assert all(s.expand(x)==0 for x in M)
def plus(Q):return Q*B(r)-B(r)*Q.T

def recover(R):
 return s.Matrix(3,3,lambda i,l:s.expand(sum(s.diff(R[i,j],r[k])*s.LeviCivita(l,j,k) for j in range(3) for k in range(3))/3))
# This is the exact inverse modulo the scalar line, not a rank test.
zero(recover(plus(K))-K+s.trace(K)*s.eye(3)/3)
R=-(K*B(H*r)-B(H*r)*K.T)
Q=recover(R);res=(plus(Q)-R).applyfunc(s.expand)
rows=[(0,0,0,c,-2*K[0,1]),(0,0,0,b,2*K[0,2]),
 (0,1,1,c,s.Rational(2,3)*K[1,0]),(0,0,1,b,s.Rational(2,3)*K[1,2]),
 (0,2,2,b,-s.Rational(2,3)*K[2,0]),(0,0,2,c,-s.Rational(2,3)*K[2,1]),
 (0,0,2,b,-s.Rational(2,3)*(K[0,0]-K[2,2])),
 (1,1,2,b,s.Rational(2,3)*(K[1,1]-K[2,2]))]
for i,j,k,h,expected in rows:assert s.expand(s.diff(res[i,j],r[k],h)-expected)==0
lam=s.symbols('lambda');zero(plus(lam*s.eye(3)))
zero((lam*s.eye(3))*B(H*r)-B(H*r)*(lam*s.eye(3)))
print('PASS: scalar-U kernel consists exactly of five scalar Q(H) coefficients and one scalar K coefficient.')
L=lambda Z:s.trace(Z)*s.eye(3)-Z.T
Li=lambda Z:s.trace(Z)*s.eye(3)/2-Z.T
zero(Li(L(K))-K);zero(L(Li(K))-K)
zero(K*B(r)+B(r)*K.T-B(L(K)*r))
Qm=Li(-L(K)*H)
zero(Qm*B(r)+B(r)*Qm.T+K*B(H*r)+B(H*r)*K.T)
print('PASS: each traceless-U component has exactly nine kernel parameters, with explicit Q=-L_inverse(L(K)H).')
# Character arithmetic, independently retaining the two three-dimensional irreducibles.
phi=(1+s.sqrt(5))/2;sz=[1,15,20,12,12]
one=s.Matrix([1,1,1,1,1]);A=s.Matrix([3,-1,0,phi,1-phi]);V=s.Matrix([3,-1,0,1-phi,phi]);P=s.Matrix([4,0,1,-1,-1]);D=s.Matrix([5,1,-1,0,0])
mul=lambda x,y:s.matrix_multiply_elementwise(x,y)
inner=lambda x,y:s.simplify(sum(sz[i]*x[i]*y[i] for i in range(5))/60)
end=2*one+A+4*V+P+3*D
raw=mul(D+one,end)
ker=D+one+mul(one+V+D,V)
expected=2*one+A+3*V+P+3*D
zero(ker-expected)
N=2*A+V+P+D
assert raw[0]==216 and ker[0]==33 and (raw-ker)[0]==183
assert inner(N,raw)==64 and inner(N,ker)==9 and inner(N,raw-ker)==55
print('PASS: universal216->183 has kernel33; the complete marked coefficient family64->55 has exactly nine presentation relations.')
print('No actual source values, actual-instance matrix/rank evaluation, source completion or fourth-value claim.')
