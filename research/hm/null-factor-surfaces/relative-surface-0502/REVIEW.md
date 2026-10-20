# Independent audit: relative-surface simplicity route

## Verdict

The proposed generic-fiber simplicity argument is valid, subject to the stated assumption that the elliptic map is the degree-two quotient x:C→P¹ and the fourfold map is its product followed by the symmetric-product map. It does not prove global H²(End₀F)=0.

## 1. Exact degree-eight direct image

Write p=q∘(x×x), where q:P¹×P¹→Sym²P¹=P² has degree two. For a smooth elliptic double cover, x_*O_C=O⊕O(-2), so p has degree eight and

p_*O_{C²}=q_*[O⊕O(-2,0)⊕O(0,-2)⊕O(-2,-2)].

The quotient double cover q is branched over the diagonal conic, hence q_*O=O⊕O(-1). Also q*O(1)=O(1,1), giving q_*O(-2,-2)=O(-2)⊕O(-3).

For the middle terms, identify P¹×P¹ with the universal degree-two divisor D⊂P¹×P², by (u,v)↦(u,u+v). It has bidegree (2,1). Tensor its ideal sequence by O(-2,0):

0→O(-4,-1)→O(-2,0)→O_D(-2,0)→0.

Pushing to P² produces

0→q_*O(-2,0)→O(-1)³→O→0.

The last map consists of the three universal quadratic coefficients, and is the Euler sequence. Thus q_*O(-2,0)=Ω¹_{P²}. Interchanging factors gives the same result for O(0,-2). Consequently the proposed direct-image formula is exact:

p_*O_{C²}=O⊕O(-1)⊕(Ω¹_{P²})^{⊕2}⊕O(-2)⊕O(-3).

Checks: rank 8; Euler characteristic 1+2(-1)+1=0, matching χ(O_{C²})=0.

## 2. Stability really implies simplicity after this finite pullback

Let E be any slope-stable bundle on P². Stability gives Hom(E,E(-k))=0 for k>0, and Hom(E,E)=C. Tensor the Euler injection Ω¹→O(-1)³ by End(E); its target has no global sections. Hence H⁰(End(E)⊗Ω¹)=0. Projection formula and the preceding decomposition yield H⁰(C²,End(p*E))=C.

This avoids any unsupported assertion that arbitrary finite ramified pullback preserves stability. Only simplicity is needed and is proved directly.

## 3. The plane family has degree nine

Let V have dimension two and parameterize h∈P(Sym²V). Multiplication gives the subbundle

O(-1)⊗Sym²V ↪ Sym⁴V⊗O.

Its fibers are h·Sym²V, so the resulting map φ:P²→Gr(3,5) satisfies φ*O_Gr(1)=O(3). The map is injective on geometric points: the greatest common divisor of all binary quartics in h·Sym²V is h, up to scalar. Therefore φ is finite and generically degree one onto its image in characteristic zero. Its image is an integral surface of Plücker degree (3H)²=9. An embedding claim is unnecessary.

## 4. Audit of the cited HM locus

Source: Ada Boralevi, “The Horrocks–Mumford bundle restricted to planes,” https://arxiv.org/pdf/math/0602002, Theorem 3.1, pages 6–7; normalization on page 3; resolution classification on pages 5–6.

The paper uses normalized HM with c₁=-1,c₂=4. Theorem 3.1 describes the entire jumping-plane locus as a smooth degree-25 surface S₂₅, birational to Shioda’s modular surface. Thus it is irreducible. The two unstable resolution types both belong to this locus. The additional 25 planes in the main theorem concern stable restrictions; they are not additional components of the unstable locus. Their special conics lie in S₂₅.

Consequently the degree-nine image φ(P²) cannot be contained in S₂₅: containment of integral surfaces would force equality, contradicting the degrees. The inverse image of the stable locus is therefore nonempty open and dense. This argument is invariant under the choice of linear identification Sym⁴V≅C⁵ used to define HM.

## 5. Exact scope of the relative consequence

For projection C⁴→C² onto the final factors, their x-values sweep Sym²P¹. On the nonempty open inverse image of the good h-locus, each surface fiber has simple restricted bundle. A line twist N does not change its endomorphism bundle. Since K_{C²} is trivial and End₀ is self-dual in characteristic zero, Serre duality gives H²(C²,End₀(F|_{fiber}))=0 on this open. Proper flat base change then gives R²π_*End₀F=0 there (and R⁰=0 there as well).

This does not imply that R² vanishes on the excluded locus, nor that global H²(C⁴,End₀F) vanishes. In the full Leray spectral sequence the total-degree-two terms H²(R⁰), H¹(R¹), and H⁰(R²), together with differentials, still require analysis. In particular H¹(R¹) is not addressed by generic surface simplicity. No explicit HM matrix, source/jet computation, or experiment has been performed in this audit.

## 6. Review of the subsequently completed RESULT.md

The converse simplicity claim is also sound for HM restrictions. The two unstable resolutions give H⁰(E)≠0 and H⁰(E(-1))=0, so a nonzero section has no divisorial zeros and yields 0→O→E→I_Z(-1)→0. Multiplication by any nonzero linear form defines a nonzero map I_Z(-1)→O. Composing with the quotient and inclusion gives a nonzero square-zero, hence tracefree, endomorphism of E. Faithful flatness preserves its nonvanishing on pullback. Therefore the bad plane parameters are exactly the nonsimple fiber parameters.

The top-degree base-change statement in RESULT.md is correct: for this relative-dimension-two, proper flat situation, (R²r_*G)⊗k(b)≅H²(G_b), even at jumps. No naive identification R²r_*G≅(r_*G)* across the jumping locus is justified. The affine-good-open H² vanishing is valid by Leray and coherent cohomology vanishing on affine bases.

One optional strengthening: globally r_*G is already zero. It is torsion-free on the integral base (pushforward of a vector bundle along this dominant projection) and has generic rank zero by generic simplicity. Thus the global Leray caveat can omit H²(B,r_*G); the unresolved pieces H¹(B,R¹r_*G) and H⁰(B,R²r_*G), and relevant differentials, remain. This strengthening does not give the requested global obstruction vanishing.

The quantization-specific conditional deductions cannot be independently checked against the prior module-lifting report because that report was not part of this audit's inputs. Their geometric/cohomological prerequisites and the stated caution about gluing are consistent with the computations above.
