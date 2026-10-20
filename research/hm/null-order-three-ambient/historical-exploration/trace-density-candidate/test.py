#!/usr/bin/env python3
"""Exact universal exterior algebra test; no geometric/model data are loaded."""
from sympy import symbols, expand, Rational

k = symbols('k')
h = symbols('h', nonzero=True)
N = 8  # ordered basis a1,a2,a3,a4,b1,b2,b3,b4

def clean(x):
    return {m: expand(c) for m,c in x.items() if expand(c) != 0}

def add(*xs):
    out = {}
    for x in xs:
        for m,c in x.items(): out[m] = out.get(m,0)+c
    return clean(out)

def scale(c,x): return clean({m:c*v for m,v in x.items()})

def wedge(x,y):
    out = {}
    for m,c in x.items():
        for n,d in y.items():
            if m & n: continue
            inversions = sum(1 for i in range(N) for j in range(N)
                             if (m >> i)&1 and (n >> j)&1 and i>j)
            out[m|n] = out.get(m|n,0)+(-1)**inversions*c*d
    return clean(out)

def power(x,n):
    out = {0:1}
    for _ in range(n): out = wedge(out,x)
    return out

def contract(i,x):
    out = {}
    for m,c in x.items():
        if (m >> i)&1:
            out[m ^ (1<<i)] = (-1)**((m & ((1<<i)-1)).bit_count())*c
    return clean(out)

def eq(name,x,y):
    assert add(x,scale(-1,y)) == {}, (name,x,y)
    print('PASS:',name)

oneforms = [{1<<i:1} for i in range(N)]
a,b = oneforms[:4],oneforms[4:]
theta = add(*(wedge(a[i],b[i]) for i in range(4)))
omega = add(wedge(a[0],a[1]),wedge(a[2],a[3]))
Pi = scale(-1,add(wedge(b[0],b[1]),wedge(b[2],b[3])))
# pi = e_a1 wedge e_a2 + e_a3 wedge e_a4;
# i_(u wedge v) = i_v i_u. This fixes the contraction sign explicitly.
i_pi_theta2 = add(contract(1,contract(0,power(theta,2))),
                     contract(3,contract(2,power(theta,2))))
eq('Pi = (1/2) i_pi(theta^2)', Pi,scale(Rational(1,2),i_pi_theta2))
eq('omega theta^2 = omega^2 Pi',wedge(omega,power(theta,2)),wedge(power(omega,2),Pi))
eq('Pi theta^2 = omega Pi^2',wedge(Pi,power(theta,2)),wedge(omega,power(Pi,2)))
eq('theta^4 = 6 omega^2 Pi^2',power(theta,4),scale(6,wedge(power(omega,2),power(Pi,2))))
eq('omega^3 = 0',power(omega,3),{})
eq('Pi^3 = 0',power(Pi,3),{})
d = scale(k,power(theta,2))
c = add(scale(1/h,omega),scale(k*h,Pi))
eq('c d - c^3/3 = 0',add(wedge(c,d),scale(-Rational(1,3),power(c,3))),{})
eq('d^2/12 - c^2 d/2 + c^4/12 = 0',add(scale(Rational(1,12),power(d,2)),scale(-Rational(1,2),wedge(power(c,2),d)),scale(Rational(1,12),power(c,4))),{})
# Expansion of exp(-c)(2-d+d^2/12), checked independently by degree.
chern = add({0:2},scale(-1,d),scale(Rational(1,12),power(d,2)))
from math import factorial
exp_minus_c = add(*(scale(Rational((-1)**j,factorial(j)),power(c,j)) for j in range(5)))
trace = wedge(exp_minus_c,chern)
for degree in (6,8):
    eq(f'[exp(-c)(2-d+d^2/12)]_{degree} = 0',
       {m:v for m,v in trace.items() if m.bit_count()==degree},{})
print('All identities hold over Q[k,h,h^-1] (including k=0 by polynomial identity).')
