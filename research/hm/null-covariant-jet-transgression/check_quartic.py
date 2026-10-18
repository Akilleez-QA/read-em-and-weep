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
H={p:vec('H'+''.join(map(str,p))) for p in [(1,3),(1,4),(2,3),(2,4)]}
J={p:vec('J'+''.join(map(str,p))) for p in H}
get=lambda jets,a,b:jets[tuple(sorted((a,b)))]
pairs=[((1,2),(3,4)),((3,4),(1,2))]
entries=[(1,3,2,4,1),(1,4,2,3,-1),(2,3,1,4,-1),(2,4,1,3,1)]
K={p:sc(F(1,4),br(L[p[0]],L[p[1]])) for p,r in pairs}
X={p:sc(F(1,4),br(U[p[0]],U[p[1]])) for p,r in pairs}
KG={p:sc(F(1,4),br(T[p[0]],T[p[1]])) for p,r in pairs}
Delta={p:d(U[p[0]],L[p[1]])-d(U[p[1]],L[p[0]]) for p,r in pairs}
def jet(c,r,jets,curr):
    i,j=r
    return sc(F(1,4),add(br(get(jets,c,i),curr[j]),br(curr[i],get(jets,c,j))))
def q(p,r,preferred=False):
    a,b=p
    yh=lambda c:jet(c,r,J,U)
    zh=lambda c:jet(c,r,H,L)
    if preferred:
        y,z=yh,zh
        cubic=add(sc(d(U[a],X[r]),L[b]),sc(-d(U[b],X[r]),L[a]),sc(d(L[b],K[r]),U[a]),sc(-d(L[a],K[r]),U[b]))
    else:
        y=lambda c:sub(yh(c),sc(F(1,2),br(U[c],X[r])))
        z=lambda c:sub(zh(c),sc(F(1,2),br(L[c],K[r])))
        D=sub(X[r],K[r]); S=add(X[r],K[r])
        cubic=add(sc(d(U[a],D),L[b]),sc(-d(U[b],D),L[a]),sc(-Delta[p],D),sc(d(L[b],S),U[a]),sc(-d(L[a],S),U[b]))
    return sc(F(1,4),add(cubic,br(y(a),L[b]),neg(br(y(b),L[a])),br(U[a],z(b)),neg(br(U[b],z(a)))))
C=add(*(sc(F(e,8),add(br(J[a,b],H[c,d_]),sc(d(U[a],U[b]),H[c,d_]),sc(d(L[c],L[d_]),J[a,b]))) for a,b,c,d_,e in entries))
quad=sc(F(1,2),add(br(X[1,2],K[3,4]),br(X[3,4],K[1,2])))
# Original full noncentral gerbe plus both F=b-c branches, with independent b symbols.
bger={p:P({('b'+str(p),):F(1)}) for p,r in pairs}
M0=add(quad,*(q(p,r) for p,r in pairs),C,*(sc(-bger[p],KG[r]) for p,r in pairs))
Ralg=add(M0,*(sc(bger[p]-F(1,4)*Delta[p],KG[r]) for p,r in pairs))
R22=add(sc(F(1,2),add(br(X[1,2],K[3,4]),br(X[3,4],K[1,2]))),*(sc(-F(1,16)*Delta[p],add(br(L[r[0]],U[r[1]]),br(U[r[0]],L[r[1]]))) for p,r in pairs))
R31=add(*(sc(F(1,32),add(br(U[b],br(L[a],br(U[i],U[j]))),neg(br(U[a],br(L[b],br(U[i],U[j])))),br(L[a],br(U[b],br(L[i],L[j]))),neg(br(L[b],br(U[a],br(L[i],L[j])))))) for (a,b),(i,j) in pairs))
Q4=add(R22,R31)

BL={p:br(L[p[0]],L[p[1]]) for p,r in pairs}
BU={p:br(U[p[0]],U[p[1]]) for p,r in pairs}
C4=sc(F(1,32),sub(br(U[3],br(BL[1,2],L[4])),br(U[4],br(BL[1,2],L[3]))))
R31threeU=add(*(sc(F(1,32),sub(br(U[b],br(L[a],BU[i,j])),br(U[a],br(L[b],BU[i,j])))) for (a,b),(i,j) in pairs))
anti=lambda x,y,z:add(br(x,br(y,z)),br(y,br(x,z)))
R13new=sc(F(1,32),add(br(L[1],br(U[2],BL[3,4])),neg(br(L[2],br(U[1],BL[3,4]))),anti(L[3],U[4],BL[1,2]),neg(anti(L[4],U[3],BL[1,2]))))
W=add(Q4,C4)
eq('full quartic collection',W,add(R22,R31threeU,R13new))
trace34=sc(F(1,16),add(sc(d(L[4],BL[1,2]),U[3]),sc(-d(L[3],BL[1,2]),U[4]),sc(d(U[3],BL[1,2]),L[4]),sc(-d(U[4],BL[1,2]),L[3]),sc(-2*Delta[3,4],BL[1,2])))
eq('changed pair trace collection',R13new,add(sc(F(1,32),sub(br(L[1],br(U[2],BL[3,4])),br(L[2],br(U[1],BL[3,4])))),trace34))
def sector(v,word):
    return tuple(P({m:c for m,c in x.items() if all(t[0]==word[int(t[1])-1] for t in m)}) for x in v)
zero=(P(),P(),P())
from itertools import product
for word in map(''.join,product('LU',repeat=4)):
    if word in ('LLUL','LLLU'):
        neq('changed assignment '+word,sector(W,word),sector(Q4,word))
    else:
        eq('unchanged assignment '+word,sector(W,word),sector(Q4,word))
    if word in ('LLLL','UUUU'):
        eq('pure assignment zero '+word,sector(W,word),zero)
    else:
        neq('mixed assignment survives '+word,sector(W,word),zero)
for m,value in [(('L10','L21','L40','U32'),F(1,8)),(('L10','L21','L30','U42'),F(-1,8))]:
    m=tuple(sorted(m))
    eq('new coefficient '+str(m),W[0].get(m,0),value)
    eq('old coefficient absent '+str(m),Q4[0].get(m,0),0)
print(json.dumps({'status':'PASS','checks':checks,'method':'Universal exact scalar-polynomial coefficient checking, with multidegree projections only; no current/jet values or matrices instantiated.'},indent=2))
