"""Integer-mask-only control. No source/model/curve/matrix/polynomial evaluation.
Entries are integer multipliers of the formal columns D*t, A, B, E/t
in 2F/R and 2G/R, as specified by the written structural formula.
"""
def bit(m, s):
    return (m >> s) & 1

def rows(masks):
    u, v, w = [tuple(bit(b, s)-bit(a, s) for s in (0, 1))
               for a, b in zip(masks, masks[1:])]
    f = (-2*u[0]*v[0]*w[1], u[0]*v[1]*(w[0]-w[1]),
         u[1]*v[0]*(w[0]-w[1]), 2*u[1]*v[1]*w[0])
    g = (2*v[0]*w[0]*u[1], v[0]*w[1]*(u[1]-u[0]),
         v[1]*w[0]*(u[1]-u[0]), -2*v[1]*w[1]*u[0])
    return f, g

cases = {
    (0,1,3,5): ((0,1,0,0), (0,0,0,2)),
    (0,2,3,6): ((0,0,-1,0), (-2,0,0,0)),
    (0,1,2,3): ((0,1,0,0), (0,0,-1,0)),
    (0,2,5,7): ((0,0,-1,0), (0,1,0,0)),
    (0,1,4,6): ((2,0,0,0), (0,1,0,0)),
    (0,2,4,5): ((0,0,0,-2), (0,0,-1,0)),
}
def require(condition, detail):
    if not condition:
        raise RuntimeError(detail)

for masks, expected in cases.items():
    require(all(a < b for a,b in zip(masks, masks[1:])), ('order', masks))
    require(all(0 <= m <= 7 for m in masks), ('range', masks))
    require(rows(masks) == expected, (masks, rows(masks), expected))

# Deliberately wrong integer metadata tables must be rejected.
mutations = 0
for masks, expected in cases.items():
    for endpoint in (0, 1):
        for column, coefficient in enumerate(expected[endpoint]):
            if coefficient:
                bad = [list(row) for row in expected]
                bad[endpoint][column] = -coefficient
                require(rows(masks) != tuple(map(tuple, bad)), ('undetected sign mutation', masks))
                mutations += 1
require(mutations == 12, ('mutation count', mutations))
print('PASS: 12 formal coefficient sign mutations detected; checks survive python -O.')
print('PASS: all six strictly increasing mask tuples match the formal integer coefficient table.')
