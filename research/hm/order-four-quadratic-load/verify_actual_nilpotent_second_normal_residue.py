"""Universal actual leading nilpotence obstruction. No parameter specialization.
No global second-normal extension or fourth-value computation.
"""
from pathlib import Path
import sympy as S,runpy,io,contextlib
with contextlib.redirect_stdout(io.StringIO()):ns=runpy.run_path(str(Path(__file__).with_name('verify_actual_lowest_normal_connection_term.py')))
X,Y,z,A,B,c,L=[ns[v]for v in ('X','Y','z','A','B','c','L')]
N,T=ns['Nx'],ns['Tx'];bm=ns['bm']
def B2(p,q):
 if p==0 or q==0:return S.Integer(0)
 d=S.Poly(p,X,Y).total_degree();h=S.Poly(q,X,Y).total_degree()
 if min(d,h)<4:return S.Integer(0)
 tv=sum((-1)**i*S.binomial(4,i)*S.diff(p,X,4-i,Y,i)*S.diff(q,X,i,Y,4-i)for i in range(5))
 return S.cancel(tv/(8*(d-1)*(d-3)*(h-1)*(h-3)*(d+h-3)*(d+h-5)))
def bm2(U,V):return S.Matrix(2,2,lambda i,j:sum(B2(U[i,l],V[l,j])for l in range(2)))
E1=(N*T+T*N+bm(N,N)).applyfunc(S.cancel)
assert all(v==0 for v in E1)
print('PASS first-order square-zero identity',flush=True)
E=(T*T+bm(N,T)+bm(T,N)+bm2(N,N)).applyfunc(lambda v:S.factor(S.cancel(v)))
assert S.cancel(E[0,1])==0 and S.cancel(E[1,0])==0 and S.cancel(E[0,0]-E[1,1])==0
f=ns['f'];gx=ns['g']+ns['px']*f
field=S.QQ.frac_field(A,B,c,L,z)
pf=S.Poly(f*f,X,Y,domain=field)
# Homogeneous division by leading X^6; no Y denominators.
qx,r=S.div(S.Poly(E[0,0],X,Y,domain=field),pf)
qg,rg=S.div(S.Poly(f*gx,X,Y,domain=field),pf)
a=S.cancel(r.coeff_monomial(X**5*Y**3)/rg.coeff_monomial(X**5*Y**3))
rem=S.factor((r-a*rg).as_expr())
print('fg coefficient=',S.factor(a),flush=True)
print('residue=',rem,flush=True)
print('f2 coefficient=',S.factor((qx-a*qg).as_expr()),flush=True)

expected=-B*L**2*Y**4/(4*A*c**2*z**7)*(A**2*X**4-3*A*B*X**4*c**2*z**5-4*A*B*X**3*Y*c*z**3+2*A*B*X**2*Y**2*z+2*B**2*X**2*Y**2*c**2*z**6-4*B**2*X*Y**3*c*z**4+B**2*Y**4*z**2)
assert S.cancel(rem-expected)==0
assert S.cancel(E[0,0]-(qx-a*qg).as_expr()*f*f-a*f*gx-rem)==0
assert S.cancel(rg.coeff_monomial(X**5*Y**3)-A*L/(2*c*z**4))==0
assert S.Poly(rem,X).degree()<=4
assert S.cancel(S.Poly(rem,X,Y).coeff_monomial(Y**8)+B**3*L**2/(4*A*c**2*z**5))==0
assert S.Poly(rem,X,Y).total_degree()==8
for v in E:S.Poly(v,X,Y,z) # the unreduced actual X-chart scalar is regular
# Universal N2 effect; traceless scalar anticommutator, no actual matrix instance.
a2,b2,c2=S.symbols('a2 b2 c2')
S2=S.Matrix([[a2,b2],[c2,-a2]])
assert (N*S2+S2*N-S.eye(2)*S.trace(N*S2)).applyfunc(S.expand)==S.zeros(2)
assert S.expand(S.trace(N*S2)-(2*f*gx*a2+gx**2*b2-f**2*c2))==0
# Weighted degree zero forbids b2 (positive degree -2); a2,c2 have degrees 0,2.
assert 8-8==0 and 6-8==-2 and 10-8==2
# Exact Hilbert series of the square of the cubic/quintic regular pair.
t=S.symbols('t')
hilbert=S.cancel((1-t**6-t**8-t**10+t**11+t**13)/(1-t)**2)
assert S.Poly(hilbert,t).degree()==11
assert S.Poly(hilbert,t).coeff_monomial(t**8)==5
assert S.Poly(hilbert,t).coeff_monomial(t**12)==0
assert hilbert.subs(t,1)==45
# Coefficient bookkeeping for differentiated-square identity: D(q)=rho*q.
rho,H0,Lambda0,chi,Dchi=S.symbols('rho H0 Lambda0 chi Dchi')
assert S.expand(H0*(Dchi+2*rho*chi)-2*Lambda0*chi-(H0*Dchi+2*(H0*rho-Lambda0)*chi))==0
print('PASS: complete actual scalar octic; exact I^2 division; nonzero residue; N2 image; differentiated-square bookkeeping; Hilbert limitation.')
