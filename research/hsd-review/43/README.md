# Independent check of the one recorded edge on PR #43

Supplied-quotient replay of a single oriented edge. This directory does not
regenerate the geometric source, and it does not import
`research/hm/second-scalar-first-edge/replay.py`.

The checker reads `quotient.json` as data. It builds
`G(T,z)^{-70}` modulo `(T^9, z^{23})` twice, by Newton reciprocal and by the
generalized binomial series, then applies the displayed selector for roles
`(0,1,2,3)` and `m=(2,2,2,0)`. The sum is one partial term. It is not a
scalar-class value.

```sh
python3 research/hsd-review/43/recompute_edge.py
```

Python 3.10+ standard library only. The recorded outcome of that run is in
`VERDICT.md`: the partial term reproduces as 8655/16, with no arithmetic
defect found, and with source regeneration left as a missing hypothesis.
