# Independent whole-proof review

## Verdict and reviewed bytes

**PASS.** The new actual-map theorem and every stated consequence in
`PROOF.md` are justified by the four pinned inputs and the written
arguments. No correction is required. In particular, the proof establishes
injectivity of simultaneous multiplication by all three positive
coordinates on the whole actual `H1(B(3))`, not just its positive part.
It establishes the actual scalar second-arrow nonvanishing, multiplicity
rank exactly one for `K`, and the canonical identification of the full
curried image with the actual 43-dimensional reachable middle. It does not
choose a scalar incidence or a trace value.

This independent review binds these exact SHA256 values:

* `PROOF.md` (11576 bytes):
  `3e63ddf20c265068aa83dfd07db008437ca8a928e4699ce7060af281c5e668f5`
* `verify.py` (3484 bytes):
  `7f60d6b1b585df8f2d47ceb1834d8da5288246409d26f5b0877afdb24e3889b5`
* `INPUTS.json` (1996 bytes):
  `3b138eed1af60a155c2ead82aedb4c6f6a934f67f7e708454ed5dc528132430c`
* `REPRODUCE.md` (938 bytes):
  `3416d638964cec0e309ed40945fa9a86e71a2a8ab45f5441bdeb4dd4d7b7d8e8`
* `RESULT.json` (315 bytes):
  `dc328337a1f7c4a2b7f0d4df6c80c143ae95b97c4bf390569bd3e0cb23986e89`

This is an independent mathematical review, not a formal proof-assistant
certificate or an independent numerical evaluation of an HM map. The
inherited HM geometric and cohomological facts remain explicitly pinned
premises. The review checks their use and the new deductions, not an
unbounded recursive re-proof of every earlier reference.

## Complete input reading and authentication

I read `INPUTS.json` and all four local originals in full, including
their hypotheses, proofs, dependencies, and scope limitations. I also
independently fetched each complete file through the read-only GitHub
connector at the exact manifest commit and path. Each successful fetch
returned precisely the manifest Git blob. The bounded checker separately
recomputed the local byte count, SHA256, and Git-blob SHA1 of each complete
copy, with all twelve checks passing:

* PR485, commit `251d9a62e97b36ad61191bfa603cdb384a3839f3`,
  `research/hm/section-tail/PROOF.md`, 12419 bytes;
  Git blob `938dc53a2905d32971d0512dfddbd71d1d647c04`;
  SHA256 `9bbfd053d4ef81ab0659e76593a5f793875c1cad9fc091bad9a4a46fda8af886`.
* PR931, commit `e28d3b74d4288239426ad1e675e806310fadf8be`,
  `research/hm/positive-reachable-middle/PROOF.md`, 10551 bytes;
  Git blob `060ad3bacb45086349e911265d6c0d6157bef4a0`;
  SHA256 `2f135afb909aa11483274a1eae49cbb3aa311f36b66b478bbeab59ad38072f8b`.
* PR1114, commit `fc79bc119a251c16d386467333f55cd46dc75367`,
  `research/hm/repeated-v-channel-pencil/PROOF.md`, 12440 bytes;
  Git blob `ef68e9d6ce7583f2f146443f157ba895e2d16925`;
  SHA256 `4ecb2dfce5a532932e29063a4ee79c2431ab1c74b00c8a3eee16d6b9ddbf2e87`.
* PR1050, commit `ec18a0fd62c4a9495adf6aad9564d379afc42b62`,
  `research/hm/canonical-negative-string/PROOF.md`, 9452 bytes;
  Git blob `8563bb31385dac0174b3d17bcae7bfa9dcfad716`;
  SHA256 `6c2f23ce2110ee91b05631e1e31932a5fe5ecb36e86731cb5e79518879f7b67d`.

Thus the authentication covers the actual content at the pinned repository
revisions, not merely agreement among unauthenticated local filenames.
No repository write was made.

## Section 2: the essential actual section multiplication

The change from PR485's four-dimensional section-space name `V` to `U`
is necessary and is handled correctly: that section space must not be
confused with the positive three-dimensional coordinate representation.
For `E0=F(3)`, the normalized identity
`B=Sym2(F)(1)` indeed gives `B(5)=Sym2(E0)`.

The primary section resolution in PR485 puts the four generators in
degree zero, fifteen further generators in degree one, and the first
relations in degree two after twisting to `E0`. It therefore proves the
actual injection `T tensor U -> H0(E0(1))`, not just the dimension of
its putative image. The distinct convention `G_j=H0(B(j-1))` is kept
separate and translated correctly at the end of the argument.

