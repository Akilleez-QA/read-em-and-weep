# Saturated lower cubic images and a torsion-sensitive quotient ledger

## 1. New result and scope

Retain the actual geometric hypotheses, physical marking and original negative parameter line in the six full sources pinned in INPUTS.json. Suppose the actual generic second-fundamental-form rank is four and its maximal ordered plateau is (k,l)=(3,1). Fix any T6 copy in H0(Q*(3)) and let J be the image of its restricted dual cubic derivative into E*(1).

If rank J is two or three, then J is saturated in E*(1), and the actual rank-four first quotient B=E/F2 has precisely the following necessary overlist. Direct sums in this statement are ordinary equivariant bundle splittings, not horizontal decompositions.

Rank three:

    J=V O(1),   B=V O + O(n),  n=2,4,6.              (1)

Rank two: write B=N+W' O(1-e), J=W' O(e). Then

    e=2: N=W O(3), W O(5), O(2)+O(4), O(2)+O(6),
           2O(4), O(4)+O(6);
    e=4: N=W O(5), O(2)+O(6), 2O(4), O(4)+O(6).     (2)

These are thirteen necessary J/B pairs, not assertions of existence or complete profile closure. They force the third plateau defect delta3=0, but not delta1=delta2=0. Their complete numerical case/degree overlist has 50 rows, including 37 with positive plateau defects. The actual inverse-image filtration further supplies a complete 96-row overlist of torsion-length partitions; 83 rows retain positive defects.

The rank-one O(9) branch is not analyzed here. No SF>=5, square surjectivity, full-adjoint invertibility or original proof repair follows. No actual coefficients, parameters, jets, matrices, instance ranks, or historical source enumeration are evaluated.

## 2. Actual inputs, kept in their unequal order

Use G=SL2(F5), T=P(W*) and irreducibles

    1,W,A=Sym2 W,S4=Sym3 W,D=Sym4 W,T6=Sym5 W,P,W',V,
    dimensions 1,2,3,4,5,6,4,2,3.

The physical three-spaces A and V are distinct. Center-odd irreducibles are W,S4,T6,W'. The group is perfect and every irreducible is self-dual.

The actual bundles satisfy

    0 -> E -> H O -> Q -> 0,
    rank E=17, rank Q*=13, deg E=deg Q*=-54, dim H=30;
    H=2A+2V+2P+2D.

The two actual Euler presentations use

    E: M3 O(-1) -> M4 O,
    Q*: M3* O(-1) -> M2* O,
    M2=A+2V+3P+4D,
    M3=3W'+3S4+6T6,
    M4=2V+4P+3D.

In particular chi(E(3))=U:=W'+2T6, and chi(Q*(3))=T6-2W-S4. The latter ensures a T6 section copy exists; it is not necessary to assume a canonical choice in the image argument.

