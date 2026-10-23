# Independent whole-packet review

## Verdict: PASS

Reviewed on 2026-10-23. No blocking mathematical, provenance, arithmetic, or scope defect was found in this packet. This is a review of the full new proof and its stated imported hypotheses, not a new proof of every upstream HM theorem or of the historical global profile-exhaustion theorem.

The supported result is the actual coefficient-space injection

    W' + 2T -> H0(A_q(3)),

uniformly for the four PR1123 primary-compatible sources, together with the exhaustive necessary alternatives

    D: H0(K(3)) in {0,S};
    P: H0(K(3)) in {0,W'};
    V and Z: H0(K(3))=0.

“Alternatives” does not assert that either nonzero alternative is realized. The result is not a rank14 subbundle injection or a generic-rank14 assertion.

## 1. Complete material and provenance checked

I read the complete PROOF.md, verify.py, characters.py, REPRODUCE.md, INPUTS.json and all six retained source-proof notes: PR1123, PR1129, actual splitting, actual ambient Gauss comparison, strict-top, and the original182 coverage/index note. I also read the retained character reference. I parsed the complete fixed182 JSON and the complete RESULT.json, rather than sampling their displayed rows.

All eight inputs were independently retrieved through read-only GitHub file calls at the exact immutable commit/path in INPUTS.json. Each full fetched content string matched the retained file exactly, and each GitHub-reported blob SHA matched the manifest. Independently recomputing byte count, SHA256, and Git blob SHA1 also passed for every file. Thus this was not merely a check of self-consistency among local claimed hashes.

| Retained input | Immutable commit | Verified Git blob |
|---|---|---|
| inputs/pr1123-proof.md | 504b7eb800407dfc7e6340c98c72cdd553939f54 | 43cc2fe6ac82d7cb01b8c32dc2ef906212c3b705 |
| inputs/pr1129-proof.md | d1238732f42df5c70ba4430e230428d2cf699bbe | c8094f1a85b48094a7538230db1f92acfd7929d0 |
| inputs/actual-splitting.md | db51525015bb7c5e825833d550d08dedf6f6ea96 | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 |
| inputs/ambient-gauss-proof.md | db51525015bb7c5e825833d550d08dedf6f6ea96 | 303c6927265296440470b9dd4015fe6e8d55ca4d |
| inputs/strict-top.md | db51525015bb7c5e825833d550d08dedf6f6ea96 | d7506dae49b4be43230450c4132bd5db91f137ef |
| inputs/frontier182.json | db51525015bb7c5e825833d550d08dedf6f6ea96 | 7e733f9543651b00b309cd56804ddd0a2eaef517 |
| inputs/character-reference.py | db51525015bb7c5e825833d550d08dedf6f6ea96 | 9eb58f03edde15dd612087440d8180e9e16d1755 |
| inputs/cover182-proof.md | db51525015bb7c5e825833d550d08dedf6f6ea96 | 4afcfab4047e1563a2655a0f362a70ea103ea93a |

The full PR1123 proof supplies the four sources unconditionally on the later rank-three source ledger, relative to its named actual HM inputs. Its argument uses both terminal coefficient arrows and the canonical lower-slope quotient; it does not identify an arbitrary negative subbundle with the canonical slope piece. I checked its reduction a=1, d=g=h=0 and b+c+e+f=3 with b,c>=1: the four tuples give exactly the four source splittings used here. Each has rank17 and degree-54. PR1129 supplies the near-top coefficient lemma; this packet restates and applies its geometric mechanism without needing its separate canonical-submodule construction.

The actual ambient comparison proves that E is the saturated plane-section subbundle of a constant thirty-space and that the derivative is its actual second fundamental form. The rank54 coefficient/terminal presentation is a different inclusion. The new proof never transfers that presentation's connection to E or treats an equivariant Birkhoff complement as horizontal.

## 2. Geometric proof audit

### 2.1 Near-top visibility and saturation

For a direct cubic block U O(-3), the quotient in E has degrees at most -2. The same assertion holds after taking a coefficient line inside that block: the other cubic coefficient lines remain degree -3. Hence a vanishing coefficient gives a saturated negative line, not merely a generically injective map with an unexamined zero divisor.

More generally, if a saturated L=U O(-3) is killed by beta_E, its second fundamental form lands in (E/L)(-2). The needed Hom group is exactly

    Hom(L,(E/L)(-2)) = U* tensor H0((E/L)(1)) = 0.

There is no reversal of the quotient degree inequality. Since E/L and H O/E are locally free, H O/L is locally free, so L is also saturated in the constant ambient bundle. The horizontal classifying-map argument is valid over C and contradicts its negative degree. This proves coefficientwise visibility, not fiberwise injectivity of the cubic block's actual derivative.

### 2.2 Coherent-image orientation and strict-top bound

The proof correctly defines I as the coherent image of p:F=R O(-2)->A_q, not the saturation of that image. A coherent subsheaf of the bundle A_q is torsion-free, hence locally free on the smooth curve. Therefore

    0 -> K_R -> F -> I -> 0

is exact with the displayed map onto I. In particular K_R is saturated in F. Replacing I by its saturation without changing the exact sequence would have been invalid; the packet does not do this.

Strict-top applies to the actual E in H O and gives H0(K(2))=0. Since K_R is a subsheaf of K, every degree of K_R is at most -3. The top coefficient map R->H0(A_q(2)) is injective by left exactness, so p|F is nonzero and r=rank(I)>=1. Consequently

    h0(K_R(3)) <= rank(K_R) = dim(R)-r <= dim(R)-1.

The upper bounds are 4,3,2 for D,P,V, respectively. These bounds concern the kernel of the actual top row. The proof does not assume its generic rank, claim surjectivity onto A_q, or evaluate a row scalar.

The exact identities D tensor W=S+T, P tensor W=W'+T, V tensor W=T each have one irreducible six-dimensional T. Killing that T would force at least six cubic kernel sections, contradicting the strict bounds. Thus its coefficient map is nonzero and, by irreducibility, injective.

### 2.3 Graph cancellation is full actual quotient cancellation

For the displayed C_T=T O(-3), the identity

    Hom_G(C_T,F)=Hom_G(T,R tensor W)

has dimension one. The nonzero top T map is its composition with p|F. If the displayed cubic T and the top T had the same target copy, Schur's lemma would make their coefficient maps proportional. Choosing the proportional lift g gives equality in

    Hom_G(T,H0(A_q(3))) = Hom_G(T O(-3),A_q).

Therefore p|C_T=(p|F)g as full bundle morphisms into A_q. This is not merely equality after projection to one target summand, equality of generic fibers, or cancellation of selected coefficients.

The graph c -> c-g(c) is the image of a triangular automorphism of F+C_T, extended by the identity on the rest of E. It is consequently a saturated direct T O(-3) summand with the same complementary quotient degrees. Its whole p-row vanishes, so its whole beta_E-row vanishes. Section2's horizontal-negative contradiction applies. Thus the two T copies are independent in H0(A_q(3)). The visible W' copy is disjoint because W' and T are distinct irreducibles.

For Z-type, all degrees of E are at most -3, so the same strict-top theorem with d=3 directly gives H0(K(3))=0. No nonexistent degree-minus-two block is invoked in this case.

### 2.4 Complete cubic-kernel alternatives

The source cubic characters are respectively W'+S+2T, 2W'+2T, W'+2T, W'+2T. The exact sequence 0->K->E->A_q gives the kernel of H0(E(3))->H0(A_q(3)) as H0(K(3)); no surjectivity on H0 is needed. The independently proved W'+2T injection uses all source T multiplicities. Finite-group semisimplicity then leaves either zero or the unique S in D-type, at most one W' in P-type, and zero in V/Z. There is no unnoticed diagonal T kernel. The asserted equivalence H0(K(3))=0 iff maxdeg(K)<=-4 follows from maxdeg(K)<=-3, with the zero bundle understood separately.

## 3. Packaged verifier and independent arithmetic

Both commands completed successfully without modifying the result:

    python verify.py
    python -O verify.py

Each reported 341 checks, 15 additional historical exclusions, 45 total historical exclusions, and exact_result_reproduced=true. I checked that conditions use explicit RuntimeError rather than Python assert. The count is 260 checks in verify.py plus 81 pointwise tensor-by-W checks in characters.py. RESULT.json was reproduced byte for byte in both modes.

For an independent calculation I did NOT import characters.py, verify.py, or the retained character-reference program, and did not use the tensor-by-W adjacency recurrence. I used the nine conjugacy classes with sizes (1,1,12,12,12,12,20,20,30), a directly specified irreducible character table over Z[phi] with phi^2=phi+1, and the closed polynomial

    chi(Sym^n W)(t) = sum_(k=0..floor(n/2)) (-1)^k binom(n-k,k) t^(n-2k).

For negative n the contribution was zero. Multiplicities were extracted by the exact class-weighted inner product divided by 120. I checked all 81 pairwise orthogonality identities, sum(dim R)^2=120, nonnegative integral decompositions, pointwise reconstruction on all nine classes, and dim(Sym^n W)=n+1 through n=31. This separately validates the representation convention and rules out a shared adjacency-table implementation error.

This independent calculation reproduced:

- All four full cubic source characters and the three top products with T multiplicity one.
- All five additional quotient-shape identities, retaining repeated constituents.
- The cubic character of every one of the 182 ordered A records.
- All45 enriched rejected records exactly, including stable ID, profile, ordered A and B, original defect, source index/commit, cubic character and missing multiplicities.
- All15 enriched additional records exactly, not only their count or their quotient shapes.
- All137 passing stable IDs in their retained order.

The original weaker condition rejects 25/1/4 in profiles11/12/21; the stronger condition rejects 39/2/4. Thus the difference is 14/1/0, with each additional record missing exactly one T. This is bounded arithmetic in the universal representation ring, not selected actual HM/source-instance computation.

## 4. Full fifteen-record cross-check

Below “one(e)” means O(e), and representation labels retain the packet's physical marking. The ordered A/B data, rather than just isomorphism classes of A, distinguish records. Character labels are defined by the five verified shapes:

- C1: A=one(-8)+Wp(3), H0(A(3))=W+Wp+S+T.
- C2: A=Wp(-3)+one(4), H0(A(3))=2Wp+T.
- C3: A=Wp(-3)+one(6), H0(A(3))=Wp+S+T.
- C4: A=V(0), H0(A(3))=Wp+S+T.
- C5: A=Wp(-3)+one(10), H0(A(3))=W+2Wp+S+T.

| Profile | Original index | Stable ID | A character/shape | Ordered B | Original defect |
|---|---:|---|---|---|---:|
| 11 | 19 | G3.11.ef6c4c677f42 | C1 | one(-28)+one(-6)+one(6) | 24 |
| 11 | 20 | G3.11.c2031710a614 | C1 | W(-17)+one(6) | 24 |
| 11 | 23 | G3.11.77693812fcd3 | C1 | one(-18)+one(-12)+one(6) | 20 |
| 11 | 42 | G3.11.73e71f5f6820 | C2 | one(-6)+W(-5) | 12 |
| 11 | 43 | G3.11.782090f51bde | C2 | one(-18)+Wp(1) | 12 |
| 11 | 44 | G3.11.e2c410c9b2e6 | C1 | W(-11)+one(6) | 12 |
| 11 | 45 | G3.11.1ac7e59e07aa | C1 | Wp(-11)+one(6) | 12 |
| 11 | 53 | G3.11.da402f4efc61 | C2 | one(-6)+Wp(1) | 0 |
| 11 | 54 | G3.11.e1e078b6c834 | C1 | Wp(-5)+one(6) | 0 |
| 11 | 62 | G3.11.0113ef1226cf | C3 | one(-8)+W(-5) | 12 |
| 11 | 67 | G3.11.122e2719ca88 | C4 | A(-6) | 12 |
| 11 | 73 | G3.11.270590072c9d | C3 | one(-8)+Wp(1) | 0 |
| 11 | 76 | G3.11.e1ae71f5de7b | C4 | V(-2) | 0 |
| 11 | 102 | G3.11.4bfd719ee9c0 | C5 | one(-12)+Wp(1) | 0 |
| 12 | 14 | G3.12.dffd5f8f4ddc | C2 | one(-6)+Wp(1) | 0 |

All fifteen pass W'+T and fail W'+2T. Every listed shape has exactly one T. The fifteen rows represent only five distinct A shapes because the historical unit is the ordered profile/A/B record.

## 5. Scope findings and nonclaims

The coefficient visibility theorem does not require generic Gauss rank three. Its application to the fixed rank-three records is a separate necessary-condition filter. Neither 137 passing rows nor 45 rejected rows is a current complete frontier, a new live campaign total, a realization assertion, or a substitute for the original coverage theorems.

The complete retained182 note is a synthesis/index of separately proved necessary quotient classifications. I verified that the packet treats its geometric necessity as imported, not proved by JSON or by counting records. I did not re-prove the original global profile-exhaustion or the later source-transfer ledger. Those limitations are explicitly respected in Sections5–6.

The mentions of the separate profile(1,2) and profile(2,1) closures are background, not premises of this new theorem. A read-only check identified PR1134 head 7cb2e260b2bcbac15df89612b6a2096263a9c89c and PR1138 head c69f97aaf00e116e3a8abebf19a8e02868c4f7c4 as the stated separate closure submissions. This review does not independently re-review those other proofs or promote their submission status into a global theorem. No part of the new W'+2T theorem depends on them.

No profile(1,1) closure, COV theorem, global rank-three exclusion, rank-four lower bound, maximal Gauss rank, obstruction value, full-adjoint invertibility, smoothing, algebraicity, or repair of the original theorem is established by this packet. No selected actual coefficient, parameter, point, matrix, tensor, derivative, jet, instance rank, or scan was evaluated during the proof or this review. There were no public writes.

## 6. Exact reviewed packet identities

These SHA256 values bind this review to the reviewed proof and verifier/result versions. REVIEW.md itself is intentionally not included.

| File | SHA256 |
|---|---|
| PROOF.md | 1af82c4986389501c01baf0f0932bfbe5cb3a224664b127acc6e22bcdace536c |
| verify.py | 0d928a64bdd7cf3a6e8f3510accc28819dd51da9597b0385ec048d13f5c55350 |
| characters.py | 5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1 |
| INPUTS.json | 4631f131047a3b90b626aed58ab105cf2433145596673ba1e05daa56be76b74b |
| RESULT.json | 2fa68f41faf1843215b3624dd12718b567d4fb7ebe71d54cea47eb1848736423 |
| REPRODUCE.md | 479972c9459ff376baf1e37b591073e3ffcbe630205dddd2da0c9b8754bc07cd |

Final finding: PASS within the stated imported-input and historical-record scope. No repair request is outstanding.
