"""Tiny invented rational sl2 controls. No physical source/data/runtime imports."""
from fractions import Fraction as Q
import unittest

Z=(Q(0),)*4
I=(Q(1),Q(0),Q(0),Q(1))
h=(Q(1),Q(0),Q(0),Q(-1));e=(Q(0),Q(1),Q(0),Q(0));f=(Q(0),Q(0),Q(1),Q(0))
p=(0,1);q=(2,3)
SIGNED=((0,2,1,3,1),(0,3,1,2,-1),(1,2,0,3,-1),(1,3,0,2,1))
def add(*xs):return tuple(sum(x[i] for x in xs) for i in range(4)) if xs else Z
def sc(c,x):return tuple(c*z for z in x)
def mul(a,b):return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def tr(a):return a[0]+a[3]
def dot(a,b):return tr(mul(a,b))
def tf(a):return add(a,sc(-tr(a)/2,I))
def br(a,b):return add(mul(a,b),sc(-1,mul(b,a)))
def K(X,r):return sc(Q(1,4),br(X[r[0]],X[r[1]]))
def covDK(X,Y,a,r):
 c,d=r
 return sc(Q(1,4),add(br(add(Y[a,c],sc(-1,mul(X[a],X[c]))),X[d]),br(X[c],add(Y[a,d],sc(-1,mul(X[a],X[d]))))))
def N(X,Y,a,r):
 c,d=r
 return sc(Q(1,4),add(br(Y[a,c],X[d]),br(X[c],Y[a,d])))
def T(L,U,H,J,r,s):
 a,b=r
 Ub=[add(mul(U[x],K(U,s)),covDK(U,J,x,s)) for x in (a,b)]
 Lb=[add(mul(L[x],K(L,s)),covDK(L,H,x,s)) for x in (a,b)]
 return sc(Q(1,2),add(mul(Ub[0],L[b]),sc(-1,mul(Ub[1],L[a])),mul(U[a],Lb[1]),sc(-1,mul(U[b],Lb[0]))))
def T2(L,U,H0,J0,r,s):
 a,b=r
 return sc(Q(1,4),add(br(N(U,J0,a,s),L[b]),sc(-1,br(N(U,J0,b,s),L[a])),br(U[a],N(L,H0,b,s)),sc(-1,br(U[b],N(L,H0,a,s)))))
def T4(L,U,r,s):
 a,b=r
 return sc(Q(1,4),add(sc(dot(U[a],K(U,s)),L[b]),sc(-dot(U[b],K(U,s)),L[a]),sc(dot(L[b],K(L,s)),U[a]),sc(-dot(L[a],K(L,s)),U[b])))
def c(L,U,r):
 a,b=r
 return (dot(U[a],L[b])-dot(U[b],L[a]))/4
def omega(H0,J0):return sc(Q(1,8),add(*(sc(sign,br(J0[i,j],H0[k,l])) for i,j,k,l,sign in SIGNED)))
def tracejet(L,U,H0,J0):
 return sc(Q(1,8),add(*(sc(sign,add(sc(dot(U[i],U[j]),H0[k,l]),sc(dot(L[k],L[l]),J0[i,j]))) for i,j,k,l,sign in SIGNED)))
def Q2(L,U,H0,J0):
 out=[]
 for i,j,k,l,sign in SIGNED:
  HH=H0[k,l];JJ=J0[i,j]
  hh=add(sc(dot(U[i],U[j])+dot(U[i],L[j])+dot(U[j],L[i]),HH),sc(-dot(HH,U[i]),L[j]),sc(-dot(HH,U[j]),L[i]))
  jj=add(sc(dot(L[k],L[l])+dot(U[k],L[l])+dot(U[l],L[k]),JJ),sc(-dot(JJ,L[k]),U[l]),sc(-dot(JJ,L[l]),U[k]))
  out.append(sc(sign,add(hh,jj)))
 return sc(Q(1,8),add(*out))
def Q4(L,U):
 V=[add(x,y) for x,y in zip(L,U)]
 return add(sc(Q(1,2),add(br(K(U,p),K(L,q)),br(K(U,q),K(L,p)))),T4(L,U,p,q),T4(L,U,q,p),sc(-c(L,U,q),K(V,p)),sc(-c(L,U,p),K(V,q)))
def invented(n):
 def X(a,b):return (Q(a),Q(b),Q(a-b),Q(-a))
 L=[X(n+i,2*i-n) for i in range(4)]
 U=[X(2*n-i,n+2*i+1) for i in range(4)]
 H0={(i,j):X(n+min(i,j)+2*max(i,j),min(i,j)-max(i,j)+1) for i in range(4) for j in range(4)}
 J0={(i,j):X(2*n-min(i,j)+max(i,j),2*min(i,j)+max(i,j)-1) for i in range(4) for j in range(4)}
 H={ij:add(y,sc(dot(L[ij[0]],L[ij[1]])/2,I)) for ij,y in H0.items()}
 J={ij:add(y,sc(dot(U[ij[0]],U[ij[1]])/2,I)) for ij,y in J0.items()}
 return L,U,H0,J0,H,J

class CurrentRemainder(unittest.TestCase):
 def test_normalized_derivative_sl2_identity(self):
  for n in range(1,9):
   L,U,H0,J0,H,J=invented(n)
   for X,Y,Y0 in ((L,H,H0),(U,J,J0)):
    for r in (p,q):
     for a in range(4):
      self.assertEqual(covDK(X,Y,a,r),add(N(X,Y0,a,r),sc(Q(-1,2),br(X[a],K(X,r)))))
      self.assertEqual(add(mul(X[a],K(X,r)),covDK(X,Y,a,r)),add(N(X,Y0,a,r),sc(dot(X[a],K(X,r))/2,I)))
 def test_compact_linear_jet_expression(self):
  for n in range(1,9):
   L,U,H0,J0,H,J=invented(n)
   self.assertEqual(Q2(L,U,H0,J0),add(T2(L,U,H0,J0,p,q),T2(L,U,H0,J0,q,p),tracejet(L,U,H0,J0)))
 def test_full_seven_term_reduction(self):
  for n in range(1,9):
   L,U,H0,J0,H,J=invented(n)
   V=[add(x,y) for x,y in zip(L,U)]
   kinetic=add(mul(K(U,p),K(L,q)),mul(K(U,q),K(L,p)),T(L,U,H,J,p,q),T(L,U,H,J,q,p),sc(Q(1,4),add(*(sc(sign,mul(J[i,j],H[k,l])) for i,j,k,l,sign in SIGNED))))
   lhs=add(tf(kinetic),sc(-c(L,U,q),K(V,p)),sc(-c(L,U,p),K(V,q)))
   rhs=add(omega(H0,J0),Q2(L,U,H0,J0),Q4(L,U))
   self.assertEqual(lhs,rhs)
   # Reversing either correction sign is detected by these invented inputs.
   wrong=add(tf(kinetic),sc(c(L,U,q),K(V,p)),sc(-c(L,U,p),K(V,q)))
   self.assertNotEqual(wrong,rhs)
 def test_zero_symbol_nonzero_quartic_control(self):
  L=[h,e,f,Z];U=[Z,Z,Z,h]
  Y0={(i,j):Z for i in range(4) for j in range(4)}
  self.assertEqual(omega(Y0,Y0),Z)
  self.assertEqual(Q2(L,U,Y0,Y0),Z)
  self.assertEqual(c(L,U,p),0);self.assertEqual(c(L,U,q),0)
  self.assertEqual(Q4(L,U),sc(Q(-1,8),h))

if __name__=='__main__':unittest.main(verbosity=2)
