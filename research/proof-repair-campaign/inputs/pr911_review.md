# Independent exact-version review of the source125 ten-row coverage

## Verdict and byte binding

**PASS.** The exact package below gives a valid whole-label coverage deduction for the original stable label `G3.11.ea6bced3bddf`, source index125. The original necessary list has ten distinct tuples. The direct ff argument excludes one, and eight immutable published whole-source proof files exclude the other nine. I found no identity mismatch, missing tuple, duplicate counted as another tuple, branch-only substitution, or unjustified strengthening of a cited theorem.

This is an independent review of the assembly and its new ff argument. The nine prior exclusions are used as published mathematical theorems, not reproved in their entirety here. I read all eight pinned proof texts, including their hypotheses, source-specific arguments and boundaries, as well as the three foundational notes and the bb/bc exact-version review. I did not infer theorem scope from PR titles, a mutable frontier, or the manifest's scope-marker searches.

Reviewed SHA256 values:

| Artifact | SHA256 |
|---|---|
| PROOF.md | `1d8c9177ff0a39a36c4f490331547b7ff25345102f957fe328a2abd7cf177973` |
| COVERAGE.json | `2aa358c6edf36026354f2df2f8a73fa5a06bbeee109dea81513f329ba2d60de8` |
| verify.py | `e05912b199443fbbeea869c0d93310c92c01c94b1b557728fdffd035a5cb0f92` |
| REPRODUCE.md | `dcc09e3247e313739709089a9d93a05e147f88dee77772fc2b27c6ea90843774` |

These hashes were checked before and after the review work. No frozen artifact or audit-input byte was changed. This verdict is bound to these four versions; substantive changes require another exact-version review or an explicitly scoped addendum.

## 1. Independently established input identity and provenance

I independently queried the GitHub connector at each recorded immutable commit and exact repository path. Its full-file Git blob metadata matched all fourteen recorded inputs: the two original catalogs, three foundational notes, eight source-proof files, and bb/bc REVIEW.md. The bounded verifier independently recomputed each cached file's Git blob from its complete local bytes. Thus the local texts I read are bound to the stated commit:path objects, rather than merely being files with an author's asserted provenance. For bb/bc PROOF.md I additionally obtained the full text directly at the publication commit.

The original snapshot is commit `db51525015bb7c5e825833d550d08dedf6f6ea96`. The five original inputs and independently matched blobs are:

- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.
- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.

I directly inspected zero-based catalog entry125. It has A_q equal to O(-10)+O(4)+O(16), B_q equal to O(-18)+O(-6)+O(8), total endpoint degrees 10 and -16, original defect zero, and exactly the ordered ten tuples in the proof. The stable-label catalog contains one matching `G3.11.ea6bced3bddf` case, with profile11, source index125 and the same endpoints and original defect. Its historical `not_excluded` status is a snapshot field, not a current conclusion. The proof correctly neither rewrites it nor treats it as an obstacle to a later exclusion.

The publication pins for all eight source proofs independently matched the manifest and the separate constants in verify.py. In particular the ee file is Section6 of `profile11-o16-six-source-exclusions/PROOF.md` at `1644b5221fe6f8c23f30401fd6f2dc64230c0f5f`, not an invented single-ee path. The bb/bc file is the full two-source proof at `d679aa09811f821505254572a51e65b2904d03c9`, not a conditional predecessor. Publication at a pinned commit is all this deduction needs; no merged-PR assertion is made.

## 2. Necessity direction and exact tuple decoding

The actual splitting note proves the necessary coefficient relations

    a+d+g+h=1,
    b+c+d+e+f+2g+h=3,
    c+g+h>=1,

and the degree-minus-two coefficient

    (c+g+h-1)V+(d+e+g+h)P+(f+g)D.

