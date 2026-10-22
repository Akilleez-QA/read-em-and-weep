# Independent review: intrinsic radical filtration and degree-eight core

## Verdict and exact reviewed text

**Verdict: sound within the stated hypotheses and evidential boundary.**
The reviewed proof establishes the canonical radical filtration, its
dimensions and characters, the fixed-pencil middle-quotient decomposition,
and the intrinsic extraction of the complete degree-eight core. No
mathematical correction is required for this version.

The reviewed file is `PROOF.md`, entitled *The intrinsic radical filtration
and degree-eight core forced by source2*, with SHA-256

    27a8802a004cb659e1b33cae9aabaca1e8188b1382d8477cac2bb31264c40937

This digest was checked directly. This review applies to precisely those
bytes, not to later changes. The review is an independent written
deductive audit, not proof-assistant certification. It establishes no
unconditional existence, realization, or exclusion of actual source2
tensors.

## 1. Public dependencies and provenance

The six sources below were retrieved directly from
`Akilleez-QA/read-em-and-weep` at their immutable public commits. Their
returned contents were compared with the corresponding local proof files;
all comparisons were equal. SHA-256 digests were independently computed
from those public contents. The Git blob identifiers were also checked.

1. [PR791: exact fixed-pencil endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md)
   - Commit: `2cd033a4a5ba549d07330427cd779364cb83c0fb`.
   - Git blob: `5a0d16a2f22032f1a0583b92ad71661b5abab59d`.
   - SHA-256: `8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290`.
   - Checked uses: the full, rather than partial, two-dimensional
     Jacobson radical; its square-zero property; the constant first-block
     separation; full faithfulness of fixed-variable reconstruction; and
     the contravariant orientation under duality.

