#!/usr/bin/env python3
"""Exact algebraic checks for explicit-hamiltonian-ribbon-monad.md."""
import sympy as S
z = S.symbols('z', nonzero=True)
x0,x1,x2,x3 = x = S.symbols('x0 x1 x2 x3')
a = S.Matrix([z*x0-x2,z*x1-x3])
hs = S.Matrix([-x0**3,-x1**3])
ht = S.Matrix([-x2**3,-x3**3])
j = S.Matrix([-a[1],a[0]])
alpha_s = a.col_join(hs)
alpha_t = (a/z).col_join(ht)
beta_s = (-hs.T).row_join(a.T)
beta_t = (-ht.T).row_join((a/z).T)
D0 = -z**2*S.diag(z**2*x0**2+z*x0*x2+x2**2,z**2*x1**2+z*x1*x3+x3**2)
ks = S.symbols('k0:5')
k = sum(ks[i]*z**i for i in range(5))
D = D0+k*j*j.T
TB = (z**5*S.eye(2)).row_join(S.zeros(2)).col_join(D.row_join(z*S.eye(2)))
zero = lambda M: all(S.expand(e)==0 for e in M)
assert zero(beta_s*alpha_s) and zero(beta_t*alpha_t)
assert zero(TB*alpha_t-alpha_s*z**4)
assert zero(beta_s*TB-z**2*beta_t)
sig_s=S.zeros(2,1).col_join(j)
sig_t=sig_s/z
assert zero(TB*sig_t-sig_s)
J4=S.zeros(2).row_join(S.eye(2)).col_join((-S.eye(2)).row_join(S.zeros(2)))
assert zero(TB.T*J4*TB-z**6*J4)
print('PASS: all global chain, section, and symplectic identities for arbitrary k0,...,k4.')
minor_mat=alpha_s.row_join(sig_s)
minors=[S.expand(minor_mat.extract([i,j],[0,1]).det()) for i in range(4) for j in range(i+1,4)]
assert all(S.expand(p-q)==0 for p,q in zip(minors,[0,-a[0]*a[1],a[0]**2,-a[1]**2,a[0]*a[1],-x0**3*a[0]-x1**3*a[1]])),minors
print('PASS: section zero ideal is (a1^2,a1*a2,a2^2,x0^3*a1+x1^3*a2).')
u,v,t=S.symbols('u v t')
def trunc(poly):
 out=0
 for (i,j),c in S.Poly(S.expand(poly),u,v).terms():
  if i<2 and j<4:out+=c*u**i*v**j
 return S.expand(out)
def expc(q):return trunc(sum(q**n/S.factorial(n) for n in range(5)))
ch=trunc(2*expc(2*u-v)+2*expc(-2*u+v)-expc(u-2*v)-expc(-u+2*v))
assert ch==2-4*u*v-2*v**2+S.Rational(4,3)*u*v**3
print('PASS: rank 2, c1=0, c2=4uv+2v^2 and ch4=(4/3)uv^3.')
# H0(V): H0(B(-2,2)) identifies with H0(O(3,1))^2.
# Unique upper-chart high lift is the nonnegative-z part of the overlap expression.
monoms=[(i,q,r,4-i-q-r) for i in range(5) for q in range(5-i) for r in range(5-i-q)]
def nonneg(poly):
 return S.Add(*[term for term in S.Add.make_args(S.expand(poly)) if term.as_powers_dict().get(z,0)>=0])
Sdiag=-D0/z**2
for kval in [0,1,z,z*z,1+z**4,1+z+2*z*z+3*z**3+5*z**4]:
 columns=[]
 for i in range(2):
  for d in range(4):
   for xx in x:
    low=S.zeros(2,1);low[i]=z**d*xx
    overlap=-Sdiag*low/z**3+kval*j*(j.T*low)[0]/z**5
    high=overlap.applyfunc(nonneg)
    im=S.expand(x0**3*low[0]+x1**3*low[1]+(a.T*high)[0])
    assert not im.has(z),im
    pol=S.Poly(im,*x)
    columns.append(S.Matrix([pol.coeff_monomial(m) for m in monoms]))
 rank=S.Matrix.hstack(*columns).rank()
 print(f'k={kval}: H0(B→C) rank {rank}; h0(V)={32-rank-3}')
print('NOT computed: mixed Atiyah class; identification with the abelian-surface Lange family.')