Its table supplies the eight negative blocks at degrees -3,-4,-5,-8,-9,-10, exactly as used in PROOF.md. The note explicitly describes compatible formal splitting data, not a realization theorem. The endpoint note defines A_q=E/E^- and B_q=Q*/(Q*)^- in the one-one profile, proves necessary endpoint tests, and says the JSON records every compatible primal type. Consequently an actual realization of the fixed label has a tuple in its catalog entry. The coverage argument uses precisely this implication. It does not assume that every listed tuple is realizable or that the necessary filters are sufficient.

The exact order is

    ff, ef, ee, cf, ce, cc, bf, be, bc, bb.

I checked each tuple and decoded bundle against the foundational formula, the written table and COVERAGE.json. Every row has a=d=g=0, h=1 and b+c+e+f=2. They are the ten distinct combinations displayed, not ten references with one source counted twice. In particular bc and bb are different tuples even though they share one proof file.

I also ran a separate small check of the three classification constraints and the rank/degree of these ten explicit tuples without importing the coverage verifier. Every rank is17 and every degree is -54. This did not regenerate the catalog or search any source space.

## 3. The direct ff exclusion is sufficient and correctly typed

For ff, decoding gives

    E=(P+2D)(-2)+2O(-8)+O(-10).

Thus H0(E(2)) is exactly P+2D; the two lower-degree tails contribute no sections. The actual E is saturated in the ambient constant bundle and has H0(E(1))=0. The strict-top lemma applies with d=2 and gives H0(E^-(2))=0. Equivalently, the exact quotient sequence

    0 -> E^- -> E -> A_q -> 0

induces an injection H0(E(2))->H0(A_q(2)). This explains the precise global-section meaning of the proof's derivative-induced injection. No fiberwise injectivity of the rank17 source into a rank3 quotient is asserted, and no equivariant bundle splitting is assumed horizontal.

The negative O(-8) summand of A_q(2) contributes zero. The positive summands contribute Sym6 W and Sym18 W. Their characters are

    Sym6 W=V+P,
    Sym18 W=A+V+2P+D,
    H0(A_q(2))=A+2V+3P+D.

Besides running the supplied exact class-character calculation, I checked these two decompositions independently by the fixed integral McKay recurrence Sym(n+1)=W tensor Sym(n)-Sym(n-1), through n=18. The tensor-W edges used were 1--W--A--S--D--T, T--V and T--P--Wp. This is a fixed universal representation calculation, not an instance evaluation. The target dimension is26 and its D multiplicity is1; the source has D multiplicity2. Semisimplicity over C rules out the required injection. This excludes all of ff, with no subsidiary branch assumption.

## 4. Scope audit of the nine published source exclusions

All the following dependencies identify the same original label and endpoint pair, with original determinant defect zero, and the actual bundle obtained from the indicated tuple. Their source-specific boundary statements restrict the result to the listed source, not to a smaller branch. I checked those restrictions against the application here.

- **ef**, tuple `(0,0,0,0,1,1,0,1)`, PR860 at `cdf1d9ae5e477ef5f541d92888059ceedb4fd9b4`, blob `75e46cbd8c56a9a969691663d34587825cb8eb71`: the bundle is (2P+D)(-2)+Wp(-5)+O(-8)+O(-10). Its forced high subsystem includes the possibility that the whole lower P row vanishes; the proof treats all three high-system kernels and all four internal-image alternatives, including zero by constant descent. Its final conclusion is the entire ef source, not only a basepoint-free branch supplied as an extra assumption.

- **ee**, tuple `(0,0,0,0,2,0,0,1)`, PR846 at `1644b5221fe6f8c23f30401fd6f2dc64230c0f5f`, blob `c62eb6cc2e5368f9a5364121fd9df4e67198f8d0`: Result and scope explicitly lists source125's one ee tuple, and Section6 treats E=3P(-2)+2Wp(-5)+O(-10). Strict-top forces the two-P kernel subblock used there, rather than assuming it. The general theorem has six source edges at three labels; only this exact one is used in the assembly.