2. [PR792: V-channel image pencil](https://github.com/Akilleez-QA/read-em-and-weep/blob/2f01f18960ce56b8b2a0c1260c277de3c5f916bf/research/hm/source2-radical-rank-profile/PROOF.md)
   - Commit: `2f01f18960ce56b8b2a0c1260c277de3c5f916bf`.
   - Git blob: `76bee93507d1a2d0840926d4e4e27edadfebb7d7`.
   - SHA-256: `0d4eb3e4e9e98dd9ea8202399590f9741c06771411d5ce40e69a139c461b3798`.
   - Checked uses: the exact image characters `(D,T,P)`, the
     factorization through the endpoint evaluation system, and the actual
     cohomological injections into the residual for every balanced
     endpoint and both residual coupling classes.

3. [PR793: A-channel image profile](https://github.com/Akilleez-QA/read-em-and-weep/blob/ba9234964af5d879675d19ae97847a9475792f98/research/hm/source2-a-channel-rank/PROOF.md)
   - Commit: `ba9234964af5d879675d19ae97847a9475792f98`.
   - Git blob: `9fd685d919caf88142441d4788e8ff59ea23fb7a`.
   - SHA-256: `7a9e75e9f1d22bb058039a94452e6edc1b788faa6e716dc5489f877346ab170a`.
   - Checked uses: first-space injectivity, the middle-space isomorphism,
     the final surjection onto endpoint cohomology, its kernel character
     `V+P`, and the precise image-pencil maps.

4. [PR794: complete radical-rank stratification](https://github.com/Akilleez-QA/read-em-and-weep/blob/7fd254100b83bb03f41b776ea3119690aa51f671/research/hm/source2-radical-rank-locus/PROOF.md)
   - Commit: `7fd254100b83bb03f41b776ea3119690aa51f671`.
   - Git blob: `3ad30b9aa1920408cc34778e78405f544b5adc8e`.
   - SHA-256: `a256ec6cc92b1151a6551e6692cfa32cac02bceaad34c60746f51f249256cf4c`.
   - **Sections 5 and 6 were read and checked, not replaced by their
     individual-channel rank consequences.** Section 5 proves that the
     first A-channel and V-channel copies of `D` are distinct. Section 6
     proves independence of the final two `P` rows on their
     two-dimensional multiplicity space. These are exactly the stronger
     inputs required for the sum of radical images and the intersection
     of radical kernels.

5. [PR789: residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md)
   - Commit: `2d1642ad40ae1111b84b50eeaca0426bfbfbb314`.
   - Git blob: `23ca8a7469e4f2817c081661435cd498e5045fa0`.
   - SHA-256: `7eb626caae70e62613e8a3e318ac4c6a858502c4fdecfb44a6693e3ed85635c3`.
   - Checked uses: the genuine quotient `R -> C`, its complete
     degree-eight intersection, and the arbitrary-coupling annihilator
     sequence. In particular its Section 6 does not make a horizontal
     residual splitting assumption.

6. [PR790: first constant block and actual-source transfer](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md)
   - Commit: `af0e03d26da5e47d18ae732291aca46f4d448dc5`.
   - Git blob: `0641ffadf54324d5520aec89767658e938815223`.
   - SHA-256: `0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4`.
   - Checked uses: the genuine constant degree-ten direct summand and
     Section 6's simultaneous identification of reconstructed arrows
     with the fixed original pencils under its actual-source hypotheses.

The verdict uses these published results with their stated hypotheses.
It does not purport to replace their earlier actual-source dependencies
by an independent verification of the original HM construction.

## 2. The residual evaluation diagram is genuinely exact

The central new exact sequence is justified at the level of the specified
evaluation maps, not merely by equality of splitting types. The given
constant projection supplies `R -> C` with kernel `A0`. Since all three
terms are vector bundles, duality gives the exact column

    0 -> C* -> R* -> A0* -> 0.

The constant coefficient column is

    0 -> H_t -> Hbar* -> V1* -> 0.

The evaluation squares commute for the reasons stated in Section 3:
restriction to `A0` depends only on the `V1*` component, and restriction
of an endpoint functional to `R` is induced by `R -> C`. The kernel
column is consequently exact by the snake lemma:

    0 -> E_C -> E_R -> E8 -> 0.

Its quotient is the actual annihilator of the complete inclusion
`U_2^8` in `Sym^8 W O`. Apolarity identifies this annihilator with
`U_5^8=T O(-3)`. Thus the quotient evaluation sequence is precisely the
complete degree-eight evaluation sequence, not a substitute chosen from
its bundle characters.

The proof checks all vanishings needed for the particular cohomological
sequence:

- `H^1(C*(-2))=H^1(O(16))=0` and
  `H^1(C*(-1))=H^1(O(17))=0` give exactness at vertices two and three.
- `H^0(E8)=H^0(T O(-3))=0` supplies injectivity on `H^1(E_C)`.
- `H^2(E_C)=0` on the projective line supplies surjectivity onto
  `H^1(E8)`.

Multiplication by each fixed linear form commutes with both quotient
maps. Naturality of the connecting homomorphisms supplies both
second-pencil squares. The resulting sequence

    0 -> N_C -> N_R -> N8 -> 0

is therefore a short exact sequence of the actual fixed-variable pencil
systems. No general exactness assertion about reconstruction is needed.

## 3. Full radical image and common kernel

PR791 identifies the full radical and accounts for its opposite-algebra
orientation. On reconstructed pencils the radical kills `N_R` and maps
`N0` into it. The image and kernel computations in the reviewed text use
this orientation consistently.

For every radical element, its image, and its kernel, are subpencils
because it commutes with every arrow. Sums and intersections are
therefore subpencils. The inclusion `JN subset Ann_J N` follows from
`J^2=0`. The two-sided ideal property proves preservation under all
fixed-pencil endomorphisms, not only invertible ones. Conjugation of the
full radical gives the claimed isomorphism invariance.

At vertex two the endpoint character is `Sym^16 W=V+P+2D`.
PR794 Section 5 proves that the two radical `D` images cannot coincide:
such a coincidence would lift from the globally generated trivial
`Q0(-2)` to a quotient-bundle factorization and would force middle
V-channel image dimension ten rather than six. Consequently their sum
is direct, and the sum of all radical images is the entire `P+2D`
isotypic part. At vertices three and four the A-channel already fills
the endpoint spaces. This verifies the precise subpencil description
of `JN`, including its arrows, and gives `N_C/JN=V[2]`.

For the common radical kernel, the A-channel's injectivity and middle
isomorphism remove all first-block contributions at vertices two and
three. At vertex four the domain is `V+2P+D` and the common target is
`P+D`. The A-channel is nonzero on `D` and has kernel `V+P`.
PR794 Section 6 proves that the V-channel is nonzero on the `P` in
that kernel, using balancedness and connecting-map naturality. Hence
the two `P` functionals are independent, and their common kernel on
the two-copy `P` isotypic part is zero. Both channels kill `V`, which
does not occur in their target. The common first-block kernel is
exactly `V` at vertex four.

The resulting equality

    Ann_J N = N_R direct-sum V[4]

is justified as a pencil equality in the chosen genuine first-block
normal form. There are no incoming arrows from `N_R` to this extra
`V`: reconstruction preserves the constant direct sum `N0 plus N_R`,
and the annihilator has no `N0` component at the preceding vertices.
This is not an unjustified inference from a character decomposition,
and it does not assert that `V[4]` splits off the entire system `N0`.

## 4. Middle quotient, characters, and dimensions

Quotienting the residual exact sequence by `JN` gives

    0 -> V[2] -> N_R/JN -> N8 -> 0.

The maps to `N8` at vertices three and four are isomorphisms.
Semisimplicity of complex finite-group representations gives an
equivariant section at vertex two. Commutation with each first arrow
then follows from injectivity of the vertex-three quotient map;
commutation with each second arrow follows from injectivity of the
vertex-four quotient map. This verifies a simultaneous section for
both pencils with the same variables. Every such source-vertex
section works because its ambiguity lands in the isolated `V[2]`.

Together with the preceding annihilator calculation, this proves

    Ann_J N/JN is isomorphic to N8 plus V[2] plus V[4].

The dimensions and characters independently reconcile as follows:

    N8 = (A+V+P+D, W'+S+2T, V+P+D),
    dim N8 = (15,18,12);

    JN = (P+2D, W'+S+2T, P+D),
    dim JN = (14,18,9);

    Ann_J N = (A+2V+2P+3D, 2W'+2S+4T, 2V+2P+2D),
    dim Ann_J N = (32,36,24);

    Ann_J N/JN = (A+2V+P+D, W'+S+2T, 2V+P+D),
    dim(Ann_J N/JN) = (18,18,15).

Adding the genuine first-block characters to the residual gives
`dim N=(41,54,37)`, as stated. Subtraction gives the additional
quotient dimensions `(9,18,13)` and characters
`(P+D, W'+S+2T, 2P+D)`. All these are universal character deductions,
not computations at an actual source instance.

## 5. Intrinsic recovery and limits of canonicity

The proof establishes the needed arrow properties for the specific
complete degree-eight system. Its first arrows are multiplication on
`A tensor Sym^4 W`, hence injective for each nonzero linear form.
Twisting its evaluation sequence by `-1` makes the constant middle
term acyclic and identifies `H^0(Q8(-1))` with `H^1(E8(-1))`.
Connecting-map naturality then identifies a second arrow with

    H^1(T O(-4)) -> H^1(T O(-3)).

Serre duality makes its scalar factor dual to multiplication
`H^0(O(1)) -> H^0(O(2))`, which is injective. Thus every nonzero
second arrow is surjective. This argument uses the actual evaluation
sequence, not just the dimensions of its three spaces.

It follows that in the canonical middle quotient `K`, the common
first-arrow kernel `Z2` is exactly the isolated source piece and the
sum of second-arrow images `D4` is exactly the degree-eight last
space. The construction

    L=(K2,K3,D4),  Z=(Z2,0,0),  Core_J(N)=L/Z

is consequently a well-defined intrinsic subquotient of fixed-variable
equivariant pencils and has isomorphism type `N8`. In fact each
nonzero first arrow has the same kernel `Z2`, and each nonzero second
arrow has the same image `D4`.

The proof correctly separates these assertions of canonicity:

- `JN`, `Ann_J N`, `K`, `Z`, `L`, and `Core_J(N)` are intrinsic.
- The isolated last piece is canonically the quotient `K/L`.
- A section of the source extension and a complementary isolated
  last-vertex subspace are not asserted to be canonical.
- No preferred scalar-normalized identification of the core with the
  displayed complete degree-eight model is asserted.

In particular the finite-dimensional splitting after quotienting by
`JN` does not imply a constant horizontal splitting of `R`. The
isolated source piece is outside the negative-evaluation objects to
which the reconstruction theorem applies. There is no invocation of
essential surjectivity for arbitrary pencil systems.

## 6. Final scope assessment

All conclusions hold uniformly over every balanced endpoint and both
residual coupling classes in the stated normal-form family. The only
horizontal separation of the original inclusion used is the published
constant first-block theorem. The residual quotient is always handled
through genuine morphisms and natural cohomology.

Transfer to fixed actual source2 tensors remains conditional on the
published actual-source hypotheses and common-pencil identification of
PR790. The proof does not measure the actual HM endomorphism algebra,
select an endpoint or coupling, claim a realization, exclude source2,
or make a statement about endomorphisms of the entire HM module or
bundle.

The audit used structural deductions and source-integrity checks only.
No actual source coefficients, parameters, points, derivative values,
matrices, instance ranks, selected models, scans, or large computation
were chosen or evaluated. Subject to its explicit dependency and
actual-source boundary, the reviewed text is publication-ready.
