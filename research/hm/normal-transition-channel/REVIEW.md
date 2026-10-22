# Independent review of the normalized ambient transition channel

## Verdict and frozen artifact

PASS, subject to the explicitly cited upstream geometric theorems. No required mathematical correction was found.

This review applies only to `PROOF.md` with SHA256

    2fab1f39ce7eea7bb4e3bc5999fb8a0a1d60f1b819aedd2aba482da18bad714c

The new result is the construction of the normalized, q-divisible, weight-four ambient transition cocycle and its invariant diagonal detector. It is not a new discovery of the existing first-normal invariant line, a value of that cocycle, or a complete fifth-section obstruction theorem.

I independently checked the full proof, the local proof interfaces, and the immutable published proofs of PR774 at eec909bef4a7e6998737773d5eadd0ad562e79d9, PR776 at c885531e345cc67d1848b0cd8baa0f02ca786f47, and PR777 at 490337fee9e8f06fa8bf3e893ab646a37f996bf2. I also checked the pinned full-frame Hessian and midpoint first-normal sources, the earlier full homogeneous normal-matrix coefficient source, and the same coefficient identification in PR671 at 0209666464b03a106f7409ac4c2f80fb30716e17. This is a targeted dependency and novelty review, not an exhaustive repository-wide search or a reproof of every upstream theorem.

## 1. Local normalization and the scalar cone overlap

PR777 supplies regular chartwise elimination of D12 at every point of L. Its input is an actual regular cubic/quintic pair with a base-unit multiplier, not a generic pair allowed to degenerate at an unexamined point. The proof does not silently replace this chartwise conclusion by a global gauge.

After normalization, the weight-twelve transformation law is precisely the weight-four commutator with n8. Both D12 terms vanish, so the trace-free part of Y4 belongs to the kernel of ad_n. PR776's injectivity is the correct statement in these exact weights. It follows directly from f alpha+g beta=0, deg(beta)=2<deg(f)=3, and then gamma f=0. Regular coefficient bundles permit the generic argument to extend across the base; alternatively PR777 gives the relative statement. Thus the cone correction is scalar everywhere. Scalars are removed only in the adjoint/projective layer, without assuming determinant square roots or a global scalar gauge.

## 2. The exact ambient reference and divisibility

The weight-zero transition matrices are lower triangular, with base-unit diagonal and an ordinary-linear transverse lower entry. Their products and inverses retain this form. Their lower entries involve only sums of linear entries multiplied by base functions, never a product of two lower entries. The degree-zero and degree-one pieces of the ambient transverse polynomial algebra inject into the quadric coordinate algebra. Consequently these matrices have unique homogeneous ambient lifts, and the lifts obey the cocycle identity exactly.

This is the essential reason the resulting first correction is an honest additive cocycle. A general entrywise harmonic lifting argument would not establish it.

The ambient trace-free weight-four correction restricts to zero on Q, so the principal ideal property gives A4=qZ0. Its upper entry has cover degree two, below the degree four of q, and is therefore zero. The diagonal and lower entries yield cover degrees zero and two after division. No selected source is inverted, and no regularity is lost along source zeros.

## 3. Bundle, equation-line sign, and equivariance

Direct conjugation gives t unchanged and ell transformed to (d/a)ell+(2c2/a)t. The lower-Hom line is O(-7), and a cover-quadratic positive function contributes V O(-1). Thus the lower kernel of J0 is V O(-8), not V O(-9) or a split summand imposed by hand.

Multiplication by the ambient equation carries the ideal-line factor O(-2). Hence the coefficient of the q-divisible transition is J=J0(-2), with lower kernel V O(-10) and diagonal quotient O(-2). Dividing out the local polynomial q does not reverse the ideal-line twist. An independent degree check gives the same answer directly: weight-four diagonal ambient polynomials have ordinary degree two, and lower polynomials have ordinary degree three together with lower-Hom O(-7).

