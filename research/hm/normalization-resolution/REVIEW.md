# Independent structural review

Verdict: PASS.

Review date: 21 October 2026.

Reviewed `PROOF.md` and the available copy of Sections 1–2 of its cited PR588 dependency. This is an independent mathematical review of the structural argument, conditional on its explicitly recorded geometric inputs. It is not a formal verification, a new audit of the original pinned repository sources or BHM, or a selected-source coefficient, point, matrix, or rank evaluation.

## Derived construction and exactness

The shifts and three cone constructions are correct. With a sheaf V[-1] in cohomological degree 1, the first cone is [E→F] in degrees 0,1; the second is [E→F→G] in degrees −1,0,1; and the final cone is [E→F→O⊕G] in degrees −2,−1,0.

The chain-map representability lemma applies in both places where it is used. Componentwise higher Ext vanishes in the required direction, so the hyper-Ext spectral sequence computes morphisms by the ordinary global Hom complex. The possibly nonzero reverse group Ext⁴(O,O(−5)) is not among those groups and introduces no obstruction. No global tilting assertion or termwise-exact pushforward is assumed.

Finiteness of the restriction of p makes the final cone concentrated in cohomology degree zero. The resulting sheaf resolution is therefore exact. Passing to all twisted global sections is also justified: H¹(E(n))=H¹(F(n))=H²(E(n))=0 yields surjectivity onto H⁰(D(n)) and H¹(D(n))=0 for every integer n. This gives the asserted graded resolution, not merely a possible Betti table.

All differential entries have strictly positive degree. Minimality, projective dimension 2, depth 3, and Cohen–Macaulayness follow as stated.

## Checked corollaries

- The added all-integer vanishing is correct: H²(F(n))=H³(E(n))=0 gives H²(D(n))=0, and H¹((O⊕G)(n))=0 then gives H¹(X,nH)=0 for every integer n. This uses only the same resolution and finite projection.
- Regularity is max{0,2,3−1,5−2}=3.
- Multiplying (1+2t+8t²+4t³) by (1−t)² gives 1+5t²−10t³+4t⁵. Thus the stated Hilbert series, h-vector (1,2,8,4), and multiplicity 15 are correct.
- The all-twist resolution gives the displayed binomial formula. The values in degrees 0 through 6 are indeed 1,5,20,50,95,155,230.
- Dualizing against P(−5) gives 0→P(−5)⊕P(−3)^5→P(−2)^10→P^4→ω_N→0. Since N is Cohen–Macaulay of codimension 2, the other Ext groups vanish and the dual complex is exact in the claimed places. Its maps remain minimal.
- Consequently the canonical module has four minimal generators, all in degree zero; the Cohen–Macaulay type is 4 and the a-invariant is 0. The level assertion is valid in the explicitly stated sense of a canonical module generated in one degree. N need not be standard graded as a C-algebra; no such stronger assertion is needed.

## Unit and quotient caution

The O summand maps by the actual unit because it comes from the final cone triangle. It does not give an injective P summand in N: its kernel is the homogeneous ideal I_S. Removing this summand leaves middle cohomology rather than an exact resolution.

The warning about N/im(P)→Γ_*T is also correct. In each degree its kernel is H⁰(O_S(n))/im H⁰(O_P4(n)), canonically H¹(I_S(n)) since H¹(O_P4(n))=0. Thus the caution does not conflate the nonambient section quotient with its conductor image. No new conductor-map rank is inferred from the free resolution alone.

## Source status and scope

The proof identifies the relative Pfaffian model and finite normalization identification as prior inputs, and its cited dependency records those exact inputs. The final source wording provides an immutable repository citation. The text correctly distinguishes a structural derivation from a selected-instance computation and explicitly disclaims historical novelty relative to BHM. No unproved novelty claim remains.

Final status: PASS. No mathematical correction is required. This review covers the final all-integer vanishing addition and revised source-status wording, as well as the resolution and canonical-module consequences.
