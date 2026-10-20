> Historical mathematical audit, preserved in full apart from nonmathematical process statements and source-link normalization. Original-source hashes identify the audited source text; publication-byte hashes are recorded separately. This is not a claim of a fresh or formal proof check.

# Independent audit: pointwise rank-two primitive-linear boundary

## Bounded verdict

The proof is correct in its expressly stated sector: constant-coefficient linear relations among the six argument permutations of the normalized, trace-free, primitive-linear defining expression, required to hold universally by rank-two fiberwise algebra. In this sector, the only relations are the three outer-reversal differences. No correction is required.

The original-source PROOF.md has SHA-256:

    65c9b28209da17b8e894d9b16ed9b4577df45dc2876c4c64a531e0e706a482ef

The cohomological cyclic relation is an additional imported geometric theorem, not a universal pointwise identity. Combining that relation with reversal leaves the stated two-dimensional formal argument-ordering quotient. Relative to the previously established equivariant description, this particular pointwise test supplies no additional equation on either the two symmetric or the two alternating components.

This verdict is not a completeness theorem for cohomological constraints, a realization theorem for eligible four-component maps, or a nonvanishing theorem for the actual operation.

## 1. Exterior signs and primitive normalization

The polarized traceless rank-two identity for ordinary coefficient matrices is the anticommutator identity. For two degree-one endomorphism-valued forms, reversing their coefficient factors contributes a minus sign. Its correctly signed form is therefore

    xy - yx = tr(xy) I.

Graded trace cyclicity also gives tr(yx) = -tr(xy). Consequently

    (xy)_0 = (xy + yx)/2 = B(x,y),
    B(x,y) = B(y,x).

Its universal coefficient tensor is one half of the nonzero bracket tensor of the abstract Lie algebra sl2, tensored with exterior multiplication. Thus its use as a nonzero universal bilinear expression requires no selected matrices or polynomial instance.

Writing h_ab = q_ab + t_ab I, adjugation acts by -1 on q_ab and +1 on t_ab I. Hence tau(h_ab) = -h_ba is exactly the pair of conditions

    q_ab = q_ba,    t_ab = -t_ba.

The scalar t_bc is itself odd. Moving it to the left of a contributes a minus sign, while t_ab is already to the left of c. Thus

    (a h_bc + h_ab c)_0
        = B(a,q_bc) + B(q_ab,c) - t_bc a + t_ab c

has the correct signs. Reversing a and c preserves this expression using the two pair-normalization conditions and the symmetry of B. No unsupported trace-free condition is imposed on an entire primitive.

## 2. What the universal multigrading proves

One can make the coefficient comparison precise by taking the free exterior coefficient algebra on separate copies of sl2* for the six families

    a, b, c, q_ab, q_bc, q_ca,

together with a separate scalar odd generator for each independent t pair. The universal traceless endomorphism-valued elements are the tautological elements associated with those copies. Each family gives an independent multigrading coordinate.

This is a grading by independent formal coefficient families. It is finer than the tridegree in the three labeled inputs: after assigning q_bc the combined input label bc, all three P terms would have input tridegree abc. The proof correctly uses the finer family grading, not that coarser input grading.

In this free coefficient algebra,

    P_a = B(a,q_bc),
    P_b = B(b,q_ca),
    P_c = B(c,q_ab)

lie in three distinct family degrees, and each is nonzero by the bracket-tensor observation. Terms involving a t generator have still different family degrees and cannot cancel any P component.

For a relation lambda X + mu Y + nu Z = 0, comparison of these three components gives

    lambda + mu = 0,
    mu + nu = 0,
    nu + lambda = 0.

Since the coefficient field has characteristic zero, all three coefficients vanish. This proves independence of X, Y, and Z in the universal expression space. The six original permutations occur in three reversal pairs, so their entire constant-coefficient relation space consists of the three reversal differences. This is a formal universal coefficient argument, not a numerical or geometric rank test.

The conclusion is about identities in the free universal algebra, where all universal rank-two matrix identities already hold. It does not assume, or establish, that arbitrary choices of these formal generators can occur simultaneously as representatives and normalized primitives in the geometric differential graded algebra.

## 3. Pointwise expressions and cohomology must remain separate

The scalar-primitive terms cancel from the cyclic sum, leaving

    X + Y + Z = 2(P_a + P_b + P_c).

Its three nonzero family components show that it is not the zero universal expression. This does not conflict with the imported cohomological cyclic identity. That identity uses a third-order lift in the actual smooth family and states that the relevant closed expression is exact in the actual complex.

The universal test intentionally imposes neither the primitive differential equations nor global existence and descent conditions. Universal expressions in the test need not be closed, and no cohomology class is assigned to arbitrary choices of q and t. Relations arising after imposing differential equations, choosing compatible homotopies, restricting to actual representatives, or using further geometric information are therefore outside the exclusion.

The statement that cyclic zero leaves a two-dimensional ordering quotient concerns the formal three-generator ordering space after imposing that one further relation. It does not assert that the three actual values for any selected triple have a two-dimensional span. They could satisfy additional special relations or all vanish.

For an actual defining cocycle, the trace-free projection is a chain map. The scalar part is a scalar cocycle, so the imported vanishing of scalar H2 makes that part exact. In the downstairs mixed weight-two complex the relevant scalar group is H2(P4,O(-2)), which vanishes. Thus passing to the trace-free expression preserves the actual cohomology class under the stipulated inputs; it does not turn the free universal variables into a geometric defining system.

## 4. Consequence for the four eligible components

The already-audited ordering formulas are

    m110(b,c,a) = F(a,c,b),
    m101(b,a,c) = -F(a,b,c) - F(a,c,b)
                 = -2 F_sym(a,b,c).

The universal calculation supplies only the reversal relation already included in those formulas. It therefore supplies no further constraint in the specified constant-coefficient permutation sector. In particular, vanishing of the middle ordering cannot follow solely from such a universal pointwise simplification.

This does not rule out a separate differential or geometric proof of middle-ordering vanishing. If that vanishing were proved using additional input, the imported four-component certificate says it would remove the two symmetric components while leaving the two alternating components eligible. Nor does this audit show that an arbitrary eligible four-component choice is realized by a rank-two Azumaya derived-endomorphism algebra.

## Mathematical inputs and scope

This audit read:

- rank-two-primitive-identity-boundary/PROOF.md;
- canonical-massey-detector/PROOF.md;
- equivariant-massey-multiplicity/PROOF.md and AUDIT.md;
- weight-two-massey/PROOF.md;
- family-extension-massey-constraint/PROOF.md.

The geometric, cohomological, and representation-theoretic statements imported from these dependencies remain dependencies. This audit independently checked the universal exterior signs, normalization, family-grading argument, and the logical limits of the stated exclusion. It did not independently reconstruct the underlying geometry or equivariant cohomology.
