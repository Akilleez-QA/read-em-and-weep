# Independent review: P-source maximal profile (1,1) closure

Verdict: PASS for the stated source-conditioned theorem, relative to the explicitly pinned original geometric necessity theorem and prior exclusion inputs. This is not a complete repair or all-source profile closure, and not proof-assistant verification.

## Frozen artifacts reviewed

- PROOF.md SHA256 d3e4714dc5808474ae664824c36a2d81975e29d40a6f2c99309542afdba8713a.
- verify.py SHA256 51f4afb4987e17f237b976f2a8d90d15ecc1117704f73874b9c1ddaf397815eb.
- RESULT.json SHA256 bf1474124d411dc5c417613bcb74932de0214b085551005b587d6c2e00bca997.
- INPUTS.json SHA256 f779997e421debdbdd4802c8a1e3b4bd9994443c3321776207d729f973562ff7.

All eleven immutable public inputs were independently freshly fetched at their full commit IDs. Their exact byte counts, SHA256 and Git blob hashes were recomputed and matched the author's inputs byte for byte. AUTHENTICATION.json preserves provenance. The full original 159-record necessity theorem and JSON were read, not replaced with regenerated candidates. Imported geometry remains an explicit mathematical dependency, not a consequence of matching JSON.

## Mathematical review

The actual source tuple is (1,1,1,0,1,0,0,0), as reconstructed from the original eight-block convention and the four-source theorem. Its rank is17 and degree−54. The two cohomological inequalities follow from E→A and B→E*(-2), respectively; the latter uses equivariant Serre duality and self-duality. They are necessary, not sufficient, and are used only on the frozen overlist.

Independent exact class-character calculations reproduce exactly35 compatible records and all124 incompatible records' full failed-twist witnesses. Cubic visibility removes16. The all-source doublet theorem removes6 and the all-source rank-one-flag theorem removes2. These groups are disjoint and leave precisely11. The prior proofs' endpoint hypotheses apply at k=1 and do not depend on B or determinant defect.

For the remaining group, the dual reversed plateau identifies L=(Q*)^- as the lower endpoint when l=1. Thus its derivative rank is at most2; this is not an illicit rank-three interior bound. The negative saturated bundle L has rank10 and degree−54−deg B. Each successive actual kernel is saturated in the same constant ambient. A nonzero horizontal saturated subbundle would be constant, contradicting negativity, so the flag reaches zero and no positive-rank remainder is suppressed.

The actual derivative induces G_j→G_(j−1)(−2), hence G_j→B(−2j). Thus positive quotient ranks are nonincreasing, at most2, and total10. Their conjugate height pairs are exactly (10,0),(9,1),(8,2),(7,3),(6,4),(5,5). Exterior powers give the stated determinant degree bound without requiring image saturation. Summation gives precisely the two-height formula. Neither a horizontal splitting nor a fixed rank for later derivatives is used.

All six capacities were independently evaluated per record, also by the quotient-rank sum. The maximum capacities in index order130,132,141,142,143,144,145,148,149,150,151 are −110,−110,−110,−110,−114,−70,−120,−120,−125,−70,−125. Actual L degrees exceed them by72,72,74,74,78,34,84,86,91,36,91. In particular the doublet degrees−1 at144 and150 do not evade the bound. The uniform−70 bound alone also suffices.

No defect-zero hypothesis is imposed by the proof or filtering. All original defects are retained; the final eleven happen to have defect zero. The capacity argument applies for arbitrary B with the specified degrees, including nonsaturated derivative images. The full35-member partition therefore closes only this actual P-source profile under the original necessity theorem.

## Reproducible controls

Author verifier replayed in ordinary and optimized Python:839 explicit checks plus81 imported character controls, both outputs byte-identical to the frozen RESULT.json.

Independent checker:4733 explicit checks, ordinary and optimized outputs byte-identical. It uses exact conjugacy-class inner products over Q(sqrt5), with symmetric traces from the closed binomial formula rather than the author's product recurrence. Its character basis is adapted from the earlier independent P-target review; that provenance is declared in character_base.py. It compares all nine irreducible products through degree40 to the separate authored character implementation, recomputes every source decision and failed-twist witness, and checks every capacity and partition member.

Run from this review directory:

    python3 independent_check.py PATH_TO_CLOSURE_PACKET
    python3 -O independent_check.py PATH_TO_CLOSURE_PACKET

The packet argument must point to the directory containing the frozen author INPUTS.json and RESULT.json. The checker reads the retained full original159 list; it does not regenerate that historical classification. Review files are supporting verification, not a new mathematical progress claim.

No actual coefficients, selected parameter points, jets, source instances, matrices, instance ranks, or experiments were evaluated. No external writes were performed. No unresolved mathematical gap was found in this bounded source-conditioned deduction; global transfer and the other source/profile branches remain outside this verdict.
