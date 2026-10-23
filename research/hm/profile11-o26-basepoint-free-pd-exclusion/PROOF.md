# A basepoint-free O(26) top system cannot have coefficient P+D

## Result and scope

For the zero-original-defect maximal profile-(1,1) labels

    G3.11.dc58cc54f352: A_q=O(-10)+O(-8)+O(26),
    G3.11.4b6dad66f329: A_q=W O(-9)+O(26),

the compatible sources

    E6  = (P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    E13 = (P+D) O(-2)+T O(-3)+W O(-9)

cannot have a basepoint-free degree-twenty-eight top section system. Together with PR813, these source branches must therefore have common divisor of degree20. The actual degree-ten block and endpoint intersections then remain governed by PR813 and PR825. No exclusion of that degree20 stratum, of either full label, of source2, or of the global rank possibility is claimed.

The proof is structural. It classifies a small exact top kernel, uses its actual internal derivative image, and excludes the forced first-polar alternatives by constant quotients, osculation, and exact intersections. The exceptional two-dimensional internal Hom space is retained in full; no coefficient is selected. There are no selected actual HM/source parameters, coefficients, points, derivative values, matrices, source-instance ranks, selected models, scans, or large computations. The bounded verifier checks declared universal character identities and supports, not an all-twist envelope.

## 1. Immutable inputs and notation

The repository is Akilleez-QA/read-em-and-weep. Original actual-bundle, quotient, source and label data are pinned at

    db51525015bb7c5e825833d550d08dedf6f6ea96,
    research/hm/order-four-quadratic-load/.

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json. The two labels have source indices112 and115 and respectively B_q=O(-28)+O(6)+O(8) and B_q=O(-28)+W O(7). The E6 tuple is (0,1,0,0,0,1,0,1); the E13 tuple is (0,1,0,0,0,0,1,0).

An E6 source listed for the second label is already impossible: only its one O(-10) summand can map to W O(-9), so the required rank-two negative quotient cannot be onto. Thus the matching E6/E13 cases displayed above are the only P+D source cases requiring the argument below.

Structural dependencies are:

- PR796, d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md, Section3's actual derivative-image sequence and Section8's quadratic-column constant-span principle.
- PR799, 2172e4a7abbbe232f9f448bea6fa01dee7927460, research/hm/profile11-quadratic-polar-obstruction/PROOF.md: first-polar generation and actual constant-quotient reasoning.
- PR813, 3f99ecf539a3a3da61743df0dff409e54270c865, research/hm/profile11-o26-divisor-reduction/PROOF.md: exact source overlists, the divisor alternatives0,12,20, exclusion of degree12, and the degree20 constant block.
- PR825, ea94799a3b1e1c18a4d83061b92d7e7e2f1c631e, research/hm/profile11-o26-degree10-endpoint/PROOF.md: the separate degree20 endpoint conclusion. It is used only for the final scope statement; the constant-residual argument needed here is proved afresh in Section5.

Each path is at https://github.com/Akilleez-QA/read-em-and-weep/blob/COMMIT/PATH for its displayed immutable COMMIT and PATH.

Work over C with binary icosahedral group G and the usual irreducibles W,Wp,A,V,P,S,D,T. Thus A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, Sym6 W=V+P, Sym7 W=Wp+T, and Sym8 W=P+D. All irreducibles are self-dual. The actual E is saturated in H O, with rank17, degree-54 and H0(E(1))=H0(E^-(2))=0.

Write

    F=(P+D) O(-2),
    E/F=T O(-3)+L,

where L is respectively O(-8)+O(-10) or W O(-9). The actual negative quotient A_q/O(26) is exactly L. Original defect zero gives the saturated derivative image A_q in Q(-2), Q=(H O)/E, and

    E^+/E=O(28)+L(2).                                (1)

Assume for contradiction that the map p:F->O(26) is everywhere onto.

## 2. Exact kernel support: twenty-five formal possibilities

Let K0=ker p. Strict-top vanishing gives

    0 -> K0(2) -> (P+D) O -> O(28) -> 0,
    rank K0=8, deg K0=-44,
    H0(K0(2))=0,
    H1(K0(2))=A+V+P+2D,
    chi_G(K0(3))=-W-S-T.                             (2)

Write U_j=U O(-j). For j>=4, an atom U_j consumes b=U tensor Sym^(j-4) W from the H1 budget, and contributes t=U tensor Sym^(j-5) W to the next H1, with t0 at j4. Every atom obeys (j-3)dim U<=20 and central parity. The complete admissible atom list, with its b and t characters, is

    atom    b                    t
    1_6     A                    W
    1_8     D                    S
    1_10    V+P                  T
    1_12    P+D                  Wp+T
    1_14    A+V+D                S+T
    1_18    A+V+P+D              W+Wp+S+T
    1_20    V+P+2D              S+2T
    A_4     A                    0
    A_8     A+V+P+D              W+S+T
    V_4     V                    0
    V_6     P+D                  T
    V_8     A+V+P+D              Wp+S+T
    P_4     P                    0
    P_6     V+P+D                Wp+T
    P_8     A+V+P+2D            S+2T
    D_4     D                    0
    D_6     A+V+P+D              S+T
    W_7     A+D                  W+S
    W_9     V+P+D                S+T
    W_13    A+V+P+2D            Wp+S+2T
    Wp_5    P                    Wp
    Wp_7    V+D                  T
    Wp_9    A+P+D                S+T
    Wp_13   A+V+P+2D            W+S+2T
    S_5     A+D                  S
    T_5     V+P+D                T.                  (3)

The dimension/parity bound has34 atoms; the eight omitted ones contain a forbidden trivial constituent or two P constituents. The accompanying checker verifies all34 individual identities. The coefficient at degree-3 is uniquely sum(t)-W-S-T and must be honest.

Exactly one W-producing atom occurs: 1_6,W_7,1_18,A_8,or Wp_13. Each consumes the unique A, so all other A-consuming atoms are then prohibited. The following nine residual configurations X_i have budget V+P+D and tail T+C_i:

    i   X_i                 C_i
    1   W_9                 S
    2   1_10+D_4           0
    3   1_10+1_8           S
    4   1_12+V_4           Wp
    5   V_6+V_4            0
    6   P_6                Wp
    7   Wp_7+P_4           0
    8   Wp_7+Wp_5          Wp
    9   T_5                0.                         (4)

This list is complete: exactly one T-producing atom is chosen; any leftover D is D_4 or1_8, any leftover V is V_4, and any leftover P is P_4 or Wp_5. Two T-producing atoms would either overlap P or V, or spend two D.

The full25 supports are explicitly the following five disjoint groups:

- C_i O(-3)+1_6+1_8+X_i, for i1,...,9; together with D_4+1_6+W_9 and T_3+1_6+1_20. These11 supports correspond to distinguished atom1_6. Without1_8, only W_9 or1_20 can supply S.
- C_i O(-3)+W_7+X_i, for i1,...,9. These9 correspond to W_7.
- Wp_3+D_4+1_18 and (Wp+S)_3+1_8+1_18.
- A_8+D_4 and S_3+A_8+1_8.
- T_3+Wp_13.

This is a human two-budget classification, not a support enumeration or an old numerical envelope. Every displayed support has rank8, degree-44 and both identities (2).

## 3. Actual internal-image alternatives

The internal derivative map K0->(E/F)(-2) has target

    T O(-5)+O(-10)+O(-12), or T O(-5)+W O(-11).

The complete nonzero channels to the T factor are

    T_5,V_6,P_6,Wp_7,A_8,W_9,1_10,1_12,1_18,1_20,Wp_13 -> T_5.

All have dimension one except 1_20 and Wp_13, which have dimension two. The only other channels are 1_10->1_10, 1_12->1_12 and1_12->W_11. Each support contains just one atom from this active list. Thus actual images from two different active source blocks never have to be combined.

We record why each possible nonzero image has the source's displayed bundle type.

- T_5 maps by a scalar isomorphism. V_6->T_5 is the tensor-V tautological inclusion, since T=V tensor W. A_8->T_5 is multiplication Sym2 W by the cube of the tautological line. These are saturated injections.
- P_6->T_5 is the restriction of contraction (V+P) O(-6)=Sym6 W O(-6)->Sym5 W O(-5), whose kernel is O(-12). The projection of this kernel to V O(-6) is a nonzero V system of degree6, which has no invariant base divisor. Hence the restriction to P_6 is injective everywhere, and saturated.
- Wp_7->T_5 is the tautological inclusion Wp tensor O(-2)->Wp tensor Sym2 W O, twisted by-5, using T=Wp tensor A. It is saturated.
- The unique channel W_9->T_5 is multiplication Sym1 W by the fourth power of the tautological line into Sym5 W. Multiplication by a nonzero homogeneous form is injective at every fiber, so this channel is a saturated injection with image W_9.
- The line sources 1_10,1_12,1_18,1_20 are injective as image sheaves. Their T coefficient degrees are5,7,13,15. A nonempty common divisor could only have degree12 in the last two cases, leaving a T system of degree1 or3, impossible. All nonzero T components are therefore nowhere zero. The possible tail components of1_10 and1_12 are scalar or tautological and are also nowhere zero. Every resulting diagonal line image is saturated.
- A nonzero Wp_13->T_5 cannot have rank-one image. A quotient line O(-j) has even j with6<=j<=12, and Wp occurs in Sym^(13-j) only at j6. But O(-6)->T O(-5) is zero. Thus the image has rank two and is isomorphic as an image sheaf to Wp_13. We do not yet assume its inclusion is saturated.

Let B be the raw first span of F, before saturation, and I its derivative image. In every case

    0 -> J -> I -> O(26) -> 0,
    0 -> F -> B -> I(2) -> 0.                         (5)

Since p is onto, the external O(26) is saturated. The image B is generated by the first polar (P+D) tensor W tensor O(-1), so every splitting degree of B is0 or-1. For t=length(F^+/B), invariance gives t0 or t>=12, while deg F^+<=0 gives t<=-deg B.

The forced first-polar types are

    J           rank B  deg B       B
    0             10      10        impossible
    1_10          11       2        impossible
    W_9           12      -4        (A+D) O+(Wp+T-S) O(-1), impossible
    V_6           13      -2        (A+V+D) O+Wp O(-1)
    Wp_7          12       0        (A+P+D) O
    1_12          11       0        (A+V+D) O
    T_5           16      -8        (A+D) O+(Wp+T) O(-1)
    A_8           13      -8        D O+(Wp+T) O(-1)
    1_20          11      -8        A O+(Wp+T) O(-1)
    P_6           14      -6        (A+D) O+T O(-1)
    1_18          11      -6        D O+T O(-1)
    Wp_13         12     -12        (Wp+S+T) O(-1).     (6)

These follow from chi_G(B)=Sym28 W-(P+D)-H1(J(2)) and chi_G(B(1))=Sym29 W-H1(J(3)). The checker verifies every row. Except possibly the last, all nonnegative or negative rows surviving the immediate contradictions are saturated by the preceding image argument or by t<12. In the last row, t is0 or12.

## 4. First-polar obstructions used repeatedly

Whenever B is saturated, its degree-zero part C O is genuinely constant, and B/C O is saturated in (H/C) O. The projected image bar F and its derivatives lie in B/C O. Therefore bar F cannot contain any full nonzero direct linear block: its first span would be a nonzero constant space inside a bundle of degree-1 summands.

We also need a generation observation. If a direct linear component U O(-1) of B/C O receives zero from F, the projected F lies in the complementary linear subbundle. Its derivative into U O(-1) tensor Omega1=U O(-3) is zero by degrees, since F=O(-2)^9. Therefore projection of the raw first span also misses U, contrary to the definition of B. Every such component must receive a nonzero map from F.

No equivariant D O(-2) embeds in (A+D) O or any constant subrepresentation of it: the tautological O(-6) in D O(-2) maps on coefficients through Sym6 W=V+P, absent from A+D.

The only linear channels from P+D to Wp+T are P->Wp, P->T, D->T, each one-dimensional. The first is the everywhere-onto tensor-Wp Euler map. The D channel is multiplication D O(-2)->T O(-1), everywhere injective. The standard contraction Sym8 W O(-2)->Sym7 W O(-1), with kernel O(-10), has all three channels nonzero: omission either misses Wp or puts a rank-two or rank-five subbundle in a rank-one kernel. Rescaling irreducible coefficients shows that any map with all three channels nonzero is onto. Its projection to T is also onto when both P and D channels are nonzero.

These facts immediately exclude the V_6 row of (6): the sole Wp linear component must receive a nonzero P channel, making it entirely contained in bar F.

They also exclude the T_5,A_8,1_20 rows. The Wp component must receive a nonzero P channel. If the P-to-T channel is zero, the full Wp component is contained in bar F. If it is nonzero, the D-to-T channel must also be nonzero, since otherwise D O(-2) would lie in the constant part, a subrepresentation of A+D. All three channels would then give the whole linear Wp+T part, again impossible.

## 5. A constant-span horizontal obstruction

We prove a useful lemma for the present matching E6/E13 sources. Let C0 O be any actual constant subbundle with

    F subset C0 O subset E^+,

and suppose its image in E^+/E is the whole positive O(28) summand of (1). Put N=E intersect C0 O and m=dim C0. Then

    rank N=m-1, deg N=-28,
    rank(N/F)=m-10, deg(N/F)=-10.                     (7)

The derivative of N lies in C0 O, so its image in A_q lies in the positive O(26). Hence N/F is killed by E/F->L. This latter map is zero on T O(-3) and an isomorphism on L by degree, equivariance and surjectivity. Therefore N/F is a saturated subbundle of T O(-3). Put Z0=T O(-3)/(N/F). It has degree-8 and all splitting degrees at least-3, since Z0(3) is globally generated.

The actual positive O(28) image C0 O/N is saturated in Q. Therefore E+C0 O is saturated in H O, and

    R=E/N=(E+C0 O)/C0 O=Z0+L

is a genuinely saturated subbundle of (H/C0) O. Its derivative lies in E^+/C0 O, whose quotient by R is L(2). The derivative of Z0 into the ambient quotient thus factors through L and vanishes by degrees. Its internal derivative Z0->L(-2) also vanishes. This makes the actual embedded Z0 horizontal, impossible since its degree is-8. Thus no such constant C0 exists.

This lemma excludes the two constant rows Wp_7 and1_12 of (6), since B=F^+ is then constant and its image in E^+/E is O(28) by (5). It also excludes t12 in the Wp_13 row: F^+ is then a constant twelve-space, and the raw B already maps onto O(28).

## 6. The two remaining T-linear rows

For J=P_6 or1_18, the saturated B is

    B=C O+T O(-1),  C=A+D or D.                       (8)

The D-to-T projection of F is nonzero, since otherwise D O(-2) lies in C, prohibited by Section4. If the P-to-T channel were nonzero, the projection would be all T O(-1), also prohibited. Hence the exact projected F is the saturated multiplication image D O(-2) in T O(-1); the P part lies in C.

Constant projection of the raw first span identifies the first span of this D O(-2) with T O(-1). Its quotient is O(4). Since its columns are quadratic, its second span is constant of rank at most7. The first span has rank6 and degree-6, so the constant span has rank7, and its quotient by T O(-1) is O(6). The induced derivative O(4)->O(4) is a nonzero constant, hence an isomorphism. Since T O(-1) has H0=H1=0, the constant coefficient space is H0(O(6))=Sym6 W, the complete evaluation sequence gives T O(-1)=U_5^6, and its backward kernel is D O(-2)=U_4^6.

Let C0 be the full constant span of B. Thus dim C0=dim C+7, and, after an actual constant splitting,

    B=C O+U_5^6,
    B^-=C O+U_4^6,
    deg B^-=-10.                                    (9)

The intersection E^+ intersect C0 O contains the saturated B of corank one. It is either B or the whole C0 O. The latter is impossible by Section5, since B already maps onto the positive O(28).

Therefore E^+ intersect C0 O=B. Put N=E intersect C0 O. The map B->E^+/E has zero component in L(2) by degrees and is onto O(28). Hence

    rank N=rank B-1, deg N=deg B-28=-34.

The actual connection gives N subset B^-: derivatives of N lie both in E^+ and in C0 O, hence in B. Both N and B^- are saturated in C0 O and have the same rank. They must be equal as sheaves, contradicting degrees-34 and-10. This excludes both rows (8).

## 7. The exceptional pure-linear row forces a tensor-quartic block

It remains to exclude J=Wp_13 with t0. Then

    B=F^+=(Wp+S+T) O(-1),
    0 -> Wp O(-11) -> B/F -> O(28) -> 0.             (10)

We derive the constant subsystem without importing an external line-quotient degree from another profile. Let C0 be the constant span of B and Q0=C0 O/B. Since B is pure linear, B^+=C0 O. Write s=rank Q0. The derivative of B kills F, so s<=rank(B/F)=3. Every degree of Q0 is positive: it is globally generated, and a trivial quotient would be a constant functional killing B and therefore its full span C0.

As H0(B)=H1(B)=0, C0=H0(Q0). Thus B is the complete evaluation kernel of Q0. Since deg Q0=12, rank Q0<=3, center parity and the coefficient Wp+S+T leave exactly

    Q0=O(4)+O(8),
    Q0=Wp O(1)+O(10),
    Q0=V O(4).                                      (11)

For completeness, a line O(12) has kernel coefficient Sym11 W=W+S+T, not ours. Two positive even lines summing to12 have degrees(2,10),(4,8),(6,6); only(4,8) works. A two-dimensional coefficient at common degree6 has wrong parity. For rank three, three even positive lines of total degree12 give none of the required coefficient. An irreducible three-space at degree4 is A or V; only V gives Wp+S+T. A two-space U at odd degree d plus a line of degree12-2d has d1,3,or5; only U=Wp,d1 gives the required kernel. These exhaust the rank bound.

The first case in (11) has backward kernel

    B^-=(A+V+P) O(-2),

which cannot contain F=(P+D) O(-2), since D is absent. In the second case, B=Wp O(-1)+U_9^10 and B^-=U_8^10. The saturated inclusion F subset B^- is an equality by rank and degree, but then its actual first span is only U_9^10 of rank10, not B of rank12. Both cases are impossible.

Hence Q0=V O(4), and the actual complete evaluation sequence gives

    C0=V tensor Sym4 W, dim C0=15,
    B=V tensor U_3^4,
    F=V tensor U_2^4,
    B/F=V O(2).                                     (12)

The last equality for F follows from its saturated inclusion in B^- and equal rank and degree. In particular differentiation induces an isomorphism

    B/F -> (C0 O/B)(-2).                             (13)

## 8. Endpoint intersection gives an impossible positive image degree

Let I0=E intersect B. By (10), I0/F=Wp O(-11), and B/I0=O(28). The second fundamental form of E^+, restricted to B, kills I0 because derivatives of E lie in E^+. By (13), this forces C0/(E^+ intersect C0) to have generic rank at most one. The intersection therefore has rank14 or15.

Rank15 would mean C0 O subset E^+, excluded by Section5. Thus Nplus=E^+ intersect C0 O has rank14. Its restricted derivative kernel on B contains I0 and has the same rank11. Both kernels are saturated, so equality holds. Twisting the quotient of (13) by two gives the exact sheaf sequences

    Nplus/B=Wp O(-9),
    C0 O/Nplus=O(30).                                (14)

These are sheaf identities; no claim about a full fiberwise intersection or saturation in H/E^+ is needed.

The map Nplus->E^+/E has zero negative component. It vanishes on B by degree; on its quotient Wp O(-9), the only possible negative components would be

    Wp O(-9) -> O(-6), O(-8), or W O(-7).

All are zero: Wp is absent from Sym3 W=S, Sym1 W=W, and W tensor Sym2 W=W+S. Therefore its image is exactly the positive O(28), already onto on B. Its kernel N=E intersect C0 O satisfies

    rank N=13, deg N=-30-28=-58.                     (15)

But the actual constant projection E->(H/C0) O has sheaf kernel N. It induces an injective map from the locally free image sheaf E/N, of rank4 and degree

    deg(E/N)=-54-(-58)=4,

into a constant bundle. Any bundle injecting into a constant bundle has every splitting degree at most zero, hence nonpositive total degree. The positive degree4 is impossible. This contradiction excludes the final row.

All basepoint-free P+D source alternatives have now been excluded. PR813 leaves only the degree20-divisor case, and PR825 gives its exact degree-ten endpoint intersections, without a full-label exclusion.
