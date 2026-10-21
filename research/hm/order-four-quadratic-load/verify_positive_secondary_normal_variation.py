#!/usr/bin/env python3
"""Formal graded-commutator differential identities, with no HM coefficients."""
from collections import defaultdict
DEG={'eta':1,'c':1,'b':0,'tau':1,'kappa':0,'dkappa':1,
     'lam':0,'dlam':1,'h':0,'a':0}
CENTRAL={'a','h'}
def normal(w):
    return tuple(sorted(x for x in w if x in CENTRAL))+tuple(x for x in w if x not in CENTRAL)
def clean(p):
    q=defaultdict(int)
    for w,n in p.items(): q[normal(w)]+=n
    return {w:n for w,n in q.items() if n}
def atom(x): return {(x,):1}
def add(*ps):
    q=defaultdict(int)
    for p in ps:
        for w,n in p.items(): q[w]+=n
    return clean(q)
def scale(p,n): return clean({w:v*n for w,v in p.items()})
def mul(p,q):
    out=defaultdict(int)
    for w,n in p.items():
        for v,m in q.items(): out[w+v]+=n*m
    return clean(out)
def degree(p):
    ds={sum(DEG[x] for x in w) for w in p}
    assert len(ds)==1
    return ds.pop()
def bracket(p,q):
    return add(mul(p,q),scale(mul(q,p),-(-1)**(degree(p)*degree(q))))
eta,c,b,tau,kappa,dkappa,lam,dlam,h,a=map(atom,
    ['eta','c','b','tau','kappa','dkappa','lam','dlam','h','a'])
D={'eta':{},'c':{},'b':mul(h,c),'tau':scale(bracket(eta,c),-1),
   'kappa':dkappa,'dkappa':{},'lam':dlam,'dlam':{},'h':{},'a':{}}
def diff(p):
    out={}
    for w,n in p.items():
        before=0
        for i,x in enumerate(w):
            term=mul(mul({w[:i]:1},D[x]),{w[i+1:]:1})
            out=add(out,scale(term,n*(-1)**before))
            before+=DEG[x]
    return out
Y=add(mul(h,tau),scale(bracket(eta,b),-1))
assert diff(Y)=={}
# c -> c+d kappa; b -> b+h kappa; tau -> tau+[eta,kappa].
bp=add(b,mul(h,kappa)); tp=add(tau,bracket(eta,kappa)); cp=add(c,dkappa)
assert add(diff(bp),scale(mul(h,cp),-1))=={}
assert add(diff(tp),bracket(eta,cp))=={}
Yp=add(mul(h,tp),scale(bracket(eta,bp),-1))
assert add(Yp,scale(Y,-1))=={}
# eta -> eta+d lambda; tau -> tau-[lambda,c].
ep=add(eta,dlam); tp=add(tau,scale(bracket(lam,c),-1))
assert add(diff(tp),bracket(ep,c))=={}
Yp=add(mul(h,tp),scale(bracket(ep,b),-1))
assert add(Yp,scale(Y,-1),diff(bracket(lam,b)))=={}
# Coefficient twists, separate from cohomological degrees.
TW={'eta':-2,'c':2,'b':4,'tau':0,'kappa':2,'dkappa':2,
    'lam':-2,'dlam':-2,'h':2,'a':2}
assert {sum(TW[x] for x in w) for w in Y}=={2}
assert {sum(TW[x] for x in w) for w in mul(a,Y)}=={4}
print('PASS: graded cocycle identity, both explicit representative changes,')
print('their lift equations, coboundary formula, and independent polynomial twists.')
print('Only universal formal identities are checked; no actual coefficients or ranks.')
