# Independent audit: full-Artin three-branch compatibility

Reviewed the relative polar construction, common-eigenline functor, spectral branch ideals, and length refinement in `PROOF.md` on 2026-10-19. This was a mathematical audit using static text only; no numerical instance was evaluated.

## Verdict

The full-Artin spectral presentation is valid under the predecessor theorem's hypotheses and the assumption of three distinct closed boundary rectangles. The first draft's possible triple function-gluing defect actually vanishes by its stronger spectral presentation. The correction below was communicated to the author before finalization.

## Checks

1. **Relative objects exist over the full polar Artin ring.** A unit polar 2-minor together with the defining vanishing of all 3-minors gives exact rank-two normal form over A, not just over its reduction. The vectors P(h), P(u) form a basis of the image. Consequently L=A P(h) is a direct summand, H is the kernel of the surjection V_A to im(P)/L, and V_A=H plus A u. Primitivity of h gives the free rank-three quotient E. The mixed symmetric form descends to E with values in K=J_A/L because P(H) is contained in L.

2. **The relative boundary functor is exact.** The unit rectangular value f(h,u,h) identifies its image line with L over every test base. The sum bundle is exactly H by the fiberwise rank test. Taking inverse images of the rank-one/rank-two splitting in H recovers the determinant and rectangular minors identically. This supplies a scheme identification, including nilpotents.

3. **Perfect forms and spectral separation lift.** A nondegenerate scalar member at the closed point lifts to a perfect form q over A. Distinct joint closed eigenvalue tuples allow a scalar member T with three distinct eigenvalues. Simple-root lifting over the Artin ring yields roots with unit pairwise differences. Polynomial interpolation and Cayley–Hamilton give orthogonal idempotent projectors and rank-one eigenbundles. Selfadjointness makes the decomposition q-orthogonal with perfect restrictions.

4. **The eigenline scheme has no hidden infinitesimals.** On the projective chart where the i-th coordinate is one, T-invariance forces its scalar eigenvalue to be the lifted root rho_i. The other equations are (rho_j-rho_i)v_j=0. Every coefficient is a unit, so all other coordinates vanish over arbitrary A-algebras. These charts prove that the full T-eigenline scheme is exactly three disjoint copies of Spec A. This proof does not assume test rings are reduced or fields.

5. **Cross ideals give exact branch equations.** Define J_ij invariantly as the image ideal of L_i tensor L_j tensor K-dual mapping to A by beta and evaluation. Its coordinate description is independent of bases. Since L_i-perpendicular is the sum of the other two eigenbundles, the common-eigenline condition is precisely I_i=J_ij+J_ik. This equality survives every base change as equality of the vanishing conditions.

6. **Two lifts imply the third with the necessary labels.** The assertion concerns two distinct closed branches over the same A-algebra. Their ideals vanish precisely when their sum Q vanishes. This implies vanishing of the third ideal, and the third lift is unique because its component is Spec(A/I_k). The statement does not assert that a closed branch lifts over all A, nor that a pair of identical lifts forces anything.

## Strengthening of the draft's length and gluing section

Let N=I_1 intersect I_2 intersect I_3. The general module computation correctly identifies the defect of

    A/N -> (A/I_1) x_(A/Q) (A/I_2) x_(A/Q) (A/I_3)

as Q/((I_1 intersect I_2)+I_3). But here J_12 is contained in both I_1 and I_2, while I_3=J_13+J_23. Therefore

    (I_1 intersect I_2)+I_3 = J_12+J_13+J_23 = Q.

The defect is zero. The diagonal map is an isomorphism of rings, not merely an injection of modules. Thus the exact geometric length identity is

    length(B_A) = length(A/N) + 2 length(A/Q)
                = 3 length(A) - length(N) - 2 length(Q).

In particular length(B_A) is at most 3 length(A)-2 length(Q). The generic example of three different lines in the square-zero two-dimensional maximal ideal shows only that equal pairwise sums alone are insufficient; it does not contradict this result because it lacks the stronger J_ij presentation.

## Scope qualifications retained

No reducedness, individual flatness, equality of branch ideals, universal lifting, or physical-source value follows. A tangent-space equality only detects the ideals modulo the square of the maximal ideal. All spectral choices are auxiliary; each branch ideal is the intrinsic kernel of its closed immersion into Spec A.

## Final revision verification

Re-read the finalized Sections 5 and 6 at 12:25 UTC. The zero-defect correction is incorporated, the scheme-theoretic union inside Spec A is correctly distinguished from the disjoint boundary components, and all stated length identities and equality conditions check.

The added first-order maps also check. Each cross coefficient c_ij lies in mK, so its class in mK/m²K canonically gives a map from the polar tangent space to K_0. Basis changes act by invertible residue transformations because c_ij has zero constant term. The ideal presentation gives exactly the displayed kernels for branch tangent images. Both scalar functionals defining q and the separating T annihilate c_ij identically. Differentiation therefore annihilates its linear term; there are no extra derivative terms because c_ij has zero residue. The two residue functionals are independent, since proportionality would make T_0 scalar. Consequently the common codimension-two target is justified. No remaining mathematical issue was found in the finalized artifact.

## Status of this record

This is a historical mathematical audit, not a new formal verification or a new execution of tests.
