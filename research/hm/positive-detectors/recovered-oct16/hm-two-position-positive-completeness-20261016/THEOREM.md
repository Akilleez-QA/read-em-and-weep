> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# A second Laurent position detecting the missing four directions

Status: **independent PASS**, including the new-position trace, four quotient columns, and the exact twelve-test basis reduction in section4a. The latter was checked directly against the existing quotient formulas, without new products. See ../hm-second-kappa-independent-20261016. No actual source values are computed by this theorem.

Independent records: ../hm-second-kappa-independent-20261016/AUDIT.md (SHA256796bcb61b64ac96b69be9762243f109cb0b24ae0894a0fef0bcfe01d8055f87e) and MINIMAL-TWELVE.md (SHA2569706c182e70e547cd25f0acc02e8b6593fb0d7b387518b6ea1c18a2a1ca253b8).

## Result

Keep the specified global epsilon splitting and inversion-positive target

    W+ = H²(B(-3))+ direct_sum H²(B(-4))+, dimensions8+4,

with B=End(L) in the authenticated genuine degrees. All30 negative-block constant scalar maps at the original Laurent position

    kappa0=(-1,-1,-3,-3)

have kernel {(-v2 eta,eta,0): eta in H²(B(-4))+}, dimension4.

One additional admitted Laurent position suffices to separate that kernel:

    kappa1=(-2,-1,-2,-1).

Indeed four specified members of the constant scalar basis at kappa1 give all four coordinates of the second summand. Together with the original all30-at-kappa0 family, they separate W+. This is a structural completeness statement; no actual source scalar is evaluated.

The detector here is the negative-block constant family. It is not the positive detector ell(n,p)=p[7]-p[25] or its78-summand Phi.

## 1. Authenticated coefficient-position correspondence

The scalar coefficient is a class in H⁴((P1)^4,O(-4,-4,-4,-4)), with the existing ordered tensor trace. For a Laurent basis element x^kappa, its Serre-dual monomial is

    q_kappa = product_i X_i^(-kappa_i-1) Y_i^(kappa_i+3).

Each factor has degree2. Multiplication followed by the canonical coefficient trace at(-1,-1,-1,-1) picks exactly the kappa coefficient. This formula reproduces the authenticated original weight

    q_kappa0 = X3²X4²Y1²Y2².

For kappa1 it gives

    q1=X1Y1 Y2² X3Y3 Y4²,

whose affine expression is x1x3. Every coordinate of kappa1 is in{-3,-2,-1}, so it belongs to the original81-position finite-model family. There is no shift guessed from a raw source numerator and no new affine normalization.

## 2. Exact homogeneous trace without a polynomial sweep

Let H be the order-eight pair stabilizer. The four distinct H translates of the degree-one cross-pair monomial X1X3Y2Y4 sum to v2-U; each occurs twice in H. Since v0=Y1Y2Y3Y4,

    average_H(q1)=v0(v2-U)/4.

For an epsilon section aG, replacing q1 by this ordinary H-average does not change its unnormalized S4 alternant: the epsilon sign of aG cancels the sign from reindexing Alt.

The already proved dual-trace kernel is W1=(U-v2)/8. Consequently

    average_H(q1)=-2v0 W1.

Using the existing identities Alt(W1 a U^j)/Delta=delta_(1,j), one obtains the full trace triple

    (Alt(q1 a)/Delta,
     Alt(q1 aU)/Delta,
     Alt(q1 aU²)/Delta) = (0,-2v0,0).

This is a global identity, valid at infinity and ramification; its final expression has no variable denominator. It introduces no extra factor1/8 or1/24. In particular, the new position extracts a v0-weighted second component and annihilates both other epsilon summands.

For every constant dual cycle E, the scalar value at kappa1 is therefore

    D_(E,kappa1)(G0,G1,G2)=-2 <G1,v0 E>.

