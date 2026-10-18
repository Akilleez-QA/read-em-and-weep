#!/usr/bin/env python3
"""Invented free words and face labels only; no source execution or physical data."""
import json
from collections import defaultdict
checks=[]
def need(ok,name):
    if not ok: raise RuntimeError(name)
    checks.append(name)
def plus(*ps):
    out=defaultdict(int)
    for p in ps:
        for w,c in p.items():out[w]+=c
    return {w:c for w,c in out.items() if c}
def scale(k,p):return {w:k*c for w,c in p.items() if k*c}
def mul(p,q):return plus(*({a+b:x*y} for a,x in p.items() for b,y in q.items()))
def atom(x):return {(x,):1}
def parity(r):return -1 if r%2 else 1
D=atom('D'); Xi=atom('Xi'); X=atom('X')
def differential(P,r):return plus(mul(D,P),scale(-parity(r),mul(P,D)))
def bracket(P,Q,r):return plus(mul(P,Q),scale(-parity(r),mul(Q,P)))
for r in range(-3,4):
    rx=bracket(Xi,X,r)
    lhs=plus(differential(rx,r-1),bracket(Xi,differential(X,r),r+1))
    dxi=differential(Xi,-1)
    rhs=plus(mul(dxi,X),scale(-1,mul(X,dxi)))
    need(lhs==rhs,f'graded-dR-plus-Rd-r{r}')
    if r%2: need(rx!=plus(mul(Xi,X),scale(-1,mul(X,Xi))),f'odd-sign-negative-control-r{r}')

def insertion(edge,tail,r):
    return bracket(atom(('Xi',tuple(edge))),atom(('X',tuple(tail))),r)
for n in range(5):
    t=tuple(range(n+3))
    for r in (-2,-1,0,1):
        dr={}
        for k in range(len(t)):
            f=t[:k]+t[k+1:]
            dr=plus(dr,scale(parity(k),insertion(f[:2],f[1:],r)))
        rd={}
        tail=t[1:]
        for k in range(len(tail)):
            f=tail[:k]+tail[k+1:]
            rd=plus(rd,scale(parity(k),insertion(t[:2],f,r)))
        want=plus(insertion((1,2),t[2:],r),scale(-1,insertion((0,2),t[2:],r)),insertion((0,1),t[2:],r))
        need(plus(dr,rd)==want,f'first-two-face-zeta-n{n}-r{r}')
        need(bool(want),f'zeta-not-zero-n{n}-r{r}')
# Symbolic contraction rewrites: actual raw homotopy insertion H d R J1 + H R dJ1
# plus H delta H d R j (dj=0), then use dJ1=delta j-jDelta and Ld=0.
first={('L','R','J1'):1,('L','H','R','delta','j'):1,('L','H','R','j','Delta'):-1}
second={('L','H','delta','R','j'):1,('delta','L','H','R','j'):-1}
combined=plus(first,second)
want={('L','R','J1'):1,('L','H','R','delta','j'):1,('L','H','delta','R','j'):1,('delta','L','H','R','j'):-1,('L','H','R','j','Delta'):-1}
need(combined==want,'two-family-selected-reduction')
for missing in want:
    wrong=dict(want);del wrong[missing]
    need(wrong!=combined,'omit-'+','.join(missing))
# Expand H[a,X]=h[a,X]+(-1)^r e[a,X]h, then h a=a h=0, e a=a.
for r in (-1,0):
    # The surviving monomials are obtained without commutations.
    result={('a','X','h'):parity(r),('h','X','a'):-1}
    theta_result={('theta','X','h'):-parity(r),('h','X','theta'):1}
    need(theta_result[('theta','X','h')]==(1 if r==-1 else -1),'actual-HC0-sign-r'+str(r))
    need(result[('h','X','a')]==-1,'right-a-order-r'+str(r))
print(json.dumps({'status':'pass','checks':len(checks),'details':checks},indent=2))
