# Independent review of the source127 a-c-e-f exclusion

## Verdict and exact scope

**PASS.** The frozen proof establishes impossibility of the entire original edge

    G3.11.cce6e3ba4eeb, source_index127,
    (1,0,1,0,1,1,0,0), original defect zero,
    E=(P+D) O(-2)+Wp O(-3)+V O(-4)+Wp O(-5)+O(-8),
    A_q=O(-8)+O(2)+O(16), B_q=O(-18)+O(-4)+O(6).

No blocking mathematical gap or required correction was found. In particular, the proof does not discard the degree-thirteen Wp covariant, the nonzero negative scalar row, or the new allowed Wp(-3) injection channel. It proves the actual interfaces needed to apply the two dual obstructions.

This verdict is for the exact two files below and the established actual-input interfaces specified in the proof. It is not a whole-label exclusion, a global frontier count, a realization assertion for another source, a claim about the separate c-d-f family, or proof-assistant certification. No publication was performed and neither frozen file was edited.

Review date: 2026-10-23 UTC.

## 1. Hash-pinned material and execution record

The reviewed SHA256 hashes are:

| File | SHA256 |
|---|---|
| PROOF.md | ee9ddd1e3f26941e0007c7e818151439e6e10f4a3340fd537f91b73331ea8a8a |
| verify.py | 31ddbdc128aaa92cfd8e4f7960195e48e0b8aab238ede05177ef613c28931191 |
| audit-inputs/manifest.json | bb9dae96277b4c734a45ecabf1020d59d5099a033457a64cdbc7e5a429498980 |

All eight supplied inputs were read where relevant, and their exact Git blob identities were authenticated against the manifest. The original catalogs were inspected at the exact entry and stable label, not merely searched for a matching degree.

| Input | Git blob | SHA256 |
|---|---|---|
| ACTUAL.md | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 | a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 |
| STRICT-TOP.md | d7506dae49b4be43230450c4132bd5db91f137ef | 53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08 |
| pairs.json | fe0afa410d89340d3082dc814277f89fbb582c19 | 6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb |
| frontier.json | 8b5971092f9ef762584912609fd5e9301c4e271d | a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad |
| PR859.md | 79ec9cd555997cb9e3b8dc76f3b64fa3f836ad2e | 0477e228a7253400fc80c58e484157a23cbadce559dcf252758155191f490f5f |
| PR867.md | 76a6bd75b77232af222ccb91555499b4a4437311 | 10030e0f7acc9ac4bb35efb29356c2a85132b88876983d58b8a359d2c660e07f |
| PR885.md | 3d473e81c158e45c923a1177e71701c40ac477c5 | 3e3a994defbeea2cefff4b0a64a93f70e0059417f8850a79d85069c1d45ab169 |
| PR888.md | 335e2a3acc3e67fbeb0d8e3970134146e25afa8b | 1740dd7bb504cb49c726952373f74700e3396b7a8a94a1f89e7e3f6121775e38 |

The first four sources are pinned at db51525015bb7c5e825833d550d08dedf6f6ea96. The four later proof commits are, respectively, 6129e92a26572779003f3295227f688b77ed881c, b2a12c98bc162062a938b7a7a6a90ab45786e340, 53939364de5459822be1a32be08f2b12dbbb4280, and e9908b1d42d59c844abdb79bc734117a041f3d04. The exact paths and immutable URLs are in the pinned manifest.

I also inspected the underlying mathematical dependencies used for the saturated image, first-polar, and degree-38 interfaces. Their local bytes were checked against the separate existing dependency manifest:

| Dependency | Commit | Git blob | SHA256 |
|---|---|---|---|
| PR796 | d2b43060c83328dd5118aee6b9288fcfa0c873ac | 46a0de762000f21182f6d3168f3ecfd63adaf75f | 622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1 |
| PR802 | e484640a6565c278321bf6557860262c1ac1b7df | 98a1bd6123e148476da0b997d879aecbf885ec97 | a18a6990f719592d71853692157161a9ca5fe6b7f2a78edacbfa060bb3513459 |
| PR870 | 3a05d057a12d24d62bf3c8e0e96fa778a4022ad5 | cfc219e5ce5c0658c484bfef21c3c90bd2d45468 | 0075805e34bdf0746a1a20cb95110144655080b6c5dfa294e23f81c6b0627895 |

Executing the frozen `python3 verify.py` returned PASS. I separately implemented a small integer representation-ring check using multiplication by W and the recurrence Sym(n+1)=W Sym(n)-Sym(n-1), without importing the frozen verifier's character values or arithmetic. It independently reproduced:

