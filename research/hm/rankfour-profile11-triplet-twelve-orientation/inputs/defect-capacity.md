# Two-column coherent capacity cuts the new local defect to 0, 12, 20, or 24

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1210, hence the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

In the genuine fifteen-dimensional constant ambient V18* O let F=p(K^-) be its actual rank-ten degree-minus-sixty-four subbundle. Write I for the actual coherent derivative image and E for its saturation, as in PR1210:

    I=im beta_F subset E=O(2)+O(10),
    delta=length(E/I).

Then the necessary defect possibilities sharpen to

    delta in {0,12,20,24}.                            (1)

If delta=24, the coherent image and its actual inclusion satisfy

    I is equivariantly isomorphic to O(10)+O(-22),
    E_{>=10}=O(10) subset I,
    E/I = O(2)/O(2)(-2D12),                           (2)

where D12 is the unique reduced orbit of length twelve for the projective icosahedral action. At each point of that orbit the two local elementary divisors of I subset E have orders zero and two; away from it I=E. Thus this endpoint defect is cyclic, not a sum of two independently vanishing image directions.

These are necessary conditions, not occurrence assertions. No value in (1), including 24, is asserted realized. The original defect remains t=0 and is distinct from delta. Neither retained F18 splitting alternative, either dual-extension class of PR1211, another triplet coherent-image branch, or the whole full-positive branch is excluded or realized here. No fourth-jet separation, algebraicity, or whole-profile exclusion is claimed. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or relative normalization is selected or evaluated.

## 1. Complete immutable inputs and actual objects

INPUTS.json records three complete freshly fetched immutable sources with exact commits, paths, Git blobs, UTF8 lengths, and SHA256 hashes:

* PR1210 at b2d020a32a3ac5aaf5f264e33e2f930c16195c34, research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md.
* PR1209 at 913892c66403ea57ed1681957ae1b9f8db9e5e15, research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md.
* ACTUAL at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md.

The new proof does not depend on the middle-type classification of PR1211; it works in both of its alternatives. All transitive actual-geometric hypotheses of the inputs remain assumptions. No rank-seventeen theorem is transferred from ACTUAL to F.

Work over C on the physical binary-icosahedral line P(W*) with G=SL2(F5), det W=1, and the retained physical representation conventions. Write A=Sym2 W, D=Sym4 W, P for the even four-space, and V for the other even three-space. All irreducibles used below are self-dual, G has no nontrivial scalar characters, and the smallest nonzero invariant effective divisor has degree twelve.

The actual retained data are

    rank F=10,  deg F=-64,  top F<=-4,
    rank beta_F=2 generically,
    0 -> F^- -> F -> I -> 0,
    I subset E=O(2)+O(10),
    rank I=2,  deg I=12-delta,
    F subset J^- subset V18* O,
    0 -> F -> J^- -> O(4) -> 0.                      (3)

Here I is locally free because it is torsion-free on the smooth line. It need not be a subbundle of E. All quotient bundles in (3) are the actual ones from the inputs. PR1209 identifies ann(J^-) with the actual saturated third jets S4(-15) of the degree-eighteen scalar curve. The degree-eighteen coefficient system has dimension fifteen, with actual coefficient kernel P in Sym18 W, and remains incomplete.

The fixed small representation identities used in the endpoint contradiction are

    Sym8 W=P+D,
    Sym14 W=A+V+P+D,
    P tensor Sym4 W=A+V+P+2D,
    Sym22 W=2A+V+P+2D.                              (4)

They are universal physical-W character identities checked in the bounded verifier, not evaluations of actual coefficient systems.

## 2. A two-column capacity inequality for the actual coherent image

Write the ordinary splitting degrees of I as a>=b. No equivariant splitting into two scalar lines is assumed at this stage: equal ordinary degrees may carry a non-scalar multiplicity representation. Thus

    deg I=a+b=12-delta.                              (5)

We prove that for some integer k with 1<=k<=5,

    -64 <= (10-k)a+kb
             -(10-k)(9-k)-k(k-1).                   (6)

The integer k will be the number of rank-two quotients in an actual finite backward-kernel flag, not a parameter scan.

Set Q0=F, and recursively set Q_(i+1)=Qi^- as long as Qi is nonzero, where the backward kernel is formed from the intrinsic derivative in the same constant ambient. Every Qi is saturated in Qi-1 and hence in the original constant ambient. Every Qi has strictly negative top degree because it is a subbundle of F, whose top is at most -4.

A nonzero Qi cannot have zero derivative. A saturated horizontal subbundle of a constant bundle on the complex projective line is constant: its Grassmannian classifying map has zero differential and is constant in characteristic zero. It would have degree zero, contradicting the strictly negative top. Consequently the ranks strictly decrease until the zero bundle is reached.

Put

    Ri=Qi/Q_(i+1).