The primary-slope source theorem gives all four necessary E types

    D: D O(-2)+(W'+T6) O(-3)+V O(-4)+O(-8),
    P: P O(-2)+(W'+T6) O(-3)+V O(-4)+W' O(-5),
    V: V O(-2)+(W'+T6) O(-3)+2V O(-4),
    Z: (W'+2T6) O(-3)+V O(-4).                         (3)

No source Z assumption is made. This actual primary theorem is retained with its transitive hypotheses, not re-enumerated.

The ordered saturated stages and quotients are

    F0 < F1 < F2 < F3=E < F4,
    ranks 5,9,13,17,21,
    Li=Fi/F(i-1), rank Li=4.

Actual kernel/saturation facts give regular generically invertible maps

    Li -> L(i+1)(-2),  i=1,2,3.                       (4)

Endpoint persistence gives H0(F0(3))=0, all degrees of F0 and F4^perp at most -4, and H0(Q*(2))=0. The last conclusion uses backward length k=3, not the forward length l=1.

Section 2 of the full original EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md proves a rank-independent consequence of H0(Q*(2))=0: exactly five necessary dual types

    Q*=T6 O(-3)+V O(-4)+R,
    R=(1+A)O(-6),
      W O(-5)+W O(-7),
      W O(-5)+O(-6)+O(-8),
      O(-4)+O(-6)+W O(-7),
      O(-4)+2O(-6)+O(-8).                            (5)

Only this conditional splitting result and its original positive Euler identities are used, not any rank-three corner exclusion. In particular maxdeg Q<=8. The five complete types are checked against both actual positive presentations; no historical classification is rerun.

## 3. The defect ledger and the correct lower-image quotient

Write a=deg F0, b=deg F4, ci=deg Li. Persistence, determinant parity and invariant A5 orbit sizes give

    a<=-20, b<=-36, all a,b,ci even,
    c(i+1)=ci+8+delta_i,
    delta_i in S=<12,20,30>,
    a+3b=-168+delta1+2delta2+3delta3.                  (6)

Equivalently a=-20-2u, b=-36-2v with

    2u+6v+delta1+2delta2+3delta3=40,
    c1=(-78-a-2delta1-delta2)/3 in 2Z.                (7)

This has 31 necessary rows, 24 with positive defects. In particular

    c3 in {-2,0,2,4,6,8,10}.                         (8)

The two c3=-2 rows have a=-24, delta1=delta2=0, and delta3=0 or12. The sole c3=0 row has a=-30 and all defects zero. No positive defect is discarded elsewhere.

Let Sbar be the saturation of J in E*(1), and put r=rank J. The generic full dual derivative image is the rank-four annihilator B*(1), where B=E/F2. Since this subbundle is saturated in E*(1), it contains Sbar as a saturated subbundle. Dualizing gives the actual exact sequence

    0 -> N -> B -> Sbar*(1) -> 0,
    rank N=4-r.                                      (9)

This is the key distinction from the full-rank case: Sbar is NOT identified with B*(1). The actual derivative identifies B(2) with its locally free image subsheaf in Q, not necessarily with its saturation. Consequently N(2) embeds into Q, so every ordinary degree of N is at most six by (5).

The image J is globally generated. The saturation Sbar is only generically generated by T6 O; global generation is not presumed. Nevertheless projection to each splitting summand R O(e) is nonzero, so e>=0 and T6 occurs in R Sym^e W. The inclusion into E*(1) imposes the same target Hom condition as for J. Thus each rank-at-most-three summand in either bundle belongs to

    V O(1), W' O(2), V O(3), W' O(4), V O(5),
    W' O(6), A O(7), W O(8), O(9).                   (10)

All blocks of a candidate must map into the SAME source type in (3). Repeated identical blocks require enough independent T6 intertwiners. In particular multiple O(9) blocks are impossible because T6 occurs just once in Sym9 W: all their maps factor through one diagonal line.

## 4. The lower images are already saturated

For rank two, the complete possible Sbar shapes from (10), cooccurrence and the single-intertwiner constraint are

    W' O(2), W' O(4), W' O(6), W O(8).

The maximum sum of two ordinary degrees of E*(1) across all four sources is 14. The determinant inclusion therefore excludes W O(8), whose degree is 16. Thus deg Sbar is 4,8 or12. Every actual rank-two image J in (10) has degree at least four, and its saturation defect is in S. Since 0<=deg Sbar-deg J<=8<12, the defect is zero: J=Sbar.

For rank three, (9), maxdeg N<=6, and c3>=-2 imply

    deg Sbar=deg N+3-c3<=11.                         (11)

The complete rank-three candidates from (10) with degree at most eleven are V O(1) and V O(3). Every rank-three actual image has degree at least three, so its saturation defect is at most eight and again is zero. Thus J=Sbar here too.

This kills only the cubic-image saturation defect. Plateau defects in (6) remain unrestricted until a specific numerical case forces a restriction.

## 5. A bounded representation inequality for the true quotient

The two interior derivative maps and H0(F0(3))=0 give

    H0(F2(3)) <= H0(B(1))+H0(B(-1))                  (12)

in the representation order. Indeed F2(3)->B(1) has kernel F1(3), and F1(3)->L2(1) has kernel F0(3); (4) embeds L2(1) into B(-1). Images need not be saturated for this inequality.

For any bundle C define

    T(C)=chi(C(3))+H0(C(1))+H0(C(-1)).

From (9), ordinary long exact cohomology and semisimplicity give the necessary inequality

    M(J,N):=T(N)+T(J*(1))-U is genuine.              (13)

To see the direction, chi(F2(3))=U-chi(B(3)) is at most the right side of (12); also H0(B(t)) is at most H0(N(t))+H0(J*(t+1)). This uses an upper bound on sections until splitting is proved, not a false equality from an unproved split extension.

The domain for N is finite without an arbitrary cutoff. For h=4-r and m=deg J,

    deg N=c3-r+m, c3 in the finite set (8),
    maxdeg N<=6,
    every ordinary degree of N >= m-r-2-6(h-1).      (14)

The last inequality follows by bounding the other h-1 ordinary line summands above by six. The coefficient parity of N is even overall, so each block R O(n) has parity R=n mod2.

We test all such N, (13), and necessary equivariant injection conditions into a common one of the five Q(-2) types. For a repeated identical summand, its multiplicity cannot exceed the dimension of its Hom space to that target; otherwise a nonzero constant linear combination of copies is killed. No injection is inferred merely from a nonzero Hom test.

These tests give exactly the following 23 preliminary pairs.

Rank three:

    J=V O(1): N=O(2),O(4),O(6);
    J=V O(3): N=O(4),O(6).                           (15)

Rank two:

    J=W' O(2): N=W O(1),W O(3),W O(5),
       O(-4)+O(4),O(-4)+O(6),O(2)+O(4),O(2)+O(6),
       2O(4),O(4)+O(6);
    J=W' O(4): N=W O(3),W O(5),O(2)+O(4),O(2)+O(6),
       2O(4),O(4)+O(6);
    J=W' O(6): N=W O(5),2O(4),O(4)+O(6).             (16)

## 6. Splitting is proved, including the two ordinary nonsplit possibilities

For (9), the equivariant extension space is the invariant part of

    Ext1(J*(1),N)=H1(N tensor J(-1)).                (17)

For all pairs (15)-(16) except J=W' O(2), N=O(-4)+O(4) or O(-4)+O(6), every ordinary degree in N tensor J(-1) is at least -1, and the entire ordinary extension space vanishes.

For either exceptional pair the only nonzero term in (17) is

    H1(W' O(-3))=W' tensor W=P.

It has no invariant vector, so the equivariant extension class is still zero. Thus every one of the 23 preliminary B bundles splits equivariantly as N+J*(1). We never replace an extension by its direct sum before this calculation. In particular the two exceptional cases are not discarded merely because their ordinary extension space is nonzero.

## 7. Endpoint tests remove exactly ten preliminary cases

Every preliminary case removed here has c3=-2 or0. The complete ledger then forces delta1=delta2=0; for c3=-2 it still allows delta3=12. Therefore the actual graded bundles below E satisfy

    L3=B, L2=B(-2), L1=B(-4),
    chi(F0(t))=chi(E(t))-chi(B(t))-chi(B(t-2))-chi(B(t-4)). (18)

For c3=-2, rank F0=5, a=-24 and maxdeg F0<=-4, so the complete ordinary window is [-8,-4]. For c3=0 the degree is -30 and the complete window is [-14,-4]. Equivariant rank/degree/parity splitting gives respectively 13 and 46 abstract shapes; the program derives each list twice from independent partitions.

The following table records all ten eliminated J/N pairs. An entry 0 means no endpoint in the forced window satisfies both exact Euler characters in (18) at twists three and four. An entry 2 means precisely the two endpoints displayed below remain.

| J | N | c3 | endpoints after both Euler tests |
|---|---|---:|---:|
| V O(3) | O(4) | -2 | 0 |
| V O(3) | O(6) | 0 | 2 |
| W' O(2) | W O(1) | 0 | 0 |
| W' O(2) | O(-4)+O(4) | -2 | 0 |
| W' O(2) | O(-4)+O(6) | 0 | 0 |
| W' O(4) | W O(3) | 0 | 0 |
| W' O(4) | O(2)+O(4) | 0 | 0 |
| W' O(6) | W O(5) | 0 | 2 |
| W' O(6) | 2O(4) | -2 | 0 |
| W' O(6) | O(4)+O(6) | 0 | 2 |

Whenever the table has two endpoints they are

    V O(-4)+O(-8)+O(-10),
    V O(-4)+W O(-9).                                (19)

For every corresponding B, the entire equivariant Hom space

    Hom_G(F0,B(-6))                                  (20)

is zero for each endpoint in (19). But the endpoint derivative takes values in L1(-2)=B(-6). Hence it is zero, forcing F0 constant in characteristic zero, contrary to degree -30. This is an exact universal Hom calculation, not a chosen matrix or rank evaluation.

All ten cases are excluded. The thirteen remaining pairs are exactly (1)-(2). Notice that the c3=-2 rows were excluded including their possible delta3=12 case; no unramified upper map was assumed.

## 8. Actual inverse images split the defects, not the connection

For any surviving pair set C3=J*(1), N3=N inside L3=B. Define N2 as the kernel of

    L2 -> L3(-2) -> C3(-2),

and define N1 as the kernel of

    L1 -> L2(-2) -> (L2/N2)(-2).

These are actual inverse images of generic rank-h kernels, not guessed summands. They are saturated in L2 and L1 since their quotient images are torsion-free. Put Ci=Li/Ni for i=1,2. Then rank Ni=h=4-r and rank Ci=r. The derivative induces regular generically invertible maps

    Ni -> N(i+1)(-2),
    Ci -> C(i+1)(-2),  i=1,2.                        (21)

Let their torsion lengths be nu_i and tau_i. The snake lemma applied to the two exact bundle rows gives exact sequences of actual torsion sheaves

    0 -> T_Ni -> T_Li -> T_Ci -> 0.

Consequently

    delta_i=nu_i+tau_i,
    nu_i,tau_i in S=<12,20,30>,  i=1,2.              (22)

The effective invariant-divisor condition applies independently to both blocks. These lengths need not vanish or equal each other. With p=deg C3=r-deg J,

    deg N2=deg N-2h-nu2,
    deg N1=deg N-4h-nu1-nu2,
    deg C2=p-2r-tau2,
    deg C1=p-4r-tau1-tau2.                           (23)

No splitting of any Fi, inverse-image extension, or ambient connection is needed for (21)-(23).

Crossing the thirteen surviving J/B pairs with the complete original 31-row ledger leaves 50 necessary rows: 13 zero-defect rows and 37 positive-defect rows. All have c3 in {2,4,6,8} and delta3=0. Partitioning delta1,delta2 by (22) gives 96 necessary rows: 13 zero-defect and 83 positive-defect. CASES.json and TORSION-LEDGER.json give every pair, endpoint degree, plateau defect, torsion partition and the resulting quotient/subbundle degrees. They are complete for the stated necessary conditions, not a realization theorem for these subbundles or extensions.

## 9. Reproduction and retained assumptions

Run python3 verify.py and python3 -O verify.py from any working directory. Both must match RESULT.json exactly. The portable standard-library verifier authenticates all six full originals, checks both actual presentations with fixed physical marking, derives both finite N domains and all endpoint domains independently, computes equivariant Ext rather than discarding nonsplit cases, verifies all endpoint exclusions, and checks every torsion partition and its degree additivity. It uses explicit exceptions, not assertions removed by optimization.

The new cubic-corner dependency is used only for Section 2's five dual splitting types under H0(Q*(2))=0. No rank-three conclusion is transported to rank four. The primary-slope source theorem retains its written transitive assumptions. Hashes authenticate source bytes, not those geometric assumptions. Saturation, actual sheaf images, derivative kernels and persistence are the written geometric inputs; the arithmetic certificate is not a proof assistant verification of the original theorem.
