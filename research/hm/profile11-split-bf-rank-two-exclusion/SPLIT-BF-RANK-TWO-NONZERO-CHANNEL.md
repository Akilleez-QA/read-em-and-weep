# The quartic subsystem excludes the split-bf rank-two nonzero channel

## Exact scope and dependencies

The target here is G3.11.863639aa192e, source_index69, profile (1,1), at original-data commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep:

    A_q=O(-10)+O(4)+O(6),
    B_q=O(-8)+O(-6)+O(8), original defect=0.

The source under consideration is only

    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10),

tuple (0,1,0,0,0,1,0,1). This note assumes the top quotient has generic rank two and its internal derivative image J is nonzero, and proves that branch impossible. It does not exclude the rank-one top O(6) branch or claim a full source or label exclusion.

Original data are the actual splitting, strict-top, one-one catalog, and stable frontier files under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The first-polar and saturated derivative-image principles are the profile-free principles of PR796 and PR799, pinned respectively at d2b43060c83328dd5118aee6b9288fcfa0c873ac and 2172e4a7abbbe232f9f448bea6fa01dee7927460. The quartic subsystem proof to be reused is Sections 2-3 of the independently reviewed BF-SUBSYSTEM.md, published in PR819:

https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BF-SUBSYSTEM.md

Its local reviewed SHA256 is 087d0b78196b7c0d5e773375e603359450e0e9fb0ebb3003734c44eea4e133b9. The precise hypotheses needed from that proof are checked below. No balanced-target quotient is assumed in the reused argument.

## 1. The rank-two top map is onto, with the same small kernel

Let F=(P+D) O(-2), rank nine. Its quotient map lands in

    p:F -> O(4)+O(6),

because maps into O(-10) vanish. Assume generic rank p=2. Strict-top injects its coefficient space into H0(O(6)+O(8))=V+2P+D.

The image of p(2) is globally generated of rank two and degree 14-delta, where delta is the torsion cokernel length. Thus

    9 <= h0(image p(2))=16-delta,

so delta<=7. Its divisor is invariant; the minimum positive invariant divisor degree is twelve. Therefore delta=0 and p is onto everywhere.

For K0=ker p,

    H1(K0(2))=V+P,
    chi_G(K0(3))=0,

using

    Sym6 W+Sym8 W=V+2P+D,
    Sym7 W+Sym9 W=Wp+S+2T=(P+D) tensor W.

The complete small kernel support therefore gives exactly

    (V+P) O(-4),
    Wp O(-3)+V O(-4)+Wp O(-5),
    T O(-3)+O(-10).

The internal derivative targets T O(-5)+O(-10)+O(-12). Only the last kernel can have nonzero image, and that image is then J=O(-10), saturated by its complete quintic T channel or its scalar O(-10) channel. This is the same channel argument as in the reviewed balanced proof; it depends only on E and K0, not on the positive target's splitting.

## 2. Nonzero J gives exactly the same actual first-polar bundle

The zero original defect makes O(4)+O(6) saturated in Q(-2). The saturated derivative-image lemma yields

    0 -> O(-8) -> F^+/F -> O(6)+O(8) -> 0.

Hence rank F^+=12 and degree F^+=-12. First-polar generation puts all its degrees in {-1,0}. The equivariant Euler characters are

    chi_G(F^+)=-(P+D)-Sym6 W+Sym6 W+Sym8 W=0,
    chi_G(F^+(1))=-Sym5 W+Sym7 W+Sym9 W=Wp+S+T.

Therefore the actual saturated M=F^+ is

    M=(Wp+S+T) O(-1).                              (1)

## 3. Why the reviewed quartic classification applies unchanged

The relevant proof uses only F=(P+D) O(-2), M=F^+, and (1). For a pure linear bundle M=U O(-1), its Gauss kernel is K O(-2), with K the kernel of its constant coefficient map U tensor W -> C, where C is its constant span. Since F is contained in M^-, P+D injects into K.

Here U tensor W=A+V+2P+2D. The span C has dimension at least thirteen, so dim K<=11. After removing P+D, there are at most two dimensions available, whereas A+V+P+D has no such nonzero subrepresentation. Hence

    K=P+D, C=A+V+P+D, M^-=F.

The quotient (C O)/M has rank three, degree twelve, and no degree-zero summands because M spans C. It has no degree-one summands because (M^-)^+=F^+=M. Its natural full evaluation sequence and its H0 at twist -1 give the same nine-row classification as in PR819, uniquely forcing

    (C O)/M=V O(4).

None of these steps involves the original positive quotient. Thus the natural quartic evaluation flag is valid here too, in particular

    F^-=T O(-3),
    F/F^-=V O.                                    (2)

## 4. The split target contradicts the forced quartic quotient

The actual derivative kernel F^- lies in K0: its derivative already lies in F, hence its derivative projection through E is zero. By (2), the onto map p therefore factors through an onto map

    V O=F/F^- -> O(4)+O(6).

But every equivariant map V O -> O(4) is zero, since

    Hom_G(V,H0(O(4)))=Hom_G(V,D)=0.

Its first projection is zero, contradicting surjectivity onto O(4)+O(6). This excludes the stated rank-two, nonzero-J split-bf branch.

No endpoint section-freeness, selected HM/source coefficients, chosen points, actual derivative evaluations, instance matrices or ranks, experiments, scans, or large computation are used. Independent review remains required before relying on the new exclusion.
