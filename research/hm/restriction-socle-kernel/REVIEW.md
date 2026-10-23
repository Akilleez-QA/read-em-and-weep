# Independent mathematical review: PASS

Reviewed the complete proof, imported interfaces, bounded checker and reproduction instructions independently of their author on 2026-10-23. This review binds to the corrected final files:

- PROOF.md SHA-256: 1ee98092e1322841d031d65649dee205299b88d9ba726599f0678d8b1e5b2a1e
- verify.py SHA-256: 780ca53e6e0a1fa5711496e6140bc442999a9ad71d9f86e5366821a3cec8bf4c
- INPUTS.json SHA-256: 9d599444acfa643a3ac8d7ae76009f8f6ad95a1b4b998fd3f3014aae2c98c47b
- REPRODUCE.md SHA-256: 5803bf35b1f1675c6f54867d86683e43f846c1125c48247403a6faf8ddcdc76b

## Mathematical audit

1. The parameter bundle is the original rank17 degree-54 kernel of the actual M3-to-M4 pencil. Its identification is checked against ACTUAL Section1 and against the catalogue's exact upstream ACTUAL hash, rather than inferred from equal rank and degree. TERMINAL supplies actual coefficient exactness, H0(E(1))=0, the parity statements and the cohomology vanishings used here. The conditional catalogue calculation concerns the same E, not the distinct opposite bundle or global receiver bundle.

2. The cohomology of the untwisted and once-twisted pencil identifies H1(E) with M4 and H1(E(1)) with the actual Koszul cokernel M5. The map-level issue is resolved, not suppressed: for the universal formal pencil u m_x+v m_y, the quotient map sends u tensor t to m_y(t) and v tensor t to -m_x(t). Its composite with the source is zero by commutativity, and the imported exact Koszul sequence proves it is exactly the required cokernel map under u-to-y, v-to-minus-x determinant rotation. Naturality of connecting maps then intertwines parameter multiplication with actual coordinate multiplication under that fixed rotation. Applying the same determinant convention to the outer factor identifies the simultaneous maps, including their kernels and cokernels. This does not evaluate any parameter.

3. Tensoring the Euler sequence by E(2) yields 0 E -> W tensor E(1) -> E(2) -> 0. Since H0(E(1))=0 and T is a projective line, its cohomology gives exactly sequence(6), including the terminal surjection onto H1(E(2)). The preceding map-level identifications therefore prove sequence(7), not just its character identity.

4. All ordinary degrees of E are at most-2. Thus evaluation of E(2) picks out precisely its canonical degree-minus-two subbundle and has no contribution from lower degrees. The quotient is locally free. Naturality of Euler for that subbundle identifies the boundary image with H1(E_{-2}); the connecting map for O(-2) is an isomorphism. Equivalently, for d>=3 Serre duality changes simultaneous cohomological multiplication into the surjective binary multiplication W tensor Sym^(d-3)W -> Sym^(d-2)W. This verifies that lower-degree summands contribute no joint kernel. No complementary splitting is claimed canonical, and E_{-2} is correctly allowed to be zero.

5. The positive part of the twist-six coordinate Koszul sequence has no preceding section term: H0(B(4))=0 and W tensor H0(B(5)) has negative parity. H2(B(4))=0 supplies the rightmost zero needed for sequence(10). Consequently its two actual defects are those of sequence(7). The restriction sequence, positive plane parity and H1(B(6))=0 then give sequence(11), with both the kernel and cokernel identified functorially. This is stronger than subtracting Euler characters, and the proof maintains the distinction.

6. The global degree-six section character follows from the normalized-monad lambda-ring expression only after all positive cohomology has been removed. The imported endpoint and higher vanishings remove H1,H2,H3; stability and Serre duality remove H4. On the plane, the displayed symmetric-square resolution follows from the locally free Steiner quotient and B_R(6)=Sym2(F_R)(7). Its terms are sums of O_R(1), O_R(2), O_R(3), hence acyclic in positive degrees; this proves actual higher-cohomology vanishing for B_R(6). Independent fixed-character arithmetic agrees with positive global character 4A+3V+5P+5D and plane character 4A+4V+5P+5D, of dimensions66 and69.

7. The three fixed E entries10,13,14 match the authenticated catalogue exactly. FRONTIER contains three records with four source pairs, namely (10,129), (10,157), (13,21), (14,148). Direct cohomology of those entries gives H0(E10(2))=P+2D and H1(E10(2))=V+P+2D; for E13 and E14 it gives H0=P+D and H1=V+P+D. The resulting conditional restriction ranks52 and57 agree from both source and target. These are mathematical implications of the specified splitting types, not evaluations of an actual restriction matrix. The proof expressly retains the necessary-ledger assumption and makes no occurrence, exclusion or unconditional type-selection claim.

8. The marked U4 is an actual selected D-subspace, not an arbitrary D constituent. Compatibility of its symmetric continuation proves f5=0 exactly when this selected subspace is contained in H1(E_{-2}). Equivariance makes any nonzero intersection sufficient, but the presence of one or two unmarked D copies in the joint kernel does not determine that intersection. The proof correctly leaves this incidence and both terminal branches unresolved. It rules out the full-restriction-injectivity strategy only conditional on each pinned remaining E type.

## Reproduction and limits

Both `python3 verify.py` and `python3 -O verify.py` were run independently and passed against the hashes above. The checker uses explicit exceptions, so its tests survive optimized mode. All five imported byte lengths, SHA-256 hashes and Git-blob hashes were checked, as was the same-E catalogue provenance. The character arithmetic is exact in Q(sqrt(5)) on nine fixed abstract classes; the only catalogue calculations concern three named fixed types and the four pinned pairs. Reproduction instructions preserve the immutable-byte requirements and correctly explain the checker's scope.

Two nonmathematical wording issues were corrected before this binding review: the number of FRONTIER records was distinguished from its four pairs, and an inherited symmetric-degree comment was updated. No mathematical correction was required.

This is an independent mathematical text and bounded-checker audit, not formal proof-assistant verification. No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix, instance rank or large scan was evaluated. No actual E type, terminal branch, opposite type, vertex scalar or smoothing conclusion was selected. Nothing was published.
