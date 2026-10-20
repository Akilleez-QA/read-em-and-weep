> Historical mathematical review retained with the source. This is not a new independent review or a formal verification certificate.

# Structural audit: exclusion of splitting on deep conic thickenings

Assume the displayed complex is exact as a complex of locally free sheaves on P², with cokernel the rank-two vector bundle E, and C is a plane conic. No matrix entries or ranks are evaluated here.

## Verdict

The proposed argument rigorously excludes a direct-sum decomposition of E|_{nC} into two line bundles for every integer n ≥ 9. Its cohomological bounds and shifts are correct. The global-generation argument for injectivity can be strengthened substantially, but the supplied dimension-two vanishing argument still has its first guaranteed surjectivity at n = 9. No claim that this is the optimal geometric threshold is justified by this audit.

## Cohomology check

For any locally free resolution ... → A₂ → A₁ → A₀ → F → 0 on a surface, H¹(A₀)=H²(A₁)=0 imply H¹(F)=0, and H²(A₀)=0 implies H²(F)=0. This follows by breaking the resolution into short exact sequences and using vanishing of H³ of coherent sheaves. No conditions on the earlier terms are needed.

Here A₀=15O(-8)⊕4O(-6), A₁=35O(-10). Since H¹(O(k))=0 for every k on P² and H²(O(k))=0 for k≥-2, this proves:

- H¹(E(t))=0 for t≥8;
- H²(E(t))=0 for t≥6.

The canonical rank-two identity E* ≅ E⊗det(E)⁻¹ gives E* ≅ E(2). Tensoring the resolution by E*(t) stays exact. Its final two terms are 15E(t-6)⊕4E(t-4) and 35E(t-8), so the same lemma proves H¹(End(E)(t))=0 for t≥14.

The trace pairing gives a nondegenerate identification End(E)* ≅ End(E), with no need to divide by the rank. Serre duality gives H¹(End(E)(-2n))* ≅ H¹(End(E)(2n-3)). Thus the needed negative-twist H¹ vanishes when 2n-3≥14, i.e. n≥9.

## Injectivity check

The quotient presentation gives global generation of E(8). Twisting E*≅E(2) gives global generation of E*(6). Tensor products of globally generated bundles are globally generated, so End(E)(14) is globally generated. Dualizing a generating surjection and using self-duality yields End(E)↪O(14)^N. Hence H⁰(End(E)(-2n))=0 for n≥8.

For the effective Cartier divisor nC, its ideal is O(-2n), so the exact restriction sequence is

0 → End(E)(-2n) → End(E) → End(E)|_{nC} → 0.

Restriction commutes with the endomorphism bundle because E is locally free. The two vanishings give an isomorphism of unital algebras H⁰(End(E)) → H⁰(End(E|_{nC})) for n≥9.

## Idempotent and contradiction

A decomposition into two line bundles on nC produces a projection idempotent that is neither zero nor the identity. Lift it through the algebra isomorphism. Injectivity ensures the lift remains idempotent. An idempotent endomorphism of a vector bundle splits it into locally free image and kernel. Their ranks are locally constant, and restriction to nC shows both have rank one. Since Pic(P²)=Z, the global splitting is E≅O(l)⊕O(-2-l). This would give c₂(E)=l(-2-l)=1-(l+1)²≤1, contradicting c₂(E)=16.

The line bundles on the nonreduced scheme nC need not themselves be restrictions of line bundles from P²; the idempotent argument avoids that potential pitfall entirely.

## Sharper auxiliary bounds without matrix evaluations

Global generation of E(8) and the Chern classes alone improve the H⁰ and H² bounds. Let O(a)⊂E be a saturated rank-one subsheaf. On the smooth surface it is a line bundle, and its quotient is I_Z(-2-a) for a zero-dimensional subscheme Z. Therefore

length(Z)=16+a(a+2)=a²+2a+16,

and I_Z(6-a) is globally generated. Put d=6-a. Two suitably general degree-d sections have no common curve and their intersection contains Z, so length(Z)≤d². The case d=0 would force Z empty and is already incompatible with the Chern classes. Thus

a²+2a+16≤(6-a)², hence 14a≤20 and a≤1.

(In this argument one may extend the ground field to an algebraic closure; all claimed vanishings descend.) A nonzero section of E(-2) would saturate to a line subbundle of degree at least 2, so H⁰(E(-2))=0. Serre duality then improves the earlier bound to H²(E(t))=0 for t≥1.

Likewise, a nonzero map E→E(-d) with d>0 has trace and determinant zero, and its twisted square vanishes by Cayley–Hamilton. Its saturated kernel O(a) has a≤1, and its image lies in O(a-d). The induced nonzero map I_Z(-2-a)→O(a-d) forces 2a+2-d≥0 (Hom(I_Z,O)=O on P²). Therefore d≤4. In particular H⁰(End(E)(-2n))=0 already for n≥3.

These refinements do not improve the claimed n≥9 conclusion by the displayed cohomology argument: at n=8 one needs H¹(End(E)(13))=0. The improved H² bound removes that obstruction from the penultimate term, but the final term still contains 15H¹(E(7)), whose vanishing is not supplied. Proving n=8 by this approach requires additional structural information or a further independent theorem; failure of the sufficient vanishing test does not establish actual splitting at n=8.

## Audit of PROOF.md

The accompanying PROOF.md was inspected in full. Sections 1–4 implement the argument above correctly, including the justification for exact pullback of a vector-bundle resolution and the distinction between indecomposability and simplicity. The imported geometric identification and original HM resolution are treated as prior established inputs, not independently reverified here.

The scope warning in Section 5 is essential and correct: the conclusion is failure of a full line-bundle direct-sum decomposition by X₉, not failure of the maximal line to lift by X₉. A line may continue to lift inside a nonsplit extension. At the first nonsplitting layer m, vanishing of the positive extension group follows from H¹(P¹,O(d−4m))=0; for even d this holds when d≥4m. The actual upper range d≤20 does not provide the uniform d≥32 condition through m=8. Thus no conclusion about a nonzero negative-root obstruction by the ninth thickening is being made. The local identifications of obstruction and extension groups are imported from the cited prior lifting analysis.

The auxiliary improvements above are optional and independent of the main proof. They should not be read as sharpening the first nonsplitting order or determining a maximal-line obstruction.
