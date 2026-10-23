# Independent review: mixed-contraction normalization defect

Reviewed 2026-10-23 against the supplied `inputs/pr815.md`, `inputs/pr816.md`,
and `inputs/ladder.md`. The reviewed `PROOF.md` SHA-256 is
`a7f6afe41fe569cb9a061a047b1d0a140fd198950cda6fe3bace6978f3cf0b14`.
This is an independent written-mathematics check of the specialized
consequences, not actual-HM evaluation, Lean certification, or verification
of the remote provenance of the supplied source copies. Local Git blob
hashes were independently checked and match the authenticated values
supplied by the coordinating reviewer:

- PR815: `bef4e26574b3085616c22d5fdaae4e808e3767e4`.
- PR816: `575004321d185de506573a1baad97bdf046b215f`.
- Ladder: `81e4b7ddf79d2c4e26ac0c99517117fe2ca63133`.

## Verdict

The core deduction is correct under its explicit premises. In particular,
the sign and multiplier in the mixed error, the source-only cone formula,
the necessary-and-sufficient regular condition, and the thirteen-dimensional
blind space for the stated affine reconstruction tests are valid. No
additional contraction normalization such as `h i=0` is needed.

The initial review identified one wording issue: the original categorical
statement that neither summand is independently invariant exceeded the
proved conclusion that their changes both equal `eta`. The final bytes
listed above resolve this issue. Section 3 now says that separate invariance
is not guaranteed by the premises and explicitly declines to claim a
genuine-HM nonzero `eta`. There is no remaining mathematical objection within
the stated scope. The reconstruction blind-space argument does not supply
a realizability assertion, and the final note correctly keeps those claims
separate.

## Checked specialized steps

1. **Transport and signs.** PR816 (1), with source `M`, target `M(t)`,
   and charts replaced by contraction choices, gives

       M_B g_0 - g_t M_A
         = p_B^(t) (T h_B + h_A^(t) T) i_A.

   Multiplication on the left by `g_t^-1` and tracefree projection give
   (N3)-(N4). Both defect terms retain positive signs. Compatibility of
   source and target twist frames is necessary for the tracefree operation;
   the note explicitly assumes the compatible tensor twists that supply it.

2. **The exact q/twist requirements.** Tensoring the same contractions
   gives (N5), including the three instances actually used:

       R_10(q^3 S) = q^3 R_4(S),
       R_4(q W_h) = q R_2(W_h),
       R_10(q^4 W_h) = q^4 R_2(W_h).

   Independent contractions merely satisfying their individual chain
   identities at twists 2, 4, and 10 would not establish these instances.
   The proof does not make that invalid inference. Frame comparison before
   harmonic extraction is likewise essential; matching only on the cone
   would not determine the third normal coefficient of the original
   nonclosed projection.

3. **One common cone error.** The ladder supplies `dX=q^3 S` and
   `dE=S-q W_h`. After the first q/twist identity, the q-cubed,
   total-weight-sixteen coefficient of the projection difference is the
   weight-four cone coefficient of `R_4(S)`. The second identity makes this
   the same as the cone coefficient of `R_4(dE)`. Thus (N9) and (N10)
   have exactly the same right-hand side, including its sign. This requires
   regular local operators and the fixed harmonic convention, both stated.
   No primitive has to be reconstructed to compute this comparison.

4. **The lower scalar Q is unchanged.** The third q/twist identity and
   `dJ4=q^4 W_h` give `P_B(J4)-P_A(J4)=q^4 R_2(W_h)` in the aligned frame.
   Consequently the leading and lower normal coefficients used in PR815
   (12) agree. Using the same `Q` in (N12) is therefore justified, not an
   unproved assumption about the projection of a nonclosed cochain.

5. **Mixed sign and regular equivalence.** Subtraction of (N12) is

       rho_AB-rho_AA = -A0 (Lambda_B(T)-Lambda_A(T))
                    = -A0 eta.

   Therefore the compensating sign is **plus** `A0 eta`. PR815 (16)-(17)
   explicitly provide the relevant integral binary-coefficient setting and
   injectivity of multiplication by the fixed nonzero `A0=a^3 h`.
   Equation (N13) is valid as a sheaf/regular-section assertion even at the
   source divisor. It would be false as an unrestricted fiberwise
   cancellation assertion at a fiber where that multiplier vanishes. The
   note explicitly avoids that mistake.

