# The conic scalar-lift correction has a regular commutator preimage

## Bounded actual application

The actual global Serre lift adds sigma r_i to the homogeneous pair, where each r_i has positive-cover degree eight. On a complete regular vertex chart the actual zero ideal is the regular pair (f,g) of degrees three and five. Its quotient has socle degree six, so r_i belongs to (f,g). Locally choose regular coefficients p,q such that

    r=fp+gq,     deg_positive(p,q)=(5,3).

Such regular local lifts follow from the surjective degree-eight Koszul map. They can also be chosen on each affine base chart: its kernel is a line bundle and affine H1 vanishes. This is an existence statement for regular coefficients, not a selected source-instance calculation.

Put sigma=(f,g)^t, J0=[[0,-1],[1,0]], and n=sigma sigma^t J0. The trace-free endomorphism

    B=sigma (p,q) - (r/2) I
     = [[(fp-gq)/2, fq],[gp,(gq-fp)/2]]

satisfies the exact universal identity

    [B,n]=r n.                                               (1)

Indeed B sigma=(r/2)sigma, and the determinant pairing gives sigma^t J0 B=-(r/2)sigma^t J0. This proves (1) without division by f or g.

With tau(V)=sigma V^t J0+V sigma^t J0, one has tau(sigma r)=2rn. Therefore a local identity

    E_hom=[K_hom,n]

changes under the actual scalar-lift subtraction to

    E_hom-tau(sigma r)=[K_hom-2B,n].                         (2)

Thus this particular higher scalar correction has a REGULAR local commutator preimage. It is not an obstruction to local cancellation.

## Exact ambiguity

For a regular pair, two lifts of r differ by its Koszul syzygy:

    (p',q')=(p,q)+ell(g,-f).

Consequently

    B'-B=ell n,
    (K_hom-2B')-(K_hom-2B)=-2ell n.

The difference centralizes n. In the homogeneous degree-eight calculation ell has positive degree zero. This records an ambiguity rather than declaring it irrelevant at all later orders.

Intrinsically, a local functional alpha with alpha(sigma)=r gives B=sigma⊗alpha-(r/2)Id. The displayed local matrices are its oriented coefficients. The argument is invariant under compatible Serre frame changes.

## A precise second-normal degree consequence

The new correction has entry degrees

    B11:8,  B12:6,  B21:10.

For the established first-normal Hessian symbol t, the off-diagonal degrees are t12:2 and t21:6. The nilpotent entries are n12:6 and n21:10. In the universal second-normal formula, the old-connection terms in the diagonal are

    K12 t21-K21 t12+B1(K12,g²)+B1(K21,f²).

The second transvectant B1 lowers total positive degree by four. Substituting the correction -2B makes EVERY displayed term have degree twelve: 6+6, 10+2, 6+10-4, and 10+6-4. The syzygy ambiguity ell n has the same degrees. Hence this specific scalar-lift correction, and its displayed choice ambiguity, contribute nothing to the degree-four homogeneous part of those second-normal terms.

This is a local graded identity. It does not prove that a global fourth obstruction is determined solely by degree four. Such a conclusion needs the actual filtered cohomology and endpoint comparison. Other normal-frame terms, the actual endpoint variation, and the failure of a global midpoint extension to 3Q remain separate issues.

## Scope and dependencies

The actual r_i and their degree are supplied by ACTUAL-GLOBAL-SERRE-LIFT-FROM-THE-CONIC-COCYCLE.md. The homogeneous identity is in UNIVERSAL-HOMOGENEOUS-FIRST-NORMAL-CONNECTION-CANCELLATION.md. The second-normal old-K terms are in UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md.

This note does not identify K_hom-2B with the complete actual normal connection, prove its required overlap transport, or evaluate the endpoint or fourth Bockstein. It resolves only the explicitly displayed scalar-lift contribution, with its remaining centralizer ambiguity. All coefficients are unassigned universal symbols; no actual point, coefficient choice or instance-rank experiment is used.

Run python3 verify_conic_scalar_commutator_preimage.py for the exact universal matrix identities and degree calculation. The geometric regular-pair and actual-lift inputs are the stated dependencies.
