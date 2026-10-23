# A source-free split backward-descent obstruction

## Statement and dependency boundary

Work over C with the binary icosahedral group G and its standard representation W. Write U[d]=U tensor O(d), and omit the trivial coefficient 1 when convenient. The irreducibles are 1,W,Wp,A,V,S,P,D,T of dimensions 1,2,2,3,3,4,4,5,6, with A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W. All are self-dual. Every nonempty invariant effective divisor on P1 has degree at least 12.

**Universal split-descent lemma.** Suppose an actual negative saturated bundle K2 in a constant bundle with its trivial connection has:

    rank K2=12, deg K2=-60, maxdeg K2<=-4,
    chi_G(K2(4))=V-A,
    chi_G(K2(5))=-W+Wp+2T.

Suppose the split target O(0)+O(2) is an actual subbundle of (H O/K2)(-2) containing its actual derivative image, so the induced map K2 -> O(0)+O(2) has exactly the actual derivative kernel and raw image. Suppose its subsequent actual backward derivatives have generic rank at most two, and the usual Gauss factorization holds: for Ki+1=ker(beta_Ki), beta_Ki+1 factors through (Ki/Ki+1)(-2). Then no such actual configuration exists.

All kernels here are actual connection kernels, hence saturated in the original constant ambient bundle. Every image called a quotient below is the raw image sheaf, not its saturation. Torsion is retained wherever present. The lemma has no source-bundle, quartic-subsystem, or balanced-target hypothesis.

The strict-top theorem and representation conventions are pinned in PR814, commit 1f94be65b3a470a1b594e61d56df7f6057c9d907:
https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

The source-free bounded support table used in Section 3 and the elementary evaluation-kernel identities used later are also available in PR823, commit 399abe93debe71232f0b7808fc8f1a5582118708:
https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-THIRD-BACKWARD-QUOTIENT.md
https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-FINITE-BACKWARD-DESCENT.md

Their SHA256 hashes are respectively 16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0 and 9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49. No balanced quotient assertion is imported. The split channels, kernels, exact images, defect alternatives, and final contradiction are proved here.

## 1. Elementary tools and character conventions

Strict-top says that if maxdeg K<=-m, then maxdeg K^-<=-m-1, and H0(K(m)) injects into H0 of the actual derivative target at twist m. A nonzero negative saturated bundle cannot be horizontal in a constant bundle.

The prescribed K2 Euler characters also force center-even parity, rather than requiring an unstated ambient assumption. Split K2 into its central-sign subbundles. Its center-odd summand has zero Euler character at twist four, since V-A is even, and at twist five, since twisting reverses central parity and -W+Wp+2T is odd. Its numerical Euler characteristics therefore vanish at two consecutive twists; their difference is its rank, so this summand is zero. All subsequent actual kernels inherit center-even parity. Thus a coefficient U at degree -j has parity U=(-1)^j.

For equivariant line systems, a nonzero irreducible subsystem of degree n<12 is basepoint-free: its common zero divisor is invariant and has degree at most n. For the complete Sym^n W evaluation map,

    ker(Sym^n W[-m] -> O(n-m))=Sym^(n-1) W[-m-1].       (1)

Useful characters are

    Sym0=1, Sym1=W, Sym2=A, Sym3=S, Sym4=D, Sym5=T,
    Sym6=V+P, Sym7=Wp+T, Sym8=P+D, Sym9=S+T,
    Sym10=A+V+D, Sym11=W+S+T, Sym12=1+A+P+D,
    Sym14=A+V+P+D.

In particular the invariant line in Sym12 is unique, and Sym2,4,6,8,10,14 have no invariants. These identities follow by the recurrence Sym(n+1)=W Sym(n)-Sym(n-1), using

    W^2=1+A, WA=W+S, WS=A+D, WD=S+T,
    WT=V+P+D, WV=T, WP=Wp+T, WWp=P.

Two further basepoint-free kernels will be used:

    ker(P[-6] -> O)=V[-8],
    ker(V[-8] -> O(-2))=Wp[-11].                        (2)

