#!/usr/bin/env python3
"""Exact checks for explicit-lange-abelian-monad.md.

The smoothness certificate uses all 12 projective chart ideals over F_101,
then the proper-specialization argument stated in the proof document.
It is not a random-point test and not a claim that modular rank alone lifts.
"""
import sympy as S
import time
z,w,tau=S.symbols('z w tau',nonzero=True)
x0,x1,x2,x3=S.symbols('x0 x1 x2 x3')
u,v=S.symbols('u v')
avec=S.Matrix([z*x0-x2,z*x1-x3]);j=S.Matrix([-avec[1],avec[0]])
h=S.Matrix([-u**3-2*u*v*v,-v**3-2*u*u*v])
hs=h.subs({u:x0,v:x1});ht=h.subs({u:x2,v:x3})
path=S.Matrix([x2,x3])+tau*avec
K=h.jacobian([u,v]).subs({u:path[0],v:path[1]},simultaneous=True).applyfunc(lambda p:S.integrate(p,(tau,0,1)))
k=1+S.Rational(2,3)*z*z+z**4
D=z*z*K+k*j*j.T
TB=(z**5*S.eye(2)).row_join(S.zeros(2)).col_join(D.row_join(z*S.eye(2)))
alpha_s=avec.col_join(hs);alpha_t=(avec/z).col_join(ht)
beta_s=(-hs.T).row_join(avec.T);beta_t=(-ht.T).row_join((avec/z).T)
zero=lambda mat: all(S.expand(c)==0 for c in mat)
assert zero(K-K.T)
assert zero(TB*alpha_t-z**4*alpha_s)
assert zero(beta_s*TB-z**2*beta_t)
assert zero(beta_s*alpha_s)
# Squarefreeness of the Hamiltonian binary quartic, including infinity.
HH=u**4+4*u*u*v*v+v**4
assert S.gcd(HH.subs(v,1),S.diff(HH,u).subs(v,1))==1
assert HH.subs({u:1,v:0})!=0
print('PASS: valid locally free Hamiltonian-ribbon monad and squarefree H.')

def section(base,A,C,p,q,sign):
 off=sign*(1-base*base)
 M=S.Matrix([[base,off],[off,0]])
 hv=S.Matrix([-A**3-2*A*C*C,-C**3-2*A*A*C])
 aa=S.Matrix([p,q]);jj=S.Matrix([-q,p])
 T=base*(q*q-p*p-A*A+C*C)+sign*(-p*q+p*A-q*C-2*A*C)
 return (M*aa).col_join(M*hv+T*jj)
Ws=section(z,x0,x1,avec[0],avec[1],1)
Wt=section(1/z,x2,x3,avec[0]/z,avec[1]/z,-1)
assert zero(Ws-TB*Wt/z**2)
assert zero(beta_s*Ws)
print('PASS: the explicit section of V=G(-2,2) glues on the two base charts.')
# Eigenline double cover has four simple branch points in characteristic zero and 101.
branch=4*z**4-7*z*z+4
assert S.gcd(branch,S.diff(branch,z))==1
assert S.gcd(S.Poly(branch,z,modulus=101),S.Poly(S.diff(branch,z),z,modulus=101)).degree()==0
print('PASS: spectral curve is a smooth connected genus-one double cover.')
# Exact H0(V) calculation and three explicit independent section classes.
xs=[x0,x1,x2,x3]
monoms=[(i,q,r,4-i-q-r) for i in range(5) for q in range(5-i) for r in range(5-i-q)]
def nonnegative_part(poly):
 return S.Add(*[term for term in S.Add.make_args(S.expand(poly)) if term.as_powers_dict().get(z,0)>=0])
columns=[]
for row in range(2):
 for degree in range(4):
  for xx in xs:
   low=S.zeros(2,1);low[row]=z**degree*xx
   overlap=K*low/z**3+k*j*(j.T*low)[0]/z**5
   high=overlap.applyfunc(nonnegative_part)
   value=S.expand((-hs.T*low)[0]+(avec.T*high)[0])
   assert not value.has(z)
   pol=S.Poly(value,*xs)
   columns.append(S.Matrix([pol.coeff_monomial(m) for m in monoms]))
