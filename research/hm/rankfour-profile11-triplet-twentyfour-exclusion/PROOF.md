# Near-top derivative rigidity excludes defect twenty-four and fixes the defect-twenty image

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1212, including the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

Let F=p(K^-) be the actual projected rank-ten degree-minus-sixty-four bundle in the genuine fifteen-dimensional constant ambient V18* O. Let I=im beta_F be its coherent derivative image, E=O(2)+O(10) its saturation, and delta=length(E/I). Then:

1. The actual top-section representation satisfies

       H0(F(4)) is a subrepresentation of A+D.       (1)

   Consequently H1(F(4)) has neither V nor the trivial representation as a constituent.

2. The defect twenty-four is impossible. Consequently

       delta in {0,12,20}.                           (2)

3. If delta=20, its actual coherent image is necessarily

       I=O(2)+O(-10),
       O(2) subset I subset E,
       E/I = O(10)/O(10)(-D20),                     (3)

   where D20 is the unique reduced projective orbit of length twenty. At its points the local elementary-divisor orders of I subset E are zero and one. The alternative coherent type O(10)+O(-18) is excluded.

These are necessary conditions, not occurrence assertions. No remaining value is asserted realized, and I=E is not claimed unless delta=0. Neither retained F18 splitting type, either dual-extension class, another triplet coherent-image branch, or the full-positive branch itself is excluded or realized. The original defect remains t=0 and is distinct from delta. No fourth-jet separation, algebraicity, or whole-profile exclusion is claimed. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or relative normalization is selected or evaluated.

## 1. Complete immutable inputs and actual maps

INPUTS.json records three complete freshly fetched immutable sources with exact commits, paths, Git blobs, UTF8 lengths, and SHA256 hashes:

* PR1212 at ca235151d5d93bbead2beffa7640fbd0741aec43, research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md.
* PR1198 at 7d71f0e2a3963cff64a069198f4415c5cfd0fe9b, research/hm/rankfour-profile11-triplet-kernels/PROOF.md.
* PR1209 at 913892c66403ea57ed1681957ae1b9f8db9e5e15, research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md.

Their transitive actual-geometric hypotheses remain assumptions. The proof uses the actual K of PR1198 in its original constant ambient and the actual constant restriction of PR1209. It does not transfer a rank-seventeen theorem to the smaller ambient, and it does not identify the original constant span of K^- with that of F.

Work over C on the physical binary-icosahedral line, with G=SL2(F5), fixed determinant convention, A=Sym2 W, S4=Sym3 W, D=Sym4 W, V the other even three-space, and P the even four-space. All representations used here are self-dual. G has no nontrivial scalar characters and its smallest nonzero invariant effective divisor has degree twelve.

PR1198 gives exactly the following necessary actual K splittings:

    K1=(V+P)(-4)+T6(-5),
    K2=(V+2P)(-4)+W'(-7),
    K3=(V+P+D)(-4)+O(-10),
    K4=S4(-3)+(V+P)(-4)+W(-9),
    K5=S4(-3)+(V+P)(-4)+O(-8)+O(-10).              (4)

We use only two structural features of these established alternatives: K1,K2,K3 have top degree -4; K4,K5 have the shape

    K=S4(-3)+(V+P)(-4)+N,  top N<=-8.             (5)

No new splitting search or re-enumeration is performed.

PR1209 identifies the actual constant restriction

    p|K^-:K^- -> F

as an everywhere equivariant bundle isomorphism. PR1212 supplies

    rank F=10,  deg F=-64,  top F<=-4,
    chi_G(F(4))=-P-2D,
    0 -> F^- -> F -> I -> 0,
    I subset E=O(2)+O(10),
    rank I=2,  deg I=12-delta,
    delta in {0,12,20,24}.                          (6)

For delta=24, it also proves I=O(10)+O(-22). The actual kernel K^- above remains the backward kernel of K in its original constant ambient. Isomorphism transfers its cohomology to F; any derivative or horizontality argument below is carried out in that original ambient, not transported through an abstract splitting.

The fixed small character identities used are

    S4 tensor W=A+D,
    Sym12 W=1+A+P+D,
    Sym16 W=V+P+2D.                                (7)

