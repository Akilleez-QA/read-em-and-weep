# Exact source pins and bounded dependency contract

## Mathematical premises

The byte-identical supplied input is dependencies/RESULT.md:
SHA256 2b07d868ec9c1fc5e38503623a8556ff7b3c71e3df76c3550385560602584db5.

Precise pins (1-based lines in this snapshot):
- Lines 17–27: fixed physical frame, commuting derivations, normalized determinant-one L/U currents and symmetric H/J jets with literal moving A transport.
- Lines 34–39: equation (3), the two full physical derivative formulas, including the moving-transport contribution.
- Lines 60–67: exact four-entry sign convention and the a/b scalar coefficients.
- Lines 86–94: entire equation (8), defining M2.
- Lines 114–116: rank-two nested-bracket reduction.
- Lines 129–131: universal scalar-coordinate invariant form.
- Lines 164–191: inherited full nonconstant kernel warning; this packet does not recompute any kernel or prove weighted exactness.

The copied independent review is dependencies/REVIEW.md:
SHA256 ea986247cc484155f86fc2b016fc88477a85e74f7a7e094d2ff6680652e0afaf.
Its physical derivative discussion is corroborative background. The new audit derives the needed product-rule identities itself. The historical input hash list dependencies/INPUT-SHA256SUMS has machine-local directory prefixes removed and is provenance context only; its earlier files are not claimed to be bundled, freshly authenticated, or independently revalidated here.

## Author certificate pins

The author proof is dependencies/author-RESULT.md, with its machine-local input path replaced by a relative source label:
Bundled SHA256 dfcfd7882e546a423f4607920d1625d06eb71c2bcad33768d5033c70ddd980ad.
Original pre-sanitization SHA256 d4390b4efef711dbb6a39badc9d370ad78d0a1a38798e0cb4b0b128d75ea8692 (historical provenance only; the original bytes are not bundled).

The supplied certificate.json is unchanged:
SHA256 bed968ee298ec44da1373f118450e38a53a3c3a0e681e7f71a7712e4e0ec7784.

The original solver had SHA256 5c1ff8cc4f4566ffa8195cbc104809ceac42ed9b2108d3a73e866b9cfe4b388a. Bundled solve.py differs only by importing pathlib.Path and resolving its certificate output beside the script instead of using an absolute working-machine path. RESULT.md has corresponding portable references and an audit-scope appendix. See SHA256SUMS for exact bundled bytes.

## Bounded dependence

The new theorem is an implication from the displayed derivative and M2 formulas, free symmetric traceless second jets, and rank-two invariant identities. It does not require re-proving the earlier S2 transgression, the source origin of M2, Q4 reduction, extraction, HPL, owner-domain or global residue premises. Those earlier claims remain conditional context. Any claim that this formal route exclusion applies to a particular physical target additionally requires the earlier source-to-formula premises; those are not independently authenticated by this packet. The reported remote commit/PR identifiers in the supplied snapshot are historical context, not newly verified source pins.

The independent checker has no imported helper dependencies: Python standard library only, and certificate.json. It creates no matrices, evaluates no physical data, and performs no external I/O. The author solver writes only its colocated certificate. Run audit_check.py for a read-only verification.
