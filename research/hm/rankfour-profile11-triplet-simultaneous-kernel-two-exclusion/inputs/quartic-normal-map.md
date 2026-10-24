# The second-jet normal map is controlled by a unique universal quartic

## Statement and scope

Retain the actual-geometric hypotheses of PR1224 and PR1222 and all their complete transitive assumptions, in the residual simultaneous rank-seven k=2 case. Let L10=O(-10) be the actual canonical scalar line in G6=F6 intersect B7. Let Zj denote its actual intrinsic j-th jet span, and let Uj=h(Tj) denote the auxiliary degree-eighteen jet bundles.

The actual second jets are saturated and have type Z2=A(-8). They give a sheaf-exact sequence

    0 -> U5 direct-sum Z2 -> B5
      -> (B5/F6)|D12 -> 0.                             (1)

The left map is not a subbundle inclusion on D12: its fiber rank is seven there, and nine away. The sheaf intersection U5 intersect Z2 is zero, whereas their fiber intersection has dimension two on D12 and zero away.

Projecting (1) through the actual orthogonal quotient

    H=B5/U5=V_alt O

gives an actual generic isomorphism

    q:A(-8) -> V_alt O                                 (2)

with elementary divisor orders (0,1,1) on D12 and no defect away. In particular its fiber rank on D12 is one, and its determinant divisor is 2D12.

Let f12 be any nonzero vector in the fixed one-dimensional universal invariant space whose divisor is D12. Then the second exterior power has the exact divisor factor

    Lambda^2 q = c4 composed with multiplication by f12,
    c4:Lambda^2 A(-4) -> Lambda^2 V_alt O.             (3)

The normalized map c4 has elementary orders (0,0,1) on D12 and is invertible away. Its equivariant Hom space is one-dimensional, so its projective class is fixed universally. With the determinant-line identifications kept explicit, q is recovered from the second exterior power of c4; equivalently it is the appropriately determinant-twisted adjugate, not an unqualified same-direction matrix adjugate.

This is a new constraint on the actual higher-jet normal map and its exact torsion quotient. It does not exclude or realize the simultaneous image, the cyclic rank-seven case, original delta=12, either F18 form, or a whole branch/profile. No original tenth jet or algebraicity is inferred. No selected actual coefficient, graph scalar, point, jet, tensor, matrix, instance rank, or invariant normalization is evaluated. All local elementary-divisor statements follow from exact sheaves and universal module identities, not an actual matrix calculation.

## 1. Complete immutable inputs and actual geometry

INPUTS.json records complete freshly fetched originals, immutable commits and paths, UTF8 lengths, SHA256 and Git blobs:

* PR1224 at 317cf0c533b6ab8ce650d566e08c87610dd11ccd, research/hm/rankfour-profile11-triplet-top-jet-complement/PROOF.md.
* PR1222 at f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1, research/hm/rankfour-profile11-triplet-nonsplit-quotient/PROOF.md.

We work over C with G=SL2(F5), det W=1, A=Sym2 W and T6=Sym5 W. The alternate even triple is V_alt; the even four-dimensional irreducible is P. All determinant characters of the named representations are trivial.

The original degree-eighteen curve v spans the entire constant representation V of dimension fifteen. Its actual separated jets satisfy

    Tj=Symj W(j-18), Bj=ann(Tj), 0<=j<=9.

The actual symmetric constant h supplies Uj=h(Tj). In particular

    U4 subset F6 subset B6 subset B5,
    U5=T6(-13), rank U5=6, deg U5=-78,
    rank B5=9, deg B5=-78.

The top-jet theorem supplies the actual decomposition

    F6=U4 direct-sum Z1,
    Z1=L10^+=W(-9), L10 subset B7.                     (4)

The retained simultaneous-image hypothesis is the exact coherent statement

    E6=(B5/F6)(-2)=O(4)+O(2),
    im beta_(F6)=I6=E6(-D12).                          (5)

Thus its saturation is E6, and F6^+=B5. This does not yet identify the unsaturated coherent span of F6 and its derivatives; that span will be determined below.

Finally PR1222 constructs the actual orthogonal quotient

    T5^(perp_h)/T5=V_alt O.

Under h this is precisely

    H=B5/U5=V_alt O.                                  (6)

It is not B6/U5, which is instead the rank-two bundle W'(-3). We will only use (6) as an actual quotient; no connection is placed on H.

## 2. Structural completeness of L10, without a coefficient calculation

We first resolve the needed intrinsic second-jet source without presuming complete degree-ten coefficients or using the separate canonical-ten-line theorem.

