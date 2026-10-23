# The actual invariant-quadratic image and transversality

**23 October 2026, PR1082 update:** [Actual quadratic commutation excludes endpoint nine](109-small-branch-exclusion.md) under the full source2 pure-V compatible-radical hypotheses. Any endpoint-nine conclusions below remain valid conditional deductions with an excluded antecedent, not active results for the surviving endpoint sixteen. In particular the nonzero-conic and positive Smith/maximal-row-rank implications do not solve its positive component. The universal component-scheme classification is unchanged.


**Craig Ward · 23 October 2026 · PR1065**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/fd75633464cd587856287cc7866520fb4105ef5b/research/hm/source2-pure-v-q-transversality/PROOF.md).

## Later refinement through PR1075

PR1075 now proves Q(NC2)∩NC4=0 in all endpoint-sixteen branches, including nonzero N0 projection. The residual-large-only restriction below is the earlier PR1065 boundary, now superseded. No Q-preservation of NC or NR follows. [Full theorem](105-nonzero-small-transfer.md).

## A new actual image in every remaining branch

Define U_Q=Q(NC2), using the invariant quadratic Q, not the negative quadratic descendants of P_h. Under compatible pure-V radical,

    ker(Q|NC2)=I2,
    U_Q≅NC2/I2=V+P+D,       dim U_Q=12,
    U_Q⊂ker h.

Since NC2 contains no A and ker Q=A⊕I2, its kernel is exactly the specified I2. Also j2 kills NR2, so hQ=j2 puts this image in ker h. The marked canonical quartic is therefore disjoint from U_Q.

## Its intersection with I4 detects the endpoint branch

The actual isomorphism Q|P_h:P_h→I4 gives

    Q⁻¹(I4)=ker Q⊕P_h=A⊕I2⊕P_h.

Intersecting with NC2 removes A and retains precisely I2 and, if present, all of P_h. Equivariant isotypical projections justify this step even when P_h is a graph in a larger P-isotypical space. Applying Q yields

    U_Q∩I4=I4   in endpoint dimension nine,
    U_Q∩I4=0    in endpoint dimension sixteen.

There is no intermediate nonzero intersection. Accordingly NC2/I2→N4/I4 is injective in the sixteen-dimensional case; in the nine-dimensional case it has kernel P and image dimension eight. Neither result selects a branch.

## Stronger statement only in residual-large

Assume zero actual N0 projection of P_h but nonzero projection to N8. The [residual-string theorem](96-canonical-residual-string.md) then gives ker h∩NC4=I4. Any element of U_Q∩NC4 must lie in I4 because U_Q⊂ker h; the endpoint-sixteen intersection result forces it to be zero. Hence

    U_Q∩NC4=0,
    NC2/I2→N4/NC4 is injective.

The actual direct sum NC4⊕U_Q has dimension 21 and character V+2P+2D. This agrees with the character of NR4 but **does not identify these subspaces**. In particular Q(NC2) is not asserted contained in NR4. Q is not assumed to preserve NC or NR.

This stronger transversality is not asserted in the endpoint-sixteen branch with nonzero N0 projection. The theorem supplies no new original Bockstein vanishing, coefficient value, residual coupling or source exclusion. The actual preimage and intersection arguments, rather than synthetic rank tests, establish the conclusions.