The actual coordinate linearizations are retained. The positive V=Sym2 U is not exchanged with A=Sym2 W. The diagonal quotient has trivial conjugation character, q is invariant, and det(W)=1 identifies the canonical bundle of L with O(-2). The even twists have trivial central sign.

Modulo weight at least eight, products of weight-four corrections disappear. Trace-free projection commutes with conjugation, so scalar corrections cannot spoil the additive cocycle. Changing a normalized ambient frame has cone trace-free correction zero by the same commutator injection and therefore changes the q-divided cocycle by a J coboundary. Weight-zero changes identify the coefficient bundle through their exact lifts; higher changes have no effect. Applying this independence to translated atlases establishes invariance without requiring equivariant local frames.

## 4. Invariant diagonal detection and uniqueness

The cohomology calculation is correct. Both terms of the extension have zero H0. Serre duality gives H1(O(-2))=C and H1(V O(-10))=V tensor (Sym8 W)*. The character of Sym8 W is P4+D5, so its tensor product with the irreducible three-space V has no invariant. Exactness of finite-group invariants and vanishing of H2 therefore give the claimed invariant diagonal isomorphism, independently of the extension class.

As numerical consistency checks, J has rank four, degree -32, H0=0 and h1=28. These agree with the inherited identification J=P4 O(-8). The full H1 is not one-dimensional; only its invariant part is.

When kappa vanishes, its local regular primitive exists after the usual affine refinement. Two primitives differ by H0(J), hence coincide. This proves uniqueness relative to the fixed reference, and equivariance follows by translating that unique primitive. This is a conditional elimination criterion and does not prove that the actual kappa vanishes.

## 5. Section 6: nonsplitting and the inherited P4 cohomology

The independent nonsplitting argument is valid. If the extension J0 split, a global lift of the diagonal section 1 could be diagonalized by regular weight-zero lower-unipotent changes. The resulting transition matrices would commute with diag(1,-1) and thus be diagonal. The actual n8 would then have global diagonal and lower coefficients in Sym8 U O(-2) and Sym10 U O(-10), respectively. Their H0 groups vanish. But the lower entry is u(g+p f)^2, and a regular (f,g) pair cannot have g+p f=0 in a fiber. The base-unit hypothesis is used correctly. Therefore the extension class e is nonzero.

For the twist-four sequence, the boundary from H0(O(4)) to H1(V O(-4)) is cup product with e. If it were identically zero, Serre duality would make e annihilate every v* tensor h s. The multiplication H0(O(4)) tensor H0(O(2)) onto H0(O(6)) is surjective, contradicting e nonzero. The boundary is equivariant, its source is D5, and its target V tensor A=P4+D5. Hence it is injective onto D5. The resulting H0(J0(4))=0 and H1(J0(4))=P4 follow.

These groups are correctly labelled inherited, not novel: the prior exact coefficient identification J0(2)=P4 O(-4) already yields them. In particular the P4 space does not become an actual fifth-layer obstruction until its transport interface has independently been established.

## 6. Scope and remaining comparison

The whole-cone theorem concerns H1(Q,End0(F_Q)(-2)), its affine extension origin, and the bracket with the invariant N. It does not itself identify that torsor or its normalized parameter with kappa on L. The proof correctly requires a restriction/associated-graded comparison compatible with the local normalization and exact reference origin. Two one-dimensional invariant spaces alone give neither such a map nor a nonzero value.

The warning about K16 is also essential and correct. Exact multiplicativity of triangular T0 does not make conjugation preserve a harmonic q-expansion. Thus even kappa=0 does not supply a global four-q-truncated K16 lift, eliminate B1,B2,B3, or prove that this channel is the sole fifth-section obstruction.

All checks above are deductive polynomial, cohomological, and representation-theoretic checks. No actual HM/source-instance coefficient, point, derivative, matrix rank, parameter scan, or large computation was used. This review is not proof-assistant certification.
