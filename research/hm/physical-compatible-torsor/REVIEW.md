# Independent final-byte review

2026-10-23. Verdict: **PASS**, conditional on the explicitly pinned geometric
inputs, for exactly these candidate bytes:

- `PROOF.md`: SHA256 `ba6c3b70f54275292b3324960f2698f9cab807d87c65bd02048fcb4738152ffd`.
- `verify_compatible_torsor.py`: SHA256 `b84d58cc3565a473ce038e45e9052b5ffe9f4a9eb473172108edefdde98c2880`.
- `README.md`: SHA256 `33b573f55728054ba5a287880e9667b7b50bd3ce5c28c009e918cb6f6413c616`.
- `SOURCE-MANIFEST.json`: SHA256 `e1b7284e6b5b945e7e62196a75bc725bba40171429db578ecf54b113d01466fe`.

The proof and checker were independently read in full. All seven input copies
were read and independently checked against `SOURCE-MANIFEST.json` for byte
length, SHA256, and the Git object hash `SHA1("blob " + length + NUL + bytes)`.
All matched. The README was also read in full and accurately summarizes the
same three linked results and stopping boundaries. No candidate or input file
was changed. This review does not
re-prove the upstream geometric theorems or certify actual HM numerical data.

## Mathematical checks

1. **Actual boundary and signs.** With `DeltaW=W1-W0` and `DeltaE=E0-E1`,
   the exact equations give `d DeltaE=q DeltaW` and
   `J4_1-J4_0=q^3 DeltaE`. The actual restriction sequence and ambient
   `H0(B(4))=0` identify the induced cone section uniquely with the kernel
   class by the stated positive boundary convention. The pinned cone closure
   identifies the positive section as `k=gN`; the older spinor note alone is
   correctly not used to assert that closure.

2. **Representative independence.** Adding `dY` to `DeltaW` can be matched
   by adding `qY` to its primitive. The cone section does not change. A
   closed global twist-four change has zero induced ambient adjoint, so also
   zero cone adjoint. This is independence of the induced section, not
   literal equality or uniqueness of degree-zero cochains.

3. **Actual coefficient vanishing.** Section 3.2 of the pinned `next_weight`
   source states and proves the vanishing of the marked weight-four
   coefficient for every actual global section of `B_Q(4)`, retaining the
   transition gap and conic regularity. Hence its use for both positive
   kernel constituents is justified. The argument does not manufacture an
   equivariant physical contraction from a character calculation.

4. **Lower-weight and affine terms.** On `4Q`, the difference is exactly
   `q^3 k`. In the pinned frames `N=n8` and the positive quadratic scalar
   has weights zero and four, giving total shift weights twenty and
   twenty-four. Thus neither the weight-twelve leading ladder nor the
   weight-sixteen layer changes. The fixed lower cochain and contraction
   keep `y`, `s`, `r`, and the full affine term `Q_i` fixed, including the
   actual first-normal transition contribution.

5. **Whole norm, only on the stated neighborhood.** Trace cyclicity gives
   the cross term `q^3 tr(J4_0|Q k)`. Substitution of `a^3 h N` and `gN`
   kills it by `N^2=0`; the quadratic variation has normal order six.
   Off-cone terms start at order four and vanish only because the equality
   is on `4Q`. The Cartier ideal inclusion identifies its order-three
   scalar coefficient faithfully, proving equality of the whole `rho` on
   `Q`. The displayed order-four cross term is genuinely uncontrolled.

6. **Source domain and quotient.** For `T=dE=qW`, torsion-freeness of the
   full cochain terms gives `dW=0`, and `E|Q` induces an actual global cone
   adjoint. The same global coefficient theorem therefore kills the full
   physical weight-four extraction and its trace. Its use here is valid
   without a positivity assumption. Restriction of global degree-one
   cochains has kernel exactly `q C^1_2` by left exactness. Hence the row
   descends on precisely `res_Q(d C^0_4)`, with no extension to arbitrary
   ambient sources. Applying it to `res_Q(S)` after compatibility has been
   certified is not an application of `Lambda` to `S`.

7. **Remaining gates.** The 27-dimensional supplied-source membership
   certificate remains necessary. The thirteen associated-graded
   normalization directions are not actual global cone sections merely
   because they glue, so the zero actual coefficient map does not remove
   the mixed-contraction normalization issue. No fifth-boundary value,
   ambient norm invariance, physical response matrix, calibration,
   primitive construction, or original proof repair is claimed.

## Independent check of the section-versus-norm distinction

The compatible freedom does not disappear as an actual section freedom.
The Cartier sequence gives an injection

`H0(B_Q(4)) --q^3--> H0(B_(4Q)(10))`.

Composing with the boundary inverse shows that

`K -> H0(B_(4Q)(10)),  [DeltaW] -> q^3 delta_q^-1([DeltaW])`

is injective. Therefore a nonzero compatible positive cohomology difference
changes the actual `J4` section, even though its full norm on `4Q` and its
whole `rho` on `Q` remain unchanged. Applying `Hom_G(R,-)` retains this
injection on the seven-dimensional family space. This distinguishes the
proved norm invariance from the false assertion that all compatible lifts
are the same section, and independently explains the checker's corresponding
negative control.

## Reproduction and checker scope

Independently replayed:

`python verify_compatible_torsor.py`

`python -O verify_compatible_torsor.py`

Both completed with:

`PASS: 66 exact q-adic/character/weight checks; 8 negative controls`

The checker uses exact rational and quadratic-character arithmetic, formal
noncommuting trace words, and explicit comparison functions that remain active
under `-O`. Its two sign cases, complete quadratic norm identity, order-four
negative controls, lower-square-condition control, representative changes,
weights, and physical twists agree with the written argument. The nilpotence
reduction is used only for length-two trace words, as documented. It does not
prove the actual cone closure or global coefficient theorem, and it does not
evaluate any actual HM source, coefficient, point, matrix, or rank.

No mathematical or reproducibility defect was found within this bounded
theorem and diagnostic scope. This is an independent written review, not a
Lean or other proof-assistant certificate.
