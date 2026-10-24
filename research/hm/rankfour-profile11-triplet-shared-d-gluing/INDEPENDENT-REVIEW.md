# Independent whole-proof review

Result: PASS for the complete, exact final proof identified below. No mathematical correction is required within its stated conditional scope.

- PROOF.md: 20,361 UTF-8 bytes; SHA256 `7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7`.
- verify.py: SHA256 `3ec7ff5fa934a8e2cd4060bbed9bb3b6acc8ad08cacd199ba5f4a578407e8d0e`.
- characters.py: SHA256 `c19423adfb673352bc313c027c2e115dbf3c7b0f01802e452da2d2524b6eaef7`.
- REPRODUCE.md: SHA256 `23af2348db82b8ae8be8c419fa3d9459633f551b3932021c0720d1c2d84807f4`.

This review covers the entire final PROOF.md, including Section 10. It is not a review of the superseded follow-on draft, and any substantive change to the final proof requires a new review binding.

## Source authentication and replay

I read INPUTS.json and all four complete retained input texts. I independently fetched each source through the GitHub read tool at its exact repository, immutable commit and path. For every response I recomputed its UTF-8 byte count, SHA256 and Git blob SHA1, checked the returned Git blob ID and exact URL, and compared the complete bytes with the retained input. All checks agree. REVIEWER-SOURCE-AUTHENTICITY.json records the compact exact evidence. Duplicate raw responses are local audit material, not publication dependencies.

I inspected the entire checker and character helper. In a fresh temporary directory containing only PROOF.md, verify.py, characters.py, INPUTS.json and the four inputs/*.md files, both `python verify.py` and `python -O verify.py` passed all 77 checks. No raw response, prior packet, or external state was present. REVIEWER-CHECKS.json binds every selected file and both results. A separate exact class-character calculation, without importing either supplied checker file, passed 37 fixed character/cohomology checks, including every displayed tensor identity and both twist-three calculations.

The executable checks validate fixed universal arithmetic and source/proof hashes. They do not certify the geometry; that is reviewed below.

## Mathematical assessment

1. **Retained actual objects and universal sequences.** The proof uses the genuine constant ambient and the actual saturated first-jet inclusion supplied by the inputs. Duality therefore gives surjective evaluation, not a generically surjective map with an omitted defect. The complete degree-ten kernel is correctly identified by the universal first-principal-parts sequence. The degree-eighteen system is never assumed complete. The quartic dual evaluation and the physical determinant convention are consistent.

2. **Exact shared-D gluing.** The dual constant sum/intersection sequence and the two evaluation maps form the asserted commutative diagram. The snake lemma gives the full exact sequence, including surjectivity onto the actual D* constant bundle. It also identifies the kernel as the actual annihilator F, rather than an abstract bundle with the same splitting.

3. **Projected degree-ten system.** Its six-dimensional independent section system is basepoint-free by the invariant-divisor bound and nonconstant by its constant span. Characteristic zero gives generic first-jet rank two. The resulting F10-to-D* map has generic rank five; its maximal minors all have degree ten. Their common vanishing divisor is invariant and has degree at most ten, so the minimum orbit degree twelve rules out every rank-drop point. This proves everywhere surjectivity without evaluating a minor or choosing a point. The subsequent H0 exclusion uses actual injections of the constant P or D summands, so the rank and determinant contradictions are valid. The bounded genuine cohomology budget forces R=V(-4)+O(-6); zero-H1 degree-three blocks cannot remain after the required blocks consume all four ranks.

4. **The two F18 alternatives.** Comparison of complete and partial jet evaluations gives the exact sequence with quotient P O. The two independent quotient constraints on H1(F18(2)) genuinely restrict it to zero or one V. The Euler characters, rank/degree constraints, central parity and atom arguments then give exactly the two stated necessary splitting types. No alternative is asserted realized. The claims about the global P, D and V components concern only their forced vanishing/nonvanishing behavior, not selected coefficients.

5. **Actual scalar cancellation.** If the scalar summand of R mapped trivially to the actual F/E0 quotient, the small equivariant Hom spaces would force it into D(-2) by the universal quartic inclusion. The resulting S4(-1) direct summand of F/a cannot map to F18, since F18 embeds into a pure degree-minus-two bundle. Its forced injection into the remaining rank-three kernel is impossible. Thus q is an isomorphism on that scalar summand and zero on V(-4). The derived restriction E0-to-F18 is everywhere onto with exactly the actual V(-4) kernel. This establishes the needed actual embedding compatibility; it is not merely a splitting-type comparison.

6. **Extension alternatives.** The first branch has zero equivariant Ext group. In the second branch the sole possible block is Ext1_G(V(-2),V(-4))=C. A zero class contradicts E0's prescribed splitting; the nonzero class has middle term (W tensor V)(-3)=T6(-3). The universal Euler sequence realizes that class, and endpoint automorphisms account for nonzero scalar rescaling without choosing an actual normalization.

7. **Section 10.** Quotienting F10 by the same actual V(-4) gives a genuine locally free extension of D* O by O(-6). Its one-dimensional equivariant Ext group and Hom(F10,O(-6))=0 force the class to be nonzero. The degree-five dual evaluation sequence identifies its middle-bundle type as T6(-1). Finally, the restriction of F-to-F10 vanishes on the same actual V(-4) kernel after passing to Q, so it descends uniquely to an actual map F18-to-Q. This construction does not require or prove a rank, image or saturation assertion for that map.

## Boundary retained

All original actual-geometric hypotheses remain conditional inputs. This review does not re-establish their transitive geometric premises. The proof uses equivariant Birkhoff splitting only as a bundle statement, never as a horizontal decomposition, and introduces no connection or unjustified derivative transport on the nonconstant quotient Q. No selected actual coefficient, point, jet, tensor, matrix or instance rank, and no broad candidate scan, was used in the proof or this review. No GitHub write occurred. Neither F18 alternative, the full-positive branch, any whole K splitting, the triplet quotient, or the original maximal profile is excluded or realized; the original defect t=0 remains unchanged.
