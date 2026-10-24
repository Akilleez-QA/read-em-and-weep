# Equality in the coherent two-column bound excludes the local defect twenty

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1213, hence the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

Let F=p(K^-) be the actual rank-ten degree-minus-sixty-four projected bundle in the genuine fifteen-dimensional constant ambient V18* O. Let I=im beta_F be its coherent derivative image, E its saturation, and delta=length(E/I). Then

    delta=20 is impossible,
    delta in {0,12}.                                 (1)

The proof uses equality and the two-unit slack in the actual coherent backward-kernel bound. The slack case is impossible by invariant divisors. One equality case forces a forbidden top-section constituent. The other equality case forces a negative auxiliary jet subbundle to be horizontal, contradicting its degree.

No occurrence is asserted for either value in (1); in particular delta=0 and I=E are not forced. The original defect remains t=0 and is distinct from delta. Neither retained F18 splitting alternative, either dual-extension class, another triplet coherent-image branch, or the whole full-positive branch is excluded or realized. The auxiliary higher-jet bundles used below are proved only inside the hypothetical delta=20 cases, from actual derivative maps and equal-degree comparisons. No fourth-jet separation for the original degree-eighteen curve, algebraicity, realization, or whole-profile exclusion is claimed. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or relative normalization is selected or evaluated.

## 1. Complete immutable inputs and actual normal flag

INPUTS.json records four complete freshly fetched immutable sources with exact commits, paths, Git blobs, UTF8 lengths and SHA256 hashes:

* PR1213 at 838bc46c3be7b4a40cb74017de421da44f00958e, research/hm/rankfour-profile11-triplet-twentyfour-exclusion/PROOF.md.
* PR1212 at ca235151d5d93bbead2beffa7640fbd0741aec43, research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md.
* PR1210 at b2d020a32a3ac5aaf5f264e33e2f930c16195c34, research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md.
* PR1199 at 95af2c0fa1e3cce92496a44ef9023708735e1ec7, research/hm/rankfour-profile11-triplet-deep-images/PROOF.md.

All transitive actual-geometric hypotheses remain assumptions. No rank-seventeen theorem is transferred to any bundle here. Every derivative below is the intrinsic derivative of an actual saturated subbundle in the same constant ambient V18* O.

Work over C on the physical binary-icosahedral line, with G=SL2(F5), the fixed determinant convention and the retained representation names. G has no nontrivial scalar characters and its smallest nonzero invariant effective divisor has degree twelve. The small fixed identities needed are

    Sym6 W=V+P,
    Sym7 W=W'+T6,
    Sym8 W=P+D,
    Sym9 W=S4+T6,
    (Sym6 W)^G=(Sym8 W)^G=0.                         (2)

PR1210 supplies the actual saturated normal flag

    F subset J^- subset J subset V18* O,
    J^-/F=O(4),  J/J^-=O(12),
    rank J^-=11,  deg J^-=-60,
    J^- is the actual backward kernel of J,
    E=(J/F)(-2)=O(2)+O(10).                         (3)

The actual subline (J^-/F)(-2) is exactly the O(2) subline in (3), not an arbitrarily chosen summand. Its degree fixes its abstract type, and any equivariant component to O(10) vanishes by the invariant degree-eight Hom space. In particular the actual derivative of J^- factors through

    beta_(J^-):J^- -> (J/J^-)(-2)=O(10).            (4)

No coherent fullness or rank is assumed for the map in (4).

We retain from PR1212 and PR1213

    rank F=10,  deg F=-64,  top F<=-4,
    H0(F(4)) subset A+D,
    delta in {0,12,20}.                             (5)

For a contradiction suppose delta=20. PR1213 then proves the actual coherent data

    I=O(2)+O(-10),
    0 -> F^- -> F -> I -> 0,
    O(2) subset I subset E,                         (6)

where the top O(2) of I maps isomorphically to the actual O(2) in (3). Thus its inverse image in F is geometrically distinguished by the actual quotient, even though no splitting is declared horizontal.

## 2. The capacity slack leaves only the two equality cases