In particular R0=F/F^-=I as the actual coherent quotient. For i>=1, derivatives of Qi lie in Qi-1 by the definition of Qi. Its intrinsic derivative therefore factors through the actual normal subbundle

    (Qi-1/Qi)(-2) subset (V18* O/Qi)(-2).

The induced map on its quotient is a coherent injection

    Ri -> R_(i-1)(-2).                               (7)

It is not required to be saturated. The quotients are locally free, and the injection follows from the exact backward kernel, not from replacing an image by a saturation. Composing (7) gives coherent injections

    Ri -> I(-2i).                                    (8)

The positive quotient ranks are nonincreasing by (7), and the first is two. Thus they consist of k copies of rank two, followed by 10-2k copies of rank one, for one k in 1,...,5; there are no other rank possibilities. This follows from the total rank ten and monotonicity, not from enumerating splitting candidates.

For a rank-two quotient Ri, (8) is generically full rank, so its determinant gives

    deg Ri <= a+b-4i.

For a rank-one quotient, its injection into I(-2i) gives

    deg Ri <= a-2i.

Summing the actual degrees of the successive quotient bundles yields

    deg F
      <= sum_(i=0)^(k-1)(a+b-4i)
           + sum_(i=k)^(9-k)(a-2i)
       = (10-k)a+kb-(10-k)(9-k)-k(k-1),              (9)

with the second sum empty when k=5. This proves (6). All possible coherent zeros in (7) are retained by the inequalities. The argument assigns no connection to I or to any quotient; every differentiation occurs only in an actual subbundle of the fixed constant ambient.

## 3. Any defect at least twenty-four forces the full top line into I

Suppose delta>=24. Then (5) gives a+b<=-12. If a<=2, equation (9) gives

    deg F
      <= (10-2k)a+k(a+b)
           -[(10-k)(9-k)+k(k-1)]
      <= 2(10-2k)-12k-(90-20k+2k^2)
       = -68-2(k-1)^2
      <= -68.                                       (10)

The substitution is valid since 10-2k>=0 for 1<=k<=5. Equation (10) contradicts deg F=-64. Hence a>2.

Since a+b<=-12, the two ordinary degrees are unequal. The highest-slope subbundle of the equivariant I is therefore a canonical rank-one bundle. G has no scalar characters, so it is O(a) with the physical linearization. Its composite with I subset E is nonzero. Degree makes its component to O(2) vanish, while the component to O(10) must be nonzero. In particular a<=10 and this component is an invariant section of O(10-a).

The degree 10-a is nonnegative and less than eight. If it were positive, its zero divisor would be a nonzero invariant effective divisor of degree less than twelve. Thus

    a=10,
    b=2-delta,
    I=O(10)+O(2-delta) equivariantly.                (11)

The direct sum in (11) is a bundle splitting only. More importantly, the actual top-line map O(10)->E_{>=10}=O(10) is a nonzero scalar map of equal-degree line bundles, hence an everywhere isomorphism. Therefore

    E_{>=10} subset I                                (12)

as actual coherent subsheaves. This is stronger than identifying the splitting of I; it will control its endpoint torsion in Section 7.

## 4. A quotient slope bound reduces the remaining range to delta<=30

Let the ten ordinary splitting degrees of F be f1,...,f10, each at most -4. Their sum is -64, so the smallest satisfies

    min F >= -64-9(-4)=-28.                          (13)

The quotient F->I in (3), composed with projection to the lower line in a splitting (11), gives an everywhere surjective ordinary map F->O(2-delta). In particular it is nonzero, so some splitting summand of F maps nontrivially to that line. Consequently

    2-delta >= min F >= -28,
    delta<=30                                       (14)

whenever delta>=24. Defects below twenty-four already satisfy (14), so delta<=30 in all cases. This uses only the existence of an ordinary quotient line; no horizontal splitting or actual coefficient normalization is chosen.

If delta=30, the line quotient has degree -28. Equations (13)-(14) force one ordinary degree of F to equal -28. The remaining nine degrees sum to -36 and are all at most -4, so each equals -4. Equivariant splitting then gives

    F=R9(-4)+O(-28),  dim R9=9.                     (15)

The scalar factor has no nontrivial character. This forced endpoint, rather than a list of possible bundle types, is the only splitting considered next.

## 5. The actual partial-system comparison excludes delta=30

The actual fifteen-dimensional coefficient system embeds in the complete degree-eighteen section space, with quotient P:

    0 -> V18* -> Sym18 W -> P -> 0.                  (16)

The actual third-jet evaluation is everywhere surjective, because its dual is the actual saturated injection S4(-15) of PR1209. Compare it with the complete third-jet evaluation. The complete kernel is universally the bundle of degree-eighteen forms divisible by the fourth power of the variable vanishing line:

    0 -> Sym14 W(-4) -> Sym18 W O
      -> P^3(O(18)) -> 0.

