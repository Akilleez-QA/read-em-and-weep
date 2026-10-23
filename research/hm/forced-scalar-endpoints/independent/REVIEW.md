# Independent review: forced scalar endpoints

PASS for the exact proof SHA256 d76c66aac6cf179ae06a03d311edffe819834db6aa6dee1f39d59cd76ed7d2af.

Reviewed theorem: conditional on the actual P source and k=1, each target W′O(-r)+O(16), r=3 or5, forces beta_K to have rank one with coherent image exactly the displayed saturated O(14). This does not exclude either target or complete the original repair.

## Mathematical findings

1. The negative V coefficient in the cubic-zero envelope forces H0(K(3))=W′. Strict-top and equivariant Birkhoff splitting give the canonical top C=W′O(-3), with twelve remaining degrees at most -4. Degree conservation gives min K at least -14/-10. This is a justified lower bound on K, not an unjustified lower bound on an arbitrary kernel.
2. The top derivative has no negative-doublet component. Its scalar component is nonzero by strict-top. A common invariant divisor has degree at most ten by the first W′ occurrence at seven; minimum nonempty projective A5 orbit twelve makes it empty. Thus C surjects onto O(14), not merely generically.
3. If a subsheaf of O(14) plus B0 contains all of O(14), subtracting the scalar component of any local lift proves exact equality with O(14) plus its projected coherent image J. This equality is stronger than a noncanonical abstract extension splitting and does not involve the connection. In rank two, K surjects onto J=O(e), so e must be at least min K even if J is not saturated in B0.
4. The negative-doublet injection requires e even, e at most -r-9, and W′ in Sym^(-r-2-e). This excludes r=5 outright. For r=3 it leaves only e=-12: e=-14 would require W′ in Sym9, which is absent.
5. For this sole rank-two case, strict-top for L=K^- gives injection H0(L(4)) into H0(I(2)). Signed Euler accounting gives exactly 1+2A_std+3D+P-V. The negative V coefficient contradicts genuineness. No unproved next-derivative rank bound is used here.
6. Consequently rank L=13, degrees -78/-74, and maxdeg L at most -4. The snake lemma gives exact 0→O(-20)→L→N→0, so the indicated line is saturated. This does not split the extension or bound the individual lower slopes of L.
7. The actual next derivative lands in O(12). It cannot vanish: a horizontal saturated bundle in the constant ambient is constant in characteristic zero, contradicting negative L. Hence it has rank one, but its invariant image divisor remains undetermined. The rank-one envelopes are genuine, so the proof correctly stops before any target exclusion.

## Exact reproducibility

- Ten complete author inputs were independently fetched from their immutable GitHub commits and matched against author bytes, UTF-8 byte counts, SHA256 hashes and Git blob SHA1. INPUTS.json contains the independently returned Git blob IDs. The raw fetch record is AUTHOR_FETCHED.json.
- Production verifier: 537 checks plus 81 character-module controls. Normal and optimized outputs are byte-identical to frozen RESULT.json (7b92ee31d7843d098d2cbae6e2a252ba386bac2a2a44abd94457aa1b61c9935a). Verifier SHA256: db3a9d84f9f8b060cfebee0a23a46c1ba50cb3c82c9e4dbf68f2787ca73b3f5f.
- Independent checker: 4,389 explicit checks under normal and optimized Python; outputs byte-identical. It uses closed-form symmetric-power characters and class inner products, rather than the production McKay recurrence, and cross-checks all nine irreducibles through symmetric degree26. Rank, degree, quotient, raw character windows, signed envelopes, and source hashes are controlled. The independent evaluator is adapted from the earlier independently written doublet-endpoint reviewer, not from the author verifier.
- Independent checker SHA256: 0de013adc12cd32bd0f2738aae618d14a273bee4ab0cdadaa53bbfcd9176bee9.
- Independent RESULT.json SHA256: 3436a802525c60e458f0d4423ae8e9def2fcd23488baf170c08179c60720f652.

The complete new proof and relevant exact dependency statements were read. Existing actual inclusion/plateau and prior cubic/source theorems remain pinned mathematical premises; this review does not re-prove their entire transitive dependency graph. Computation supports, but does not replace, the sheaf and geometric arguments.

No actual source coefficients, points, parameters, jets, matrices, instance ranks, historical enumeration, external publication, or stopped experiment were used. No unresolved gap found in the frozen theorem.
