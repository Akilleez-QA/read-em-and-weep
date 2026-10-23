# The nonzero internal channel forces a quartic V subsystem

## Target and scope

Only G3.11.73682b4c817f (source_index72) is considered. Assume its original zero-defect quotient A_q=O(-10)+W O(5), and the compatible source

    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10).

All original source and label inputs are at immutable commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json. The last file identifies the stable label and source_index72. The source tuple at issue is (0,1,0,0,0,1,0,1).

The saturated derivative-image lemma and small V+P kernel support are from PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, Sections 3 and 5:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

The first-polar generation principle is from PR799, commit 2172e4a7abbbe232f9f448bea6fa01dee7927460, Section 4:

https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md

Only the profile-free principles are used. The rank-two variant of the saturated derivative-image lemma has the identical quotient-extension proof. All required applications are explained below. PR802 was read as context but is not a dependency of this proof.

Notation: G is the binary icosahedral group, W its defining two-space, Wp the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P the other even irreducibles of dimensions three and four. Every nonempty invariant divisor on P1 has degree at least twelve.

In particular E is saturated in H O, H0(E^-(2))=0, and the profile is (1,1). The latter means that the backward endpoint E^- has generic derivative rank at most two. No endpoint section-freeness is used.

This note does not exclude the source. It resolves the actual constant-span structure and a further backward endpoint quotient in its nonzero internal-derivative branch.

## 1. Top map and exhaustive kernel choices

Put F=(P+D) O(-2), rank nine. Its actual quotient map p:F -> W O(5) is onto everywhere. Indeed strict-top vanishing injects its nine-dimensional coefficient space into W tensor Sym7 W. Generic rank one would force all nine sections through a line of degree at most five, with at most eight sections after twist two. For generic rank two the image of p(2) is globally generated, and a torsion cokernel of length delta satisfies

    9 <= h0(image p(2))=16-delta.

Thus delta<=7; equivariance and minimum divisor degree 12 force delta=0.

For K0=ker p,

    H1(K0(2))=V+P,
    chi_G(K0(3))=0.

The complete j>=4 blocks supported by the V+P H1 budget are V O(-4), P O(-4), Wp O(-5), and O(-10), as checked in PR796. Their H1-at-twist-two contributions are V,P,P,V+P, respectively; their H1-at-twist-three contributions are 0,0,Wp,T. Matching both cohomology identities and the degree-minus-three part gives exactly

    K0=(V+P) O(-4),
    K0=Wp O(-3)+V O(-4)+Wp O(-5),
    K0=T O(-3)+O(-10).                              (1)

The internal derivative targets

    (E/F)(-2)=T O(-5)+O(-10)+O(-12).

The first two kernels in (1) have no nonzero component: ordinary degrees kill all but the possible Wp-to-T constant map, and distinct irreducibility kills that one. In the last kernel only O(-10) can contribute, through the unique quintic channel to T O(-5) and the scalar channel to O(-10). Any nonzero combination is saturated: the quintic channel is the complete Sym5 W tautological inclusion, and the scalar channel is an isomorphism onto its summand. Hence either J=0 or J=O(-10).

Assume henceforth J is nonzero. The saturated derivative-image sequence gives

    0 -> O(-8) -> F^+/F -> W O(7) -> 0,
    rank F^+=12,   degree F^+=-12.                   (2)

The first-polar map is onto F^+, so all its degrees are 0 or -1. Equivariant Euler characteristics in (2) give

    chi_G(F^+)=0,
    chi_G(F^+(1))=Wp+S+T.

Consequently the actual saturated bundle M=F^+ is

    M=(Wp+S+T) O(-1).                               (3)

## 2. A linear bundle's constant relations are its Gauss kernel

For any saturated actual linear bundle U O(-1) in a constant space, let C be its constant coefficient span and let K be the kernel of its coefficient map

    U tensor W -> C.

At an arbitrary line l in W, the inclusion of U tensor l has zero kernel. Thus K intersects U tensor l trivially. Projecting K to (U tensor W)/(U tensor l) identifies it with the kernel of the derivative of U O(-1), with the appropriate tautological twist. Globally this gives the exact identity

    (U O(-1))^-=K O(-2).                            (4)

In particular this kernel is saturated and pure of degree -2. Also the first forward transform of a linear bundle is exactly its constant coefficient span.

Apply this to (3). Since derivatives of F lie in M, F is a subbundle of M^-. Equation (4) turns this into an injective map of constant representations

    P+D -> K.

