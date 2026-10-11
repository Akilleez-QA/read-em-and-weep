# All 81 L_minus scalar coordinates: exact supplied-quotient replay

For the pinned map `L_minus(X)=X02[0,5]-X13[10,1]`, all 81 displayed scalar coordinates over Q are zero: 65 are exact nonempty-boundary contractions and 16 have empty boundary index sets. This is the complete scalar-image computation under the stated selector and source-attribution hypotheses. It does not establish vanishing or nonvanishing of the full obstruction, and does not repair the target theorem.

The finite replay uses all 24 full exact quotients. Eighteen previously accepted quotients are reused unchanged; six orientations with first role 3 complete the coverage. No modular coefficients, point samples, variable-exponent reduction or old scalar zero relations are substituted.

## Reproduction

Python 3.10+ standard library only:

```sh
python3 research/hm/second-scalar-all81/replay.py
python3 -O research/hm/second-scalar-all81/replay.py
python3 -m unittest discover -s research/hm/second-scalar-all81 -p 'test_replay.py' -v
```

The checker generates every selector row from the supplied quotient data, verifies its canonical row-list SHA-256 against a digest prepared by comparing the historical primary and independent exact rows, and recomputes each oriented sum and each coordinate. It also checks repeated physical source coefficients for equality. Full row lists are generated in memory rather than duplicated in the package.

Verified totals:
- 24 full quotients, 81 targets, 648 oriented requests
- 65 computed coordinates and 16 empty-boundary coordinates
- 114,048 selected rows and 32,472 distinct physical exponent vectors
- 10,504 nonzero rows and 3,152 distinct exponent vectors carrying nonzero coefficients
- 552 nonzero signed oriented selections; all 81 coordinate sums are exactly zero

The 3,152 count is not the number of distinct numerical coefficient values. It counts nonzero coefficients indexed by distinct physical exponent vectors.

## Target and selector derivation

Enumerate `m` in `{2,1,0}^4` lexicographically, with index `sum((2-m_i)*3^(3-i))`. Laurent exponents are `(-m_i-1)`. An orientation `(i,j,k,l)` contributes precisely when `m_i=2`.

For each active orientation, set `S=sum(m)`, `d=6+m_j`, `L=22-m_l`, `w=35+S`. Read quotient slots `(r,w,ell)` for `0<=r<=d`, `0<=ell<=L`. Multiply by `[T^(d-r)z^(L-ell)]G(T,z)^(-70)`, where `G=1+z+T+3Tz+Tz^2+T^2z+T^2z^2`, and apply the orientation sign. The source-root scalar is already embedded in the quotient. Role-ordered physical exponents are `(272,215-r,157-S+r-ell,47+ell)`, summing to `691-S`.

Exactly 16 monomials have every entry at most 1, hence no active orientation. Their zero is an empty-boundary sum under this selector. The geometric justification of that selector remains part of the external source-to-residue hypotheses; it is not a reuse of the original scalar's zero list.

All quotients retain shape `(9,44,23)`, common denominator 64 and separate homogeneous degrees. A missing coefficient inside a supplied full quotient is zero; a missing quotient or required orientation is an error.

## Evidence layers

The public finite computation is reproducible from the included data. Historical independent audits additionally checked exact integer/Fraction terminal products, all selector rows, archived frontiers, source bindings and recovery history. The seal verified 1,143 final artifact pins and 1,140 frozen audit pins. Those historical checks reevaluated zero source DAG nodes.

The large source/checkpoint archives are not included. Their original hashes in `provenance.json` and per-quotient records identify undistributed evidence; hashes alone do not reproduce it. This package does not regenerate the new-map source DAG, reconstruct the original terminal checkpoints or independently prove geometric attribution. See SOURCES.md.

Equal role-relative quotient arrays do occur and are retained separately with distinct bindings. They do not license omitting orientations. DUPLICATE-ARRAYS.md gives the precise physical-variable permutation and an executable 1,086-row covariance check; symbolic source symmetry is not asserted.
