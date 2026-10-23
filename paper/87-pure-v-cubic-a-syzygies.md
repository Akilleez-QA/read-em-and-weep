# Cubic A syzygies on the order-three gate line

**Craig Ward · 23 October 2026 · PR1053**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/9658196f793afda6767565307ebc818ddfe341a5/research/hm/source2-pure-v-cubic-syzygies/PROOF.md).

## Exact equivariant kernel, not a Chern-class guess

On the nonzero universal line ℓ₃=span(R₁−2R₂), the four nonics F=N L(R₁−2R₂) have an equivariant Hilbert-Burch resolution

    0→A O(-12)→P O(-9)→I_B→0.

Thus the normalized nonic kernel bundle is K_F=A O(-3), **not V O(-3)**. Its homogeneous component ideal is saturated and has length 54. This refines the already completed component-scheme classification on one exceptional line; it does not select the actual coefficient ratio.

## Whole-polynomial certificate

Over K=Q(√5), a general cubic syzygy has forty coefficients. Equating all degree-twelve coefficients gives a 91×40 matrix of rank 37, hence a three-dimensional solution space. This rank is a universal coefficient-system rank, not an evaluated HM map rank.

The public S.json supplies all entries of a 4×3 cubic matrix S. The certificate verifies FS=0 and, for every deleted row i,

    (-1)^i det(S with row i deleted)=(9√5/2050)F_i.

The common scalar is nonzero. All four full polynomial identities are checked, rather than just zero sets or one nonzero minor. Consequently the maximal-minor ideal equals the raw homogeneous ideal (F) on this line. This particular equality must not be confused with the earlier comparison of differently graded F and FL ideals, which is only an ideal-sheaf comparison.

The known nonempty finite projective scheme gives height two. Hilbert-Burch therefore gives the genuine minimal graded resolution 0→K[p,q,t](-12)³→K[p,q,t](-9)⁴→(F)→0. Its quotient has depth one, so there is no irrelevant-maximal-ideal torsion and (F) is saturated. The Hilbert numerator 1−4t⁹+3t¹² recovers length 54; that number is a consistency check, not the reason for splitting.

## Why the representation is A

The cubic syzygy space factors through A₅ and has dimension three. The possibilities are A, V or three trivial representations. The exact action of a pinned binary-icosahedral generator is computed on all forty coefficients by S_j(a)↦P_g S_j(A_g⁻¹a), retaining the complete change-of-basis identity. Its trace is (1+√5)/2, distinguishing A from V, whose trace is (1−√5)/2, and from three trivial representations. The canonical evaluation isomorphism then identifies K_F equivariantly with A O(-3).

## Original-fourth consequence and limits

Substitution into the [kernel bridge](86-pure-v-kernel-bridge.md) gives

    0→O(-4)→K_H→E→0,
    0→E→A O(-2)→C_L→0.

E remains locally R²⊕m at all ten order-three axes, with nontrivial local Koszul extension and double dual A O(-2). Its defect C_L has length ten. The second Chern numbers are 27 for K_F, 22 for E and 46 for K_H; K_H has rank four and c1=−10h. No splitting of K_H is asserted. These are conditional restrictions if the unknown nonzero gate lies on ℓ₃, not an assertion that it does or that the source is excluded.

Exact coefficient, maximal-minor and group-action checks support the written height, Hilbert-Burch, saturation and equivariance arguments. They do not evaluate an actual source or choose either gate coefficient.
