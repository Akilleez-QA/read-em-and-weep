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
python3 research/hsd-review/57/symmetry/check_involution.py
python3 -m unittest discover -s research/hsd-review/57 -p 'test_*.py' -v
python3 -m unittest discover -s research/hsd-review/57/symmetry -p 'test_*.py' -v
```

Python 3.10+ standard library only. Exit status `0` means the acceptance gate
holds: every pinned arithmetic check passes, there are exactly 18 orientations,
the only equal lists are the six iota orbits, paired signs match, there are
12 distinct lists, there are six active singletons, and the signed total is
`0/1`. Those six equalities are informational. Exit status `1` means an
unexpected equal-list partition, a singleton collision, a wrong distinct count,
or a total other than zero. Exit status `2` means a pinned arithmetic or
selector check failed. `symmetry/README.md` identifies the six equal lists as
the carrier involution. The tests do not regenerate the source DAG.

The recorded outcome is in `VERDICT.md`. The finite contraction of the supplied
arrays sums to zero. That zero uses twelve quotient polynomials, six of them
read twice. It is not a full-obstruction result.
