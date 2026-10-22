"""Independent finite integer envelope for a negative Gauss-kernel flag.
No selected source coefficients, maps, points, or actual-instance ranks.
"""
from functools import lru_cache
from itertools import product

def partitions(n, ceiling):
    if n == 0:
        yield ()
    for q in range(min(n, ceiling), 0, -1):
        for tail in partitions(n-q, q):
            yield (q,)+tail

def envelope(n, degrees):
    assert n>0 and len(degrees)>0
    ds=tuple(sorted(degrees, reverse=True))
    ps=list(partitions(n,len(ds)))
    values=[(sum(sum(ds[:q])-2*j*q for j,q in enumerate(p,1)),p) for p in ps]
    # Independently structured memoized maximization, retaining the step index.
    @lru_cache(None)
    def dynamic(left, ceiling, j):
        if left==0:return 0
        return max(sum(ds[:q])-2*j*q+dynamic(left-q,q,j+1)
                   for q in range(1,min(left,ceiling)+1))
    best=max(v for v,p in values)
    assert best==dynamic(n,len(ds),1)
    heights=[h for h in product(range(n+1),repeat=len(ds))
             if sum(h)==n and all(h[i]>=h[i+1] for i in range(len(ds)-1))]
    assert len(heights)==len(ps)
    assert best==max(sum(k*d-k*(k+1) for k,d in zip(h,ds)) for h in heights)
    return best,[p for v,p in values if v==best],len(ps)

cases=[((-10,-10,4),-52,-78),((-10,-6,4),-56,-70),((-10,0,2),-56,-60),((-10,2,2),-60,-50)]
for ds, actual, expected in cases:
    cap, winners, count=envelope(11,ds)
    assert count==16 and cap==expected
    print({'J_degrees':ds,'given_degree':actual,'necessary_upper_bound':cap,
           'contradiction_if_hypotheses_hold':actual>cap,'maximizing_partitions':winners})
assert len(list(partitions(11,3)))==16
print('PASS: partitions, dynamic recurrence and conjugate-column enumeration agree.')
print('Scope: necessary envelope only; geometric hypotheses must be proved separately.')
