# Independent whole-proof review

Verdict: PASS. No mathematical blocker found in the theorem or its stated consequences. This is an independent mathematical review, not proof-assistant verification. The review uses the pinned prior results as mathematical inputs and checks that the new argument invokes their actual maps and geometric hypotheses rather than character-compatible substitutes.

## Exact reviewed bytes

SHA256:

- PROOF.md: `ce5bb0fa0b9a6012a8e2e545aa0d4fee2049a9d21d8736f1ad9b47b37cc8884e`
- verify.py: `1d0454184bf6b762e3a6a1d5298cce64c60f89433251fbc779108db43ed2ec48`
- INPUTS.json: `3768089da697fc5a357c3010eb92505d2bc1c7ea31e709e7e116556c2ece3a0f`
- REPRODUCE.md: `6b6ec14cdc4e85642210c62689d8c8b723d328ccd8c58703156618b9ecac10f0`

The final proof has been read in full. The five local immutable inputs FIRST, SECOND, FINITE, STEINER, and POLAR were read and authenticated by the verifier's Git-blob calculations. STEINER was also compared byte-for-byte with the supplied exceptional-adjoint-exhaustion SQUARE input, and POLAR with the supplied exceptional-polar-obstruction proof; both comparisons agreed. The final attribution of H0(B_R(2)) to POLAR is accurate.

## Mathematical checks

1. The multiplication kernel is an actual equivariant subrepresentation of A tensor V = P direct sum D. In characteristic zero this multiplicity-free decomposition reduces noninjectivity to the inclusion of P or D in the kernel. A generically surjective relation-evaluation map into S tensor O_R would kill every section in S on a dense open set, hence globally, which is impossible.

2. The D relation-evaluation map is the actual dual Steiner surjection D* tensor O_R(-1) to A* tensor O_R, after an equivariant S = A* identification. Its coefficient embedding is nonzero; multiplicity one identifies its image with the unique D summand. Thus the proof correctly excludes D without choosing source coefficients.

3. If P were a relation space, a nonzero annihilator at a general point gives a decomposable tensor in P-perpendicular inside S* tensor U*. This annihilator is the unique D summand. Equivariant isomorphisms S* = A* and U* = U preserve decomposability and transport it to the unique dual-Steiner D summand. The resulting nonzero constant functional on D descends to an everywhere surjective map F_R(2)|L to O_L. This is a genuine quotient, not merely a nonzero cohomology class. The fixed isomorphism U* to U sends general points to general lines, so the line in this contradiction is legitimately general.

4. The Grauert–Mülich hypotheses hold: F_R is a stable complex rank-two bundle with c1 = -1. I checked the stated formula visually in Schneider, Bourbaki 530, Theorem 5.1, printed page 97, PDF page 19, at https://www.numdam.org/article/SB_1978-1979__21__80_0.pdf. Its general-line splitting is O direct sum O(-1). Twisting by two gives O(2) direct sum O(1), which has no nonzero homomorphism to O. Therefore P is excluded as well, and the nine-dimensional multiplication image M is established structurally. No special-line splitting is used.

5. The boundary at ordinary normal degree four is the actual commutator with the quadratic transition class. The invariant candidate begins in ideal degree two; the unique first-normal comparison eliminates a degree-one transition contribution. Thus the first relevant defect is [zeta,e] in degree four. Higher transition terms cannot alter this degree. This matches FIRST's actual Cech derivation and does not replace the formal bundle by a split bundle.

6. The equivalence alpha = 0 if and only if mu = 0 is justified beyond multiplicity counting. The nonzero invariant tensors zeta and e identify N* with Z and S. Dualizing normal multiplication N tensor N to Sym4 W gives a nonzero inclusion of D* into Z tensor S. Its image is the unique D summand. The only possible nonzero channel of mu is that same D summand, with multiplicity one in H1(B_R). Consequently composing mu with this inclusion is nonzero exactly when mu is nonzero. There is no unverified recoupling coefficient or symmetric/alternating cancellation.

7. FIRST identifies the first cup as the actual adjoint commutator, and SECOND constructs the actual family with locally free kernel K of rank nine and degree -12. O_R-linearity gives [z,ell s] = ell[z,s] in the correct twists. If mu vanished, the fixed nine-space M would therefore lie in every actual fiber kernel. The resulting map M tensor O_T to K is injective on every fiber because its composite into H0(B_R(3)) tensor O_T is the fixed constant inclusion. Equal ranks force an isomorphism of vector bundles, contradicting the degree of K. A merely generic injection or a nonsaturated rank-nine subsheaf is not being mistaken for a trivial subbundle.

8. FINITE supplies the actual duality and boundary orientation: ker(alpha*) is the invariant section space on 5R. Odd intervening layers have no invariant cohomology, so the unique 3R candidate reaches 4R and then fails precisely at degree four. Later invariant restriction maps are injective, proving vanishing on every mR for m at least five.

9. POLAR identifies H1(K6)^G with ker alpha and H2(K6)^G with coker alpha. Both vanish when alpha is an isomorphism. The actual sequence at G8 then canonically identifies H1(K8)^G with H1(G8)^G; the odd G9 and invariant-acyclic G10 layers canonically transport this identification to H1(K10)^G. The lower beta therefore has zero target. These conclusions do not split the sheaf filtration, determine the top sigma rank, select an opposite-bundle row, or determine the vertex scalar.

## Reproduction and scope

I inspected verify.py and REPRODUCE.md in full and replayed both `python3 verify.py` and `python3 -O verify.py` successfully against the authenticated inputs. The verifier uses exact rational arithmetic in Q(sqrt(5)), checks the nine abstract character classes and relevant identities, and uses explicit require checks that remain active under optimization. It authenticates all five immutable input blobs. The documented reconstruction commands recover the named bytes from the named repository commits and paths.

The checker does not establish Grauert–Mülich, multiplication injectivity, actual cup compatibility, the nonzero contraction, or the bundle-degree contradiction; those are the mathematical steps reviewed above. No selected actual HM/source coefficients, points, normal jets, derivatives, matrices, or instance-rank evaluations were used in this review. No proof edits or external writes were made by the reviewer. Any change to the four bound files requires a corresponding review update.
