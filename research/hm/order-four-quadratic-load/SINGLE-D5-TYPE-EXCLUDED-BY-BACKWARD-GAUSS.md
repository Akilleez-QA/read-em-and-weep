# The single-D5 type is excluded by backward Gauss persistence

## Result and scope

In the hypothetical generic-SF-rank-three plateau `(k,l)=(3,2)`, the remaining formal primal type

    (1,1,1,0,0,1,0,0),
    E=D O(-2)+(Wp+T) O(-3)+V O(-4)+O(-8)

is impossible. Here D=D5, Wp=Wprime, T=T6, P=P4, S=S4, and A=Sym^2 W. This is one new exclusion, disjoint from the eighteen checked in `THREE-DOUBLE-P4-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md`. Together they leave at most nine of the original 28 formal primal types.

This does not exclude the whole adjacent profile, improve the established SF lower bound three or square-rank lower bound 27, or prove smoothing closure. No remaining type is asserted realizable. The proof and verifier use only universal representations and hypothetical bundle geometry: no actual HM/source coefficients, source-instance matrices or rank tests, selected points, scans, model spikes, or consumed experiments.

## 1. Frozen input and initial reduction

Use the unchanged double-P4 note and verifier, and their dependencies, particularly `P4-ZERO-PAIRING-EXCLUDED-BY-BACKWARD-PERSISTENCE.md`, `SIX-LARGE-QUADRATIC-MODULES-EXCLUDED-BY-BACKWARD-GAUSS.md`, `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, and the rank-three cubic-pairing exclusion.

The saturated plateau has stages

    F0 < K2 < K < E < F4 < F5,

of ranks 8,11,14,17,20,23. Its relevant derivatives have rank three, deg E=-54, and persistence gives

    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.             (1)

Every positive invariant torsion length is at least twelve. Each of the five possible Q bundles has maximum ordinary degree at most eight and maximum rank-two subbundle degree at most fourteen. The canonical cubic evaluation in Q* has coefficient T.

Set

    phi:D O -> Q, psi:T O -> E*(1), B:D O -> T O(3),

with ranks a,b,t. Both restricted derivatives are section-injective. The frozen pairing theorem says B is zero or has saturated image Wp O(1). But H0(Wp O(1))=P and Hom_G(D,P)=0, so B=0. The rank inequality gives a+b<=3. Thus only

    (a,b)=(1,1),(1,2),(2,1)                           (2)

remain.

All splittings used below are equivariant bundle splittings, not horizontal splittings. Every image is the actual locally free image sheaf until saturation is explicitly proved.

## 2. Rank-two cubic image

Assume b=2, hence a=1. The line J=im phi is globally generated, contains D in its sections, and injects into Q. The complete necessary line list is

    J=O(n), n=4 or 8.

It is saturated in Q, since its possible saturation defect is at most 8-n<12.

The universal necessary image-block list for psi, through rank two, is

    Wp O(2), Wp O(4), W O(8), O(9).

The largest two degrees of E*(1) are nine and five. Thus W O(8), of degree sixteen, cannot inject; neither can a pair of O(9) lines. Consequently the rank-two image is

    L=Wp O(e), e=2 or 4.

Its saturation defect is at most 14-2e<12, so it is saturated.

Let I=im[beta_E(2):E(2)->Q]. Duality with saturated L identifies its projected image in T O(3) as Wp O(3-e). The rank-one kernel contains saturated J and therefore equals J. The extension splits since H1(O(n+e-3))=0. Hence the exact quotient is

    A0:=E/K=O(n-2)+Wp O(1-e).                         (3)

Let C be the actual rank-three image of beta_K in A0(-2), with torsion cokernel length delta. Then

    chi(K2(4))=7-2n+4e+delta.

By (1), the next derivative is injective on sections after twist four, and its target C(2) injects into A0. Therefore

    7-2n+4e+delta <= h0(K2(4)) <= h0(A0)=n-1,
    delta <= 3n-4e-8.                                 (4)

For n=4 the bound is negative for both e. For n=8,e=2 it is eight; for n=8,e=4 it is zero. In both remaining cases the invariant gap forces delta=0, so C=A0(-2).

For n=8,e=4, exact equivariant Euler arithmetic gives

    chi_G(K2(4))=-A+2V+P,
    H0(A0)=V+P.

The source sections contain at least two copies of V, while the target contains one, contradicting (1).

For n=8,e=2, the exact quotients are

    E/K=O(6)+Wp O(-1), K/K2=O(4)+Wp O(-3).

Their Euler characters are exactly the frozen endpoint case:

    chi_G(K2(3))=-(Wp+S+T),
    chi_G(K2(4))=-A+V+P-D.

The exhaustive positive-character classification in the frozen single-P4 proof gives precisely

    K2=(V+P) O(-4)+Wp O(-5)+Htail,
    Htail=W O(-9) or O(-8)+O(-10).

Its endpoint argument applies without change: F0=T O(-5)+Htail has rank-one derivative, rank eight, degree -48, and smallest constant span of dimension thirteen. Invariant ramification would require

    104 in <96,160,240,60,100,150>,

which is impossible. The companion verifier executes that unchanged classification and endpoint check. Thus b=2 is excluded.

## 3. Rank-one cubic image: exact constraints without assuming generation

Assume b=1. The same image-block list gives the unique line O(9), which is the highest-degree summand of E*(1), hence saturated. The projected image of I is consequently O(-6). Write C0 for its rank-two kernel. Because B=0, the section-injective quadratic image lies in C0, so H0(C0) contains D. No global generation of C0 is assumed.

There is an exact sequence

    0 -> C0(-2) -> E/K -> O(-8) -> 0.                 (5)

Only the O(-8) summand of E maps nontrivially to this last quotient; its scalar is an isomorphism. Put

    E'=D O(-2)+(Wp+T) O(-3)+V O(-4).

Then

    0 -> K -> E' -> C0(-2) -> 0.                      (6)

Writing c=deg C0, we have deg K=-42-c. Persistence (1) implies every ordinary degree of K is at most -3, so c>=0. The inclusion C0->Q gives c<=14 and every degree of C0 at most eight, hence every degree at least -8.

The derivative K->(E/K)(-2) has rank three. Its composite with the line quotient O(-10) must be nonzero, otherwise its image has rank at most two. Thus

    Hom_G(K,O(-10)) is nonzero.                        (7)

These restrictions yield a small exhaustive necessary splitting list. The method is as follows, and is fully implemented in the verifier:

1. Enumerate every parity-compatible irreducible block R O(-j) of K with j>=3 and (j-3)dim R<=14. This is complete because the total excess over 14 O(-3) is c<=14; in particular j<=17.
2. Require each block to have nonzero Hom into E'. For j=3, also bound its multiplicity by its multiplicity in H0(E'(3))=S+Wp+2T. Require rank fourteen, excess at most fourteen, and (7). Exactly twenty necessary K splittings survive these conditions.
3. Enumerate all rank-two equivariant C0 splittings with ordinary degrees in [-8,8], total degree in [0,14], necessary block Hom into at least one of the five Q bundles, and D in H0(C0). Test the degree identity and the Euler-character identity of (6) at twists zero through four. These are necessary tests, not a claim that they suffice for a bundle embedding. They leave exactly the ten pairs below.

The list, grouped to avoid repeating equivalent rows, is:

    c=10:
      C0=W O(5) or O(4)+O(6);
      K=(S+T) O(-3)+V O(-4)+O(-10).

    c=12:
      C0=O(4)+O(8);
      K=(Wp+T) O(-3)+D O(-4)+O(-10), or
        (Wp+S+T) O(-3)+O(-8)+O(-10).

    c=14:
      C0=W O(7) or O(6)+O(8);
      K=T O(-3)+(V+P) O(-4)+O(-10), or
        2T O(-3)+2O(-10), or
        (Wp+T) O(-3)+V O(-4)+Wp O(-5)+O(-10).

This is an overlist of necessary pairs. No pair is asserted realizable. In particular the finite universal classification does not evaluate any map or select any source coefficients.

## 4. Two further rank-three derivatives exclude all ten pairs

Every surviving C0 degree is at least four, so (5) splits by Ext vanishing. Thus

    E/K=C0(-2)+O(-8).

Every surviving K has at least one O(-10) summand; all its other ordinary summands have degree at least -8, except for a possible second O(-10). Only its O(-10) summands can map to the last line in

    beta_K:K -> C0(-4)+O(-10).

Rank three forces a nonzero scalar, hence a surjection onto O(-10). Choose an equivariant O(-10) summand giving that isomorphism and subtract its graph. The full image consequently splits as

    K/K2=C+O(-10),

where C is a rank-two image inside C0(-4). If its invariant torsion cokernel has length delta>=0, then

    deg C=c-8-delta,
    deg K2=-24-2c+delta.                               (8)

The next derivative of K2 has rank three and target

    C(-2)+O(-12).

It must project nontrivially onto O(-12). By H0(K2(3))=0, all eleven ordinary degrees of K2 are at most -4; one is at most -12. Therefore

    deg K2<=-12-10*4=-52.                              (9)

For c=10 or12, (8) contradicts (9). For c=14, equality is forced, delta=0, C=C0(-4), and

    K2=U O(-4)+O(-12), dim U=10.                       (10)

Subtracting the two exact quotients from E in equivariant K-theory gives, for both degree-fourteen C0 shapes,

    chi_G(K2(4))=V.

Since H1(O(-8))=Sym^6 W=V+P, equation (10) forces

    U=2V+P.

But the next derivative, twisted by four, has section target

    H0(C0(-2)+O(-8))=V+P+D.

The source H0(K2(4))=2V+P cannot inject into this target, which has only one V copy. Its kernel is H0(F0(4)), contradicting (1). This excludes all ten pairs and finishes the b=1 branch independently of whether a=1 or2.

## Reproduction

Run `python3 verify_single_d5_backward_gauss.py` in this directory. It runs all preceding frozen verifiers unchanged, checks the unique selected tuple, the zero pairing, complete necessary small-image lists and saturation bounds, all four b=2 quotient cases, the exhaustive twenty-to-ten necessary K/C0 classification, the two further derivative contradictions, and the final count nine.

Only this single D5 type is newly claimed excluded. The full adjacent-profile exclusion, SF rank at least four, square rank 28, and smoothing closure remain unproved.
