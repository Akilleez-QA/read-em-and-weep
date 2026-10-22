"""Universal tensor identities only. No instance data, sampling or matrix ranks."""
import sympy as s
r=s.Matrix(s.symbols('r0:3')); a,b,c,d,e=s.symbols('a b c d e')
H=s.Matrix([[a,b,c],[b,d,e],[c,e,-a-d]])
K=s.Matrix(3,3,s.symbols('k0:9'))
B=lambda v:s.Matrix(3,3,lambda i,j:sum(s.LeviCivita(i,j,k)*v[k] for k in range(3)))
def zero(M): assert all(s.expand(v)==0 for v in M)
L=lambda Z:s.trace(Z)*s.eye(3)-Z.T
Li=lambda Z:s.trace(Z)*s.eye(3)/2-Z.T
zero(Li(L(K))-K); zero(L(Li(K))-K)
zero(K*B(r)+B(r)*K.T-B(L(K)*r))
Q=-Li(L(K)*H)
zero(Q*B(r)+B(r)*Q.T+K*B(H*r)+B(H*r)*K.T)
zero((-H)*B(r)+B(r)*(-H).T-B(H*r))
print('PASS: scalar-U/traceless-W kernel has explicit arbitrary-K inverse, dimension9.')
def minus(Q): return Q*B(r)-B(r)*Q.T
def rec(X):return s.Matrix(3,3,lambda i,l:sum(s.diff(X[i,j],r[k])*s.LeviCivita(l,j,k) for j in range(3) for k in range(3))/3)
zero(rec(minus(K))-K+s.trace(K)*s.eye(3)/3)
X=-(K*B(H*r)-B(H*r)*K.T); residual=(minus(rec(X))-X).applyfunc(s.expand)
rows=[(0,0,0,c,-2*K[0,1]),(0,0,0,b,2*K[0,2]),(0,1,1,c,s.Rational(2,3)*K[1,0]),(0,0,1,b,s.Rational(2,3)*K[1,2]),(0,2,2,b,-s.Rational(2,3)*K[2,0]),(0,0,2,c,-s.Rational(2,3)*K[2,1]),(0,0,2,b,-s.Rational(2,3)*(K[0,0]-K[2,2])),(1,1,2,b,s.Rational(2,3)*(K[1,1]-K[2,2]))]
for i,j,k,h,v in rows:assert s.expand(s.diff(residual[i,j],r[k],h)-v)==0
lam=s.symbols('lam');zero(minus(lam*s.eye(3)))
zero(lam*s.eye(3)*B(H*r)-B(H*r)*lam*s.eye(3))
print('PASS: each traceless-U/traceless-W kernel is Q=lambda(H)I, K=sI, dimension6.')
# New explicit inverse for positive contraction on parity-constrained linear matrices.
for parity in (1,-1):
    C={}; n=0
    for k in range(3):
        for i in range(3):
            for j in range(i,3):
                v=s.Symbol('c%d'%n) if i!=j or parity==1 else s.Integer(0);n+=1
                C[i,j,k]=v;C[j,i,k]=parity*v if i!=j else v
    A=s.Matrix(3,3,lambda i,j:sum(C[i,j,k]*r[k] for k in range(3)))
    F=B(r)*A
    D={(i,j,k):s.expand(sum(s.LeviCivita(t,i,l)*s.diff(F[t,j],r[l],r[k]) for t in range(3) for l in range(3))) for i in range(3) for j in range(3) for k in range(3)}
    trace=[sum(D[j,i,i] for i in range(3))/(3*parity-1) for j in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):assert s.expand((D[i,j,k]+(trace[j] if i==k else 0))/3-C[i,j,k])==0
print('PASS: explicit left inverse for final positive contraction, for every free symmetric/skew linear matrix.')
phi=(1+s.sqrt(5))/2;sz=[1,15,20,12,12]
one=s.Matrix([1,1,1,1,1]);A=s.Matrix([3,-1,0,phi,1-phi]);V=s.Matrix([3,-1,0,1-phi,phi]);P=s.Matrix([4,0,1,-1,-1]);D=s.Matrix([5,1,-1,0,0])
mul=lambda x,y:s.matrix_multiply_elementwise(x,y)
inner=lambda x,y:s.simplify(sum(sz[i]*x[i]*y[i] for i in range(5))/60)
end=2*one+A+4*V+P+3*D;N=2*A+V+P+D
kplus=one+V+D+mul(D+one,V)
zero(kplus-(one+A+3*V+P+2*D))
ker=mul(kplus,A);zero(ker-(one+4*A+3*V+6*P+7*D))
raw=mul(mul(D+one,end),A)
assert raw[0]==648 and ker[0]==81 and inner(N,raw)==195 and inner(N,ker)==24
oldker=D+one+mul(one+V+D,V);oldraw=mul(D+one,end)
assert inner(N,oldraw+raw)==259 and inner(N,oldker+ker)==33
assert inner(N,raw-ker)==171 and inner(N,oldraw+raw-oldker-ker)==226
print('PASS: traceless648->567 kernel81; marked195->171 kernel24; joint259->226 kernel33.')
print('No source coefficient assignments, source solve, numerical scans or matrix ranks used.')
