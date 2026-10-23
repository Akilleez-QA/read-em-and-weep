# Independent review: exact negative-truncation extension interface

Verdict: PASS on the frozen document below, as a written mathematical
derivation from its pinned inputs. No blocking error was found. This is
not a source2 exclusion, an actual tensor calculation, or proof-assistant
certification.

Reviewer: source2_constraints, independently of the frontier_plan author.
The reviewer did not edit the reviewed document.

Reviewed file: `work/swarm/frontier-plan/TRUNCATION-EXTENSION.md`.

Reviewed SHA-256:

    7525df1e58ac8683a5a0b828209f4f35cc79a09527307ee47b35025d5c2ad636

## Source authentication and audit scope

The following exact public files were fetched and read in this review.
SHA-256 values are calculated on the fetched UTF-8 content, including its
published final newline.

| Input | Commit | Path | SHA-256 |
|---|---|---|---|
| PR476 | 3aa461bc3581fb72fbf923fbe869ddee023b435a | research/hm/five-generator-module/PROOF.md | e05d41c601aac6d89b427b4ed036e8b83a400375a53504d96a605d35646143e6 |
| PR481 | 6b20de2e4a06e7553bf2d59480cd6c02536f70a3 | research/hm/quartic-scalar-exclusion/PROOF.md | 4de5f90b0ed95a5c70cb9916b7628aacb4b74fe39e7553821a75e68dd291da14 |
| PR758 | 063216038f3aefd65617651c2426721efafc7f9b | research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md | 0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2 |

The connector returned Git blob identifiers 3d308f6fbdb5c224a085b41eec26e917a6031692,
ad2dc2a07ca4d028924eb107b613a66fbb0d06bf and
303c6927265296440470b9dd4015fe6e8d55ca4d, respectively.

The review also read the relevant actual-source bridge, algebra and
filtration sections of the previously authenticated exact PR790, PR791
and PR795 copies. Their immutable commits and content hashes are:

- PR790, af0e03d26da5e47d18ae732291aca46f4d448dc5,
  `research/hm/source2-first-constant-block/PROOF.md`,
  0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4.
- PR791, 2cd033a4a5ba549d07330427cd779364cb83c0fb,
  `research/hm/source2-pencil-endomorphism-algebra/PROOF.md`,
  8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290.
- PR795, 3f811311d76914a555c7e7d0c5b887b41805aa6c,
  `research/hm/source2-radical-filtration/PROOF.md`,
  27a8802a004cb659e1b33cae9aabaca1e8188b1382d8477cac2bb31264c40937.

Campaign source-specific.md at d79b4ed8263076476296066def7f0c5be7752707
was fetched and read for the S03/S04/S06 boundary. Its campaign directions
were checked against the claim; they were not substituted for a theorem.

The review checks the new deductions and the precise content they import.
It does not independently reprove every historical theorem used inside
PR476, PR481, PR790, PR791 or PR795.

## Adversarial checks

1. **Actual module, generation and Euler relation.** PR476 states
   K_j=H^1(B(j-1)) with the actual cohomological S-action, proves the
   degree-zero cover S tensor V -> K, and identifies the actual R_1
   with the identity tensor epsilon in T tensor V. Thus this is not a
   representation-character model or a claim inferred from bundle
   simplicity. In particular the input is K, not PR481's distinct H
   module. PR476 also checks the negative tail. The cover is therefore
   the full relevant graded module, not only a nonnegative window.

2. **The scalar argument and higher relations.** An S-linear degree-zero
   f is determined by f_0 because the cover is generated in degree zero.
   The induced free-cover map 1 tensor f_0 must preserve R_1. Comparing
   coefficients in (1 tensor f_0)epsilon=c epsilon forces every generator
   to have the same scalar c. Conversely scalars preserve every relation.
   Thus no unknown higher relation can invalidate sufficiency or create
   an additional endomorphism. PR481 independently supplies precisely the
   claimed finite relation presentation, including its possible cubic
   alternative; the argument does not need to resolve that alternative.