- **cf**, tuple `(0,0,1,0,0,1,0,1)`, PR882 at `ef8ed8d457494608472a2c07de776e9162b2c20f`, blob `b4ccaf9d3e5a77f0069664e86ae303a962e39442`: the bundle is (V+P+D)(-2)+V(-4)+O(-8)+O(-10). The proof first excludes the lower-P-zero alternative and then handles both surviving high-D first spans, including all quotient component cases. Its Section5 conclusion and Boundary expressly give the whole cf source.

- **ce**, tuple `(0,0,1,0,1,0,0,1)`, PR893 at `7645e2458c3b85c5d814c22255dae8cabc7226bc`, blob `fba1eb60737405f3ced37ab2d5542ca17eef20cb`: the bundle is (V+2P)(-2)+V(-4)+Wp(-5)+O(-10). This is not merely the exclusion of a high-P basepoint-free branch. The proof rules out that branch, treats the forced divisor12 alternative with nonzero V lower row, and then treats both zero and nonzero restricted high rows in the zero-V-lower-row alternative. Its final scope is the entire original ce source.

- **cc**, tuple `(0,0,2,0,0,0,0,1)`, PR895 at `f720acbe80547fd1bccd5ff54e6b62a4daa41834`, blob `d997b3822a32f33ab63ad8e3db27fcf043528bf7`: the bundle is (2V+P)(-2)+2V(-4)+O(-10). The proof explicitly recognizes two available V copies in the strict-top target, so does not claim a false V-multiplicity exclusion. It excludes the saturated positive-image case, derives the divisor12 case for the remaining rows, and finishes with a genuine constant space and trapped quartic tail. Its boundary is exactly the whole cc tuple.

- **bf**, tuple `(0,1,0,0,0,1,0,1)`, PR875 at `01f835fda6e771351555f0af1fa11647c27eb01e`, blob `5c0ec54ce5d234780f16c20d41134c18a32e6417`: the bundle is (P+D)(-2)+T(-3)+O(-8)+O(-10). The lower P row is proved nonzero, the complete high-D first-span alternatives are handled, and the constant and linear survivors are excluded with all residual scalar/T component alternatives. The final conclusion is the bf source, not an invocation of ef's source exclusion for a different bundle.

- **be**, tuple `(0,1,0,0,1,0,0,1)`, PR887 at `3ab2f311ed2e87828d42c7c0ce0124bcd6e35771`, blob `139ed6f19e5ab2ead6c9029e95e751ea132a0a49`: the bundle is 2P(-2)+T(-3)+Wp(-5)+O(-10). The lower-row and divisor alternatives are treated before the three high-P kernels. The subsequent actual constant projections and negative-only residual contradiction close the whole source. The theorem does not transfer a different source's exclusion by character analogy.

- **bc** and **bb**, respectively `(0,1,1,0,0,0,0,1)` and `(0,2,0,0,0,0,0,1)`, PR906 at `d679aa09811f821505254572a51e65b2904d03c9`, blob `2d6256b9b3350c0cecfadd022cdd302c216b37cb`: their bundles are (V+P)(-2)+T(-3)+V(-4)+O(-10), and P(-2)+2T(-3)+O(-10). The common actual-constant-A argument retains the scalar O(-10), removes actual constants P, and excludes a surviving linear top. Section4 treats bb. Section5 explicitly separates the nonzero and zero W(-9)-to-V(-4) component cases for bc; the first uses the nonzero cohomology map by Serre duality and the second preserves the actual quartic direct summand. Sections6-7 exclude both resulting residual bundles. Thus both full original tuples are available as theorem inputs, not just a conditional bc branch.

