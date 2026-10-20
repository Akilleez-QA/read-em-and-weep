# One-step reversal-compatible lift freedom

For a fixed literal reversal-compatible presentation modulo `h^N`, `N >= 3`, the nonempty set of relative lifts modulo `h^(N+1)` is a torsor under

- `H^1(X,T_X)^G` at even `N`;
- `H^0(X,Lambda^2 T_X)^G direct_sum H^2(X,O_X)^G` at odd `N`.

The new product, overlap-map, and triple-unit coefficients may all vary. The allowed relative gauges are invariant even chart maps and invariant reversal-unitary edge units, literally the identity in every lower degree. For an abelian fourfold with geometric inversion, the dimensions are **16 at even steps and 12 at odd steps**, rather than the unrestricted 28 at every step.

## Files and review

- [PROOF.md](PROOF.md): full difference equations, exact gauge transport, torsor classification, injective comparison with unrestricted classes, both 2-morphism conventions, and the continuation boundary.
- [REVIEW.md](REVIEW.md): independent mathematical text review, passing under the stated one-step category and retained nonemptiness input. This is not formal machine verification or a source-instance evaluation.

SHA-256:

- `PROOF.md`: `6d1e3164e0180757267aba1339d3a163b628f5ec55a90df4901a9e362b0174c2`
- `REVIEW.md`: `b724ea74fa1d3539ba937226985d2ae7ab4c36f0c712fd886e4bd7e1afa77269`

## Exact dependencies

1. [PR409](https://github.com/Akilleez-QA/read-em-and-weep/pull/409), exact head `59fc9cdc40cf9a21fbb38549767829ff7471294f`: the [parity-separated proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/59fc9cdc40cf9a21fbb38549767829ff7471294f/research/hm/parity-separated-ambient-lifting/PROOF.md) and [odd-bivector repair](https://github.com/Akilleez-QA/read-em-and-weep/blob/59fc9cdc40cf9a21fbb38549767829ff7471294f/research/hm/parity-separated-ambient-lifting/ODD-BIVECTOR-REPAIR.md).
2. [PR416](https://github.com/Akilleez-QA/read-em-and-weep/pull/416), exact head and base commit `c71356722bc7bd1a426d26ea0ca6d050f4c3ed81`: the [reversal-compatible continuation proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/c71356722bc7bd1a426d26ea0ca6d050f4c3ed81/research/hm/parity-separated-ambient-lifting/REVERSAL-COMPATIBLE-CONTINUATION.md). Its retained invariant literal lifting input supplies nonemptiness and, separately, existence of a continuation of each chosen representative.
3. The [public invariant literal small-extension proof](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725): regular normalized differential three-slot descent on the stated individually invariant affine acyclic cover. The unrestricted comparison calculations are repeated in PROOF.md.
4. Ordinary differential HKR on smooth affine intersections, coherent Cech acyclicity, and exactness of finite-group invariants in characteristic zero.

## Scope

This classifies the stated **one-step relative equivalence classes**, with a temporary, noncanonical origin. It does not classify arbitrary formal continuations or show that an unrestricted continuation is equivalent to reversal form. It proves no module lift, period identification, algebraicity, prescribed-product gluing theorem, fixed-Moyal theorem, or six-pure-condition vanishing. No selected source, HM function, module, matrix, or retained detector is evaluated.
