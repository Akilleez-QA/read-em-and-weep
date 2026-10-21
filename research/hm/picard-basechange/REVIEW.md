# Independent review: faithful-column parameter base change

Status: PASS, independent mathematical review of `PROOF.md` completed. Not formally checked.

## Pinned inputs checked

I read the exact GitHub files at PR584 commit `df1e09bb456974ec43ab598709bd60d0378cfedf`, `research/hm/picard-defect-singularity/PROOF.md`, and PR585 commit `257777c4451d16201202d18f227ff82d5e30956c`, `research/hm/picard-blowup/PROOF.md`. These establish the actual residue-complex input. The present audit does not independently rederive its geometric provenance.

## Independent algebraic checks

1. For an arbitrary C-algebra B receiving A, the residue module E_B is identified with T_B=R⊗_C B by branch scaling with the unit t1. The inherited inclusion of m_B is retained; forgetting its branch scaling would misidentify the extension class. The quotient map β:E_B→B is surjective, and its kernel is m_B.

2. The A-complex `[E_A→A⁴]` is bounded and termwise A-flat. Thus its parameter-derived tensor product with B is the termwise complex `[E_B→B⁴]`, without any flatness hypothesis on A→B. Independently, the length-one A-free resolution of K gives Tor_1^A(K,B)=Ann_B(IB), with all higher Tors zero. The faithful-column condition is exactly the vanishing of this Tor_1, not an assertion that B is flat.

3. Under Ann_B(IB)=0, the kernel of δ_Bβ is m_B and the cokernel is K_B. Without faithfulness, the correct general formula is an exact sequence `0→m_B→H⁰→Ann_B(IB)→0`. This distinguishes recomputed cohomology from blindly pulled-back endpoints.

4. The nodal resolution of C has finite-rank free terms: d1=(s,t), followed by alternating diag(t,s) and diag(s,t). Tensoring over C gives a T_B-free resolution of B even if B is nonreduced or nonflat over A. Since all free terms have finite rank, the Hom complex with m_B is the original Hom complex tensored over C with B. Therefore Ext¹_(T_B)(B,m_B)=B². This uses only scalar extension over the field C, not regularity of B or of the four δ_i.

5. In the normalization-residue basis, the extension `0→m_B→E_B→B→0` is the pullback of the normalization extension along b↦(t1b,b). Its class is (t1,1). In particular its second coordinate remains a unit over every B.

6. The faithful-column exact sequence `0→B→B⁴→K_B→0`, regarded as T_B-modules via residue, supplies the injection `(B/IB)²→Ext²_(T_B)(K_B,m_B)` in its long exact Ext sequence. This is not claimed to compute the entire Ext² group. The injection sends (t1,1) modulo IB to the actual complex's Postnikov class by Yoneda composition. Its cyclic B-submodule is exactly B/IB, so the exact parameter annihilator is IB, not merely its radical. The argument works for nonreduced IB and even IB=B, when the class is zero and its annihilator is B.

## Localization and scheme-level checks

No assertion that T_B is noetherian is needed or should be inferred merely because B is a noetherian C-algebra. For a prime p of B, localize the faithful column (which preserves injectivity), then redo the preceding nodal free-resolution and Ext long-exact-sequence calculation over B_p. This directly computes the Postnikov class of the localized complex. It is nonzero precisely when IB_p is proper, namely p∈V(IB). This method does not require an unproved identification between localized Ext and Ext of localized modules.

Outside V(IB), a coordinate of δ is locally a unit. An elementary target-basis change gives `[E_B→B]⊕B³[-1]` locally, and the first block is quasi-isomorphic to m_B. Thus the result determines the parameter-local splitting locus. It should not assert an unproved global splitting over the entire complement.

For a locally noetherian integral scheme X and a dominant morphism X→Spec A, each nonempty affine open has a domain as coordinate ring and receives A injectively: the generic-point map induces an inclusion of function fields. At least one δ_i is consequently nonzero, so the pulled-back column is injective on every such affine open. The preceding theorem applies. This means an integral source and a dominant morphism; the morphism itself need not be integral. Nonproper dominant morphisms can omit the center entirely. If the morphism is proper and dominant, its image is closed and dense, hence is all of Spec A, and the nonempty uniform center has nonempty preimage. The family then cannot be split everywhere. This includes proper dominant alterations and modifications with integral source.

The annihilator assertions can be interpreted as the annihilator of the canonical local Postnikov section in the sheafification of the relevant Ext presheaf. The kernel of multiplication by that section is locally IB by the direct affine calculation and hence is I O_X. Its cyclic image is O_X/I O_X. No global Ext decomposition is necessary.

## DVR and uniform-restriction checks

For B=C[[u]], with at least one nonzero pulled-back δ_i, write IB=(u^m), where m=min_i ord_u(δ_i). Dividing the column by u^m gives a unimodular column. A target-basis change sends it to a coordinate vector, so K_B≅B³⊕B/(u^m) and the complex becomes `[E_B --u^mβ→ B]⊕B³[-1]`. Its class has exact annihilator (u^m). When m>0, the cyclic obstruction has B-length m; when m=0, it vanishes. Under a local map of DVRs with u↦a(v)v^e and a(v) a unit, the ideal becomes (v^(em)); contact thickness is multiplied by the ramification index. No dominance of the arc onto the full thirty-dimensional parameter space is required.

If all δ_i vanish in a nonzero B, the faithful-column hypothesis fails. The actual termwise derived pullback is the zero-differential complex E_B⊕B⁴[-1]. Its degree-zero cohomology is E_B, not m_B, and Tor_1^A(K,B)=B. Thus restriction entirely into the uniform locus is split but does not contradict persistence under faithful-column base changes.

## Scope

All claims concern the actual pinned one-node relative residue complex and its ordinary cohomological splitting. They do not determine a selected HM/source instance, the full adjoint obstruction, multiplicative formality, or higher-order lifting. No public write or selected-instance evaluation was performed for this audit.

## Final manuscript assessment

I subsequently read the complete new `PROOF.md`, sections 1–6, against the independent checks above. No mathematical correction is required. Its stated hypotheses and conclusions are justified; in particular it handles the unit-ideal case, distinguishes an integral source from an integral morphism, recomputes localized Ext instead of assuming an unjustified localization theorem, and does not incorrectly force nonproper dominant maps to meet the center. The general nonfaithful H⁰/Tor formulas and DVR contact-length refinement are correct. The local-to-scheme conclusion is carefully phrased as a local annihilator assertion rather than a global Ext decomposition.

The theorem is conditional on the pinned actual normalization/residue input, exactly as disclosed in the manuscript. PASS is an independent mathematical assessment, not formal verification.
