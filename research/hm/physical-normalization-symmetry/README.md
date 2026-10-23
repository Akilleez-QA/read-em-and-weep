# Symmetry-certified physical normalization calibration

This is a NEW conditional family theorem beyond the PR866/PR880 scalar
normalization algebra. It keeps U=Wprime, the positive binary representation,
distinct from the negative W.

## Findings

- PR815/866 alone do not certify coherent equivariance of the chosen physical
  contraction packet. Their unrestricted global trace error still has thirteen
  coordinates; finite symmetry does not make a fixed source an invariant vector.
- If global eta is additionally certified G-equivariant, cubic in a and linear
  in h, its universal family space has dimension ten. The invariant output
  vanishes; its universal output span has dimension twelve, V+P4+D5.
- The entire h-family at any one semisimple C5 axis and any one C5-fixed square
  detects all ten family channels. Individually the kernels have dimensions
  four and three. The pair need not be associated.
- The physical norm observation is quadratic in h because its multiplier is
  a^3 h. The proof retains that multiplier and proves the relevant universal
  polynomial multiplication map injective. It never treats the multiplier
  as a single fixed linear observation across sources.

## Scope

No actual contractions are proved equivariant, no physical calibration is
performed, and no actual HM coefficient, point, matrix, source or rank is
selected or evaluated. The actual source image could be smaller; the universal
dimension ten is not a claim about its realized dimension. This does not
exclude a geometric source or repair the original theorem. PR866 is unchanged.

The three counts are distinct: thirteen unconstrained global traces, twelve
possible nontrivial output coordinates under the family gate, and ten
equivariant family parameters. Both observations require the complete h-family,
prior globality, and independently authenticated reference values.

## Reproduce the bounded diagnostic

    python verify_symmetry_calibration.py
    python -O verify_symmetry_calibration.py

Both modes pass 122 exact character/degree/coefficient checks and 5 negative
controls. The checker uses only the standard library and formal character and
polynomial coefficient algebra. It does not establish the geometric orbit or
actual coherent-action premises; those are treated explicitly in PROOF.md.
This is independently reviewed written mathematics, not Lean certification.

## Package

PROOF.md and REVIEW.md contain the deduction and independent review.
SOURCE-MANIFEST.json pins six exact source files in inputs/.
verification.log and verification-optimized.log record direct replay.
FINAL-MANIFEST.json and SHA256SUMS bind final bytes.
