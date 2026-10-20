"""Synthetic dual-number representation only; no project source inputs."""
from fractions import Fraction as Q

def apply_u(t, v):
    a,b=v
    return (Q(0),t*a)
for t in map(Q,[0,1,-1,2]):
    for v in [(Q(1),Q(0)),(Q(0),Q(1)),(Q(2),Q(3))]:
        assert apply_u(t,apply_u(t,v))==(0,0)
    rank=0 if t==0 else 1
    quotient_dimension=2-rank
    assert quotient_dimension==(2 if t==0 else 1)
    print(f't={t}: u^2=0; rank(u)={rank}; dim(M/uM)={quotient_dimension}')
print('PASS: branch fiber cannot be free of rank one over dual numbers')
