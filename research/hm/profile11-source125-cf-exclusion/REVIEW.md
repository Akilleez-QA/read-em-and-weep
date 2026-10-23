# Independent review of the source125 cf exclusion

## Verdict and exact reviewed bytes

PASS. I found no mathematical gap in the complete source125 cf exclusion at the exact file hashes below. This is an independent written-mathematics audit, together with a successful independent execution of the bounded verifier. It is not Lean certification, an evaluation of a selected source instance, or a claim about the entire stable label.

SHA256 bindings:

- `PROOF.md`: `4ca484460729d1873eab5e6ff1beb534927abc865b478e9bfa971ac928ded05c`
- `verify.py`: `f2dbdd99e2b4c33e2acb81caceafc0d1fa5d731a578163d8e0d2f6a5b4198870`
- `REPRODUCE.md`: `585ac477f0e150714fbb935aefe50bd352fa9a95bde10849fc2e7413afef4384`

The scope is precisely source index125, tuple `(0,0,1,0,0,1,0,1)`, stable label `G3.11.ea6bced3bddf`. The high-D and high-(P+D) kernel classifications and the reusable linear-channel argument are used as universal lemmas from the stated bf/ef dependencies, not as exclusions of the present source. I read those dependency arguments and the underlying strict-top, saturated derivative-image, first-polar and quadratic-gap arguments while checking their use here.

## Actual-connection and saturation audit

1. Section 1.1 uses the exact degree-six V system. Its kernel is `Wp O(-5)`, all internal channels vanish, and the first span has rank4 and degree0. Thus the projected P is an actual constant subspace. Its quotient by the V top identifies with the saturated `O(6)` in the original quotient, so the intersection is exact and the subsequent negative-tail strict-top contradiction applies.

2. Section 1.2 is valid without assuming that the whole second-span quotient is saturated in the quotient by Z. The complete top system has kernel `T O(-3)`, first span `(Wp+T) O(-1)` and first increment rank1. Quadratic generation and the nonconstancy of that first span give a constant second span of rank9. The V tail has zero external derivative and only its top V internal channel. Consequently its coherent image after projection by the genuine constant second span is preserved by the regular connection.

   The coherent-image lemma is essential and correct: first the saturation is horizontal, hence constant; connection preservation then excludes a positive elementary-divisor exponent in the unsaturated lattice in characteristic zero. The image itself is therefore a constant bundle. Ranks1 and2 would have trivial representations and are excluded by `Hom_G(V O(-4),O)=0`. A rank3 image would be an equal-rank quotient bundle of `V O(-4)`, hence an isomorphism, contradicting degree. The tail therefore lies in the same constant rank9 space as the disjoint rank7 top. The resulting rank10-versus-rank9 contradiction closes this obstruction.

3. Every use of a nonzero degree6 or degree7 covariant as a saturated line system is justified by the invariant-divisor lower bound12. For the combined high-D internal image, quotienting by the Euler `Wp O(-5)` cannot kill a nonzero P line component: such killing would require the vanishing Hom from `O(-10)` to `Wp O(-5)`. The resulting degree7 quotient component is again saturated. Thus there is no hidden divisor in the four internal-image possibilities or the subsequent first-span degrees.

## Lower-P-zero branch

The three high-(P+D) kernels give exactly the listed internal images `0`, `V O(-4)` and `O(-10)`. The zero case descends by a genuine constant first span; the line case uses precisely the previously established linear-channel argument, whose proof depends on F and its actual first span rather than on the changed complementary tails.

For `J=V O(-4)`, both V-low-row alternatives are included. If the V row to `O(4)` is zero, the full-top kernel sits in an exact sequence with subbundle `K1` or `K2` and quotient `V O(-2)`. Both ends have zero Hom to the remaining internal target. Therefore the full quadratic rank12 block has actual saturated first increment `O(18)`, excluded by the universal alternatives24 or at most11.

If the V-low row is nonzero, its degree6 system is onto and has kernel `Wp O(-5)`. Together with the onto high row on F it covers the positive pair everywhere. The full external kernel is now an extension with quotient `Wp O(-5)`; the same zero-Hom argument applies. The first span has rank14 and degree0, is genuinely constant, and intersects E exactly in the full top. Its constant projection leaves only the three negative tails. Thus no scalar alternative was omitted from the lower-P-zero argument.

## Final two first-span branches

For the constant `(A+P) O` first span, the intersection and high quotient follow from the actual saturated derivative image. The remaining `O(-8)` has exactly its V, P and scalar channels. A nonzero scalar gives Section 1.2. If both V and P are nonzero, the twist-zero cohomology map is an isomorphism on its inequivalent V and P factors, forcing the rank6 quotient to be `T O(-1)`; its first span is an actual constant `V+P`. The V-only case has a positive-degree direct summand, and the P-only case has the exact constant V quotient. These exhaust all nonzero line embeddings.

For `A O+T O(-1)`, the canonical Euler `Wp O(-3)` is an actual source subbundle: all other internal components and its possible D lift vanish. Its onto lower derivative supplies the second positive direction in the genuine constant second span. Thus `C/N` maps generically isomorphically to the positive pair. The map factors through that saturated pair, and equal rank and degree make it an isomorphism everywhere. This proves the exact intersection and saturated negative-only projected derivative image, rather than presuming them.

In the final presentation, a nonzero scalar leaves a section-free negative bundle and the degree contradiction `-30 > -90`. A zero scalar with nonzero V component gives a locally free rank4 degree-zero direct summand, which is an actual constant four-space in the ambient constant bundle. The remaining tails again contradict strict-top. If scalar and V both vanish, the Wp-only quotient is the positive line `O(6)`. All scalar-zero and scalar-nonzero cases are covered.

## Verifier and reproduction audit

I inspected `verify.py` and ran `python3 verify.py` independently against the exact frozen bytes. It exited successfully with:

    PASS: 105 fixed internal Hom checks, polar and trapped-tail identities, original source125 cf identity.
    No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.

The verifier checks the two immutable catalog Git blob hashes before parsing their contents. Its representation arithmetic is restricted to the fixed universal identities and Hom tables used by the proof. The reproduction instructions name those same immutable inputs and the same expected command/output. The arithmetic output is not substituted for the connection, saturation, exact-intersection or exhaustion arguments audited above.

No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance ranks, experiments, scans or large computation were used in this review. No publication action was taken. This approval applies only to the three exact byte sequences bound above; substantive changes require renewed review.