3. **Restriction, grading and finite lift system.** N_2,N_3,N_4 are
   K_3^+,K_4^-,K_5^+, namely H^1(B(2))_+,H^1(B(3))_-,H^1(B(4))_+.
   PR758 supplies the actual negative multiplication arrows. Equivariant
   full-module endomorphisms preserve these spaces. Their image is
   exactly the scalar identity line, and restriction is injective because
   N is nonzero. The quotient obstruction is explicitly a vector-space
   quotient, avoiding the false claim that the scalar line is an algebra
   ideal. In (7), apply the degree-zero square to epsilon: it forces F_0
   scalar. The surjectivity of successive bundled multiplication maps,
   supplied by generation, then forces all F_d through degree five to
   be the same scalar. Omitting that first square would break the proof;
   the document correctly does not apply it to the smaller window alone.

4. **Conditional source2 transfer.** PR790 identifies both reconstructed
   arrows with the same fixed original negative variables. PR791 identifies
   the full equivariant pencil algebra and handles its opposite orientation.
   Hence its dimensions four or five give obstruction dimensions three or
   four, and no nonzero square-zero radical element is scalar. The proper
   projector's dimensions (9,18,16) make it neither zero nor identity.
   The document keeps all of these statements conditional on the actual
   source2 bridge. It correctly concludes non-extension rather than using
   non-extension to claim nonexistence of the negative system.

5. **Positive-quadratic typing.** Sym^2(T_+) sends K_3^+ to K_5^+.
   Thus q_+ and Theta_+ have exactly the displayed types. Commutativity
   gives the symmetric-square factor. Applying two positive squares of
   a five-variable window map yields Theta_+=0; the negative analogue
   already follows from the given two pencil squares. Mixed sign products
   land in K_5^- and cannot be silently made into another equation on the
   marked endpoints. The derivation rule (11) proves the kernel is a
   unital subalgebra. Sufficiency for a window lift is not asserted.

6. **Exact submodule extension criterion.** The minimal actual S-span
   of U_2,U_3,U_4 in degrees three, four and five has exactly the three
   degree pieces (14). These are images in K, so all existing relations
   are already imposed. Since inversion is central, taking eigenspaces
   commutes with the indicated sums. Its degree-five positive part is
   the sum of Sym^2(T_+)U_2, Sym^2(W)U_2, WU_3 and U_4, with no missing
   sign term. Negative subpencil stability absorbs the last two W terms.
   Consequently (13) is both necessary and sufficient for the marked
   intersections. Homogeneous higher-degree relations cannot create
   additional lower-degree pieces in this actual submodule; no negative
   grading operation or saturation is being imposed. Lower-degree choices
   in another candidate cannot remove the minimal span. Nested minimal
   spans prove the nested-pair assertion without an intersection gap.

7. **Filtration and projector consequences.** The imported joint image
   and common kernel are the intrinsic PR795 spaces, not inferred from
   separate radical ranks. Their dimensions and marked placements agree.
   Their two chi maps are exactly the two instances of the theorem.
   Commutation with every radical element forces both vanishing maps;
   the converse is deliberately absent. For an idempotent, Theta_+=0
   is precisely the vanishing of both cross terms. The resulting minimal
   submodules need not remain complementary in other degrees or parities,
   so no global splitting has been smuggled into this argument.

## Final assessment and limitations

Theorem 1 gives an exact answer to the full-module lifting problem from
the actual Euler relation. Theorem 2 gives an exact answer to the stated
marked submodule-intersection problem. The finite missing q_+ interface
is typed correctly using the actual relation embeddings, and the text
states that its values are not supplied.

A nonzero chi or Theta would obstruct the proposed extension only.
The reviewed proof does not supply a theorem requiring that extension
under source2. Its recommendation to stop the projector/radical-to-full-
module exclusion route is therefore justified. This review authorizes no
change to the source2 frontier and certifies no actual tensor, coefficient,
point, parameter or rank. No such instance was evaluated in the review.
