"""Exact rational linear-algebra tests; all matrices are invented below."""
import sympy as s

class Complex:
    def __init__(self, dims, differential=None):
        self.dims = dims
        self.diff = differential or {}
    def dim(self, n): return self.dims.get(n, 0)
    def d(self, n): return self.diff.get(n, s.zeros(self.dim(n+1), self.dim(n)))

class Hom:
    def __init__(self, A, B, k):
        self.A,self.B,self.k=A,B,k
        self.slots=[(n,i,j) for n in sorted(A.dims) for i in range(B.dim(n+k)) for j in range(A.dim(n))]
        self.size=len(self.slots)
    def unpack(self, v):
        out={n:s.zeros(self.B.dim(n+self.k),self.A.dim(n)) for n in self.A.dims}
        for z,(n,i,j) in zip(v,self.slots): out[n][i,j]=z
        return out
    def pack(self, f): return s.Matrix([f[n][i,j] for n,i,j in self.slots]).reshape(self.size,1)
    def get(self,f,n): return f.get(n,s.zeros(self.B.dim(n+self.k),self.A.dim(n)))
    def differential(self):
        nxt=Hom(self.A,self.B,self.k+1)
        def op(f):
            return {n:self.B.d(n+self.k)*self.get(f,n)-(-1 if self.k%2 else 1)*self.get(f,n+1)*self.A.d(n) for n in self.A.dims}
        return linear(self,nxt,op)

def linear(source,target,op):
    cols=[target.pack(op(source.unpack(s.eye(source.size)[:,i]))) for i in range(source.size)]
    return s.Matrix.hstack(*cols) if cols else s.zeros(target.size,0)

def basis_kernel(M):
    cols=M.nullspace()
    return s.Matrix.hstack(*cols) if cols else s.zeros(M.cols,0)

def attainable(M,b): return M.rank()==M.row_join(b).rank()

def setup(A,B,C,Pi,T):
    for E in (A,B,C):
        for n in E.dims:
            assert E.d(n+1)*E.d(n)==s.zeros(E.dim(n+2),E.dim(n))
    for n in B.dims:
        pi=Pi.get(n,s.zeros(C.dim(n),B.dim(n)))
        pinext=Pi.get(n+1,s.zeros(C.dim(n+1),B.dim(n+1)))
        assert C.d(n)*pi==pinext*B.d(n)
    for n in A.dims:
        t=T.get(n,s.zeros(B.dim(n+2),A.dim(n)))
        tnext=T.get(n+1,s.zeros(B.dim(n+3),A.dim(n+1)))
        assert B.d(n+2)*t==tnext*A.d(n)
    X1,X2,Y1,Y2,H=Hom(A,B,1),Hom(A,B,2),Hom(A,C,1),Hom(A,C,2),Hom(B,C,-1)
    def post(X,Y):
        return linear(X,Y,lambda f:{n:Pi.get(n+X.k,s.zeros(C.dim(n+X.k),B.dim(n+X.k)))*X.get(f,n) for n in A.dims})
    P1,P2=post(X1,Y1),post(X2,Y2)
    R=linear(H,Y1,lambda u:{n:H.get(u,n+2)*T.get(n,s.zeros(B.dim(n+2),A.dim(n))) for n in A.dims})
    closedU=basis_kernel(H.differential())
    actual=(R*closedU).row_join(-P1)
    return X1,X2,Y1,Y2,H,P1,P2,R,closedU,actual

# Example 1: a projected nonzero F is closed but not exact.
A=Complex({0:1}); B=Complex({2:1}); C=Complex({1:1,2:1},{1:s.Matrix([[1]])})
X1,X2,Y1,Y2,H,P1,P2,R,ZU,L=setup(A,B,C,{2:s.eye(1)},{0:s.eye(1)})
j=Y1.pack({0:s.eye(1)}); f=X2.pack({0:-s.eye(1)})
assert Y1.differential()*j+P2*f==s.zeros(Y2.size,1)
assert not attainable(L,j)
assert not attainable(X1.differential(),f)
print('Example 1: projected yes; actual no; prescribed F not exact.')

# Example 2: F=0 exact and J exact in Y itself, yet no actual U,V.
A=Complex({0:1,1:1},{0:s.eye(1)}); B=Complex({2:1})
C=Complex({1:1,2:2},{1:s.Matrix([[0],[1]])})
Pi={2:s.Matrix([[1],[0]])}; T={0:s.eye(1),1:s.zeros(0,1)}
X1,X2,Y1,Y2,H,P1,P2,R,ZU,L=setup(A,B,C,Pi,T)
j=Y1.pack({0:s.Matrix([[1]]),1:s.Matrix([[0],[-1]])})
f=s.zeros(X2.size,1)
assert Y1.differential()*j==s.zeros(Y2.size,1)
Y0=Hom(A,C,0)
h=Y0.pack({0:s.zeros(0,1),1:s.Matrix([[1]])})
assert j==-Y0.differential()*h
assert attainable(X1.differential(),f)
assert not attainable(L,j)
assert ZU.cols==0
print('Example 2: F=0; J Hom-exact; projected yes; actual no.')

# Example 3: defect removal is possible but requires nonzero compensation.
A=Complex({0:1,1:1},{0:s.eye(1)}); B=Complex({2:1}); C=Complex({2:1})
X1,X2,Y1,Y2,H,P1,P2,R,ZU,L=setup(A,B,C,{2:s.eye(1)},{0:s.eye(1)})
k=Y1.pack({0:s.zeros(0,1),1:s.eye(1)})
v=X1.pack({0:s.zeros(0,1),1:s.eye(1)})
j=-P1*v; f=X1.differential()*v
assert k+j==s.zeros(Y1.size,1)
assert f==s.Matrix([[1]])
assert Y1.differential()*j+P2*f==s.zeros(Y2.size,1)
# r maps a degree-one map to its composition with Delta.
r=linear(Y1,Y2,lambda g:{n:Y1.get(g,n+1)*A.d(n) for n in A.dims})
assert attainable(r*L,-r*k)
L_fixed=(R*ZU).row_join(-P1*basis_kernel(X1.differential()))
assert not attainable(r*L_fixed,-r*k)
assert r*k==P2*f
print('Example 3: kill K on im Delta with compensation; impossible with E fixed.')
print('All exact-rational synthetic checks passed. No external data read.')
