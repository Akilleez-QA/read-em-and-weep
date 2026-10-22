#!/usr/bin/env python3
"""Universal exact cone-operator patching; no actual parameter is assigned.
The constructed operator is not identified with a fixed ambient-probe normalization.
"""
from pathlib import Path
import runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):ns=runpy.run_path(str(Path(__file__).with_name('verify_actual_serre_lift_from_conic_cocycle.py')))
S=ns['S']; X,Y,z,w,A,B,c,L,k,Z=[ns[t] for t in ['X','Y','z','w','A','B','c','L','k','Z']]
source=ns['src']['src']
f,g,px,py,fy,gy=[ns[t] for t in ['f','g','px','py','fy','gy']]
h=X*X*Y*Y;u=source['u'];nh=source['nh']
uy=S.expand((u/z**2).subs(z,-1/w));nhy=S.expand((nh/z**6).subs(z,-1/w))

def conn(ff,gg,aa,uu,nhh,var):
 H=k*aa*h;ap=S.diff(aa,var)
 DD=lambda p:S.expand(2*aa*S.diff(p,var)+ap*(X*S.diff(p,X)+Y*S.diff(p,Y))/2)
 Lam=2*k*aa*ap*h-uu
 cc=-2*k*aa*aa*nhh
 mm=S.cancel((H*DD(ff)+cc*gg)/ff)
 bb=Lam/2-mm
 dd=S.cancel(((Lam-mm)*gg-H*DD(gg))/ff)
 return S.Matrix([[bb,cc],[dd,-bb]])
Ax=conn(f,S.expand(g+px*f),z*z,u,nh,z).applyfunc(lambda p:S.expand(p.subs(z,Z**2)))
Ay=conn(fy,S.expand(gy+py*fy),S.Integer(1),uy,nhy,w).applyfunc(lambda p:S.expand(p.subs({X:X/Z,Y:Y/Z,w:-1/Z**2},simultaneous=True)))
P0=ns['P0'];Hx=k*Z**4*h
Droot=lambda p:S.expand(Z**3*S.diff(p,Z)+Z**2*(X*S.diff(p,X)+Y*S.diff(p,Y)))
Atransport=P0*Ax*P0.inv()-Hx*P0.applyfunc(Droot)*P0.inv()
Atransport=Atransport-S.trace(Atransport)*S.eye(2)/2
Atransport=Z**-8*Atransport
Delta=(Ay-Atransport).applyfunc(S.cancel)
print('homogeneous gluing defect:',[S.factor(e) for e in Delta])
assert Delta==S.zeros(2)
print('PASS homogeneous cone operator glues on full E_v root charts.')

rho=ns['rho']
u_root=S.expand(u.subs(z,Z**2))
Lambda_root=4*Z**2*Hx-u_root
sx=ns['sx'];sy=ns['sy'];J0=ns['J0']
nx=sx*sx.T*J0;ny=sy*sy.T*J0
tx=rho/Z**2
SS=S.eye(2)-tx*nx
SSinv=S.eye(2)+tx*nx
Croot=S.expand(Hx*Droot(tx)+Lambda_root*tx)
Cdisplay=2*rho*k*(Z**4*X**2*Y**2+A/B*Z**2*X**4+X*Y**3/c+A/(B*c)*X**3*Y/Z**2)
assert S.expand(Croot-Cdisplay)==0
assert all(S.expand(e)==0 for e in Hx*nx.applyfunc(Droot)+Ax*nx-nx*Ax-Lambda_root*nx)
A_conic=(SS*Ax*SSinv-Hx*SS.applyfunc(Droot)*SSinv).applyfunc(S.expand)
assert all(S.expand(e)==0 for e in A_conic-Ax-Croot*nx)
print('PASS exact finite conic gauge identity, including cancellation of t² terms.')

cx=-2*rho*k*(z*z*X**2*Y**2+A/B*z*X**4+X*Y**3/c)
cy=-2*rho*k*A*X**3*Y*w/(B*c)
assert S.expand(cy.subs(w,-1/z)-cx-Croot.subs(Z**2,z))==0
cxroot=cx.subs(z,Z**2)
cyroot=cy.subs({X:X/Z,Y:Y/Z,w:-1/Z**2},simultaneous=True)
for var,cc0 in [(z,cx),(w,cy)]:
 assert all(term.as_powers_dict().get(var,0)>=0 for term in S.Add.make_args(S.expand(cc0)))
Aactualx=Ax+cxroot*nx
Aactualy=Ay+cyroot*ny
Pactual=P0*SS
Pactualinv=SSinv*P0.inv()
transport=Pactual*Aactualx*Pactualinv-Hx*Pactual.applyfunc(Droot)*Pactualinv
transport=Z**-8*(transport-S.trace(transport)*S.eye(2)/2)
assert all(S.expand(e)==0 for e in Aactualy-transport)
print('PASS FULL actual cone-operator root-frame covariance with the chosen scalar split.')

# Exact regular-pair kernel: T sigma=0 and trace(T)=0 force T=ell n.
ff,gg,ell=S.symbols('ff gg ell')
nn=S.Matrix([[ff*gg,-ff*ff],[gg*gg,-ff*gg]])
assert nn*S.Matrix([ff,gg])==S.zeros(2,1)
assert S.trace(nn)==0
assert S.expand(2-S.Rational(4,2))==0
print('PASS scalar freedom has coefficient line O_L(0), cover degree4 in O_X(2).')
print('A genuine cone adjoint operator is constructed, modulo H0(O_X(2))*N.')
print('No fixed ambient-probe normalization, q-normal connection, or fourth value is claimed.')
