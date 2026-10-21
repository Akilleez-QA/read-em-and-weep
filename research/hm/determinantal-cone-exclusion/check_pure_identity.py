"""Exact universal pure-diagram arithmetic; no HM matrix or source evaluation."""
from fractions import Fraction as F
from math import prod

sequences = [(0,4,5,6,8,9), (0,4,5,7,8,9),
             (0,4,6,7,8,9), (0,4,6,7,8,10)]

def pure(d):
    return {(i,j): F(prod(d[1:]), prod(abs(j-d[l])
            for l in range(6) if l != i)) for i,j in enumerate(d)}

def verify(k):
    weights = [F(k,120), F(13,21)-F(k,70), F(k+10,168), F(9,28)]
    result = {}
    for d,w in zip(sequences, weights):
        for position,value in pure(d).items():
            result[position] = result.get(position, 0) + w*value
    expected = {(0,0):1, (1,4):35, (2,5):52, (2,6):55+k,
                (3,6):k, (3,7):160, (4,8):110, (5,9):20, (5,10):3}
    assert result == expected
    return weights

# Both sides are affine in k, so two distinct substitutions verify the identity.
verify(0)
verify(1)
for k in (15,25,35):
    assert all(w >= 0 for w in verify(k))
for c in (9,10):
    p = pure((0,4,5,6,8,c))
    assert p[3,6] / p[2,5] <= F(5,6)
assert 45 > F(5,6)*52
print('PASS: pure-diagram identity, positivity, and extreme exclusion')
