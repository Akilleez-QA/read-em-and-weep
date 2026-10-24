# The actual dual extension has two rigid middle types and a canonical scalar-line incidence

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1210, hence the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

In the genuine fifteen-dimensional constant ambient V18 O, let S=ann(F) be the actual rank-five degree-minus-sixty-four bundle of PR1210. Retain the actual scalar line T0=O(-18), second jets T2=A(-16), and third jets T3=S4(-15) from PR1209. Then the actual extension

    0 -> T3 -> S -> O(-4) -> 0                         (1)

has exactly the following necessary alternatives:

1. If its equivariant extension class is zero, then

       S=S4(-15)+O(-4).

   Its canonical highest-slope subbundle U=O(-4) is an actual complement to T3 inside S.

2. If that class is nonzero, then

       S=W'(-11)+A(-14).                              (2)

   This middle type is proved by a universal binary apolar argument below, not assumed from the dimension of the extension space. Its canonical highest-slope subbundle U=W'(-11) satisfies the actual exact sequence and incidences

       0 -> T0=O(-18) -> U -> O(-4) -> 0,
       U intersect T3 = U intersect T2 = T0,
       U+T3=S.                                        (3)

   Moreover the intrinsic derivative of U has generic rank two and U^-=0. In particular, the actual S is the pushout of the two actual inclusions of T0 in U and T3:

       0 -> T0 -> U direct-sum T3 -> S -> 0.           (4)

The abstract direct sum in (2) is not a horizontal splitting and does not prescribe either summand's ambient embedding. The incidences (3)-(4) are proved separately from the actual maps.

Neither alternative is excluded or asserted realized. No fourth-jet separation, algebraicity, or new whole-branch exclusion is claimed. The original defect remains t=0; the new local derivative-image defect of PR1210 remains delta=0 or 12<=delta<=36. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or relative normalization is selected or evaluated.

## 1. Complete immutable inputs and actual extension

INPUTS.json records three complete freshly fetched immutable sources with exact commits, paths, Git blobs, UTF8 lengths, and SHA256 hashes:

* PR1210 at b2d020a32a3ac5aaf5f264e33e2f930c16195c34, research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md.
* PR1209 at 913892c66403ea57ed1681957ae1b9f8db9e5e15, research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md.
* ACTUAL at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md.

Their transitive actual-geometric hypotheses remain assumptions. The fixed physical group is G=SL2(F5) on P(W*), with det W=1. All irreducibles used here are self-dual; A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W, and W' is the other center-odd doublet. G has no nontrivial scalar characters. Its smallest nonzero invariant effective divisor on this line has degree twelve. No rank-seventeen statement from ACTUAL is transferred to S.

PR1210 supplies the actual saturated flag

    F subset J^- subset J subset V18* O,
    J^-/F=O(4),
    ann(J)=T2,  ann(J^-)=T3,
    S=ann(F),  S^-=T2.                                (5)

Dualizing the first quotient in (5) in the actual constant pairing gives (1). PR1209 identifies T2 and T3 by the actual intrinsic second- and third-jet maps of T0, not merely by their abstract splitting types. In particular

    T0 subset T1=W(-17) subset T2 subset T3,
    T0^+=T1,
    T3/T2=O(-12).                                     (6)

The physical symmetric-power facts required below are

    Sym6 W=V+P,
    Sym7 W=W'+T6,
    Sym8 W=P+D,
    Sym9 W=S4+T6,
    Sym10 W=A+V+D,
    Sym12 W=1+A+P+D,
    W' tensor W=P,
    W' tensor Sym2 W=T6,
    W' tensor Sym3 W=V+D.                            (7)

These are fixed universal representation identities; the checker verifies them using the physical-W character recurrence. No actual coefficients enter them.

## 2. The unique extension class is a polarized invariant

Equivariant Serre duality gives

    Ext1_G(O(-4),S4(-15))
      = (S4 tensor H1(O(-11)))^G
      = (Sym3 W tensor Sym9 W)^G.                    (8)

The Clebsch-Gordan decomposition is

    Sym3 W tensor Sym9 W
      = Sym12 W + Sym10 W + Sym8 W + Sym6 W.         (9)

Only the first summand has an invariant, and its invariant space is one-dimensional by (7). Thus (8) is one-dimensional. Write f for an unspecified nonzero element of the fixed universal line (Sym12 W)^G. The invariant tensor representing a nonzero extension class is a nonzero scalar multiple of the Cartan polarization

    Delta_(3,9)(f) in Sym3 W tensor Sym9 W.          (10)

Here f is a universal representation-theoretic invariant, not a selected actual HM coefficient or an evaluation of the degree-eighteen curve. No coordinate expression, scalar normalization, or value of f is chosen. Every nonzero element of the one-dimensional extension space has the same arguments below.

For precision about the dual conventions, put R=Sym(W*) and view elements of R as constant-coefficient differential operators on Sym(W). The invariant alternating form identifies W* with W equivariantly. Serre duality identifies H1(O(-11)) with Sym9 W in these conventions, and multiplication on H1 by a section h in H0(O(m))=Sym^m(W*) is contraction of that Sym9 factor by h. Changing divided-power normalizations changes only nonzero scalar factors and none of the kernels.

