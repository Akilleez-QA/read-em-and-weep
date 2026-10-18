#!/usr/bin/env python3
"""Independent universal-coefficient audit; no physical values or matrix products."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy,json
with redirect_stdout(StringIO()):
    s=runpy.run_path(str(Path(__file__).resolve().with_name('check.py')))
P,F,vec,add,sc,sub,d,br=[s[k] for k in ('P','F','vec','add','sc','sub','d','br')]
checks=[]
def eq(n,a,b):
    if a!=b: raise RuntimeError('FAIL: '+n)
    checks.append(n)
def neq(n,a,b):
    if a==b: raise RuntimeError('MUTATION SURVIVED: '+n)
    checks.append(n)
L,U,T,H,J,get,entries=[s[k] for k in ('L','U','T','H','J','get','entries')]
W=vec('W'); DW={a:vec('DW'+str(a)) for a in L}
# Full kernel W is unrestricted, and its physical coefficient derivatives are independent.
expected=P(); direct=P(); ordinary_flux=P(); transport_flux=P()
for a,b,c,e_,sign in entries:
    h,j=get(H,c,e_),get(J,a,b)
    aa=d(T[a],T[b])-d(L[a],L[b]); bb=d(T[c],T[e_])-d(U[c],U[e_])
    p=sc(F(1,2),L[a]); nablaW=add(DW[a],br(p,W))
    WH=add(sc(aa,W),sc(-d(W,L[b]),U[a]),sc(d(W,U[a]),U[b]),sc(-d(W,U[b]),T[a]),sc(-1,br(nablaW,U[b])))
    WJ=add(sc(bb,W),sc(-d(W,U[e_]),L[c]),sc(-d(W,U[c]),L[e_]))
    expected+=F(sign,8)*(d(h,WH)+d(j,WJ))
    direct+=F(sign,8)*(-d(nablaW,br(U[b],h)))
    ordinary_flux+=F(sign,8)*(-d(DW[a],br(U[b],h)))
    transport_flux+=F(sign,8)*(-d(br(p,W),br(U[b],h)))
eq('full nonconstant dual-kernel adjoint',expected,d(W,s['M2'])+direct)
eq('ordinary physical derivative and connection adjoint both retained',direct,ordinary_flux+transport_flux)
neq('kernel derivative omission rejected',expected,d(W,s['M2'])+transport_flux)
neq('kernel connection omission rejected',expected,d(W,s['M2'])+ordinary_flux)
neq('kernel derivative sign reversal rejected',expected,d(W,s['M2'])-direct)
# Differentiate moving conjugation: D(A^-1 X A)=A^-1(DX)A+[A^-1XA,L].
# Check the resulting transported Maurer-Cartan and both symmetric midpoint jets.
for a,b in ((1,2),(1,3),(2,4),(3,4)):
    h,j=get(H,a,b),get(J,a,b)
    DL=sub(h,sc(F(1,2),br(L[a],L[b])))
    DU=sub(sub(j,br(L[a],U[b])),sc(F(1,2),br(U[a],U[b])))
    eq('A midpoint jet '+str((a,b)),add(DL,sc(F(1,2),br(L[a],L[b]))),h)
    eq('transported B midpoint jet '+str((a,b)),add(DU,br(add(L[a],sc(F(1,2),U[a])),U[b])),j)
    eq('shift between midpoint connections '+str((a,b)),add(DU,sc(F(1,2),br(L[a],U[b]))),sub(j,sc(F(1,2),br(T[a],U[b]))))
    neq('frozen transport rejected '+str((a,b)),add(sub(j,sc(F(1,2),br(U[a],U[b]))),br(add(L[a],sc(F(1,2),U[a])),U[b])),j)
x,y,z=vec('x'),vec('y'),vec('z')
eq('trace connection skew adjoint',d(x,br(y,z)),-d(br(y,x),z))
eq('rank-two Fierz normalization',br(x,br(y,z)),sc(2,sub(sc(d(x,y),z),sc(d(x,z),y))))
print(json.dumps({'status':'PASS','checks':checks,'scope':'Universal scalar coefficients only; no physical matrix-polynomial products, source/model/owner/jet values, or production imports.'},indent=2))
