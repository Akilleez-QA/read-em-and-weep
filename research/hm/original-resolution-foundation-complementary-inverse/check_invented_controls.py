#!/usr/bin/env python3
"""Tiny INVENTED systems only: one 3-cycle+forced coordinate and one triangular.

There are no file reads, model data, physical source matrices, symbolic
polynomials, or production imports. This is not a specialization of the pinned
8-coordinate problem. All arithmetic is on independently invented rationals.
"""
from fractions import Fraction as Q

COUNT = 0


def require(ok, message):
    global COUNT
    if not ok:
        raise RuntimeError(message)
    COUNT += 1


# An unrelated three-cycle, using u^3-abc rather than the pinned four-cycle.
u, a, b, c, e = map(Q, (2, 3, 5, 7, 11))
gap = u**3-a*b*c


def cycle_map(x):
    return (u*x[0]-a*x[1], u*x[1]-b*x[2],
            u*x[2]-c*x[0], u*x[3]+e*x[1])


def cycle_solve(y, wrong_sign=False):
    sign = -1 if wrong_sign else 1
    x1 = (u*u*y[0]+sign*a*u*y[1]+a*b*y[2])/gap
    x3 = (y[2]+c*x1)/u
    x2 = (y[1]+b*x3)/u
    x4 = (y[3]-e*x2)/u
    return x1,x2,x3,x4


require(gap == -97, 'Invented nonzero cycle gap')
samples = [tuple(Q(int(i==j)) for i in range(4)) for j in range(4)]
samples += [(Q(2,3),Q(-5,7),Q(11,13),Q(-17,19)), (Q(0),)*4]
for x in samples:
    require(cycle_solve(cycle_map(x)) == x, 'Invented cycle left inverse')
for y in samples:
    require(cycle_map(cycle_solve(y)) == y, 'Invented cycle right inverse')
require(cycle_map(cycle_solve(samples[1], True)) != samples[1], 'Invented closing-sign drift detected')
# A singular three-cycle has a visible nonzero kernel; no inverse is claimed.
singular_x = (Q(1),Q(1),Q(1),Q(-3))
singular_y = (singular_x[0]-singular_x[1],singular_x[1]-singular_x[2],
              singular_x[2]-singular_x[0],singular_x[3]+3*singular_x[1])
require(singular_x != (Q(0),)*4 and singular_y == (Q(0),)*4, 'Singular cycle retained')


# A separately invented triangular system with four coordinates.
def triangular_map(x):
    return 2*x[3], -3*x[2]+5*x[3], 7*x[1]+11*x[2], 13*x[0]-17*x[1]


def triangular_solve(y):
    x4=y[0]/2
    x3=(5*x4-y[1])/3
    x2=(y[2]-11*x3)/7
    x1=(y[3]+17*x2)/13
    return x1,x2,x3,x4


for x in samples:
    require(triangular_solve(triangular_map(x)) == x, 'Invented triangular left inverse')
for y in samples:
    require(triangular_map(triangular_solve(y)) == y, 'Invented triangular right inverse')
print(f'PASS: {COUNT} tiny invented rational checks, including wrong-sign and singular-cycle controls.')
print('No source/model reads, physical data, 8-coordinate source specialization, polynomial expansion, or source execution.')
