#!/usr/bin/env python3
"""Complete universal polynomial identities; no source coefficients assigned."""
import sympy as S,runpy
from pathlib import Path
ns=runpy.run_path(str(Path(__file__).with_name('verify_lowest_normal_class_apolar_reconstruction.py')))
z,X,Y,A,B,c,L=[ns[q] for q in ('z','X','Y','A','B','c','L')]; k,w=S.symbols('k w',nonzero=True)
f,g,px,py=[ns[q] for q in ('f','g','px','py')]
fac=lambda e:S.factor(S.cancel(e))
zero=lambda e:all(S.cancel(v)==0 for v in e) if isinstance(e,S.MatrixBase) else S.cancel(e)==0
P=lambda p:S.Matrix([[1,0],[p,1]])
def regular(e,t):
 S.Poly(S.cancel(e),t,X,Y)
 for term in S.Add.make_args(S.expand(e)):
  assert term.as_powers_dict().get(t,0)>=0,(t,S.factor(e))
def lift(F,f,g,t):
 # Work over the symbolic coefficient field with Y unassigned as well.
 f1,g1,F1=[S.expand(e) for e in (f,g,F)]
 gi=S.invert(g1,f1,X)
 cc=fac(S.rem(F1*gi**2,f1,X))
 G=fac((F1-g1*g1*cc)/f1)
 bb=fac(S.rem(S.expand(G)*gi/2,f1,X))
 dd=fac((2*g1*bb-G)/f1)
 for e,degree in ((cc,2),(bb,4),(dd,6)):
  assert zero(X*S.diff(e,X)+Y*S.diff(e,Y)-degree*e)
 assert zero(2*f*g*bb+g*g*cc-f*f*dd-F)
 correction=S.series(-bb/f,t,0,1).removeO().expand()
 correction=S.expand(sum(term for term in S.Add.make_args(correction) if term.as_powers_dict().get(t,0)<0))
 correction=fac(correction)
 bb=fac(bb+f*correction);dd=fac(dd+2*g*correction)
 for e in (bb,cc,dd):regular(S.expand(e),t)
 print('regular trace lift',t,'correction =',correction,flush=True)
 return S.Matrix([[bb,cc],[dd,-bb]])
nh=A*(A*X**2*c*z**2+A*X*Y+B*X*Y*c**2*z**5+3*B*Y**2*c*z**3)/(B*L)
u=-2*k*A*X**3*Y*z**2/B-3*k*Y**4*z/c-3*k*A*X**2*Y**2/(B*c)
source_m=X*Y**2*(A*X+5*B*Y*c*z**3)/(2*B*c*z**4)
assert zero(X*Y**3*S.diff(f,z)-source_m*f-nh*g)
H=k*z**2*X*Y**3;rho=4*z
D=lambda e: e.applyfunc(D) if isinstance(e,S.MatrixBase) else S.expand(2*z*z*S.diff(e,z)+z*(X*S.diff(e,X)+Y*S.diff(e,Y)))
T=lambda e:S.expand(H*D(e)+u*e)
gx=S.expand(g+px*f)
Kx=lift(T(ns['nx']),f,gx,z)
fy=S.expand((f/z**3).subs(z,-1/w));gy0=S.expand((z**5*g).subs(z,-1/w))
py_y=-L*Y**2/(2*A*c*c*w*w)+L*X*X/(B*c*c*w)
gy=S.expand(gy0+py_y*fy)
uy=S.expand((u/z**2).subs(z,-1/w));Hy=k*X*Y**3
ny_y=S.expand((z**4*ns['ny']).subs(z,-1/w))
Fy=S.expand(Hy*2*S.diff(ny_y,w)+uy*ny_y)
assert zero(Fy-(z*z*T(ns['ny'])).subs(z,-1/w))
Ky=lift(Fy,fy,gy,w)
# Convert the regular y matrix to x coefficient lines, then change from regular y to regular x.
Kyback=Ky.subs(w,-1/z)
Kyback=S.Matrix([[Kyback[0,0],z**8*Kyback[0,1]],[z**-8*Kyback[1,0],Kyback[1,1]]])
Kyinx=P(px-py)*Kyback*P(py-px)
# Original lowest eta, expressed in the regular x quintic frame.
deta=ns['diag'];reta=ns['r_eta']+2*px*deta
eta=S.Matrix([[deta,0],[reta,-deta]])
cc=-2*k*z**4*nh
Lam=4*z*H-u
m=fac((H*D(f)+cc*gx)/f)
bb=fac(Lam/2-m);dd=fac(((Lam-m)*gx-H*D(gx))/f)
AA=S.Matrix([[bb,cc],[dd,-bb]])
for entry in AA: regular(entry,z)
Leta=(H*D(eta)+AA*eta-eta*AA+H*rho*eta).applyfunc(S.expand)
R=(Leta-Kyinx+Kx).applyfunc(fac)
assert zero(R[0,1]);assert zero(R[0,0]+R[1,1])
gamma=fac(R[0,0]/f)
assert zero(R[1,0]-2*gx*gamma)
print('gamma =',gamma,flush=True)
print('H1 coefficient z^-1 =',fac(S.expand(gamma).coeff(z,-1)),flush=True)
print('H1 coefficient z^-2 =',fac(S.expand(gamma).coeff(z,-2)),flush=True)
assert zero(S.diff(gamma,X,2));assert zero(S.diff(gamma,Y,2));assert zero(S.diff(gamma,X,Y))

# Keep and certify the exact trace-lift correction, not just its quotient.
nxmat=S.Matrix([[f*gx,-f*f],[gx*gx,-f*gx]])
assert zero(H*D(nxmat)+AA*nxmat-nxmat*AA-Lam*nxmat)
assert zero(S.trace(nxmat*Kx)-T(ns['nx']))
assert zero(S.trace(nxmat*Kyinx)-T(ns['ny']))
assert zero(S.trace(nxmat*Leta)-T(ns['trace']))

print('Exact endpoint coefficients:',fac(S.expand(gamma).coeff(z,-1)),fac(S.expand(gamma).coeff(z,-2)),flush=True)

assert zero(S.expand(gamma).coeff(z,-1)-3*k*Y/(B*c))
assert zero(S.expand(gamma).coeff(z,-2))
# Split off all terms except the genuine O(-3) cohomology coefficient.
gammax=-2*k*X*z/B+2*k*c**2*X*z**6/A-7*k*c*Y*z**4/A+2*k*B*c**3*Y*z**9/A**2
gammay=4*k*A**2*X*w**6/(B**3*c**4)-6*k*A*X*w/(B**2*c**2)-10*k*A*Y*w**3/(B**2*c**3)
regular(gammax,z);regular(gammay,w)
assert zero(gamma-3*k*Y/(B*c*z)-z**-3*gammay.subs(w,-1/z)+gammax)
# The GLOBAL dual test Y* tensor 1 of Wprime* O(1) gives this residue.
paired=S.diff(gamma,Y)
assert zero(S.expand(paired).coeff(z,-1)-3*k/(B*c))
print('PASS: source relation, regular cone operator, and both regular trace lifts.')
print('PASS: exact frame-transported secondary difference is tau(0,gamma).')
print('PASS: endpoint class is 3k/(Bc) [Y/z], with explicit remaining coboundary.')
print('PASS: global dual O(1) section Y* gives nonzero residue 3k/(Bc).')
print('All variables and source parameters remain unassigned. No instance rank or scan.')
print('Fixed actual operator comparison and a fourth Bockstein value are not inferred here.')
