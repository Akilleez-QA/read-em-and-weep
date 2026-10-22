# Independent review of the universal A-channel radical image profile

## Verdict and exact object reviewed

**Verdict: sound as a structural, conditional theorem.** No substantive
gap was found in the argument for the A-channel image characters
`(P+D, W'+S+2T, P+D)`, ranks `(9,18,9)`, or the stated fixed-variable
image pencils. The generic-middle-rank corollary follows with its stated
limitations. The distinction between the image system and the full
endpoint evaluation system is essential and is handled correctly.

This review applies to `PROOF.md`, titled **The universal A-channel
radical image profile for source2**, with exact SHA-256

    7a9e75e9f1d22bb058039a94452e6edc1b788faa6e716dc5489f877346ab170a

The file's digest was checked before review and again after the review
was written. Review date: 2026-10-22. This is a deductive mathematical
review, not proof-assistant or formal certification. It does not verify
the existence of an actual HM/source2 realization or independently
re-establish the earlier actual-source hypotheses.

## 1. Dependency and provenance audit

All four direct dependencies were retrieved from
`Akilleez-QA/read-em-and-weep` at the exact immutable commits named in the
proof. Their relevant assertions agree with the inputs used here. The
retrieved contents were also checked against their returned Git blob
identifiers. The following SHA-256 digests identify the retrieved file
contents, without local newline changes.

1. [PR789: residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md)
   - Commit: `2d1642ad40ae1111b84b50eeaca0426bfbfbb314`.
   - Git blob: `23ca8a7469e4f2817c081661435cd498e5045fa0`.
   - SHA-256: `7eb626caae70e62613e8a3e318ac4c6a858502c4fdecfb44a6693e3ed85635c3`.
   - Sections 2 and 5 establish the arbitrary residual graph and the
     two zero/nonzero quotient-coupling classes. Section 6 supplies the
     exact annihilator sequence for every coupling over every balanced
     endpoint. Section 2 records the representation products used in
     the present character computations.

2. [PR790: first constant block](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md)
   - Commit: `af0e03d26da5e47d18ae732291aca46f4d448dc5`.
   - Git blob: `0641ffadf54324d5520aec89767658e938815223`.
   - SHA-256: `0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4`.
   - Sections 1–5 supply the genuine constant separation of
     `U_8^10` and the annihilator `E0=W O(-9)`, rather than an abstract
     bundle splitting declared horizontal. Section 6 proves the
     simultaneous identification of natural reconstruction with the
     original fixed pencils under its actual-source hypotheses.
     Sections 7–8 supply the block characters and compatibility with
     both residual constant-gauge classes.

3. [PR791: exact pencil endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md)
   - Commit: `2cd033a4a5ba549d07330427cd779364cb83c0fb`.
   - Git blob: `5a0d16a2f22032f1a0583b92ad71661b5abab59d`.
   - SHA-256: `8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290`.
   - Sections 4–5 show that the A and V constant channels are exactly
     the two-dimensional square-zero radical, and in particular that
     every A-channel map carries `R` into `U_8^10`. Sections 6–7 give
     the fully faithful, fixed-variable reconstruction and distinguish
     its covariance from the contravariance of ambient duality.