## 3. A self-contained binary apolar lemma

We need the following universal algebra fact, with its proof included to avoid importing a candidate computation.

Let f be any nonzero homogeneous binary form of degree d, let R=C[x,y] act by differentiation, and let Q=Ann(f). The finite-dimensional graded algebra R/Q has one-dimensional socle in degree d and no socle in smaller degree. Indeed a nonzero homogeneous class represented by h has h(f) a nonzero homogeneous polynomial of degree d-deg(h). If that degree is positive, at least one first derivative is nonzero, so the class is not killed by both x and y. In degree d the differential pairing has one-dimensional nonzero image C. All degrees above d vanish.

The minimal graded free resolution of R/Q over the two-variable polynomial ring has length at most two. The top Koszul homology identifies

    Tor_2^R(R/Q,C) = soc(R/Q)(-2),

so its final free module is a single R(-d-2). The rank Euler characteristic over the fraction field then makes the preceding free module have rank two. Thus, for positive integers a<=b,

    0 -> R(-d-2) -> R(-a)+R(-b) -> R -> R/Q -> 0.    (11)

The numerator 1-z^a-z^b+z^(d+2) of its Hilbert series has a double zero at z=1 because R/Q is finite-dimensional. Differentiating once gives

    a+b=d+2.                                         (12)

In particular Q has exactly two minimal homogeneous generators in those degrees. They have no common nonconstant factor, because R/Q is finite-dimensional; hence they form a binary complete intersection. This derivation uses only the two-variable free-resolution theorem and the displayed elementary Koszul-socle calculation. It does not choose or evaluate a form or a catalecticant matrix.

Apply this to the universal invariant f of degree twelve in (10). The ideal Q is G-stable. If a<7, then b=14-a>a, and Q_a is a unique one-dimensional minimal-generator space. G acts on it through a scalar character, necessarily trivial. It would therefore be spanned by a nonzero invariant form of positive degree a<7<12. Such a form defines a nonzero invariant effective divisor of degree a, contradicting the invariant-divisor minimum. Consequently

    a=b=7.                                           (13)

The equal-generator case has not been omitted: it is exactly (13), whose two-dimensional generator space is a G-subrepresentation of Sym7 W. By (7), it must be W', since the other irreducible summand T6 has dimension six. There is no relation in degree less than fourteen by (11). Therefore

    Q_m=0 for 0<=m<=6,
    Q_7=W',
    Q_8=W' tensor W=P,
    Q_9=W' tensor Sym2 W=T6.                         (14)

Equations (11)-(14) concern the fixed universal invariant line. No actual coefficient, apolar point, or instance matrix is computed.

## 4. Twisted connecting maps are the apolar maps

Assume the class of (1) is nonzero. Twist (1) by k=m+4, with 0<=m<=9. Since k<=13, H0(T3(k))=0. Its connecting map is

    partial_m: H0(O(m)) -> H1(S4(m-11)),
    partial_m: Sym^m(W*) -> Sym3 W tensor Sym^(9-m) W. (15)

The connecting homomorphism is cup product by the extension class. In the conventions of Section 2, it contracts the Sym9 factor of Delta_(3,9)(f) by the differential operator h. The polarization-contraction identity is

    partial_m(h) = c_m Delta_(3,9-m)(h(f)),
    c_m != 0,                                        (16)

where the constants depend only on factorial conventions. One may prove (16) directly by expanding the universal polarization of an arbitrary homogeneous degree-twelve form: differentiating m entries in the second factor leaves three entries in the first and nine-minus-m in the second, exactly the indicated polarization of the derivative. This identity is multilinear and universal; it is not a test on an actual form.

The Cartan polarization Delta_(3,9-m) is injective. Its multiplication composite is a nonzero scalar multiple of the identity on Sym^(12-m) W, in characteristic zero. Hence (16) gives the exact equality

    ker partial_m=Q_m.                               (17)

The range m<=9 matters: at m=10 the H1 target vanishes, so no extrapolation of (17) is made there.

Using (14)-(17) in the long exact cohomology sequence yields

    H0(S(k))=0 for k<=10,
    H0(S(11))=W',
    H0(S(12))=P,
    H0(S(13))=T6.                                   (18)

For k<4 the vanishing follows directly from (1); the range 4<=k<=10 is the apolar vanishing. At k=14, both H0(T3(14)) and H1(T3(14)) vanish because T3(14)=S4(-1). Therefore the actual quotient in (1) identifies

    H0(S(14))=H0(O(10))=Sym10 W=A+V+D.               (19)

Thus the connecting maps, including their precise cutoff, are established without assigning a differential connection to S/T3.

## 5. The nonzero middle type is forced

Use equivariant Birkhoff-Grothendieck splitting only for ordinary slopes and cohomology. By (18), S has no summand above degree -11. Its degree-minus-eleven multiplicity space is exactly W'. Accordingly its canonical highest-slope subbundle is

    U=W'(-11).                                       (20)

