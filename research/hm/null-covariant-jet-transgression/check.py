#!/usr/bin/env python3
"""Universal scalar-coordinate polynomial identities; no source imports or values."""
from fractions import Fraction as F
import json
class P(dict):
    def __add__(a,b):
        if not isinstance(b,P): b=P({():F(b)}) if b else P()
        c=P(a)
        for k,v in b.items():
            c[k]=c.get(k,0)+v
            if not c[k]: del c[k]
        return c
    __radd__=__add__
    def __neg__(a): return P({k:-v for k,v in a.items()})
    def __sub__(a,b): return a+-b
    def __mul__(a,b):
        if not isinstance(b,P): b=P({():F(b)}) if b else P()
        c=P()
        for k,v in a.items():
            for l,w in b.items():
                m=tuple(sorted(k+l)); c[m]=c.get(m,0)+v*w
        return P({k:v for k,v in c.items() if v})
    __rmul__=__mul__
def vec(name): return tuple(P({(name+str(i),):F(1)}) for i in range(3))
def add(*vs): return tuple(sum((v[i] for v in vs),P()) for i in range(3))
def sc(c,v): return tuple(c*x for x in v)
def neg(v): return sc(-1,v)
def sub(v,w): return add(v,neg(w))
def d(v,w): return 2*v[0]*w[0]+v[1]*w[2]+v[2]*w[1]
def br(v,w): return (v[1]*w[2]-v[2]*w[1],2*(v[0]*w[1]-v[1]*w[0]),2*(v[2]*w[0]-v[0]*w[2]))
checks=[]
def eq(label,a,b):
    if a!=b: raise RuntimeError('FAILED: '+label)
    checks.append(label)
def neq(label,a,b):
    if a==b: raise RuntimeError('MUTATION SURVIVED: '+label)
    checks.append(label)

L={i:vec('L'+str(i)) for i in range(1,5)}
U={i:vec('U'+str(i)) for i in range(1,5)}
T={i:add(L[i],U[i]) for i in L}
H={(a,b):vec('H'+str(a)+str(b)) for a in range(1,5) for b in range(a,5)}
J={(a,b):vec('J'+str(a)+str(b)) for a in range(1,5) for b in range(a,5)}
get=lambda A,a,b:A[tuple(sorted((a,b)))]
entries=[(1,3,2,4,1),(1,4,2,3,-1),(2,3,1,4,-1),(2,4,1,3,1)]
# Formal symmetric remainder of second covariant derivatives, not physical third jets.
R={(1,2,d_):vec('R12'+str(d_)) for d_ in (3,4)}
zero=(P(),P(),P())
S=[]; M=[]; C=[]; div=[]; mismatch=[]
for a,b,c,d_,e in entries:
    h,j=get(H,c,d_),get(J,a,b)
    aa=d(T[a],T[b])-d(L[a],L[b]); bb=d(T[c],T[d_])-d(U[c],U[d_])
    linear=add(sc(aa,h),sc(bb,j),sc(-d(U[a],h),L[b]),sc(-d(U[b],h),L[a]),sc(-d(j,L[c]),U[d_]),sc(-d(j,L[d_]),U[c]))
    shift=sc(F(1,2),br(T[a],U[b]))
    S.append(sc(F(e,8),add(br(j,h),linear)))
    collected=add(sc(aa,h),sc(bb,j),sc(-d(U[a],h),L[b]),sc(d(U[b],h),U[a]),sc(-d(T[a],h),U[b]),sc(-d(j,L[c]),U[d_]),sc(-d(j,L[d_]),U[c]))
    eq('collected transport mismatch '+str((a,b,c,d_)),collected,add(linear,br(shift,h)))
    M.append(sc(F(e,8),collected))
    curvature=sc(F(-1,4),br(L[a],L[c]))
    covH=add(R[1,2,d_],sc(F(1,2),br(curvature,L[d_])))
    div.append(sc(F(e,8),add(br(sub(j,shift),h),br(U[b],covH))))
    C.append(sc(F(e,64),br(U[b],br(br(L[a],L[c]),L[d_]))))
    mismatch.append(sc(F(e,8),br(shift,h)))
S2=add(*S); M2=add(*M); C4=add(*C); divergence=add(*div)
eq('complete S2 covariant divergence plus curvature and linear jets',S2,add(divergence,C4,M2))
neq('curvature omission rejected',S2,add(divergence,M2))
neq('curvature sign reversal rejected',S2,add(divergence,neg(C4),M2))
neq('transport mismatch omission rejected',S2,sub(add(divergence,C4,M2),add(*mismatch)))
neq('linear-jet omission rejected',S2,add(divergence,C4))
# Coefficient extraction, NOT a numerical/current/jet specialization.
mon=tuple(sorted(('U10','U30','H240')))
eq('surviving current-jet coefficient is 1/4',M2[0].get(mon),F(1,4))
# Derive both midpoint curvatures with every transport bracket retained.
for a,c in ((1,2),(3,4)):
    DaLc=sub(get(H,a,c),sc(F(1,2),br(L[a],L[c])))
    DcLa=sub(get(H,c,a),sc(F(1,2),br(L[c],L[a])))
    DaUc=sub(sub(get(J,a,c),br(L[a],U[c])),sc(F(1,2),br(U[a],U[c])))
    DcUa=sub(sub(get(J,c,a),br(L[c],U[a])),sc(F(1,2),br(U[c],U[a])))
    fp=add(sc(F(1,2),sub(DaLc,DcLa)),sc(F(1,4),br(L[a],L[c])))
    qa=add(L[a],sc(F(1,2),U[a])); qc=add(L[c],sc(F(1,2),U[c]))
    fq=add(sub(DaLc,DcLa),sc(F(1,2),sub(DaUc,DcUa)),br(qa,qc))
    eq('L midpoint curvature '+str((a,c)),fp,sc(F(-1,4),br(L[a],L[c])))
    eq('transported B midpoint curvature '+str((a,c)),fq,sc(F(-1,4),br(U[a],U[c])))
print(json.dumps({'status':'PASS','checks':checks,'method':'Exact universal scalar-polynomial coefficient identities; no matrices, source imports, or current/jet values instantiated.'},indent=2))
