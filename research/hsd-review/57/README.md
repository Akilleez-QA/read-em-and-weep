# Independent aggregate check of PR #57

Supplied-quotient replay of the eighteen oriented contributions in
`research/hm/second-scalar-m2220-complete/`, pinned at
`b1fdcdd666ed188250d6def3616733f1417fca81`. This directory does not regenerate
the geometric source, and it does not import that package's `replay.py`.

The checker reads `contributions.json` as data. It builds `G(T,z)^{-70}`
modulo `(T^9, z^{23})` twice, by Newton reciprocal and by the generalized
binomial series, then applies the displayed selector and orientation sign for
every active permutation of `m=(2,2,2,0)`. It also compares the thirteen
previously published coefficient arrays with the pinned partial-edge packages.

```sh
python3 research/hsd-review/57/recompute_aggregate.py
python3 -m unittest discover -s research/hsd-review/57 -p 'test_recompute.py' -v
```

Python 3.10+ standard library only. Exit status `1` means the signed sum of the
supplied arrays is `0/1` and the duplicate-quotient defect below is present.
Exit status `2` means the selector arithmetic itself failed.

The recorded outcome is in `VERDICT.md`. The finite contraction of the supplied
arrays sums to zero. Six of those arrays are copies of another orientation's
array, so the zero is not an aggregate of eighteen distinct quotients, and it
is not a full-obstruction result.