For the first, after twist six its kernel has rank three, degree -6, no constant sections and H1 budget V. A block U[-j], j>=2, contributes U Sym(j-2) to that budget. The sole possibility is V[-2]: at j=3 the smallest odd coefficient already contributes dimension four; at j=4 the trivial coefficient gives A, not V; later admissible degrees exceed the budget. Rank then leaves no degree-minus-one block.

For the second, twist eight. Its rank-two degree-minus-six kernel has no constant sections. Equivariant splitting and central parity leave W[-3], Wp[-3], or O(-2)+O(-4). The last is impossible because its twist-two trivial section would inject into V Sym2=P+D. At twist three,

    V Sym3-Sym9=(Wp+S+T)-(S+T)=Wp,

so the coefficient is Wp. All maps in (2) are nonzero unique irreducible degree-six systems, hence onto by the preceding divisor argument.

An extension 0->U[a]->M->Z[b]->0 splits equivariantly whenever H1(O(a-b))=0; take G-invariants of ordinary Ext and use exactness of invariants over C. Every extension used below has a-b>=-1. Where both rows and all lower components vanish separately, the kernel is already a direct sum, requiring no Ext assertion.

## 2. The first quotient is exactly O(0)+O(2)

Since chi(K2(4))=V-A, H0(K2(4)) contains V. Thus K2 has an actual top subblock V[-4]. Its derivative has no component to O(0), because V is absent from Sym4=D. Strict-top makes its component to O(2) nonzero. That is a basepoint-free degree-six V system. Hence the full image contains the entire direct summand O(2).

Put K3=ker(beta_K2). Strict-top gives maxdeg K3<=-5. The actual derivative has rank one or two.

### 2.1 Rank one is impossible

A rank-one raw image containing O(2) in O(0)+O(2) is exactly O(2). In this case

    H1(K3(4))=A+P,    chi(K3(5))=T-W.                 (3)

For degree-minus-j blocks j>=6 the H1 budget in (3) supports only A[-6], P[-6], Wp[-7], and O(-8), with respective twist-five H1 characters 0,0,Wp,W. This is the corresponding subtable of Section 3 and can equally be checked directly by the dimension bound (j-5)dim U<=7 and central parity.

The negative W in chi(K3(5)) forces O(-8), consuming A. The remaining P budget gives exactly two necessary possibilities:

    T[-5]+P[-6]+O(-8),
    (T+Wp)[-5]+Wp[-7]+O(-8).

The derivative target for K3 is O(0), whose twist-five sections are T. Strict-top excludes the Wp top in the second possibility. In the first, the T[-5] top is the complete quintic system onto O(0). Its kernel is D[-6]. The rest of K3 gives an extension of P[-6]+O(-8) by D[-6], split since the degree differences are 0 and 2. Therefore

    K4=(P+D)[-6]+O(-8).

Its derivative targets O(-2), and strict-top at twist six would inject P+D into Sym4=D. Contradiction.

### 2.2 A rank-two torsion defect is impossible

The raw image I contains O(2). Its projection to O(0) is an invariant ideal line O(-d), d>=0. Since the target is split and O(2) is contained in I,

    I=O(2)+O(-d).

If d>0, invariance gives d>=12. The exact quotient and H0(K3(4))=0 then give

    H1(K3(4))=A+P-Sym^(d-6) W.                      (4)

Dimensions force d-5<=7, hence d<=12. At d=12 the right side is A+P-(V+P)=A-V, not genuine. Thus d=0 and

    K2/K3=O(0)+O(2),
    rank K3=10, deg K3=-62, maxdeg K3<=-5.           (5)

In particular no saturation has been silently substituted for I.

## 3. Complete small support for K3

Subtracting (5) from the two input characters gives

    H1(K3(4))=A+P+D,    chi(K3(5))=-W.               (6)

