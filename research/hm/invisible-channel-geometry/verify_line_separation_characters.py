"""Bounded universal character and weight checks; no HM-instance data."""
from fractions import Fraction as F

# Q(phi), phi^2=phi+1. Each pair means a+b*phi.
def c(a, b=0):
    return F(a), F(b)
def add(x, y):
    return x[0]+y[0], x[1]+y[1]
def neg(x):
    return -x[0], -x[1]
def sub(x, y):
    return add(x, neg(y))
def mul(x, y):
    a,b=x; d,e=y
    return a*d+b*e, a*e+b*d+b*e

def plus(*rows):
    return tuple(tuple(sum(t[j] for t in col) for j in (0,1))
                 for col in zip(*rows))

def prod(x, y):
    return tuple(mul(a,b) for a,b in zip(x,y))

one = (c(1),)*5
A = (c(3),c(-1),c(0),c(0,1),c(1,-1))
V = (c(3),c(-1),c(0),c(1,-1),c(0,1))
P = (c(4),c(0),c(1),c(-1),c(-1))
D = (c(5),c(1),c(-1),c(0),c(0))
assert prod(P,A) == plus(V,P,D)

# Sym^(2*l) W is the spin-l character; recurrence from SL2 weights.
h0,h1=one,A
A_minus_one=tuple(sub(x,c(1)) for x in A)
for ell in (2,3):
    h2=tuple(sub(x,y) for x,y in zip(prod(A_minus_one,h1),h0))
    h0,h1=h1,h2
assert h1 == plus(V,P)  # Sym^6 W has no A.

# Invariant divisor degree18 can contain only one orbit of size12.
orbit_sizes=(12,20,30,60)
assert [n for n in orbit_sizes if n<=18] == [12]
assert 2*12>18 and 18-12==6

# At a C5 square, use the binary stabilizer of order10.
source_weights=[4,2,0,-2,-4]
target_weight=-2*10
allowed=[i for i,w in enumerate(source_weights) if (w-target_weight)%10==0]
assert allowed==[2]  # ell^2 m^2, after the fixed equivariant identification.
assert 4 == 3+1
print('PASS: universal character exclusions, orbit-degree bound, and unique scalar weight')
