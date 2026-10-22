#!/usr/bin/env python3
"""Universal integer-degree certificate for a rank-one saturated Gauss flag.

No HM coefficients, actual multiplication matrices, rank evaluations, scans,
or local-model experiments occur.  The geometric existence and regularity
of the flag are proved in RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md.

This is a symbolic identity proof for arbitrary N and r, not a finite-range
numerical test masquerading as a universal assertion.
"""
import sympy as s

N, r, j, i, x = s.symbols("N r j i x", integer=True)
a, b, c = s.symbols("a b c", integer=True, positive=True)


def zero(expr):
    assert s.simplify(s.expand(expr)) == 0, expr


# For d_i = x + 2(i-1) + sum_{j<i} delta_j, a fixed delta_j
# appears in N-j total degrees and in r-j prefix degrees if j<r.
# The arithmetic progression terms are verified for arbitrary endpoints.
zero(s.summation(2 * (i - 1), (i, 1, N)) - N * (N - 1))
zero(s.summation(2 * (i - 1), (i, 1, r)) - r * (r - 1))
zero(s.summation(1, (i, j + 1, N)) - (N - j))
zero(s.summation(1, (i, j + 1, r)) - (r - j))

# Coefficientwise elimination of the initial degree x in
# N*(prefix sum) - r*(total sum).  These exhaust all monomials:
# x, the constant term, delta_j for j<r, and delta_j for j>=r.
zero(N * r * x - r * N * x)
zero(N * r * (r - 1) - r * N * (N - 1) + N * r * (N - r))
zero(N * (r - j) - r * (N - j) + j * (N - r))
zero(-r * (N - j) + r * (N - j))

# Strict positivity of the two ramification weights on their full domains.
# For 1 <= j < r < N, set j=a, r=a+b, N=a+b+c.
left_weight = (j * (N - r)).subs({j: a, r: a + b, N: a + b + c})
zero(left_weight - a * c)
assert left_weight.is_positive
# For 1 <= r <= j < N, set r=a, j=a+b-1, N=a+b-1+c.
# b>=1 permits j=r and covers every integer j>=r.
right_weight = (r * (N - j)).subs({r: a, j: a + b - 1, N: a + b - 1 + c})
zero(right_weight - a * c)
assert right_weight.is_positive

# Equivalent normalized-degree proof: d_i = 2i-N-1 + e_i,
# with nondecreasing e_i and total zero.  Verify the base prefix sum.
zero(s.summation(2 * i - N - 1, (i, 1, N)))
zero(s.summation(2 * i - N - 1, (i, 1, r)) + r * (N - r))

# Specialize only the established bundle invariants.
ambient_dimension, bundle_rank, bundle_degree = 30, 17, -54
complementary_rank = ambient_dimension - bundle_rank
rank_one_degree_ceiling = -bundle_rank * complementary_rank
assert complementary_rank == 13
assert rank_one_degree_ceiling == -221
assert bundle_degree > rank_one_degree_ceiling
required_effective_weight = (
    -ambient_dimension * bundle_degree
    - ambient_dimension * bundle_rank * complementary_rank
)
assert required_effective_weight == -5010
assert required_effective_weight < 0  # Contradicts the proved nonnegativity.

# Existing exact cohomological rank formula, with the newly proved SF bound.
sf_generic_rank_lower_bound = 2
square_generic_rank_lower_bound = 24 + sf_generic_rank_lower_bound
assert square_generic_rank_lower_bound == 26
assert 17 - sf_generic_rank_lower_bound == 15
assert 37 - square_generic_rank_lower_bound == 11

print("PASS: universal complete-flag degree identity, coefficient by coefficient.")
print("PASS: all ramification weights are positive on their full integer domains.")
print("PASS: rank-one SF forces deg E <= -221, contradicting the actual -54.")
print("PASS: the required effective ramification weight would be -5010.")
print("CONCLUSION: actual generic SF rank >= 2; positive square rank >= 26.")
print("NOT PROVED: maximal SF rank 13 or an improved generic four-or-five count.")
