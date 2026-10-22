# Four mixed P4+D5 profiles excluded by octic evaluation

## Result and scope

All four profiles X, Y, Z, U in `MIXED-P4-D5-FORCED-OCTIC-EVALUATION.md` are impossible in the hypothetical `(k,l)=(3,2)` plateau. This closes precisely the two remaining branches `(a,b)=(1,1),(1,2)` of that note. It does not exclude the entire plateau or prove a smoothing theorem; the established SF-rank bound three and square-rank bound 27 are unchanged.

The preceding double-P4 exclusions left ten of 28 formal types. The separately proved single-D5 exclusion leaves nine. Removing the four types proved here leaves **five of 28**, not nine.

The argument uses only universal representations, hypothetical equivariant bundle geometry, backward persistence and degrees. No actual source coefficients, selected actual points, source matrices, rank tests, scans, model spikes or consumed experiments enter. Frozen dependencies are read and executed unchanged.

## 1. Inputs and notation

Use the cited necessary-condition note and its dependencies. Write P=P4, D=D5, Wp=Wprime and T=T6. The four bundles are

    X: (P+D)O(-2)+T O(-3)+O(-8)+O(-10),
    Y: (P+D)O(-2)+T O(-3)+W O(-9),
    Z: (P+D)O(-2)+(V+P)O(-4)+O(-8),
    U: (P+D)O(-2)+Wp O(-3)+V O(-4)+Wp O(-5)+O(-8).

Their ranks are 17, their degrees are -54, and their equivariant Euler characters agree. The plateau has successive ranks 8,11,14,17,20,23 and

    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.

Both backward derivatives have rank three. Positive invariant torsion length is at least twelve. The quadratic image is the saturated line O(8), and its map from `(P+D)O` is complete evaluation. The cubic pairing vanishes. The restricted cubic image `psi:T O -> E*(1)` has rank b=1 or2.

Put A0=E/K. If C=K/K2 is the next actual image, then C embeds in A0(-2) with invariant torsion colength delta. Thus

    deg K2=-54-2 deg A0+6+delta,
    chi(K2(4))=7-2 deg A0+delta.

The next derivative and H0(F0(4))=0 give an injection

    H0(K2(4)) -> H0(C(2)) -> H0(A0).                 (1)

These use actual images; no equality with a saturation is assumed.

## 2. Rank-two cubic image: saturation follows from persistence

Suppose b=2. Let L be the actual image of psi, let Lbar be its saturation in E*(1), and let epsilon=deg Lbar-deg L. Every equivariant Birkhoff–Grothendieck summand of L is globally generated and receives a nonzero map from T O. The universal character test, including central parity, says that every such ordinary degree is at least two; a line first occurs in degree five. A degree-two rank-two block is Wp O(2).

Every ordinary degree of Lbar is also at least two. Indeed, if Lbar had a summand of smaller degree, every map from L to its projection would vanish, contradicting generic rank two of L -> Lbar. Set m=deg Lbar; then m>=4.

The projected image of the full derivative in T O(3) is **Lbar*(3)**. To see why saturation rather than L occurs here, factor psi through the subbundle Lbar. The dual of its inclusion in E*(1) is a surjection onto Lbar*, while dualizing the generically surjective map T O -> Lbar embeds Lbar* in T* O. Thus its actual dual image is Lbar*, regardless of epsilon.

The rank-one kernel of this projection contains the saturated O(8) inside Q, hence equals O(8). Consequently

    0 -> O(6) -> A0 -> Lbar*(1) -> 0.                (2)

All degrees of the quotient are at most -1, so h0(A0)=7 and deg A0=8-m. Formula (1) and Riemann–Roch give

    2m-9+delta <= 7,

hence m<=8. Since deg L>=4, epsilon<=4<12. Invariant torsion therefore forces epsilon=0. This proves saturation even for X with its two high lines; no maximum-target-degree shortcut is used.

Now deg L<=8. A pair of eligible line summands would have degree at least ten. The exhaustive eligible irreducible rank-two list of degree at most eight is

    Wp O(2), W O(4), Wp O(4).

For all four E, `Hom_G(W O(4),E*(1))=0`. Thus L=Wp O(ell), ell=2 or4. The extension (2) splits, since its Ext group is copies of H1(O(5+ell))=0, giving

    A0=O(6)+Wp O(1-ell).

For ell=2, (1) gives delta<=8; for ell=4 it gives delta<=0. In both cases delta=0. The universal Euler characters are

    ell=2: chi_G(K2(3))=-(Wp+S+T),
           chi_G(K2(4))=-A+V+P-D;
    ell=4: chi_G(K2(4))=-A+2V+P.

