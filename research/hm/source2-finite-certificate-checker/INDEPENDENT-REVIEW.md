# Independent review: finite correction-certificate checker

Result: PASS on the frozen artifacts below. This review verifies the
bounded supplied-data checker and its stated scope; it does not evaluate
an actual source or authenticate the geometric hypotheses for one.

## Source and mathematical interface

Read the full PR1107 theorem and freshly fetched its immutable file at
commit5b52eedce3420ccc3e407e97201bcdd056501bbf, path
research/hm/source2-pure-v-finite-obstruction/PROOF.md. Remote Git blob
a8f57401d93c296d23a5ed55cd09d8893222e7c1 matches retained bytes, whose
SHA256 is d1f96ad68df6781474e0aa247625b08de8cfc06e2af854418cbd32ce52469140.
This authenticates this written source only, not an actual instance or
all ancestor geometric hypotheses.

Read all implementation, tests, schema and README. The checker verifies
x0=s, Qx0=i_P and Qxi=-T x(i-1) for1<=i<=23, with exact sparse rational
polynomial coefficients and the required homogeneous degrees. The
matrix multiplication and substitution convention F(Aa)Rsource=Rtarget F(a)
are consistent. Optional nonsingular actions are not claimed to satisfy
group relations or generate the intended group. Absence of actions is
explicitly reported as unchecked equivariance.

The terminal T x23 need not vanish. The synthetic original-string test
correctly leaves a nonzero order25 remainder while all lower coefficients
cancel. The order31 versus degree30 inference is explicitly conditional
on the actual original lower pivots and geometric transport theorem,
not inferred from arbitrary supplied matrices. Original dimensions alone
and self-consistent digests cannot turn authenticity or rank flags true.

## Replay and adversarial review

- Independently replayed python verify.py and python -O verify.py: all45
  tests pass, byte-identical outputs, both matching RESULT.json.
- Added verify_independent.py, a separate scalar full-multinomial chain
  Q=3, T=2a0-3a1+5a2, xi=(-T/3)^i, with all three formal variables.
  Its33 checks pass in both modes with identical output.
- Every independent changed coefficient at x1 through x23 is detected
  even after rebinding the content digest. Malformed exponents and JSON
  duplicate keys, floating-point notation and nonfinite numbers reject.
- Production tests additionally cover dimensions, signs, inclusions,
  seed equality, degrees, indices, fractions, duplicate monomials,
  generator nonsingularity/intertwining and stale/incorrect digests.
- Resource-limit behavior is distinguished from invalid certificates.
  The initial oversized dimension/generator discrepancy was corrected:
  positive oversize now returns RESOURCE_LIMIT_INCONCLUSIVE, with two
  dedicated tests. Malformed dimensions remain invalid.

Only newly constructed synthetic or universal data were executed. No
actual HM coefficients, parameter values, selected directions, source
matrices or instance ranks were supplied, loaded or evaluated.

## Frozen SHA256 bindings

    check_certificate.py
    1967814e84a698f5abefd43f8b1e9b50c20789b76a8c1e097544844091900c91
    test_certificate.py
    9991960bb8716bc3d41b11fac1895f664b010fe2ed8d89737975842edf3ecef4
    verify.py
    f442f82ae4c641882ac26c4cc15a5ac6044b5b801dd0f4ae94fd4f02202fd216
    verify_independent.py
    7694489a3ca2b814f400f304cbf7d5faa2f6c9bf38ae3e9ab3b4d4786c59084c
    SCHEMA.md
    0204ede6c683e5d462eb932846dcb28041cb457b5afa0ee006b1986d50ffb947
    README.md
    7dc9848a0f5b747e8dea0356add664c83f3aa53a99ab548f99bbf250cb8a3444
    synthetic-example.json
    7cebb42f259a8c2f4aaed623bfa95026326257074f46d3acfc3376f3bdea37b9
    RESULT.json
    2dfab4b6dafbe6d8298640870d9532a13ce202de3633b9b164af4c4648ba04ec

The final README capacity caveat was read: fixed testing bounds do not
guarantee dense original-size capacity, and limits are not raised
automatically. This is accurate and does not change the tested code.

No remaining blocker found. The result remains an algebraic supplied-data
verification tool, not a certificate that an actual geometric object
has been found or that its rank has been evaluated.
