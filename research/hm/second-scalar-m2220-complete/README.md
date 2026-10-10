# Complete selected L_minus coordinate: m=(2,2,2,0) equals zero over Q

For the supplied full quotients of

`L_minus(X) = X02[0,5] - X13[10,1]`,

the displayed selector for `m=(2,2,2,0)` (Laurent exponents `(-3,-3,-3,-1)`) contracts **all eighteen required oriented contributions to exactly 0 in Q**. There are 3,258 distinct selected source exponents, 288 nonzero selected coefficients and 4,014 retained terms across the full quotients. All eighteen signed edge contributions are individually nonzero; their exact sum cancels.

This completes one selected coordinate. It does **not** establish that the entire L_minus scalar image vanishes, that the full obstruction vanishes, or that a theorem is repaired. Interpreting the supplied numerical data as a geometric coordinate remains conditional on the pinned model and source-attribution hypotheses described in [SOURCES.md](SOURCES.md).

## Exact oriented contributions

| Orientation | Signed contribution | Quotient terms | Selector rows | Nonzero selected |
| --- | ---: | ---: | ---: | ---: |
| 0123 | 8655/16 | 203 | 207 | 24 |
| 0132 | -2817/16 | 203 | 189 | 16 |
| 0213 | 18831/8 | 233 | 207 | 24 |
| 0231 | -21601/8 | 233 | 189 | 16 |
| 0312 | 1457/8 | 233 | 147 | 8 |
| 0321 | -803/4 | 233 | 147 | 8 |
| 1023 | 15705/16 | 203 | 207 | 24 |
| 1032 | -5667/16 | 203 | 189 | 16 |
| 1203 | 1953/4 | 233 | 207 | 24 |
| 1230 | -4313/4 | 233 | 189 | 16 |
| 1302 | 407/8 | 233 | 147 | 8 |
| 1320 | -353/4 | 233 | 147 | 8 |
| 2013 | -41517/16 | 233 | 207 | 24 |
| 2031 | 42869/16 | 233 | 189 | 16 |
| 2103 | -22917/16 | 233 | 207 | 24 |
| 2130 | 21869/16 | 233 | 189 | 16 |
| 2301 | 131/2 | 203 | 147 | 8 |
| 2310 | -169/2 | 203 | 147 | 8 |
| **Exact selected total** | **0/1** | **4014** | **3258** | **288** |

The last five rows of oriented data (2031, 2103, 2130, 2301, 2310) were not supplied in the earlier partial replay packages. They are included here together with all thirteen previously published orientations. No orientation is omitted or silently replaced by zero.

## Clean replay

Python 3.10+ standard library only. This package is standalone: it does not import previous packages, access a network, unpickle checkpoints, start subprocesses or evaluate a numerical source DAG.

```sh
python3 research/hm/second-scalar-m2220-complete/replay.py
python3 -m unittest discover -s research/hm/second-scalar-m2220-complete -p 'test_replay.py' -v
python3 -O research/hm/second-scalar-m2220-complete/replay.py
```

The checker verifies the distributed file hashes, all 4,014 full-quotient terms and all 3,258 selector rows. It derives the integer kernel, physical source exponents and permutation signs independently of the recorded rows, recomputes each rational contraction, verifies exact orientation coverage and exponent distinctness, then sums all eighteen signed contributions. Checks stay active under optimized Python.

The tests independently construct the positive power of the kernel polynomial and verify its inverse identity. Negative guards reject missing/duplicated/inactive orientations, zero-filled missing contributions, changed coefficient arrays even with recomputed array digests, altered signs/slots/weights/exponents, invalid rational encodings, wrong counts/totals, overbroad geometric claims and package corruption.

## Selector and sign conventions

Write an orientation as `(i,j,k,l)`, with `m=(2,2,2,0)` and `S=sum(m)=6`. Exactly the permutations with `m_i=2` enter this selected coordinate. Set

- `d = 6 + m_j`
- `L = 22 - m_l`
- `w = 35 + S = 41`

The retained quotient has shape `(9,44,23)` and common denominator 64, with homogeneous degrees separated. At each `0 <= r <= d`, `0 <= ell <= L`, the selector reads quotient slot `(r,w,ell)` and multiplies it by

`[T^(d-r) z^(L-ell)] G(T,z)^(-70)`,

where `G=1+z+T+3Tz+Tz^2+T^2z+T^2z^2`. The checker derives this kernel by the finite binomial expansion modulo `(T^9,z^23)`.

In role order, physical source exponents are

`(272, 215-r, 157-S+r-ell, 47+ell)`.

Their sum is 685. The source-root scalar is already incorporated into the quotient coefficients; only the orientation permutation sign is then applied. For example, 1302 contracts unsigned to `-407/8` and has orientation sign `-1`, yielding `407/8`. An absent slot of a supplied full quotient denotes a zero coefficient within that quotient; an absent orientation is an error.

The fresh L_minus support enclosures 47/215/454 and shape `(9,44,23)` are the relevant external source bounds. The original scalar's narrower window, failed factor-48 diagnostic, structural-zero list and scalar-specific relations are not used as substitutes.

## Delivered evidence and limits

- `contributions.json`: all eighteen full quotients, exact selector rows, signed contributions, per-edge historical artifact digests and explicit selected-coordinate scope; compact JSON keeps the finite data small.
- `replay.py` and `test_replay.py`: executable supplied-data replay and guards.
- `provenance.json`: historical sealed-result/comparison/manifest hashes, distinguished from public reproduction.
- `SOURCES.md`: dependency and source-regeneration boundary.
- `manifest.json`: SHA-256 and byte counts of every distributed file except itself. It detects changes relative to its pins; it is not a cryptographic signature.

Historical independent audits checked exact integer and Fraction terminal reconstruction, selected rows, archived frontiers and the interruption-recovery history. The final sealed result and primary comparison agree on all eighteen edges and all 3,258 rows. The seal checked 904 final artifact pins, 609 frozen audit pins, twenty first-edge historical mappings and twenty-three recovery mappings. Those historical audits reevaluated zero source DAG nodes. Their large checkpoint archives and manifests are not distributed here; hashes identify them but do not make their verification reproducible from this package.

The publicly executable result here is the exact finite contraction of the supplied data. Full new-map source regeneration, terminal reconstruction from distributed checkpoints, and geometric source attribution are separate evidence layers, not newly established by this replay.
