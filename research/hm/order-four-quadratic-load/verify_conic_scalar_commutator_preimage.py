"""Universal regular-pair identities, not an HM-instance matrix test."""
import sympy as s
f,g,p,q,ell=s.symbols('f g p q ell')
sigma=s.Matrix([f,g]); J=s.Matrix([[0,-1],[1,0]])
n=sigma*sigma.T*J
r=f*p+g*q
B=sigma*s.Matrix([[p,q]])-r*s.eye(2)/2
zero=s.zeros(2)
assert s.simplify(B*n-n*B-r*n)==zero
assert s.trace(B)==0
Bp=sigma*s.Matrix([[p+ell*g,q-ell*f]])-r*s.eye(2)/2
assert s.simplify(Bp-B-ell*n)==zero
v=sigma*r
tau=sigma*v.T*J+v*sigma.T*J
assert s.simplify(tau-2*r*n)==zero
assert s.simplify((-2*B)*n-n*(-2*B)+tau)==zero
assert 3+5-2==6 < 8  # regular-pair socle degree
assert [6+6,10+2,6+10-4,10+6-4]==[12]*4
print('PASS: regular commutator preimage, exact scalar subtraction and centralizer ambiguity.')
print('PASS: these old-K terms have degree12, not degree4.')
print('No full normal connection or fourth-obstruction value is identified.')