4. [PR786: endpoint Wronskian](https://github.com/Akilleez-QA/read-em-and-weep/blob/575c0720268af5bb4b305e29284f65614ba9f9ca/research/hm/source2-endpoint-wronskian/PROOF.md)
   - Commit: `575c0720268af5bb4b305e29284f65614ba9f9ca`.
   - Git blob: `1a7206b974f3687a292a11cda1a427558b95321d`.
   - SHA-256: `858a750d6a7c320affc28fcea614164e5c9c40fcf96be687faa1cc9d38af99c0`.
   - Sections 1 and 3 give the full projective orbit-size list,
     uniqueness of the exceptional twelve-orbit, perfectness of the
     binary group, and the consequent invariance of its orbit form.
     No evaluated Wronskian or exceptional endpoint value is required
     by the proof under review.

The present theorem is independent of any claim about the individual
rank profile of the V channel. Its actual-source application retains the
explicit conditions inherited from PR790; those conditions are not
silently promoted to established actual-source existence.

## 2. The A18 subsystem is basepoint-free

The base-divisor argument is complete. A common base divisor of `A18` is
effective, invariant, and of degree at most 18. The allowed orbit sizes
are exactly 12, 20, 30, and 60. Thus a nonempty such divisor must be the
unique reduced twelve-orbit, with multiplicity one: a second copy would
already have degree 24.

Its defining form spans a stable line. Perfectness of `G` makes that
line's character trivial. Division by this invariant form would
therefore give an equivariant embedding of `A` into `Sym^6 W=V+P`, which
is impossible. This proves basepoint-freeness of `A18` itself, a stronger
fact than basepoint-freeness of the larger endpoint system.

Consequently the evaluation kernel `E_A` is a rank-two vector bundle of
degree -18. Its global sections vanish because the three elements of
the subsystem are linearly independent. No balanced-endpoint assertion
is needed for this step, and the proof correctly uses the full orbit
list rather than only its minimum.

## 3. The kernel map is an everywhere isomorphism

The map `g:E0 -> E_A` is genuinely induced by the constant A-channel
projection. Preservation of the full annihilator, together with the
genuine projection `R -> C`, places its image in the kernel of evaluation
on `A18`. This establishes the commutative evaluation diagram before
any rank or determinant argument is used.

Under the invariant apolar pairing, `E0` is the complete first
osculating bundle `U_1^10`. The transpose of the unique A projection is
the unique three-dimensional A subsystem in degree ten. The rank of the
projection on an osculating fiber is thus the rank of restriction of
that subsystem to the corresponding first-jet space. The proof's common
symplectic point convention is important: it identifies the osculating
and jet fibers at the same projective point, not at an independently
chosen dual point.

The degree-ten subsystem has no common base divisor, because a nonempty
invariant divisor would have degree at least 12. Its independent
sections define a nonconstant morphism to a projective plane. In
characteristic zero a nonconstant rational coordinate ratio cannot have
identically zero differential. Hence the morphism has generically
nonzero differential, and its value-and-first-jet evaluation has generic
rank two. This is a separability argument, not a pointwise numerical
evaluation.

Both the source and target of `g` have rank two and degree -18. Its
determinant is therefore a nonzero section of a degree-zero line bundle
on the projective line. Such a section is nowhere zero. Thus `g` is an
isomorphism everywhere, not only generically, and is equivariantly an
isomorphism `E_A ≅ W O(-9)`. The conclusion does not assume a syzygy
splitting for `E_A`; it proves that splitting through the particular
channel map.

## 4. The constant quotient kernel and the first two images

The middle map of the evaluation diagram is surjective with constant
kernel `(V+D)O`. Since its left map is an isomorphism, the snake lemma
gives precisely

    0 -> (V+D)O -> Q0 -> O(18) -> 0.

This is a statement about the actual quotient morphism induced by the
channel. It is not inferred from the ranks or degrees of an unrelated
abstract bundle map.

After twisting by -2, the vanishing of `H0(O(-2))` makes the induced
map from `H0(Q0(-2))=Sym^8 W` injective. Its image `I_A` therefore has
dimension 9 and character `P+D`. The underlying quotient map depends
only on the fixed A projection and the unique embedded `A18`, up to
nonzero scalar. Thus its image is independent of the endpoint parameter
and of the residual graph class.

After twisting by -1, both cohomology groups of the constant kernel
twisted by `O(-1)` vanish. Hence `H0(Q0(-1)) -> H0(O(17))` is an
isomorphism. Both spaces have dimension 18 and character `W'+S+2T`.
Naturality also makes `I_A tensor H0(O(1)) -> H0(O(17))` an isomorphism:
on the `Q0=Sym^8 W O(2)` side it is the ordinary isomorphism from
constant sections tensored with linear forms to its once-twisted section
space.

The dual of the genuine residual quotient is the injection
`O(18) -> R*`. Its maps on global sections remain injective after the
two relevant twists. Composing with this injection therefore computes
the actual first and middle images of the full endomorphism. The map
vanishes on the residual domain summands, so no additional image term
has been omitted.

## 5. The final image and both residual coupling classes

The inclusion of the A evaluation sequence into the endpoint evaluation
sequence has identity on `O(18)`. Its snake sequence is

    0 -> E_A -> E_C -> (V+P)O -> 0.

Because the constant right-hand bundle has zero first cohomology,
`H1(E_A) -> H1(E_C)` is surjective. The endpoint evaluation sequence
identifies its target canonically with `H0(O(18))/H_t`. For a balanced
endpoint, `E_C=(P+D)O(-2)`, so this target has dimension 9 and character
`P+D`.

The independent residual annihilator sequence is

    0 -> E_C -> E_R -> T O(-3) -> 0.

The absence of global sections of its right-hand term makes
`H1(E_C) -> H1(E_R)` injective. The full degree-four channel map is
therefore exactly the composite of the isomorphism on `H1(E0)` induced
by `g`, the endpoint surjection, and this residual injection. Its image
is precisely the indicated embedded copy of `P+D`, and its rank is 9.

Both exact sequences concern specified inclusions and the genuine
residual quotient. Neither requires a constant splitting of the
residual extension. PR789 provides that exact structure for both
quotient-coupling classes. The argument consequently applies without
change to the nonzero class as well as to the split class. The source
character `V+2P+D` and the kernel character `V+P` agree with the exact
sequence; the proof correctly does not substitute those character
counts for the required surjectivity and injectivity.

## 6. Image pencils, orientation, and fixed variables

The constant radical map acts from the residual ambient space to the
degree-ten block before duality and in the reverse direction after
duality. The proof respects this reversal. Once the dual evaluation
sequence is formed, cohomological reconstruction is covariant. There is
no unsupported interchange of an algebra with its opposite.

Multiplication and connecting-map naturality identify the restricted
image pencils as

    I_A -> H0(O(17)) -> H0(O(18))/H_t,
    s   -> l s,         r -> [l r],

using the same linear form `l` as in the original reconstruction.
PR790 Section 6 supplies the fixed-variable identification with the
actual negative pencils under its stated hypotheses; this is stronger
than an independent representation isomorphism in each degree.

For every nonzero `l`, the first map is injective because multiplication
by a nonzero polynomial is injective. For the second map, the subspace
`l H0(O(17))` is the hyperplane of sections vanishing at the zero of
`l`. The basepoint-free subsystem `A18` contained in `H_t` prevents
`H_t` from lying in that hyperplane. Their sum is all of `H0(O(18))`,
which proves surjectivity to the endpoint quotient for every nonzero
`l`.

The image system must not be replaced by the full endpoint evaluation
system. Its first space is the nine-dimensional `I_A`, whereas the full
endpoint reconstruction starts with the seventeen-dimensional
`H0(O(16))`. The A-only evaluation system also has a sixteen-dimensional
final space `H1(E_A)`, rather than the nine-dimensional endpoint
quotient here. An isomorphism of the middle spaces does not identify
either of those larger systems with this image system. The proof
explicitly preserves this distinction and does not claim that the whole
image pencil system is endpoint-independent.

## 7. Generic middle rank in the full radical

Every element of the two-dimensional radical kills the residual
ambient domain after duality. Its degree-three map thus factors through
the fixed eighteen-dimensional space `H0(Q0(-1))`, giving a uniform
upper bound of 18. The A direction attains that bound by the preceding
argument. Nonvanishing of the eighteenth exterior power is a nonempty
Zariski-open condition on the radical vector space, which is
irreducible. It follows that a Zariski-open dense subset has middle rank
exactly 18.

This corollary neither determines the V-direction rank nor establishes
the existence or description of any additional exceptional direction.
The proof makes neither inference.

## 8. Final assessment and evidential boundary

The claimed image profile follows from the specific induced maps and
their natural exact sequences, uniformly over the balanced endpoint
family and both residual classes. Square-zero and commutation with all
fixed pencil maps follow from the pinned radical construction and
reconstruction naturality. Rescaling the nonzero generator of the
one-dimensional A channel leaves its image spaces unchanged.

The audit used structural representation identities, invariant-divisor
arguments, generic separability, bundle determinants, the snake lemma,
and natural cohomology. No actual source coefficient, selected endpoint,
point, derivative value, matrix, source-instance rank, selected model,
scan, or large computation was used. File-integrity hashing served only
to identify the reviewed text and its immutable sources.

Accordingly, the exact reviewed version is suitable for publication as
a written structural proof with the conditional and non-realization
boundaries it already states. This review authorizes no claim of formal
certification, actual-source evaluation, HM realization, or exclusion
of source2.
