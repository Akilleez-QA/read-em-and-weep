# Six large quadratic-section types are excluded by backward Gauss persistence

## Result and scope

In the hypothetical generic-SF-rank-three adjacent profile `(k,l)=(3,2)`, none of the six formal primal splitting types whose quadratic section modules are

    R = 2V+P4, V+2P4, V+P4+D5, or 2P4+D5

can occur. The last two modules each have two formal types. Together with the five previously excluded types, this leaves **at most 17 of the original 28 formal primal types** for this profile.

This is not an exclusion of the entire `(3,2)` profile, generic SF rank three, or the zero-quadratic case. The previously established numerical square-rank bound remains 27. No realizability claim is made for the 17 remaining formal types.

Only universal characters, hypothetical bundle degrees, exact evaluation sequences, invariant-divisor bounds, and geometric differentiation are used. There are no actual coefficient selections, source matrices, map/rank evaluations, parameter scans, or local-model experiments.

## 1. Frozen inputs

Use the frozen notes:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`;
- `ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md`;
- `RANK-THREE-CUBIC-PAIRING-EXCLUDED-IN-ADJACENT-GAUSS-PROFILE.md`;
- `TWO-D5-BACKWARD-GAUSS-EXCLUSION.md`;
- the universal rank-one flag theorem and invariant-divisor refinement in `RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md` and `GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md`.

Write `P=P4`, `D=D5`, `S=S4`, `T=T6`, and `Wp=Wprime`. The plateau is

    F0 < F1=K2 < F2=K < F3=E < F4 < F5,

with ranks 8,11,14,17,20,23. All stages are saturated; the derivatives of K and K2 have generic rank three and forward transforms E and K. We have

    deg E=-54,
    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.                 (1)

Every interior stage has no nonzero constant subbundle. The five possible dual types have maximum ordinary degree at most eight in Q, and their two largest ordinary degrees sum to at most 14. The canonical cubic evaluation in Q* is `T O(-3)`.

The restricted derivative maps and cubic pairing are

    phi: R O -> Q,
    psi: T O -> E*(1),
    B: R O -> T O(3),      R=H0(E(2)).                    (2)

Both restricted derivatives are injective on global sections. If their ranks are a,b and the pairing rank is t, then `a+b-3 <= t`. The frozen rank-three-pairing theorem gives exactly these alternatives:

    B=0, or im B=Wp O(1).                                 (3)

The latter image is saturated in `T O(3)`.

The six formal primal bundles are the following. A displayed representation is a coefficient space, not a horizontal splitting:

    X  = (2V+P) O(-2) + 2V O(-4) + O(-10),
    Y  = (V+2P) O(-2) + V O(-4) + Wp O(-5) + O(-10),
    Z1 = (V+P+D) O(-2) + V O(-4) + O(-8) + O(-10),
    Z2 = (V+P+D) O(-2) + V O(-4) + W O(-9),
    U1 = (2P+D) O(-2) + Wp O(-5) + O(-8) + O(-10),
    U2 = (2P+D) O(-2) + Wp O(-5) + W O(-9).              (4)

The following standard evaluation sequence will be used repeatedly:

    0 -> Sym^(d-1) W O(-1) -> Sym^d W O -> O(d) -> 0.     (5)

It is SL2-equivariant and therefore equivariant for the binary icosahedral group. Splittings below are ordinary equivariant bundle splittings, obtained by vanishing Ext groups and finite-group averaging, never horizontal splittings.

## 2. The rank-two-pairing branch

Assume `im B=Wp O(1)`. All six R in (4) strictly contain P. If a were two, the generic kernels of B and phi would coincide. Their saturated sheaf kernels would coincide, forcing the nonzero section submodule `ker[H0(B)]=R-P` into `ker[H0(phi)]`, contrary to section injectivity. Hence a=3. The rank inequality and t=2 give b=2.

Put `I=im[beta_E(2):E(2)->Q]`. Its projection to `T O(3)` has rank b=2 and contains im B. Since im B is saturated, the projected image equals it. Thus

    0 -> O(n) -> I -> Wp O(1) -> 0.                       (6)

Here the kernel is an equivariant line, so the coefficient character is trivial. It lies in Q, hence n is even and at most eight. The section submodule R-P maps injectively into its sections. Testing `Sym^n W` for n=0,2,4,6,8 yields:

- X is impossible because no such line contains two V copies;
- Z1,Z2 are impossible because no such line contains both V and D;
- Y forces n=6;
- U1,U2 force n=8.

In the last three cases the extension (6) splits, since `H1(O(n-1))=0`, and

    H0(I)=P+Sym^n W=R.

The injective section map induced by phi is therefore an isomorphism onto the complete section module of I. Since I is globally generated, phi surjects onto all of I, not just a subsheaf of finite colength. Consequently

    E/K=Wp O(-1)+O(n-2).                                 (7)

Write E=`R O(-2)+H`, with H its high part in (4). The complete-evaluation kernel and (5) give

    K=(Wp+Sym^(n-1)W) O(-3)+H.                            (8)

For example, the extension by H splits because every ordinary degree of H is at most -4, while the evaluation kernel has degree -3.

The next derivative is

    K(3) -> (E/K)(1)=Wp O+O(n-1),                         (9)

and is injective on global sections by (1). Its source and target section modules both equal `Wp+Sym^(n-1)W`. Thus the restriction to the constant evaluation block is complete evaluation, up to an automorphism of its section module. It is surjective as a bundle map. Applying (5) again gives

    K2=Sym^(n-2)W O(-4)+H,
    K/K2=Wp O(-3)+O(n-4).                                (10)

The extension calculation is unaffected by the components of H mapping to the target of (9): its evaluation kernel has degree -4, and all degrees of H are at most -4, so the required Ext groups still vanish.

### 2.1. Excluding Y

Here n=6, so

    K2=(D+V) O(-4)+Wp O(-5)+O(-10).

The next derivative, twisted by four, has target

    (K/K2)(2)=Wp O(-1)+O(4).

Its section source contains D+V, while its section target is D. This contradicts `H0(F0(4))=0`. Thus Y has no rank-two pairing.

### 2.2. Excluding U1 and U2

Here n=8. Put

    H=Wp O(-5)+Htail,
    Htail=O(-8)+O(-10) or W O(-9).

By (10), the next required derivative is

    (V+P) O + Wp O(-1) + Htail(4)
       -> Wp O(-1)+O(6).                                (11)

The section map to O(6) is an isomorphism, by (1), since both section modules are V+P. It is therefore complete evaluation. The only summand that can map equivariantly to the Wp O(-1) target is the displayed Wp O(-1): the constant block cannot by degree, and the needed tail Hom spaces are zero. Generic rank three forces that scalar map to be an isomorphism. Hence (11) is surjective and

    F0=T O(-5)+Htail,
    K2/F0=Wp O(-5)+O(2).                                (12)

The derivative of F0 consequently has target

    (K2/F0)(-2)=Wp O(-7)+O.

Every Hom from the bundle F0 in (12) to Wp O(-7) vanishes. This follows by degree on T O(-5), and on the tails from

    Hom(1,Wp tensor W)=0,
    Hom(1,Wp tensor Sym^3 W)=0,
    Hom(W,Wp tensor Sym^2 W)=0.

Thus the endpoint F0 has SF rank at most one. Rank zero would make it a positive-rank constant subbundle of E, impossible. It has rank one, rank eight, and degree -48.

Let its smallest constant span have dimension 8+s. Its rank-one forward transforms are contained in the respective F_j. Since no F_j for j<5 contains a constant subbundle, s>=5. The universal rank-one degree bound gives `48>=8s`, hence s<=6. Moreover `H0(F0(5))` contains T. Universal section persistence applied to the rank-one flag within this smallest constant span gives s<=5: a section of degree at most five reaches a constant span after at most five derivatives, which cannot lie in an interior rank-one-flag stage. Hence s=5.

The exact rank-one flag degree identity and invariant-orbit divisor semigroup require

    (8+5)(48-8*5)=104
       in <12*8,20*8,30*8,12*5,20*5,30*5>
       = <96,160,240,60,100,150>.                       (13)

This is impossible: the only positive generators at most 104 are 60,96,100, and no nonnegative combination equals 104. This excludes U1 and U2 in the rank-two-pairing branch.

All six types therefore force B=0 if they are to survive.

## 3. The zero-pairing branch: force a high negative quotient

Assume B=0. Each R in (4) has dimension at least ten; no line subbundle of Q has that many sections, since its degree is at most eight. Thus a>=2. Since b>=1, the rank inequality gives

    a=2, b=1.                                           (14)

Let `J=im phi`. It is globally generated, and R injects into H0(J). Equivariant splitting, central parity, the target Hom spaces in the five Q types, and the section character give the following necessary list:

    X:     J=2O(6);
    Y:     J=W O(7), 2O(6), or O(6)+O(8);
    Z1,Z2: J=W O(5), O(4)+O(6), W O(7), or O(6)+O(8);
    U1,U2: J=W O(7) or O(6)+O(8).                        (15)

This is an overlist of necessary bundle shapes, not a claim that all shapes embed into every Q. For completeness, the only individual blocks of rank at most two that can occur in an image into Q are lines O(4), O(6), O(8) and two-dimensional blocks W O(3), W O(5), W O(7), Wp O(1). Section injectivity removes W O(3), Wp O(1), and the unwanted line pairs. Two O(8) summands cannot embed: `dim Hom_G(O(8),Q)<=1`. The retained degrees j=deg J are 10,12,14.

The rank-one image of psi is O(e). It is globally generated and its sections contain T. Testing odd e against `Hom_G(O(e),E*(1))` gives exactly

    X,Y: e=11;
    Z1,U1: e=9 or 11;
    Z2,U2: e=9.                                         (16)

These lines are saturated in E*(1): their saturation defect is bounded by the maximum ordinary target degree minus e, at most two, whereas a positive equivariant torsion length is at least 12. Similarly J is saturated in Q: its degree is at least ten and the maximum rank-two degree in Q is at most 14, leaving possible defect at most four.

Duality with the saturated image O(e) shows that the projection of the full image I to T O(3) is exactly O(3-e). Its kernel contains the saturated rank-two J and hence equals J. Consequently

    I=J+O(3-e),
    E/K=J(-2)+O(1-e).                                  (17)

The extension splits because every degree of J in (15) is at least four, and e>=9. The equality of the rank-two kernel with J uses saturation, not an unjustified identification of actual images with saturated images.

## 4. Exclude every e=11 case

Write `E=R O(-2)+H` and

    N0=ker[R O -> J],      N=N0(-2).

The map is surjective by the definition of J. Section injectivity gives `H0(N0)=0`. If r=dim R-2 and j=deg J, its r ordinary degrees are all at most -1 and sum to -j. Therefore every degree of N is at least

    dim R-j-5.                                         (18)

For all listed types and shapes this is at least -8.

When e=11, the last quotient in (17) is O(-10). Only the O(-10) summand in E can map to it; its scalar map must be an isomorphism. The high-part kernel Htail then has every ordinary degree at least -8. There is an exact sequence

    0 -> N -> K -> Htail -> 0.

Both end bundles become globally generated after twist eight, and `H1(N(8))=0`; thus K(8) is globally generated. No summand of K can map to O(-12). But its next derivative has target

    (E/K)(-2)=J(-4)+O(-12).

Its rank is at most two, contradicting the rank-three plateau. This excludes X and Y outright, and all e=11 cases of Z1,U1.

## 5. Exclude every remaining e=9 case

Only Z1,Z2,U1,U2 remain. Write

    M=V O(-4) for Z1,Z2,
    M=Wp O(-5) for U1,U2.

The high part H maps surjectively to the last quotient O(-8) in (17). Its kernel is

    M+O(-10).                                          (19)

For Z1,U1 this simply cancels O(-8); the other high summands have no map to it. For Z2,U2 it is the unique nonzero universal evaluation `W O(-9)->O(-8)`, whose kernel is O(-10). The maps from M to O(-8) vanish by the corresponding character Hom spaces.

Formula (18) gives every degree of N at least -7. Thus the extension defining K splits over O(-10), and

    K=L+O(-10),
    0 -> N -> L -> M -> 0,
    every ordinary degree of L is at least -7.           (20)

The last degree claim follows from global generation after twist seven. In

    beta_K: K -> J(-4)+O(-10),                           (21)

the projection from L to the last line vanishes. Generic rank three therefore forces the O(-10)-to-O(-10) scalar to be an isomorphism. After subtracting its graph, let C be the rank-two image of L in J(-4), and let delta>=0 be the length of its torsion quotient. Then

    K/K2=C+O(-10),
    deg C=j-8-delta,
    deg K2=-24-2j+delta.                                (22)

The next derivative of K2 has rank three and target

    C(-2)+O(-12).

It must have a nonzero projection to O(-12), so some ordinary summand of K2 has degree at most -12. On the other hand `H0(K2(3))=0` forces all its eleven degrees to be at most -4. Therefore

    deg K2<=-12-10*4=-52.                               (23)

If j=10, (22) is at least -44, a contradiction. If j=14, equations (22)-(23) force delta=0 and

    C=J(-4),
    K2=U O(-4)+O(-12),          dim U=10.                (24)

Its coefficient U is determined without evaluating any map. Subtract the two exact derivative quotients from E in equivariant K-theory. For both U and Z families, using (5) for the W O(-9) tail when present, exact character arithmetic gives

    chi_G(K2(4))=V.

Since `H1(O(-8))=Sym^6 W=V+P`, equation (24) yields

    U=2V+P.                                             (25)

The two j=14 shapes in (15) have identical cohomology characters by (5). In particular

    H0(J(-2))=V+P+D.

Finally, the next derivative twisted by four maps

    H0(K2(4))=2V+P -> H0(J(-2)+O(-8))=V+P+D.

It cannot be injective because the source has two V copies and the target only one. Its kernel is H0(F0(4)), contradicting (1). This excludes all e=9 cases and completes all six exclusions.

## Verification and remaining limits

Run `python3 verify_six_large_quadratic_gauss_exclusions.py`. It checks the six formal primal types, the rank-two-pairing line possibilities, all necessary zero-pairing rank-two image shapes, the rank-one cubic-image degrees, saturation bounds, evaluation characters and vanishing Hom spaces, every degree bottleneck, the endpoint semigroup obstruction, and the remaining count 17.

The geometric derivative, saturation, complete-evaluation, extension, and endpoint-persistence arguments are supplied above. The verifier uses no actual map or rank evaluation. The rank-one theorem is applied to the endpoint inside its own smallest constant span, not assumed to hold in all 30 ambient dimensions.
