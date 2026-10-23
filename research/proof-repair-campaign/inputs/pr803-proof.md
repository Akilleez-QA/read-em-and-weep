# The defect-twelve tensor-quartic endpoint still forces a longer backward plateau

## Result and scope

The two maximal profile-(1,1) labels

    G3.11.cb71f599859d,
    G3.11.0fe2a757439f

are impossible. Both have original determinant defect twelve. This proof retains that defect and does not assume H0(E^+)=0. Its new step recovers the exact tensor-quartic endpoint intersections despite the defective external O(16) image. The already-published backward-rank argument then gives the contradiction.

The distinct label G3.11.64d33b6d4139 is not excluded. Its precise residual theorem remains unchanged. No selected actual HM/source-instance coefficients, parameters, points, derivative evaluations, matrices, ranks, model experiments, scans, or large computation are used. All rank assertions below are deductions under the universal formal branch hypotheses. No conclusion about higher-order lifting, algebraicity, SF>=4, or the original research goal is made.

## 1. Exact inputs

The immutable original setup is at db51525015bb7c5e825833d550d08dedf6f6ea96 in Akilleez-QA/read-em-and-weep, under research/hm/order-four-quadratic-load:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md gives the saturated E in H O, H0(E(1))=0, actual source types, and maximal Gauss-plateau convention.
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md and the pinned JSON catalogs identify the two quotient pairs and their genuine original derivative data.

The companion theorem “Defect-twelve top blocks force a saturated constant-quotient residual” is public in PR801, commit 4301e3b3027afa1c32e1e7359a5fdf5b9d27edfd, at

https://github.com/Akilleez-QA/read-em-and-weep/blob/4301e3b3027afa1c32e1e7359a5fdf5b9d27edfd/research/hm/profile11-defect12-constant-residual/PROOF.md

Its independently reviewed proof has SHA256

    0e28eed42faf99a0ebaed4bfcf7e54b20f0e13d642f92f61864e421043e71915.

It is an explicit input. We use exactly its conclusions that the only remaining strata are E6 for cb71f599859d and E6,E13 for0fe2a757439f, and that in those strata the full first-polar image of the top block is saturated and has the actual tensor-quartic shape stated below. We do not use its separate abstract residual-construction supplement.

Two public structural dependencies are:

- PR797, commit cdee9396133fb96d4a91babba87b1a7a35903635, research/hm/profile12-tensor-quartic-block/PROOF.md. Its tensor-quartic quotient and Section7 Euler-extension argument are used; its profile-(1,2) interior-stage argument is not imported.
- PR798, commit2bbf244bafc380cf5b0ce1114f86fcd8053e4e55, research/hm/profile12-backward-plateau-exclusion/PROOF.md. Its Sections2-6 are a connection-based backward-rank obstruction once the exact intersection data are supplied. The relevant maximal backward index is one in both the present profile and that publication.

Write W for the defining binary-icosahedral two-space, Wp for the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P for the other even three- and four-spaces. All representations are self-dual.

