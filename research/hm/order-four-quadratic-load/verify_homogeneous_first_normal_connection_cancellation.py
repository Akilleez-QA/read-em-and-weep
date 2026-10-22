#!/usr/bin/env python3
"""Universal homogeneous identities, with every source parameter unassigned.
This does NOT identify a full actual G(4) lift or a next ambient connection.
"""
from pathlib import Path
import contextlib, io, runpy
import sympy as S
with contextlib.redirect_stdout(io.StringIO()):
    src=runpy.run_path(str(Path(__file__).with_name('verify_midpoint_absolute_square_error.py')))
X,Y,z,w,A,B,c,L,k=[src[t] for t in ['X','Y','z','w','A','B','c','L','k']]
f,g,a,u,h,D,Lam,px,py=[src[t] for t in ['f','g','a','u','h','D','Lam','px','py']]
tau=src['tau']
N=S.Matrix([[f*g,-f*f],[g*g,-f*g]])
T=S.Matrix([[src['T'],src['T12']],[src['T21'],-src['T']]])
m,cc,bb,dd=src['conn']
Ac=S.Matrix([[bb,cc],[dd,-bb]])
H=k*a*h

def B1(P,Q):
    if P==0 or Q==0:return S.Integer(0)
    pd=S.Poly(P,X,Y).total_degree();qd=S.Poly(Q,X,Y).total_degree()
    assert pd%2==qd%2==0
    if min(pd,qd)<2:return S.Integer(0)
    return tau(P,Q)/(2*(pd-1)*(qd-1)*(pd+qd-1))

def bm(U,V):
    return S.Matrix(2,2,lambda i,j:sum(B1(U[i,l],V[l,j]) for l in range(2)))

# Reconstruct the entire error from the universal first-normal product,
# independently of the previously displayed individual entry formulas.
Rmid=(N.applyfunc(lambda P:B1(H,D(P))-B1(Lam,P))
      +bm(Ac,N)-bm(N,Ac)+H*T.applyfunc(D)+u*T+Ac*T-T*Ac).applyfunc(S.expand)
known=S.Matrix([[src['ex'],src['E12']],[src['E21'],-src['ex']]])
assert all(S.expand(v)==0 for v in Rmid-known)
print('PASS: full homogeneous normal error independently reconstructed with B1.')
Rt=(k*a*(N.applyfunc(D)-2*S.diff(a,z)*N)).applyfunc(S.expand)
assert S.expand(Rt[0,0]-2*k*a*S.diff(a*f*g,z))==0
assert S.expand(2*f*g*Rt[0,0]+g*g*Rt[0,1]-f*f*Rt[1,0])==0

# Values forced by the homogeneous wedge/square-ideal comparison.
# They do not assign any actual source parameter A,B,c,L,k.
theta=-S.Rational(1,12)
chi=A*k/(3*B*c*c)
v1=k*z**5*(A*c*z*z*X**3/6-A*X**2*Y/2-2*B*z*Y**3/3)
v2=L*k*(A*X**5/(6*B*c)+z*X**3*Y**2/(12*c)-B*Y**5/(3*A*c*c))
V1=S.expand(v1+chi*f/2);V2=S.expand(v2+chi*g/2)
J0=S.Matrix([[0,-1],[1,0]])
sigma=S.Matrix([f,g]);V=S.Matrix([V1,V2])
assert all(S.expand(e)==0 for e in N-sigma*sigma.T*J0)
tauV=sigma*V.T*J0+V*sigma.T*J0
E=(a*(Rmid-theta*Rt)-tauV).applyfunc(S.expand)
assert S.expand(2*f*g*E[0,0]+g*g*E[0,1]-f*f*E[1,0])==0
K21=S.cancel(E[0,0]/(f*f));K11=S.cancel(-E[0,1]/(2*f*f))
assert not S.denom(K21).has(X,Y)
assert not S.denom(K11).has(X,Y)
assert S.cancel(K11+k*(2*A+B*c*c*z**5)/(12*B*c*c))==0
assert S.cancel(K21-L*k*(-11*A*c*z*z*X*X+5*A*X*Y+B*c*z**3*Y*Y)/(30*A*B*c**3*z**4))==0
K=S.Matrix([[K11,0],[K21,-K11]])
assert all(S.cancel(v)==0 for v in K*N-N*K-E)
print('PASS: both f² divisibilities, displayed K, and every entry of [K,n]=E.')

# Coefficient-frame checks only, not a full-actual-Serre-frame identification.
fy=S.expand((f/z**3).subs(z,-1/w));gy=S.expand((g*z**5).subs(z,-1/w))
V1y=S.expand((V1/z**7).subs(z,-1/w));V2y=S.expand((V2*z).subs(z,-1/w))
v1y=S.expand((v1/z**7).subs(z,-1/w));v2y=S.expand((v2*z).subs(z,-1/w))
assert S.expand(v2y+py*v1y-L*k*(11*X*X*Y**3/(12*c*c)-A*X**4*Y*w/(2*B*c*c)))==0
chiy=S.expand((chi/z**4).subs(z,-1/w))
assert S.expand(V1y-v1y-chiy*fy/2)==0
assert S.expand(V2y+py*V1y-v2y-py*v1y-chiy*(gy+py*fy)/2)==0
for var,components in [(z,[V1,S.expand(V2+px*V1)]),(w,[V1y,S.expand(V2y+py*V1y)])]:
    for comp in components:
        assert all(term.as_powers_dict().get(var,0)>=0 for term in S.Add.make_args(comp))
print('PASS: both complete triangular coefficient charts, including scalar transport.')

# EXACT generic stabilizer identity, no special source choice.
ff,gg,vv1,vv2,eps=S.symbols('ff gg vv1 vv2 eps')
ss=S.Matrix([ff,gg]);vv=S.Matrix([vv1,vv2]);nn=ss*ss.T*J0
wedge=ff*vv2-gg*vv1
P=S.eye(2)+eps*nn
assert all(S.expand(e)==0 for e in P*ss-ss)
assert all(S.expand(e)==0 for e in P*vv-vv+eps*wedge*ss)
def tt(v):return ss*v.T*J0+v*ss.T*J0
assert all(S.expand(e)==0 for e in tt(P*vv)-tt(vv)+2*eps*wedge*nn)
assert S.expand(ff*(P*vv)[1]-gg*(P*vv)[0]-wedge)==0
print('PASS: higher stabilizers preserve the wedge but change its Serre representative.')
print('Only a homogeneous local cancellation is proved; full actual K and beta4 are unclaimed.')
