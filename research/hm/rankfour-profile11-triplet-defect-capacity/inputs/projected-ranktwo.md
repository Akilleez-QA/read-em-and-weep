# The projected rank-ten bundle has derivative rank two with a controlled new defect

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1209, hence the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

Let p:C->V18* be the actual constant restriction from PR1209, and write

    F=p(K^-) subset V18* O,
    S=ann(F) subset V18 O.

The actual F has rank ten, degree -64, and full constant span V18*, of dimension fifteen. Let J=F18^- be the actual degree-eighteen first-jet-annihilator kernel of PR1209. Then:

1. The actual derivative beta_F has generic rank two, and its saturated image in its normal target is exactly

       E=(J/F)(-2)=O(2)+O(10).

   Equivalently the actual saturated forward transform is F^+=J. This is a saturation statement; the actual coherent image need not equal E.

2. The dual actual backward kernel and quotient are exactly

       S^-=ann(J)=A(-16),
       S/S^-=O(-12)+O(-4).

3. If I=im beta_F denotes its actual coherent image and

       delta=length(E/I),

   then

       rank F^-=8,
       deg F^-=-76+delta,
       delta=0 or 12<=delta<=36.

The integer delta is a new derivative-image defect for F. It is not the original defect t, which remains zero. No exact value of delta, equality I=E, fourth-jet separation, longer osculating flag, algebraicity, realization, or new whole-branch exclusion is claimed. Neither retained splitting alternative for F18 is excluded. No whole K splitting, triplet quotient, or maximal profile is excluded or realized. No actual coefficient, point, parameter, jet, tensor, matrix, or relative normalization is selected or evaluated.

## 1. Immutable inputs and retained actual flag

INPUTS.json records the complete immutable sources and their exact commits, paths, Git blobs, byte lengths, and SHA256 hashes. The principal input is PR1209 at commit 913892c66403ea57ed1681957ae1b9f8db9e5e15, path research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md, whose complete proof has SHA256 33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf. The universal principal-parts input is PR1199 at commit 95af2c0fa1e3cce92496a44ef9023708735e1ec7, path research/hm/rankfour-profile11-triplet-deep-images/PROOF.md. The physical representation and equivariant splitting conventions are those of ACTUAL at commit db51525015bb7c5e825833d550d08dedf6f6ea96, path research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md. Their transitive actual-geometric hypotheses remain assumptions. No rank-seventeen theorem is transferred to F or S.

Work on the physical binary-icosahedral line P(W*) over C with G=SL2(F5) and the fixed determinant convention. The constant pairing is the actual pairing V18* x V18. Retain from PR1209 the saturated actual flag

    F=p(K^-) subset J^- subset J subset V18* O,
    rank F=10,   deg F=-64,
    rank J^-=11, deg J^-=-60,
    rank J=12,   deg J=-48,
    J^-/F=O(4),
    J/J^-=O(12).                                      (1)

The map p is constant, p(K)=J, and p|K^- is an everywhere bundle isomorphism onto F. The full constant span of F is all V18*. In the dual constant ambient the actual second and third jets are

    T2=ann(J)=A(-16),
    T3=ann(J^-)=S4(-15),
    T2^+=T3.                                           (2)

In particular the actual first derivatives of local sections of T2 lie in T3. The degree-eighteen coefficient system has dimension fifteen and remains incomplete; the complete degree-eighteen section space has dimension nineteen.

The physical representation facts needed below are

    Sym4 W=D,
    Sym6 W=V+P,
    (Sym4 W)^G=(Sym6 W)^G=0.                           (3)

The group has no nontrivial scalar characters. All the bundles in (1) and their dual annihilators are center-even. The smallest nonzero invariant effective divisor on P(W*) has degree twelve.

## 2. The actual normal subbundle is O(2)+O(10)

The flag (1) gives an exact bundle sequence

    0 -> O(4) -> J/F -> O(12) -> 0.

Its equivariant extension group vanishes:

    Ext1_G(O(12),O(4))
       = H1(O(-8))^G
       = (Sym6 W)^G
       = 0.                                              (4)

Thus

    J/F=O(4)+O(12),
    E:=(J/F)(-2)=O(2)+O(10).                            (5)

This is an equivariant splitting of the actual quotient bundle, not a horizontal splitting or a chosen connection.

The derivatives of F lie in J. Indeed a local section of F has a local lift in K^- through the actual isomorphism p|K^-. Its derivative is the constant restriction p of the derivative of that lift. Since K^- is the actual backward kernel of K, those derivatives lie in K, and their restrictions lie in p(K)=J. Hence the intrinsic derivative of F factors regularly as

    beta_F:F -> E=(J/F)(-2)
                   subset (V18* O/F)(-2).                (6)

