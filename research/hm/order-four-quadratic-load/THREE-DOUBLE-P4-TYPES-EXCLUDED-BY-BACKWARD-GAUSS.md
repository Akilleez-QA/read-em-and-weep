# Three double-P4 types are excluded by backward Gauss persistence

## Result and scope

For the hypothetical generic-SF-rank-three plateau `(k,l)=(3,2)`, all three remaining formal primal types with quadratic section module `2P4` are impossible:

    X: (0,1,0,0,1,0,0,1), E=2P O(-2)+T O(-3)+Wp O(-5)+O(-10);
    Y: (0,0,1,1,1,0,0,0), E=2P O(-2)+(V+P) O(-4)+Wp O(-5);
    Z: (1,0,1,0,2,0,0,0), E=2P O(-2)+Wp O(-3)+V O(-4)+2Wp O(-5).

Here P=P4, Wp=Wprime, A=Sym^2 W, S=S4, D=D5, T=T6. These are three new exclusions, disjoint from the fifteen exclusions checked in `verify_three_p4_backward_gauss.py`. Thus at most ten of the original 28 formal primal types remain. This is not a full adjacent-profile exclusion or a realizability statement. SF rank >=3 and square rank >=27 remain unchanged; no smoothing closure follows.

Only universal representation arithmetic and hypothetical equivariant bundle geometry are used. No actual HM/source coefficients, source-instance matrices or ranks, selected points, parameter scans, local models, or consumed experiments enter.

## 1. Frozen input

Read `THREE-P4-QUADRATIC-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md`, `P4-ZERO-PAIRING-EXCLUDED-BY-BACKWARD-PERSISTENCE.md`, and their unchanged dependencies, especially `SIX-LARGE-QUADRATIC-MODULES-EXCLUDED-BY-BACKWARD-GAUSS.md` and `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`.

The saturated plateau has ranks 8,11,14,17,20,23, with middle stages F0<K2<K<E, deg E=-54, and

    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.

The derivatives of K and K2 have rank three. Every positive invariant torsion length is at least twelve. The five possible Q bundles have largest degree at most eight and largest-two-degree sum at most fourteen. Every E above has the same equivariant Euler characteristics as the three frozen single-P types.

Put phi:2P O -> Q, psi:T O -> E*(1), and let B:2P O -> T O(3) be their pairing. Both restricted derivatives are section-injective. Write a,b,t for their ranks. Then a+b-3<=t<=min(a,b), and either B=0 or its saturated image is Wp O(1).

A rank-one phi is impossible: its globally generated line image would be O(n) for even 0<=n<=8 and would have to contain two P copies in sections. None of these symmetric powers does. Thus a>=2 throughout.

## 2. Nonzero pairing: the exact quotient and frozen endpoint

Suppose B is nonzero. If a=2, the generic kernels of B and phi coincide and therefore their saturated sheaf kernels coincide. But B maps the section module 2P onto P, so its kernel contains a nonzero P section module, contradicting section injectivity of phi. Hence a=3 and the rank inequality forces b=2.

Let I be the actual full image of beta_E(2):E(2)->Q. The projection of I into T O(3) has rank b=2 and contains the saturated image Wp O(1) of B, so equals it. Its rank-one kernel N lies in Q, and therefore N=O(n), with n even and n<=8. The P kernel of the section map of B injects into H0(N). Testing symmetric powers forces n=6 or 8. The extension splits since H1(O(n-1))=0, giving the actual quotient

    A_n=E/K=O(n-2)+Wp O(-1).

No saturation of I in Q is presumed. Write C=K/K2 inside A_n(-2), with torsion cokernel length delta. Riemann--Roch and section persistence give

    15-2n+delta = chi(K2(4)) <= h0(K2(4)) <= h0(A_n)=n-1.

For n=6,8 this bounds delta by two,eight respectively. The invariant gap forces delta=0. For n=6 the exact equivariant Euler character is chi_G(K2(4))=V, whereas H0(A_6)=D; section persistence is impossible.

For n=8 the two exact quotients are

    E/K=O(6)+Wp O(-1), K/K2=O(4)+Wp O(-3).

Since all the E types have the same Euler characters, the exact hypotheses of Sections 5-6 of the frozen three-single-P note apply unchanged:

    chi_G(K2(3))=-(Wp+S+T),
    chi_G(K2(4))=-A+V+P-D.

Its exhaustive positive-character classification gives exactly

    K2=(V+P)O(-4)+Wp O(-5)+Htail,
    Htail=W O(-9) or O(-8)+O(-10).

Its endpoint proof then gives F0=T O(-5)+Htail, a rank-eight, degree-minus-48 bundle with rank-one derivative and smallest constant span of dimension thirteen. Invariant ramification would require

    104 in <96,160,240,60,100,150>,

