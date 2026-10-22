# The V+D5 profile is excluded by backward Gauss persistence

## Result and scope

The hypothetical `(k,l)=(3,2)` profile

    (1,0,2,0,0,1,0,0),
    E=(V+D)O(-2)+Wp O(-3)+2V O(-4)+O(-8)

is impossible. Here D=D5, P=P4 and Wp=Wprime. Combined only with the frozen mixed-octic closure, this reduces its five remaining formal types to four of 28. Other concurrent exclusions are not counted here. The established SF rank bound three and square rank bound 27 remain unchanged; this is not full plateau or smoothing closure.

The proof uses only hypothetical equivariant bundle geometry and universal representation arithmetic. No actual source coefficients, selected points, actual-instance matrices/ranks, parameter scans, model spikes or consumed experiments are used. Predecessors remain unchanged.

## 1. Frozen inputs and the pairing

Use `FOUR-MIXED-P4-D5-TYPES-EXCLUDED-BY-OCTIC-EVALUATION.md`, `MIXED-P4-D5-FORCED-OCTIC-EVALUATION.md`, and their frozen predecessors. The plateau bundles have successive ranks 8,11,14,17,20,23, with E of degree -54, K=E^- of rank14, and K2=K^- of rank11. Persistence gives

    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.

The backward derivatives have rank three. Positive invariant torsion length is at least twelve. The five possible Q bundles have maximum ordinary degree eight and largest-two-degree sum at most fourteen.

Set R=V+D. The section-injective restricted derivatives are

    phi:R O -> Q, psi:T O -> E*(1),

and their pairing is B:R O -> T O(3). If a,b,t denote their ranks, then a+b-3<=t. By `RANK-THREE-CUBIC-PAIRING-EXCLUDED-IN-ADJACENT-GAUSS-PROFILE.md`, every nonzero B has saturated image Wp O(1), with section module P. Since Hom_G(V+D,P)=0, B=0. A rank-one phi would be a globally generated equivariant line O(n), with even 0<=n<=8, containing V+D in its sections. No Sym^n W in this range contains both. Thus a>=2; b>=1 and a+b<=3 force

    (a,b)=(2,1).

## 2. Exhaustive necessary image shapes

Let J be the actual quadratic image. It is globally generated of rank two and contains R in sections. Equivariant splitting, central parity, the target Hom test, and the degree bound fourteen give exactly the following necessary overlist:

    W O(5), O(4)+O(6), W O(7), O(6)+O(8).

These are necessary possibilities, not assertions of realizability. Against the five ordered Q types in the frozen verifier, the shape lists are respectively

    1: W O(5), O(4)+O(6);
    2: W O(5), O(4)+O(6), W O(7);
    3: all four;
    4: W O(5), O(4)+O(6), W O(7);
    5: all four.

In particular Wp O(7) cannot map to any Q. The only Q summands of degree at least seven are W O(7) and O(8); their Hom spaces from Wp O(7) are Hom(Wp,W)=0 and Hom(Wp,W)=0 respectively. All lower-degree target summands receive no map by degree.

Write j=deg J, so j=10 or14. Its saturation defect in Q is at most 14-j<=4<12 and hence zero. The exhaustive rank-one image test for psi gives only O(9). It is saturated because E*(1) has maximum degree nine.

The actual projected full derivative image in T O(3) is O(-6): dualize the inclusion of the saturated cubic image and then its evaluation quotient, as in the frozen mixed-octic proof. The rank-two kernel of that projection contains saturated J and therefore equals J. After twisting by -2, the extension splits by H1 vanishing, giving the exact first quotient

    A0=E/K=J(-2)+O(-8).                              (1)

## 3. The essential parity improvement for the quadratic kernel

Let N0 be the kernel of the surjection R O -> J. It has rank six, degree -j and no sections. Thus all its ordinary degrees are at most -1. Write an equivariant irreducible block as R0 O(-q), q>=1. It consumes

    (q-1) dim R0

of the excess j-6 over six copies of O(-1). Central parity requires R0 to be center-odd when q is odd, and every center-odd representation has dimension at least two.

For j=14 the excess is eight. If q>=9 is odd, its block consumes at least sixteen; if q>=10 is even, it consumes at least nine. Both are impossible. Consequently all degrees of N0 are at least -8. For j=10 the same argument gives the stronger bound -4: odd q>=5 costs at least eight, while even q>=6 costs at least five, both exceeding the excess four.

Therefore N=N0(-2) has all degrees at least -10. This parity argument is essential: rank and degree alone would only give -11 when j=14.

In (1) the projection E -> O(-8) is a nonzero constant map on its unique O(-8) summand; all other summands have larger degree and cannot contribute. Its kernel is

    E'=(V+D)O(-2)+Htail,
    Htail=Wp O(-3)+2V O(-4).

Since the quadratic part surjects onto J(-2), projection from K to Htail is surjective, with kernel N. Hence

    0 -> N -> K -> Htail -> 0.

Both N(10) and Htail(10) are globally generated, and H1(N(10))=0. Lifting generators proves that K(10) is globally generated.

## 4. The two subsequent derivatives force a contradiction

The next rank-three derivative targets A0(-2)=J(-4)+O(-10). Its projection to O(-10) must be nonzero, since the other target has rank two. Every ordinary degree of K is at least -10. Therefore this projection is a nonzero constant map on a trivial-coefficient O(-10) summand of K and is a split surjection. Subtract its equivariant graph in the target. The actual image then has the form

    K/K2=C+O(-10), C subset J(-4), rank C=2,
    deg C=j-8-delta, delta>=0,
    deg K2=-24-2j+delta.                            (2)

Here delta is torsion colength; no equality of C with its saturation is assumed. The direct summand arises from the actual split O(-10) quotient, not from an unproved splitting of an arbitrary extension.

The following rank-three derivative has target C(-2)+O(-12). Again full rank forces a nonzero projection to its last line. Thus K2 has an ordinary summand of degree at most -12. All eleven ordinary degrees of K2 are at most -4 by H0(K2(3))=0, so

    deg K2<=10(-4)-12=-52.

For j=10, (2) gives degree at least -44, impossible. For j=14, (2) gives degree -52+delta. Equality is forced: delta=0 and

    K2=U0 O(-4)+O(-12), dim U0=10,
    K/K2=J(-4)+O(-10)=A0(-2).

For either degree-fourteen shape of J, universal equivariant Euler arithmetic using the two exact quotients gives

    chi_G(K2(4))=V.

Since H1(O(-8))=Sym^6 W=V+P, it follows that U0=2V+P. But the next persistence vanishing gives an injection

    H0(K2(4)) -> H0((K/K2)(2))=H0(A0),

which would be

    2V+P -> V+P+D.

This is impossible because the source contains two copies of V and the target only one. The profile is excluded.

## Reproduction

Run `python3 verify_v_d5_backward_gauss.py`. It executes the frozen mixed-octic closure and rank-three-pairing verifier unchanged. It checks the exact profile, pairing and line-image obstructions, all five Q image lists, the Wp O(7) vanishings, saturation bounds, the parity-improved kernel bounds, extension and degree calculations, final Euler characters, multiplicity contradiction and the four-type remainder relative to the frozen five-type list.
