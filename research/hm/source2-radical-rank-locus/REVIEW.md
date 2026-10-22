# Independent deductive review: complete source2 radical rank locus

## Reviewed artifact and verdict

The reviewed artifact is `PROOF.md`, titled **The complete universal
projective radical rank stratification for source2**, with exact SHA-256

    a256ec6cc92b1151a6551e6692cfa32cac02bceaad34c60746f51f249256cf4c

Review date: 22 October 2026.

**Verdict:** the proof is deductively sound within its stated universal
constant-normal-form hypotheses and its explicitly conditional
actual-source boundary. No correction is required. It proves that the
projective radical has exactly the following strata:

- the V-channel direction, with ranks `(5,6,4)` and image characters
  `(D,T,P)`;
- one further direction, different from both channel axes, with ranks
  `(9,12,9)` and image characters `(P+D,W'+S+T,P+D)`;
- every remaining direction, with ranks `(9,18,9)` and image characters
  `(P+D,W'+S+2T,P+D)`.

It also proves the divisor `12[V] + 6[additional direction]` for the
determinant of the reduced eighteen-dimensional middle map. This is not
the determinant of the full degree-three radical endomorphism.

This is an independent written deductive review, not formal or
proof-assistant certification. It does not verify the actual-source
hypotheses by an instance calculation or claim an HM realization or
exclusion.

## 1. Exact published dependency verification

The following public proof files were retrieved at the exact immutable
commits. Their returned contents were read, and their SHA-256 digests
were independently checked. The three direct rank/algebra dependencies
agree with the hashes stated in the reviewed proof.

- [PR791: exact pencil endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md)
  - Commit: `2cd033a4a5ba549d07330427cd779364cb83c0fb`.
  - SHA-256: `8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290`.
  - Git blob: `5a0d16a2f22032f1a0583b92ad71661b5abab59d`.