They are universal physical-W identities, not actual-map evaluations.

## 2. A killed near-top direct summand cannot exist

We record the precise derivative argument, so that no connection-compatible splitting is assumed.

Suppose a nonzero actual subbundle U of K is abstractly R(-4), is an ordinary direct summand of K, and lies in K^-. Since U lies in the actual backward kernel, derivatives of its local sections lie in K. Its intrinsic second fundamental form in the original constant ambient therefore factors regularly through

    beta_U:U -> (K/U)(-2).                           (8)

The quotient is a bundle because U is a direct summand. In all types (4), top K<=-3. Since U is an ordinary direct summand, top(K/U)<=-3, so the target in (8) has top degree at most -5. Thus

    Hom(R(-4),(K/U)(-2))=0.

It follows that U is horizontal in the constant ambient. Its Grassmannian classifying map then has zero differential and is constant in characteristic zero; a saturated horizontal subbundle of a constant bundle is a constant bundle and has degree zero. This contradicts deg U=-4 rank U<0.

The contradiction is derived from the actual condition U subset K^-. The Birkhoff direct-summand property is used only to bound the quotient degrees, not to declare a summand horizontal in advance.

## 3. The actual top-section space contains neither V nor the trivial representation

Through p|K^-, the bound top F<=-4 gives top K^-<=-4 and

    H0(F(4))=H0(K^-(4))                             (9)

as representations. Evaluation of H0(K^-(4)), twisted by -4, is the canonical degree-minus-four block of K^- and is a subbundle. Thus every irreducible constituent R of that section space supplies an actual subbundle R(-4) of K^-.

First suppose K is one of K1,K2,K3, with top K=-4. Any such subbundle maps into the degree-minus-four coefficient block of K by a constant matrix: every map from O(-4) to a deeper ordinary summand is zero. Its image is consequently an ordinary direct summand of K. Section 2 excludes it. Therefore

    H0(K^-(4))=0  for K1,K2,K3.                     (10)

Now suppose K has the cubic shape (5). Then

    H0(K(4))=(S4 tensor W)+V+P=A+D+V+P.             (11)

All four constituents in (11) occur with multiplicity one. The subrepresentation H0(K^-(4)) can contain only these constituents.

If it contained V or P, its corresponding actual R(-4) subbundle could not map to S4(-3), because

    Hom_G(R(-4),S4(-3))=Hom_G(R,S4 tensor W)=0
    for R=V or P.

Its maps to N vanish by ordinary degree. Thus its image lies by constant coefficients in the (V+P)(-4) block and is an ordinary direct summand of K. Section 2 again excludes it. Only A and D remain possible. Combined with (9)-(10), this proves (1).

The Euler character in (6) gives, in the semisimple representation category,

    H1(F(4))=H0(F(4))+P+2D.                         (12)

In particular neither V nor the trivial representation occurs in H1(F(4)). No vanishing of this cohomology group was presumed. We do not need to decide which subrepresentation of A+D actually occurs.

## 4. Scalar quotient cohomology excludes defect twenty-four

If delta=24, the retained coherent splitting I=O(10)+O(-22) provides an actual equivariant surjection

    F -> I -> O(-22).                               (13)

Its kernel is locally free. Twist its exact sequence by four and take cohomology. Because H2 of a coherent sheaf on the projective line vanishes, (13) induces a surjection

    H1(F(4)) -> H1(O(-18))=Sym16 W=V+P+2D.          (14)

But the source in (14) has no V constituent by (12). Semisimplicity makes such a surjection impossible. Thus delta=24 is excluded, and (2) follows from (6).

This argument uses the actual quotient and its cohomology, not a chosen negative summand of F or a classification of a complementary kernel. It does not replace the coherent image by its saturation.

The same observation will be used once more below: there is no equivariant surjection F->O(-18). Such a quotient would induce

    H1(F(4)) -> H1(O(-14))=Sym12 W=1+A+P+D,         (15)

whereas the source in (12) contains no trivial constituent.

## 5. Two-column capacity leaves only two image shapes at defect twenty

Suppose delta=20, so deg I=-8. Write its ordinary splitting degrees as a>=b, with a+b=-8. We do not initially assume that equal-degree multiplicities split into scalar representations.