Let R be the actual constant coefficient span of L10, of dimension r. It is a nonzero equivariant quotient of Sym10 W. In characteristic zero a scalar curve spanning a constant r-space has generic jet rank r at order r-1. Here is the formal reason. Its coefficient functions are linearly independent over C. Their Wronskian over C(t) is nonzero: divide by a nonzero first function, reduce to the functions 1 and their ratios, and expand the Wronskian along the first column. Induction reduces zero Wronskian to a constant linear dependence of the derivatives of the ratios, hence to a constant linear dependence of the ratios and 1, since the constants of C(t) are C. Thus the generic jet span is the whole R. This is a formal differential-field argument, not evaluation at any chosen point.

Successive annihilator differentiation gives

    derivatives of Bj lie in B_(j-1), j>=1.

Indeed differentiating an annihilation identity against T_(j-1) introduces only Tj. Starting with L10 subset B7, its jets through order k lie in B_(7-k) for k<=7, at least as coherent images; saturation preserves the inclusion because the containing Bj is a saturated subbundle of the constant ambient.

If r<=8, the generic (r-1)-jet span R would therefore lie in B_(8-r). The induced morphism from the constant R O to the quotient by this subbundle is generically zero and hence zero identically. Thus R O would lie in B_(8-r), and therefore in B0. But H0(B0)=0: a constant functional annihilating every fiber of the original scalar curve is zero because that original curve spans all fifteen dimensions. This contradiction proves

    r>=9.                                             (7)

The fixed physical decomposition is

    Sym10 W=A+V_alt+D,

a multiplicity-free sum of dimensions 3,3,5. Every proper quotient has dimension at most eight. Semisimplicity and (7) force r=11, and the coefficient quotient is an isomorphism. Hence L10 is the complete degree-ten Veronese curve in its actual eleven-dimensional constant span.

Its universal intrinsic jets are consequently globally saturated through order ten:

    Zj=Symj W(j-10), 0<=j<=10.                         (8)

This is a statement about the auxiliary degree-ten curve, not a new original degree-eighteen jet assertion. The complete evaluation maps are everywhere onto their principal parts; dualizing identifies the displayed sources with the actual saturated jet bundles. We need only

    Z2=A(-8), rank Z2=3, deg Z2=-24, Z2 subset B5.    (9)

The original full span used to prove (7) was never transferred to an auxiliary tail. The auxiliary completeness has just been proved separately from its actual B7 incidence.

## 3. The exact unsaturated sum and its torsion quotient

The coherent span of F6 and its first derivatives is, by (4) and the actual jet properties,

    S=U5+Z2 subset B5.                                (10)

Indeed U4 and its first derivatives coherently generate U5, and Z1 and its first derivatives coherently generate Z2. The corresponding jet maps are already globally saturated and separated in the needed orders, so there is no hidden saturation in these two assertions.

For the actual second fundamental form, the quotient of this coherent span by F6 is its coherent image tensored by the tangent line:

    S/F6=I6(2)=(B5/F6)(-D12).                          (11)

This follows directly by differentiating local sections in the constant ambient and contracting the image of beta_(F6) with the tangent bundle O(2). It is invariant under coordinate changes and gives no quotient connection. Consequently

    B5/S=(B5/F6)/(B5/F6)(-D12)
         =(B5/F6)|D12.                                (12)

The saturation of S is B5 by (5). The map U5 direct-sum Z2 -> B5 is therefore generically onto, and both source and target have rank nine. Its kernel is zero: a kernel subsheaf of a vector bundle that is generically zero is zero on the integral curve. This proves the exact sequence (1).

The quotient in (12) is a rank-two bundle restricted to the reduced divisor, not merely a torsion sheaf of length twenty-four with unspecified layers. Hence the full-rank inclusion in (1) has local elementary orders seven zeros and two ones at D12. Equivalently its fiber rank is seven there. Away from D12 it is an isomorphism. Since U5 and Z2 are individually saturated subbundles, their fiber maps into B5 are injective. The fiber intersection therefore has dimension 6+3-7=2 on D12 and zero away. Their sheaf intersection is nevertheless zero, as just proved. No intersection is commuted incorrectly with restriction to a fiber.

The degree check is

    deg B5-deg U5-deg Z2=-78-(-78)-(-24)=24,

in agreement with the exact rank-two quotient on a degree-twelve divisor. The exact quotient, not this length calculation, determines its local orders.

## 4. The actual rank-three normal map and its exterior divisor

Project Z2 into the actual quotient H=B5/U5 from (6). Equation (1) gives an exact sequence

    0 -> Z2=A(-8) --q--> H=V_alt O
      -> (B5/F6)|D12 -> 0.                            (13)

In particular q is generically an isomorphism and is injective as a sheaf. At the reduced divisor its cokernel is free of rank two over O_D. The structure theorem for a map of free modules over a discrete valuation ring therefore gives elementary orders

    (0,1,1).                                         (14)

