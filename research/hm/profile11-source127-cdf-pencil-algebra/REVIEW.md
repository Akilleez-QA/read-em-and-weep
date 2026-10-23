# Independent whole-proof review

## Verdict and exact reviewed version

**PASS, conditional on the stated actual c-d-f occurrence and the pinned actual-data theorems.** The complete proof, including the appended radical-rank corollary, is mathematically sound within its stated scope. It computes every equivariant constant endomorphism preserving the inclusion, transfers the resulting algebra covariantly to both fixed actual negative pencils, determines the radical rank triple, and gives the exact limited positive-quadratic and full-module extension boundaries. No mathematical blocker was found.

Reviewed on 2026-10-23. This is an independent written mathematical review, not proof-assistant certification. I read the complete proof and all eight immediate immutable input documents, with particular attention to the actual maps in the original sheaf notes, Section 6 of the simultaneous reconstruction, Section 5 of full faithfulness, and Sections 2–5 of the full-module theorem. The imported actual-data theorems remain hypotheses of this audit; the character checker is not being used to authenticate unprovided actual coefficient data or to replace those theorems.

This verdict binds the following exact bytes:

- `PROOF.md`, SHA256 `0d740d6f70de924b0442af71cb37e050165efbe9ab984a76f0e1e40b5d27a599`.
- `verify.py`, SHA256 `0542231119e31f0e0d02f1cf9a13b8432e28c843a4fbd23440f9062ae597bfe8`.
- `REPRODUCE.md`, SHA256 `eff6ef886794534afeca93079440ced8d43ad4adb02eb9903c258254aedd8f56`.
- `audit-inputs/manifest.json`, SHA256 `31896f46d09b5be8b8c3359450b1e4c648aabf4dced06a3f15e0f5244269b34c`.

The original frozen proof and checker were preserved as `PROOF-pre-rank-corollary.md` and `verify-pre-rank-corollary.py`, with their original SHA256 hashes `4241136d8c138733a6aa5a49652ca893315b2be1a94c3e3ab7dc9c01821efcd3` and `3e3e3bb1cf1726383777ab3522aaa0ec20c6fcb6645f2081c1112029d3d351f9`. I checked the byte diff: the mathematical proof change is only the appended Section 7; the checker adds only its fixed character and dimension checks. The verdict above is a review of the entire final combined proof, not just that delta.

## 1. Authentication and the eight precise dependency interfaces

I independently recomputed each Git blob hash as SHA1 of `blob <byte-length>\0` followed by the exact local bytes. All eight match the manifest. The references below are immutable repository URLs; the SHA256 values additionally bind the local bytes reviewed.

