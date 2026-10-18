"""Invented free alternating cochains only; no actual owners, source, or matrix products."""
import itertools
from collections import defaultdict
import sympy as s

def add(out, vertices, coefficient):
    if len(set(vertices)) != len(vertices): return
    parity=(-1)**sum(vertices[i]>vertices[j] for i in range(len(vertices)) for j in range(i+1,len(vertices)))
    out[tuple(sorted(vertices))]+=parity*coefficient

def weights(tag, bit, dotted=False):
    r,d=s.symbols('r%d d%d'%(tag,tag))
    return (d if bit==0 else -d) if dotted else (r if bit==0 else 1-r)

def pi_dot(tags):
    out=defaultdict(lambda:0)
    for bits in itertools.product(range(2),repeat=len(tags)):
        vertices=tuple(zip(tags,bits))
        coefficient=sum(s.prod(weights(t,b,i==h) for i,(t,b) in enumerate(vertices)) for h in range(len(tags)))
        add(out,vertices,coefficient)
    return out

def q_terms(tags):
    for k in range(len(tags)):
        for bits in itertools.product(range(2),repeat=len(tags)+1):
            expanded=tags[:k+1]+tags[k:k+1]+tags[k+1:]
            vertices=tuple(zip(expanded,bits))
            coefficient=(-1)**k*s.prod(weights(t,b,i==k+1) for i,(t,b) in enumerate(vertices))
            yield vertices,coefficient

def rhs(tags):
    out=defaultdict(lambda:0)
    for h in range(len(tags)):
        for vertices,coef in q_terms(tags[:h]+tags[h+1:]): add(out,vertices,(-1)**h*coef)
    for vertices,coef in q_terms(tags):
        for h in range(len(vertices)): add(out,vertices[:h]+vertices[h+1:],(-1)**h*coef)
    return out

for q in range(5):
    tags=tuple(range(q+1)); left=pi_dot(tags);right=rhs(tags)
    for key in set(left)|set(right):
        if s.expand(left[key]-right[key])!=0: raise AssertionError((q,key))
    # This differentiated projection is generally nonzero.
    if not any(s.expand(v)!=0 for v in left.values()): raise AssertionError('false zero mutation')
print('PASS: differentiated partition homotopy in degrees 0..4, free alternating coefficients; false-zero mutation rejected')
