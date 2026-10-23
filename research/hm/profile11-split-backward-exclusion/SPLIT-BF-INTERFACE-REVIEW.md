# Independent exact-version review: split-bf backward quotient

## Verdict and exact scope

**PASS for the stated conditional theorem and character interface.** The reviewed proof forces the actual, saturated quotient

    K_1/K_2 = O(2)+O(4),
    K_1 = E^-, K_2 = E^{--},

for the top-rank-one branch of the split bf source. It also forces the asserted splitting of K_1 and the three K_2 cohomology/Euler-character constraints. The argument distinguishes actual derivative kernels and raw derivative images from abstract equivariant bundle splittings. No correction is required to the reviewed version.

This is **not a complete bf-source exclusion, a label exclusion, or a frontier-count change**. In particular, the next derivative target is O+O(2), not the balanced target W O(1). A further argument specific to the split target remains necessary.

The reviewed file is `SPLIT-BF-BACKWARD-INTERFACE.md`, exactly SHA256

    b5924ec48fe1dd7583b37d75d47b8ef1ec3f0b3a589744349ebf924c08de4a61.

The target is G3.11.863639aa192e, source index 69, original defect zero, with

    A_q = O(-10)+O(4)+O(6),
    B_q = O(-8)+O(-6)+O(8),
    E = (P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    source tuple (0,1,0,0,0,1,0,1).

The target identity, source index, A_q, B_q, and zero defect were checked against the immutable original frontier record. The source tuple decodes to the displayed E, of rank 17 and degree -54, by the original source formula.

## 1. Public dependencies and exact input identity

The rank-two branch reduction is the combination of these two pinned proofs:

1. PR814, commit `1f94be65b3a470a1b594e61d56df7f6057c9d907`:
   https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

   SHA256:

       f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc

2. PR830, commit `620d5598ccc19e5e1c458a4cddb0d3a0709d83c3`:
   https://github.com/Akilleez-QA/read-em-and-weep/blob/620d5598ccc19e5e1c458a4cddb0d3a0709d83c3/research/hm/profile11-split-bf-rank-two-exclusion/SPLIT-BF-RANK-TWO-NONZERO-CHANNEL.md

   SHA256:

       d762e23c6b402bf8bfd62160e310ecacf601a910d47f6a3e278cd8a3806657f6

Their supplied contents have exactly these hashes. PR814 forces the nonzero internal channel when the bf top map has rank two; PR830 excludes that channel for the split target. The new conditional rank-one theorem does not use the quartic classification inside PR830. Calling rank one the remaining branch additionally uses those pinned prior conclusions. This review audits the new rank-one theorem, not an independent re-review of every prior theorem.

The immutable original inputs are pinned to commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

in this public directory:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The original-input identities were checked both by SHA256 and Git blob hash:

| File | Git blob | SHA256 |
|---|---|---|
| ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 | a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 |
| NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md | d7506dae49b4be43230450c4132bd5db91f137ef | 53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08 |
| ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md | dcacf0bcdef8377c1ed7654e5b82659ea409456e | 8d3f7f9f0492484edc104cf070ed72be4b969545a1e4b184be37a00dc5e7cac0 |
| one-one-endpoint-necessary-pairs.json | fe0afa410d89340d3082dc814277f89fbb582c19 | 6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb |
| rank-three-quotient-frontier-144.json | 8b5971092f9ef762584912609fd5e9301c4e271d | a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad |

The hypotheses used below are characteristic zero, the actual saturated inclusion in a constant bundle, the actual derivative connection, zero original defect, and the equivariant splitting and strict-top statements from these inputs. In particular, successive Gauss kernels remain saturated, and a kernel strictly lowers the highest negative splitting degree. The action on P1 factors through A5, so a nonempty invariant effective divisor has degree at least 12.

## 2. Independent representation audit

Write 1 for the trivial representation. The dimensions are

    dim(1,W,Wp,A,V,P,S,D,T) = (1,2,2,3,3,4,4,5,6).

The W-tensor rules needed here are

    W·1 = W,             W·W = 1+A,
    W·A = W+S,           W·S = A+D,
    W·D = S+T,           W·T = V+P+D,
    W·V = T,             W·P = Wp+T,
    W·Wp = P.

The recurrence Sym^(n+1) W = W·Sym^n W - Sym^(n-1) W gives the complete small list used in the review:

| n | Sym^n W |
|---:|---|
| 0 | 1 |
| 1 | W |
| 2 | A |
| 3 | S |
| 4 | D |
| 5 | T |
| 6 | V+P |
| 7 | Wp+T |
| 8 | P+D |
| 9 | S+T |
| 10 | A+V+D |
| 11 | W+S+T |

In particular Sym^10 W has no trivial constituent. Tensoring with A=W^2-1 gives

    W·A = W+S,
    Wp·A = T,
    T·A = Wp+S+2T,
    (P+D)·A = A+2V+2P+2D.

These rules independently reproduce every displayed character in the reviewed proof. Only this bounded universal representation arithmetic is used; it is not a computation of any selected source map.

## 3. The actual rank-one top and the forced lower channel

Put F=(P+D) O(-2), and let L=O(k) be the saturation of its rank-one image in O(4)+O(6). Strict-top injects

    P+D = H0(E(2)) -> H0(L(2)).

The source has dimension 9, while h0(O(k+2))=k+3 when this space is nonzero. Thus k>=6. An injection of O(k) into O(4)+O(6) requires k<=6. Therefore k=6. Its projection to O(4) is zero by ordinary degree, and its nonzero projection to O(6) is an isomorphism. The nine source sections inject into the nine-dimensional H0(O(8)), so they are the complete degree-eight system. Consequently the **raw** image is already O(6), and the evaluation sequence gives

    ker(F -> O(6)) = Sym^7 W O(-3) = (Wp+T) O(-3).

This proves saturation, not merely generic rank one.

The projection E->O(-10) is onto. Every source block except the unique O(-10) has zero Hom to this quotient by degrees, so that block maps by a nonzero scalar. Hence

    E' = ker(E -> O(-10)) = F+T O(-3)+O(-8),
    0 -> K_1 -> E' -> O(4)+O(6) -> 0

is an exact sequence of actual bundles. Removing the already-surjective F->O(6) shows that

    T O(-3)+O(-8) -> O(4)

is onto. If its T component vanished, one section of O(12) would have to be nowhere zero. That is impossible on P1. The T component is therefore nonzero. Its associated degree-seven row system has an invariant common-zero divisor of degree at most 7; the degree-12 orbit bound makes that divisor empty. Thus this lower T row is itself everywhere surjective onto O(4).

At twist 3, F supplies all of H0(O(9))=S+T. Modulo that summand, the lower T supplies one injective copy of T in H0(O(7))=Wp+T. Therefore the full section image has character S+2T. The source section character is

    H0(E'(3)) = (P+D)·W+T = Wp+S+3T.

Its kernel is Wp+T and its section cokernel is Wp. Also H1(E'(3))=H1(O(-5))=S and H1(O(7)+O(9))=0. Complete reducibility of finite-group representations gives

    H0(K_1(3)) = Wp+T,
    H1(K_1(3)) = Wp+S.

Rank and degree are

    rank K_1 = 16-2 = 14,
    deg K_1 = (-44)-10 = -54.

Strict-top applied to E gives maxdeg K_1<=-3. No splitting of the ambient connection was used.

## 4. Exhaustive lower support and the unique first kernel

An irreducible block Z O(-j), j>=5, contributes

    Z·Sym^(j-5) W

to H1(K_1(3)). This is a genuine representation, so its contribution must be a subrepresentation of Wp+S. Its dimension must satisfy

    (j-4) dim Z <= 6.

Central parity requires Z to be odd for odd j and even for even j. These two restrictions give the following complete list of candidates; there are no omitted representations within the dimension bound:

| j | Possible irreducible Z | H1 contribution | Result |
|---:|---|---|---|
| 5 | W | W | forbidden |
| 5 | Wp | Wp | allowed |
| 5 | S | S | allowed |
| 5 | T | T | forbidden |
| 6 | 1 | W | forbidden |
| 6 | A | W+S | forbidden |
| 6 | V | T | forbidden |
| 7 | W | W+S | forbidden |
| 7 | Wp | T | forbidden |
| 8 | 1 | S | allowed |
| 9 | none | odd coefficients have dimension at least 2, giving at least 10 | excluded by dimension |
| 10 | 1 | T | forbidden |

For j>=11, even a one-dimensional coefficient has contribution dimension j-4>=7, so no further block fits. This also rules out the parity-allowed larger irreducibles at the earlier degrees.

The Wp contribution can only be Wp O(-5), with multiplicity one. The S contribution must be either S O(-5) or O(-8), each with multiplicity one. Hence the two lower-support possibilities in the proof are exhaustive.

The degree-minus-three coefficient is already Wp+T, by H0(K_1(3)) and maxdeg K_1<=-3. Write R_4 for the unknown degree-minus-four coefficient. Directly from the actual exact sequence,

    chi_G(K_1(4))
      = (P+D)·A + T·W - A - Sym^8 W - Sym^10 W
      = 2V+2P+D-A.

The degree-minus-three block contributes

    (Wp+T)·W = V+2P+D.

If the lower blocks were Wp O(-5)+S O(-5), they would contribute zero at twist 4, requiring R_4=V-A, which is not genuine. If they are Wp O(-5)+O(-8), their contribution is -A, requiring exactly R_4=V. Therefore

    K_1 = (Wp+T) O(-3)+V O(-4)+Wp O(-5)+O(-8).

The rank is 8+3+2+1=14 and the degree is -24-12-10-8=-54, consistent with the independently obtained totals. Equivariant splitting is being used solely as a bundle splitting.

## 5. The second derivative: actual image and extension audit

Because K_1 is the actual Gauss kernel of E, its second fundamental form factors through

    (E/K_1)(-2) = O(-12)+O(2)+O(4).

Every summand of the proved K_1 has degree greater than -12, so the O(-12) component vanishes by ordinary degrees. Thus its actual derivative takes values in O(2)+O(4).

The top Wp O(-3) has no map to O(2), since Sym^5 W=T contains no Wp. Strict-top for K_1 makes its remaining map to O(4) nonzero. The degree-seven system has no common zeros by the invariant-divisor bound. Therefore the raw derivative image contains the entire **direct summand** O(4), not just a generically isomorphic line or a graph with an unknown O(2) component.

The possible complementary maps to O(2) are precisely:

| Source block | Section degree | Relevant constituent |
|---|---:|---|
| T O(-3) | 5 | T in Sym^5 W |
| V O(-4) | 6 | V in Sym^6 W |
| Wp O(-5) | 7 | Wp in Sym^7 W |

Wp O(-3) is already ruled out, and O(-8) has no map to O(2), because Sym^10 W has no invariant. Any nonzero channel in the table is basepoint-free: the common-zero divisor is invariant and has degree at most 7. Together with the existing O(4) direct summand, such a channel makes the raw derivative image the full O(2)+O(4), everywhere.

It remains to rule out simultaneous vanishing of all three channels. In that case the raw derivative image is exactly O(4). Strict-top injects

    H0(K_1(3)) = Wp+T -> H0(O(7)) = Wp+T.

This is an isomorphism. Hence the restriction to the entire top block is the complete degree-seven evaluation system, whose kernel is

    L = Sym^6 W O(-4) = (V+P) O(-4).

Let N=V O(-4)+Wp O(-5)+O(-8). Since the top block already surjects onto O(4), projection to N gives an exact sequence

    0 -> L -> K_2 -> N -> 0.

The order of the Ext arguments matters. The relevant ordinary groups are

    Ext^1(O(-4),O(-4)) = H1(O) = 0,
    Ext^1(O(-5),O(-4)) = H1(O(1)) = 0,
    Ext^1(O(-8),O(-4)) = H1(O(4)) = 0.

Thus Ext^1(N,L)=0, including all coefficient multiplicities. Averaging a splitting over the finite group makes it equivariant. This proves

    K_2 = (2V+P) O(-4)+Wp O(-5)+O(-8)

under the assumed failure, rather than merely giving this as a formal character.

Now K_2 is the actual kernel of the derivative of K_1. Its derivative factors through

    (K_1/K_2)(-2) = O(2).

Strict-top at twist 4 would inject its entire top coefficient space

    2V+P -> H0(O(6)) = V+P.

This is impossible, both by the V multiplicity and by dimension (10>7). Therefore the assumed simultaneous vanishing is impossible. At least one complementary channel is nonzero, so

    im beta_(K_1) = O(2)+O(4)

as the raw sheaf image. It is saturated, and the exact quotient is

    K_1/K_2 = O(2)+O(4).

There is no torsion divisor or determinant-defect correction at this step. Every factorization used here follows from the actual Gauss-kernel definition, not from declaring the displayed abstract summands horizontal.

## 6. The exact K_2 interface

Subtracting the actual quotient gives

    rank K_2 = 14-2 = 12,
    deg K_2 = -54-(2+4) = -60.

Strict-top for K_1 gives maxdeg K_2<=-4. The actual next derivative factors through

    (K_1/K_2)(-2) = O+O(2).

From the now-proved splitting of K_1, its Euler characters at twists 3,4,5 are

    chi_G(K_1(3)) = T-S,
    chi_G(K_1(4)) = 2V+2P+D-A,
    chi_G(K_1(5)) = -W+2Wp+S+4T.

For example, the last identity is

    (Wp+T)·A + V·W + Wp - W
      = -W+2Wp+S+4T.

The quotient O(2)+O(4) contributes, respectively,

    Sym^5 W+Sym^7 W = Wp+2T,
    Sym^6 W+Sym^8 W = V+2P+D,
    Sym^7 W+Sym^9 W = Wp+S+2T.

Thus

    chi_G(K_2(3)) = -Wp-S-T,
    chi_G(K_2(4)) = V-A,
    chi_G(K_2(5)) = -W+Wp+2T.

Because H0(K_2(3))=0, the first equality is equivalently the genuine cohomology assertion

    H1(K_2(3)) = Wp+S+T.

The numerical Euler characteristics are -12, 0, and 12. These agree with rank 12 and degree -60 through chi(K_2(t))=12(t+1)-60. This independently checks all the interface values.

## 7. Contribution and remaining boundary

The proof resolves the possible rank-one failure of the second backward image. It supplies both the unique first-kernel splitting and an exact saturated second quotient, reducing any further argument to an actual rank-12, degree-minus-60 kernel with maximum degree at most -4 and the stated bounded character interface.

It does not determine the full splitting of K_2, prove what its next raw derivative image is, or exclude the source. The split target O+O(2) must be analyzed on its own terms. The proof and this review use only universal exact-sequence arguments, standard evaluation kernels, finite-dimensional representation identities, degree bounds, and the immutable input record. No selected actual source coefficients, points, derivatives, matrices, instance ranks, model experiments, scans, or unapproved large computation were used.
