#!/usr/bin/env python3
"""Universal integer checks only; no HM coefficients or rank tests."""
layers = [3*(m+1)*(9-2*m) for m in range(5)]
assert layers == [27,42,45,36,15]
jp, jm = sum(layers[::2]), sum(layers[1::2])
assert (jp,jm) == (87,78)
kp, km = jp-4, jm+4
assert (kp,km) == (83,82)
assert kp-layers[4] == 68
assert kp-layers[4]-layers[2] == 23
assert km-layers[3] == 46
assert (64-60,87-83) == (4,4)
assert (87-41,83-37) == (46,46)
assert (78-44,82-48) == (34,34)
assert kp == 83 and km-4 == 78
assert 37 == 37 and 48-4 == 44
# Verify every formally possible stage-kernel integer has the stated Euler index.
for k4 in range(16):
    for kstage2 in range(46):
        k2=k4+kstage2
        r2=23+k2
        for rank0 in range(min(27,r2)+1):
            h0=k2+27-rank0
            h1=r2-rank0
            assert h0-h1 == 4
            assert h1 >= max(0,k2-4)
for k3 in range(37):
    r3=46+k3
    for rank1 in range(43):
        h0=k3+42-rank1
        h1=r3-rank1
        assert h0-h1 == -4
print('PASS: finite-jet ranks (87,78) -> (83,82), with actual indices (4,-4)')
print('PASS: positive staged ranks 15 -> 83, 45 -> 68+k4, 27 -> 23+k2')
print('PASS: odd staged ranks 36 -> 82, 42 -> 46+k3')
print('PASS: positive 60 -> 83 and 64 -> 87 have the same Euler index')
print('PASS: Fitting indices match actual ambient (41 -> 37, 44 -> 48) blocks')
print('BOUNDARY: integer checks assert no actual rank, jet lifting, or nonzero minor')
