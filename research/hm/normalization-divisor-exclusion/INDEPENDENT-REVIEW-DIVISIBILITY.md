# Independent structural review: regular source divisibility

Reviewed 2026-10-23. Verdict: **the conditional theorem is valid under the stated regular, full-cover, all-twist realization hypotheses. No substantive mathematical gap found.** This is a review of the exact local proof and pinned inputs, not authentication of an actual physical packet or an independent live-PR coordination review.

## Exact material reviewed

- Final `PROOF.md`, SHA-256 `824b6fdb62f835a21f42ad50b038c038a5c035a677f7a6cb454a31328fff1a35`, 10,950 bytes. The immediately preceding `e2484359...` version was read in full; the final paired-globality clarification was checked directly and the final hash verified. This supersedes the originally assigned `88e99095...` version.
- `inputs/normalization866.md`, SHA-256 `a7f6afe41fe569cb9a061a047b1d0a140fd198950cda6fe3bace6978f3cf0b14`, read in full.
- `inputs/pr815.md`, SHA-256 `78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236`, read in full.
- Consulted `inputs/calibration889.md`, Sections 1–2 and representation identification, and read `inputs/torsor904.md` in full for the actual-cone/associated-graded distinction.

## Checks

1. **The new scalar compatibility follows from the actual operator formula.** PR866 (N3) is defined on every local degree-one input. With contractions, comparison isomorphisms and homotopies obtained by tensoring the same maps, each composition commutes with multiplication by the section `a: O -> O(2)`. Trace-free projection does too. Substitution therefore gives `R4(aY)=aR2(Y)`. This does not follow merely from an isolated q-compatibility check, and the proof explicitly excludes that weaker premise. No derivative of a occurs.

2. **The coefficient type is correct.** PR815 (17) gives the regular marked weight-four trace map at physical twist four, with target `Sym12(U) tensor O_L`. Tensoring its physical line by `O_L(-2)` gives the corresponding twist-two map with target `Sym12(U) tensor O_L(-2)`. This is a statement about local coefficient types, not global sections of the source bundle. PR815 explicitly makes a transverse weight zero, so extracting weight four from `aR2(Y)` retains a as a factor and does not change the positive binary degree twelve. The h described as a positive quartic here is the binary `Sym4(U)` source; it is not the negative-base quadratic a. The two binary spaces U and W are not interchanged.

3. **Divisibility is regular at the entire divisor.** The quotient coefficient xi is constructed by applying regular R2 and the marked extraction to the regular source Y. It is not defined by dividing eta by a. Consequently eta is locally in the image of the sheaf map `a: T_trace(-2) -> T_trace`, including at multiple zeros. The proof would not establish this if a were inverted, the cover omitted its divisor, or the tensor/marking comparison were meromorphic.

4. **The gluing argument is valid and does not assume its conclusion.** Since nonzero a is a non-zero-divisor on the integral base and the target sheaf is locally free, multiplication is injective on sections over overlaps. If eta glues, cancellation in `a_i(xi_i - theta_ij t_ij^-1 xi_j)=0` forces precisely the prescribed transitions for xi. Thus xi becomes a global section of `Sym12(U) tensor O(-2)`, whose H0 vanishes. No claim about gluing the full operator value R2(Y), its uncontracted coefficient, or an actual cone adjoint is needed. The updated proof expressly preserves these distinctions.

5. **The normalization consequence retains its required premises.** PR866 (N1), (N13) and (N14) identify the mixed discrepancy with `-a^3 h eta` and, when the paired rho_AA is global, identify mixed gluing with eta gluing. Multiplication by h is injective on binary forms, and multiplication by nonzero a cubed is sheaf-injective, including over its divisor. Combining these with item 4 yields D6. It does not compare arbitrary global candidate responses: the stated same-source/same-lower-data realization through D5 is essential.

6. **The source-domain and realization boundaries are respected.** R4(S) is legal because R4 has the full local degree-one domain; nothing evaluates Lambda(S). Lambda remains applied to the certified corrected source `T=S-qW_h` in `im(d)`. The full lower projection y, authenticated contractions and rows, preceding division/correction and source membership remain unsupplied prerequisites. The thirteen-dimensional abstract global trace space survives: only its intersection with these regular a-divisible realized defects is proved zero. The argument neither invokes PR904's actual-global-cone vanishing theorem for eta nor removes any fifth-order boundary gate.

## Clarification incorporated

No mathematical repair is required. The final reviewed version incorporates my recommendation to repeat “assuming the paired rho_AA is global” immediately before D6. This makes the displayed conclusion's scope explicit rather than relying on the preceding paragraph. No remaining objection was found.

This review selected or evaluated no actual source, parameter, base point, coefficient, derivative, matrix or instance rank. It used no source scan, large computation, publication or external write. The only new artifact is this local review.
