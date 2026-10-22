"""Exact comparison with the fixed apolar scalar marking. No parameter values."""
from pathlib import Path
import sympy as S,runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
    data=runpy.run_path(str(Path(__file__).with_name('verify_actual_nilpotent_second_normal_residue.py')))
X,Y,z,A,B,c,L,f,gx,chi,R=[data[q] for q in ('X','Y','z','A','B','c','L','f','gx','E','rem')]
chi=chi[0,0]
v1=-2*A*c*X**3*z+3*B*c*X*Y**2*z**2-B*Y**3
v2=-B*c*L*X**3*Y**2/(2*A)+3*B**2*c*L*X*Y**4*z/A**2
nx=S.expand(gx*v1-f*v2) # sigma wedge Vx = -nx, not +nx
field=S.QQ.frac_field(A,B,c,L,z)
pf=S.Poly(f*f,X,Y,domain=field)
qg,rg=S.div(S.Poly(f*gx,X,Y,domain=field),pf)
qn,rn=S.div(S.Poly(nx,X,Y,domain=field),pf)
b=S.cancel(rn.coeff_monomial(X**5*Y**3)/rg.coeff_monomial(X**5*Y**3))
rn=S.factor((rn-b*rg).as_expr())
assert S.cancel(nx-(qn-b*qg).as_expr()*f*f-b*f*gx-rn)==0
assert S.Poly(rn,X).degree()<=4
assert S.cancel(R+B*L*rn/4)==0
Q=B**2*L**2*(207*A*c**2*z**2*X**2-95*A*c*X*Y-134*B*c**2*z**3*Y**2)/(140*A**3)
a=7*B**2*L*c**2*z**4/(6*A)
assert S.cancel(chi+B*L*nx/4-Q*f*f-a*f*gx)==0
for p in (nx,Q,a):S.Poly(p,X,Y,z)
# Match nx to the original apolar reconstruction, rather than only the displayed Vx.
with contextlib.redirect_stdout(io.StringIO()):
    ap=runpy.run_path(str(Path(__file__).with_name('verify_lowest_normal_class_apolar_reconstruction.py')))
# The source names this same formal parameter 'lambda'; this source names it 'L'.
assert S.cancel(nx-ap['nx'].subs(ap['L'],L))==0
nu=S.symbols('nu',nonzero=True)
assert S.cancel((R+B*L*rn/4)/nu**2)==0
print('PASS: both complete ideal reductions; exact regular polynomial identity; original apolar nx sign and marking.')
print('chi_bar = -(B*lambda/4) nx_bar; physical q0=nu*q gives -(B*lambda/(4*nu**2)).')
print('No actual normal-generator scale, endpoint lift, or fourth value is assigned.')