The available coefficient representation is

    (Wp+S+T) tensor W=A+V+2P+2D.

The constant span C of M has dimension at least 13: a rank-12 negative saturated bundle cannot be the entire constant span of dimension 12. Hence dim K<=24-13=11. After removing its injected P+D of dimension nine, K has at most two dimensions left. But the remaining representation A+V+P+D has no nonzero subrepresentation of dimension at most two. Therefore

    K=P+D,   C=A+V+P+D,   dim C=15,
    M^-=F.                                          (5)

These are actual embedded kernel and constant-span statements.

## 3. The quotient by M is uniquely V O(4)

Let Q_C=(C O)/M. It is a globally generated rank-three bundle of degree twelve. It has no degree-zero summands: such a summand would provide a nonzero constant functional on C annihilating M, contradicting that C is its full span.

Since H0(M)=H1(M)=0, the quotient map identifies C with H0(Q_C), so its presentation is the full natural evaluation sequence. If

    Q_C=direct sum_i R_i O(d_i),

then this sequence identifies

    M=direct sum_i R_i tensor Sym^(d_i-1)W O(-1),
    M^-=direct sum_(d_i>=2) R_i tensor Sym^(d_i-2)W O(-2).

A d_i=1 summand contributes a nonzero linear block to M but nothing to M^-. Because (M^-)^+=F^+=M, no such degree-one block is permitted. Thus every d_i>=2.

The center-even, rank-three, degree-twelve possibilities are exactly the nine rows below. The second column is H0(Q_C(-1)), which must equal Wp+S+T by (3).

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

This is an exhaustive bounded abstract representation check, not a map or instance scan. The only possibility is

    Q_C=V O(4).                                     (6)

Consequently the actual evaluation sequence and its canonical derivatives identify the whole subsystem as

    C=V tensor Sym4 W=A+V+P+D,
    M=V tensor Sym3 W O(-1)=(Wp+S+T) O(-1),
    F=V tensor Sym2 W O(-2)=(P+D) O(-2),
    F^-=V tensor W O(-3)=T O(-3),
    F^{--}=V O(-4).                                 (7)

The identification is with the natural quartic evaluation/osculation subsystem. It does not choose coefficients of the actual source.

## 4. The backward endpoint quotient is forced

From (1) and (7), F^- is the full T O(-3) subbundle of K0. Thus

    K0/F^-=O(-10),
    F/F^-=V O,
    0 -> O(-10) -> V O -> W O(5) -> 0.              (8)

The derivative of F^- inside the quartic subsystem is onto

    (F/F^-)(-2)=V O(-2).

Its composition with the quotient in (8), twisted by -2, is onto W O(3). Since F^- is a subbundle of E^-, this shows that the actual derivative image of E^- contains the whole W O(3) in

    (E/E^-)(-2)=O(-12)+W O(3).

Profile (1,1) says that the generic derivative rank of E^- is at most two. The exhibited saturated W O(3) already has rank two, so no additional component is possible. Consequently

    E^-/E^{--}=W O(3),
    (E^-)^+/E^-=W O(5),                             (9)

with no torsion correction.

The negative projection E -> O(-10) is onto and only its actual O(-10) summand can map nontrivially there. Its kernel is therefore the saturated bundle

    E'=(P+D) O(-2)+T O(-3)+O(-8).

Equation (9) identifies this kernel with (E^-)^+. Put K=E^-. Since E'=(E^-)^+, actual derivatives of K lie in E'; therefore the actual second fundamental form of E' kills K. The projection of that form to Q(-2) has exact kernel K and saturated image W O(5), so its full image factors injectively through E'/K=W O(5). Its internal image on K is zero by the preceding actual connection statement. The saturated derivative-image lemma applies, without making any projection to an abstract complement of E' in E. Hence

    (E')^-=E^-,
    E'/E^-=W O(5),
    (E')^+/E'=W O(7).                              (10)

This produces an actual rank-two chain E^- ⊂ E' ⊂ (E')^+ inside the original constant connection.

## Contribution and limits

The nonzero internal channel for this source forces a unique equivariant quartic V subsystem, fixes its genuine constant fifteen-space, and fixes the backward endpoint's exact quotient W O(3). This is a structural missing-dependency resolution, not an exclusion. The remaining question is whether this forced subsystem and chain can coexist with the full original E and its endpoint conditions. No other stable label is addressed here.

Independent review is required before relying on the new steps.