- [PR792: degree-six V-channel image pencil](https://github.com/Akilleez-QA/read-em-and-weep/blob/2f01f18960ce56b8b2a0c1260c277de3c5f916bf/research/hm/source2-radical-rank-profile/PROOF.md)
  - Commit: `2f01f18960ce56b8b2a0c1260c277de3c5f916bf`.
  - SHA-256: `0d4eb3e4e9e98dd9ea8202399590f9741c06771411d5ce40e69a139c461b3798`.
  - Git blob: `76bee93507d1a2d0840926d4e4e27edadfebb7d7`.
- [PR793: universal A-channel image profile](https://github.com/Akilleez-QA/read-em-and-weep/blob/ba9234964af5d879675d19ae97847a9475792f98/research/hm/source2-a-channel-rank/PROOF.md)
  - Commit: `ba9234964af5d879675d19ae97847a9475792f98`.
  - SHA-256: `7a9e75e9f1d22bb058039a94452e6edc1b788faa6e716dc5489f877346ab170a`.
  - Git blob: `9fd685d919caf88142441d4788e8ff59ea23fb7a`.
- [PR789: arbitrary residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md)
  - Commit: `2d1642ad40ae1111b84b50eeaca0426bfbfbb314`.
  - SHA-256: `7eb626caae70e62613e8a3e318ac4c6a858502c4fdecfb44a6693e3ed85635c3`.
- [PR790: separated first constant block and actual-pencil reconstruction](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md)
  - Commit: `af0e03d26da5e47d18ae732291aca46f4d448dc5`.
  - SHA-256: `0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4`.

The endpoint exclusion used by PR792 was also checked directly in
[PR754, Sections 3–5](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md),
at commit `044add76ebb14043a0edf73171517c90b9ef0c13`: the P subsystem
divisible by the invariant orbit form is outside the balanced locus.

The audit checks the present deductions and their stated use of these
published results. It does not represent a fresh recursive certification
of every earlier actual-source input in their dependency chains.

## 2. The maps imported from the A and V theorems are the required maps

PR793 supplies an actual morphism of evaluation sequences, with
`g_A:E0 -> E_A` an equivariant bundle isomorphism and

    0 -> (V+D)O -> Q0 -> O(18) -> 0.

It therefore supplies an injective first section map and an isomorphism
on sections after twist `-1`, not merely spaces of matching characters.
Its kernel map is obtained from the constant A projection.

PR792 supplies the actual map `g_V:E0 -> E_V`, with
`E_V=W'O(-3)` and torsion cokernel, together with the surjective section
maps of `q_V` after twists `-2` and `-1`. The induced map
`H^1(E_V) -> H^1(E_C)` is injective for every balanced endpoint. In
particular the nonsaturation of `g_V(E0)` inside `E_V` is neither
suppressed nor used as a substitute for a cohomological statement.

PR789, Section 6, verifies the exact annihilator sequence for arbitrary
residual coupling. The inclusion `O(18) -> R*` is an actual dual of the
endpoint quotient; its section maps are injective. The quotient of
`E_C -> E_R` is `TO(-3)`, whose zero section space gives the required
injection on `H^1`. These facts justify computing the entire radical
image in the smaller targets used in the proof.

## 3. Both multiplication nonvanishings are established geometrically

The proof correctly distinguishes a multiplicity statement from
nonvanishing of a specific map. Twisting the torsion-cokernel sequence
for `r=g_V g_A^{-1}` gives surjectivity

    H^1(E_A(1)) = W'+2T -> H^1(E_V(1)) = W'.

Thus the unique W' in the source is not killed. The A connecting map
from `Sym^19 W` is onto and has kernel `A18 tensor W = W+S`, so its
composition with this map is nonzero on the unique W' in `Sym^19 W`.

Naturality with multiplication is enough to transfer this fact to the
two untwisted nonvanishings. If beta killed a subspace L, then beta_1
would kill its product with all linear forms. For
`L=f12 Sym^6 W`, that product is `f12 Sym^7 W`; its W' is nonzero
because multiplication by the nonzero form f12 is injective.

For `L=P_t`, balancedness makes `E_C(1)` acyclic. Consequently
`H_t tensor W -> Sym^19 W` is an isomorphism. The unique W' in its
source comes from `P_t tensor W`, so its image cannot vanish. This
proves `beta(P_t) != 0` for every balanced endpoint, without selecting
an endpoint or calculating an intertwiner scalar.

## 4. Extension signs, dimension, and nonzero pushout

The quotient map from `E_AV` is `(a,v) -> ev_6(v)`. Lifting a section s
of `O(6)` requires the A evaluation to be `-f12 s`. Therefore the
extension with kernel `E_A plus E_V` is the pullback along

    s -> (-f12 s,s),

and its components are exactly

    xi_A = -f12^* eta_A,    xi_V = eta_V.

The invariant extension space is

    Ext^1_G(O(6),E_V) = (W' tensor Sym^7 W)^G,

which has dimension one. Exactness of invariants for a finite group
over C justifies passing from ordinary to equivariant Ext. The
evaluation class xi_V is nonzero, since a splitting would give a
nonzero map from `O(6)` to the trivial bundle `V6 O`.

The pushout `r_*xi_A` is nonzero for a separate, valid reason: its
connecting map is minus beta after multiplication by f12, and the
first multiplication nonvanishing proves that this connecting map is
nonzero. The argument does not infer nonvanishing merely from the
dimension of the extension space.

## 5. Saturated graph quotient and the snake lemma

After the A-kernel identification, the kernel map of a mixed direction
is `x -> (x,z r(x))`. Its quotient inside `E_A plus E_V` is `E_V`
through `(x,y) -> y-z r(x)`. This map is onto irrespective of the
torsion cokernel of r. Thus the graph is saturated in that direct sum.

Its quotient K_z in `E_AV` fits into

    0 -> E_V -> K_z -> O(6) -> 0,

and is locally free because an extension of locally free sheaves is
locally split. This also proves saturation in `E_AV`. The quotient map
on the kernel sends the first component by `-z r` and the second by
the identity, so the resulting class is exactly

    xi_V - z r_*xi_A.

Both terms are nonzero in the same one-dimensional extension space.
There is therefore one and only one mixed split direction. It is
different from both axes. At that direction K_z is
`E_V plus O(6)`; elsewhere in the mixed locus it is equivariantly
isomorphic to `V6 O`, by equivalence of nonzero proportional extension
classes after rescaling an end term.

The constant map onto `A18 plus V6` is surjective with kernel D.
The kernel map is injective. The snake lemma consequently gives

    0 -> DO -> ker q_z -> K_z -> 0

and surjectivity of q_z. After twist `-1`, `DO(-1)` is acyclic.
The section kernel is therefore zero in the nonsplit case and is
`H^0(O(5))=T` in the split case. This proves the asserted middle
ranks and the exact kernel character at the exceptional direction.

## 6. The first rank cannot fall away from the V axis

The distinct-D-image argument is valid and uses more than characters.
If the D images of the two first section maps were equal, Schur's
lemma would factor the V map through the A map by an endomorphism
L_0 of `Sym^8 W=P+D` that kills P and is nonzero on D. A morphism
from the trivial bundle `Q0(-2)` is determined by its constant
sections, so this would be an equality of the actual bundle maps.

After twist `-1`, the A section map is an isomorphism and the image
of the induced L is `D tensor W`, of dimension ten. This contradicts
the proven six-dimensional V image. The two D subrepresentations
are thus distinct; their intersection is zero, and neither can
cancel a P component. Every direction with nonzero A coefficient
is injective on the first nine-dimensional domain, with image P+D.

## 7. The final rank cannot fall away from the V axis

The A evaluation sequence canonically identifies the relevant map a
as the quotient

    Sym^18 W/A18 -> Sym^18 W/H_t,

with kernel V+P and target P+D. The V map b has image P because
`H^1(E_V) -> H^1(E_C)` is injective. The second multiplication
nonvanishing proves that b is nonzero on the P subrepresentation of
`ker a` coming from P_t.

Thus the two maps on the P-isotypic source are linearly independent.
Every combination with nonzero A coefficient has a nonzero, hence
surjective, P component. On D, b is zero and a is an isomorphism.
The image is consequently exactly P+D. The subsequent injection
into residual cohomology preserves it for both coupling classes.

## 8. Reduced comparison operator and determinant multiplicities

The comparison operator `s=u_A^{-1}u_V` is equivariant and its image
is an irreducible T. Its image is stable under s by definition, so
Schur's lemma applies to the restriction and gives `s^2=c s`.
If c were zero, `id+z s` would be invertible for every z with inverse
`id-z s`, contradicting the already established mixed singular
direction. Hence c is nonzero and `s/c` is a projector.

Its kernel and image have dimensions twelve and six. The reduced
homogeneous pencil acts by the A coefficient on the first summand
and by a nonzero linear functional on the second. Those two linear
factors have distinct projective zeros, respectively the V axis and
the additional split direction. Their multiplicities are exactly
twelve and six. This proves the full reduced determinant divisor,
not only its set-theoretic support.

The comparison operator is not a radical element. The actual full
degree-three radical maps are square-zero endomorphisms of the
54-dimensional space, so their full determinants vanish identically.
The reviewed proof explicitly and correctly separates these facts.

## 9. Exact characters, exhaustiveness, and universality

The middle domain has character `W'+S+2T`. At the split direction
the kernel is T, so semisimplicity gives image `W'+S+T`. At every
other non-V direction it is the full `W'+S+2T`. The preceding first
and final arguments give P+D in both outer degrees. PR792 gives
the remaining V-axis characters D, T, P.

PR791 identifies the two channels with the entire radical. The proof
therefore exhausts the projective radical, rather than an unexplained
two-dimensional subspace. The mixed extension and its split-class
condition involve no P_t and no residual graph. The additional
direction is consequently independent of endpoint and coupling under
the stated universal channel identifications; rescaling channel
generators changes only a coordinate description.

The only endpoint-dependent nonvanishing added in the argument is
proved uniformly by balanced acyclicity. The residual maps are
injective in the precise cohomological degrees required, for arbitrary
coupling. The actual-source application remains conditional on PR790,
and contravariant duality does not change the ranks or square-zero
property. No change of the pencil variables is introduced.

## Review boundary

This review uses structural evaluation sequences, equivariant
representation theory, natural multiplication and cohomology, exact
extension classes, saturation, and Schur's lemma. No actual source
coefficient, endpoint value, point, derivative value, tensor, matrix,
source-instance rank, selected model, scan, or large computation was
chosen or evaluated. Hashing retrieved proof text was solely an
artifact-integrity check. The verdict is a deductive assessment of
the exact reviewed text under its declared hypotheses, not formal
certification or an instance test.
