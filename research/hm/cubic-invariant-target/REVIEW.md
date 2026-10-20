# Independent mathematical review

Reviewed proof SHA256: `530535211c0b18ca19f70230acc9385302df0a33cb6f22a4b36ed747559e02b7`.

Result: **PASS within the stated dependencies and scope**. This is independent mathematical text and primary-character review, not formal verification.

## Checks performed

1. The dual section resolution at twist −4 has left term F(−3). Its cohomology in degrees zero through three vanishes by the imported primary HM groups. Splitting the resolution into short exact sequences and using intermediate line-bundle acyclicity gives the exact four-term section sequence (3). No surjectivity of an unproved selected differential is assumed.

2. The polynomial representation identities were compared with HM Lemma3.3 on printed p.70. The Galois operation interchanges the two two-dimensional characters and their symmetric squares. In particular S₁⊗A uses U′⊕W, whereas A*⊗A* uses U⊕W′. The dual S₄ formula uses V, not V*.

3. The coefficient bracket in (4) was checked against all nine columns of the primary HM Appendix on printed p.81, using η+η′=−1 and ηη′=−1. It gives the unprimed U character, hence B₀,₄=V*⊗U. The values at the two order-five classes distinguish U from U′. The roles of T=χ₄ and Q=χ₄♯ remain distinct.

4. Since H₅ is finite and the coefficient field has characteristic zero, taking invariants preserves the imported degree-five presentation exactly. The invariant factors in End(V) and End(A) are scalar lines with trivial normalizer-quotient action. The four small tensor identities used in Section3 agree with the same primary character table. Thus the invariant source is T⊕Q⊕R and the invariant target before taking the cokernel is W⊕2R.

5. Schur's lemma leaves only the unique source R mapping to the two target R copies. Its map is either zero or injective. This proves exactly the two character alternatives in (7), but does not choose between them. The coordinates (a,b) are presentation dependent, as the proof says.

6. Generation of the primary cohomology module in degree zero and associativity of the cup product justify equality (8), not only containment. The intrinsic primary source T⊗M₃=W⊕R is H₅-trivial. The preceding invariant differential has no W-type image, so this W survives isomorphically; the primary R is either killed or injective. Thus the primary cubic image is nonzero and has dimension two or eight.

7. The normalizer-equivariant universal cubic map uses the imported unique lift from PR452. Its C₁₅ invariant domain is (J⊕W′)⊗U. Central parity kills J⊗U, and W′⊗U=R cannot map to W. Averaging over H₅ extends this zero-projection conclusion from invariant inputs to the full universal source. It does not assert that any fixed-pair quotient is an N-representation. The analogous parity exclusions for W′⊗Q and W′⊗R are also valid.

8. The additional Section5 is valid. Central triviality makes the H₅-action factor through F₅². The standard SL₂(F₅) action is transitive on its twenty-four nonzero dual vectors, so every nontrivial character space in an N-representation has the same dimension m. End(V) contains each of the twenty-five characters once: its character is 25 at the identity of H₅/Z and zero at every other quotient element, equivalently the regular character. Hence the presentation bounds each nontrivial target multiplicity by dim R=6. Combining the already proved invariant dimensions with h¹B(5)≥32 gives 1≤m≤6. The sum K of the nontrivial character spaces is canonical, N-stable, and disjoint from the H₅-trivial primary cubic image L. It remains a direct summand after quotienting by L. Neither the value of m nor the image of the defect cubic map on K has been asserted.

## Imported dependencies and remaining questions

The section resolution, the natural degree-five presentation, primary module generation, the bound h¹B(5)≥32, and the canonical defect lift are imported from the exact PR167/451/452 commits linked in the proof. This review does not reprove their geometric prerequisites or assert that those PRs are merged.

The surviving R-type map, total dimension of H¹B(5), universal cubic surjectivity, and the fixed order-five endpoint quotient remain unresolved. No selected HM/source evaluation, numerical matrix, rank routine, computational tensor-cohomology table, or large computation was used. No conclusion about actual-source ideal membership, pure conditions, higher-order lifting, or algebraicity follows from this review.