- the full rank-three kernel classification;
- every Hom component into the changed internal target;
- every first-polar rank, degree, constant coefficient and linear coefficient;
- the saturation-related covariant vanishings;
- the new C8 injection obstruction;
- the twelve-atom PR888 support list and both residual cohomology identities.

The independent classification starts with only 17 abstract rank-three splitting candidates. Four contain a forbidden scalar degree-minus-four block, leaving the 13 candidates of PR867; eight pass the first character and exactly five pass both characters. This is a bounded check of fixed abstract representations, not a source-instance scan.

The verifier's PASS is not being substituted for proof of saturation, intersections, or connection compatibility. Those were checked mathematically below.

## 2. Original source and dependency interfaces

The original tuple decoder gives no V(-2) coefficient, one P(-2), one D(-2), and precisely the four displayed lower blocks. The total rank and degree are 17 and -54. Entry127 and the frontier object agree on A_q, B_q and zero original defect.

The actual presentation gives the negative dual bundle Q* of rank13 and degree-54, with H1(Q*)=M2. Strict-top applies to Q* because H0(Q*)=0, so H0(Q*(1)) injects into H0(B_q(1))=Sym7 W=Wp+T. The argument never substitutes H0(Q*(1))=0 or an interior-stage condition on E^+.

Original zero defect identifies the actual raw derivative image with the saturated A_q in Q(-2). Consequently A2=A_q(2) and its L=O(18) summand are genuinely saturated. This justifies all later high-line intersections and constant projections.

PR859 explicitly includes this a-c-e-f tuple. Its proof of basepoint-freeness treats the degree-twelve common-divisor branch before saturation and then proves its saturation defect zero; it does not silently replace the residual O(4) image by O(16). Its profile-free polar contradiction therefore applies to the exact source under review.

PR867 Section2 classifies the high-P kernel using only its rank, degree, parity, and two characters. Its subsequent c-d-f-specific internal exclusions are not transferred. PR885's Section8 is used only through its stated constant-space, rank/degree, span and original-dual-endpoint interface. PR888 is used through its Sections1-4 scalar-row geometry, not through the title or whole h-b-f exclusion.

## 3. Complete kernels, changed internal maps, and saturation

For F=P(-2), the lower external rows vanish and the high map is onto O(16). Strict-top gives H0(K0(2))=0, rank K0=3, degree -24, and

    H1(K0(2))=A+V+P+D,
    chi(K0(3))=-(W+S+T).

The five kernels in the proof are exactly the five survivors of the complete rank-three classification. No possible higher-dimensional coefficient can occur in a rank-three bundle, and central parity and the no-section condition bound the scalar and two-dimensional forms exactly as in PR867.

The full changed target is

    D(-4)+Wp(-5)+V(-6)+Wp(-7)+O(-10).

I checked every component from every kernel atom. The proof's list (5) is complete and every listed Hom space is one-dimensional. In particular O(-18)->Wp(-5) exists and is a degree-thirteen Wp covariant; replacing it by a T covariant would have been incorrect, but the reviewed proof does not do that.

The nonzero D maps have the asserted saturated universal images:

- A(-8) surjects by the Euler map onto W(-7), which injects into D(-4) by multiplication by the tautological cube.
- W(-7) itself injects by that multiplication.
- W(-9) surjects onto O(-8), followed by the tautological fourth-power line.
- O(-8)->D(-4) is that saturated fourth-power line.

The same-degree scalar maps are zero or isomorphisms. In case IV, any common divisor of a nonzero D covariant of degree14 or Wp covariant of degree13 is invariant. If nonempty its degree is at least12. Dividing would require D in Sym(n) for 0<=n<=2, or Wp in Sym(n) for 0<=n<=1, respectively; all these spaces are zero. Thus each nonzero component is saturated. A combination with at least one saturated component remains a saturated line in the direct sum. The other simultaneous images land in distinct direct summands and are saturated direct sums.

This proves the complete image list (6), including zero images, before invoking the internal/external image lemma. That lemma then really does give the two exact sequences (7) with no hidden divisor.

## 4. Every first-polar alternative is accounted for

First polars of the actual quadratic F generate its raw first span. Since the preceding step proves that raw span saturated, M(1) is globally generated and M has only degrees0 and -1. The relevant numerical and character consequences are:

| Internal J | rank M | degree M | Result |
|---|---:|---:|---|
| 0 | 5 | 10 | Impossible in a constant bundle |
| O(-8) | 6 | 4 | Impossible |
| O(-10) | 6 | 2 | Impossible |
| W(-7) | 7 | 0 | M=(V+P) O |
| W(-7)+O(-10) | 8 | -8 | M=(Wp+T) O(-1) |
| O(-18) | 6 | -6 | M=T O(-1) |
| O(-8)+O(-10) | 7 | -4 | Constant A, linear character Wp+T-S, impossible |

