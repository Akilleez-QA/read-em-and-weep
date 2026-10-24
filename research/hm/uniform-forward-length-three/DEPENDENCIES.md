# Exact import ledger and shorter dependency bridge

## Direct foundational imports

The theorem is conditional on the original actual geometry. The four files
in INPUTS.json are exact public originals at commit
`db51525015bb7c5e825833d550d08dedf6f6ea96`, under
`research/hm/order-four-quadratic-load/`. Their full text is retained in
`sources/`; retaining a document does not import every theorem inside it.

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, Section 1:
   the actual E and Q* presentations, the fixed physical module marking,
   ranks/degrees, no-constant and full-span premises. The standard
   equivariant splitting argument in Section 2 is reproved briefly here;
   the section-persistence argument in Section 4 is also reproved. The
   Section 3 enumeration of 28 sources and its conclusions are not used.
2. `POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md`: the actual saturated
   inclusion in the original constant rank-30 plane-section space and
   its trivial-connection interpretation. Neither the positive-square
   numerical consequence nor any global rank bound is imported or
   asserted by this packet.
3. `TWIST-ONE-ACTUAL-SECTION-KERNEL-VANISHING.md`: the global actual
   vanishing H0(E(1))=0, with its original geometric hypotheses retained.
   This is not inferred from the character certificate alone.
4. `GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md`, Section 1 only: orbit
   sizes 12,20,30,60 and the invariant-divisor minimum twelve. The short
   proof is recalled in PROOF.md. Its rank-two profile, endpoint-flag,
   and semigroup-exhaustion conclusions are not imported.

The original physical construction, hyperplane cohomology and actual
embedding prerequisites of these inputs remain premises. This packet is
not an independent reproof of all transitive ancestors. Conversely, no
historical splitting or quotient-list necessity theorem is a premise of
the new four-shape argument.

## What is proved here

PROOF.md derives, under those inputs and the actual maximal rank-three
plateau hypothesis:

- the section-length bound and unique l=3 source without the 28-source
  recursion;
- a full derivative-image saturation, not a restricted cubic-image
  saturation, of one of exactly four necessary shapes;
- the dual envelope for every k>=1, including the lower endpoint at k=1;
- saturation by a strictly sub-twelve determinant defect;
- a top-V multiplicity contradiction for all four shapes, without
  classifying the lower tail of the rank-fourteen kernel.

The fourth necessary saturation retained relative to the old terminal
route is W' O + O(15). It has exact quotient W' O(-3)+O(12),
chi(K(4))=2V+P, and the same one-dimensional target Hom obstruction.
Thus no positive-Q* high-degree target filter is needed to discard it.

## Exact replacement in the existing combination

The already published [nine-profile combination, Section 5](https://github.com/Akilleez-QA/read-em-and-weep/blob/89def56cc66f96d8dc240a7298b281a22e5670dd/research/hm/nine-profile-rank-bound/PROOF.md)
uses distinct routes for the three entries with l=3:

- (1,3): `EXTREMAL-13-FULL-SATURATION-EXCLUDES-THE-PROFILE.md`, with
  the three-exact-quotients and cubic-image-exclusion inputs. The old
  route first removes O(15) by high-degree Q* target eligibility and
  classifies the remaining negative kernel tails.
- (2,3): `ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md`,
  Sections 2-4, with the 37-dual-type necessity split into nonzero
  quadratic-evaluation and zero-quadratic branches.
- (3,3): `EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md`, with its
  five-dual-splitting/cubic-pairing route.

These old routes are located at the same immutable source commit and
path root as the foundational files. They are comparison references, not
inputs needed by PROOF.md. This single theorem can replace those three
entries after integration review. It does not modify the existing
combination certificate, remove its other six dependencies, or establish
a new global rank conclusion. No extra case is counted as newly excluded.

PR #1172's direct (2,2) cover and PR #1182's direct (1,1) closure are
separate dependency reductions. Rank-four work is outside this slice.
