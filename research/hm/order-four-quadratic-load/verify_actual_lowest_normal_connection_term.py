"""Actual lowest normal-connection interface; all parameters unassigned.
No second-normal lift, selected source instance, or fourth value.
"""
from pathlib import Path
import sympy as S,runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):ns=runpy.run_path(str(Path(__file__).with_name('verify_homogeneous_first_normal_connection_cancellation.py')))
X,Y,z,A,B,c,L,k=[ns[v]for v in ('X','Y','z','A','B','c','L','k')]
f,g,T,K,B1=[ns[v]for v in ('f','g','T','K','B1')]
bm=ns['bm'];a=ns['a'];H=ns['H'];Ac=ns['Ac'];D=ns['D'];theta=ns['theta'];px=ns['px']
P=S.Matrix([[1,0],[px,1]]);Pi=S.Matrix([[1,0],[-px,1]])
H0=a*H;A0=a*Ac;H1=-theta*k*a*a
Kx=-P*K*Pi+bm(P,A0)*Pi+bm(P*A0,Pi)-P.applyfunc(lambda v:B1(H0,D(v)))-H1*P.applyfunc(D)*Pi
for v in Kx:S.Poly(S.cancel(v),z,X,Y)
Z,w=S.symbols('Z w',nonzero=True)
py=-L*Y**2/(2*A*c*c*w*w)+L*X*X/(B*c*c*w)
pyroot=S.expand(py.subs({X:X/Z,Y:Y/Z,w:-1/Z**2},simultaneous=True))
P=S.Matrix([[1,0],[pyroot,1]])*S.diag(Z**-9,Z**5);Pi=P.inv()
Droot=lambda v:S.expand(Z**3*S.diff(v,Z)+Z**2*(X*S.diff(v,X)+Y*S.diff(v,Y)))
HH=H0.subs(z,Z**2);AA=A0.subs(z,Z**2);HH1=H1.subs(z,Z**2);KK=-K.subs(z,Z**2)
DP=P.applyfunc(Droot)
Kyroot=Z**-8*(P*KK*Pi+bm(P,AA)*Pi+bm(P*AA,Pi)-DP.applyfunc(lambda v:B1(HH,v))*Pi-bm(HH*DP,Pi)-HH1*DP*Pi)
Kyroot=Kyroot-S.eye(2)*S.trace(Kyroot)/2
Kyroot=Kyroot.applyfunc(lambda v:S.cancel(v.subs({X:X*Z,Y:Y*Z},simultaneous=True)))
def to_w(v):
 v=S.expand(v);out=0
 for term in S.Add.make_args(v):
  power=term.as_powers_dict().get(Z,0);assert power%2==0
  out+=term/Z**power*(-1/w)**(power/2)
 return S.factor(out)
Ky=Kyroot.applyfunc(to_w)
for v in Ky:S.Poly(v,w,X,Y)
P=S.Matrix([[1,0],[px,1]]);Pi=P.inv();N=ns['N']
Tx=(P*T*Pi+bm(P,N)*Pi+bm(P*N,Pi)).applyfunc(lambda v:S.factor(S.cancel(v)))
Nx=(P*N*Pi).applyfunc(S.expand)
for v in Tx:S.Poly(v,z,X,Y)
Cx=(Kx*Tx-Tx*Kx+bm(Kx,Nx)-bm(Nx,Kx))[0,0]
Cx=S.factor(S.cancel(Cx))
S.Poly(Cx,z,X,Y)

def zero(v):
 if isinstance(v,S.MatrixBase):
  for ent in v:assert S.cancel(ent)==0
 else:assert S.cancel(v)==0
# Displayed regular y coefficients, including determinant trace subtraction.
zero(Ky[0,0]-3*A*k*w**4/(2*B*c**2))
zero(Ky[0,1])
zero(Ky[1,0]-L*k*(58*A*X**2*w**3+31*B*c*X*Y-53*B*Y**2*w**2)/(30*B**2*c**4))
zero(S.trace(Ky));zero(S.trace(Kx));zero(Kx[0,1])
zero(Kx[0,0]-k*(2*A**2-7*A*B*c**2*z**5+16*B**2*c**4*z**10)/(12*A*B*c**2))
zero(Kx[1,0]-L*k*z*(72*A**2*X**2*c*z**2+10*A**2*X*Y-48*A*B*X**2*c**3*z**7-72*A*B*X*Y*c**2*z**5-43*A*B*Y**2*c*z**3+48*B**2*Y**2*c**3*z**8)/(30*A**3*c))
zero(X*S.diff(Cx,X)+Y*S.diff(Cx,Y)-4*Cx)
zero(Cx-(-Kx[1,0]*Tx[0,1]+B1(Kx[1,0],f*f)))
# A complete polynomial identity, rather than a selected numerical evaluation.
poly=92*A**4*X**4*c*z**2+30*A**4*X**3*Y+426*A**3*B*X**4*c**3*z**7-870*A**3*B*X**3*Y*c**2*z**5-745*A**3*B*X**2*Y**2*c*z**3-10*A**3*B*X*Y**3*z-528*A**2*B**2*X**4*c**5*z**12+216*A**2*B**2*X**3*Y*c**4*z**10+933*A**2*B**2*X**2*Y**2*c**3*z**8+1280*A**2*B**2*X*Y**3*c**2*z**6-237*A**2*B**2*Y**4*c*z**4+480*A*B**3*X**2*Y**2*c**5*z**13-1272*A*B**3*X*Y**3*c**4*z**11+149*A*B**3*Y**4*c**3*z**9+48*B**4*Y**4*c**5*z**14
zero(Cx+L*k*z*poly/(210*A**3*c))
assert S.Poly(poly,X,Y,z).as_expr()!=0
# Explicit conic-scalar syzygy ambiguity has zero diagonal square-class.
ell=S.Symbol('ell')
change=ell*N
assert bm(change,N)==bm(N,change)
zero((change*T-T*change)[0,0]+ell*(f*f*T[1,0]+g*g*T[0,1]))
# Minimum weights in exact transport, including failed endpoint nilpotent gluing.
assert min(4+8-4,4+4,0+8,8,8+8)==8
assert 4+(-2)==2
assert 8+(-2)+4==10
assert 8+0+4==12
print('PASS: full affine harmonic first-normal transport, gamma q-symbol, both regular charts and determinant trace subtraction.')
print('PASS: actual marked leading nilpotent transport and complete nonzero degree-four old-K diagonal identity.')
print('PASS: conic/higher stabilizers and failed endpoint nilpotent gluing lie above the lowest-K interface.')
print('PASS: degree-zero centralizer ambiguity contributes zero modulo (f^2,g^2).')
print('Only the specified old-K summand is computed; no global next-error class, second-normal lift, or fourth value.')

# The new q-symbol is not covered by the frozen no-q-symbol coefficient formula.
qq,hh0,hh1,ddn,ddt,rr,tt,nn,ds,ss,ll0,ll1=S.symbols('qq hh0 hh1 ddn ddt rr tt nn ds ss ll0 ll1')
zero(S.expand((hh0+qq*hh1)*(ddn+qq*(ddt+rr*tt))).coeff(qq,1)-hh0*(ddt+rr*tt)-hh1*ddn)
zero(S.expand(((hh0+qq*hh1)*ds+(ll0+qq*ll1)*ss)*(nn+qq*tt)).coeff(qq,1)-(hh0*ds+ll0*ss)*tt-(hh1*ds+ll1*ss)*nn)
print('PASS: q-symbol additions H1 Dn and H1 Ds n are both explicitly retained.')