The last row is a representation contradiction, not merely a negative degree count. The three retained M types are therefore exhaustive.

## 5. The actual constant seven-space projection is valid

For M=(V+P) O, the actual derivative-image exact sequence gives M/N=L and N/F=W(-5), with N=E intersect M. Thus E+M is saturated in H O. This is what permits constant projection by M; an abstract splitting alone would not suffice.

The only map from W(-5) into E/F is its D(-2) component. This is the saturated tautological-cube injection and its quotient is A O. The projected E/N therefore has the displayed A O summand and residual lower blocks. The A summand is an actual constant subspace in the projected ambient constant bundle, since its inclusion has degree-zero source. Projection by it is again legitimate.

Under the first constant projection the raw quotient loses precisely L; the second projection removes a horizontal subbundle already in the projected source and does not remove an additional derivative row. The residual Z is saturated and has actual raw derivative quotient O(2)+O(-8).

Its top Wp(-3) has zero external derivative: Wp is absent from Sym5 W, and the negative row is too low. Its internal derivative into V(-6)+Wp(-7)+O(-10) is zero by degree. Hence this actual negative subbundle is preserved by the original constant connection. Its Grassmannian map has zero differential, so it must be a degree-zero constant subbundle in characteristic zero, contradicting degree -6. This excludes M7 without assigning a connection to an abstract complement.

## 6. C9 and full C12 are the correct rank-eight alternatives

Here the first-polar map P W O(-1)->M is an isomorphism, since it is onto between equal-rank, equal-degree bundles. The full constant span C of F and M is a quotient of P Sym2 W=V+P+D. A negative rank-eight bundle cannot have a constant span of dimension eight, so dim C>=9. The only possible quotient dimensions are consequently nine (P+D) and twelve (V+P+D).

These are identifications of the actual coefficient map. For C9 its kernel on P Sym2 W is V; together with the alternating P in P W W, the linear coefficient kernel is V+P. This explains M^-=(V+P)(-2), while the rank-one quotient C/M has degree8 and hence is O(8). It is not necessary to assume that an arbitrary equivariant linear embedding of an abstract M has this form.

For C12 the quadratic coefficient map is an isomorphism onto its full image, yielding the complete quadratic Euler sequences

    M/F=P O, C/M=P O(2), M^-=F,
    beta_M: M/F -> (C/M)(-2) an isomorphism.

The intersection N is saturated in M and has rank7, degree-26 and N/F=W(-5)+O(-8). In C9, containment N subset M^- would force equality by saturation and equal rank, which is impossible, in particular because it would supply the absent V(-2) top coefficient to E. Otherwise differentiation of N fills the line C/M generically. Together with F^+=M and saturation, this puts C in E^+.

The lower rows of C then vanish, so E intersect C has rank8 and degree-18. Its degrees are at most-2; the degree-minus-two coefficient has dimension6 or7. It must inject into the multiplicity-free P+D top of E, whose subrepresentation dimensions are0,4,5,9. This is a contradiction.

In C12, the isomorphism beta_M transports the saturated N/F to a saturated quotient of C/M. Hence Y=N^+ really is saturated and has

    Y/M=W(-3)+O(-6), rank Y=11, degree Y=-20,
    C/Y=O(20).

If C were in E^+, its lower rows would vanish through the quotient P O(2), and its high-only kernel in E would have rank11 and degree-18, violating the degree-at-most-minus-two bound. Thus E^+ intersect C=Y, because Y is already saturated of codimension one in C.

The O(4) row of Y is zero. The negative O(-6) row vanishes on M and W(-3), but the equal-degree scalar row on O(-6) is allowed. The high row is onto L already on M. These are exactly the two branches required next; no negative row is lost.

## 7. The scalar-zero branch has the exact degree-38 interface

When the scalar row is zero, X=E intersect C has rank10 and degree-38, and C/X is an extension of O(20) by L. The same type of interface arises later with c=8 and rank X=6.

For arbitrary c in these two applications, E/X has rank19-c, degree-16, and full constant span H/C of dimension30-c. The projected image and C/X in Q have the same cokernel, hence the same torsion saturation length delta. The dual-section span bound gives

    35-c-delta >=30-c,

so delta<=5. Invariance and the minimum positive divisor degree12 force delta=0. This verifies, rather than assumes, saturation in both applications.

The two equivariant extensions are O(18)+O(20) and W O(19). For R=(Q/(C/X))* the original presentation then gives rank11, degree-16, H1(R)=D and

    chi(R(3))=-W+Wp+S+4T.

The entire H1=D support is D(-2) or O(-6), with remaining atoms of degree-1. The former requires a nongenuine linear coefficient; the latter forces the linear coefficient 2Wp+T. Thus H0(R(1))=2Wp+T would inject into H0(Q*(1)), which injects into Wp+T. This is impossible. PR885 Section8 therefore applies without any source-specific lower-splitting assumption.

