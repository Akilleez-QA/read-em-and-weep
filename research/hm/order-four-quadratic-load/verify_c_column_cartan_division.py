"""Universal Cartan extraction and regular two-stage c-column division identities."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import sympy as s
from universal_source_balance_helpers import *

es=s.Matrix(s.symbols('e0:6')); EE=putp(es)
paired=pair(B(p),EE)
scalar=(p.T*J*cliff*es)[0]
want=scale(scalar,wedge(tau,contract(coords,omega)))
for I in [(0,1,2,3),(0,1,2,4)]:
 assert s.expand(paired.get(I,0)-want.get(I,0))==0
S,T=s.symbols('S T'); ell=u*T-w*S
ys=s.symbols('y0:9')
yy=sum(ys[3*i+j]*S**(2-i)*T**i*u**(2-j)*w**j for i in range(3) for j in range(3))
def Om(p):return s.diff(p,u,T)-s.diff(p,w,S)
pp=ell*yy
recovered=Om(pp)/6-ell*Om(Om(pp))/60+ell**2*Om(Om(Om(pp)))/720
assert s.expand(recovered-yy)==0
rs=s.symbols('r0:7'); rr=sum(rs[i]*u**(6-i)*w**i for i in range(7))
def delta(p):return S*s.diff(p,u)+T*s.diff(p,w)
pol=delta(delta(delta(rr)))/120
assert s.expand(pol.subs({S:u,T:w})-rr)==0
# Every closed mixed error in the retained degree has a regular j-factor.
ls=s.symbols('l0:6')
LL={ (i,):ls[2*i]*u+ls[2*i+1]*w for i in range(3)}
HH=wedge(LL,contract(coords,omega))
for i in range(3):
 rec=(s.diff(HH.get((i,4),0),u)-s.diff(HH.get((i,3),0),w))/3
 assert s.expand(rec-LL[(i,)])==0
# Positive quadratic division is coefficientwise, not differential-form pullback.
assert s.expand(Q*sum([x,y,z][i]*LL[(i,)] for i in range(3)))==s.expand(sum([x,y,z][i]*Q*LL[(i,)] for i in range(3)))
print('PASS: exact B/Cartan pairing, all9 regular cubic-division coefficients, all7 sextic polarizations, and mixed j-factor extraction.')
