"""Universal C5 weight arithmetic only. No HM coefficients or matrices."""
A = {0, 2, 3}
D = set(range(5))
V = {0, 1, 4}

def quotient_fiber(point_weight):
    return D - {(a + point_weight) % 5 for a in A}

def cotangent(point_weight):
    return sorted((point_weight - v) % 5 for v in V if v != point_weight)

def monomial_weights(coords, degree):
    a, b = coords
    return {(i*a + (degree-i)*b) % 5 for i in range(degree+1)}

assert quotient_fiber(0) == {1, 4}
assert quotient_fiber(4) == {0, 3}
assert quotient_fiber(1) == {0, 2}
assert cotangent(0) == [1, 4]
assert cotangent(4) == [3, 4]
assert 1 in monomial_weights((1, 4), 1)
assert 1 not in monomial_weights((1, 4), 2)
assert 3 not in monomial_weights((1, 4), 1)
assert 3 in monomial_weights((1, 4), 2)
assert 4 in monomial_weights((4, 3), 1)
assert 4 not in monomial_weights((4, 3), 2)
assert 2 not in monomial_weights((4, 3), 1)
assert 2 in monomial_weights((4, 3), 2)
assert [k for k in range(1, 7) if 4*k % 5 == 3] == [2]
assert [k for k in range(1, 5) if 3*k % 5 == 2] == [4]
assert 2 + 4 == 6
print('PASS: universal fixed-point fibers, dual weights, order bounds, and lengths 2+4.')