Twists match: E represents H²(B(-2)), v0E represents H²(B(-1)), and G1 lies in H²(B(-4)). The product in the Serre trace has degree-5 on P4. Polynomial multiplication commutes with the complete total differential and must include full primitives when applying it to d5 boundaries.

## 3. Constant basis and cached quotient maps

Use index r=15b+i, with b=0,1 and i=0,...,14. The constant scalar map L_(i,b) corresponds to the global cycle E_r with

    E13[b,i]=1,
    E02[5b+k,a]=gamma[i,a,k],

and all other coefficients zero. These are the genuine supertrace conventions already authenticated for the all30 family.

The positive projection is mandatory: v0 alone is exchanged with v4 by inversion. In the ambient400-dimensional degree+2 section space for B(-1), let Pplus=(1+I)/2. The saved196-dimensional positive basis uses e_j+s e_j′ on two-element orbits and no built-in half. Thus an ambient coordinate contributes1/2 or s/2 to the corresponding positive basis coordinate. Fixed positive coordinates contribute1; fixed negative coordinates vanish.

Let Q:Q^196->Q^4 and L:Q^196->Q^123 be the already certified quotient and boundary-lift maps, with differential A and quotient cycle columns C0,...,C3. The cached certificate gives, for every positive cycle z,

    z=A L(z)+sum_j (Qz)_j Cj.

The single fixed-map pass recorded in v0-map.json reports

    Q(Pplus v0 E9)  = (1/2,0,0,0),
    Q(Pplus v0 E4)  = (0,-1/2,0,0),
    Q(Pplus v0 E5)  = (0,0,1,0),
    Q(Pplus v0 E12) = (0,0,0,1/2).

These four columns form an explicit diagonal spanning set, without an elimination or rank routine. Their exact original-column boundary witnesses are specified by the cached map itself:

    L(Pplus v0 E9), L(Pplus v0 E4),
    L(Pplus v0 E5), L(Pplus v0 E12).

No new lift computation is asserted here. The saved certificate's universal identity supplies each witness once these inputs and quotient values are independently authenticated.

## 4. Consequence for the twelve-coordinate interface

In the existing coordinates wj=<G1,Cj>, inversion-positive G1 pairs only with the positive projection of its dual cycle. Thus the four new scalar values, in order r=9,4,5,12, are

    -w0, +w1, -2w2, -w3.

All four vanish if and only if G1=0. If the original all30 single-position outputs also vanish, their exact kernel equation gives G0=-v2G1=0; G2=0 already holds in W+. Hence the union of the two position families is injective on W+.

One total position is insufficient for this original family, by its previously proved four-dimensional kernel. Thus, with the original position retained, the two-position set is minimal in number of positions. This does not claim that every single position has rank below12 or that these are an optimal source-arithmetic schedule.

## 4a. Exactly twelve specified scalar tests suffice

The four new columns and the eight old-row identification below have independent acceptance. The original all30 family reduces to eight specified original rows, without computing any further quotient entries.

At kappa0 select K30 indices

    r=(0,1,5,6,10,11,15,16).

In the constant scalar notation L_(i,b), these are

    L_(0,0), L_(1,0), L_(5,0), L_(6,0),
    L_(10,0), L_(11,0), L_(0,1), L_(1,1).

At kappa1 select the four already specified rows

    r=(9,4,5,12), namely
    L_(9,0), L_(4,0), L_(5,0), L_(12,0).

Using the pinned finite-model coordinate number

    k=27(kappa_1+3)+9(kappa_2+3)+3(kappa_3+3)+(kappa_4+3),

the original and new positions are k=72 and k=50 respectively. Thus the twelve row/position IDs are unambiguously the eight (r,72) pairs above and four (r,50) pairs above. The same row r=5 occurs at two different positions.

This ordering is authenticated by section1 of the pinned `current-scalar-proof/structural-relations.md` (Git blob d48c88141e80f0005cf598d4796d6f358d45f07a) and the literal `mons(-3,-1)` loop used by `makeBasis(-2,4)` in the pinned finite-model oracle (Git blob8f534fd7a074e333fa031a6d8c51b864faf76d42). The loops run the first exponent outermost and fourth innermost. The scalar rows themselves are section3's declared L_(i,b), bound to the literal gamma coefficients in modelJSON SHA256635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926.

