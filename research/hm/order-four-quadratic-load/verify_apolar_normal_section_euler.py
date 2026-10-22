"""Uniform reduction of eta sigma to the scalar Euler channel."""
import runpy
from pathlib import Path
import sympy as S
ns=runpy.run_path(str(Path(__file__).with_name('verify_lowest_normal_class_apolar_reconstruction.py')))
z,X,Y,A,B,c,L=[ns[q] for q in ('z','X','Y','A','B','c','L')]
w=S.Symbol('w',nonzero=True)
f,g,px,py=[ns[q] for q in ('f','g','px','py')]
fac=lambda a:S.factor(S.cancel(a))
def zero(a):
 if isinstance(a,S.MatrixBase):
  for v in a:assert S.cancel(v)==0
 else:assert S.cancel(a)==0

def lift(n,f,g,t):
 # wedge(sigma,V)=-n, so V1 is n/g modulo f.
 gi=S.invert(g,f,X)
 v1=fac(S.rem(S.expand(n*gi),f,X))
 v2=fac((g*v1-n)/f)
 print('raw lift',t,v1,v2,flush=True)
 # A scalar multiple of sigma leaves wedge unchanged; remove any base poles.
 ratio=S.series(-v1/f,t,0,1).removeO().expand()
 corr=fac(sum(v for v in S.Add.make_args(ratio) if v.as_powers_dict().get(t,0)<0))
 v1=fac(v1+f*corr);v2=fac(v2+g*corr)
 for v in (v1,v2):S.Poly(v,t,X,Y)
 zero(f*v2-g*v1+n)
 print('correction',t,corr,flush=True)
 return S.Matrix([v1,v2])
gx=S.expand(g+px*f)
Vx=lift(ns['nx'],f,gx,z)
fy=S.expand((f/z**3).subs(z,-1/w))
pyy=-L*Y**2/(2*A*c*c*w*w)+L*X*X/(B*c*c*w)
gy=S.expand((z**5*g).subs(z,-1/w)+pyy*fy)
nyy=S.expand((z**4*ns['ny']).subs(z,-1/w))
Vy=lift(nyy,fy,gy,w)
# G(-2) coefficient lines for components of cover degrees3,5: O(1),O(-7).
back=Vy.subs(w,-1/z)
back=S.Matrix([z*back[0],z**-7*back[1]])
P=lambda p:S.Matrix([[1,0],[p,1]])
Vyinx=P(px-py)*back
eta=S.Matrix([[ns['diag'],0],[ns['r_eta']+2*px*ns['diag'],-ns['diag']]])
sigma=S.Matrix([f,gx])
R=(eta*sigma-Vyinx+Vx).applyfunc(fac)
r=fac(R[0]/f)
zero(R-sigma*r)
print('r =',r,flush=True)
print('Euler coefficient =',S.expand(r).coeff(z,-1),flush=True)

# Exact scalar coboundary in O(-2), retaining the oriented coordinate.
d=B*c*c/A
rx=d*z**4
ry=w**4/d
zero(r-1/z-z**-2*ry.subs(w,-1/z)+rx)
zero(S.expand(r).coeff(z,-1)-1)
S.Poly(rx,z);S.Poly(ry,w)
assert not ((r.free_symbols)&{X,Y})
# Check eta*sigma wedge and bracket conventions directly.
zero(f*(eta*sigma)[1]-gx*(eta*sigma)[0]+ns['trace'])
J=S.Matrix([[0,-1],[1,0]])
nmat=sigma*sigma.T*J
v=eta*sigma
tau=lambda v:sigma*v.T*J+v*sigma.T*J
zero(eta*nmat-nmat*eta-tau(v))
zero(tau(sigma)-2*nmat)
print('Vx =',Vx.applyfunc(S.expand),flush=True)
print('Vy =',Vy.applyfunc(S.expand),flush=True)
print('PASS: exact regular Serre lifts of -n_i, full O(1)/O(-7) transport, and scalar Euler coefficient ONE.')
print('PASS: r=1/z+delta(rx,ry); bracket equals tau(eta sigma), and tau(sigma)=2n in the stated marking.')
print('Unknown actual normal scale and conic marking remain unchanged. No ambient second-normal lift or fourth value.')

zero(Vx-S.Matrix([-2*A*c*X**3*z+3*B*c*X*Y**2*z**2-B*Y**3,
 -B*c*L*X**3*Y**2/(2*A)+3*B**2*c*L*X*Y**4*z/A**2]))
zero(Vy-S.Matrix([A*c*X**3+3*A*X**2*Y*w**2-2*B*Y**3*w,
 3*A*L*X**4*Y*w/(B*c**2)-L*X**2*Y**3/(2*c**2)]))
print('PASS: both complete displayed regular lift formulas.')
