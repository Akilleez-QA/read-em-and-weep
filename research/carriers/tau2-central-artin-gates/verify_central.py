#!/usr/bin/env python3
"""Exact symbolic checks for the conditional tau-two central criterion.
Does not construct a completed monad and imports no previous calculation.
"""
from itertools import combinations
import sympy as sp
ell,h,a=sp.symbols('ell h a'); J=sp.Matrix([[0,1],[-1,0]])
L=sp.Matrix([[ell,h],[0,a]]); I=sp.eye(2); Z=sp.zeros(2)
def zero(M): return all(sp.cancel(x)==0 for x in M)
def mat(p): return sp.Matrix(2,2,sp.symbols(p+'0:4'))
def sym(p):
    x,y,z=sp.symbols(p+'0:3'); return sp.Matrix([[x,y],[y,z]])
def half(V): return V.T*J*V/2
def cross(V,W): return (V.T*J*W-W.T*J*V)/2
def g(V,S): return sp.BlockMatrix([[I,V.T*J,S+half(V)],[Z,I,V],[Z,Z,I]]).as_explicit()
V,W,Ui,Uj,Q,R,Rj=[mat(p) for p in ('v','w','ui','uj','q','r','rj')]
S,T=sym('s'),sym('t'); Omega=sp.BlockMatrix([[Z,Z,I],[Z,J,Z],[-I,Z,Z]]).as_explicit()
assert zero(g(V,S).T*Omega*g(V,S)-Omega)
assert zero(g(V,S)*g(W,T)-g(V+W,S+T+cross(V,W)))
B=L.row_join(Q).row_join(R)
assert zero(B*Omega.inv()*B.T-(R*L.T-L*R.T-Q*J*Q.T))
Qj=Q+L*V.T*J
dmap=lambda A:(A*L.T-L*A.T)[0,1]
fmap=lambda A:(A*J*A.T)[0,1]
assert sp.cancel(dmap(Q*V+L*half(V))-fmap(Qj)+fmap(Q))==0
C=Rj-R-Q*V-L*half(V)
Cnew=(Rj+Qj*Uj+L*half(Uj))-(R+Q*Ui+L*half(Ui))-(Q+L*Ui.T*J)*(V+Uj-Ui)-L*half(V+Uj-Ui)
assert zero(Cnew-C-L*(-cross(Ui,V)+cross(V,Uj)-cross(Ui,Uj)))
print('PASS: full symplectic identity, half correction, and change-of-lift invariance')
r,b,c,d,k,z=sp.symbols('r b c d k z')
Rsyz=sp.Matrix([[r,ell*b+h*c],[a*b+h*d,a*c-ell*d]])
assert zero(Rsyz*L.T-L*Rsyz.T)
Rpair=lambda rr,dd:sp.Matrix([[rr,0],[h*dd,-ell*dd]])
assert zero(Rsyz-L*sp.Matrix([[0,b],[b,c]])-Rpair(r-h*b,d))
P=sp.Matrix([[ell,h*h],[0,a]])
assert zero(Rpair(ell*z+h*h*k,a*k)-L*sp.Matrix([[z,h*k],[h*k,-ell*k]]))
assert sp.det(P)==a*ell
assert zero(sp.Matrix([[a,-h*h]])*P-sp.Matrix([[a*ell,0]]))
assert zero(a*sp.Matrix([0,ell])-P*sp.Matrix([-h*h,ell]))
assert zero(Rpair(0,ell)-L*sp.Matrix([[-h*h/a,h*ell/a],[h*ell/a,-ell*ell/a]]))
assert zero(Rpair(0,ell).subs(ell,0))
print('PASS: exact presentation relations, a-torsion generator, and torsion rank invariance')
q1,q2,d1,d2,rho,v,w=sp.symbols('q1 q2 d1 d2 rho v w')
# Work in the Laurent polynomial ring with a inverted, without setting a=1.
Qo=sp.Matrix([[(q1+h*d1)/a,(q2+h*d2)/a],[d1,d2]])
Ro=sp.Matrix([[(rho+h*v)/a,(ell*v+h*w+(q1*d2-q2*d1)/a)/a],[v,w]])
Bo=L.row_join(Qo).row_join(Ro)
assert zero(Ro*L.T-L*Ro.T-Qo*J*Qo.T)
mi=lambda i,j:sp.cancel(Bo[:,[i,j]].det())
assert [mi(0,1),mi(1,2),mi(1,3),mi(1,4)]==[a*ell,-q1,-q2,-rho]
assert all(sp.expand(mi(i,j).subs({ell:0,q1:0,q2:0,rho:0}))==0 for i,j in combinations(range(6),2))
print('PASS: on a invertible, rank-minor ideal is (ell,q1,q2,rho)')
# Exact exceptional normal form after the necessary invertibility of Q_D.
b11,b12,b21,b22,C1,C2,zz=sp.symbols('b11 b12 b21 b22 C1 C2 zz')
D1,D2=b11*ell+b12*h,b21*ell+b22*h
ve,we=-b21*C1+b11*C2+h*zz,-b22*C1+b12*C2-ell*zz
assert sp.expand(ell*ve+h*we+C1*D2-C2*D1)==0
assert sp.det(sp.Matrix([[-b21,b11],[-b22,b12]]))==b11*b22-b12*b21
# Changing the free linear syzygy zz cannot alter the pair on Lambda.
assert [sp.expand(ve).subs({ell:0,h:0}),sp.expand(we).subs({ell:0,h:0})]==[-b21*C1+b11*C2,-b22*C1+b12*C2]
print('PASS: sharp exceptional-gate isotropy formula and invertible restriction transform')
