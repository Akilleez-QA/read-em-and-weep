# Independent mathematical review

Verdict: PASS, conditional on the actual source2, common-pencil, and nonzero pure-V Q-compatible-radical hypotheses explicitly retained in the proof. This review does not prove those hypotheses are realized.

## Reviewed immutable local content

The complete proof and checker were read independently against all four retained original input proofs. The reviewed SHA-256 hashes are:

- PROOF.md: `4b027c735a5f46c1a293aace296d36b25699614997a64567dbc7994e5456d415`.
- verify.py: `e4826ee53dd5b64ec7aa941114a8cb970a43138220f9dc5114f755ce66427133`.
- INPUTS.json: `6734a55219d73639203c90e29ff1e3ab08c5fd07ad0209132f65e7dfb2731d28`.
- REPRODUCE.md: `3765b2b50ed5835fa107c3dfbb59265998b7ef542eaded2300af035e313ab292`.

Independent byte-count, SHA-256, and Git-blob computations matched INPUTS.json for FILTRATION, TERMINAL, SOCLE, and RESIDUAL. This authenticates the retained originals against the pinned manifest; it is not a fresh proof of every upstream result.

## Actual-map and naturality audit

1. The same-E issue is resolved at map level. Pushing the diagonal resolution after tensoring by the negative evaluation kernel gives the natural exact sequence with coefficient spaces H1(E(-1)) and H1(E). The evaluation connecting isomorphism identifies its second pencil with the reconstructed one. Naturality for the endpoint/residual inclusions therefore transports their kernels to the original actual pencil. Equal rank, degree, or character is not being used as a substitute for this identification.
2. The genuine first-block splitting and residual exact sequence give an actual quotient E/E_C = W O(-9) plus T6 O(-3). After twisting by 2 this quotient has no sections. Hence all sections of E(2) come from the globally generated E_C(2), and the evaluation images agree: E_C is the canonical E_{-2}. The argument requires no horizontal splitting of E_R. The quotient also has no untwisted sections, giving the required injection on H1.
3. FILTRATION's connecting-map naturality identifies this embedded H1(E_C) with the actual NC4, while SOCLE identifies the same image with the actual joint-negative kernel. The fixed determinant convention is retained throughout. Thus the proof establishes an equality of embedded subspaces, not merely of P+D characters.
4. The separate Koszul check is valid: NC is stable under both original arrows, so the actual injective delta restricts from the 18-dimensional NC3 to the 18-dimensional W tensor NC4. It is onto, and exactness makes mu vanish on W tensor NC4. The proof correctly labels this as an independent containment check and uses the bundle argument for the equality/dimension conclusion.
5. RESIDUAL's transversality concerns the marked D_can, not an arbitrary D copy. If f5 vanished, actual multiplication would put all of that marked D_can in NC4, contradicting its zero intersection there. Nonzero f5 is injective because Sym5 W is irreducible. The coherent normalization gives a canonical image; H1(B(6))=0 makes it terminal under every ambient coordinate. The final selected parameter subpencil is the ordinary binary multiplication sequence with quotient O(5).
6. For each radical j, im(j4) is contained in NC4 and hence killed by the next negative arrows. Defining j5=0 satisfies all new intertwining equations. Actual surjectivity of W tensor M4 onto M5 forces uniqueness. This extends the radical only on the negative-coordinate system in degrees 2 through 5; neither h nor the full HM module action is asserted to extend.

## Reproduction and scope

Both `python verify.py` and `python -O verify.py` completed successfully on the reviewed files. Checks remain active under optimization because failures use explicit RuntimeError conditions, not removable assertions. The verifier checks only the four input authentications and bounded exact abstract character/dimension identities; the naturality and actual-map arguments were reviewed separately above.

No selected actual HM/source coefficients, points, parameters, jets, matrices, instance ranks, or scans were evaluated. The proof conditionally rules out the marked terminal-zero alternative. It neither realizes nor excludes source2, selects a 9/16 generated-endpoint branch, identifies unmarked and marked D copies, nor claims positive-coordinate commutation of the radical. No mathematical blocker remains for the reviewed statement.
