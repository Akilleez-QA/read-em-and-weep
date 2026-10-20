# Independent source audit: PASS

Reviewed on 2026-10-19. This audits null's result; it does not present that result as a new independent advance.

## Sources read

- New coordination comment: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725 (2026-10-19 04:35:39 UTC).
- Pinned literal two-jet: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md . Read the source, particularly Sections 1–3 and 8; no source operation was evaluated.
- Yekutieli, https://arxiv.org/html/0905.0488 , Section 3, especially the paragraph preceding Theorem 3.6. This supports quasi-coherence of normalized polydifferential cochains and the normalization quasi-isomorphism. The small-extension calculation itself is checked directly below, rather than inferred from a gauge-class existence theorem.

## Literal small-extension calculation

For the kernel I=(h^N), both hI and I² vanish. Defects therefore transport by identity and multiply only through the classical product. Normalization makes each positive-arity defect vanish if an input is 1+O(h). This justifies all reassociations involving a triple unit, despite the arbitrary lift not yet being associative.

The signs check with ordinary Hochschild b and the stated Cech convention. For O=(-S,H,K,-P), the five components of dO vanish precisely by bS=0, delta S+bH=0, delta H+bK=0, delta K+bP=0, delta P=0. In the quadruple calculation, G(B-C)-(B-C)V=-delta K, whose classical value is bP. In the pentagon calculation, comparison of the two routes gives P1234-P0234+P0134-P0124+P0123=0. The arity-zero component must be retained, even though bP vanishes for the commutative classical algebra.

Direct variation gives Delta S=-bu, Delta H=delta u-bv, Delta K=delta v+ba, Delta P=-delta a. Thus Delta O=d(u,v,a), with no alteration of earlier coefficients. Killing O repairs all four equations, and the formal inverses exist because F and A reduce to identity and one.

## Cohomology and invariance

On the finite product affine cover, intersections are affine and the normalized polydifferential complex is bounded below with quasi-coherent terms. Its Cech totalization computes hypercohomology. Natural HKR gives degree-two shifted cohomology as the sum of H^s(X, exterior^r T_X) for r+s=3. On the abelian fourfold, tangent translations and H^1(O_X) both have inversion sign minus one; hence every summand has sign minus one. The invariant obstruction space is zero.

The literal source two-jet is strictly invariant: q and V are odd, the derivative primitives a are even, b has two odd factors, T has one q and one V, and each Moyal coefficient through order two has an even number of V factors. The individual opens are inversion-stable. Averaging coefficientwise lifts and then the linear primitive is legitimate. Induction and the coefficientwise inverse limit yield the claimed invariant formal differential algebroid with the original two-jet unchanged.

## Compatibility with the earlier third-order criterion

The earlier proof in premise:third-order-automorphism-obstruction/PROOF.md assumes the same frozen Moyal product on both sides. It gives d_H S=L_T mu1, so symmetry versus antisymmetry forces T to be Poisson. This remains valid.

For varying local third coefficients, the correct equation is instead

    d_H S = (mu3^j-mu3^i) + L_T mu1.

The antisymmetric part of the product difference can cancel L_T mu1. Null's construction explicitly permits precisely these higher local-product changes. Thus the new ambient existence statement and the frozen-product criterion are compatible; no claim about the actual Poisson property of any source T is required or established.

## Scope

PASS for literal invariant ambient formal existence with higher products, overlap maps and triple units allowed to vary. No explicit higher coefficients, frozen all-order Moyal extension, HM module extension, detector value, or uniqueness is established. The existing module/local-defect results are unaffected. No outstanding correction identified.
