# Independent review: pure-V conic base scheme

Result: PASS, with no mathematical blocker found.

Reviewed the complete PROOF.md, verify.py, INPUTS.json, both retained input
proofs, and the older FOURTH-SQUARE-CHANNELS-HAVE-A-C5-DETECTION-FILTRATION.md.

## Mathematical audit

- A nonzero restricted gate embeds the irreducible P into binary degree
  eighteen. The gcd of its component space spans a stable line. Perfectness
  of the binary icosahedral group eliminates all nontrivial characters,
  including any possible odd-degree semi-invariant. The displayed even
  binary recurrence and central parity therefore exhaust allowable gcds.
- The recurrence is the character identity for Sym^(2m) W, with multiplier
  char(Sym^2 W)-1. It is not the recurrence for plane symmetric powers.
  The invariant and P multiplicities in the proof are correct.
- The unique degree-twelve invariant has a reduced zero divisor: every
  nonempty orbit on the binary projective line has size at least twelve,
  and the unique twelve-point orbit is the order-five fixed-point orbit.
  A residual degree-six P system cannot have a common zero. Thus the
  exceptional restricted ideal is exactly (f12), not merely supported
  on its divisor. All other nonzero systems have unit local ideal.
- The published restriction isomorphism identifies a unique global gate
  line. Restricting the component ideal gives the scheme-theoretic
  intersection with the conic. The argument does not determine transverse
  surface multiplicity and the proof explicitly preserves that boundary.
- Near the conic, j is an isomorphism and L is a split surjection locally.
  The component ideals of s and -j s L consequently agree there. This
  justifies the correspondence with the older fourth C5-invisible line.
  It identifies neither of the plane-axis jet lines and selects no actual
  gate coefficient.

## Provenance and novelty

Fresh direct GitHub reads at the two declared commits returned exactly:

- 2793b3dcca821d9f3b90c3d3e02309d33639288a,
  research/hm/source2-pure-v-square-restriction/PROOF.md,
  blob 5cdcf96267a623959737e25cfc6be24cf13df590.
- 418a7d9ebedaae9b5d00db9f69e449b5d8767108,
  research/hm/source2-pure-v-nonic-base/PROOF.md,
  blob aec4e3f550d3dc4bedb2911019de65e61852c436.

These match the retained files and manifest. The first input supplies the
exact restriction isomorphism; the second supplies the finite ambient base
scheme. The old fourth filtration already contains its own distinguished
binary degree-twenty D line and off-orbit detection statement. Those are
not new. The present packet adds the full degree-eighteen P gcd dichotomy,
its unique lift to the conditional pure-V gate, and its exact conic
intersection scheme. Its novelty statement is appropriately bounded.

## Reproduction and frozen bytes

Independently ran python verify.py and python -O verify.py. Both passed
16 checks, produced byte-identical output, and agreed with RESULT.json.
The checker supports exact character arithmetic and dependency integrity;
the written arguments supply the group, divisor, and sheaf geometry.

SHA256:

- PROOF.md: c5c00f73f82e2e47803b7ca71bb1953dcacf9ca015f15ca8c4dc7ccea8c90f5c
- verify.py: 2e865c421cf5771064de98bfd91c32b350fc050bbb794c9e8151344c6a50c3f5
- INPUTS.json: 75fbc0eed3a827033328d7af050d060a7da57e19f86feb201133fd923fa5412a
- RESULT.json: 73286a78e1854260ef05262734c07b5b0783bf7382b1a1cc5ef4c7b370ff102b

No actual HM coefficient, selected parameter, source instance, or matrix
rank was evaluated. No public files were changed.