The actual coherent two-column capacity of PR1212 gives, for some 1<=k<=5,

    -64 <= (10-k)a+kb
             -[(10-k)(9-k)+k(k-1)].                 (16)

If a<=0, then 10-2k>=0 gives

    deg F
      <= (10-2k)a-8k-(90-20k+2k^2)
      <= -90+12k-2k^2
       = -72-2(k-3)^2
      <= -72,

contradicting deg F=-64. Therefore a>0. Since a+b=-8, the two ordinary degrees are unequal; their canonical highest-slope subbundle is a scalar O(a), with no character ambiguity.

The inclusion O(a)->I->E is nonzero. Its components are invariant sections of O(2-a) and O(10-a), where components of negative degree vanish. The top degree of E gives a<=10. Every possible nonnegative component degree is then less than twelve. A nonzero invariant section of positive such degree would give a forbidden invariant effective divisor. Thus a component can be nonzero only at degree zero, and

    a=2 or a=10.

Equivariant splitting consequently gives only

    I=O(2)+O(-10)  or  I=O(10)+O(-18).              (17)

No range of source splittings or actual coefficients has been scanned; the capacity square and invariant-divisor minimum force these two shapes directly.

The second shape in (17) would give the prohibited quotient F->O(-18) of (15). Hence

    I=O(2)+O(-10).                                  (18)

Both uses of capacity refer to the coherent I. The proof never substitutes E for I in that inequality.

## 6. The actual defect-twenty inclusion is cyclic on the orbit of length twenty

The actual highest-slope line O(2) of I in (18) maps into E=O(2)+O(10). Its component to O(10) is an invariant section of O(8), and is therefore zero. Its component to O(2) is a nonzero constant. Consequently it maps isomorphically onto the full O(2) subbundle of E, proving

    O(2) subset I subset E                          (19)

as actual coherent subsheaves. The lower O(2) summand of the retained equivariant splitting of E is unambiguous: possible different equivariant complements differ by Hom_G(O(2),O(10))=H0(O(8))^G=0. No horizontal splitting is asserted.

Quotient (19) by that common O(2). The remaining coherent line inclusion is

    I/O(2) subset E/O(2)=O(10).

Its source has degree -10, so it equals O(10)(-D_delta), where D_delta is the effective determinant divisor of I subset E and has degree twenty. Therefore

    E/I=O(10)/O(10)(-D_delta).                       (20)

The projective A5 orbit sizes are 12,20,30,60, as proved in PR1212. Thus an invariant effective divisor of degree twenty must be a single reduced orbit of length twenty. That orbit is unique. A5 has ten subgroups of order three, each with two fixed points on the projective line. These twenty points are distinct for distinct subgroups because finite point stabilizers are cyclic. They all have stabilizer of order three, hence they form one orbit of length twenty. Denote its reduced divisor by D20.

It follows that D_delta=D20, and (20) proves the quotient formula in (3). At any point of D20 the inclusion has one unit elementary divisor because of the full subbundle (19), and the other has order one because the determinant divisor is reduced there. Away from D20 it is an isomorphism. This is a universal local-module consequence of the actual sheaf inclusion, not an evaluated source-instance matrix or a selected point calculation.

No occurrence of delta=20 is asserted. The local description is conditional on that value, and the case delta=12 remains unresolved.

## 7. Contribution and exact stopping point

The root-cause obstruction is the near-top derivative rigidity of the original actual K. It controls the projected bundle's cohomology through the proved actual isomorphism p|K^- without transporting a rank-seventeen theorem or pretending a Birkhoff splitting is horizontal. The two forbidden scalar quotients are then excluded by genuine H1 surjections and missing irreducible constituents.

This removes delta=24 and fixes the actual cyclic shape of the largest remaining defect twenty. The proof uses no apolar coefficient construction, ideal enumeration, actual-instance evaluation, broad candidate scan, or additional computation beyond fixed universal characters and scalar degree identities. All other triplet-image branches remain separate, both original dual-extension alternatives remain open, and no value in (2) is realized or excluded beyond what is explicitly stated. The original t=0 and all fourth-jet/algebraicity boundaries are unchanged.