Both actual and complete evaluation maps have the same principal-parts target, and the inclusion in (16) commutes with them. The snake lemma, retaining the surjectivity of the actual evaluation, therefore gives the exact bundle sequence

    0 -> J^- -> Sym14 W(-4) -> P O -> 0.             (17)

In particular the rightmost map in (17) is onto everywhere. This is not inferred from a generic-rank calculation. The actual incomplete system is not replaced by a complete one; (17) compares their distinct kernels.

Twist (17) by four and combine its equivariant Euler characteristic with the exact sequence 0->F->J^-->O(4)->0 from (3). Since all indicated nonnegative line twists have vanishing H1,

    chi_G(F(4))
      = Sym14 W - P tensor Sym4 W - Sym8 W
      = -P-2D                                      (18)

by (4). Also the actual inclusions give an injection of representations

    H0(F(4)) -> Sym14 W=A+V+P+D.                    (19)

On the other hand, the forced endpoint splitting (15) gives

    H0(F(4))=R9,
    H1(F(4))=H1(O(-24))=Sym22 W.

Combining this with (18) and the last identity in (4) forces

    R9=Sym22 W-P-2D=2A+V.                           (20)

Equation (20) contradicts (19): the source would contain two copies of the irreducible A, whereas the target contains only one. Finite-group representations over C are semisimple, so such an injection is impossible.

Thus delta=30 is excluded. This is a cohomological multiplicity obstruction at a forced endpoint, not a test of the actual coefficient map or a scan through candidate splittings.

## 6. Projective orbit sizes give the exact remaining defect set

The projective action factors through A5, of order sixty. A finite subgroup of PGL2(C) fixing a point injects into the derivative character at that point and hence is cyclic: a finite-order transformation fixing the point with derivative one is the identity in characteristic zero. The possible cyclic subgroup orders of A5 are 1,2,3,5. Therefore every projective orbit has size

    60,30,20,12.                                    (21)

The determinant of I subset E defines an effective invariant divisor whose degree is delta. Its multiplicities are constant on each orbit, so delta is a nonnegative integer combination of the sizes (21). From delta<=30 and the exclusion of delta=30, the only possible totals are

    0,12,20,24.

Indeed an orbit of length at least thirty cannot occur; one orbit of length twenty cannot combine with a positive orbit length to stay below thirty; and the multiples of twelve below thirty are twelve and twenty-four. This proves (1) structurally, without checking a range of invariant polynomials or actual points.

There is exactly one orbit of size twelve. A5 has six subgroups of order five. Each has two fixed points on the projective line, and these fixed points are distinct for distinct subgroups because any point stabilizer is cyclic. Their twelve points all have stabilizer of order five, so they form one orbit. Denote its reduced divisor by D12. It follows in particular that an invariant effective divisor of degree twenty-four is necessarily

    2D12.                                           (22)

These are statements about the fixed projective group action, not selected evaluations of the actual source curve.

## 7. Conditional delta=24 has a cyclic doubled-orbit defect

Suppose delta=24. Equation (11) gives I=O(10)+O(-22), and (12) says that I contains the full actual top subbundle E_{>=10}=O(10). Quotienting by that common subbundle gives a coherent line inclusion

    I/O(10) subset E/O(10)=O(2).

Its degree is -22, so it is precisely O(2)(-D_delta), where D_delta is the effective determinant divisor of I subset E. Thus

    E/I = O(2)/O(2)(-D_delta).

The determinant divisor has degree twenty-four, so (22) identifies D_delta=2D12, proving (2).

Equivalently, over the local discrete valuation ring at an arbitrary point of D12, with any local uniformizer z, the inclusion I subset E has one elementary divisor a unit and the other z^2 up to a unit. The first unit comes from the complete top subbundle in (12), and the length two comes from (22). This is a universal local module consequence of the proved sheaf inclusion, not an evaluated actual matrix or a selected source-instance rank calculation. The torsion E/I is cyclic of local length two at each of the twelve points and vanishes elsewhere.

Nothing here proves that this conditional case occurs, and nothing identifies the remaining images for delta=12 or delta=20 with their saturations. The case delta=0 alone means I=E by definition.

## 8. Contribution and exact stopping point

The new two-column capacity argument uses the actual coherent image throughout. It forces every defect at least twenty-four into an embedded full-top-line situation, gives the sharp forced endpoint at thirty, and excludes that endpoint by one fixed equivariant Euler-character contradiction. The projective orbit sizes then leave exactly the necessary set (1). At the largest remaining value, the actual inclusion yields the cyclic local description (2), not merely an abstract splitting type.

The proof neither differentiates a quotient bundle nor substitutes a saturated image into the capacity inequalities. Its finite backward-kernel flag is used only for this universal degree bound; no new scalar-curve fourth-jet separation, higher-order integrability, or algebraicity conclusion follows. Both dual-extension classes and both F18 splitting alternatives remain open. The original t=0 is unchanged, and no occurrence claim is made for any of the four remaining local defect values.