I checked the derivation of the quotient in equation (7), not just the
claim that PR485 states it. Twisting PR485's symmetric-evaluation complex
by one makes its left term `det(U) tensor O(-4)`. Its zeroth cohomology
and the required intermediate line-bundle cohomologies vanish on P4.
Consequently the first image sheaf has sections
`Lambda2 U tensor T` and vanishing H1. The next image sheaf therefore
has sections the indicated quotient of `U tensor H0(E0(1))`.
The last cokernel is `Lc^2(1)`, which has degree -1 on each of the
disjoint degeneracy lines and no sections. This identifies that image
sheaf's sections with all of `H0(B(6))`.

Inside the numerator, `U tensor (T tensor U)` is genuinely embedded.
The alternating-evaluation denominator lies entirely in this embedded
subspace and is exactly `T tensor Lambda2 U`. Hence quotienting that
subspace produces `T tensor Sym2 U`, and its inclusion in the larger
quotient is injective. The augmentations in the symmetric-evaluation
complex identify this inclusion with natural multiplication on the actual
sections `H0(B(5))=Sym2 U`. This proves (9) as an actual-map statement.
It does not infer a kernel from generator counts alone and does not
depend on a noncanonical splitting. Restricting the coordinate factor
from T to V preserves injectivity.

## Section 3: exact joint-kernel chase and equivariance

The three independent positive linear forms cut out the negative line
regularly. Tensoring their Koszul complex with a locally free sheaf A
preserves exactness. The displayed twists 3, 4, 5, 6 in (10) are correct.
Its first map is injective, and its second image Z is exactly the kernel
of `V tensor A(5) -> A(6)`.

The first short exact sequence in (11) gives the relevant part of the
long exact sequence

    Lambda2 V tensor H0(A(4)) -> H0(Z)
      -> Lambda3 V tensor H1(A(3))
      -> Lambda2 V tensor H1(A(4)).

When `H0(A(4))=0`, this identifies H0(Z) with precisely the kernel
of the last displayed map. Independently, taking sections of the sheaf
kernel description of Z identifies H0(Z) with the kernel on degree-five
sections in (13). The use of left exactness here requires neither a
surjection onto A(6) nor any higher-cohomology vanishing. These two
identifications use the same actual Koszul maps and give an exact image
chase, without an unresolved spectral-sequence differential.

Under `Lambda2 V = V* tensor Lambda3 V`, the left Koszul differential
is the simultaneous three-coordinate multiplication map tensored with
`Lambda3 V`, with the standard alternating signs. For example the three
terms from `v1 wedge v2 wedge v3` pair with the three multiplication
components in the corresponding exterior-dual basis. No single chosen
coordinate map is asserted injective. Tensoring with the determinant
line does not affect vanishing; for G this line is moreover trivial
because its determinant is a one-dimensional character of the perfect
group. Therefore the representation identifications used later also
carry no hidden character twist.

For A=B, PR485 supplies H0(B(4))=0, and the actual injection (9) kills
the section-relation kernel. This proves (14) on all of H1(B(3)). Since
V has positive central parity, the map preserves parity, and restriction
to the positive eigenspace gives the stated injective btilde. No H2/H3
term, parity switch, or determinant factor has been omitted.

## Reachable image and the actual quadratic curry

PR931 identifies R with an actual image of a and an actual restriction
kernel, not merely an abstract representation with the same character.
The two-step polynomial action satisfies ordinary coordinate
associativity and commutativity. Thus for a source `y tensor z`, its
full quadratic curry sends x to `b(x,a(y,z))`, exactly `btilde a`.
Injectivity of btilde now gives `ker Cplus=ker a` and the canonical
isomorphism `R -> btilde(R)=im Cplus`.

The resulting character `1+3A+2V+3P+3D` has dimension 43. The middle
P3 has dimension 46 and is itself embedded by btilde. Both embeddings
land in `V* tensor N4`, of dimension 111, not in N4 of dimension 37.
The paper explicitly distinguishes these spaces. This closes exactly
the second-arrow-kernel gap left open in PR931 and makes no unsupported
claim about a particular quadratic or coordinate.

## Section 4: scalar faithfulness and multiplicity rank

The one-dimensional trivial isotypical part H of P3 cannot be killed by
an injective btilde. Consequently b on `V tensor H` is nonzero.
That source is irreducible of type V, so equivariance makes b injective
on it, with an actual nonzero embedded image B0 of type V. Its target is
the full V-isotypical space F4; no residual row or replacement copy has
been inserted at this step.