The bb/bc proof SHA256 is `9d0ac1a9bfbd0bb1f30b42721d456f0ee7776b215c07b52648e62f416f90758c`. Its published REVIEW.md has blob `31fc9e225dc0c2201ba88520ff7b01d794a76b6b`, SHA256 `4cdb87817e8722602ce01ebf5db793b8db3e90b1fd9644941ed35e86626fe0d1`, and a PASS verdict bound to those exact proof bytes. I read that review rather than relying solely on the PASS search. It covers both quartic-component cases and expressly disclaims whole-label coverage; the present assembly supplies that separate coverage step.

The dependencies may reuse universal kernel or connection lemmas. That is different from substituting an exclusion for a nonmatching source. No such substitution is made in this assembly, and the pinned statements impose no unresolved extra source-specific assumption on the nine applications.

## 5. Independent verifier execution and fail-closed checks

I inspected verify.py and ran both

    python3 verify.py
    python3 -O verify.py

against the unchanged cached inputs. Both exited0 with all three declared PASS lines and the stated boundary. Explicit check calls remain active under optimization; the verifier does not depend on Python assert for its checks.

I independently constructed seventeen negative controls in disposable copies outside the frozen package. Each was run in normal and optimized mode. All thirty-four runs exited1, printed no PASS line, and failed at the appropriate check:

| Mutation | Observed rejection |
|---|---|
| Omit bb | coverage row count |
| Duplicate bc in bb's slot | coverage row mapping: bb |
| Exchange ef and ee | coverage row mapping: ef |
| Point cf at ce's proof | coverage row mapping: cf |
| Change ff D multiplicity | bundle decoding: ff |
| Change stable label | source identity |
| Change an endpoint degree | manifest endpoints/defect |
| Mark closure incomplete | closure gate is incomplete |
| Mark bb/bc unpublished | unverified or changed publication pin: bb_bc |
| Change ee publication commit | unverified or changed publication pin: ee |
| Replace a scope marker with absent text | missing theorem-scope marker: ce |
| Change bb/bc review SHA binding | bb/bc SHA256 manifest binding |
| Change the written ff table bundle | written proof table identity: ff |
| Alter bb/bc immutable proof bytes | Git blob mismatch |
| Alter strict-top foundational bytes | Git blob mismatch |
| Remove the bb/bc review copy | missing-file failure |
| Append a byte to the source catalog | Git blob mismatch |

These are independent controls, not acceptance of the author's reported seven tests. They establish the tested rejection behavior, not a claim that the script is a general-purpose formal proof checker. In particular, textual scope-marker searches cannot establish a theorem's truth or scope; the manual readings above are essential. Nor does the verifier hash every sentence of its own PROOF.md or REPRODUCE.md. This review's whole-artifact SHA256 binding covers the reviewed versions.

The reproduction instructions accurately describe fourteen input files and standard-library-only execution, match the observed cached-mode output, and distinguish hash-checked cached copies from immutable repository readback. I inspected the --repository implementation: it uses the recorded commit:path with git show, without fetching or consulting working-tree versions, and applies the same blob checks. I did not execute that mode against an authenticated checkout. Instead I independently checked all fourteen commit:path-to-blob associations through GitHub as described above. The original catalog generator and prior proofs' mathematical verifiers were not rerun, which is consistent with this bounded coverage-review scope.

## 6. Exhaustion and final boundary

Assume an actual source realizes this original label. The necessary classification places its tuple in the exact original ten-row list. The matching row is either ff, contradicted directly by strict-top and D multiplicity, or one of the other nine, contradicted by the matching immutable whole-source theorem. There are no remaining tuples in that necessary list. This is a valid contradiction establishing exclusion of exactly the original label `G3.11.ea6bced3bddf`.

Nothing in this deduction recomputes a current frontier count, decrements a catalog, removes another label, or proves a global rank-four conclusion. The historical catalog remains untouched. No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance ranks, experiments, source scans or large computation were used. The supplemental calculations were small fixed universal representation and identity checks. No publication action was taken.

The package is suitable for publication as this exact label-coverage result. This review performs no publication or catalog accounting. This is a written mathematical coverage review, not formal proof certification.
