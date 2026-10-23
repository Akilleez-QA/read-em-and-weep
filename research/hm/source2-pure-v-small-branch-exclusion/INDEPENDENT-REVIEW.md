# Independent review: exclusion of the nine-dimensional generated endpoint

## Verdict and immutable scope

The theorem is sound under its retained actual-source hypotheses. The argument excludes the generated endpoint nine, not source2 or the compatible pure-V hypothesis itself. It leaves both mechanisms for endpoint sixteen undecided.

This review binds to:

- `PROOF.md` SHA256 `4a97fddf0fd37c5b34839482d0fa25b209cfb63541c038ab0a2bbc8ca3e6f58e`.
- `verify.py` SHA256 `53c7de7c7e2c903e393a8f978d764e72f9ce983062836bc40f076ae2926e0af1`.

## Actual-map audit

1. **Containment before subtraction.** PR1059 identifies endpoint nine with the actual containment of the canonical P_h in NC2. Since I2 is also contained there and NC is a submodule for both fixed negative arrows, F2=I2+P_h and F3=W F2 are actual subspaces of NC2 and NC3. PR1054 supplies the exact middle character W′+2T. Thus the actual quotient NC3/F3 is S; this is not an inference that an arbitrary representation embedding exists.

2. **Correct degree and parity.** The quadratic Q is invariant and therefore central-even. Its multiplication from H1(B(3))_- lands in the full H1(B(5))_-=W′+3T. The latter character is supplied by PR1072 and agrees with the actual Koszul continuation retained in PR1068. There is no S in this entire target, not merely in a chosen residual summand. Both routes in Q3(ell a)=ell Q2(a) land in that negative-parity target.

3. **Literal commutation, not a new hypothesis on h.** Q2 and Q3 are multiplication by the same polynomial on cohomology; functoriality of multiplication proves their commutation with each negative linear form. Since Q2(F2)=I4 and the actual degree-four joint kernel contains I4, Q3 annihilates F3. Its restriction to NC3 consequently factors through S, and equivariance forces that restriction to vanish. Neither h nor a three-vertex radical map is being extended for this step.

4. **The decisive full-kernel contradiction.** The unique V_C in NC2 is disjoint from ker(Q2|NC2)=I2, so its Q2 image is an embedded nonzero V. All its negative linear descendants vanish because W V_C lies in NC3. PR1068 identifies the full ambient joint-negative kernel with the actual NC4=P+D. This rules out that embedded V. A mere inclusion NC4 in the joint kernel would not suffice; the pinned theorem supplies equality.

5. **No hidden preservation or normalization.** The proof never assumes Q(NC2) lies in NR4, Q preserves the endpoint subsystem, or h commutes across directions. No repeated-D identification, horizontal splitting, transfer scalar, transvectant normalization, or actual-instance evaluation is involved. Earlier endpoint-nine statements remain conditional deductions on an excluded branch; the contradiction does not select either surviving endpoint-sixteen projection.

## Input authentication

Each of the five complete originals was independently retrieved at the exact commit and path in `INPUTS.json`. Retrieved bytes matched the retained input exactly. SHA256 values matched the manifest, and independent Git blob computations gave:

| Input | Commit | Git blob |
|---|---|---|
| 1054 | `8732cb65fe0e72da59e785f3f85ad197a7092e6c` | `64e6bf9f1bf46440700ebab7c90a18f9d8155fd8` |
| 1059 | `af2f163e4bcc593b6895ace840c139d2d4668cde` | `2b00a40de04a7084ff2f08c767fdd2f4f13ae5f4` |
| 1065 | `fd75633464cd587856287cc7866520fb4105ef5b` | `41f7dada9c1606c4a2a47b330b676b1f090ec1b4` |
| 1068 | `05e8b33eb87e9f36aa30500145cc42bc0ea00df8` | `5ae07c02624d70c0ccd33d7ec34202504173ff83` |
| 1072 | `d03beb727c7e778026dcceb3555c899a0808e093` | `65dda3e16ded2b79ad84c583f248b09c425e9881` |

This authenticates the stated immediate inputs and audits their use; it is not a claim to have recursively reproved every ancestral geometric theorem.

## Reproduction and evidence

Independent executions of `python verify.py` and `python -O verify.py` each passed all 24 checks. Their outputs were byte-identical to one another and to `RESULT.json`. The checker uses explicit failures rather than optimization-sensitive assertions.

The finite checks confirm input integrity and representation, dimension, and parity bookkeeping. Their formal commutative-polynomial test is not itself evidence for the actual cohomological map identification: that identification was separately checked in the proof and pinned inputs as explained above. No selected actual source coefficients or instances were evaluated.

Independent mathematical review completed 2026-10-23.