The contribution of U to H0(S(12)) is W' tensor W=P, already all of (18). Therefore there is no degree-minus-twelve summand. Its contribution to H0(S(13)) is W' tensor Sym2 W=T6, again already all of (18), so there is no degree-minus-thirteen summand.

The remaining three ordinary line summands have degrees at most -14. Their sum is

    deg S-deg U=-64-2(-11)=-42.

All three must consequently have degree exactly -14. Write their coefficient representation as R3. At twist fourteen, (19) and (7) give

    (W' tensor Sym3 W)+R3=Sym10 W,
    (V+D)+R3=A+V+D,
    R3=A.                                            (21)

This proves (2). The conclusion is a derived splitting classification, not an inference that a one-dimensional extension space automatically has some familiar middle bundle. No actual ambient embedding or horizontal splitting was used.

If the class of (1) is zero, its equivariant splitting gives S=S4(-15)+O(-4). Since the degree-minus-four summand is the canonical highest-slope subbundle and Hom(O(-4),T3)=0, it maps isomorphically to the actual O(-4) quotient. This proves the actual complementary assertion in alternative 1.

## 6. The nonzero case forces the actual degree-eighteen line into the top doublet

Continue in the nonzero case, and let U be the actual canonical subbundle (20). Restrict the actual quotient of (1):

    q|U:W'(-11) -> O(-4).                            (22)

It cannot vanish, since otherwise U would map into T3=S4(-15), while Hom(W'(-11),S4(-15))=0 by the negative degree difference -4. The entries of the nonzero equivariant map (22) are binary forms of degree seven. Their common-zero divisor is invariant and has degree at most seven, bounded by any nonzero entry. Since the smallest nonzero invariant effective divisor has degree twelve, this divisor is empty. Thus (22) is everywhere onto, and its kernel L is a saturated line in U and T3 of degree

    deg L=2(-11)-(-4)=-18.

There are no scalar characters, so L=O(-18) with the physical linearization. The composite from L to the actual quotient T3/T2=O(-12) is zero, because

    Hom_G(O(-18),O(-12))=(Sym6 W)^G=0.                (23)

Consequently L lies in the actual T2. Finally

    Hom_G(O(-18),T2)
      = (A tensor Sym2 W)^G
      = End_G(A)=C.                                  (24)

The actual intrinsic scalar-to-second-jet inclusion T0=O(-18)->T2 is one nonzero member of this space, by PR1209. Hence the nonzero inclusion L->T2 has the same image as T0. This identifies actual subbundles, without selecting their nonzero scalar ratio:

    L=T0.

The exact sequence (22) now proves U intersect T3=T0 and U+T3=S on every fiber. Since T0 lies in T2 subset T3, it also proves U intersect T2=T0. The addition map U direct-sum T3->S is onto, with kernel the anti-diagonal copy of T0, giving (4).

One further narrowly scoped derivative consequence follows: the restriction of beta_S to U has kernel T0, because S^-=T2 and U intersect T2=T0. Thus it has generic rank one and coherent image abstractly O(-4). This concerns the restriction of beta_S, not the intrinsic derivative of U. It does not say that this image is saturated in the actual normal target.

In contrast, the intrinsic derivative beta_U is generically injective. Indeed a local section of its backward kernel has derivative in U, hence in S, and therefore belongs to S^-=T2. Thus

    U^- subset U intersect T2=T0.

If U^- had rank one, it would equal T0: both are saturated lines in U with the same generic line. Its derivative containment would then force the actual forward transform T0^+=T1 into U. But T1 lies in T2, and U intersect T2=T0 has rank one, a contradiction to rank T1=2. The containment also rules out rank two for U^-. Therefore

    U^-=0,  generic rank beta_U=2.                    (25)

This is a first-derivative assertion for the actual canonical U. It does not assert that its coherent image is saturated or draw a new conclusion about the fourth jets of T0.

## 7. Contribution and exact stopping point

The new proof resolves the middle-bundle ambiguity of the embedded rank-five extension by deriving both necessary types. The nonzero case additionally forces the actual degree-eighteen scalar line into the canonical W'(-11) subbundle and gives the actual pushout incidence (4). The argument passes from an abstract extension classification to an actual embedded statement only in Section 6, using the genuine quotient, saturation, degree-seven divisor bound, and uniqueness of the scalar-line map into the actual second jets.

The universal degree-twelve invariant is used only as the unnormalized generator of a fixed one-dimensional representation space. Its apolar complete-intersection degrees and representation are proved, not computed on a selected form. All checks are fixed small representation identities or displayed rank/degree arithmetic.

No choice between the zero and nonzero extension classes has been made. The two retained F18 splitting alternatives, all other triplet coherent-image branches, and the original t=0 remain unchanged. The exact new defect delta is still open. No coherent image is silently replaced by its saturation, no quotient receives a connection, and no fourth jet, algebraicity, realization, higher-degree exclusion, or entire-branch exclusion is claimed.