For ell=4 the coefficient of V in H0(K2(4)) is at least two, whereas H0(A0)=V+P contains only one, contradicting (1).

For ell=2 the exact quotients and the two Euler characters are precisely those of the frozen endpoint in Sections 5–6 of `THREE-P4-QUADRATIC-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md`. Its exhaustive universal classification gives

    K2=(V+P)O(-4)+Wp O(-5)+Htail,
    Htail=O(-8)+O(-10) or W O(-9).

Its subsequent rank-one flag requires the impossible membership

    104 in <96,160,240,60,100,150>.

All hypotheses of that endpoint are the exact quotients, these characters and the plateau vanishings already verified here. The unchanged endpoint verifier is executed by the new verifier. This excludes b=2.

## 3. Rank-one cubic image: a dimension bound before splitting

Suppose b=1. The necessary-condition note proves the saturated image is O(e), with e=11 only for X, or e=9 for any of X,Y,Z,U. Its actual projected dual image is O(3-e). Let C0 be the rank-two kernel of the projection from the full image I to this line. It contains saturated O(8) and embeds in Q. Hence

    0 -> O(8) -> C0 -> O(n) -> 0,

where n is even and n<=6, by the largest-two-degree bound fourteen. This sequence splits since H1(O(8-n))=0. Twisting the full image sequence yields

    0 -> O(6)+O(n-2) -> A0 -> O(1-e) -> 0.           (3)

At this stage we do **not** assume (3) splits. It always gives

    deg A0=n+5-e,
    h0(A0)<=7+max(n-1,0).                           (4)

Since all fourteen degrees of K are at most -3, deg K<=-42. But deg K=e-n-59, so n>=e-17.

The quotient onto O(n-2) is supplied by the Htail identified in Section 4 of the necessary-condition note. Indeed, remove the quotient E -> O(1-e); the remaining quadratic summand maps onto O(6) by complete evaluation. After taking the quotient by O(6), Htail must surject onto O(n-2). Necessary nonzero universal Hom tests in the finite interval e-17<=n<=6 give exactly

    e=11, X: n=-6,4,6;
    e=9, X or Y: n=-8,4,6;
    e=9, Z or U: n=4,6.

These are necessary lists only, not claims that the quotient maps exist.

By (1), (4) and Riemann–Roch,

    2e-2n-3+delta <= 7+max(n-1,0).                  (5)

Every negative n is impossible: the left side is at least 31 and the right side is seven. In particular, no splitting of (3) has been used for n=-8. The pair (e,n)=(11,4) is also impossible, giving 11<=10. The remaining possibilities are

    (e,n)=(9,4),(9,6),(11,6).

Their upper bounds on delta are respectively 3,9,5, all below twelve, so delta=0.

## 4. Final low-degree bottleneck

For the remaining positive n, (3) does split: both extension groups vanish since 5+e and n+e-3 are at least -1. Thus

    A0=O(6)+O(n-2)+O(1-e),
    K/K2=A0(-2),
    deg K2=2e-2n-58.

The next rank-three derivative targets A0(-4), whose last summand is O(-e-3). Full rank forces a nonzero projection to that line, so K2 has an ordinary summand of degree at most -e-3. All eleven degrees are at most -4. Therefore

    deg K2<=-40-e-3.

For (9,4), its required degree is -48 but the bound is -52. For (11,6), its required degree is -48 but the bound is -54. Both are impossible.

For (9,6), equality holds at degree -52. It forces exactly ten degree-minus-four dimensions and one degree-minus-twelve line:

    K2=U0 O(-4)+O(-12).

The line has trivial coefficient representation. Subtracting the exact quotients from each E gives chi_G(K2(4))=V. Since H1(O(-8))=Sym^6 W=V+P, necessarily U0=2V+P. But (1) would require

    2V+P -> H0(A0)=V+P+D

to be injective, impossible on the multiplicity of V. This excludes b=1 and completes the four-profile exclusion.

## Reproduction

Run `python3 verify_mixed_p4_d5_octic_exclusion.py`. It runs frozen dependencies unchanged and checks the minimum image degrees, the low-degree image list and target Hom vanishing, saturation bounds, exact Euler characters and endpoint hypotheses, all five Htail quotient lists, the dimension-only negative-n exclusions, every torsion bound, both degree bottlenecks, the final representation contradiction and the remaining count five.
