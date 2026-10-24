"""Fixed physical even characters; exact Q(sqrt(5)), with degree cap twelve."""
from fractions import Fraction as F


def q(a, b=0):
    return F(a), F(b)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(a, x):
    return a*x[0], a*x[1]


def mul(x, y):
    return x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0]


# Five A5 conjugacy classes, using fixed lifts for the physical W traces.
SIZES=(1,15,20,12,12)
TRACE_W=(q(2),q(0),q(1),q(F(1,2),F(1,2)),q(F(1,2),F(-1,2)))
PHI=q(F(1,2),F(1,2))
PHIBAR=q(F(1,2),F(-1,2))
IRREPS={
    'one': tuple(q(x) for x in (1,1,1,1,1)),
    'A': (q(3),q(-1),q(0),PHI,PHIBAR),
    'V': (q(3),q(-1),q(0),PHIBAR,PHI),
    'P': tuple(q(x) for x in (4,0,1,-1,-1)),
    'D': tuple(q(x) for x in (5,1,-1,0,0)),
}
DIMENSIONS={'one':1,'A':3,'V':3,'P':4,'D':5}


def sym_character(n):
    if n not in (1,2,8,9,10,12):
        raise ValueError('Only the six fixed universal degrees are supported')
    out=[]
    for t in TRACE_W:
        a,b=q(1),t
        for unused in range(2,n+1):
            a,b=b,add(mul(t,b),scale(-1,a))
        out.append(b)
    return tuple(out)


def tensor(x,y):
    return tuple(mul(a,b) for a,b in zip(x,y))


def character_sum(x,y):
    return tuple(add(a,b) for a,b in zip(x,y))


def inner(x,y):
    total=q(0)
    for size,a,b in zip(SIZES,x,y):
        total=add(total,scale(F(size,60),mul(a,b)))
    if total[1]!=0 or total[0].denominator!=1:
        raise RuntimeError('Expected an integral character multiplicity')
    return int(total[0])


def decompose_even(character):
    return {name:mult for name,chi in IRREPS.items()
            if (mult:=inner(character,chi))!=0}
