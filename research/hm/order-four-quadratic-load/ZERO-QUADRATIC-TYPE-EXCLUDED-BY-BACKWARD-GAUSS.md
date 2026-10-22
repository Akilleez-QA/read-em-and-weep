# The zero-quadratic-section Gauss type is excluded

## Result and scope

The hypothetical `(k,l)=(3,2)` type

    (1,2,1,0,0,0,0,0),
    E=(Wp+2T) O(-3)+V O(-4), H0(E(2))=0,

is impossible. This note addresses only this type, not the other four survivors of the frozen mixed-octic closure. It does not assume that the absence of quadratic sections forces l=3. The established generic SF rank bound three and positive-square rank bound 27 are unchanged; no general rank-three exclusion or smoothing closure is claimed.

The deduction uses universal equivariant representations, hypothetical bundle images, degrees and backward Gauss persistence. It uses no actual coefficients, selected actual points, actual-instance matrices or rank tests, scans, local-model spikes, or consumed experiments. Predecessor files are unchanged.

## 1. Exact frozen setting

Read `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, `EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md`, `ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md`, and the frozen `FOUR-MIXED-P4-D5-TYPES-EXCLUDED-BY-OCTIC-EVALUATION.md` chain. Write G=2.A5, W for its standard two-space, Wp for its other two-space, A=Sym^2 W, V for the other even three-space, P=P4, S=S4, D=D5 and T=T6. All are self-dual. The center acts on O(d) by (-1)^d; G has no nontrivial characters.

The saturated plateau is

    F0 < K2 < K < E < F4 < F5,
    ranks: 8,11,14,17,20,23,
    deg E=-54,
    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.

The derivatives of E,K,K2 have rank three and their sheaf kernels are K,K2,F0 respectively. The five possible dual splittings are

    Q*=T O(-3)+V O(-4)+Htail,
    Htail=(1+A)O(-6),
          W O(-5)+W O(-7),
          W O(-5)+O(-6)+O(-8),
          O(-4)+O(-6)+W O(-7),
          O(-4)+2O(-6)+O(-8).

Thus Q has rank13, degree54, maximum ordinary degree at most8, and its canonical dual cubic evaluation is T O(-3). The restricted dual derivative

    psi:T O -> E*(1)=(Wp+2T) O(4)+V O(5)

is injective on sections, by dual persistence. Its rank b is therefore positive and at most three. The two derivatives are negative transposes, from differentiation of E perpendicular Q*. Positive invariant torsion length belongs to <12,20,30> and is at least12.

Put A0=E/K and C=K/K2. The derivative of K identifies C with its actual image in A0(-2); both have rank three. If delta is the torsion colength, then

    deg K2=-54-2 deg A0+6+delta,
    chi(K2(4))=7-2 deg A0+delta.                       (1)

The derivative of K2 and its section-free kernel F0(4) give

    H0(K2(4)) injects into H0(C(2)) into H0(A0).       (2)

These statements concern actual images and require no unproved saturation.

## 2. Rank three of the cubic image is impossible

Let L=im psi. It is globally generated. Every equivariant irreducible splitting block R O(d) receives a nonzero map from T O and maps nontrivially to E*(1). Its degree lies between zero and five, its rank is at most three, and its central parity is odd. Exhaustively imposing these two Hom conditions gives exactly

    V O(1), Wp O(2), V O(3), Wp O(4), V O(5).          (3)

There is no line block, so b cannot be one. If b=3, L must be one of the three V blocks, and in particular every ordinary degree of L is at least one.

Let Lbar be the saturation of L in E*(1). Every ordinary degree of Lbar is also at least one: a projection to a lower-degree summand would annihilate L by degree, contradicting generic surjectivity onto Lbar. Since L has the full derivative rank, its saturation is exactly A0*(1). Indeed A0 is the locally free quotient E/K, so its dual inclusion is saturated, and both inclusions have the same generic image. Hence every ordinary degree of A0=Lbar*(1) is at most zero. Consequently

    deg A0<=0, h0(A0)<=3.

But (1)-(2) require 7<=chi(K2(4))<=h0(A0)<=3. Thus b=3 is impossible. This argument does not assume L itself saturated or bound its saturation defect.

## 3. Rank two leaves three exact first quotients

We now have b=2. By (3),

    L=Wp O(e), e=2 or4.

Its saturation in E*(1) has degree at most 2*5=10. Thus its invariant torsion defect is at most 10-2e, respectively six or two, and must vanish. The actual projected image of beta_E(2) in T O(3) is therefore L*(3)=Wp O(3-e). To justify the actual image assertion, dualize the saturated inclusion L -> E*(1), which yields a surjection, and then dualize the evaluation surjection T O -> L, which yields an injection. Their composite is the projected derivative, up to sign.

Let I=im beta_E(2). Its projection has rank two, so its kernel is an equivariant line O(n) embedded in Q. It has even degree n<=8. Twisting the exact image sequence gives

    0 -> O(n-2) -> A0 -> Wp O(1-e) -> 0.              (4)

We do not yet assume this extension splits. Its quotient has no sections. Therefore

    deg A0=n-2e, h0(A0)=max(n-1,0).                   (5)

Since K has rank14 and all ordinary degrees at most -3, deg K<=-42. From deg K=-54-n+2e we obtain n>=2e-12. Applying (1)-(2) and (5) gives the necessary inequality

    7-2n+4e+delta <= max(n-1,0).                     (6)

For even 2e-12<=n<=8 and e=2,4, (6) leaves precisely

    (n,e)=(6,2), (8,2), (8,4).

The respective upper bounds on delta are 2,8,0. Hence delta=0 in each case, and C=A0(-2). For these positive n the extension (4) splits because H1(O(n+e-3))=0. Thus both exact quotients are fixed:

    A0=O(n-2)+Wp O(1-e), C=A0(-2).                   (7)

## 4. Exclude the three candidates

For (n,e)=(6,2), subtracting the two exact quotients (7) from E in equivariant K-theory yields

    chi_G(K2(4))=V, H0(A0)=D.

The V multiplicity of H0(K2(4)) is at least its Euler multiplicity one. This contradicts the injection (2) into D.

For (n,e)=(8,4), the same calculation gives

    chi_G(K2(4))=-A+2V+P, H0(A0)=V+P.

Here the required V multiplicity is at least two but the target has only one. This also contradicts (2).

For (n,e)=(8,2), the exact quotients are

    A0=O(6)+Wp O(-1), C=O(4)+Wp O(-3),
    chi_G(K2(3))=-(Wp+S+T),
    chi_G(K2(4))=-A+V+P-D.

These are precisely the hypotheses of the universal second-kernel classification and endpoint proof in Sections5-6 of `THREE-P4-QUADRATIC-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md`. That proof uses only these characters, exact C, plateau ranks and persistence, not a P summand of E or a nonzero quadratic pairing at this stage. For clarity, its complete classification gives

    K2=(V+P)O(-4)+Wp O(-5)+Htail,
    Htail=W O(-9) or O(-8)+O(-10).

The next derivative and complete sextic evaluation then force

    F0=T O(-5)+Htail, rank F0=8, deg F0=-48,
    K2/F0=O(2)+Wp O(-5).

The derivative of F0 can only have rank one: all maps to the Wp O(-7) part of its derivative target vanish, and rank zero would produce a forbidden constant subbundle. The constant span and section persistence force its rank-one forward length to be five. Its exact invariant-ramification degree formula requires

    104 in <96,160,240,60,100,150>,

which is false. The unchanged frozen verifier executes the exhaustive classification and endpoint check. Thus the final candidate is excluded, completing this type's exclusion.

## Reproduction

Run `python3 verify_zero_quadratic_backward_gauss.py`. It executes the frozen mixed-octic closure and universal endpoint verifier unchanged; verifies the exact remaining tuple, all five Q types, the complete image-block list, saturation bounds, every possible line degree, all three quotient candidates and torsion bounds, both character discrepancies, and the final endpoint's exact character hypotheses.

The note proves the geometric image and persistence statements; the verifier checks their universal representation and degree arithmetic. It does not evaluate the actual second fundamental form or assert a smoothing result.