1. **CLASSIFICATION.md, PR923.** Commit `91af637305fd0a76b4e68a889b2a2cb59f8f7067`; Git blob `6742093385b0aefc7b678151d90e7966bf4effa6`; SHA256 `373546019cfbaa6f2a8acfd9653acc1201cb43bafaaeac90f574878ef20ab3e6`.
   [Exact source](https://github.com/Akilleez-QA/read-em-and-weep/blob/91af637305fd0a76b4e68a889b2a2cb59f8f7067/research/hm/profile11-source127-cdf-lift-classification/PROOF.md).
   The relevant conclusions are an actual constant direct-sum identification over the fixed base, and injectivity of the quartic restriction map R. Section 4 proves the required generic third-jet surjectivity of the D coefficient system; Section 5 then proves R injective by factorization and the injective coefficient map of q. This is not an inference from equal dimensions. No parameter value or actual realization is imported.

2. **NORMAL-FORM.md, PR920.** Commit `1528ff8ea56b21e03f7501a962bdaa6728a75904`; Git blob `718b5245560a84568492874bab8d8c34730e8319`; SHA256 `5cc83c225a03ba670b7859d1a64aec161611ec9cc35fffe79479fdd5b7dadf62`.
   [Exact source](https://github.com/Akilleez-QA/read-em-and-weep/blob/1528ff8ea56b21e03f7501a962bdaa6728a75904/research/hm/profile11-source127-cdf-normal-form/PROOF.md).
   Sections 4 and 7 explicitly justify the standalone derivative, all intermediate saturated kernels, the complete degree-ten line, and the actual equality B=U_6^10. Section 8 proves the full degree-eight coefficient span and complementary constant summands. These supply actual flags and coefficient spans, not just splitting characters.

3. **FULL-FAITHFUL.md, PR862.** Commit `e103e25456897a1123f9636eb20080e8641ce66a`; Git blob `e18035dcceb1c7e0d0d4356ee578937d3172390b`; SHA256 `eb468f88d6d5121fa38a695ecf9c47c97e365590ade8f122be82f0476ec8e79b`.
   [Exact source](https://github.com/Akilleez-QA/read-em-and-weep/blob/e103e25456897a1123f9636eb20080e8641ce66a/research/hm/profile11-degree28-pencil-algebra/PROOF.md).
   Only the general theorem in Section 5 is transferred. Its hypotheses are H0(E)=0 and global generation of Q(-1); it explicitly permits degree-one summands of Q and arbitrary singular pencil morphisms. None of its degree-twenty-eight algebra classifications is used.

4. **SOURCE-BRIDGE.md, PR790.** Commit `af0e03d26da5e47d18ae732291aca46f4d448dc5`; Git blob `0641ffadf54324d5520aec89767658e938815223`; SHA256 `0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4`.
   [Exact source](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md).
   Section 6 proves simultaneous identification with both original actual multiplication tensors using their original plane quotient, universal representatives, and one determinant convention. Its source2-specific block decompositions and rank conclusions are not transferred.

5. **ACTUAL.md.** Commit `db51525015bb7c5e825833d550d08dedf6f6ea96`; Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`; SHA256 `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
   [Exact source](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md).
   This supplies the actual presentation, representations, negativity, and full-span context. Its H1(Q*) character identity is not substituted for the covariant definition N2=H0(Q(-2)).

6. **GAUSS.md.** The same commit; Git blob `303c6927265296440470b9dd4015fe6e8d55ca4d`; SHA256 `0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2`.
   [Exact source](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md).
   This identifies the actual plane-section space as Koszul middle cohomology and the actual quotient by the formula [y-zx], with the original A and B. It supplies actual injectivity and surjectivity, not an abstract dimension model.

7. **UNIFORM.md.** The same commit; Git blob `d34434e3bffe4e9de4a6aaa4d5e469336b12d5d0`; SHA256 `c7de926d4b63deaa6e36d6ce9b220792cb0a5869ecb557398b381c4cc0dcc3d4`.
   [Exact source](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md).
   This proves the everywhere-exact actual quotient 0→E→30 O→D_lin(1)→0 and the actual first multiplication presentation. No quotient identification is made only from characters.

8. **FULL-MODULE.md, PR818.** Commit `f4a73af666900ad2cb34a756d24b88e19dd6feaa`; Git blob `2ba0a7eee6ef2eb5413683e85618d7902dca3970`; SHA256 `7525df1e58ac8683a5a0b828209f4f35cc79a09527307ee47b35025d5c2ad636`.
   [Exact source](https://github.com/Akilleez-QA/read-em-and-weep/blob/f4a73af666900ad2cb34a756d24b88e19dd6feaa/research/hm/negative-truncation-extension/PROOF.md).
   Sections 2–3 prove full-module scalar rigidity from the actual degree-zero generation and unique degree-one Euler relation. Section 4 distinguishes the positive-quadratic necessary test from a window lift. Section 5 proves the necessary-and-sufficient marked-submodule criterion, including its nested-pair version. The source2 numerical applications are not used.

The eight immediate dependencies are all authenticated. This is not a claim to have independently reconstructed every earlier result in their transitive citation graph.

## 2. Completeness of the constant endomorphism calculation

Write h in all nine blocks relative to C10⊕C11⊕C9. The proof exhausts these blocks without assuming h invertible.

- A bundle map F→B or F→L vanishes by ordinary degree. Thus h(F)⊂F. The coefficient span of F is C10, so both blocks from C10 to the other constant summands vanish. One can also check this span directly: F is a saturated rank-nine, degree-minus-eighteen subbundle of the ten-dimensional constant C10; a proper span would have dimension at most nine and force F to be that constant bundle, contradicting its degree.
- The induced map on C10 O/F=O(18) is a scalar a. Exactness and H0(F)=0 make C10→H0(O(18)) injective. Therefore q h=a q forces h|C10=a id, including a=0.
- Modulo C10, B cannot map to L by degree. Its full span is C11, so the C11→C9 block vanishes. This reasoning uses the actual quotient inclusion, not a presumed invariant complement.
- The C11 diagonal block preserves B and every successive negative Gauss kernel, hence its terminal full Veronese line O(-10). Its action on that line is a scalar b. Full coefficient span then gives b id on C11, with no need for b to be nonzero.
- On the final constant quotient C9, the full degree-eight line similarly forces d id.
- The remaining C9→C11 block z would induce L→B. The equivariant Hom space is zero because Sym4 W=D has neither V nor P. Hence z kills L, and full span forces z=0.
- The C11→C10 block lies in ker R and is zero by the actual injectivity theorem in CLASSIFICATION.md. The two-dimensional source of R is not being declared zero by a character count.
- Finally Hom_G(C9,C10) is precisely the one-dimensional common P channel J. For every w in it, q w|L is an invariant degree-26 form. Sym26 W=A+2V+2P+2D has no invariant, so this composite vanishes identically and w|L factors through the actual kernel F. Every such w therefore preserves E. A nonzero w cannot kill L because L spans C9, so this is a genuine radical arrow.

The resulting formula h(c,x,y)=(ac+w(y),bx,dy) is therefore necessary and sufficient, not merely a family of allowed automorphisms.

### Singular-map naturality and saturation

For a constant map h preserving a saturated subbundle S of a constant bundle, the induced quotient map satisfies β_S(hs)=h_bar β_S(s). This follows from h commuting with the trivial connection; no inverse occurs. Thus h preserves ker β_S. Repeating the same argument for that kernel proves preservation of the whole flag. If a kernel is described as a saturation, preservation persists: locally, f s in the unsaturated subsheaf implies f h(s) lies there, and the saturated quotient is torsion-free. Neither equality of images nor equality of ranks under h is needed. This validates the diagonal-scalar argument for all singular h.

## 3. Algebra structure and orientation

Rightmost-first composition gives (aa',bb',dd',a w'+d' w), exactly as stated. The isolated b vertex and the arrow C9→C10 identify the algebra with C×T(J), dim J=1, in the stated covariant orientation.

The ideal J is square-zero and the quotient is C^3. A nilpotent ideal lies in the Jacobson radical, and the semisimple quotient forces the reverse inclusion. Commuting with the vertex idempotents kills a central radical component; commuting with nonzero J forces a=d while leaving b free. Thus the radical and center assertions are exact. The units have a,b,d nonzero, with torus conjugation weight a/d on J. The statement about ambient-frame ambiguity does not claim a family-level or moduli-scheme trivialization.

## 4. Covariant transfer to the entire fixed-variable commutant

The quotient is O(18)⊕S O(7)⊕(Wp+T)O(1). Its twist by minus one is globally generated, including the degree-zero residual summands, and H0(E)=0. Consequently the weaker full-faithfulness theorem applies exactly as written. A stronger hypothesis excluding degree-one quotient summands would be unavailable and is correctly not imported.

The natural evaluation sequence reconstructs Q(-1) from N2 and N3. The Koszul cokernel reconstructs H0(Q), and the surjective connecting map reconstructs H as its kernel. An arbitrary intertwining triple therefore induces a constant h preserving E everywhere. The proof recovers e2 by injectivity of multiplication by a nonzero linear form and recovers e4 by the surjective boundary. These constructions preserve addition and composition and do not require any e_i to be invertible.

The actual-source identification is simultaneous. In the original quotient, [(x,y)] maps to [a y-b x]. With t_l=βa−αb, the universal representatives in SOURCE-BRIDGE.md give A_rec,t_l=A_l, and t_l m is represented by (αm,βm), giving B_rec,t_l=B_l through the same descended (B_u,B_v). The two identifications use one determinant/sign convention and the same actual quotient; they are not independent representation isomorphisms. Constant changes of normal-form coordinates induce simultaneous pencil gauges over the identity of the fixed base, not changes of the negative variables.

In particular N2 is H0(Q(-2)) covariantly. The character equality with an H1(Q*) description elsewhere is not used to reverse maps or to turn this algebra into an opposite algebra.

## 5. Full-module and positive-quadratic boundary

The grading N2=K3+, N3=K4−, N4=K5+ agrees with FULL-MODULE.md. The unique Euler relation is the coevaluation tensor in T_coord⊗K0. Its preservation forces a degree-zero generator map to be scalar, and generation in degree zero forces that same scalar on the entire module. This is not a bundle-simplicity argument or a statement only about a three-degree window.

Because N is nonzero, restriction has zero kernel and image exactly the common scalar line. Therefore C_N/(C id_N) is a three-dimensional **vector space** measuring this precise lifting question. It is not an Ext group, an algebra quotient, or an evaluated compatibility rank. Nonzero radical maps and proper block projectors fail to lift, but their presence is consistent with occurrence of the smaller negative pencil.

The marked-submodule criterion has a separate proof and scope. For a negative subpencil U, the minimal module generated in actual degrees 3,4,5 has degree-five positive part

    Sym²(T_+)U2 + Sym²(W)U2 + WU3 + U4.

The last three terms lie in U4 by negative-pencil stability. Thus the positive-quadratic condition is necessary and sufficient for the prescribed three marked intersections, without requiring a retraction, direct summand, or control in other degrees. Applying this to nested subpencils uses their nested minimal spans, not a lifted projector.

## 6. The radical P-channel and its exact conditional meaning

The displayed cohomology blocks follow from H0(Q(-2)) and H1(E). Their dimensions are respectively (17,24,0) and (9,21,7), totaling the actual 41 and 37. The radical quotient arrow is Q_L→Q_F. Since H0(Q_L(-2))=0, j2=0.

On E the nonzero radical map is L→F. Degree-six equivariant Hom spaces leave only L→P(-2), with a one-dimensional choice, and exclude D(-2). Its nonvanishing follows from the full span of L and the nonzero original constant w. Keeping dual arrows explicit, Serre duality identifies the dual H1 map with a nonzero coefficient injection P*→H0(O(6)); self-duality labels this the unique P constituent of Sym6 W=V+P. Thus j4 is the nonzero P projection from the scalar-block V+P to the top-block P+D, and its kernel within the scalar block is exactly V.

The positive-quadratic commutator Θ_+(e)=e4 q_+−q_+(1⊗e2) is linear and vanishes on common scalars, so it factors through the stated vector-space quotient. For the radical it equals j4 q_+. Its vanishing is therefore exactly the vanishing of the P component of the scalar-target block of q_+, equivalently containment of im q_+ in the intrinsic common radical kernel on N4. This condition survives a change of normal form or a nonzero rescaling of j. The diagonal formulas and their sum with the radical term have the correct target-minus-source signs.

Since J²=0, JN⊂Ann_J N. The radical-image subpencil has U2=0, so its marked-submodule condition is automatic. The common-kernel subpencil has Vker2=N2 and Vker4=ker j4, so its condition is precisely Θ_+(j)=0. Accordingly the nested marked pair exists exactly under that one conditional vanishing. The proof neither proves nor disproves the vanishing of this q_+ channel and does not assert a rank for Θ_+.

## 7. Audit of the appended rank triple

The appended argument is sound, including both nonzero middle channels.

1. Twisting the actual quotient sequence by O(-1) gives the natural covariant isomorphism H0(Q(-1))≅H1(E(-1)), since both cohomology groups of H O(-1) vanish. Naturality of the connecting morphism identifies j3 with H1 of the original L→F map, twisted by minus one. This is not an arbitrary self-dual identification of N3.
2. The dual map is H0(F*(-1))→H0(L*(-1)). Its only possibly nonzero component is P*⊗H0(O(1))→H0(O(7)), given by multiplying the same P*→H0(O(6)) coefficient injection. With the fixed self-dual representation notation this is precisely P⊗W→Sym7 W. Its D⊗W component is zero.
3. The full multiplication Sym6 W⊗W→Sym7 W is onto with kernel Sym5 W=T, of dimension six. The kernel is **not** S. Since Wp does not occur in T, the restriction to the Wp summand of P⊗W=Wp+T cannot vanish. Duality then gives a nonzero Wp channel of j3.
4. The T channel cannot vanish either. For every nonzero l, the actual B_l is onto and B_l j3=j4 B_l. Therefore B_l(im j3)=im j4, a four-dimensional space. If only the Wp channel of j3 survived, its image would have dimension two, contradicting that surjection. This step uses actual uniform surjectivity and the already-proved rank-four j4, not a selected l or a computed tensor matrix.
5. The only domain block for j3 is N3,L=Wp+T. Nonzero maps on these two inequivalent irreducibles are injective on each, with disjoint images. Hence rank j3=2+6=8. Together with j2=0 and rank j4=4 this proves (0,8,4) for every nonzero j. Since dim J=1, the joint image and common kernel have dimensions (0,8,4) and (41,46,33).

This is a universal conditional rank theorem for the represented radical. It does not compute the actual positive-quadratic map, evaluate a source instance, or prove an extension to the full module.

## 8. Reproduction and final limits

I ran `python3 verify.py` on the exact final checker. It returned PASS. Independently checked hashes agree with all eight blob identities and the final proof/checker hashes above. The checker uses exact arithmetic in Q(sqrt(5)), fixed small character recurrences, the stated Hom vanishings, cohomology characters, invariant-free degree 26, and the corrected Clebsch–Gordan kernel. It supplies useful finite verification but does not prove singular-map naturality, full span, sheaf saturation, actual-source identification, full faithfulness, or the extension theorem; those were audited in the written arguments.

No selected actual HM/source coefficients, parameters, points, derivative values, matrices, or instance-rank tests were used in this review, and no large computation was performed. No external write or publication was made by the reviewer. The frozen mathematical proof and verifier were not edited by the reviewer.

The final theorem remains conditional on actual c-d-f occurrence. It does not decide whether any parameter in the abstract family is realized, whether the relevant q_+ P-channel vanishes, what rank Θ_+ has, or whether a positive-quadratic-compatible map extends even to the five-variable window. Full-module scalar rigidity cannot supply any missing forced-extension premise. The conclusion changes no source count, excludes no source or stable label, and does not establish the global rank goal.