The final inclusion is a subbundle inclusion, because F and J are saturated in the same constant ambient and J/F is locally free. Thus rank beta_F<=2. Rank zero is impossible: a horizontal saturated subbundle of a constant bundle on the complex projective line is constant and has degree zero, whereas deg F=-64.

## 3. Negative top for F and its dual annihilator

We first record a universal complete-system kernel identity solely to control ordinary degrees. The actual coefficient sections give an injection

    V18* -> H0(O(18))=Sym18 W.

The actual order-three evaluation is the restriction of the complete order-three evaluation. The former is everywhere onto by the actual third-jet identification in (2); its kernel is J^-.

For the complete system, the kernel at the variable point consists of degree-eighteen forms vanishing to order at least four. Such forms are precisely multiples of the fourth power of the point's vanishing linear form. Universal multiplication gives the exact bundle sequence

    0 -> Sym14 W(-4) -> Sym18 W O
      -> P^3(O(18)) -> 0.                              (7)

This identifies the complete kernel without evaluating an actual curve, point, or coefficient. Comparing the actual and complete evaluation maps gives the actual injection

    J^- -> Sym14 W(-4).

Consequently

    F subset J^- subset Sym14 W(-4),
    top F<=-4.                                         (8)

No completeness is inferred for the actual fifteen-dimensional system. Its actual kernel J^- has rank eleven, whereas the complete kernel in (7) has rank fifteen.

Now S=ann(F) is a saturated bundle of rank five and degree -64. The full constant span of F is essential: it implies H0(S)=0, since a nonzero constant vector annihilating every fiber of F would cut its constant span down. Hence

    rank S=5,  deg S=-64,
    top S<=-1.                                         (9)

In particular F, S, and all their subbundles have strictly negative ordinary degrees at the top.

## 4. A finite coherent rank-one kernel-capacity lemma

We use the following direct consequence of differentiation in a constant ambient. Let Q be a saturated rank-n subbundle of a constant bundle, with strictly negative top degree, and suppose its actual derivative has generic rank one. Write its actual rank-one quotient as

    Q/Q^-=O(c).

Then

    deg Q^- <= (n-1)c-n(n-1).                           (10)

To prove this, set Q0=Q and Q1=Q^-. The derivatives of Q1 lie in Q0, so beta_Q1 factors through (Q0/Q1)(-2), a line. It cannot vanish: a negative nonzero saturated subbundle cannot be horizontal in a constant ambient. Indeed its Grassmannian classifying map would have zero differential and hence be constant in characteristic zero, forcing degree zero. Thus beta_Q1 has generic rank one and Q2=Q1^- has rank n-2.

Inductively, for every i=1,...,n-1 the derivative of Qi factors through (Q_(i-1)/Qi)(-2), is nonzero by the same negativity argument, and has rank one. We obtain actual coherent injections

    Qi/Q_(i+1) -> (Q_(i-1)/Qi)(-2)
              -> O(c-2i),
    rank Qi=n-i,
    Qn=0.                                              (11)

All kernels are saturated and remain subbundles of the negative-top Q. Zeros of the coherent injections in (11) are permitted; no image is replaced by its saturation. Adding their ordinary degree inequalities gives

    deg Q1
       <= sum_(i=1)^(n-1) (c-2i)
       = (n-1)c-n(n-1),

which is (10). This is a fixed finite rank-one derivative flag, not a search over bundle candidates or actual maps.

## 5. Simultaneous primal and dual capacities exclude rank one

Suppose rank beta_F=1. The annihilator transpose gives rank beta_S=1 as well. Write the actual scalar derivative quotients as

    F/F^-=O(a),
    S/S^-=O(b).

Their scalar characters are trivial, and center-evenness makes a and b even. The actual transpose is a nonzero coherent injection

    O(b) -> O(-a-2),
    a+b<=-2.                                           (12)

Apply (10) to F, of rank ten and degree -64. Its backward kernel has rank nine and degree -64-a, so

    -64-a <= 9a-90,
    a>=26/10,
    a>=4 since a is even.                              (13)

Apply the same lemma to S, of rank five and degree -64, using its negative top from full span in (9). Its backward kernel has rank four and degree -64-b. Hence

    -64-b <= 4b-20,
    b>=-44/5,
    b>=-8 since b is even.                             (14)

Combining (12)-(14) gives

    4<=a<=6,
    a=4 or a=6.                                        (15)

On the other hand, (6) makes the actual scalar quotient O(a) inject coherently and nontrivially into E=O(2)+O(10). Both options in (15) have zero equivariant Hom space:

    Hom_G(O(4),O(2)+O(10))
       = H0(O(-2))^G + (Sym6 W)^G
       = 0,
    Hom_G(O(6),O(2)+O(10))
       = H0(O(-4))^G + (Sym4 W)^G
       = 0.                                             (16)

This contradiction excludes rank one. The rank-zero case was already excluded in Section 2, so

    rank beta_F=2.                                     (17)

