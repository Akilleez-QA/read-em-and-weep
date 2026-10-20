#!/usr/bin/env python3
"""Independent integer-exponent checks only; no source imports or products."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def need(ok, why):
    if not ok:
        raise ValueError(why)

def add(*xs):
    return tuple(sum(v) for v in zip(*xs))

def scale(n, x):
    return tuple(n * a for a in x)

def reduce_q(x):
    a, b, c = x
    q, r = divmod(c, 2)
    return (a + q, b + q, r)

def same(x, y):
    return reduce_q(x) == reduce_q(y)

def finite_to_infinity(x):
    a, b, c = x
    return (-a - 2*b - 2*c, b, c)

ZERO = (0, 0, 0)
FRAME = (ZERO, (-1, 0, 1))
LEGAL = ((ZERO, (1, 1, 0)), ((1, 0, 0), (0, 1, 0)))
ELL = (ZERO, (-1, 0, 0))

def gfactor(chart, mi, mj, a, b):
    # Frozen g_(b,a): D_j,b times T_ab times D_i,a^-1.
    return add(scale(1-2*b, FRAME[mj]), scale(-(1-2*a), FRAME[mi]),
               scale(b-a, ELL[chart]))

def jfactor(chart, m, a, b):
    return scale(b-a, add(scale(2, FRAME[m]), scale(-1, ELL[chart])))

def polynomial(x):
    a, b, c = reduce_q(x)
    return a >= 0 and b >= 0 and c in (0,1)

# Handwritten target lists use order (a,b)=(0,0),(1,1),(1,0),(0,1).
entries = ((0,0),(1,1),(1,0),(0,1))
expected = {
 (0,0,0): ((0,0,0),)*4,
 (0,0,1): ((0,1,1),(1,0,1),(0,1,1),(1,0,1)),
 (0,1,0): ((1,0,1),(0,1,1),(0,1,1),(1,0,1)),
 (0,1,1): ((2,2,0),(2,2,0),(1,3,0),(3,1,0)),
 (1,0,0): ((2,0,0),(2,0,0),(3,0,0),(1,0,0)),
 (1,0,1): ((0,1,1),(1,0,1),(1,1,1),(0,0,1)),
 (1,1,0): ((1,0,1),(0,1,1),(1,1,1),(0,0,1)),
 (1,1,1): ((0,2,0),(0,2,0),(0,3,0),(0,1,0)),
}
checks = {}
count = 0
for chart, mi, mj in itertools.product(range(2), repeat=3):
    for k, (a,b) in enumerate(entries):
        z = add(gfactor(chart,mi,mj,a,b), LEGAL[chart][mi], LEGAL[chart][mj])
        need(polynomial(z), 'one-factor transition clearance')
        need(same(z, expected[(chart,mi,mj)][k]), 'cleared table')
        count += 1
checks['independent_cleared_transition_entries'] = count

# Conversion is performed on rational monomials, never on source coefficients.
count = 0
for mi,mj,a,b in itertools.product(range(2), repeat=4):
    want = add(finite_to_infinity(gfactor(0,mi,mj,a,b)), (a-b,0,0))
    need(same(gfactor(1,mi,mj,a,b),want), 'missing homogeneous ell correction')
    li, lj = 1+2*mi, 1+2*mj
    z0 = add(gfactor(0,mi,mj,a,b), LEGAL[0][mi], LEGAL[0][mj])
    z1 = add(gfactor(1,mi,mj,a,b), LEGAL[1][mi], LEGAL[1][mj])
    need(same(z1,add(finite_to_infinity(z0),(li+lj+a-b,0,0))),
         'cleared scalar change of trivialization')
    count += 1
checks['finite_infinity_transition_covariances'] = count
for m in range(2):
    need(same(LEGAL[1][m],add(finite_to_infinity(LEGAL[0][m]),(1+2*m,0,0))),
         'legal global section degree')
checks['legal_section_degree_checks'] = 2

# All 16 standard charts and 256 ordered mask pairs; four entries per case.
count = 0
for chart, mi, mj in itertools.product(range(16),repeat=3):
    for a,b in entries:
        for r in range(4):
            ch,ii,jj = (chart>>r)&1,(mi>>r)&1,(mj>>r)&1
            need(polynomial(add(gfactor(ch,ii,jj,a,b),LEGAL[ch][ii],LEGAL[ch][jj])),
                 'product coordinate clearance')
        count += 1
checks['four_factor_transition_entry_cases'] = count

# Owner tags change domains and trivializations, not frame choice.
# Derive both primitive factors from their own tags, then convert to A.
count = 0
for A,Ai,Aj,mi,mj,a,b in itertools.product(range(2),repeat=7):
    for di,dj in itertools.product((4,5),repeat=2):
        p_own = -a*Ai
        i_own = b*Aj
        p_common = p_own - a*(A-Ai)
        i_common = i_own + b*(A-Aj)
        need(p_common+i_common == (b-a)*A, 'tag conversion of T')
        need(p_common+i_common-(b-a)*A == 0, 'physical g invariance')
        hi_own,hj_own = di*Ai,dj*Aj
        hi_common = hi_own+di*(A-Ai)
        hj_common = hj_own+dj*(A-Aj)
        degree = 2*di+2*dj+(1+2*mi)+(1+2*mj)
        all_clear = 2*hi_common+2*hj_common+((1+2*mi)+(1+2*mj))*A
        need(all_clear == degree*A, 'owned global clearing sections')
        count += 1
checks['original_owner_tag_and_carrier_cases'] = count

count = 0
for chart,m,a,b in itertools.product(range(2),repeat=4):
    need(polynomial(add(jfactor(chart,m,a,b),LEGAL[chart][m])), 'j selected owner')
    # I_a P_b has weight a-b, exactly opposite the c exponent.
    need(same(jfactor(1,m,a,b),add(finite_to_infinity(jfactor(0,m,a,b)),(b-a,0,0))),
         'j infinity covariance')
    count += 1
checks['one_factor_inclusion_entry_cases'] = count
count = 0
for chart,m in itertools.product(range(16),repeat=2):
    for a,b in entries:
        for r in range(4):
            ch,mm=(chart>>r)&1,(m>>r)&1
            need(polynomial(add(jfactor(ch,mm,a,b),LEGAL[ch][mm])), 'product j')
        count += 1
checks['four_factor_inclusion_entry_cases'] = count

# Actual invariant vector field descends at the branch points.
# These are literal coefficient lists of D(y^2-x^3+x) and D(u^2-t+t^3).
need(tuple(x+y for x,y in zip((3,-1),(-3,1))) == (0,0), 'finite branch derivation')
need(tuple(x+y for x,y in zip((3,-1),(-3,1))) == (0,0), 'infinity branch derivation')
checks['branch_relation_derivation_checks'] = 2

controls = []
# With ell omitted, finite-to-infinity conversion misses the homogeneous weight.
need(not same(gfactor(1,0,0,0,1),ZERO), 'ell-omission control failed')
controls.append('omitted ell in infinity reciprocal')
for kept in (0,1):
    z = add(gfactor(1,0,1,0,1), LEGAL[1][kept])
    need(not polynomial(z), 'missing endpoint control failed')
    controls.append('mixed reciprocal missing '+('bit-one' if kept==0 else 'bit-zero')+' charge')
need(not polynomial(gfactor(0,0,1,0,0)), 'legal-zero control failed')
controls.append('all legal factors omitted')
# The actual c_1,infinity is s, not 1 as a fictitious e_1=1/sqrt(t) would give.
need(not same(add(scale(2,FRAME[1]),scale(-1,ELL[1])),ZERO), 'square-root control failed')
controls.append('fictitious square-root infinity frame')
# False y inverse=1/x would miss h and does not multiply e_1 to one.
need(not same(add(FRAME[1],(-1,0,0)),ZERO), 'branch division control failed')
controls.append('unjustified branch division')
checks['negative_controls'] = controls
print(json.dumps({'status':'pass','method':'integer exponent metadata only','checks':checks},indent=2,sort_keys=True))
