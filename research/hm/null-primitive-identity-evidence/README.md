# Portable primitive identity evidence (unpublished review copy)

## Verdict and trust boundary

C, the identity ev delta = 0, follows from the literal skew-column structure of the included model. The static checker verifies 20 paired and 10 zero block columns, the full ev pattern, and fixed file hashes. It performs no polynomial products or model/source evaluation.

A has a committed historical exact-computation receipt reporting 1350 entry checks: six 15-by-15 matrices, one for each carrier. Its inert checker source explicitly checks I P - Id15 + gamma H0 + H1 delta entry by entry. The package manifest binds model, checker, receipt and package verifier. A was NOT independently replayed or proved in this review. Hash binding and source inspection do not prove that the historical program ran, that its arithmetic implementation is correct, or that its report is true. Accepting A requires accepting that computation report and its producer as an imported premise.

The checker source homogenizes regular matrices to degree 1 and the rational primitive entries according to recorded weights. Setting v0=1 recovers each original polynomial token and each numerator/denominator quotient, wherever the denominator is invertible. Therefore an admitted homogeneous A identity specializes to the finite identity on those denominator localizations, for all six included carriers. This is a termwise interpretation of the source formula, not a new execution of A.

The receipt does not explicitly check C or delta gamma. No independent review of the earlier B proof or the contraction theorem is included here; any conclusions invoking those require their separately established premises. No claims about implementation correctness, owner domains, higher residuals, HPL, resource or aggregate admission, or an ID0 value follow from this review.

## Public source coordinates

Repository: https://github.com/Akilleez-QA/read-em-and-weep

Historical package: https://github.com/Akilleez-QA/read-em-and-weep/tree/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies

Pinned model: https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-operator-compiler/hm-pinned-model.json

The historical model and pinned-model copies are byte-identical. The public source coordinates are inherited from the evidence package; this independent review does not re-fetch or independently authenticate the remote repository. The self-contained checker fixes the SHA256 of all six included input files and checks the four relevant original manifest entries. The manifest lists additional files that are outside this subset and are not bundled or checked. The manifest and this subset are not signatures or independent execution attestations.

Only immutable public input bytes and inert historical source text are included under sources/. There are no connector receipts, machine-specific paths, private notes, or live production modules. The original evidence package is preserved separately, unchanged.

## Safe reproduction

Run python check_static.py or python -O check_static.py from any working directory. Only the standalone static checker should run. Never execute the historical .py.txt files under this review's authorization. The two saved static reports were reproduced and are byte-identical. SHA256SUMS covers all bundle files except itself.

provenance.json records source coordinates and input hashes. Fixed hashes in check_static.py are integrity pins, not an independent trust anchor against malicious replacement of the whole bundle.

## Structural proof of C

Let R be any commutative ring, and choose arbitrary `v0,...,v4` in R. For each block h=0,1 let its five basis vectors be `e0,...,e4`, and let the corresponding row of ev be `lambda=(v0,...,v4)`, zero on the other block. A skew-column of type `(r,s,epsilon)` means

    epsilon (v_s e_r - v_r e_s),  r<s, epsilon in {1,-1}.

The universal identity `lambda(v_s e_r-v_r e_s)=v_r v_s-v_s v_r=0` follows from commutativity. This is an abstract algebraic proof, not computation of the model's polynomial products. An empty block column is also killed by lambda.

Literal JSON inspection finds precisely these types in delta (indices zero-based):

    block 0:
    columns 0..4:  (2,3,-1), (3,4,-1), (0,4,+1), (0,1,-1), (1,2,-1)
    columns 5..9:  zero
    columns 10..14:(1,4,-1), (0,2,+1), (1,3,+1), (2,4,+1), (0,3,-1)

    block 1:
    columns 0..4:  zero
    columns 5..9:  (1,4,-1), (0,2,+1), (1,3,+1), (2,4,+1), (0,3,-1)
    columns 10..14:(2,3,-1), (3,4,-1), (0,4,+1), (0,1,-1), (1,2,-1)

The checker verifies all 30 block columns, with 20 nonempty pairs and 10 zero block columns, and verifies every literal entry of ev. A nonempty pair must have exactly two singleton records, the two symbol tokens must match the opposite row indices, and their unit coefficients must be opposite. All other entries are literal empty lists. It does not build polynomial objects, multiply records, or evaluate any field element.

In the finite model the literal constant token is `v0=1`. In the homogeneous degree-1 model the same token is `v0`; all other tokens are `v1,...,v4`. Thus the same literal pair map proves C both finitely and homogeneously, before any localization or pullback. It survives any commutative-ring specialization and any localization where the remaining formulas are defined. It is common to all six carriers, because delta and ev are shared model-level fields.

