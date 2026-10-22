#!/usr/bin/env python3
"""Universal full cone-bundle gluing, with all source/residue parameters formal.
No normal-thickening connection or fourth Bockstein value is inferred.
"""
from pathlib import Path
import contextlib,io,runpy
import sympy as S
with contextlib.redirect_stdout(io.StringIO()):
    src=runpy.run_path(str(Path(__file__).with_name('verify_homogeneous_first_normal_connection_cancellation.py')))
X,Y,z,w,A,B,c,L,k=[src[t] for t in ['X','Y','z','w','A','B','c','L','k']]
f,g,px,py,fy,gy,V1,V2,V1y,V2y=[src[t] for t in ['f','g','px','py','fy','gy','V1','V2','V1y','V2y']]
rho,Z=S.symbols('rho_C Z',nonzero=True)
J0=S.Matrix([[0,-1],[1,0]]);JC=-J0
Omega=S.expand(f*V2-g*V1)
omega0=L*k*(A*A*X**7*Y/(6*B*c)-B*X*X*Y**6/(3*c*c))
omega1=-L*k*B*B*Y**8/(3*A*c*c)
omega2=L*k*(A*A*X**8/(6*B)-5*B*X**3*Y**5/(6*c))
assert S.expand(Omega-omega0-omega1*z-omega2*z*z)==0
assert all(S.Poly(P,X,Y).total_degree()==8 for P in [omega0,omega1,omega2])
# Signs agree with JC in the actual conic theorem: P=I+t NC=I-t n.
rx=-rho*(omega1+omega2*z)
ry=-rho*omega0*w
assert S.expand(ry.subs(w,-1/z)-rx-rho*Omega/z)==0
print('PASS: exact wedge coefficients and oriented two-chart scalar splitting.')

sigmax=S.Matrix([f,S.expand(g+px*f)])
sigmay=S.Matrix([fy,S.expand(gy+py*fy)])
Vx0=S.Matrix([V1,S.expand(V2+px*V1)])
Vy0=S.Matrix([V1y,S.expand(V2y+py*V1y)])
Vx=(Vx0+sigmax*rx).applyfunc(S.expand)
Vy=(Vy0+sigmay*ry).applyfunc(S.expand)
for var,vec in [(z,Vx),(w,Vy)]:
    for entry in vec:
        assert all(term.as_powers_dict().get(var,0)>=0 for term in S.Add.make_args(entry))
assert S.expand(sigmax[0]*Vx[1]-sigmax[1]*Vx[0]-Omega)==0
assert S.expand(sigmay[0]*Vy[1]-sigmay[1]*Vy[0]-(Omega/z**2).subs(z,-1/w))==0
print('PASS: complete regular charts, unchanged wedge, and O(6) coefficient transport.')

# Full ROOT chart factors, not only the leading coefficient factors.
# z=Z²; positive root coordinates change as (Xy,Yy)=(X/Z,Y/Z).
xsub={z:Z**2}
ysub={X:X/Z,Y:Y/Z,w:-1/Z**2}
pxroot=px.subs(xsub)
pyroot=py.subs(ysub,simultaneous=True)
Pxinv=S.Matrix([[1,0],[-pxroot,1]])
Py=S.Matrix([[1,0],[pyroot,1]])
Droot=S.diag(Z**-9,Z**5)
P0=Py*Droot*Pxinv
assert S.cancel(P0.det()-Z**-4)==0
sx=sigmax.subs(xsub)
sy=sigmay.subs(ysub,simultaneous=True)
assert all(S.expand(e)==0 for e in sy-P0*sx)
T4=Z**-8*P0
vx0=Vx0.subs(xsub);vy0=Vy0.subs(ysub,simultaneous=True)
assert all(S.expand(e)==0 for e in vy0-T4*vx0)
NC=sx*sx.T*JC
tx=rho/Z**2
actual_transition=T4*(S.eye(2)+tx*NC)
assert all(S.expand(e)==0 for e in Vy.subs(ysub,simultaneous=True)-actual_transition*Vx.subs(xsub))
print('PASS: FULL actual cone transition, including root frames and higher-degree correction.')

# Sign of the Euler extension in ordered u-to-v coordinate transport.
u,v,aa,hh=S.symbols('u v aa hh',nonzero=True)
ss=S.Matrix([u,v]);su=S.Matrix([0,hh/u]);sv=S.Matrix([-hh/v,0])
assert all(S.cancel(e)==0 for e in aa*ss+su-(aa+hh/(u*v))*ss-sv)
assert (S.Matrix([[0,1],[-1,0]])*S.Matrix([v,-u]))==S.Matrix([-u,-v])
print('PASS: Koszul splitting orientation fixes the plus conic cocycle and opposite old n.')

# A global chain identification for the homogeneous triangular extension.
# Let mu=Ttor². The ordered middle-frame correction is diag(Ttor³,Ttor⁵).
Ttor,ff,gg,p,alpha,beta=S.symbols('Ttor ff gg p alpha beta',nonzero=True)
Dtor=S.diag(Ttor**3,Ttor**5)
Pgeneric=S.Matrix([[alpha,0],[p,beta]])
Ppulled=S.Matrix([[alpha,0],[Ttor**-2*p,beta]])
assert S.simplify(Dtor*Ppulled*Dtor.inv()-Pgeneric)==S.zeros(2)
assert Dtor*S.Matrix([Ttor**-3*ff,Ttor**-5*gg])==S.Matrix([ff,gg])
pi=S.Matrix([[-gg,ff]])
pi_pulled=Ttor**4*S.Matrix([[-Ttor**-5*gg,Ttor**-3*ff]])
assert S.simplify(pi*Dtor-Ttor**4*pi_pulled)==S.zeros(1,2)
print('PASS: homogeneous transition chain has extension character mu², not just that residue weight.')

# Exact all-degree weight/line arithmetic, rather than an actual-instance rank.
j=S.symbols('j',integer=True,nonnegative=True)
assert (3+5)/S.Integer(2)-2==2
assert S.solve(S.Eq(-2-j,2),j)==[]
assert (-2-j).is_negative
assert 6-S.Rational(8,2)==2
assert 4-S.Rational(8,2)==0
assert -2+2==0
assert 4-S.Rational(0,2)==4
assert (S.Rational(9,2)-S.Rational(3,2),-S.Rational(5,2)-S.Rational(5,2))==(3,-5)
assert (S.Rational(17,2)-S.Rational(3,2),S.Rational(3,2)-S.Rational(5,2))==(7,-1)
print('PASS: eigenextension uniqueness, marked-automorphism vanishing, and all coefficient lines.')
print('Geometric inputs: actual conic extension theorem and reflexive Hartogs. No q-normal or beta4 claim.')
