# Six necessary constant-span forms for the degree-twenty cubic residual

## Result and boundary

Consider either matching zero-original-defect profile-(1,1) source

    G3.11.dc58cc54f352: E6 =(P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    G3.11.4b6dad66f329: E13=(P+D) O(-2)+T O(-3)+W O(-9),

whose top degree-twenty-eight section system is forced to have common divisor of degree20 by PR813 and PR840. Let C=Sym10 W be its actual constant degree-ten block, and put K=E^-. There is an exact sequence

    0 -> U_7^10 -> K -> M' -> 0,
    M'=ker[T O(-3) -> T20],
    T20=O(26)/(f20 O(6)), length T20=20.                (1)

The map to T20 is onto. Thus M' has degree-38; it is not to be identified with T O(-3), and no saturation of M' in the constant quotient is asserted.

The actual sheaf embedding T O(-3) -> (H/C) O has saturated image G0 of generic Gauss rank exactly one. Its saturation defect is 0 or12. Its full constant span C1 has dimension7,8,or9. Up to an equivariant constant identification of C1, there are precisely the following necessary alternatives:

    defect  dim C1  C1        G0 inside C1 O
       0       7    A+P       kernel of a basepoint-free O(18) quotient,
                             with the stipulated splitting T O(-3);
       0       8    A+D       annihilator of the first-jet bundle of the
                             projected degree-ten Veronese in A+D;
       0       9    P+D       U_5^8 in Sym8 W;
      12       7    V+P       U_5^6 in Sym6 W;
      12       7    A+P       A O plus V O(-2) in A plus P;
      12       7    V+P       V O plus V O(-2) in V plus P.             (2)

In the last two rows, the negative V O(-2) is the kernel of the unique P coefficient system P O->O(6). The first row may retain a choice of a P subspace in the multiplicity-two P part of Sym18 W. The table is a necessary classification, not a realization theorem: no assertion that all six rows occur for a fixed HM source is made. The torsion modification T O(-3)->G0, its compatibility with the rest of E, and any residual constant coupling remain unclassified.

No source label, the degree20 stratum, source2, or the global rank possibility is excluded here. All statements concern actual quotient/intersection maps, universal characters and arbitrary-point ramification inequalities. No selected actual HM/source coefficient, parameter, point, derivative value, matrix, source-instance rank, selected model, scan, or large computation is used.

## 1. Immutable inputs and notation

The repository is Akilleez-QA/read-em-and-weep. The original source and plateau inputs are pinned at

    db51525015bb7c5e825833d550d08dedf6f6ea96,
    research/hm/order-four-quadratic-load/.

The files used are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json. The displayed labels have source indices112 and115. Their quotients are A_q=O(26)+L, where L=O(-8)+O(-10) or W O(-9), respectively. Their original determinant defect is zero.

The structural dependencies are:

- PR840, commit a69b5a8b9a7c4cb673a89c6465e152fcf699840a, research/hm/profile11-o26-basepoint-free-pd-exclusion/PROOF.md: the basepoint-free P+D source exclusion, which together with PR813 forces the assumed degree20 stratum. It is used only to make this theorem necessary for the matching sources, not inside the residual classification.
- PR813, commit 3f99ecf539a3a3da61743df0dff409e54270c865, research/hm/profile11-o26-divisor-reduction/PROOF.md: the actual degree-ten block in the degree20-divisor stratum.
- PR825, commit ea94799a3b1e1c18a4d83061b92d7e7e2f1c631e, research/hm/profile11-o26-degree10-endpoint/PROOF.md: its exact endpoint intersections.
- PR798, commit 2bbf244bafc380cf5b0ce1114f86fcd8053e4e55, research/hm/profile12-backward-plateau-exclusion/PROOF.md: the generic internal/projected Gauss-rank inequality and maximal backward-index-one convention.
- PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md, Section8: the quadratic-column constant-span and gap lemma. Its needed special case is also explained in Section7 below.

Every path is at https://github.com/Akilleez-QA/read-em-and-weep/blob/COMMIT/PATH for the displayed immutable commit and path.

Work over C. The binary icosahedral group G acts on the parameter line through A5. Its orbit sizes are12,20,30,60. Write W for its defining two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W and T=Sym5 W, and Wp,V,P for the other irreducibles of dimensions2,3,4. All irreducibles are self-dual, and the group has no nontrivial one-dimensional characters. The central parity is positive on 1,A,V,P,D and negative on W,Wp,S,T. Put

    U_j^d=Sym^j W O(j-d) subset Sym^d W O.

The actual degree20 conclusions are

    F=(P+D) O(-2)=U_8^10,
    F^+=U_9^10,
    C=Sym10 W=A+V+D,
    E intersect C O=F,
    E^+ intersect C O=F^+,
    E/F=T O(-3)+L,
    E^+/E=O(28)+L(2).                                (3)

The map E->A_q is onto; its restriction to F has image f20 O(6) in O(26). The invariant degree20 divisor is reduced. The actual maximal backward index one gives

    rank beta_K <3.                                   (4)

## 2. The projected backward kernel is an elementary modification

Let I=f20 O(6) in O(26), and T20=O(26)/I. Dividing E->A_q by F->I gives an onto map

    E/F=T O(-3)+L -> T20+L.                            (5)

Its component to L is zero on T O(-3) by degrees and is an isomorphism on L by surjectivity. For the split L, the cross degree-two invariant vanishes; for W O(-9), the scalar statement is Schur's lemma. Thus the kernel of (5) lies entirely in T O(-3), and its map T O(-3)->T20 is onto. Indeed any desired torsion value with zero L coordinate has a preimage in (5), whose L coordinate must be zero.

The kernel of F->I is the actual backward transform F^-=U_7^10. The kernel diagram for the two surjections therefore gives (1). In particular

    rank M'=6, deg M'=-18-20=-38,
    K intersect C O=U_7^10.                           (6)

The sheaf map E/F->(H/C) O is injective because E intersect C O=F. Its T O(-3) factor is consequently an actual injective sheaf map to a constant bundle. Denote its saturation by G0. The image of K is the composite image of M' in this constant quotient, so it has the same generic plane as G0, but generally differs as a sheaf.

## 3. Gauss rank one and the two saturation defects

At the generic point, the derivative of K has a projected component equal to the derivative of its projected plane. The derivative of K intersect C gives an independent component in the kernel of that projection. Concretely the latter derivative is the nonzero rank-one map

    U_7^10 -> (U_8^10/U_7^10)(-2)

inside C/(K intersect C). Thus generic rank addition and (4) imply

    1+rank beta_(G0) <= rank beta_K <=2.              (7)

This uses only generic planes, so the length20 modification does not change the projected rank in (7).

Write delta=length(G0/T O(-3)). Since G0 is saturated in a constant bundle, deg G0<=0, so 0<=delta<=18. Its torsion support, with multiplicities, is invariant. The orbit sizes leave only

    delta=0 or12,
    deg G0=-18 or-6.                                 (8)

A rank-zero Gauss map would make G0 horizontal and hence constant in characteristic zero, contradicting either negative degree. Equation (7) therefore forces Gauss rank exactly one.

Let C1 be the full constant span of G0, equivalently of the original cubic columns. On an affine chart the map T O(-3)->H/C has polynomial columns of degree at most3. Their derivatives through order3 span their constant coefficients. For a generic rank-one Gauss increment, every successive increment is at most one: after adjoining one new vector, further new derivatives come only from its derivative. Hence

    7 <= m=dim C1 <=6+3=9.                            (9)

This is a degree-three column argument, not an evaluation at a chosen parameter. G0 is saturated in C1 O. The quotient Q=C1 O/G0 is positive: it is globally generated, and any degree-zero quotient would be a constant functional killing G0 and hence its full span. Its rank is s=m-6, with 1<=s<=3.

## 4. Defect zero: the seven- and eight-dimensional spans

Suppose delta=0, so G0=T O(-3), with no global sections. Its annihilator J=Q* in C1* O has rank s, degree-18 and generic Gauss rank one. Moreover J spans all of C1*: a constant vector annihilating every J fiber would be a global section of G0. Annihilator duality preserves Gauss rank by differentiating the constant pairing.

The exact sequence of G0 gives

    H0(Q)=C1+(V+P+D),
    H0(Q(1))=C1 tensor W+T.                           (10)

For s1, Q=O(18), and Sym18 W=A+V+2P+D gives C1=A+P. This is the first row of (2).

For s2, let the saturated backward kernel of J be O(-d). It is not horizontal, since J has only negative degrees. Its first saturation is J. The line therefore spans the same eight-dimensional constant space as J and is a basepoint-free eight-section degree-d system. Its first derivative has a zero divisor of degree

    r0=2d-20 >=0.                                    (11)

At an arbitrary point let 0=a0<a1<...<a7 be its vanishing sequence. The local first-jet ramification is a1-1. Every a_i with i>=1 is at least i+(a1-1), so the Wronskian weight is at least seven times that ramification. The characteristic-zero Wronskian is nonzero and has degree8(d-7). Thus

    7(2d-20) <=8(d-7),
    10<=d<=14.                                       (12)

Its ramification divisor is invariant, while (11)-(12) give 0<=r0<=8. The minimum orbit size12 forces r0=0 and d10. Consequently the actual first-jet bundle is W O(-9), and its map onto J is an isomorphism. Equation (10) now gives

    C1=H0(W O(9))-(V+P+D)=A+D.                       (13)

This derivation needs no classification of rank-two quotient splittings.

The line O(-10) spans C1*=A+D, so both its A and D components are nonzero. Each occurs once in Sym10 W. An equivariant constant change of coordinates therefore identifies it with the projection of the complete degree-ten Veronese to A+D. Its first jets give J, and G0 is their actual annihilator. This proves the second row of (2), not merely its character.

## 5. Defect zero: the nine-dimensional span

If s3, J is a negative rank-three subbundle of degree-18 with Gauss rank one, spanning nine constants. Its backward kernel J1 has rank two. The derivative of J1 into J/J1 has rank at most one and cannot have rank zero, since a horizontal nonzero subbundle of the negative J would be constant. Its backward kernel is therefore a line J0=O(-d). Neither this line nor J1 is horizontal. Thus

    J0^+=J1, J1^+=J,

as saturated sheaves, and J0 spans the same nine constants.

Let r0,r1 be the degrees of the first two nonnegative ramification divisors of this line curve. The successive line-quotient degrees are

    -d, 2-d+r0, 4-d+r0+r1.

Since their sum is deg J=-18,

    3d=24+2r0+r1.                                   (14)

At an arbitrary point with vanishing sequence 0=a0<a1<...<a8, the local first two ramification orders are a1-1 and a2-a1-1. The Wronskian weight is at least eight times the first plus seven times the second. Integrating and using its degree9(d-8) gives

    8r0+7r1 <=9(d-8)=6r0+3r1.                        (15)

Hence r0=r1=0 and d8. The nine independent sections are all of H0(O(8)). The actual line is the complete degree-eight Veronese, J=U_2^8, and constant annihilator duality gives

    C1=Sym8 W=P+D, G0=U_5^8.                         (16)

This proves the third row. Equations (14)-(15) are arbitrary-point Wronskian inequalities; no coefficient, point or derivative has been selected.

## 6. Defect twelve: the splitting is severely constrained

Suppose delta12. The rank-six saturated G0 has degree-6. Every splitting degree is at least-3: otherwise the corresponding quotient of G0 would receive zero from T O(-3), contradicting generic surjectivity. Every degree is at most zero because G0 is embedded in a constant bundle.

Let C2 O be its degree-zero part. This is an actual constant subspace. Every irreducible constituent U of C2 must have a nonzero channel T O(-3)->U O, so U occurs in

    T tensor Sym3 W=A+V+2P+2D.                       (17)

In particular there is no trivial constituent. As deg G0=-6, its constant rank is at most5. The only possible constant ranks are consequently0,3,4,5, with coefficients respectively0, A or V, P, D.

Constant rank4 is impossible: the remaining rank-two degree-6 negative quotient, all of whose degrees are at least-3, must be W O(-3) or Wp O(-3). It receives no map from T O(-3). Constant rank5 would leave O(-6), also impossible. These are actual quotient maps, not just incompatible rank counts.

If the constant rank is zero, all six degrees are-1. The first span of a pure linear bundle is its constant span. Gauss rank one forces m7, and Q=O(6). The vanishing H0(G0)=H1(G0)=0 identifies C1 with all H0(O(6)), so

    C1=Sym6 W=V+P, G0=U_5^6=T O(-1).                (18)

If the constant rank is three, its coefficient C2 is A or V. The remaining negative rank-three quotient has degree-6 and degrees in {-1,-2,-3}. Parity and rank leave either an even three-dimensional coefficient at degree-2, or scalar even lines; the alternative odd two-space at degree-1 would require a degree-4 line, while at degree-3 it would leave a degree-zero line. The scalar lines must be three O(-2) and receive no T O(-3). An A O(-2) also receives no such map, since A tensor W=W+S. Only V O(-2) remains, using V tensor W=T. Thus

    G0=C2 O plus V O(-2), C2=A or V,                 (19)

inside a genuine constant decomposition by C2. Indeed once G0 contains all of the constant C2, its image in any constant complementary quotient lifts as the whole direct sum, so no horizontal splitting of an abstract extension is being presumed.

## 7. The remaining quadratic factor spans precisely four constants

The actual V O(-2) in (19), in the constant quotient by C2, has Gauss rank one. Its quadratic columns make its constant span have rank four or five. Write O(b) for its saturated first forward quotient.

The quadratic gap principle says that in the rank-five-span alternative b<=2. Here is the degree argument in this special case. The first span has rank four and degree-6+b; its quotient in the constant five-space is O(6-b). Its derivative, factored through O(b), gives a nonzero map

    O(b) -> O(4-b),

forcing b<=2. The second span is constant by quadratic generation, so the displayed derivative is nonzero.

But the first derivative of V O(-2) is a nonzero equivariant map

    V O(-2) -> O(b-2).

It requires V to occur in Sym^b W. Its first occurrence is degree6, contradicting b<=2. Therefore this factor spans exactly four constants. Its constant coefficient is a four-dimensional quotient of V tensor Sym2 W=P+D, hence precisely P. The saturated quotient is O(6), and its coefficient map is the unique P constituent of Sym6 W=V+P. This identifies the embedded negative factor as the kernel of that P-system, and gives the last two rows of (2).

All six stated alternatives have now been derived. The proof classifies necessary saturated generic planes and their constant spans, while preserving the distinct elementary modification M' in (1). It neither declares that modification saturated nor supplies the remaining coupling to C or to L.