## 8. The PR888 scalar-nonzero interface is genuinely reproduced

All hypotheses used by PR888 Sections1-4 have now been proved for the new source: the same actual A2 and dual endpoint, the same original presentation and ranks, full constant span C=V+P+D of F, M=(Wp+T)(-1), the saturated Y and E^+ intersection, zero middle row, nonzero scalar negative row, and onto high row already on M. PR888 does not use the h-b-f lower splitting once these facts are supplied.

Taking the actual kernel of the negative row first gives a saturated Y0 with Y0/M=W(-3), rank10 and degree-14. Only then is X formed as the kernel of Y0->L, giving rank9 and degree-32. This order is essential and is respected.

The rank-two quotient V0=C/Y0 is globally generated. Since F spans C, H0(V0*)=0, so both its ordinary degrees are strictly positive. The five possible center-even rank-two degree14 splittings are exhaustive. Their Euler characters select only Wp O(7). The resulting extension by O(18) splits equivariantly, giving

    U0=C/X=O(18)+Wp O(7).

Saturation is not imported from its splitting. The projected E/X has rank8, degree-22 and spans an eighteen-space, so its shared defect satisfies delta<=12. Invariance leaves delta=0 or12. At delta12, the dual residual is rank10, degree-10, and all degrees at most-1, so h0(R(1))=10. This contradicts the original dimension-eight strict-top bound. Thus U0 is saturated.

For the saturated residual, exact cohomology gives

    rank R=10, degree R=-22,
    H1(R)=V+P+D, chi(R(1))=-W.

The atom list in the proof is exhaustive under (j-1)dim B<=12 and center parity. I independently checked all twelve atoms. None contributes W to H1(R(1)); degree-minus-one atoms contribute only nonnegative multiplicity to H0(R(1)). The W coefficient of chi(R(1)) cannot be -1. This proves the nonzero scalar-row contradiction through the exact extracted interface, not an unproved transfer of the earlier whole-source theorem.

## 9. The C8 case and its new injection check are sound

For M=T(-1), the linear coefficient kernel contains P because beta_M kills F. The decomposition T W=V+P+D and the fact that a negative rank-six bundle spans at least seven constants force kernel P and full span C=V+D of dimension8. Since T=Wp Sym2 W and V+D=Wp Sym3 W, this is the complete cubic Euler sequence tensored with Wp. Hence

    M^-=F, M/F=Wp O(1), C/M=Wp O(3),
    beta_M an isomorphism between these quotients after twisting.

The saturated N/F=O(-16) gives saturated Y/M=O(-14), rank Y=7, degree Y=-20, and C/Y=O(20), by the same actual-image argument as in C12.

If C were in E^+, its lower rows would vanish through Wp O(3), and X=E intersect C would have rank7 and degree-18. Then X/F of rank3 and degree-10 injects into

    D(-2)+Wp(-3)+V(-4)+Wp(-5)+O(-8).

It has no degree above-2 by the target bound, and no degree-minus-two coefficient because a coefficient of dimension at most3 cannot map to the irreducible D at equal degree. Thus its degrees are at most-3, forcing precisely (-3,-3,-4). Equivariant splitting and center parity force a trivial-coefficient O(-4) direct summand. Every equivariant map from this line to the displayed target is zero: D is absent from Sym2 W, Wp is absent from Sym1 W, V has no invariant, and the other targets are too low.

The Wp(-3)->Wp(-3) component is indeed nonzero and allowed. It cannot remedy the zero map on the obligatory O(-4) companion. Thus the injection is impossible for the correct reason, and C is not contained in E^+.

Consequently E^+ intersect C=Y. Its lower rows factor through O(-14) and require invariant degrees18 and8, both absent. The resulting X has rank6 and degree-38 and satisfies precisely the already checked obstruction in Section7. This excludes the last first-polar alternative.

## 10. Corrections, limits, and final assessment

No correction to the frozen proof or verifier is required for the stated conclusion. Two distinctions should be retained in any later reuse:

1. C9 and C12 come from the actual quadratic coefficient map of F, not from an arbitrary abstract embedding of the split bundle M.
2. PR888 applies after reconstructing its full saturated scalar-row interface. Its earlier source-specific theorem by itself would not justify the transfer.

The frozen text respects both distinctions. The review spells them out to make the scope of the accepted argument explicit.

The computations were limited to immutable-input authentication, original-catalog identity reads, and bounded universal representation arithmetic. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans, or large computation were used. All actual connection, saturation and intersection claims are justified structurally.

**Final verdict: PASS for the entire displayed a-c-e-f source127 edge, and only that edge.**