Use the actual backward flag of PR1212:

    Q0=F,  Q_(i+1)=Qi^-,  Ri=Qi/Q_(i+1).

Every nonzero Qi has negative top degree, so cannot be horizontal. The positive quotient ranks are therefore two repeated k times and then one repeated 10-2k times, for one 1<=k<=5. The actual coherent quotient injections are

    Ri -> R_(i-1)(-2) -> I(-2i),
    R0=I.                                           (7)

These injections may initially have torsion cokernels; no saturation is substituted for them.

For (a,b)=(2,-10), the capacity bound is

    -64 <= (10-k)2-10k-(10-k)(9-k)-k(k-1)
         = -70+8k-2k^2.

Equivalently

    (k-2)^2<=1,
    k=1,2,3.                                        (8)

For each rank-two quotient define its nonnegative deficit by

    e_i=deg I(-2i)-deg Ri.

For a rank-one quotient define it by

    e_i=(2-2i)-deg Ri.

The sum of these deficits is exactly the difference between the capacity upper bound and deg F:

    sum e_i=2-2(k-2)^2.                             (9)

Thus k=1 or k=3 gives equality at every quotient; k=2 would give total deficit two.

The latter is impossible. For a rank-two quotient, the determinant of its coherent injection into I(-2i) gives an invariant effective divisor of degree e_i. Since e_i<=2<12, it is empty, so e_i=0. For a rank-one quotient Ri=O(c), the lower summand of I(-2i) has degree -10-2i. If e_i<=2, then

    (-10-2i)-c=-12+e_i<0.

Therefore that component vanishes, and the nonzero injection maps only to the upper scalar line O(2-2i), with zero divisor of degree e_i. It is invariant and has degree at most two, so again e_i=0. The sum cannot be two. Hence

    k=1 or k=3,  and every e_i=0.                    (10)

In these cases every rank-two map Ri->I(-2i) is an everywhere isomorphism. Every rank-one map identifies Ri with the full upper line O(2-2i), because its lower component vanishes by the twelve-degree gap and its upper map has degree zero. Between consecutive rank-two quotients the maps in (7) are likewise isomorphisms. These are actual coherent-map conclusions obtained from equality, not identifications of arbitrary splittings with a connection.

## 3. Two elementary tools for the auxiliary actual jets

We will need actual jet identifications at the equality cases. The complete universal identity from PR1199 is

    P^j(O(d))*=Sym^j W(j-d),  0<=j<=d.              (11)

It describes the intrinsic principal-parts source, whether the actual scalar coefficient system is complete or not.

For an actual saturated scalar line L=O(-d) in a constant bundle, its intrinsic order-j jet map is

    eta_j:P^j(O(d))* -> constant ambient.

Its generic image is the span of L and its derivatives through order j. If this image has a saturated rank-(j+1) containing bundle T_j of the same degree as the source in (11), then eta_j factors regularly through T_j by saturation. Its determinant has degree zero and is nonzero generically, so it is an everywhere isomorphism onto T_j. No actual coefficient or point is evaluated in this comparison.

Once T_j is thus identified with the actual j-th jets, its derivative has generic rank at most one: differentiating the local span of the first j+1 derivatives adds at most the next derivative. A nonzero projection of its derivative proves that this rank is exactly one. This local spanning argument is universal; it does not choose or test an actual jet value.

We also record a saturation-projection lemma. Suppose T subset B0 subset B1 are actual saturated subbundles of a constant ambient, derivatives of T lie in B1, and beta_T has generic rank one. Suppose its projection to (B1/B0)(-2) has coherent image exactly a subbundle line L1, everywhere onto. Let C be the saturation of im beta_T inside (B1/T)(-2). Its composite to the quotient by L1 vanishes generically, hence identically. Thus C maps to L1. The coherent image already projects onto L1, so the line-bundle map C->L1 is onto and hence an isomorphism. It follows also that im beta_T=C: its image under that isomorphism is all L1.

Consequently the actual forward transform T^+ is a saturated subbundle of B1, and

    T^+/T=L1(2),
    T^+ intersect B0=T,                              (12)