This is the universal module consequence of the exact quotient. It is not obtained by selecting or evaluating a matrix of the actual q. Away from D12 there is no defect. Thus q has fiber rank one on D12 and determinant divisor 2D12.

For a rank-three map with orders (0,1,1), the second exterior power has the pairwise-sum orders

    (1,1,2).

It is therefore divisible by the local equation of D12 in every component, and not by its square in every component. These local divisibilities glue intrinsically. Write L=O(D12) and let s=f12 be its nonzero invariant section. There is a unique equivariant map

    c:Lambda^2 Z2 tensor L -> Lambda^2 H              (15)

such that

    Lambda^2 q = c composed with
        (id tensor s):Lambda^2 Z2 -> Lambda^2 Z2 tensor L.

Its local orders are (0,0,1), and there is no other defect. Since Lambda^2 Z2 tensor L=Lambda^2 A(-4), this is exactly c4 in (3). It is generically invertible, has fiber rank two on D12, and its determinant divisor is D12.

The section f12 is the fixed universal group invariant, not an actual HM coefficient selected for evaluation. Rescaling it simply rescales c inversely. All conclusions concern intrinsic maps or their projective classes.

## 5. The quartic Hom is one-dimensional

The two even triples A and V_alt are self-dual and have trivial determinant characters. Thus Lambda^2 A is isomorphic to A and Lambda^2 V_alt to V_alt. This identifies representation types only; no actual volume form or matrix entries are selected.

The fixed physical tensor identity is

    V_alt tensor Sym4 W=A+D+V_alt+P.                  (16)

It follows that

    dim Hom_G(Lambda^2 A(-4),Lambda^2 V_alt O)=1.       (17)

Hence the nonzero normalized map c belongs to one fixed universal projective class. Its existence here proves that this class has generic rank three and the stated divisor properties, conditionally on the retained actual configuration. No actual representative of the universal quartic class has been computed or normalized.

For comparison, the original degree-eight Hom has dimension two: A occurs twice in V_alt tensor Sym8 W. Thus (15)-(17) are a genuine additional exterior-power constraint on the actual map q, not merely a restatement of its source and target types.

## 6. Recovery with the determinant lines retained

We give a coordinate-free recovery statement to fix the direction and twists. For this section set E=Z2 and F=H. By (14), det q has exactly the divisor 2D12, so division by s^2 gives an everywhere nonzero determinant-line isomorphism

    d:det E tensor L^2 -> det F,
    det q=d composed with multiplication by s^2.      (18)

For every rank-three bundle J there is the natural isomorphism

    Lambda^2(Lambda^2 J) = J tensor det J.

Under these natural isomorphisms, exterior functoriality gives the universal identity

    Lambda^2(Lambda^2 q)=q tensor det q.

Take the second exterior power of (15), and use (18). Cancelling the common s^2 factor yields the exact identity

    Lambda^2 c = q tensor d                           (19)

as maps

    E tensor det E tensor L^2 -> F tensor det F.

The cancellation is legitimate for morphisms of vector bundles: multiplication by the nonzero divisor s^2 is injective, and the two maps agree away from its divisor and hence everywhere. Formula (19) is the appropriately determinant-twisted cofactor/adjugate identity; it is not an assertion that an ordinary adjugate has the same unmodified source and target.

With E=A(-8), F=V_alt O and L=O(12), the source of (19) is

    (A tensor det A)(-8),

and the target is V_alt tensor det V_alt. The map d reduces to a nonzero constant isomorphism det A -> det V_alt, because det E tensor L^2 has degree -24+24=0. Consequently (19) recovers the projective class of q from the unique projective class of c, without choosing either determinant-line normalization. Any equivariant identifications of E with A(-8) and F with V_alt O differ only by scalars, by irreducibility. Thus this projective assertion is independent of those identifications. In particular q is restricted to one projective class inside the two-dimensional Hom space noted above.

## 7. Contribution and retained boundaries

The actual second-jet projection now has an exact rank-two torsion quotient on D12, rank-one fibers there, and a normalized exterior-power map in a one-dimensional universal quartic Hom space. The determinant-line identity recovers its projective class. This strengthens the embedded normal-map constraint beyond the earlier decomposition of F6.

The structural coefficient-span argument is used only to resolve the intrinsic second-jet dependency and does not serve as a standalone repetition of the earlier degree-ten completeness result. The proof does not require that result's differential-operator calculation or the stationary-graph theorem. It does not differentiate the orthogonal quotient H or assume its trivial-bundle identification is connection compatible.

Neither the remaining simultaneous case nor any other branch is excluded or realized. Exact local orders in (14)-(15) concern these specific coherent quotient maps, not original tenth-jet separation or higher ramification/algebraicity. The original t, local delta, e9, cyclic rank-seven alternative, F18 alternatives and whole-profile questions remain distinct.
