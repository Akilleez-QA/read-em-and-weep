# Independent review: split-bf rank-two nonzero-channel exclusion

## Verdict and exact reviewed version

**PASS.** The argument excludes the nonzero internal-derivative branch of the generic-rank-two top map for precisely

    G3.11.863639aa192e, source_index69,
    tuple (0,1,0,0,0,1,0,1).

Reviewed file: `SPLIT-BF-RANK-TWO-NONZERO-CHANNEL.md`.

Reviewed SHA256:

    d762e23c6b402bf8bfd62160e310ecacf601a910d47f6a3e278cd8a3806657f6

Review date: 2026-10-23 UTC.

The quartic subsystem argument of PR819 is applicable here, but not merely because its final balanced-target theorem was previously reviewed. The hypotheses of its universal constant-coefficient and evaluation-sequence arguments have been independently checked for the split target below. No balanced-target endpoint conclusion is imported. No mathematical blocker remains in the displayed version.

The rank-one top image in O(6) is not excluded by this review. Neither the entire source nor the entire stable label is declared impossible.

## 1. Public pins and scope of verification

The original source data are at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

of `Akilleez-QA/read-em-and-weep`, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The supplied immutable copies have the following independently recomputed Git blob identifiers:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.

The designated frontier record gives the stated label, source_index69, profile (1,1), original defect zero, and

    A_q=O(-10)+O(4)+O(6),
    B_q=O(-8)+O(-6)+O(8).

The zero-based quotient record 69 contains the stated tuple. Its source decoding gives

    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10).

The relevant public proof pins are:

1. PR796, commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, Sections 3 and 5, for saturated derivative images and the bounded V+P kernel support. The checked proof copy has Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`.

   https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

2. PR799, commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`, Section 4, for first-polar generation. The checked proof copy has Git blob `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1`.

   https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md

3. PR814, commit `1f94be65b3a470a1b594e61d56df7f6057c9d907`, `PROOF.md`, SHA256 `f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc`. This provides the source-wide top-kernel calculation and the separate exclusion of the zero internal channel for a rank-two bf top map.

   https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

4. PR819, commit `03fee9278072f9ac00a5fcee5deb04b7fce61ae5`, `BF-SUBSYSTEM.md`, SHA256 `087d0b78196b7c0d5e773375e603359450e0e9fb0ebb3003734c44eea4e133b9`. Only its universal coefficient-kernel and full-evaluation classification in Sections 2–3 are reused; their split-target hypotheses are verified here.

   https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BF-SUBSYSTEM.md

Both displayed SHA256 dependency hashes were recomputed and match. The checks here use the immutable copies and universal deductions; they are not a claim to have repeated an external publication or remote read-back.

## 2. Split-target surjectivity and the exact kernel budget

Work over C with the binary icosahedral group G. Let W be its defining two-space, Wp the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P the remaining even irreducibles of dimensions three and four. All these representations are self-dual. The central involution acts trivially on E. The group has no nontrivial one-dimensional characters, and every nonempty invariant divisor on P1 has degree at least twelve.

Set F=(P+D) O(-2). It is the actual saturated top subbundle of E and hence of the original constant ambient bundle. Its quotient map has no component into O(-10), by ordinary degree. Write

    p:F -> U0=O(4)+O(6).

Generic rank two is a hypothesis, not a conclusion inferred merely from the nine-dimensional coefficient space. Strict-top vanishing H0(E^-(2))=0 makes

    P+D -> H0(U0(2))=Sym6 W+Sym8 W=V+2P+D

injective. If S0 is the rank-two image sheaf and delta is the torsion length of U0/S0, then S0(2) is globally generated as a quotient of (P+D) O. Its H1 vanishes and Riemann–Roch gives

    9 <= h0(S0(2))=16-delta.

Thus delta<=7. The determinant torsion divisor is invariant, so it is empty. In particular p is onto everywhere; the argument establishes the required actual saturation.

For K0=ker p, the exact sequence at twist two gives H0(K0(2))=0 and

    H1(K0(2))=V+P.

At twist three,

    chi_G(K0(3))=(P+D) tensor W-Sym7 W-Sym9 W=0,

since both positive expressions are Wp+S+2T. Every degree of K0 is at most -3. A block Z O(-j), j>=4, contributes Z tensor Sym^(j-4) W to H1(K0(2)), with dimension (j-3) dim Z<=7 and the required central parity. The only possibilities are

    V O(-4), P O(-4), Wp O(-5), O(-10),