The remaining source types and original quotients are

    E6 =(P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    E13=(P+D) O(-2)+T O(-3)+W O(-9),

    cb71: A_q=O(-10)+O(-8)+O(14), B_q*=O(28)+O(-6)+O(-8);
    0fe2: A_q=W O(-9)+O(14),      B_q*=O(28)+W O(-7).

There is an actual constant fifteen-space C0 inside H such that, putting F=(P+D) O(-2) and G=F^+,

    C0=V tensor Sym4 W,
    F=V tensor U_2^4,
    G=V tensor U_3^4=(Wp+S+T) O(-1),
    (C0 O)/G=V O(4),
    X=G/F=V O(2).

The derivative of G induces an isomorphism

    X -> ((C0 O)/G)(-2).                                (1)

The exact internal image sequence is

    0 -> Wp O(-5) -> X -> O(16) -> 0.                   (2)

The original derivative of E has saturated forward quotient E^+/E=B_q*. The image of G in this quotient is f12 O(16) inside its positive O(28) summand, where f12 has the reduced invariant twelve-point divisor D12. In particular the image is abstractly O(16), but is not saturated in O(28). Its kernel is

    G0=E intersect G,
    0 -> F -> G0 -> Wp O(-5) -> 0,
    G/G0=O(16).                                        (3)

All intersections are sheaf intersections in H O.

## 2. The endpoint quotient inside C0 has rank exactly one

Let Nplus=E^+ intersect (C0 O). It is saturated in C0 O and contains G. The derivative of E^+ kills E, so its restriction to G kills G0. By (3), that restriction has generic rank at most one. But (1) is onto the entire (C0 O)/G, up to the indicated twist. Projection to H O/E^+ therefore shows

    rank((C0 O)/Nplus)<=1.                              (4)

This argument uses the automatic inclusion E in (E^+)^- and does not assert the reverse equality at the endpoint.

Suppose first that C0 O is contained in E^+. Its projection to B_q*=E^+/E has zero component in the negative summands, since C0 O is constant. Its nonzero image is a line subsheaf of O(28) containing f12 O(16), because it contains the image of G. Thus that image is O(28)(-D') for an invariant effective divisor 0<=D'<=D12. The invariant orbit has twelve points, so D' is zero or D12. Consequently

    N=E intersect (C0 O)

has rank14 and degree -28 or -16.

Every ordinary degree of N is at most -2 because N is a subbundle of E and H0(E(1))=0. Degree -16 is therefore impossible. Degree -28 would force N=O(-2)^14; its inclusion in E factors through the rank9 top block F, also impossible. This excludes C0 O subset E^+.

Hence (4) has rank exactly one:

    rank Nplus=14,  (C0 O)/Nplus=O(e)                   (5)

for some integer e. We now determine e without discarding any divisor.

## 3. The actual endpoint quotient is O(18)

Since G is saturated and Nplus contains G, projection gives a surjection

    (C0 O)/G=V O(4) -> (C0 O)/Nplus=O(e).

Twisting by minus two and composing with (1) gives a surjection

    X=V O(2) -> O(e-2).                                 (6)

Its kernel is rank two and contains G0/F=Wp O(-5), because the derivative of E^+ kills E. That subbundle is saturated in X by (2). The two kernels have equal generic rank, so saturation makes them equal. Thus the locally free quotient in (6) is precisely the quotient in (2), with no zeros remaining:

    e=18,
    (C0 O)/Nplus=O(18),
    Nplus/G=Wp O(-3).                                  (7)

This is why an injective map of line bundles alone is not used to determine e: surjectivity of (6) is essential.

The extension of Wp O(-3) by G=O(-1)^12 splits equivariantly as bundles because H1(O(2))=0. Hence every degree of Nplus is -1 or -3. In particular Nplus maps to zero in every negative summand of B_q*, whose degrees are at most -6.

The image of Nplus in B_q* is therefore a nonzero line in O(28), since it contains the image of G. Its kernel N=E intersect (C0 O) has generic rank13 and is saturated in Nplus.

The derivative of Nplus within the actual constant C0 O takes values in O(16), by (7). Its restriction to G is onto by (1),(6), so its kernel Nprime=(Nplus)^- is saturated of rank13 and degree-34. The derivative of N lies simultaneously in C0 O and E^+, hence lies in Nplus. Therefore

    N subset Nprime.

Since N is saturated in Nplus and both have rank13, the inclusion is equality. We have proved the exact endpoint identities

    N=(Nplus)^-,
    rank N=13,  deg N=-34,
    0 -> N -> Nplus -> O(16) -> 0.                     (8)

No equality (E^+)^-=E, no vanishing H0(E^+), and no saturation of f12 O(16) in O(28) was used.

## 4. The exact residual is the one needed for the backward obstruction

The now-proved sequences (3),(7),(8) give, by subtracting a local section of G with a prescribed derivative in O(16),

    0 -> Wp O(-5) -> N/F -> Wp O(-3) -> 0.              (9)

The equivariant extension space is one-dimensional. Its split element cannot inject into E/F=T O(-3)+lower terms: its Wp O(-3) summand has no map to the inequivalent T at the same degree and no map to lower degrees. Hence (9) is the nonzero Euler extension. It follows that

    N/F=P O(-4),
    N=(P+D) O(-2)+P O(-4).                             (10)

The map P O(-4)->T O(-3) is the unique nonzero equivariant linear channel; it is saturated with quotient Wp O(-1). Consequently the actual locally free image sheaf of E in the constant quotient (H/C0) O is

    E/N=Wp O(-1)+L,                                    (11)

where L=O(-8)+O(-10) for E6 and L=W O(-9) for E13. As in PR797, saturation of this entire residual image is not asserted or needed.

The E6 stratum for0fe2 is impossible directly: E6 cannot surject onto the negative W O(-9) part of A_q, because only its O(-10) line has any possible nonzero component there and a line cannot supply generic rank two. Thus the only remaining matching pairs have L equal to the negative part of A_q.

## 5. The backward kernel has at least three independent derivative directions

For completeness, we state the connection argument rather than relying only on profile labels. Put K=E^-. The map N->A_q has image exactly O(14), since F already maps onto that line and every map from N's displayed degrees to the negative part vanishes. From (11), the induced map E/N->L kills Wp O(-1) and restricts to an isomorphism on L. Hence the actual projection of K to (H/C0) O is exactly Wp O(-1), with an onto map

    K -> Wp O(-1).                                     (12)

The latter embedded bundle has Gauss rank two. Indeed its coefficient map is a nonzero equivariant intertwiner Wp tensor W=P->H/C0. Since P is irreducible it is injective, and the bundle is the standard tautological Wp O(-1) inside the constant P O.

The quotient in (7) is induced by an onto map V O(4)->O(18), a basepoint-free three-section system of degree fourteen. Its composite with C0 O is the product of that system with all degree-four sections. At an arbitrary point some degree-fourteen section is nonvanishing, so multiplication by it identifies local jets; the complete degree-four system generates every jet through order four. Thus the composite C0 O->O(18) is jet-surjective through order four everywhere.

Let J_i be its order-i jet kernel. Then

    J_0=Nplus,   J_1=N,
    J_2=N^-=K intersect (C0 O).

The last equality follows because derivatives inside C0 vanish modulo E exactly when they vanish modulo N=E intersect C0. Jet-surjectivity implies that the derivative of J_2 has a nonzero rank-one image in (N/J_2)(-2). This image remains nonzero modulo K, since N intersect K=J_2.

At the generic point, the derivative of K followed by the constant quotient to (H/C0)/Wp O(-1) has rank two by (12). Its restriction to J_2 contributes the just-proved nonzero rank-one image in the kernel of that quotient, represented inside C0. The contributions are independent. Therefore

    generic rank beta_K >= 2+1=3.                      (13)

This is the same intrinsic argument as PR798 Sections3-5. It does not require global saturation of K+C0 or of the whole image in (11).

For maximal profile (1,1), the backward rank-three plateau has length one, so the Gauss rank of K=E^- is strictly smaller than three. Equation (13) is the contradiction. The two stated full labels are excluded.

## Verification boundary

The new ingredient is the endpoint intersection recovery in Sections2-3. It uses the exact defective inclusion f12 O(16) in O(28), the canonical first-polar and tensor-quartic subbundles, and actual quotient connections. Once the same exact Nplus,N data are established, the public Euler-extension and backward-rank arguments apply with no change to their mathematical hypotheses. The remaining defect-twelve label64d33 and the distinct source2 branch stay open.
