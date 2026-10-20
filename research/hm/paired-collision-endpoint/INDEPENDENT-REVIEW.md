# Independent mathematical review: order-six paired endpoint

## Verdict and exact editions

**PASS as an exact cohomological reduction. No blocking finding.**

This review binds:

- Endpoint `PROOF.md`, SHA-256
  `4ed13b7412e21665d2e102c9dbece152c47e962e3913596f5f0475e4187a7453`.
- Its filtration dependency `../paired-collision-filtration/PROOF.md`,
  SHA-256
  `41fd8967a1bd876c0375ab35c889d3eec431e5a72cd66ca2fa74937e503cbca1`.

Both files were read in full and independently checked on 20 October 2026.
The accompanying filtration review records the global geometric checks.
This verdict depends on that exact filtered subsheaf identity, not merely
on the abstract unrestricted bundle decomposition.

The endpoint's initially reviewed SHA-256 was
`40a00587cef040a977f4b89b28d066aca3912eae933a84faee69edce27e67dcf`.
The final diff was inspected: its only changes replace the two relative
predecessor links with the immutable published proof URL and record that
proof's commit, Git blob, and SHA-256. No mathematical statement or map
changed. An independent public fetch of the predecessor at commit
`50e82ed233cd7729c38608194f990376eb832418` returned Git blob
`9697423e880070cdf34cbc3548f5a2b32b2a40a0`; its complete text matched the
reviewed local proof exactly, with the SHA-256 above. The PASS verdict
therefore binds the final endpoint edition stated here.

## Independent endpoint calculation

At k=6 the three coefficient ideals are K₅, K₄, K₃ with coefficient
shifts −3, −4, −5. Their explicit resolutions have:

- K₅=(u³,uv,v²): generator degrees (6,5,6), adjacent syzygy
  degrees (9,8), with columns (v,−u²,0) and (0,v,−u).
- K₄=(u²,uv,v²): generator degrees (4,5,6), adjacent syzygy
  degrees (7,8), with columns (v,−u,0) and (0,v,−u).
- K₃=(v,u²): generator degrees (3,4), syzygy degree 7,
  with column (u²,−v).

All compositions with the generator rows are zero. These are the
adjacent-monomial resolutions supplied by PR158, so their exactness
persists globally by the cited flatness argument, including at
quadruple roots.

For the K₃ summand the dual controlling groups are H²B₀(3),
H²B₀(4), and H¹B₀(7); all vanish by PR167.

For the K₄ summand, the generator H² groups have dual twists 3,4,5
and vanish. Thus its H² is exactly the kernel of the map from syzygy
H³ to generator H³. Serre duality identifies its dual with the
cokernel of the transposed multiplication map. The target is
H¹B₀(6)⊕H¹B₀(7); the second summand vanishes. The surviving
map is (a,b,c)↦va−ub from twists 3,4,5.

For the K₅ summand, the generator H² groups have dual twists 4,3,4
and vanish. Its corresponding target is H¹B₀(7)⊕H¹B₀(6).
The first summand vanishes, leaving (a,b,c)↦vb−uc.

Consequently the two surviving cokernels are both

    Q = H¹B₀(6) / (u H¹B₀(4) + v H¹B₀(3)),

and the third summand is zero. This verifies
H²(Z,I⁶E)_χ^∨ ≅ Q⊕Q, with the stated fixed weight-line factors.
The incoming images are essential; the answer is not two bare copies
of H¹B₀(6). Naturality of Serre duality justifies retaining the
transpose maps, not only their dimensions.

## Dependencies and scope

The exact public dependencies were checked:

- PR158 all-powers proof at
  `aab61d34a84c9b8b5a908606a7beb7212d45fe7c`,
  blob `cea0e8cf665c2800bc141759e97921ec71277032`.
- PR167 sharp regularity at
  `063da90fc4543304e87e701cdefcc08225412f17`,
  blob `58785a8799c43fd2c7da089d0ddc5e05822132a9`.

PR167 leaves H¹B₀(6) undetermined and proves the upper bound 30;
therefore the manuscript's bound h²(Z,I⁶E)_χ≤60 is valid, but
neither equality nor positivity follows.

The prior sixth-power full-sign proof, blob
`8838faef24065d5e0bab027163e51b6a34faabee`, concerns a different
coefficient B₀(−4)K₃. PR171's socle-syzygy detector at
`8236d128910c667610361966011456aa9478747f`, blob
`d450a7e58e0abd39bc0ba88223f2df22b2d4e674`, uses different
coordinate-Koszul transgressions and a different quotient. The
present endpoint does not silently identify either with its Q.

The claimed equivalence is only between whole order-six coefficient
vanishing and surjectivity of (u,v) onto H¹B₀(6). A nonzero Q would
not establish a nonzero image in unrestricted H²(E), failure of
restriction injectivity, or a nonzero actual source class. Conversely,
the present calculation does not prove the map surjective and does
not lower the sufficient order to six.

No actual HM multiplication, source, generator, or checker was
executed. No external state was changed. This is an independent
mathematical review, not formal machine verification.