with respective H1 contributions V, P, P, V+P. Their H1 contributions at twist three are 0, 0, Wp, T. Consequently the genuine degree-minus-three coefficients forced by chi_G(K0(3))=0 give exactly

    (V+P) O(-4),
    Wp O(-3)+V O(-4)+Wp O(-5),
    T O(-3)+O(-10).

Each has rank seven and degree -28. The dimension/parity bound rules out additional negative blocks; thus the list is complete rather than only a list of examples.

The internal derivative targets

    (E/F)(-2)=T O(-5)+O(-10)+O(-12).

For the first two kernels all components vanish by degrees, except the possible constant Wp-to-T component, which vanishes by inequivalent irreducibility. For the last kernel only O(-10) can contribute. Its allowed maps are the unique complete-quintic tautological channel into T O(-5) and the scalar channel into O(-10). A nonzero quintic channel is nowhere zero as a line inclusion; a nonzero scalar channel is an isomorphism onto its summand. Every nonzero combination therefore has saturated image O(-10).

This proves directly for the split target that the assumed nonzero internal image is precisely J=O(-10).

## 3. All hypotheses for the linear first transform hold

The original defect zero identifies A_q with the saturated derivative image in Q(-2), where Q=(H O)/E. Its direct summand U0 is saturated there. The actual derivative image I of F therefore fits into

    0 -> J -> I -> U0 -> 0.

Here J is saturated in (E/F)(-2), and U0 is saturated in Q(-2). The quotient by I is an extension of their locally free complementary quotients. Thus I is saturated in (H O/F)(-2), with no torsion correction. This is exactly the profile-free proof of the derivative-image lemma; it does not require the external quotient to have rank one or to be balanced.

After twisting by two,

    0 -> O(-8) -> M/F -> O(6)+O(8) -> 0,
    M=F^+,
    rank M=12, degree M=-12.

Because the raw derivative image has already been proved saturated, the quadratic first-polar map surjects onto the actual M. Hence M(1) is globally generated. M is also saturated in the original constant ambient bundle, so every ordinary splitting degree of M is either -1 or 0.

The equivariant Euler characters are independently consistent:

    chi_G(M)=-(P+D)-Sym6 W+Sym6 W+Sym8 W=0,
    chi_G(M(1))=-Sym5 W+Sym7 W+Sym9 W=Wp+S+T.

The first identity and the allowed degrees eliminate all degree-zero summands. The second fixes the full coefficient representation. Therefore

    M=U1 O(-1), U1=Wp+S+T.

This establishes, for the split target, every required input to the universal PR819 argument: an actual saturated quadratic F, its actual saturated first transform M, the pure linear splitting with coefficient U1, and the unchanged ambient constant connection. Neither H0(E^+)=0 nor any balanced-target endpoint quotient is needed.

## 4. Constant relations are exactly the actual Gauss kernel

Let C be the constant coefficient span of M and let

    a:U1 tensor W -> C, K=ker a.

The tautological sequence on P(W), with L=O(-1), is

    0 -> U1 tensor L -> (U1 tensor W) O
      -> U1 tensor (W/L) -> 0.

The actual subbundle condition for M says K O intersects U1 tensor L trivially at every fiber. Projection therefore identifies K O with the kernel of the induced map from U1 tensor (W/L) to (C O)/M. Since det W is trivial, the canonical derivative identifies L with (W/L) tensor Omega1. Tensoring the preceding kernel with Omega1 consequently gives the actual embedded identity

    M^-=K O(-2).

It is a saturated kernel, not merely a generic or abstract splitting identification. First derivatives of a linear bundle also recover its entire coefficient span, so M^+=C O.

Since derivatives of F lie in M, the actual subbundle F lies in M^-. Their degree-minus-two presentations make this an injection of constant representations P+D into K. Meanwhile

    U1 tensor W=A+V+2P+2D.

A saturated rank-twelve negative bundle cannot fill a twelve-dimensional constant span: otherwise its quotient in that span would be both torsion-free of rank zero and nonzero by degree. Hence dim C>=13 and dim K<=11. By semisimplicity, after removing the injected P+D, the remaining part of K is a subrepresentation of A+V+P+D and has dimension at most two. None of the latter irreducibles has such dimension. Therefore

    K=P+D,
    C=A+V+P+D,
    dim C=15,
    M^-=F.

All statements are about the actual embedded subbundles. No connection was assigned to an arbitrary splitting complement.

## 5. Independent exhaustive quotient classification

Put Q_C=(C O)/M. It is locally free because M is saturated, globally generated, of rank three and degree twelve, and center-even because C is center-even.

