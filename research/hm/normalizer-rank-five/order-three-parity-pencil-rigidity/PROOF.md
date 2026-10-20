# Order-three fixed-line parity-pencil rigidity

## Result and scope

Retain the hypotheses and notation of `../order-three-rank-point-bound/PROOF.md`, and use the actual twenty-dimensional target representation from `../../cubic-loci/canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md`. No value of the source operation is evaluated.

On either projective fixed line of an order-three subgroup, a rank-three point can occur only if a certain two-vector coefficient map into a three-dimensional parity quotient has rank at most one. In the nondegenerate case the possible pair has a uniquely prescribed squared coordinate. This is a new necessary obstruction, not an exclusion of the last 1000-point orbit.

## 1. Weight blocks and a second rank-two floor

Choose a normalized lift a of order three and its commuting canonical reflection c. Write

    V = X_0 ⊕ U_1 ⊕ Y_2,     dimensions 1,2,2,

with subscripts indicating a-weights modulo three. The c-parity on X is positive, and on each of U,Y it is (+,−). Write u=s t_1+t w_1 with t_1 positive and w_1 negative. The two endpoints s=0 and t=0 are already excluded from Z3.

The constant binary image H_U has dimension two, a-weight zero, and one dimension in each c-parity: universally it is U⊗det U. Its injectivity follows from repeated-input injectivity, as in the cited point-bound proof.

The quotient pencil B_U has three independent blocks:

    B_0: X⊗Y → J_0/H_U,
    B_1: Sym²X ⊕ U⊗Y → J_1,
    B_2: X⊗U ⊕ Sym²Y → J_2.

Their source dimensions are 2,5,5. All are linear in u and their ranks sum to rank b_u−2. The repeated-input map v↦f(u,u,v), v∈Y, injects a two-dimensional space into im B_1(u); hence rank B_1(u)≥2.

Also rank B_2(u)≥2 at every nonzero u∈U. Indeed its restriction to Sym²Y sends y² to

    f(y,u,y) = −2 f(y,y,u),

which is nonzero for every nonzero y∈Y, since u∉Cy. A linear map out of the three-dimensional Sym²Y with rank at most one has kernel dimension at least two. Its projective kernel then contains a line in P², which intersects the Veronese conic { [y²] }. This contradicts the preceding nonvanishing.

Consequently at a point of Z3 the block-rank tuple (rank B_0,rank B_1,rank B_2) satisfies

    rank B_0≤1,   rank B_1≥2,   rank B_2≥2,
    rank B_0+rank B_1+rank B_2≤5.

In particular, if B_0 has rank one there, the tuple is exactly (1,2,2).

## 2. Target dimensions and reflection normal form

For clarity the required restriction of the actual target J=A*⊗Sym³W can be checked using only characters. On the binary-icosahedral complement, A* has a positive three-space and a negative two-space. An order-three element has weights (0,1,2) on the positive three-space and (1,2) on the negative two-space. The four-space Sym³W is c-negative, with a-weight multiplicities (2,1,1). Tensoring gives

    J_0: c-parity dimensions (+2,−4),
    J_1,J_2: c-parity dimensions (+3,−4).

Thus J_0/H_U has parity dimensions (+1,−3). These facts also follow from the usual Galois-conjugate Schrödinger restriction; no source tensor is needed.

Choose bases of X⊗Y with first vector c-positive and second c-negative, and choose a basis of the one-dimensional positive target quotient. Reflection equivariance forces the entire B_0 pencil into the form

    positive row:    [ α s,  β t ],
    negative rows:   [ C t,  D s ],

where α,β are scalars and C,D are fixed vectors in the three-dimensional negative target quotient. The statements below are independent of the choices; changing the coordinates rescales the displayed constants and squared slope compatibly.

Its two-by-two minors consist precisely of

    s t (C∧D),
    α D s² − β C t².

The first expression denotes the three minors formed by two negative rows; the second denotes the three minors formed by the positive row and one negative row.

Every rank-three point has st≠0. Section 1 therefore implies the necessary conditions

    C∧D=0,
    α D s²=β C t².                         (★)

In particular, if C,D are independent, this entire fixed line is disjoint from Z3. Since all order-three subgroups are conjugate and the normalizer exchanges their two fixed lines, independence for one such pencil excludes every 1000-point orbit.

## 3. Location and generic-rank rigidity if the pair survives

Suppose B_0 has generic rank two and the line contains a Z3 point. By (★), write C=c_0 v and D=d_0 v for a nonzero vector v. The scalar polynomial

    α d_0 s² − β c_0 t²

is nonzero because generic rank is two. Having a zero with st≠0 forces both αd_0 and βc_0 to be nonzero. Thus C,D,α,β are all nonzero and

    (t/s)² = α d_0 / (β c_0).

The rank-one locus of B_0 is precisely this reflection pair; B_0 has rank two at both endpoints. Any Z3 point on the line must belong to that pair, and at it the full quotient block tuple is (1,2,2).

Let r_i be the generic rank of B_i. Since the pair has B_1 and B_2 ranks two, each nonzero maximal minor of either block vanishes to order at least r_i−2 at each point. Its degree is r_i. Hence

    2(r_i−2)≤r_i, so r_1,r_2≤4.

Therefore a surviving pair in this case forces generic rank B_U≤10, equivalently generic rank b≤12. If either five-column block has generic rank five, the pair is impossible.

If B_0 instead has generic rank one, it cannot vanish at both members of an off-endpoint reflection pair: a nonzero entry is linear and cannot vanish at two distinct points. Thus a surviving pair again has block tuple (1,2,2), and again r_1,r_2≤4; here generic rank b≤11. If B_0 is identically zero, Section 1 gives only the earlier sum-of-ranks constraint; no stronger claim is made for that case.

## 4. What is still missing

The representation dimensions and repeated-input injectivity alone, as used here, do not prove C∧D≠0 or exclude the exceptional coefficient configurations. Nor does the quadratic repeated-input subbundle alone prevent two rank-two drops in a five-column pencil. A valid next step is to use the full normalizer coupling to determine whether the abstract coefficient map with columns C,D is injective, or to eliminate its rank-one alternative by a representation-theoretic identity. This would use more than the local C3 and reflection restrictions.

The proof does not evaluate α,β,C,D for the source operation, compute a selected rank matrix, or assert existence of any candidate point. Its only writes are local proof artifacts.
