#!/usr/bin/env python3
"""Universal formal identities only: no actual coefficient assignments or matrix/rank tests."""
import sympy as S
X,Y,z,v,A,B,c,l,k=S.symbols('X Y z v A B c l k', nonzero=True)
def tau(p,q):
 return S.expand(S.diff(p,X,2)*S.diff(q,Y,2)-2*S.diff(p,X,Y)*S.diff(q,X,Y)+S.diff(p,Y,2)*S.diff(q,X,2))
f=A*X**2*Y+B*z*Y**3+A*c*z**2*X**3-B*c*z**3*X*Y**2
g=-l/(2*A*c)*(B*X*Y**4/z**3+A*X**3*Y**2/z**4)
n=(X**2*(-4*A*z+B*c**2*z**6)+2*B*c*X*Y*z**4-3*B*Y**2*z**2)/l
m=S.cancel((X**4*S.diff(f,z)-n*g)/f)
assert S.denom(m).has(X)==False and S.denom(m).has(Y)==False
qx=-l/(2*A*c)*X*Y/z**4+l/(2*A)*X**2/z**2-l*B/A**2*Y**2/z
px=-qx
gx=S.expand(g+px*f)
assert all(t.as_powers_dict().get(z,0)>=0 for t in S.Add.make_args(gx))
u=4*k*B/(A*c)*X*Y**3*z**2+4*k/c*X**3*Y*z
Gamma=u+4*k*z**3*X**4
v0=2*B/A

def R(p,m,n,a,Gamma,v0,t):
 return S.expand(k*a*a*(-S.Rational(2,15)*tau(p,m)+S.Rational(2,5)*p*tau(p,n)+S.Rational(1,5)*tau(p,p)*n-S.Rational(1,15)*tau(X**4,S.diff(p,t))+S.Rational(2,3)*p*v0)-tau(p,Gamma)/30)
Rx=R(px,m,n,z*z,Gamma,v0,z)
zeta=Y**2*z*z-2*c*X*Y*z**4
sx=S.expand(tau(Rx,zeta))
bx=S.expand(sx).coeff(z,-1)
# Volume-compatible second chart v=-1/z; O(d) coefficients multiply by z^-d.
sub={z:-1/v}
fy=S.expand((f/z**3).subs(sub)); gy=S.expand((g*z**5).subs(sub)); ny=S.expand((n/z**6).subs(sub))
my=S.cancel((X**4*S.diff(fy,v)-ny*gy)/fy)
assert S.denom(my).has(X)==False and S.denom(my).has(Y)==False
py=-l/(2*A*c**2)*Y**2/v**2+l/(B*c**2)*X**2/v
assert all(t.as_powers_dict().get(v,0)>=0 for t in S.Add.make_args(S.expand(gy+py*fy)))
Gammay=S.expand((u/z**2).subs(sub)); v0y=v0/v**2
assert all(t.as_powers_dict().get(v,0)>=0 for t in S.Add.make_args(S.expand(v0y+tau(py,ny))))
Ry=R(py,my,ny,S.Integer(1),Gammay,v0y,v)
zetay=S.expand((zeta/z**4).subs(sub)); sy=S.expand(tau(Ry,zetay)); by=S.expand(sy).coeff(v,-1)
alpha=B*k*l/(10*A**2*c**2)
def regular(expr,t):
    return all(term.as_powers_dict().get(t,0)>=0 for term in S.Add.make_args(S.expand(expr)))
assert regular(Rx-alpha*Y**2/z**2,z)
assert regular(Ry+4*alpha*Y**2/v**4,v)
assert regular(v0+tau(px,n),z)
assert regular(v0y+tau(py,ny),v)
assert bx==0 and by==0
assert regular(sx,z) and regular(sy,v)
# Cup a=z^2 at x and a=1 at y. The only remaining y principal part
# is a globally meromorphic O(-4) section, constant in the x frame.
assert regular(z*z*Rx,z)
assert regular(Ry+4*alpha*Y**2/v**4,v)
assert S.cancel((-1/v)**4*(-4*alpha*Y**2)+4*alpha*Y**2/v**4)==0
print('PASS: universal divisor-quintic, exact operator relation, regular target generators and Gram primitive.')
print('PASS: complete R has only alpha Y^2/z^2 and -4 alpha Y^2/v^4 as its principal parts.')
print('PASS: both scalar Serre tests are regular; after cup a the vector principal parts are globally removable.')
print('No actual coefficient values, source-instance matrices, rank evaluations, or parameter scans were used.')