which is impossible. The companion verifier runs this frozen exhaustive classification and endpoint check unchanged, and checks the matching Euler identities for all three new E types. Thus every nonzero-pairing branch is excluded.

## 3. Zero pairing leaves only the high-line case X

If B=0, then a+b<=3. Since a>=2 and b>=1, necessarily a=2,b=1. Enumerating all possible globally generated rank-one images of T O in E*(1) gives no line for Y or Z, and only O(11) for X. (Its section module is the first eligible symmetric power containing T with the required parity and target Hom.) Thus Y and Z are already impossible in this branch.

For X, the line O(11) is the unique highest-degree summand of E*(1), hence saturated. Duality identifies the projected image of I in T O(3) with O(-8). Write C0 for its rank-two kernel. Since B=0, the quadratic image J=im phi lies in C0 with the same rank.

We now classify J, not a chosen map. J is globally generated, its sections contain 2P, it embeds into Q, and deg J<=14. Enumerate the rank-two irreducible blocks and pairs of equivariant lines subject to these necessary conditions. The only possibilities are

    J=2O(6), O(6)+O(8), or W O(7).

Indeed eligible lines with P sections have degrees six or eight; the total-degree bound rules out 2O(8). Among rank-two irreducible blocks through degree seven, only W O(7) has two P copies in sections. The verifier checks the full necessary image-block lists against all five Q types, not just these candidates. This is a necessary overlist; no candidate is asserted realizable.

The saturation of J in Q has degree at most fourteen. Its defect is consequently at most two, less than twelve, and is zero. Thus J is saturated in Q and C0=J. The extension by O(-8) splits because H1(C0(8))=0, giving

    E/K=C0(-2)+O(-10).                                  (1)

The quotient to O(-10) is nonzero only on E's unique O(-10) summand, and is an isomorphism there. Hence K embeds into

    E'=2P O(-2)+T O(-3)+Wp O(-5).

Putting c=deg C0, equation (1) gives deg K=-40-c>=-54.

## 4. New high-line obstruction: a forced kernel has the wrong character

The next derivative K -> (E/K)(-2) has rank three. The target has a quotient O(-12); the composite to this quotient must be nonzero, or its image would have rank at most two. We prove Hom_G(K,O(-12))=0 instead.

All degrees of K are at most -3 by persistence. Its excess over 14O(-3) is

    q=-deg K-42=c-2<=12.

Any coefficient block of degree <=-12 and dimension at least two alone contributes at least eighteen to q. Thus a block contributing to Hom(K,O(-12)) must be a line, and central parity with q<=12 leaves only O(-12) or O(-14).

After O(-14) the remaining rank thirteen has excess at most one. Odd-degree coefficient representations all have even dimension, so a degree-even block is required; the only possibility is O(-4). But Hom_G(O(-4),E')=0.

After O(-12) the remaining rank thirteen has excess at most three. An odd-degree block below degree -3 costs at least four, so cannot occur. The even-degree possibilities are O(-4), O(-6), or one rank-three block at degree -4. Both lines have zero Hom into E'. The rank-three case leaves ten dimensions at degree -3. Since

    H0(E'(3))=2Wp+3T,

the only ten-dimensional subrepresentation is 2Wp+T. Of the two rank-three even irreducibles A,V, only V has a nonzero Hom from its degree-minus-four block into E'. Thus the only remaining necessary splitting is

    K=(2Wp+T)O(-3)+V O(-4)+O(-12).                       (2)

Its degree is -54 and its equivariant Euler character at twist three is Wp. This contradicts the character forced by (1):

    C0=2O(6):          chi_G(K(3))=T-Wp;
    C0=O(6)+O(8):      chi_G(K(3))=T-S;
    C0=W O(7):         chi_G(K(3))=T-S.

None equals Wp. In particular the c=12 case also disagrees in degree. This excludes the required nonzero composite to O(-12), and closes the last zero-pairing branch of X.

The verifier independently enumerates every parity-compatible block of K with rank fourteen, q<=12, the necessary Hom into E', the degree-minus-three section multiplicity bound, and a nonzero Hom into O(-12). It finds precisely (2), then checks all three Euler-character contradictions. No map rank or actual-instance experiment is used.

## Reproduction

Run `python3 verify_double_p4_backward_gauss.py`. It executes all frozen preceding verifiers unchanged, checks the three new tuples and common Euler characters, the nonzero-pairing reduction, the zero-pairing line lists, the complete necessary rank-two quadratic image list, saturation bounds, the exhaustive high-line kernel possibilities, and the contradictions. The resulting formal remainder is at most ten of 28. The full `(3,2)` exclusion, SF rank >=4, square rank 28, and smoothing closure are not proved.
