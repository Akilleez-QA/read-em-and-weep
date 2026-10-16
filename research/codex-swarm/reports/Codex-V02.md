> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-V02 — independent label audit. Reviewer: Codex-V01; review pending.

Authenticated basis: pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js`; sparse rows in GitHub comment #6141530883. Read the pinned source/model and closure notes. No code, arithmetic oracle, or physical-source calculation was run.

**Canonical reconstruction.** Matrix indices are zero-based. Keep each row’s entries in this order:

| q | Chart; exponent | Ordered entries with coefficients |
|---|---|---|
| 2 | CCBB; (−1,−2,−2,−2) | M11[9,3]:1; M11[10,4]:1; M11[12,6]:−2 |
| 3 | CCCB; (−1,−2,−3,−3) | M10[0,3]:1; M10[2,6]:2; M21[10,1]:1; M21[12,5]:2 |
| 4 | CCCC; (−1,−2,−3,−4) | M20[0,0]:−1; M31[10,0]:1 |

For every permutation σ of coordinates 1,…,q, construct staircase vertices t₀,…,t_q: coordinates greater than q stay 1; the first q coordinates start 0 and flip in order σ. Its orientation is sgn(σ). Thus the raw seed coefficient is **row coefficient × sgn(σ)**. Source sorting contributes an additional alternating sign.

Use key `(q,entry,σ,channel)` and local rank  
`r=entry_index·q!+lexrank(σ)`, both indices starting at zero. This gives 6+24+48=78 seeds expanding **one detector** (#6205341120), not 78 independent tests. Keep standard tags as coordinate tuples until the cloud encoding is bound.

**12-way ownership certificate.** V01’s proposed assignment is disjoint and exhaustive on this reconstructed seed/channel domain:

| Owners | Channel | q | Half-open rank intervals |
|---|---|---:|---|
| C01/C02 | E12 | 2 | [0,3), [3,6) |
| C03/C04 | E34 | 2 | [0,3), [3,6) |
| C05/C06 | E12 | 3 | [0,12), [12,24) |
| C07/C08 | E34 | 3 | [0,12), [12,24) |
| C09/C10 | E12 | 4 | [0,24), [24,48) |
| C11/C12 | E34 | 4 | [0,24), [24,48) |

The q2 cut splits the second entry’s two staircases; it does not split by whole rows. These intervals certify 156 ownership cells only.

**Domain and sign controls.** Retain full vertices `(standard,carrier,mask)`. Source order is carrier/mask first, standard last, auxiliary carrier first (#6205660472). Equal carriers alone do not imply alternating zero. Prefix strictness from #6205455951 permits repeated residual-tail carriers; deleted prefix owners and denominator multiplicities persist. For q4, the negative J2 M20 selector cancels its negative terminal-row coefficient: both surviving selector words have positive coefficient before orientation. Applying that minus twice is an error.

**Exact gaps.** No C reports were present at inspection, so no C source-label enumeration is accepted. Cloud numbering, channel/operator binding and seed4’s exact key remain missing. E12 stays preparation-only; seed4’s scan and 704 active primary tuples remain reserved. Once authenticated, transfer that key to a reserved-owner record without reranking. C coverage of the E channels also does not cover the baseline M0⁰+Fq·kp+Fp·kq.

Original progress here is independent reconstruction and roster review; the sparse rows and pruning identities are published dependencies. Next: bind the cloud manifest, then require every full label to have exactly one status—proved zero, unresolved, or reserved—with its source-sorting sign. No exclusion rate or obstruction verdict follows.