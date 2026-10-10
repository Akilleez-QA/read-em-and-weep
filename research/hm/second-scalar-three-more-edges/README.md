# Three more exact partial contributions for the second scalar map

This small package extends [PR #43](https://github.com/Akilleez-QA/read-em-and-weep/pull/43)'s single-edge evidence without rerunning that edge or changing its package. Coordination and ownership remain in [PR #1](https://github.com/Akilleez-QA/read-em-and-weep/pull/1).

For `L_minus(X) = X02[0,5] - X13[10,1]`, coefficient field Q and pairing monomial `m = (2,2,2,0)`, the supplied quotients give:

| Orientation | Signed contribution | Full quotient terms | Selector rows | Nonzero selected coefficients |
| --- | ---: | ---: | ---: | ---: |
| 0132 | -2817/16 | 203 | 189 | 16 |
| 0213 | 18831/8 | 233 | 207 | 24 |
| 0231 | -21601/8 | 233 | 189 | 16 |

These are three oriented contributions, not the scalar pairing. Together with the separately published 0123 contribution `8655/16`, they cover four of the eighteen required orientations. The fourteen other orientations are neither supplied nor assigned zero here. Cancellation remains possible. No scalar-class value, full-obstruction value, vanishing/nonvanishing conclusion or theorem repair is claimed.

## Replay

Python 3.10+ standard library only, from the repository root:

```sh
python3 research/hm/second-scalar-three-more-edges/replay.py
python3 -m unittest discover -s research/hm/second-scalar-three-more-edges -p 'test_replay.py' -v
python3 -O research/hm/second-scalar-three-more-edges/replay.py
```

The checker verifies all 669 supplied quotient terms and independently derives all 585 selector rows, signs, physical exponents, integer weights and exact rational contributions. No process spawning, numerical DAG evaluation, pickle loading or checkpoint mutation occurs. Checks remain active under optimized Python. The tests include an independent positive-power kernel identity and corruption controls for orientation, sign, grading, bounds, coefficient arrays, selector rows, rational encodings, scope and package integrity.

## Exact extraction formula

Write roles as `(i,j,k,l)` and set `d=6+m_j`, `L=22-m_l`, `w=35+sum(m)=41`. The full quotient is retained modulo `(U^9,V^44,B^23)` with common denominator 64 and homogeneous degrees separated. For `0 <= r <= d`, `0 <= ell <= L`, read quotient slot `(r,w,ell)`, assigning its absent coefficient zero within the **supplied full quotient**, and multiply by

`[T^(d-r) z^(L-ell)] G(T,z)^(-70)`,

where `G=1+z+T+3Tz+Tz^2+T^2z+T^2z^2`. The replay derives the kernel using the finite binomial expansion of `(1+H)^(-70)` in `Z[T,z]/(T^9,z^23)`. It independently derives physical source exponents in role order as `(272, 215-r, 157-sum(m)+r-ell, 47+ell)`, whose sum is 685, then applies the permutation sign. It uses the fresh second-map support enclosures 47/215/454 and 9×44×23 window; it does not reuse the original scalar's narrower bounds or zero list.

## Provenance and evidence boundary

`contributions.json` contains all full quotient terms and all selector rows for the three orientations. Values and rows were compared to existing independent completion receipts, whose original hashes are recorded alongside original quotient, edge-result, configuration, execution-plan and terminal-checkpoint hashes. At packaging, every artifact hash named by those receipts was checked against the corresponding existing artifact. The receipts record exact terminal-factor reconstruction in both integer and rational arithmetic, archive/frontier bookkeeping checks, and zero source DAG nodes reevaluated. Those historical records are provenance anchors, not public regeneration evidence: large checkpoints, source DAGs and the original receipts are not distributed in this package.

A fresh run of this package replays **supplied quotients and selectors only**. It does not independently reconstruct terminal checkpoints, reevaluate the source DAG, or establish the full source-to-edge geometric attribution. Those remain distinct evidence layers. The displayed historical hashes refer to original artifacts; `manifest.json` hashes the sanitized files actually distributed here. The manifest detects accidental changes relative to its pins; it is not a cryptographic signature or substitute for a trusted repository commit.

The map/model and source-attribution boundaries remain those documented in #43 and its linked #32/#34/#40/#41 foundations. No new proof of all-entry pole bounds, legal-line hypotheses, safe reversal, source support or evaluation faithfulness is asserted here. No numerical evaluator, batch driver, resume tool or new execution authorization is included.
