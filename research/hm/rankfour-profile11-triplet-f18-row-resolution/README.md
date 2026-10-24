# The nonzero alternate-triplet row selects the first F18 kernel

This packet proves that the canonical universal quotient gamma is nonzero
on the P component of ordinary multiplication H2 times H16[V_alt]. Equivalently,
the standard complete first-jet map at twist two has a nonzero V_alt row.

The structural proof constructs the universal quadratic syzygy of the
degree-six P system, proves its everywhere second-jet spanning by a degree-12
Wronskian, and excludes stationarity of the resulting degree-eighteen P
product by the exact principal-parts filtration and invariant-divisor degrees.
The determinant-square contraction identifies the required map itself,
not merely a map of the same representation type.

Under the common full-positive triplet, original t=0, original local delta=12,
residual simultaneous rank-seven k=2 and K1 hypotheses of the two complete
direct originals, including all their transitive actual-geometric hypotheses,
this selects

    F18 = D(-2) + (W' + T6)(-3),
    H0(F18(2)) = D,     H1(F18(2)) = 0.

The actual extension 0 -> V_alt(-4) -> E0 -> F18 -> 0 therefore splits
equivariantly as a bundle extension. No horizontal splitting is claimed.
This excludes only the second F18 alternative in the retained common case,
not K1, a whole profile, or any other branch. It neither realizes K1 nor
proves higher-order branch matching or algebraicity.

Exactly two entire direct originals are retained: PR1239 at
360b7e8f55b05ca5740a10cb3ed844a594766f70 and PR1207 at
af136934955f1bcc700ee768e2debb983e75451d. They were freshly fetched through
complete read-only GitHub path and blob calls on 2026-10-24, then read in full.
INPUTS.json records their exact authentication; INPUTS.md and PROVENANCE.md
state the imported assertions and the boundary. Preparatory audits and the
orthogonal-top packet are not direct mathematical dependencies.

Run from this directory:

    python verify.py
    python -O verify.py

The checker uses explicit runtime requirements, not Python assert statements.
It verifies exact complete-file hashes and a fixed, small collection of
character, degree, cohomology-dimension, and integer identities. It performs
no actual HM/source coefficient, point, parameter, matrix, tensor, jet, or
instance-rank evaluation, no broad scan, and no historical enumeration.
It does not prove the theorem or replace independent whole-proof review.

FROZEN.json binds the eight core files. FREEZE-REPORT.md and AUTHOR-REPLAY.json
record author verification; verification/ retains the normal and optimized
outputs. Raw LOCAL-SOURCE-FETCHES.json replies are local evidence only and
are not selected for publication. The author does not publish or merge this
packet. A new reviewer must read this entire frozen proof and both complete
freshly authenticated originals. Earlier review of the preparatory draft
does not count as review of this frozen publication packet.