assert S.Matrix.hstack(*columns).rank()==26
print('PASS: global beta map has rank 26; h0(V)=32-26-3=3.')
pp,qq,AA,CC=S.symbols('pp qq AA CC')
hhat=S.Matrix([-AA**3-2*AA*CC*CC,-CC**3-2*AA*AA*CC])
aa=S.Matrix([pp,qq]);jj=S.Matrix([-qq,pp])
Ms=[S.diag(z,0),S.Matrix([[0,1-z*z],[1-z*z,0]]),S.Matrix([[0,1+z*z],[-1-z*z,0]])]
Ts=[-pp*qq-2*AA*CC,z*(qq*qq-pp*pp-AA*AA+CC*CC)+pp*AA-qq*CC,-z*(pp*pp+qq*qq)-5*(pp*AA+qq*CC)+5*z*(AA*AA+CC*CC)]
for MM,TT in zip(Ms,Ts):
 low=MM*avec
 high=(K*low/z**3+k*j*(j.T*low)[0]/z**5).applyfunc(nonnegative_part)
 expected=(MM.T*hhat+TT*jj).subs({pp:avec[0],qq:avec[1],AA:x0,CC:x1},simultaneous=True)
 assert zero(high-expected)
 assert zero((-hs.T*low)+avec.T*high)
print('PASS: the three stated basis sections have the exact polynomial lifts.')
# Their low matrices are independent modulo scalar matrices, hence modulo alpha.
ca,cb,cc=S.symbols('ca cb cc')
MM=ca*Ms[0]+cb*Ms[1]+cc*Ms[2]
discriminant=S.expand(S.trace(MM)**2-4*MM.det())
assert discriminant==S.expand(4*(cb*cb-cc*cc)*z**4+(ca*ca-8*cb*cb-8*cc*cc)*z*z+4*(cb*cb-cc*cc))
print('PASS: branch quartic formula for the projective net of sections.')
# Complete singular-fiber test: 2 base charts × 2 eigenline charts × 3 plane charts.
b,r,A,C,p=S.symbols('b r A C p')
h1=-A**3-2*A*C*C;h2=-C**3-2*A*A*C
checks=0
for sign in [1,-1]:
 off=sign*(1-b*b)
 for eigenchart in [0,1]:
  an1,an2=(p,r*p) if eigenchart==0 else (r*p,p)
  T=b*(an2*an2-an1*an1-A*A+C*C)+sign*(-an1*an2+an1*A-an2*C-2*A*C)
  if eigenchart==0:
   Q=off*(1-r*r)-b*r
   lam=b+off*r
   cubic=off*h1-lam*h2+p*T
  else:
   Q=off*(r*r-1)-b*r
   lam=off*r
   cubic=(b-lam)*h1+off*h2-p*T
  for fixed in [p,A,C]:
   polys=[Q]+[S.diff(cubic,c).subs(fixed,1) for c in [A,C,p]]
   variables=[b,r]+[c for c in [A,C,p] if c!=fixed]
   start=time.time()
   gb=S.groebner(polys,*variables,modulus=101,order='grevlex')
   assert len(gb.polys)==1 and gb.polys[0].as_expr()==1,(sign,eigenchart,fixed,gb)
   checks+=1
   print(f'PASS {checks}/12: base sign {sign}, eigenline chart {eigenchart}, plane chart {fixed}; singularity ideal=(1) over F_101 ({time.time()-start:.2f}s).',flush=True)
print('PASS: no geometric singular cubic fibers in characteristic 101, across the complete projective atlas.')
print('By properness of the projective relative singular locus over Z[1/30], no singular cubic fibers exist over Qbar.')
print('Combined with the proved spectral identification, adjunction and connectedness: the section zero locus is an abelian surface.')
print('NOT computed by this script: mixed Atiyah evaluation or higher-order deformations.')
