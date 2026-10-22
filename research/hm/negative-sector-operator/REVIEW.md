# Independent mathematical review

## Reviewed version and verdict

Reviewed `PROOF.md`, SHA-256:

`98f8c819bae1dc6fdd4f9208ecc21b215e3871368953fe0a0dd4e45a5e276043`.

**Verdict:** the algebraic-geometric argument and representation-theoretic accounting are correct under the source assumptions stated below. No mathematical correction is required. This is an independent mathematical review of the displayed derivation, not a proof-assistant certificate, a reconstruction of the full HM foundation, or an evaluation of the actual third operator.

## Source assumptions and scope

The review treats the following interfaces as hypotheses supplied by the immutable sources cited in `PROOF.md`; it does not independently re-prove their identification with the actual geometric construction:

- The physically marked lower quotient is `P tensor A*`, and multiplication by the negative quadratic is universal evaluation, as stated in [the negative-sector source](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md).
- The actual second symbol is an equivariant sheaf injection `A O(-2) -> P O` with quotient `I_Z(6)`, where `length(Z)=24`, as stated in [the universal-symbol source](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-UNIVERSAL-SYMBOLS.md) and [the nonvanishing source](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md).
- The class represented by the indicated quotient is the relevant third class, with the source marking and corrected positive-boundary interface retained from [the third-channel source](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/THIRD-BOCKSTEIN-POLARIZATION-AND-SQUARE-DIRECTION-GATE.md) and [the corrected extractor](https://github.com/Akilleez-QA/read-em-and-weep/blob/389d5488257348d7bd57ceb1b81cdb8f1b916ce8/research/hm/last-jet-double-cubic/PROOF.md).

The argument is over characteristic zero with the specified finite icosahedral representations. In particular, exactness of invariants and averaging are available. Compatible binary-icosahedral identifications are understood when binary transvectants are used.

## Checks completed

1. **Pullback sequence and local freeness.** The Euler kernel of `E -> P O(1)` is `P tensor Omega^1(1)`. Pulling back the twist of the second-symbol sequence gives exactly (3). Since both end terms are vector bundles, its middle term is locally free. This does not make its injection into `E` a subbundle along `Z`.

2. **Existence and uniqueness of the equivariant splitting.** The extension group reduces to `Hom(A,P) tensor H^1(Omega^1(2))`, which vanishes by the Euler sequence. The difference space of equivariant splittings is `Hom_G(A,P tensor Lambda^2 A*)=0`, using `Lambda^2 A*` isomorphic to `A` and `P tensor A=V+P+D`, with `V` the other three-dimensional irreducible. Thus the claimed uniqueness is valid in the equivariant category and relative to the given actual symbol.

3. **Derivative lift.** Formula (6) has the correct homogeneity and twist. Euler's identity yields `eL=beta`, so it really splits (3). It preserves the actual scalar in the universal symbol. The derivative must hold `b` fixed before substituting `b=B(a,h)`. Taking the total derivative of `beta(a,B(a,h))` would introduce an extra term and would not be the displayed lift. The proof explicitly and correctly includes this caveat.

4. **Chern classes and fibers.** Four copies of `Omega^1(1)` have `c_1=-4H`, `c_2=10H^2`; three copies of `O(-1)` have `c_1=-3H`, `c_2=3H^2`. Their direct sum has `c_1=-7H`, `c_2=25H^2`. At a fiber where `beta` has rank `r`, the image of `F_x -> E_x` has dimension `8+r`, as stated. The distinction between the vector bundle `F` and its fiber image in `E` is maintained.

5. **Koszul twists.** Display (8) is correct as written:

   `0 -> Lambda^3 A* tensor O -> Lambda^2 A* tensor O(1) -> Omega^1(3) -> 0`.

   This is the Koszul presentation of the Euler kernel, twisted by two. The remainder of a quadratic family lies in `P tensor Omega^1(3)`, so the lift `S` is linear in `a`. Global sections are exact because `H^1(O)=0`. The ambiguity is precisely `Hom_G(D,P tensor Lambda^3 A*)`, which vanishes. No twist correction is needed.

6. **Normal form.** Factorization through the sheaf kernel first gives a unique `B` and a unique contraction-invisible remainder. The preceding Koszul argument then gives a unique equivariant `S`. Conversely, evaluation at `v=a` kills the alternating term and produces `beta(a,B(a,h))`. This proves both directions of (7). The proof correctly restricts uniqueness to equivariant whole polynomial families, not individual parameter values or arbitrary nonequivariant lifts.

7. **Binary-form B channel.** With `A=Sym^2 W` and `D=Sym^4 W`, the second transvectant has output `Sym^2 W`. It is a nonzero equivariant bilinear map, and `A` occurs once in `A tensor D`. Therefore it spans the claimed one-dimensional channel. Its normalization can be absorbed in the free scalar; the statement does not determine an actual lower-operator coefficient.

8. **Coefficient spaces and surjectivity.** The lower space has dimension six. The contraction-invisible space has dimension three because `H^0(Omega^1(3))=A+D`; the second-symbol-exact channel has dimension one. The effective quotient therefore has dimension two. Moreover, `H^1(F(2))=0` proves surjectivity onto `Hom_G(D,H^0(I_Z(9)))`; the argument establishes an exact sequence, not merely a character subtraction.

## Interpretation and limits

The contribution beyond the known channel count is a canonical equivariant kernel splitting and an explicit unique polynomial normal form, with the second-symbol-exact channel tied to the actual symbol. These are consequences of standard Euler/Koszul methods applied to the stated interfaces; this review makes no claim of literature priority.

Nothing in the derivation establishes whether the actual lower family lies in the four-dimensional ineffective subspace. Neither effective third-channel coefficient is computed or eliminated. The boundary stated in `PROOF.md` is accurate.
