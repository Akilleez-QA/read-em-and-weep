# Independent review of the secondary-homotopy theorem

## Verdict and scope

No mathematical blocker found in the stated theorem, conditional on an actual Type II occurrence and full-radical compatibility. The canonical object is the line J0 and the linear assignment j to h_j, not a canonically scaled nonzero generator. The surviving transvectant scalar is not determined. No full-J exclusion, catalogue cut, or complete original repair follows.

## Independently checked arguments

1. PR973 gives a nonzero linear map from the two-dimensional J to the one-dimensional induced D channel. Its kernel J0 is therefore a canonical line. Both cohomology maps vanish for an element of J0.
2. Over C, split two-term complexes give a null-homotopy for every cohomologically zero map. Averaging gives an equivariant one. The difference of two homotopies factors from H1(T)=P to H0(S)=A+D, whose equivariant Hom is zero. This proves actual uniqueness and linearity, not merely uniqueness modulo a choice of splitting.
3. The Hom differential has plus signs on a degree-minus-one homotopy: j0=h Q_T and j1=Q_S h. Thus K=(h L_T,L_S h). The equation d_Q K=-d_L j=0 uses that j commutes with the negative family. The identity d_L K=0 is direct. This proves that K_a is a chain map for Q+t L_a. It does not assert that K_a commutes with every unrelated L_b; the proof does not need that stronger assertion.
4. First-symbol naturality gives b_S,a k0_a=k1_a b_T,a with the same a on both sides. Taking the bilinear invariant adjoint of b_T,a yields an a-linear equivariant family P to D without conjugating or changing the parameter. Self-duality gives the unique channel, so k1_a is a fixed scalar multiple of that adjoint.
5. For any nonzero square, b_T,a is surjective by the imported uniform theorem, so its bilinear adjoint is injective. Their composition has rank four over C, independently of positivity or isotropy. The other side of naturality factors through A and has rank at most three. Hence the secondary cokernel component vanishes. Injectivity of multiplication by a on A then forces the secondary A component to vanish.
6. The only remaining D channel is the first transvectant, equivalently the binary quartic sl2 action. The universal representatives x^2 and xy both give rank four and kernel spanned by a^2. These are representation-model orbit computations, not actual HM parameter evaluations. The nowhere-zero quadratic vector a^2 gives kernel O(-3) inside D O(-1). Constant rank gives a line cokernel; its determinant is O(2).
7. Nonzero homotopy does not imply nonzero induced secondary cohomology. The stated unselected scalar branch and synthetic negative control correctly preserve this limitation.

## Final-byte authentication and tests

Independently read the checker and ran both `python verify.py` and `python -O verify.py`. Both produced byte-identical output:

    PASS: 111 exact checks; two immutable inputs; no actual HM evaluation.

The checker authenticates the two input copies by SHA256 and Git blob identities, checks representation multiplicities and synthetic Hom-complex identities, tests the adjoint rank argument with indefinite bilinear pairings, and checks the two universal quartic orbit types. These checks support the written proof; they do not formally certify its geometric dependencies.

Final reviewed hashes:

- PROOF.md: `10a70239af9d2af034ed8b66b51d476484d28a243e2eaaa0c2e03095568db5c2`
- verify.py: `c6361f5e4e0f6e2fe8d97391374991894f51d6927e15e0674f2074f12e2407ab`
- INPUTS.json: `8e019710519ae2400cab310ee39016ffd89dbf9a6c26b8254d6cb189e55f7ebb`

The packet uses plain checker stdout rather than a RESULT.json file. No actual HM coefficient or instance rank was evaluated during this review.
