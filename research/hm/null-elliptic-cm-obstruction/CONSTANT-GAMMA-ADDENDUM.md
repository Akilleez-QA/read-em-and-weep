# Arbitrary constant gamma intertwiners: exact coefficient certificate

## Result

For the frozen homogeneous 15-by-5 linear map gamma(v), and S(v_j)=(-1)^j v_j, the only constant pair M in Mat15(Q(i)), N in Mat5(Q(i)) satisfying

    M gamma(v) = gamma(Sv) N

is M=N=0. In particular there is no constant invertible pair, including non-diagonal changes or basis permutations. The original diagonal-only obstruction is thus strengthened for this exact homogeneous presentation. This does not, without additional lifting/uniqueness theorems, prove the cohomology bundle is not isomorphic to its CM pullback, nor exclude coordinate-dependent maps on the elliptic product or refined-cover comparisons.

## Exact source-to-linear-system bridge

The same immutable model pin as RESULT.md is used (SHA256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926). Every nonzero gamma record is one coefficient times either 1 or one v_j, j=1,...,4. The established homogeneous prescription replaces 1 by v0. Write the formal coefficient maps as gamma(v)=sum_(j=0)^4 v_j G_j; the checker represents each G_j only as a list of literal (row,column,integer coefficient) slots.

Since v0,...,v4 are independent homogeneous variables, equality is equivalent to 375 scalar linear equations:

    sum_a M[r,a] (G_j)[a,c]
       - (-1)^j sum_b (G_j)[r,b] N[b,c] = 0

for j=0,...,4, r=0,...,14, c=0,...,4. There are 250 unknowns, indexed M[r,a] at 15r+a and N[b,c] at 225+5b+c. The checker constructs these linear equations by visiting support slots, not by assigning coordinate values or multiplying actual polynomial matrices. On v0=1 the constant plus four independent elementary-coordinate coefficients give the same system.

## Certificate and replay

constant_gamma_check.py uses only the standard library. Its deterministic sparse Gaussian elimination processes equations in the displayed j,r,c order, always choosing the smallest surviving unknown column and dividing by its exact nonzero Fraction pivot. Every earlier pivot elimination and normalizer for each newly accepted pivot is recorded in constant-gamma-elimination.json. The 250 pivot columns are precisely 0,...,249. constant-gamma-result.json records rank250 and nullity0; normal and optimized output agree, and explicit runtime checks enforce the full rank in both modes.

This supplies a replayable coefficient-system certificate: reconstruct the sparse equation from its (j,r,c) index, perform the listed eliminations against previously normalized pivot rows, and divide by the listed normalizer. Each accepted row has no lower surviving column. Full pivot coverage therefore yields an upper-triangular system with unit diagonal after column ordering, so its homogeneous solution is zero. The unselected 125 equations are not needed to establish rank250. The checker includes the identity coordinate-action positive control M=Id15,N=Id5 to distinguish a covariance obstruction from absence of all intertwiner equations.

All coefficients and row operations are rational. A rank250 rational minor remains nonzero after extension to Q(i) (indeed any characteristic-zero extension), so the zero-space conclusion is not merely a rational-only limitation.

## Execution scope

This is a fixed, bounded coefficient linear-system calculation. It did not evaluate gamma at a point, compute matrix-polynomial products, import production modules, run physical sources, evaluate jets, or change execution guards. It does not evaluate any obstruction or detector. All 30 tests remain unknown.