Both capacity inequalities matter: the primal inequality alone would not control larger scalar quotient degrees. The dual inequality is justified specifically by the proved full constant span of F.

## 6. The exact dual endpoint and the saturated forward transform

The annihilator transpose and (17) give rank beta_S=2 and rank S^-=3. By (2), derivatives of the actual T2=ann(J) lie in T3=ann(J^-). Since F subset J^-, we have T3 subset S. Thus

    T2 subset S^-.

The two sides have rank three and are saturated in the same constant bundle V18 O. Equality of generic spans and saturation therefore imply the actual equality

    S^-=T2=ann(J)=A(-16).                              (18)

Dualizing the actual inclusion F subset J in the constant pairing gives

    0 -> ann(J) -> ann(F) -> (J/F)* -> 0.

Consequently the actual quotient in (18) is

    B:=S/S^-=(J/F)*=O(-12)+O(-4).                       (19)

Equivalently B fits 0->O(-12)->B->O(-4)->0 and that extension splits equivariantly by the same invariant vanishing (4). The splitting (19) does not prescribe a connection on B.

The factorization (6) is now generically full rank in the rank-two subbundle E. Therefore the saturation of its actual coherent image in the full normal target is exactly

    saturation(im beta_F)=E=(J/F)(-2)=B*(-2).

The preimage of E(2)=J/F in the constant ambient is J. By the definition of the actual saturated forward transform,

    F^+=J.                                             (20)

Equations (18)-(20) are actual subbundle and saturation statements. They do not assert that beta_F is onto E everywhere.

## 7. The new coherent-image defect

Let

    I=im beta_F subset E,
    delta=length(E/I).

Because (17) gives full generic rank in E, E/I is torsion and delta is a finite nonnegative integer. On the smooth binary line I is locally free of rank two, as a torsion-free coherent subsheaf of E. Thus

    deg I=deg E-delta=12-delta,
    0 -> F^- -> F -> I -> 0,
    rank F^-=8,
    deg F^-=-64-(12-delta)=-76+delta.                    (21)

The determinant of I->E defines an effective G-invariant divisor whose degree is exactly delta. If it is nonzero, the invariant-divisor minimum gives

    delta>=12.                                         (22)

This new divisor belongs to beta_F in its genuine fifteen-dimensional constant ambient. It is not the original determinant defect t=0 retained in the earlier actual E0/S0 analysis. No conclusion about equality of these distinct defects is made.

## 8. A strict-top kernel lemma gives delta<=36

By (8), F^- subset F has top degree at most -4. In fact

    top F^-<=-5.                                       (23)

Here is the required actual argument. If F^- had an ordinary degree-minus-four summand, there would be a nonzero map U=O(-4)->F^- and hence into F. Since every ordinary degree of F is at most -4, any such map lands by constant coefficients in the degree-minus-four multiplicity block of an ordinary Birkhoff splitting of F. It is an everywhere line inclusion and an ordinary direct summand of F; the quotient F/U has top degree at most -4.

Because U subset F^-, its derivatives lie in F. The intrinsic second fundamental form of U in the constant ambient therefore factors through

    U=O(-4) -> (F/U)(-2).

The target has top degree at most -6, so this Hom space is zero. Thus U would be a negative horizontal line in a constant bundle, impossible. This proves (23).

The splitting is used here only to prove an ordinary degree bound and identify the top-degree line as an ordinary direct summand. It is not assumed horizontal. Horizontality is deduced from the actual derivative-kernel condition and the vanishing Hom space, and then contradicted. No equivariant choice of an actual coefficient line or evaluation is needed.

Since F^- has rank eight, (23) implies

    deg F^-<=8(-5)=-40.

Combining with (21) gives

    -76+delta<=-40,
    delta<=36.                                         (24)

Together with nonnegativity and (22),

    delta=0 or 12<=delta<=36.                           (25)

No exact value or realizability of any value in this interval is asserted.

## 9. Contribution and exact stopping point

The projected rank-ten bundle F now has an actual rank-two derivative, the exact dual endpoint S^-=A(-16), and the exact saturated derivative target O(2)+O(10). The proof excludes rank one using simultaneous nine-step primal and four-step dual coherent-kernel capacities, with the latter made available by the full constant span in the fifteen-dimensional ambient.

The coherent image itself remains distinct from its saturation. Its possible failure of equality is recorded by the new invariant divisor delta, bounded by (25). The top-degree argument uses the universal complete-system third-jet kernel only as a containing bundle for the actual partial-system kernel; it does not replace the actual degree-eighteen system with a complete one.

No fourth-jet separation, rank or image assertion for the derivative of J^-, longer osculating flag, algebraicity, realization, or whole-branch exclusion is proved. The original defect remains t=0, and the two retained F18 splitting alternatives remain unexcluded at this stage.