The secondary scalar-only argument is also valid independently of (9).
The Koszul chase embeds the joint kernel, after the trivial determinant
identification, into `V tensor H0(B(5))`. PR1050 Section 2 obtains the
actual section character `1+P+D` by dimension exhaustion and the natural
symmetric-square isomorphism. It does not identify sections with an
Euler character without controlling other cohomology. The resulting
ambient character is `2A+2V+2P+2D`, dimension 30, with no scalar.
Semisimplicity over C then excludes a scalar joint kernel.

PR1114's scalar first map s is onto H: PR931's actual reachability
contains H, and only the V-isotypical source can contribute a scalar
to `V tensor N2`. Its second multiplicity map d represents exactly
the b just shown nonzero on `V tensor H`. Thus d is injective from a
line. The actual Q is invertible on the two-dimensional multiplicity
spaces. It follows that `K=Q^{-1}d s` has rank exactly one, its kernel
is `ker s`, and its image is `Q^{-1}(im d)`. Rank here is a deduction
from the proved maps, not an evaluated instance matrix. The paper
correctly excludes K=0 without excluding nonzero nilpotency.

## Section 5: conditional incidence sharpening

The source2 pure-V compatible-radical, residual-large, and R=0 premises
are all retained by reference to PR1114 Section 4. That reference's R=0
is the source correction hypothesis, not the newly discussed nonzero
reachable middle also denoted R in the main theorem. No conclusion is
being made under an assertion that the reachable middle vanishes.

Under those hypotheses, the genuine negative projector is applied only
after b. PR1114 supplies `p_V e0=rho r`, `lambda=rho Q`, the line
`L_h=ker lambda`, and the criterion with `B0 subset NR4` or
`V_h=V_s`. The new B0 is a nonzero V subspace of F4. Because
`(NR4)_V=V_R` is precisely one V under the hypotheses, its inclusion
in NR4 is equivalent to equality with V_R. This justifies (5) without
moving e0 to P3 or confusing isotypical multiplicity lines.

Since s is onto, `im K=Q^{-1}(im d)`; the first incidence is therefore
exactly `im K=L_h`. Since d is injective, the second is exactly
`ker K=L_h`. On a two-dimensional space a nonzero rank-one K has
`im K=ker K` if and only if it is nilpotent, equivalently `tr K=0`.
Thus if both incidences hold, the trace must vanish. Conversely, trace
zero makes the two incidence assertions equivalent, not automatically
true: their common line need not be L_h. The written proof states this
correctly. For nonzero trace the incidences are mutually exclusive.
Neither incidence, either trace regime, or source realization is selected.

## Bounded checker and execution

I inspected the complete checker before running it. Its arithmetic is
exact in the fixed quadratic character field, on nine fixed conjugacy
classes. Its finite symmetric-power recurrence and tensor identities
check the characters, dimensions, and first-arrow character subtraction
used in the text. Its degree comparisons check the stated conventions,
not the existence of a geometric resolution. Its two Koszul-index
checks are only bookkeeping and are not substituted for the sheaf
chase. The twelve authentication checks use full source bytes.

Both `python verify.py` and `python -O verify.py` passed all 33 checks.
Both outputs were compared with `RESULT.json` and matched it exactly.
The implementation uses explicit `require` exceptions rather than
Python assertions, so optimization does not disable the checks.

The printed scalar image dimension and transported operator rank are
written-theorem consequences, not independently calculated actual ranks.
This limitation is accurately disclosed in the checker, reproduction
instructions, and proof. The checker is appropriate supporting evidence,
not an independent proof of geometric exactness or natural-map identity.

No selected actual HM/source coefficient, parameter, point, derivative,
jet, tensor, matrix, or instance rank was evaluated. No large computation
or public write was performed. Apart from read-only source retrieval,
file reading, and ordinary digest/byte/output comparisons, the only
executed mathematical program was the supplied bounded checker in its
normal and optimized modes.

## Whole-proof conclusion

The proof is a genuine additional structural constraint on the actual
HM module: absence of linear relations among its degree-five adjoint
sections forces joint positive-coordinate faithfulness in degree three.
It is not a repackaging of the abstract rank-at-most-one identities in
PR1114. It validates exactly the new theorem and consequences advertised,
while preserving the unresolved incidence, trace, source-occurrence,
higher-symbol, Smith-exponent, and algebraicity boundaries.
