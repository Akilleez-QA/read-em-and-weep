# Independent review: two-height endpoint capacity certificate

Verdict: **PASS**, scoped to the immutable file hashes below.

## Scope and sources

Read the full pinned PR1138 proof, the implementation, proof and tests, and fork PR1 coordination through [comment 6374674829](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6374674829). The motivating source at commit `c69f97aaf00e116e3a8abebf19a8e02868c4f7c4` was independently fetched; its returned Git blob `49a0b288cb3adc9c7e6df6f29f96ce46896f51e4` equals the blob computed from the retained input. This review does not re-certify the entire geometric proof or claim a new profile exclusion. The contribution reviewed here is reusable exact arithmetic and a checkable certificate.

## Mathematical review

Expansion of the two-summand capacity gives `F(h)=-2h^2+B h+C`, with `B=lambda1-lambda2+2N` and `C=N lambda2-N^2-N`. The completed-square identity is exact. Clipping the two adjacent integers around `B/4` supplies every feasible nearest integer, including singleton domains, boundary maxima and two-point ties. Integer floor division and arbitrary-precision arithmetic introduce no rounding assumptions.

The verifier does not trust the optimizer. It checks feasible equal-valued consecutive heights and the completed-square identity. Its strict outside forward-difference checks, together with the decrement of four in successive differences, prove global optimality and exclude omitted ties. They are sufficient as well as necessary. Parameter validation rejects booleans, nonintegers, zero/negative ranks and reversed degree order.

The strict-top filter is correctly equality-only. Below-capacity data are rejected rather than silently discarding partitions. Actual top-image flags and the final-stage top identity remain external geometric hypotheses; the explicit Boolean is an attestation, not proof authentication. The proof additionally states the initial-top bound and strict decrease assumptions. The filter leaves the universal capacity unchanged and does not claim realization of any surviving height.

## Independent reproducible checks

The author's 62,442 checks were replayed in ordinary and optimized Python, both exactly reproducing its retained RESULT.json. The separate independent script adds **385,882 checks** with byte-identical ordinary/optimized output:

- 74,725 synthetic instances compared with exhaustive evaluation of the original two-height sum, independently of the completed square;
- 12,093 independently constructed singleton/pair certificates, checking acceptance if and only if the complete optimizer list is supplied;
- 224,175 equality-boundary checks and 74,725 below-capacity misuse controls;
- 99 huge-integer cases checked against a separate discrete binary-search oracle rather than the optimizer formula;
- 65 remaining malformed-input and hypothesis-gate checks.

All arithmetic uses Python integers. No actual source coefficients, selected geometric instances, jets, historical row enumeration or prohibited experiment were run. The four author regressions are already-known PR1138 examples, not additional exclusions. This is not proof-assistant verification or a claim of literature novelty.

For relocation, place the independent script and result beside this review, then supply the packet directory explicitly:

```sh
python independent_verify.py PATH_TO_PACKET > independent.normal.json
python -O independent_verify.py PATH_TO_PACKET > independent.optimized.json
cmp independent.normal.json independent.optimized.json
cmp INDEPENDENT-RESULT.json independent.normal.json
```

## SHA-256 binding

Paths below are relative to the packet root, except the two independent test artifacts, which are relative to this review. ROOT-DERIVATION.md is scratch and is neither reviewed for publication nor included in this binding.

```json
{
  "INDEPENDENT-RESULT.json": "2cd2d9d3114418421f014e982fbe613f0c6002d4dde4005eb19ff55ddea5e558",
  "INPUTS.json": "1ad157d85632460ef538d54ddee309c6ad3c578b1a04171ceceb7db47f191037",
  "PROOF.md": "11bfbab8fa9108d6f8c31d53979c4731cfeec5f3de81e7bcbf3b1ea27ab6b459",
  "README.md": "e8bc5c0e7a1e12f52e2c29c7282866c514ceb350a996d52b87c68c7004a188c5",
  "RESULT.json": "1b515d6cf10edbdea8f43bd3adf23fa8a016fde65ff797c20f2227493074c69e",
  "capacity.py": "bfe4be6c274e71529cf6c0aff64d2e3429cd6655bbec656edf2f1749585df383",
  "independent_verify.py": "9b156e711f7329c338d3410c9bcfceb23094f6d1630adf70ed0f63c8d216b240",
  "inputs/pr1138-proof.md": "be3e6ef741268733f9ddc02405a3d8e030742d8ff3f2378570a0f0d1fe4d1328",
  "verify.py": "6583e06f780764943dcc933f7d44b746fdaa0c3edd914b34e7d8e09083770cad"
}
```
