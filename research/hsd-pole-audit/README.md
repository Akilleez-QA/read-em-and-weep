# Independent pole and degree audit

Exact checks of the five source-to-residue gates in PR #40 at
`dc60a859a0157b1d2d1b57b37324509abc22c600`. The scripts read the pinned
package and do not call its `verify.py` checkers.

```sh
python3 research/hsd-pole-audit/audit_exact.py
python3 research/hsd-pole-audit/factor48_walk.py --jets /tmp/current-L-jets
```

`audit_exact.py` rebuilds the pole graph (`pole_graph.js`), the 3,090
homogeneous identities, the 451 divisor clearances, the physical-frame
weights, and the degree-272 arithmetic. The factor-48 walk needs the four
normalized axis circuits regenerated from the pinned numerator and jet
packages; those circuits are not stored in PR #40.