For an irreducible block U[-j], j>=6, its contribution to the first budget is U Sym(j-6). The bound (j-5)dim U<=12 and parity U=(-1)^j give precisely:

    block       H1 at twist4    H1 at twist5
    A[-6]           A                0
    P[-6]           P                0
    D[-6]           D                0
    Wp[-7]          P                Wp
    S[-7]           A+D              S
    O(-8)           A                W
    V[-8]           P+D              T
    W[-9]           A+D              W+S
    O(-10)          D                S
    Wp[-11]         A+P+D            S+T
    O(-14)          P+D              Wp+T.

Completeness is bounded and elementary. At j6 only A,P,D fit. At j7, W^2=1+A is forbidden while Wp W=P and S W=A+D fit; T W includes V. At j8 the coefficients 1,A,V,P are the only dimension candidates; A^2 contains 1 and P A contains V, leaving 1 and V, with V A=P+D. At j9 only W,Wp fit and W S=A+D survives whereas Wp S=V+D does not. At j10 only 1 fits. At j11 only W,Wp fit, with W T containing V and Wp T=A+P+D. At j12 only 1 fits and gives Sym6=V+P, forbidden. Odd j>=13 exceed the bound. Even j14,16 allow only 1 and give P+D, A+V+D respectively. Even j>=18 exceed the bound too.

Only O(-8) and W[-9] supply W to H1 at twist five; precisely one must occur, and each consumes A. Matching the remaining P,D budget and chi=-W gives the complete eight-type necessary list:

    S[-5]+P[-6]+W[-9];
    (S+Wp)[-5]+Wp[-7]+W[-9];
    (P+D)[-6]+O(-8);
    S[-5]+P[-6]+O(-8)+O(-10);
    Wp[-5]+D[-6]+Wp[-7]+O(-8);
    (Wp+S)[-5]+Wp[-7]+O(-8)+O(-10);
    T[-5]+(V+1)[-8];
    (Wp+T)[-5]+O(-8)+O(-14).

The derivative of K3 targets O(-2)+O(0). Its twist-five sections are S+T, so strict-top removes exactly the four types having Wp at degree minus five. The surviving types are

    I:   S[-5]+P[-6]+W[-9];
    II:  (P+D)[-6]+O(-8);
    III: S[-5]+P[-6]+O(-8)+O(-10);
    IV:  T[-5]+(V+1)[-8].                            (7)

Each has rank ten and degree minus sixty-two. This is a necessary overlist, not a claim of realization. It is the same support calculation as the public PR823 table, but the target here is split; all remaining derivative arguments are rederived next.

## 4. Force K3/K4=O(-2)+O(0), including the new type IV

In I and III, S[-5] maps only to O(-2), via its complete cubic system: Hom to O(0) vanishes since S is absent from Sym5=T. Strict-top makes this first row onto. Only P[-6] can reach O(0): W is absent from Sym9=S+T, and invariants are absent from Sym8,10. If P had zero O(0) component, the raw image would be O(-2). Its kernel would have top (A+P)[-6], since the cubic kernel is A[-6], P also has no component to O(-2), and the extension splits. The next derivative would target O(-4), whose twist-six sections are A, contradicting strict-top. Thus the P degree-six row is nonzero and basepoint-free. Both target lines are supplied exactly.

In II the two top irreducibles separate: D[-6] maps only to O(-2), because D is absent from Sym6=V+P; P[-6] maps only to O(0), because P is absent from Sym4=D. Strict-top requires both nonzero. The complete quartic D row and the degree-six P row are onto, giving the whole split target.

In IV, T[-5] maps only to O(0), through its complete quintic system. The O(-8) summand has no component to either target. V[-8] can map only to O(-2): V is absent from Sym8=P+D. If that degree-six V row is nonzero, it is onto and the claim follows.

