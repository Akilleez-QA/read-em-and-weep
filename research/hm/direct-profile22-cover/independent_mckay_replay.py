"""Independent integer McKay-ring replay of the new abstract (2,2) cover.

No imports from the certificate, old frontiers, or historical record files.
"""
from functools import lru_cache
from itertools import combinations_with_replacement
import json

names = ('one', 'W', 'A', 'S', 'D', 'T', 'P', 'Wp', 'V')
dim = dict(zip(names, (1, 2, 3, 4, 5, 6, 4, 2, 3)))
odd = {'W', 'S', 'T', 'Wp'}
neighbors = {
    'one': ('W',), 'W': ('one', 'A'), 'A': ('W', 'S'),
    'S': ('A', 'D'), 'D': ('S', 'T'), 'T': ('D', 'P', 'V'),
    'P': ('T', 'Wp'), 'Wp': ('P',), 'V': ('T',),
}
zero = (0,) * 9
def add(*vs): return tuple(sum(xs) for xs in zip(*vs)) if vs else zero
def minus(v): return tuple(-x for x in v)
def sub(a,b): return add(a,minus(b))
def unit(n): return tuple(int(n == m) for m in names)
def wt(v):
    out = [0]*9
    for n,c in zip(names,v):
        for m in neighbors[n]: out[names.index(m)] += c
    return tuple(out)
@lru_cache(None)
def tensor(n,d):
    if d == 0: return unit(n)
    if d == 1: return wt(unit(n))
    return sub(wt(tensor(n,d-1)),tensor(n,d-2))
def h(bundle,t,i):
    terms=[]
    for e,n in bundle:
        d=e+t
        if i == 0 and d >= 0: terms.append(tensor(n,d))
        if i == 1 and d <= -2: terms.append(tensor(n,-d-2))
    return add(*terms)
def chi(bundle,t): return sub(h(bundle,t,0),h(bundle,t,1))
def effective(v): return all(x>=0 for x in v)
def deg(bundle): return sum(e*dim[n] for e,n in bundle)
def hom_from_source(E,block):
    e,n=block
    return sum(tensor(m,e-d)[names.index(n)] for d,m in E if e>=d)
sources=(
    ((-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-8,'one')),
    ((-2,'P'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-5,'Wp')),
    ((-2,'V'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-4,'V')),
    ((-3,'Wp'),(-3,'T'),(-3,'T'),(-4,'V')),
)
middle=((-1,'Wp'),)*3+((-1,'S'),)*3+((-1,'T'),)*6
M4=((0,'V'),)*2+((0,'P'),)*4+((0,'D'),)*3
M2=((0,'A'),)+((0,'V'),)*2+((0,'P'),)*3+((0,'D'),)*4
def eE(t): return sub(chi(middle,t),chi(M4,t))
def eQ(t): return sub(chi(middle,t),chi(M2,t))

# Enumerate by rank budget rather than prespecifying three structural families.
blocks=sorted((e,n) for e in range(-8,21) for n in names
              if dim[n]<=3 and (e%2==1)==(n in odd))
def all_bundles(start=0,remaining=3,prefix=()):
    if not remaining:
        yield prefix
        return
    for k in range(start,len(blocks)):
        e,n=blocks[k]
        if dim[n]<=remaining:
            yield from all_bundles(k,remaining-dim[n],prefix+((e,n),))

stages=[set() for _ in range(6)]
all_shapes=list(all_bundles())
for A in all_shapes:
    a=deg(A)
    if not -2 <= a <=4: continue
    B=tuple(sorted((-e-2,n) for e,n in A))
    pair=(A,B)
    stages[0].add(pair)
    good_source=any(all(hom_from_source(E,b)>0 for b in A)
                    and effective(sub(h(A,2,0),h(E,2,0)))
                    and effective(sub(h(E,2,1),h(A,2,1))) for E in sources)
    if not good_source: continue
    stages[1].add(pair)
    if not all(effective(sub(chi(C,2),f(2))) for C,f in ((A,eE),(B,eQ))): continue
    stages[2].add(pair)
    if not all(effective(sub(add(chi(C,3),chi(C,1)),f(3)))
               for C,f in ((A,eE),(B,eQ))): continue
    stages[3].add(pair)
    if a<=2 and not effective(sub(add(h(A,0,0),chi(A,2),chi(A,4)),eE(4))): continue
    stages[4].add(pair)
    if a>=0 and not effective(sub(add(h(B,0,0),chi(B,2),chi(B,4)),eQ(4))): continue
    stages[5].add(pair)

expected={
    (((-8,'one'),(2,'one'),(6,'one')),((-8,'one'),(-4,'one'),(6,'one'))),
    (((-8,'one'),(4,'one'),(6,'one')),((-8,'one'),(-6,'one'),(6,'one'))),
    (((-8,'one'),(5,'W')),((-7,'W'),(6,'one'))),
}
if stages[-1] != expected: raise RuntimeError('Independent cover mismatch')
if any(deg(A)%2 for A in all_shapes): raise RuntimeError('Parity mismatch')
for n in names:
    for d in range(31):
        v=tensor(n,d)
        if not effective(v) or sum(c*dim[m] for m,c in zip(names,v))!=dim[n]*(d+1):
            raise RuntimeError('McKay recurrence failed positivity or dimension')
print(json.dumps({'status':'pass','ring':'integer affine-E8 McKay adjacency',
                  'shape_count':len(all_shapes),'stage_counts':[len(x) for x in stages],
                  'survivors':sorted(stages[-1])},indent=2))