The index r=15b+i is the authenticated K30/E13 coordinate. It is **not** claimed to be a flattened2430-row ordinal in an arbitrary serialization of S; both i and b are given explicitly in twelve-tests.json. In particular, the historical current scalar map is -L_(10,0), whereas old_4 here is +L_(10,0). A consumer using that historical scalar must retain this sign conversion.

The first dual quotient retains e0,...,e19, with the complete d5 relations already incorporated. Its positive basis is

    P_(b,s)=e_(5b+s)-e_(5b+4-s),
    b=0,...,3, s=0,1.

Inversion sends e_(5b+s) to -e_(5b+4-s). Hence the positive projection of each selected original row's dual class is exactly P_(b,s)/2. These are the specified eight basis classes P0,...,P7, not an inferred basis from dimension alone.

Let y_i denote the corresponding original-position scalar value, in the displayed order. The original trace triple gives

    y_i=2z_i+2<G1,v2 P_i>, i=0,...,7.

No values of the second term are computed here. It is a well-defined linear function of the already specified four coordinates w. The four new tests give (-w0,+w1,-2w2,-w3). Therefore vanishing of those four tests implies G1=0, after which vanishing of the eight old tests gives all z_i=0. This proves completeness.

Equivalently, the twelve tests have a block triangular coordinate matrix with upper-left block2I8 and lower-right block diag(-1,1,-2,-1). Both diagonal blocks are invertible over Q. The unspecified upper-right block is irrelevant to injectivity, and no rank routine or additional map product is needed.

Since W+ has dimension12, fewer than twelve scalar linear values cannot separate every class in it. Thus these twelve tests are cardinality-minimal among scalar linear tests on the entire specified positive target. This minimality is distinct from computational cost: it does not certify source acquisition or a cheapest implementation.

## 5. Exact scope of the fixed-map pass

The input is the authenticated homogeneous gamma data and saved linear certificates only. The code reads gamma; it does not use the nonlinear chart arrays in the same model file. The source and certificate hashes, all30 projected output columns and execution receipt are retained in v0-map.json. check_v0.py records the precise projection and basis conventions.

The independent review verified the position map, trace normalization, gamma graph, mandatory positive projection, closedness and all four saved-map values. Its exact Cox-ring alternation gives the full triple(0,-2v0,0). It used856 universal coefficient products, with no elimination or source values, and separately verified the producer's80 projector/14 quotient-product counts. It then checked the old eight basis classes textually, including the important relations e20=-e10 and e21=-e11: rows10/11 are retained quotient directions, not zero classes. This verifies the invertible block triangular map without any further products. Any use on an actual source requires its complete corrected-source binding and regular cover comparison.

## Existing sources

- ../hm-pr80-scalar-completeness-independent-20261016/THEOREM.md: exact original-position kernel.
- ../hm-epsilon-projective-generator-bridge-20261016/THEOREM.md: specified epsilon splitting, trace, supertrace and original kappa normalization.
- ../DUAL-TRACE-IDENTITIES.md: W1 and the nine exact dual-trace identities.
- ../hm-positive-twelve-detector-interface-20261016/interface.json: the z/w coordinates and dual cycles.
- ../hm-plus-twist-minus1-quotient-20261016/certificate.json: saved positive bases, Q, L and complete original-column identities; SHA256616006681d2952a3d895e2bf369d2c5813a9091c38a490b9bd936c2299e5de3c.
- ../hm-factored-coefficient-action-20261014/pinned-model-input.json: authenticated linear gamma literals; nonlinear chart arrays unused.
- Pinned scalar row and Laurent-position definitions: https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/structural-relations.md , sections1 and3.
- Pinned basis loop: https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js , mons and makeBasis.
