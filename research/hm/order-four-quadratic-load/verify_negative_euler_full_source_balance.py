"""Full c companion of every quartic symbol annihilating Cartan, all coefficients free."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import sympy as s
from universal_source_balance_helpers import *

S,T=s.symbols('S T'); ell=u*T-w*S
Fmat=s.Matrix(4,4,s.symbols('f0:16'))
def coeff3(poly):
 po=s.Poly(s.expand(poly),S,T)
 return s.Matrix([po.coeff_monomial(S**(3-i)*T**i) for i in range(4)])
def fc(poly):return Kinc*Fmat*coeff3(poly)
ks=s.symbols('kappa0:60')
Rspin=s.Matrix(6,2,lambda i,j:sum(ks[10*i+5*j+l]*u**(4-l)*w**l for l in range(5)))
K=Rspin*cliff
zz=s.symbols('zz0:3'); zzp=sum(zz[i]*S**(2-i)*T**i for i in range(3))
Z=adds(putp(fc(-T*zzp),(3,)),putp(fc(S*zzp),(4,)))
Cfull=[contract(coords,ff) for ff in Z]
TC=fullT(K,4,Cfull)
F3=-up*adj6(K)*low*getY(Cfull,(3,))
F4=-up*adj6(K)*low*getY(Cfull,(4,))
Sneg=u*F3+w*F4
zero_matrix(getY(TC,(3,))-(5*F3-Sneg.diff(u))/4)
zero_matrix(getY(TC,(4,))-(5*F4-Sneg.diff(w))/4)
beta=-(cliff*(adj6(K.diff(u))*low*getY(Cfull,(4,))-adj6(K.diff(w))*low*getY(Cfull,(3,))))/4
Lbeta=putY(up*spin*beta,())
rhs=[scale(-1,contract(coords,wedge(ff,omega))) for ff in Lbeta]
eqvec(TC,rhs)
Pc=-beta/3
eqvec(TC,B(Pc))
Pss=cliff*Rspin
Pu=-J.inv()*Pss.T*J
eqvec(fullT(K,4,B(p)),B(Pu*p))
# With the forced U-row source, all B companions cancel exactly.
am,bm,cm=s.symbols('a_m b_m c_m',nonzero=True)
Sc=cm*Pc/bm
eqvec(adds(sc(cm,TC),sc(-bm,B(Sc)),sc(-am,A(Sc))),sc(-am*cm/bm,A(Pc)))
zero_matrix(getp(TC))
for ff in TC:assert not contract(coords,ff)
zero_matrix(s.Matrix(1,3,[x,y,z])*s.Matrix(3,2,lambda i,j:(up*spin*beta)[2*i+j])- (M*beta).T/3)
# Entire mixed coefficient determines beta by negative Koszul extraction.
recovered=cliff*low*(getY(TC,(4,)).diff(u)-getY(TC,(3,)).diff(w))/5
zero_matrix(recovered-beta)
print('PASS: all60 quartic Cartan-annihilating coefficients and all16 cubic marking coefficients give the exact full U/c B-companion balance, signs, closure, and regular beta recovery.')
