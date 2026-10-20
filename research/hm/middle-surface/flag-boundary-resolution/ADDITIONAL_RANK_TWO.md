# Rank-two boundary points have only finitely many limiting supports

This supplements Sections 4A–4B of PROOF.md. All hypotheses, particularly global repeated-input injectivity and the canonical supported correction on the dense good locus, remain in force. Work over C.

## Statement

At a middle point b with rank Q_b=2, the set of limiting support hyperplanes H from the good locus has at most six distinct members. Unlike the rank-three and higher statement, uniqueness is not asserted.

Consequently the full-flag positivity argument sharpens the boundary alternative to:

    the bad middle locus contains a curve;
    or a point of rank Q≤1 has a positive-dimensional family of limiting H.

Thus a finite bad locus on a middle surface with rank Q≥2 everywhere is impossible. No assertion excludes the remaining ranks zero and one.

## 1. The annihilator pencil and its factors

Set E=V/U_b, so dim E=4. Let K=ker Q_b⊂Sym²E; its dimension is eight. Under the perfect symmetric pairing put

    P=K^⊥⊂Sym²E*,    dim P=2.

For every limiting support three-plane A⊂E, the proper augmented kernel/support graph of PROOF.md provides a five-plane K_A⊂K∩Sym²A. Therefore

    rank(P→Sym²A*)≤1.

There is a nonzero quadratic form q∈P restricting to zero on A. If m is a defining linear equation of A, divisibility by the equation of a hyperplane gives q=mℓ for some linear form ℓ. In particular q has rank at most two.

Each fixed nonzero quadratic form has at most two distinct linear factors up to scalar. Consequently infinitely many limiting A would require infinitely many points [q]∈P(P) with rank q≤2. This rank condition is closed; because P(P) is a projective line, it would follow that every q in P has rank at most two.

The limiting-support set itself is closed and projective, being the image of the proper flag fiber over b. An infinite such set has a positive-dimensional irreducible component. In what follows suppose such a component exists.

## 2. The bounded-rank pencil classification

The bounded-rank-two Schur-complement argument in `/research/hm/normalizer-rank-five/extremal-kernel-planes/PROOF.md`, Section 2, applies unchanged to a two-dimensional space of symmetric forms until its concluding dimension count. Its conclusion for P is:

    (i) P⊂Sym²M for a two-dimensional M⊂E*;
    or
    (ii) P=ℓ M for a nonzero ℓ∈E* and a two-dimensional M⊂E*.

For clarity, the dimension-independent part of that proof chooses a rank-two member with hyperbolic block J, writes any other member in blocks (B,C;Cᵗ,D), and applies the rank bound to J+t(B,C;Cᵗ,D). The Schur complement forces D=0 and CᵗJC=0. The linear space of cross-blocks must use one of the two isotropic lines of J, since a linear space cannot be the union of two proper linear subspaces. If all C vanish, the forms are supported in a fixed binary M. Otherwise one fixed row of C is zero and the corresponding opposite diagonal entry of B must vanish, yielding a common linear factor ℓ. The inverse image under multiplication by ℓ has dimension dim P=2. A rank-two member exists: a two-dimensional space consisting only of rank-one symmetric forms is impossible, since the sum of two independent squares has rank two.

This invokes the established elementary proof rather than assuming that a pencil can be extended to a three-dimensional bounded-rank space.

In case (i), every linear factor of every member belongs to M. In case (ii), the factor set is the fixed factor [ℓ] together with the projective line P(M). Hence, in either case, every positive-dimensional component of varying factors is contained in P(M), and is dense there. The corresponding varying supports are

    A=ker m,    [m]∈P(M).

Their common intersection is the fixed two-plane W=ann(M)⊂E.

## 3. The common binary kernel and correction contradiction

In both classified cases every form in P vanishes on W. Therefore

    Sym²W⊂K.

For all but at most one of the varying supports A=ker m, the restriction map P→Sym²A* has rank exactly one. Indeed rank zero says every member of P is divisible by m; two independent quadrics can have at most one common linear factor, because two distinct common factors would make them proportional. Rank at most one is already known for the limiting supports under consideration.

For such a general A,

    dim(K∩Sym²A)=6−1=5,
    K_A=K∩Sym²A⊃Sym²W.

Use the regular ambient correction constructed in PROOF.md Section 4B. The closed supported-correction incidence gives

    v_b(K_A)⊂A.

Thus v_b(Sym²W) lies in every general varying A. Their intersection is W, and hence

    v_b(Sym²W)⊂W.

The homogeneous binary cubic e↦e∧v_b(e²) has a projective zero. This supplies a nonzero e∈W with e²∈K and v_b(e²)∈Ce, a compatible square. Global repeated-input injectivity forbids it. Therefore the assumed positive-dimensional family of limiting supports cannot exist.

Since the support-limit set is projective, it is finite. Finally, the positivity theorem in PROOF.md forces a positive-dimensional support-limit family at some point whenever the bad locus is finite. Ranks three through five have unique limits and rank two has finitely many; consequently that point has rank at most one.

## 4. An optional uniform bound of six

If the annihilator pencil P is not entirely of rank at most two, some 3×3 minor is a nonzero homogeneous cubic on P(P)≅P¹. All rank-at-most-two pencil members are zeros of that cubic, so there are at most three distinct such members. Each has at most two distinct linear factors; Section 1 then bounds the number of limiting supports by six.

If the entire pencil has rank at most two, use Section 2. Apart from at most one exceptional support defined by a common factor of all members, every possible limiting support belongs to the hyperplane pencil with base W and has restriction rank exactly one. There cannot be two distinct such nonexceptional supports A and B: both their limiting kernels contain Sym²W, so correction incidence gives v_b(Sym²W)⊂A∩B=W, already yielding the forbidden binary compatible square. Thus in this case there are at most two limiting supports in total.

The weaker common bound of six therefore applies in every rank-two case. It counts distinct geometric support limits; no scheme-length or multiplicity bound is asserted.

## Scope

This is a pointwise finiteness and distinct-limit bound, not a statement that all rank-two points have a unique limit. It uses only kernel/support incidence, regularity of the correction, the elementary bounded-rank pencil classification, and square avoidance. It makes no physical-source computation and leaves the possible rank-zero and rank-one boundary configurations unresolved.
