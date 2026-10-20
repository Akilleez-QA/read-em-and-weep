# Independent review of the legacy-volume comparison

## Exact edition and verdict

This review binds the following UTF-8 files by SHA256:

- `PROOF.md`: `2a04ce7247f2273aa92e4df4a040c571be1b6cf31d1bd7a09e6f47657e763039`
- `SOURCES.md`: `e644414d7e8b98be3469243fb50a3fd8aa19c5abea4c816cf12a77d2ca0decae`

**Verdict: pass within the expressly retained source hypotheses.** The
argument identifies the specified legacy map with natural root-deck
descent in canonical-form coefficients. It correctly distinguishes this
map from its quarter-normalization and preserves the boundary and
binary-volume qualifications. No mathematical correction is required
for this edition.

## Independent checks

1. **Source and frame normalization.** Static reading of the pinned
   generator confirms the seven kinetic terms, three gerbe terms, left
   adjugate normalization, and absence of a subsequent common descent
   divisor. The source dictionary retains the nonzero logarithmic frame
   jets. Under the draft's stated constant row-frame convention, the
   endpoint transformations give exactly
   `M' = S_i^{-1} M S_i`; undoing this conjugation introduces no scalar.
   Bare arrays are not identified before restoring their frames.

2. **Volume and ramification.** The actual vector field satisfies
   `(dx/y)(V)=1`, fixing both pair volumes. The finite-branch and infinity
   formulas establish regularity and fix the infinity minus sign.
   Multiplying the all-four-odd source by the same-character volume
   produces an invariant top form. Normalized canonical trace then sends
   it to the stripped coefficient times the ordered differential volume,
   with no extra factor two, sixteen, or mixed factorial.

3. **Exact source cover, including (11a).** The two displayed legal opens
   are precisely full inverse images of the indicated opens of
   `P^1`. Intersecting their products with carrier pullbacks remains
   adapted to the degree-sixteen root map. The affineness argument uses
   finite pullback of affine carrier opens and affine intersections in
   the separated variety `Z`; it is valid. Thus the trace in (11) is
   literal on the stated source cover. The separate common-refinement
   discussion does not assume surjectivity of a cochain refinement map
   or permit tracing sections on arbitrary unrelated opens.

4. **Complete raw correction.** PR351 (7.4) supplies
   `R_raw = tf(M) + delta W`, with the same displayed `W`.
   Coefficient trace commutes with the differential and trace-free
   projection. Therefore the draft's descended boundary and class
   formulas follow. Trace removal is retained throughout; the full
   emitted matrix is not silently treated as trace-free.

5. **Ordinary line and binary volume.** The homogeneous form
   `Y dX - X dY` gives `dx` in the finite frame and `-dt` in the infinity
   frame. The frame transition and the sign `(-1)^{|S|}` in (14) agree,
   including partial infinity charts. With `a = c a_std`, the inclusion
   scales by `c^{-1}`, so (17), in particular the normalized coefficient
   `(4c)^{-1} L^0`, is correct. The cited PR387 text does not supply the
   missing explicit equation identifying its chosen volume with (13);
   this review does not set `c=1`.

6. **Imported class comparison and limitations.** The public PR434
   proof has the stated coefficient identity `D_rho j_64 = 4 j_4`.
   Its complete-source, ambient, localization, and marking hypotheses
   remain imports, not conclusions of this note. The present argument
   does not assert literal equality with an independently chosen
   representative, high-ideal membership, a primitive, or a new
   obstruction value or vanishing.

## Method and evidence

The review is a mathematical reread of the exact two files above, checked
against the relevant public source passages listed in `SOURCES.md`:
the legacy generator and source dictionaries, physical frame and chart
arguments, PR351's complete raw identity, PR131's pair marking, PR387's
trace and volume conventions, and PR434's public normalization proof.
The pinned generator was inspected as inert text, including its final
assignment and subsequent mask-coefficient extraction.

No generator, model, checker, source-instance calculation, matrix
evaluation, coefficient evaluation, parameter search, or numerical
experiment was run. SHA256 hashing only binds the reviewed document
bytes; it is not a mathematical or implementation certificate.