with the indicated quotient projecting isomorphically onto L1(2) in B1/B0. This lemma does not split B1/T horizontally or assume that its complementary normal directions are constant. It uses only an actual derivative, an actual projection, rank one and surjectivity.

## 4. The k=3 equality case forces a forbidden degree-four block

Assume k=3. The ranks of R0,R1,R2 are two; R3,R4,R5,R6 have rank one. Equality (10) gives

    R0=O(2)+O(-10),
    R1=O(0)+O(-12),
    R2=O(-2)+O(-14),
    R3=O(-4), R4=O(-6), R5=O(-8), R6=O(-10).

The last bundle Q6 is the actual line O(-10). Along the rank-one tail, the maps in (7) are everywhere isomorphisms, so the successive saturated forward transforms are Q5,Q4,Q3. Their ranks and degrees are respectively

    Q5: rank2, degree-18,
    Q4: rank3, degree-24,
    Q3: rank4, degree-28.

Starting with Q6, the intrinsic jet comparison (11) therefore identifies these as the actual first, second and third jets of that auxiliary degree-ten line. Write

    T0=Q6=O(-10),
    T1=Q5=W(-9),
    T2=Q4=A(-8),
    T3=Q3=S4(-7).                                   (13)

These names refer only to the auxiliary line in this hypothetical case, not to the original degree-eighteen curve.

The derivative of Q3 factors through R2(-2)=O(-4)+O(-16), with quotient R3=O(-4). By (10), its actual image is the full upper line O(-4). Its forward transform T4 is therefore the actual preimage of the upper O(-2) in R2=Q2/Q3. It is a saturated rank-five bundle in Q2 with

    T4/T3=O(-2),  deg T4=-30.

The intrinsic fourth-jet source has rank five and degree 5(4-10)=-30, so (11) identifies

    T4=Sym4 W(-6).                                  (14)

To cross the next rank-two stage, use the actual isomorphism R2->R1(-2) in (7). The image of T4 in R2 is its full upper O(-2), with kernel T3. Hence the derivative of T4, projected to (Q1/Q2)(-2), is everywhere onto that upper O(-2). Its generic derivative rank is one by the scalar-jet observation after (11). Apply the saturation-projection lemma with T=T4, B0=Q2, B1=Q1. It gives a saturated T5=T4^+ in Q1 with

    T5/T4=O(0),
    T5 intersect Q2=T4,
    deg T5=-30.

Its rank is six, and (11) has degree 6(5-10)=-30. Thus

    T5=Sym5 W(-5),                                  (15)

as the actual fifth jets. Its image in R1=Q1/Q2 is the full upper O(0).

Now use the actual isomorphism R1->R0(-2). The derivative of T5 projected to (F/Q1)(-2) is everywhere onto its upper O(0). Apply the same lemma with T=T5, B0=Q1, B1=F. The resulting saturated T6 in F satisfies

    T6/T5=O(2),  rank T6=7,  deg T6=-28.

Equal rank and degree with the intrinsic sixth-jet source give

    T6=Sym6 W(-4)=(V+P)(-4) subset F.               (16)

Taking global sections after twist four makes V+P a subrepresentation of H0(F(4)). This contradicts H0(F(4)) subset A+D in (5). Thus k=3 is impossible.

The lower-column directions O(-14), O(-12), and O(-10) were not split off horizontally. At each rank-two crossing, the actual upper projection, the rank-one derivative and the saturation-projection lemma supplied the needed actual inclusion and degree before the jet source was identified.

## 5. The k=1 equality case produces the actual eighth jets in F

Assume k=1. Now R0=I has rank two, and R1,...,R8 have rank one, with

    Ri=O(2-2i),  1<=i<=8.

The last bundle Q8 is the actual line O(-14). The rank-one tail consists of everywhere isomorphisms in (7). Successive forward transforms therefore give its actual jets through order seven, by the equal-degree intrinsic comparison (11). In particular

    Q1=F^-=P^7(O(14))*=Sym7 W(-7),
    rank Q1=8,  deg Q1=-56.                          (17)