A degree-zero direct summand would produce a nonzero constant functional on C vanishing on M, contrary to the definition of C. Thus its degrees are positive. Furthermore H0(M)=H1(M)=0 identifies C with H0(Q_C), making its quotient presentation the complete natural evaluation sequence.

For a positive block R O(d), the full evaluation kernel is

    R tensor Sym^(d-1) W O(-1).

Its backward kernel is R tensor Sym^(d-2) W O(-2) when d>=2 and is zero for d=1. In the full evaluation direct sum, a degree-one block of M cannot be recovered by the forward transform of M^-. But here

    (M^-)^+=F^+=M.

Thus Q_C has no degree-one summand either.

There are exactly nine center-even, rank-three, degree-twelve splittings with all degrees at least two:

    Q_C                         H0(Q_C(-1))
    O(2)+O(2)+O(8)             2W+Wp+T
    O(2)+O(4)+O(6)             W+S+T
    3 O(4)                    3S
    W O(3)+O(6)               W+S+T
    Wp O(3)+O(6)              2T
    W O(5)+O(2)               W+S+T
    Wp O(5)+O(2)              W+S+T
    A O(4)                    W+S+T
    V O(4)                    Wp+S+T

For completeness of the list: three rank-one coefficient blocks have even degrees, giving only (2,2,8), (2,4,6), or (4,4,4); a rank-two odd coefficient W or Wp has odd degree 3 or 5, paired respectively with a line of degree 6 or 2; a rank-three irreducible is A or V and has degree 4. Perfectness and central parity leave no other coefficient types.

The characters can be rederived from the bounded universal tensor identities

    W W=1+A, A W=W+S, S W=A+D, D W=S+T,
    T W=D+P+V, P W=T+Wp, Wp W=P, V W=T,

together with Sym^(n+1) W=W tensor Sym^n W-Sym^(n-1) W. In particular

    Wp tensor A=T,
    Wp tensor D=S+T,
    A tensor S=W+S+T,
    V tensor S=Wp+S+T.

The full evaluation presentation identifies H0(Q_C(-1)) with the coefficient representation U1 of M. Thus only the last row is possible:

    Q_C=V O(4).

No property of O(4)+O(6) versus W O(5) entered this classification after M was established.

## 6. The actual quartic flag and the final split-target contradiction

Since C=H0(V O(4)), the actual presentation is the natural quartic evaluation sequence, not simply an abstract bundle with the same splitting. Its canonical derivative kernels give

    C=V tensor Sym4 W=A+V+P+D,
    M=V tensor Sym3 W O(-1),
    F=V tensor Sym2 W O(-2),
    F^-=V tensor W O(-3)=T O(-3).

The quotient F/F^- is canonically V O. One can see the twist directly: under the quartic flag, quotienting the factor Sym2 W by L W gives (W/L)^2, and

    (W/L)^2 tensor L^2=O

because det W is trivial. Equivalently the standard flag supplies the actual exact sequence

    0 -> V tensor W O(-3)
      -> V tensor Sym2 W O(-2) -> V O -> 0.

Every local section of F^- has derivative in F and hence in E. Therefore F^- is contained in the actual Gauss kernel E^- and in K0=ker p. This is the required connection-based containment; an abstract identification F^-=T O(-3) alone would not suffice.

The already proved surjection p consequently factors as a surjection

    F/F^-=V O -> O(4)+O(6).

The first component must vanish:

    Hom_G(V O,O(4))
      =Hom_G(V,H0(O(4)))
      =Hom_G(V,Sym4 W)
      =Hom_G(V,D)=0.

Here V and D are inequivalent irreducibles. An onto map to O(4)+O(6) cannot have zero O(4) projection. This is the contradiction, and it completes the reviewed nonzero-channel exclusion.

## 7. Contribution and boundaries

The new step is the transfer of a universal quartic evaluation classification to a different actual positive quotient, with every transfer hypothesis explicitly checked, followed by an incompatible equivariant quotient. The balanced-only backward endpoint analysis in PR819 Section 4 is not a dependency.

Together with the separately published zero-channel exclusion in PR814, this removes the generic-rank-two top branch of this split bf source. That combined consequence does not remove its rank-one O(6) branch and does not constitute a full source or label exclusion.

The review used only fixed catalog metadata, exact-sequence and constant-connection arguments, and bounded abstract character identities. It used no selected actual HM/source coefficients, parameters, points, derivative evaluations, instance matrices, instance ranks, model experiments, scans, large computation, or external writes. This is an independent written mathematical review, not proof-assistant certification.