6. **Response-domain distinction.** `R_4` is defined on all local degree-one
   maps, whereas `Lambda` is only certified on the image of the differential
   of global degree-zero cochains. Evaluating `R_4(S)` on the cone is valid;
   evaluating `Lambda(S)` need not be. The retained corrected input
   `T=S-q W_h` is necessary, and the note correctly keeps it.

## Gluing and the precise dimension claim

The transition identity `A0_i theta_ij=lambda_ij A0_j` and the correctly
paired scalar's globality imply (N14) directly. Injectivity of `A0` on each
overlap proves both directions: the mixed scalar glues if and only if its
local defects `eta_i` form a global section of `T_trace`. This is distinct
from the section being zero.

The supplied PR815 sequence is

    0 -> U O_L(-1) -> E_weight4(4) -> Sym^12 U O_L -> 0.

On `L=P^1`, the vanishing of both `H^0` and `H^1` of `U O_L(-1)` makes
the induced map on global sections an isomorphism. Thus every global
`eta` has exactly one global lift `v`. Replacing the affine coefficient
`e` by `e-v` preserves its affine transport: the homogeneous difference
`v` obeys the linear transition `G`. The square datum changes by
`-A0 tau(v)=-A0 eta`, with no change in the fixed lower data.

Since `dim Sym^12 U=13` and multiplication by `A0` is injective, these are
exactly thirteen independent scalar-error directions in this reconstruction
problem. They are not thirteen parameters of genuine contraction changes,
actual ambient adjoints, source solutions, or fourth/fifth values. The
scope restrictions in Section 4 are sufficient and important. In particular,
no contradiction arises with ambient `H^0(B(4))=0`: a global coefficient
section is not automatically an ambient global adjoint.

## Additional checked calibration corollary, now included as (N15)

There is a sharper consequence of the same restricted gluing calculation.
Assume the mixed scalar has already been proved to glue. Let `x` be any
base point at which `A0_x` is a nonzero binary form, and compare the **full
binary coefficient vectors** of the two scalar sections at that fiber.
Then

    rho_AB|_x = rho_AA|_x  if and only if  rho_AB = rho_AA globally.

Indeed, gluing has already made `eta` a global section of
`Sym^12 U O_L`. Its evaluation at a base point is injective (an isomorphism
over a rational point, or injective after extending scalars). Multiplication
by the nonzero binary polynomial `A0_x` is injective on the fiber's binary
polynomial space. Fiber equality therefore forces `eta(x)=0`, hence
`eta=0`, and (N1) finishes the argument. The converse is immediate.

This is only a symbolic calibration criterion. No point or HM coefficient
has been selected or evaluated here. A single scalar value at one binary
argument is not enough; neither is a fiber on which `A0_x` is zero. Without
the prior gluing check, one fiber cannot control unrelated local defects.

## Limits of this review

The actual physical contractions, marking maps, source rows, and values
remain unconstructed. This review does not upgrade generic free-word tests
into authentication of the actual source interface. It also does not repeat
or replace the previously supplied factorization or abstract nonclosed-transfer
formalization.

## Verifier inspection and independent replay

The later supplied `verify_normalization_coupling.py` was read in full and
independently executed with the standard-library-only commands
`python verify_normalization_coupling.py` and
`python -O verify_normalization_coupling.py`. Its reviewed final SHA-256 is
`8a627c8247fa766fcb2e4a91b99ed6add016523567403f8fc65a0aff367199ca`.
Both runs exit successfully, reporting **115 exact q-adic free-word identities
and 16 negative mutation tests**. An initial accounting issue has been
resolved: the runtime guard now runs separately from the algebraic counter.

The script supports the new coupled-error calculation rather than proving
all of its geometric premises. Its exact limits are:

- The three formal contractions have the same ambient cohomology frame,
  so `g=1` is checked within this model; nontrivial frame alignment still
  rests on the written transported identity and authenticated actual maps.
- The common polynomial operator has built-in central-q linearity. Physical
  tensor/twist compatibility for independently supplied maps is not
  certified by running this fixture.
- The source is constructed from free cochains `E,F` with `W=dF`. This is a
  valid exact-tail test family, not a claim that the actual HM `W_h` has that
  form or that every geometric instance has been represented.
- Formal cyclic trace uses an independent symbol `N` and records `tr(N)=0`;
  it supplies no actual `n8`, weight extraction, or HM nonvanishing example.
- The regular sheaf cancellation, affine gluing, thirteen-dimensional
  cohomology argument, and (N15) remain written mathematical deductions,
  not facts certified by this q-adic test script.

These limits are compatible with the final proof's diagnostic-only label.
