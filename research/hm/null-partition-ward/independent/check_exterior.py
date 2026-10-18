"""Independent exterior-chain controls; invented symbols only, no source imports."""
import itertools
import sympy as s
from collections import defaultdict

def plus(*terms):
    out=defaultdict(lambda:s.S.Zero)
    for a in terms:
        for k,v in a.items(): out[k]+=v
    return {k:s.expand(v) for k,v in out.items() if s.expand(v)!=0}
def scale(a,c): return {k:c*v for k,v in a.items()}
def wedge(a,b):
    out=defaultdict(lambda:s.S.Zero)
    for u,x in a.items():
        for v,y in b.items():
            if set(u)&set(v): continue
            sign=(-1)**sum(i>j for i in u for j in v)
            out[tuple(sorted(u+v))]+=sign*x*y
    return plus(out)
def product(vs):
    a={():s.S.One}
    for v in vs: a=wedge(a,v)
    return a
def boundary(a):
    out=defaultdict(lambda:s.S.Zero)
    for u,v in a.items():
        for h in range(len(u)): out[u[:h]+u[h+1:]]+=(-1)**h*v
    return plus(out)
def vectors(tag,n):
    r=s.symbols('r%s_0:%d'%(tag,n-1)); d=s.symbols('d%s_0:%d'%(tag,n-1))
    rr=tuple(r)+(1-sum(r),); dd=tuple(d)+(-sum(d),)
    return ({((tag,i),):rr[i] for i in range(n)}, {((tag,i),):dd[i] for i in range(n)})
def prism(tags,vec,wrong_sign=False):
    terms=[]
    for k,tag in enumerate(tags):
        vs=[vec[e][0] for e in tags]
        vs.insert(k+1,vec[tag][1])
        terms.append(scale(product(vs),1 if wrong_sign else (-1)**k))
    return plus(*terms)
def check(tags,n):
    vec={e:vectors(e,n) for e in tags}
    derivative=plus(*(product([vec[e][int(h==j)] for j,e in enumerate(tags)]) for h in range(len(tags))))
    dq=plus(*(scale(prism(tags[:h]+tags[h+1:],vec),(-1)**h) for h in range(len(tags))))
    qd=boundary(prism(tags,vec))
    if plus(derivative,scale(plus(dq,qd),-1)): raise RuntimeError('chain homotopy failed')
    if not derivative: raise RuntimeError('false-zero mutation survived')
    if len(tags)>1:
        if not plus(derivative,scale(dq,-1)): raise RuntimeError('dropped defect mutation survived')
        if not plus(derivative,scale(plus(dq,scale(qd,-1)),-1)): raise RuntimeError('defect sign mutation survived')
    # The mixed-partition finite prism has the same derivative at equal partitions.
    t=s.Symbol('t'); terms=[]
    for k,tag in enumerate(tags):
        vs=[vec[e][0] if j<=k else plus(vec[e][0],scale(vec[e][1],t)) for j,e in enumerate(tags)]
        vs.insert(k+1,plus(vec[tag][0],scale(vec[tag][1],t)))
        terms.append(scale(product(vs),(-1)**k))
    dt={u:s.diff(v,t).subs(t,0) for u,v in plus(*terms).items()}
    if plus(dt,scale(prism(tags,vec),-1)): raise RuntimeError('parameter derivative failed')
for degree in range(5): check(tuple(reversed(range(degree+1))),2)
for degree in range(3): check(tuple(range(degree+1)),3)
print('PASS: independent exterior-chain identities, degrees 0..4; three-letter fibers 0..2; reversed ordering; mixed-prism derivative; false-zero and defect mutations')
