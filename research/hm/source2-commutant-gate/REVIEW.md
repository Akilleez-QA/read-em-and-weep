# Review record for the source2 commutant gate

Verdict: PASS as a conditional written preparation theorem, retaining
PR790's actual-source hypotheses and simultaneous fixed-tensor
identification. No actual HM tensor evaluation or source2 exclusion is
certified. This is not proof-assistant verification.

## Final bytes and separate reviews

The final files reviewed are:

    PROOF.md
    316ef592bc74f29de4698e740b90ad760ef7ad6cc09777ae3d913fc69043a5d2
    SPEC.md
    c5233fc4c4c858ebb6eab7362af21b45c6dd787618f6f63440ce3a86ce91b332

A separate native reviewer read all lines of these final files and the
relevant pinned dependency sections. Its retained SOURCE2-REVIEW.md has
SHA-256 152c21bbc06ed29a8ce85eb307358ac8fc2c8de7cdef128d32a1e93a1262172b.
It found no blocking mathematical or certificate-contract defect.

A separate Codex CLI worker independently reviewed the same PROOF.md and
an earlier SPEC.md with SHA-256
33c82786ca6a8e1533121b0d3e11c801d43da42efc9038670c8051d9c4cdeded.
Its retained gate-cli-review.md has SHA-256
81ef2ff7fe21e6473fe893fb560b335bb3561277c37c4d77f0b01020c5880e73.
It found no mathematical must-fix and conditionally accepted the proof,
while flagging a dependency-copy hash discrepancy reconciled below.

The CLI worker did not audit the final SPEC bytes. The final delta was
checked by reconstructing the earlier SPEC and matching its exact hash:
it only clarifies that isotypic coordinates require a splitting field,
that a raw-matrix alternative must independently authenticate complete
End_G bases, and the closing statement that no actual tensor package is
supplied. The separate native reviewer explicitly read and accepted that
final clarification. No PROOF.md change followed either audit.

## Mathematical checks

Both independent reviews confirmed all of the following:

- Complete endomorphism dimensions 30+54+29=113, retaining every repeated
  irreducible channel, and complete equivariant equation dimensions
  78+75=153 using both fixed pencil variables.
- The reconstruction dimensions (9,18,16), (15,18,12), (17,18,9) and their
  use as the actual diagonal scalar-action blocks of PR791. This does not
  infer an action from an abstract algebra isomorphism alone.
- The trace determinant 180 in the zero-coupling class and the nonzero
  minor -252 in the coupled class. The full radical is square-zero, so
  its vertex traces vanish; injectivity on the semisimple quotient gives
  precisely the radical as the common trace kernel.
- Ordinary traces weighted by irreducible dimensions, the opposite-algebra
  orientation, the 156-by-113 augmented matrix of necessary rank 111, and
  the unaugmented necessary ranks 108 and 109.
- Exact-field and certificate requirements, including the one-sided
  meaning of modular nonzero minors and the need for exact identities
  and independence for upper-rank witnesses. Passing the necessary ranks
  is not a realization theorem.

A separate elementary arithmetic replay confirmed the displayed
dimension counts, trace determinants, and 8424 uncompressed scalar
equations. It used universal character multiplicities only; no actual
source coefficient or tensor was evaluated.

## Published dependency digests and reconciliation

The immutable commit/path links are in PROOF.md Section 1. The fetched
proof bytes were compared with these published SHA-256 digests:

| Input | Published proof SHA-256 |
| --- | --- |
| PR788 at 941b7b3b77dc8ae8a19b1e000dddeb0438d05db7 | 81bb2d40705fa1e35f5719ef59323cd60af675ebe74015651dda9590a2488f29 |
| PR789 at 2d1642ad40ae1111b84b50eeaca0426bfbfbb314 | 7eb626caae70e62613e8a3e318ac4c6a858502c4fdecfb44a6693e3ed85635c3 |
| PR790 at af0e03d26da5e47d18ae732291aca46f4d448dc5 | 0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4 |
| PR791 at 2cd033a4a5ba549d07330427cd779364cb83c0fb | 8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290 |
| PR795 at 3f811311d76914a555c7e7d0c5b887b41805aa6c | 27a8802a004cb659e1b33cae9aabaca1e8188b1382d8477cac2bb31264c40937 |

At the CLI audit, each local source copy had one extra terminal LF added
when materializing the fetched text. The CLI correctly reported different
hashes for its supplied PR790, PR791 and PR795 copies. Post-audit, removing
exactly that final byte from each local copy produced the published digest
above; no mathematical content was changed. The native reviewer separately
confirmed the same one-byte comparison. The corrected copies were then
hashed again and matched all five listed digests. The unchanged CLI report
is retained with its original concern, rather than rewritten as if it had
reviewed the corrected bytes.

The audits check this new deduction and its immediate pinned interfaces.
They do not independently re-prove the earlier PR744/751/758 geometry,
the complete HM foundation, or the existence of authenticated actual
tensor arrays. Those remain explicit external inputs to any future run.