Suppose it vanishes. Then the raw quotient is O(0), and the next kernel is D[-6]+(V+1)[-8]. Its derivative targets O(-2), and its D top gives the complete quartic row. Consequently its kernel is S[-7]+(V+1)[-8], even if the V[-8] row into O(-2) is nonzero: the extension by S[-7] splits by degree difference 1. The next derivative targets O(-4), whose only nonzero top row is the complete cubic S system. V[-8] and O(-8) have zero components to O(-4), because Sym4=D. Its kernel is (A+V+1)[-8], whose derivative targets O(-6). Strict-top would inject A+V+1 into Sym2=A. Contradiction.

Thus in every case

    K3/K4=O(-2)+O(0).                               (8)

The separate-row kernels (1),(2) now give exactly:

    a: K4=S[-7]+(V+1)[-8];
    b: K4=A[-6]+V[-8]+W[-9];
    c: K4=A[-6]+(V+1)[-8]+O(-10);
    d: K4=D[-6]+O(-8)+Wp[-11].                      (9)

The correspondences are II->a, I->b, III->c, IV->d. All have rank eight, degree -60. In d the D kernel comes from the complete quintic T row and Wp[-11] from the V sextic row. This fourth type is genuinely new to the split target and cannot be dropped by importing a balanced overlist.

For b,c the lower W[-9], O(-8), O(-10) maps into (8) vanish separately: W is absent from Sym7,9 and 1 from Sym6,8,10. For a the O(-8) maps vanish as well. Thus these are direct kernel sums. There is no hidden extension or divisor correction in (9).

## 5. The a,b,c alternatives force two more full split quotients

The derivative target for K4 is O(-4)+O(-2). In a, S[-7] maps only onto O(-4), by the complete cubic system. In b,c, A[-6] maps only onto O(-4), by the complete quadratic system. These top maps are nonzero by strict-top. The only component capable of reaching O(-2) is V[-8], via the degree-six V system. Every other lower component is zero, using W absent from Sym5,7 and 1 absent from Sym4,6,8.

If V were zero in a, the raw quotient would be O(-4), with kernel (A+V+1)[-8]. Its derivative targets O(-6), and strict-top fails against Sym2=A.

If V were zero in b,c, the raw quotient would again be O(-4). Its kernel has W[-7] top and retains V[-8]. Its next derivative targets O(-6), where the W top is the complete linear system, onto. V has no component to that line because V is absent from Sym2=A. Hence the following kernel contains V[-8] and has maximum degree at most -8. Its derivative targets O(-8); strict-top at twist eight would inject a representation containing V into 1. Impossible.

Therefore

    K4/K5=O(-4)+O(-2)                               (10)

for a,b,c, with exact kernels

    a: (A+1)[-8]+Wp[-11];
    b: W[-7]+W[-9]+Wp[-11];
    c: W[-7]+O(-8)+O(-10)+Wp[-11].                 (11)

All have rank six, degree -54. Type a is immediately impossible: the next derivative target is O(-6)+O(-4), with twist-eight sections A+D, which has no trivial coefficient, whereas its top has A+1.

For the remaining b,c, the W[-7] top maps only onto O(-6), by its complete linear system. Only Wp[-11] can reach O(-4); its degree-seven system is nonzero exactly when that row is onto. The other lower components are zero since W is absent from Sym3,5, 1 from Sym2,4,6, and Wp from Sym5=T.

If the Wp row vanished, the raw quotient would be O(-6), with kernel respectively

    O(-8)+W[-9]+Wp[-11],
    2 O(-8)+O(-10)+Wp[-11].

The latter cannot have an injective strict top into O(-8) at twist eight. In the former the top O(-8) isomorphically supplies that next derivative target. Eliminating any lower graph into this isomorphic line gives the next kernel W[-9]+Wp[-11]. Its derivative targets O(-10), and strict-top at twist nine fails because the target has no sections.

Thus

    K5/K6=O(-6)+O(-4),                              (12)

and the kernels are respectively

    O(-8)+W[-9]+O(-18),
    2 O(-8)+O(-10)+O(-18).                         (13)

Indeed the W top kernel is O(-8), and the onto Wp[-11]->O(-4) kernel is the line O(-18) by degree. The rows are separate; equivalently any extension of O(-18) by O(-8) has H1(O(10))=0. The second kernel in (13) is impossible: its derivative target O(-8)+O(-6) has twist-eight sections 1+A, containing only one trivial copy, not two.

