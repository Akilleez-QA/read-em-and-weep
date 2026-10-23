# Independent review of the split-ce constant-span exclusion

## Verdict and exact reviewed version

**Pass.** The argument proves that the source tuple

    (0,0,1,0,1,0,0,1)

cannot occur for the original-zero-defect label **G3.11.863639aa192e**, source index 69. No mathematical correction is required for this conclusion. This is a source-stratum exclusion, not an exclusion of the whole label.

The complete reviewed proof is `SPLIT-CE-CONSTANT-SPAN-EXCLUSION.md`, frozen at:

    SHA256 e3c1cb16be8ed7714cb2c3d5f6a3ba9f7da85567aa5a53e100b2d3458fc977bd
    Git blob 79a5b368077d610da48b2cb884046a82dd90557d

This review is of those exact bytes. It independently checks the new constant-span, endpoint-removal, saturation, rank, intersection, and determinant arguments, as well as the relevant upstream mathematical inputs. The bounded representation calculation was also recomputed from the tensor-with-W recurrence through degree 22.

## 1. Immutable dependencies and source identity

The principal dependency is the full proof of PR814, at commit

    1f94be65b3a470a1b594e61d56df7f6057c9d907

[PR814 proof at its immutable commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md).

The checked copy has:

    SHA256 f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc
    Git blob 6321c101cb2cba2f6e6abde3cd9531496e41baf2

