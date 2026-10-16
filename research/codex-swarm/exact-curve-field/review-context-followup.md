# RF-R-1 independent repair acceptance

Accepted narrowly: receiving `Execution.rational` checks receiver liveness first,
then checks both polynomial arguments belong to that receiver before constant
construction or Rational normalization. This closes foreign-pair meter escape
and poisoned-receiver bypass. No physical source admission follows.

Compared against preserved `9f670dbb8`: `field.py` adds exactly three lines at
the start of `rational`; the producer marker changes only field digest and
derived bundle digest. Current field SHA256 is
`4dade295de59741ceb54eb4574c58ffc82c8a1a17063fd1c081656a8b2069b01`;
bundle is `dfd6e32864e5739c65600f58da6b91261c3cd3c60dd0f43d8ec63d81f413c7a7`.
The new independent byte control verifies every producer payload and recomputes
the bundle digest. Original review bytes are preserved. As explicitly authorized,
the old independent test loses only the former regression's expectedFailure
decorator, with its header identifying the repair; the regression must now pass.

Four new tests cover marker integrity, foreign numerator/denominator/both with
an otherwise healthy receiver, poisoned receiver with foreign/same-context/
constant arguments, and valid same-context constructors. Invalid calls leave
both receiver and foreign counters unchanged. A poisoned receiver must raise
LimitExceeded first, even when inputs are foreign. Healthy receivers remain live
after ownership rejection. Mixed scalar cases detect allocation-before-validation.

Bounded replay: 13 producer + 13 original independent + 4 new independent tests
pass in each of normal and `-O`. Direct historical independent invocation uses
`--child` to avoid its nested runner. Each child has hard 768MiB address space,
59-second CPU and parent 60-second wall bounds. All inputs are tiny artificial
constants/polynomials; no physical source, jets, or fibers were executed.

Separately replayed the UNCHANGED public Null regression bytes from commit
`23bffa822566ff98b0e7ff4c6c63b266827b7aaa`, path
`research/hm/null-source-integration/exact-field-review/test_factory_regression.py`.
SHA256 `74c729f8eff58ecfcbb93221acc27e391c85fe62320c07d7470b94fa64a1f4c7`.
Both original public tests pass normal and `-O`, under the same bounds. Code was
read via `git show`, compiled and executed in the child's real `__main__`
namespace against the current field module, without copying or changing it.
An initial wrapper used an unregistered dictionary and collected zero tests
(exit 5); it was rejected, corrected, and both successful replays explicitly
reported `Ran 2 tests`. Public tests are not claimed as newly authored cases.

Total repair replay: 32 tests per mode (30 local plus 2 separately attributed
public tests), no expected failures. This is a constructor/meter repair review,
not renewed validation of source geometry or physical resource feasibility.
