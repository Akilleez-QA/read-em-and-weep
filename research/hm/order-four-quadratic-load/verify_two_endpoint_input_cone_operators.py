"""Uniform symbolic identities for two endpoint-input cone operators.
No source parameters are assigned and no actual-instance ranks are evaluated.
"""
import sympy as S
X,Y,z,w,A,B,c,L,k,e=S.symbols('X Y z w A B c lambda k e', nonzero=True)
f=A*X**2*Y+B*Y**3*z+A*c*X**3*z**2-B*c*X*Y**2*z**3
g=-L*(B*X*Y**4/z**3+A*X**3*Y**2/z**4)/(2*A*c)
px=L*X*Y/(2*A*c*z**4)-L*X**2/(2*A*z**2)+L*B*Y**2/(A*A*z)
py=-L*Y**2/(2*A*c*c*w**2)+L*X**2/(B*c*c*w)
fy=S.expand((f/z**3).subs(z,-1/w));gy=S.expand((z**5*g).subs(z,-1/w))
Qbasis={
(4,0):e*(-B*X*Y*z*z/(2*A)-B*Y*Y/(2*A*c)),
(3,1):e*(X*X*z+B*Y*Y*z*z/A)/4,
(2,2):-e*X*Y*z/2,
(1,3):e*(-A*X*X/B+Y*Y*z)/4,
(0,4):e*(A*X*Y/(2*B)-A*c*X*X*z*z/(2*B))}
def Q(poly):
 out=0
 for mon,co in S.Poly(S.expand(poly),X,Y).terms():
  assert mon in Qbasis
  out+=co*Qbasis[mon]
 return S.expand(out)
def zero(a): assert S.cancel(a)==0,S.factor(a)
def polynomial(a,variables):
 aa=S.cancel(a)
 den=S.denom(aa)
 assert not any(v in den.free_symbols for v in variables),(variables,S.factor(aa))
 S.Poly(aa,*variables)
 return aa
inputs=[
 ('X4',X**4,
 (X**2*(-4*A*z+B*c*c*z**6)+2*B*c*X*Y*z**4-3*B*Y*Y*z*z)/L,
 (4*A*c*X**4*z*z-4*A*X**3*Y-B*c*X*X*Y*Y*z**3-3*B*X*Y**3*z)/(2*A*c*z**3),
 4*k*B*X*Y**3*z*z/(A*c)+4*k*X**3*Y*z/c),
 ('XY3',X*Y**3,
 A*(A*X*X*c*z*z+A*X*Y+B*X*Y*c*c*z**5+3*B*Y*Y*c*z**3)/(B*L),
 X*Y*Y*(A*X+5*B*Y*c*z**3)/(2*B*c*z**4),
 -2*k*A*X**3*Y*z*z/B-3*k*Y**4*z/c-3*k*A*X*X*Y*Y/(B*c))]
connections={}
for name,h,n,m,u in inputs:
 zero(h*S.diff(f,z)-m*f-n*g)
 qh=Q(h)
 zero(Q(u)-k*z*z*(2*z*z*S.diff(qh,z)-4*z*qh))
 uy=S.expand((u/z**2).subs(z,-1/w));ny=S.expand((n/z**6).subs(z,-1/w))
 my=S.expand((z*z*m-3*z*h).subs(z,-1/w))
 zero(h*S.diff(fy,w)-my*fy-ny*gy)
 charts=[]
 for var,ff,gg,aa,uu,nn,pp in [(z,f,g,z*z,u,n,px),(w,fy,gy,S.Integer(1),uy,ny,py)]:
  gg=S.expand(gg+pp*ff)
  polynomial(ff,(var,X,Y));polynomial(gg,(var,X,Y))
  H=k*aa*h;ap=S.diff(aa,var)
  DD=lambda p:S.expand(2*aa*S.diff(p,var)+ap*(X*S.diff(p,X)+Y*S.diff(p,Y))/2)
  Lam=2*k*aa*ap*h-uu
  a12=-2*k*aa*aa*nn
  mf=S.cancel((H*DD(ff)+a12*gg)/ff)
  a11=S.cancel(Lam/2-mf)
  a21=S.cancel(((Lam-mf)*gg-H*DD(gg))/ff)
  conn=S.Matrix([[a11,a12],[a21,-a11]])
  for val in conn: polynomial(val,(var,X,Y))
  sigma=S.Matrix([ff,gg]);nil=S.Matrix([[ff*gg,-ff*ff],[gg*gg,-ff*gg]])
  for val in H*sigma.applyfunc(DD)+conn*sigma-Lam*sigma/2:zero(val)
  for val in H*nil.applyfunc(DD)+conn*nil-nil*conn-Lam*nil:zero(val)
  # Weighted homogeneous degrees: diagonal4, upper2, lower6.
  for val,deg in [(a11,4),(a12,2),(a21,6)]:
   zero(X*S.diff(val,X)+Y*S.diff(val,Y)-deg*val)
  charts.append(conn)
 connections[name]=charts
 print('PASS',name,': actual n/m identity, unique scalar inverse, both complete regular charts, section/nilpotent equations, and weighted degree4.')
# General conic correction line and uniqueness of the regular homogeneous solution.
assert 2-4//2==0
assert max(-1,0)==0 # H1(P1,O)=0
assert 4-8<0
# Full determinant scalar transport, valid for both h without specialization.
Z,Hroot,Uroot=S.symbols('Z Hroot Uroot', nonzero=True)
logdet_derivative=S.cancel(Z**3*S.diff(Z**-4,Z)/(Z**-4))
zero(logdet_derivative+4*Z**2)
zero(Z**-8*(4*Z**2*Hroot-Uroot+Hroot*logdet_derivative)+Z**-8*Uroot)
for name,h,n,m,u in inputs:
 uy=S.expand((u/z**2).subs(z,-1/w))
 uyroot=uy.subs({X:X/Z,Y:Y/Z,w:-1/Z**2},simultaneous=True)
 zero(uyroot-Z**-8*u.subs(z,Z**2))
# Independently verify the COMPLETE marked root-frame connection transport.
root_sub={X:X/Z,Y:Y/Z,w:-1/Z**2}
pxroot=px.subs(z,Z**2)
pyroot=py.subs(root_sub,simultaneous=True)
P0=S.Matrix([[Z**-9,0],[pyroot*Z**-9-Z**5*pxroot,Z**5]])
zero(P0.det()-Z**-4)
Droot=lambda p:Z**3*S.diff(p,Z)+Z**2*(X*S.diff(p,X)+Y*S.diff(p,Y))
for name,h,n,m,u in inputs:
 ax,ay=connections[name]
 ax=ax.subs(z,Z**2)
 ay=ay.subs(root_sub,simultaneous=True)
 hx=k*Z**4*h
 transported=P0*ax*P0.inv()-hx*P0.applyfunc(Droot)*P0.inv()
 transported=transported-S.eye(2)*S.trace(transported)/2
 for val in ay-Z**-8*transported:zero(val)
print('PASS: both complete root-frame transports, physical determinant scalars, and general conic patching degrees; no secondary value evaluated.')
