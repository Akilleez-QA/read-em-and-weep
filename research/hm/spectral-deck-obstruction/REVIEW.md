# Independent mathematical review

Review scope: the structural proof in PROOF.md, conditional on [the pinned Gram spectral input](https://github.com/Akilleez-QA/read-em-and-weep/blob/f0c94ff7979652c094da3efaa11fea4629dbf59a/research/hm/gram-spectral-geometry/PROOF.md), commit f0c94ff7979652c094da3efaa11fea4629dbf59a. The pinned input was read independently. This is a mathematical review, not a proof-assistant certificate and not an actual selected-source evaluation.

## Checks of the deck obstruction and Galois construction

1. The norm of a degree-zero line bundle has degree zero, hence is trivial on P1. The identity pi^*pi_*Z=sum sigma^j Z remains valid for divisors at branch points: both sides count the totally ramified point three times. The proof does not incorrectly assume an etale cubic cover.

2. An invariant two-torsion class has both square and cube trivial, so is trivial. The actual nonzero T consequently has an orbit of length three. The norm relation makes the third class the product of the first two, giving exactly a two-dimensional F2 subgroup. This proves an obstruction at the level of line-bundle isomorphism classes, before any linearization choice.

3. Since base pullbacks are invariant, the obstruction applies to B and Theta and all their base-line twists. A global conjugacy between M and either nontrivial cube-root multiple is exactly an isomorphism with a deck-pulled spectral module, up to the harmless choice of inverse generator. Excluding both generators covers that convention. The assertion is global and makes no claim against local diagonalization.

4. Kummer theory over C identifies the two-torsion Picard classes with etale double-cover classes. Independence gives a surjective pair of characters and therefore a connected degree-four cover. The algebra is constructed using square trivializations; its direct-sum decomposition alone is not erroneously treated as an already specified multiplication. All choices produce the same unlabelled covering isomorphism class.

5. Stability of the character subgroup under sigma implies stability of its common kernel, and hence lifting of sigma to the connected cover. This is valid without a lift to any individual eigensheaf. There are twelve automorphisms over P1, proving the composite is Galois. Conjugation acts without nonidentity fixed points on K. For any lift g, g^3 is in K and is fixed by conjugation by g; thus g^3=1. This proves the split extension and the A4 identification without assuming a splitting in advance.

6. The etale degree-four Riemann–Hurwitz calculation gives genus37. Independently the degree-twelve cover has four ramification-index-three points above each of twelve branch points, so -24+12*4*2=72=2*37-2. No additional branch points occur.

7. The T double cover has genus19. Its order-two subgroup in A4 is nonnormal and has trivial core, since its three conjugates are the distinct order-two subgroups of K. This proves both non-Galoisness of the degree-six composite and that Y is its exact normal closure.

## Tetragonal consequence

Section 5 was read back in its final form and is also justified. The quotient C=Y/<g> is a smooth connected projective curve in characteristic zero. Its degree over P1 is four. A nontrivial order-three inertia generator acts on A4/<g> with cycle type (3,1), so there are twelve contributions of two to Riemann–Hurwitz. Therefore 2g(C)-2=-8+24=16 and g(C)=9. The order-three subgroup is nonnormal, proving that this tetragonal cover is not Galois.

For its pushforward, the K-eigensheaf decomposition of f_*O_Y is preserved by <g>, with the trivial-character term pi_*O_S stable and the other three terms cyclically permuted. The invariant part of the former is O_L. Projection to the pi_*T term identifies the invariants of the latter with pi_*T: because g^3=1, any chosen component has a unique invariant triple. The projection formula and the actual pi_*B=V tensor O_L yield pi_*T=V tensor O_L(-4). Thus h_*O_C=O_L plus V tensor O_L(-4). The second summand is the trace-zero bundle; the usual Tschirnhausen bundle is its dual, V^* tensor O_L(4). This distinction in terminology must be retained.

As an independent numerical check, chi(h_*O_C)=1+3*(-3)=-8=1-9, matching the genus. No compatibility with an A5 action, Recillas construction, or Prym identification has been assumed.

## Scope

No defect was found in the stated structural arguments. The conclusions are conditional on PR654's actual spectral line and exact nontrivial two-torsion input. They do not calculate the actual R-class, Bockstein value, source-instance normal form, or algebraicity outcome. No selected coefficients, actual-instance points, matrices, ranks, or scans were used.

Verdict: PASS, conditional on the pinned input. All five sections were independently mathematically reviewed. No mathematical correction was required; the final wording correctly distinguishes the trace-zero bundle from its dual Tschirnhausen bundle and records noncanonicity of choices. This review is not a formal verification.