## 6. The remaining b branch has a forced degree-twelve raw image

We are left with

    K6=O(-8)+W[-9]+O(-18),
    target(beta_K6)=O(-8)+O(-6).

Strict-top makes the O(-8) source isomorphic onto the O(-8) target line; its component to O(-6) is zero. W[-9] has no component to O(-6), since W is absent from Sym3=S. Only O(-18) can reach that quotient line, and its component is a scalar multiple of the invariant f12.

If it were zero, the raw image would be O(-8), and eliminating the possible W[-9] graph into this isomorphic top line leaves kernel W[-9]+O(-18). The next target is O(-10), contradicting strict-top at degree nine. Therefore f12 is nonzero.

Retain its divisor. The actual rank-two image is

    K6/K7=O(-8)+O(-18) subset O(-8)+O(-6),          (14)

with determinant defect 12. The two displayed source lines map injectively as a rank-two sheaf, and every W[-9] image is already inside the first line. The kernel, after removing that graph, is K7=W[-9]. Its actual derivative factors through the twist of (14), namely

    O(-10)+O(-20).

All maps from W[-9] to that target vanish by ordinary degrees. K7 would be negative and horizontal in a constant bundle, a contradiction.

## 7. The new d alternative also contradicts strict-top

For d in (9), K4=D[-6]+O(-8)+Wp[-11], with target O(-4)+O(-2). D[-6] maps only onto O(-2), by the complete quartic system. The O(-8) block has no component to either line. Wp[-11] has no O(-2) component because Wp is absent from Sym9=S+T; its only possible row is the degree-seven Wp system to O(-4).

If the Wp row were zero, the raw quotient would be O(-2) and

    K5=S[-7]+O(-8)+Wp[-11].

Its derivative targets O(-4), and the S top supplies the complete cubic row. Regardless of any lower Wp component to this same line, its kernel is

    K6=(A+1)[-8]+Wp[-11],

because Ext1(Wp[-11],A[-8]) has degree difference 3 and vanishes. The O(-8) component to O(-4) is zero. Its next derivative target is O(-6), and strict-top fails: A+1 cannot inject into A.

Thus the Wp degree-seven row is nonzero and onto. The quotient is O(-4)+O(-2), and its exact kernel is

    K5=S[-7]+O(-8)+O(-18).                         (15)

Its derivative targets O(-6)+O(-4). The S top maps only onto O(-4), via the complete cubic system; O(-8) has zero components. The only possible O(-6) row is O(-18)->O(-6), a scalar multiple of f12. The O(-18)->O(-4) channel is zero since Sym14 has no invariant, although allowing such a graph would not change the argument.

If f12 is zero, the raw quotient is O(-4), and its kernel is (A+1)[-8]+O(-18). Its derivative targets O(-6), and strict-top again fails at twist eight.

If f12 is nonzero, retain its entire length-twelve defect. The raw image is O(-4)+O(-18), and the kernel is (A+1)[-8]. Its derivative targets O(-6)+O(-20). At twist eight this target has sections A only, so strict-top again cannot inject A+1.

This excludes d. Together with Sections 2–6 it proves the universal split-descent lemma.

## Verification and scope

The proof exhausts rank one and rank two at its initial interface, retains the only possible initial defect and both terminal f12 defects, and checks the split-specific IV/d alternative independently. Full-image claims arise from separate basepoint-free rows or from explicit ideal-sheaf decomposition, not from an imported balanced quotient. Ordinary Ext degrees used in kernel identifications are all at least -1; graph eliminations use an actual isomorphic top row.

This is a universal formal exclusion conditional only on its stated actual-connection interface. It is not a source or label count by itself. It uses bounded abstract character identities and exact sequences only: no selected HM/source coefficients, parameters, points, evaluated derivatives, matrices, instance ranks, experiments, scans, or unapproved large computation.
