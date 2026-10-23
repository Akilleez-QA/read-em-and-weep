# Independent audit of the degree-twenty-eight simple-polar exclusion

## Binding and verdict

Audited frozen proof:

    PROOF.md
    SHA256 5f145e5fb7c6b791c9200d5c58d58618312443c80cc5ae30db1dbef132a41527

The inspected companion theorem is:

    ../profile11-defect12-constant-residual/PROOF.md
    SHA256 0e28eed42faf99a0ebaed4bfcf7e54b20f0e13d642f92f61864e421043e71915
    PR801, commit 4301e3b3027afa1c32e1e7359a5fdf5b9d27edfd

**Verdict: valid.** The new proof supplies a genuine first-order obstruction in the original constant block and excludes the full label G3.11.64d33b6d4139, using the companion theorem's exhaustive source reduction. I found no substantive gap or required repair in the frozen version. The companion's separate abstract residual construction remains valid and is not contradicted.

This review independently checked the new implication and its precise use of the companion theorem. It reread the companion proof and existing review; it does not claim a new audit of every earlier catalog and source-stratum theorem imported there. Neither proof was modified.

## 1. The full derivative, not just its external projection, vanishes

The companion theorem supplies actual inclusions in the original constant thirty-space, not merely isomorphism classes:

    F=(P+2D) O(-2) subset C O,
    C=A+V+P+D,
    F^+=C O,
    0 -> F -> C O -> O(28) -> 0.

Here F has rank fourteen and degree minus twenty-eight, so the displayed quotient has the correct rank and degree. Since C O is constant, the second fundamental form of F in the original ambient bundle takes values in (C O/F)(-2)=O(26).

The companion's J=0 gives full derivative image I isomorphic to O(14). Its delta=12 and constant first transform give saturated image Ibar=O(26). Thus the inclusion of the **full** image is a nonzero equivariant map

    O(14) -> O(26).

It is multiplication by the invariant degree-twelve form f12. Consequently the full map F -> O(26) factors through multiplication by f12, and its fiber map is zero wherever f12 vanishes. This conclusion is not inferred merely from a zero external projection. There is no additional internal component in the full image that could restore a nonzero fiber value.

An invariant effective divisor of degree twelve must be a single orbit of twelve points with multiplicity one, since every projective orbit has size at least twelve. Thus f12 has simple zeros. This part does not require selecting an actual point or evaluating a derivative there.

## 2. The representation-theoretic obstruction is universal

I independently propagated the nine displayed McKay identities using the symmetric-power recurrence through degree twenty-eight. This bounded representation-ring check gave exactly

    Sym4 W  = D,
    Sym12 W = 1+A+P+D,
    Sym16 W = V+P+2D,
    Sym28 W = A+V+2P+3D.

All terms had nonnegative multiplicities and dimension n+1 at each intermediate degree. The check used only integer multiplicities in the fixed nine-irreducible representation ring, not a source-instance matrix, coefficient map, or rank experiment.

Multiplication by the fixed nonzero invariant f12 is injective on homogeneous polynomials and equivariant. The unique V summand of Sym16 therefore maps nontrivially into the unique V summand of Sym28, proving equality of the actual polynomial subspaces

    V28=f12 V16.

There is no freedom to choose a different V channel in degree twenty-eight, even though other irreducibles have higher multiplicity there.

The common-divisor argument for V16 is sound in the frozen version. The greatest common zero divisor is G-invariant. If nonempty, its degree lies between twelve and sixteen. The projective orbit sizes 12,20,30,60 force degree twelve. Its defining polynomial spans a one-dimensional G-representation, which is trivial because the binary icosahedral group has no nontrivial characters. The invariant subspace of Sym12 is one-dimensional, so this polynomial is a scalar multiple of f12. Division would then give an equivariant injection V -> Sym4 W=D, impossible for distinct irreducibles.

Hence V16 has no common zero. At every zero of f12, at least one section of V16 is nonzero. Multiplication by the simple factor f12 makes the corresponding section of V28 vanish to order exactly one. Thus V28 has zero value but nonzero first jet on the whole twelve-point divisor. The statement is universal and does not depend on a selected coefficient map or a numerical derivative test.

## 3. The actual quotient cannot lose the V channel

Let q:C O -> O(28) be the actual quotient from the companion theorem. Its global-section map is

    C=H0(C O) -> H0(O(28)).

The kernel is H0(F)=0 because F is a sum of O(-2)'s. Therefore this is an injective equivariant map, not merely a possibly degenerate abstract parameter choice. Equivariance identifies the unique V in C isomorphically with V28. Self-duality removes any convention change between W and W*, and the absence of characters removes a potential equivariant line-bundle twist.

Because q is a quotient of vector bundles, q(x) is a nonzero functional at every point. At an arbitrary point of the invariant divisor, its restriction to C_V is zero, while the restriction of its first derivative to C_V is nonzero. These two facts cannot hold if q'(x) is proportional to q(x). Hence the associated projective quotient curve has nonzero derivative there.

This argument uses the actual coefficient-map injection forced by the exact sequence. It does not assume every abstract choice of an A+V+P+D subsystem has the required kernel or first transform.

## 4. Quotient and kernel derivatives are exactly equivalent here

The constant space C supplies the original flat connection. In a local trivialization of O(28), write q as a row of functions and let s be any local section of its kernel F. Differentiation gives

    q s'=-q' s.

The quotient class of s' is precisely the second fundamental form of F. Since F is a subbundle, every vector in ker q(x) extends to a local section of F. Therefore

    beta_F(x)=0
    if and only if q'(x) vanishes on ker q(x)
    if and only if q'(x) is proportional to q(x).

The last equivalence is elementary linear algebra for a nonzero functional q(x). Changing the line-bundle trivialization multiplies the derivative by a nonzero scalar and adds a multiple of q(x); changing the local parameter multiplies it by a nonzero scalar. Thus the zero/nonzero assertion is intrinsic. The O(-2) twist is the cotangent bundle of P1 and does not change fiberwise vanishing.

Section 1 forces beta_F to vanish on the divisor, whereas Sections 2-3 and this identity force it to be nonzero there. This is the required contradiction.

## 5. Scope of the conclusion and residual compatibility

The companion theorem already reduces the full label to E10. The contradiction eliminates that remaining branch, so a full-label exclusion follows, not merely a restriction on one optional construction.

The abstract residual supplement concerns Z=O(-8)+W O(-9) inside (H/C) O. It constructs neither the original constant block F inside C O nor its degree-twenty-eight quotient with the prescribed degree-twelve vanishing of the full derivative. A valid residual in H/C therefore does not supply the object ruled out here. Conversely, excluding the original constant block does not invalidate the residual family.

The result is a first-order formal-branch obstruction. It makes no claim of actual-source realization, higher-order lifting, algebraicity, SF>=4, or completion of the larger research goal. The audit used only universal bundle/connection reasoning and bounded representation identities. No selected actual HM/source-instance coefficients, parameter values, points, derivative evaluations, matrices, source-instance ranks, model experiments, scans, or large computation were used. There were no external writes or publication actions.