The saturated internal/external derivative-image argument is Section 3 of [PR796 at commit d2b43060c83328dd5118aee6b9288fcfa0c873ac](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md). Its checked copy has SHA256 `622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1` and Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`. Its proof applies to the present rank-two external image without change: the conclusion uses local freeness of the internal and external quotients, not rank one of the external image.

The first-polar input was checked in its restatement in PR814 and against [PR799 at commit 2172e4a7abbbe232f9f448bea6fa01dee7927460](https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md) and [PR802 at commit e484640a6565c278321bf6557860262c1ac1b7df](https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md). The checked Git blobs are respectively `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1` and `98a1bd6123e148476da0b997d879aecbf885ec97`.

The original data are at [commit db51525015bb7c5e825833d550d08dedf6f6ea96, in research/hm/order-four-quadratic-load](https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load). Recomputed Git blob hashes agree with all five pins in PR814:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.

Entry 69 of the necessary-pair catalog contains the stated tuple and has

    A_q=O(-10)+O(4)+O(6),
    B_q=O(-8)+O(-6)+O(8),
    original defect=0.

The stable-label catalog identifies it as G3.11.863639aa192e. Substituting the tuple into the actual splitting formula gives

    E=(V+2P) O(-2)+V O(-4)+Wp O(-5)+O(-10).

The extra P is correctly retained. Thus rank E=17 and deg E=-54.

## 2. The upstream split-ce subsystem is valid

Let F=(V+2P) O(-2) and U=O(4)+O(6). Strict-top vanishing makes the map on top-block sections injective. The two P multiplicity spaces in source and target both have dimension two, so their map is invertible. After changing the source multiplicity basis, each target row has a nonzero P system. A common zero divisor of either row would be invariant of positive degree at most eight, impossible because every nonempty projective orbit has at least twelve points. Therefore F maps onto U everywhere.

The exact kernel follows from

    H1(K0(2))=D,
    chi_G(K0(3))=Wp+T-S.

The only blocks that can contribute to the D budget are D O(-4) and O(-8). The first would force a negative S coefficient in H0(K0(3)); the second gives precisely

    K0=(Wp+T) O(-3)+O(-8).

The internal derivative into V O(-6)+Wp O(-7)+O(-12) vanishes. The only degree-eligible exceptional channels are O(-8) to the first two summands, and they vanish because V is absent from Sym^2 W and Wp is absent from W. The raw derivative image is consequently saturated, with

    0 -> F -> F^+ -> U(2) -> 0,
    F^+ intersect E=F.

First-polar generation restricts the splitting degrees of F^+ to zero and minus one. Its actual constant part is D, and its constant projection is the saturated standard evaluation kernel

    M=Sym^7 W O(-1) subset (Sym^8 W) O.

These are statements about the original embedded bundle and its connection. They do not require a horizontal splitting of an abstract complement, nor the false endpoint assumption H0(E^+)=0.

## 3. The full constant span really has dimension fourteen

Let C be the smallest constant subspace containing F^+. It contains the actual D because D O is contained in F^+. Under constant projection H -> H/D, its image is exactly the full constant coefficient span of M, namely Sym^8 W, of dimension nine. The kernel on C is exactly D. Therefore

    dim C=5+9=14,
    C is isomorphic to D+Sym^8 W=P+2D.

There is no hidden increase in dimension caused by a choice of lifts: the span is taken inside the actual H, and the kernel of H -> H/D is already contained in C.

The exact top sequence gives rank F^+=13 and deg F^+=-8. Because F^+ is saturated in H O, it is also saturated in C O. Thus C O/F^+ is a line bundle of degree eight. The proof correctly distinguishes this established quotient from any unproved saturation after projecting E'.

## 4. Removing O(-10) and establishing the actual forward sum

Only the O(-10) source block can map to the O(-10) quotient. Surjectivity makes this component an isomorphism, so

    E'=ker(E -> O(-10))=F+V O(-4)+Wp O(-5).

With K=E^-, the surjection F -> U gives the exact sequence

    0 -> K0 -> K -> V O(-4)+Wp O(-5) -> 0.

After twist eight, both outer terms are globally generated and H1(K0(8))=0. Sections of the quotient lift, so K(8) is globally generated. Every degree of K is consequently at least -8, and Hom(K,O(-12))=0.

The derivative of K already lies in E. Its component in (E/E')(-2)=O(-12) therefore vanishes. For the derivative of E', the external image is the saturated U, and the internal image of its external kernel K is zero. The internal/external image exact sequence makes the complete raw image saturated and isomorphic to U. Hence

    (E')^+/E'=U(2),
    rank (E')^+=18,
    deg (E')^+=-44+14=-30.

Moreover F supplies the same entire external image. Since it is contained in E', its derivative image modulo E' equals that of E'. This proves the equality of actual sheaves

    (E')^+=E'+F^+.

No backward-endpoint theorem or extra plateau identity is needed.

## 5. Horizontal saturation forces rank nineteen and exact intersection

Set S0=E'+C O and let S be its saturation in H O. The derivative of E' lies in E'+F^+, which is contained in S0; C O is constant. Hence the generic subspace of S0 is horizontal. Its saturated Grassmannian map has zero differential, so characteristic zero makes it constant:

    S=H' O.

The construction is equivariant, so H' is G-stable.

The sum contains the saturated rank-eighteen bundle (E')^+. Since C O/F^+ has rank one, its rank is at most nineteen. Rank eighteen would force S=(E')^+: saturated subbundles with the same generic subspace coincide. That would make a degree-minus-thirty bundle constant, which is impossible. Thus dim H'=19.

The actual intersection E' intersect C O has rank 16+14-19=11 and contains F of rank eleven. The quotient by F is a rank-zero subsheaf of the locally free E'/F; it is therefore zero. Consequently

    E' intersect C O=F.

This is the precise justification for the injection

    E'/F=V O(-4)+Wp O(-5) -> (H'/C) O.

The proof neither asserts nor needs its saturation. Indeed a saturated injection here would be impossible already by degree, but that fact cannot be substituted for the determinant argument.

## 6. The determinant obstruction is exact

Both sides of the last injection have rank five. The source degree is

    3(-4)+2(-5)=-22,

and the target degree is zero. Taking determinants gives a nonzero equivariant map O(-22) -> O. All coefficient determinant characters are trivial because the binary icosahedral group is perfect. The resulting section is therefore an invariant in Sym^22 W, not merely a semi-invariant with an unspecified character.

Starting with Sym^0 W=1 and Sym^1 W=W, the displayed tensor-with-W rules and the recurrence give

    Sym^18 W=A+V+2P+D,
    Sym^19 W=W+Wp+S+2T,
    Sym^20 W=1+A+V+P+2D,
    Sym^21 W=W+2S+2T,
    Sym^22 W=2A+V+P+2D.

The recurrence through degree 22 has nonnegative multiplicities and the expected dimension n+1 at each degree. There is no trivial constituent at degree 22. As a second check, the determinant would define a nonempty invariant effective divisor of degree 22; the projective orbit sizes 12,20,30,60 cannot sum to 22 with nonnegative multiplicities.

The possible torsion cokernel has not been discarded. Its total length would be exactly 22, and its determinant divisor is precisely the obstruction. This is why no assumption that the projection E'/F is saturated enters the proof.

## Scope and verification boundary

The result excludes only the ce source stratum for G3.11.863639aa192e. It does not exclude cf, bf, bc, bb, or the full stable label. The balanced ce exclusion belongs to the earlier proof and is not a new whole-label consequence.

The verification uses universal exact-sequence and connection arguments, source-catalog inspection, immutable-file hash checks, and bounded abstract representation identities. No selected actual HM/source coefficients, points, derivatives, instance matrices, instance ranks, scans, or large computation are used. This is an independent written mathematical verification, not proof-assistant certification.