The derivative quotient R1=O(0) maps isomorphically to the upper line of R0(-2)=I(-2). Consequently Q1^+ is the actual preimage in F of the full upper O(2) in I. Denote that preimage by G9. Then

    0 -> Q1 -> G9 -> O(2) -> 0,
    0 -> G9 -> F -> O(-10) -> 0,
    rank G9=9,  deg G9=-54.                          (18)

The intrinsic eighth-jet source of O(-14) has rank nine and degree 9(8-14)=-54. Thus

    G9=P^8(O(14))*=Sym8 W(-6)                       (19)

is the actual saturated eighth-jet bundle. No completeness of that auxiliary scalar coefficient system has been assumed.

## 6. Its actual ninth jets lie in J^-

By definition, G9 is the preimage of the upper O(2) under the actual coherent quotient F->I. The restriction of beta_F to G9 therefore has precisely the full upper O(2) image in E, with kernel Q1. By (3), that upper line of I is the actual lower normal subline (J^-/F)(-2) of E. Thus derivatives of G9 lie in J^-, and their projection onto

    (J^-/F)(-2)=O(2)

is everywhere onto.

Because G9 is the actual eighth jets in (19), its intrinsic derivative has generic rank at most one. The displayed nonzero projection proves rank one. Apply the saturation-projection lemma with T=G9, B0=F and B1=J^-. It yields a saturated rank-ten bundle T9=G9^+ in J^- such that

    T9/G9=O(4),
    T9 intersect F=G9,
    deg T9=-54+4=-50.                               (20)

The actual image of T9 in J^-/F=O(4) is the whole line. Consequently the inclusion F->J^-/T9 is onto with kernel G9, so

    J^-/T9 = F/G9 = O(-10)                          (21)

as actual quotient bundles.

The intrinsic ninth-jet source of O(-14) has rank ten and degree 10(9-14)=-50. It maps generically onto T9, by (19)-(20), and factors regularly through it by saturation. Equal degree proves

    T9=P^9(O(14))*=Sym9 W(-5).                      (22)

The generic jet rank ten here is proved by the everywhere nonzero normal projection from G9, not inferred from complete degree-fourteen coefficients or from the dimension of the original ambient.

## 7. The ninth-jet bundle would be negative and horizontal

The actual derivative (4) of J^- kills G9, since derivatives of G9 lie in T9 subset J^-. Its restriction to T9 therefore factors through the actual quotient in (20):

    T9/G9=O(4) -> O(10).

This equivariant map vanishes because

    Hom_G(O(4),O(10))=H0(O(6))^G=0.                 (23)

Thus derivatives of local sections of T9 lie in J^-. Its intrinsic derivative in the constant ambient factors regularly through the actual line quotient from (21):

    beta_T9:T9=Sym9 W(-5)
      -> (J^-/T9)(-2)=O(-12).

This Hom space is zero by ordinary degree, since -12-(-5)=-7<0. Therefore T9 is horizontal. It is a saturated subbundle of the constant ambient with degree -50, whereas a horizontal subbundle there is constant and has degree zero. This contradiction excludes k=1.

All possibilities in (8) have now been excluded. Therefore the hypothesis delta=20 is impossible, proving (1).

## 8. Contribution and exact stopping point

The proof upgrades the scalar capacity inequality only at its forced equality and two-unit-slack cases. Every slack term is treated as an actual coherent-map defect; the rank-one terms are shown to land in the upper line before applying invariant divisors. The auxiliary jet bundles are then built from actual derivative projections and equal-degree intrinsic principal-parts maps. No quotient connection or horizontal Birkhoff splitting is used to cross a rank-two stage.

The final k=1 obstruction uses the actual O(2) normal line from J^-/F and the genuine lower quotient J^-/T9=O(-10). It does not rely on completeness of auxiliary coefficients, on a theorem for a larger-rank bundle, or on evaluating a selected jet. Its higher-order auxiliary jets occur only within the contradicted delta=20 branch. The original degree-eighteen curve receives no new fourth-jet assertion.

The new local defect is reduced to zero or twelve. The original t=0, both retained F18 types, both dual-extension alternatives, other triplet coherent-image branches, and all realization/algebraicity boundaries remain unchanged.
