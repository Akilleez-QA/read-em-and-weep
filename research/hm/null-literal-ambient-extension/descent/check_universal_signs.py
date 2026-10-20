"""Synthetic free-associative dual-number check, with no geometric inputs.
Checks linearized signs and all five cocycle equations. Nonlinear small-
extension coherence is proved in LEMMA.md, not certified by this test alone.
"""
from collections import defaultdict

def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
    q=defaultdict(int)
    for p in ps:
        for k,v in p.items(): q[k]+=v
    return clean(q)
def neg(p): return {k:-v for k,v in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r=defaultdict(int)
    for (a,w),c in p.items():
        for (b,z),d in q.items():
            if a+b<2: r[a+b,w+z]+=c*d
    return clean(r)
def atom(s): return {(0,(s,)):1}
one={(0,()):1}
x,y,z,w=map(atom,'xyzw')
def op(name,*args):
    # t times a normalized multilinear operation on classical words.
    choices=[((),1)]
    for p in args:
        choices=[(ws+(word,),c*v) for ws,c in choices
                 for (t,word),v in p.items() if t==0 and word]
    out=defaultdict(int)
    for ws,c in choices:
        label=name+'('+','.join(''.join(a) for a in ws)+')'
        out[1,(label,)]+=c
    return clean(out)
def m(i,a,b): return add(mul(a,b),op('u'+str(i),a,b))
def F(i,j,a): return add(a,op('v'+str(i)+str(j),a))
def A(i,j,k): return add(one,{(1,('a'+str(i)+str(j)+str(k),)):1})
def S(i,a,b,c): return sub(m(i,m(i,a,b),c),m(i,a,m(i,b,c)))
def H(i,j,a,b): return sub(F(i,j,m(j,a,b)),m(i,F(i,j,a),F(i,j,b)))
def K(i,j,k,a): return sub(m(i,F(i,j,F(j,k,a)),A(i,j,k)),m(i,A(i,j,k),F(i,k,a)))
def P(i,j,k,l): return sub(m(i,A(i,j,k),A(i,k,l)),m(i,F(i,j,A(j,k,l)),A(i,j,l)))
def b(cochain,args):
    r=mul(args[0],cochain(*args[1:]))
    for t in range(len(args)-1):
        term=cochain(*(args[:t]+(mul(args[t],args[t+1]),)+args[t+2:]))
        r=add(r,neg(term) if (t+1)%2 else term)
    term=mul(cochain(*args[:-1]),args[-1])
    return add(r,neg(term) if len(args)%2 else term)
def delta(fn,indices,*args):
    return add(*(neg(fn(*(indices[:t]+indices[t+1:]),*args)) if t%2
                 else fn(*(indices[:t]+indices[t+1:]),*args)
                 for t in range(len(indices))))
def check(label,lhs,rhs=None):
    assert sub(lhs,rhs or {})=={},label
    print('PASS',label)
check('Delta S = -bu',S(0,x,y,z),neg(b(lambda *a:op('u0',*a),(x,y,z))))
check('Delta H = delta u - bv',H(0,1,x,y),sub(sub(op('u1',x,y),op('u0',x,y)),b(lambda a:op('v01',a),(x,y))))
a={(1,('a012',)):1}
check('Delta K = delta v + ba',K(0,1,2,x),add(op('v12',x),neg(op('v02',x)),op('v01',x),sub(mul(x,a),mul(a,x))))
check('Delta P = -delta a',P(0,1,2,3),neg(delta(lambda i,j,k:sub(A(i,j,k),one),(0,1,2,3))))
check('bS=0',b(lambda *a:S(0,*a),(x,y,z,w)))
check('delta S+bH=0',add(delta(S,(0,1),x,y,z),b(lambda *a:H(0,1,*a),(x,y,z))))
check('delta H+bK=0',add(delta(H,(0,1,2),x,y),b(lambda a:K(0,1,2,a),(x,y))))
check('delta K+bP=0',add(delta(K,(0,1,2,3),x),b(lambda:P(0,1,2,3),(x,))))
check('delta P=0',delta(P,(0,1,2,3,4)))
