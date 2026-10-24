# A canonical complete degree-ten Veronese line in the seventh original annihilator

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1216, hence the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

The original scalar line is O(-18) in the genuine fifteen-dimensional constant ambient V18 O. Its actual coefficient system V18* is a proper fifteen-dimensional subspace of Sym18 W, with quotient P. Write T_j for its actual saturated order-j jets and B_j=ann(T_j) in V18* O. PR1216 identifies these actual jets through order nine.

There is a unique nonzero G-equivariant map O(-10)->B7 up to scalar. It is an everywhere saturated line inclusion. Denote its image by L10. Its constant coefficient span R11 in V18* has dimension eleven and representation A+V+D=Sym10 W. In this span L10 is the complete degree-ten Veronese scalar line. In particular its intrinsic differential-evaluation maps are everywhere subbundle injections for exactly the stated range

    P^j(O(10))* -> R11 O,  0<=j<=10,
    T_j(L10)=Sym^j W(j-10).                         (1)

The actual coherent derivative beta_(B7):B7->O(2) restricts nontrivially to L10. Up to a nonzero scalar this restriction is the universal degree-twelve invariant

    f12:O(-10)->O(2).                               (2)

Its zero divisor is the reduced twelve-point orbit D12. Equivalently, the everywhere rank-two first osculating bundle of L10 satisfies

    T_1(L10)(q) subset B7(q) if and only if q in D12. (3)

Thus the vanishing in (2) is normal-incidence vanishing, not intrinsic ramification of L10.

This result is unconditional within the retained full-positive branch and does not assume either value of its local defect delta or of PR1216's endpoint e9. It decides neither delta nor e9, does not prove original tenth-jet separation, and makes no occurrence, algebraicity, full-branch, or whole-profile exclusion assertion. The original degree-eighteen system remains incomplete. The eleven-dimensional span in (1) is not the full fifteen-dimensional ambient. Both retained F18 types and both dual-extension alternatives remain untouched. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or relative normalization is selected or evaluated.

## 1. Complete immutable inputs and representation conventions

INPUTS.json records three complete freshly fetched immutable originals, with commit, repository path, complete UTF8 byte length, SHA256, and Git blob identity:

* PR1216 at 66a6bfe8dd424da58f3d775be1818d1f4f71eff1, research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md.
* PR1212 at ca235151d5d93bbead2beffa7640fbd0741aec43, research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md.
* PR1199 at 95af2c0fa1e3cce92496a44ef9023708735e1ec7, research/hm/rankfour-profile11-triplet-deep-images/PROOF.md.

All their transitive actual-geometric hypotheses remain assumptions. Work over C on the physical binary-icosahedral line X=P(W*) with G=SL2(F5), det W=1. Thus H0(O(d))=Sym^d W, and determinant-one duality identifies the symmetric powers with their duals. All coefficient pairings below use the actual dual constant ambients V18* and V18; these identifications do not exchange their roles.

The fixed even irreducibles A,V,P,D have dimensions 3,3,4,5, with A=Sym2 W and D=Sym4 W. They are self-dual and pairwise nonisomorphic. G has no nontrivial scalar character. The fixed small representation identities needed here are

    Sym8 W=P+D,
    Sym10 W=A+V+D,
    (Sym12 W)^G=C.                                 (4)

In particular neither Sym8 W nor Sym10 W has invariant vectors. Every nonzero invariant effective divisor on X has degree at least twelve, and a degree-twelve invariant divisor is exactly the unique reduced orbit D12. The divisor D12 determines an invariant section f12 of O(12), unique up to a nonzero scalar. Indeed its defining section is semi-invariant because the divisor is invariant, and the scalar character must be trivial. This is a fixed universal invariant of the physical group action, not a selected coefficient of the actual HM system. No formula or normalization for f12 is used.

From PR1216 retain

    T_j=P^j(O(18))*=Sym^j W(j-18),  0<=j<=9,
    B_(j+1)=B_j^- in this range,
    beta_(B7):B7 -> (B6/B7)(-2)=O(2) is onto,
    ker beta_(B7)=B8.                              (5)

The beta maps are intrinsic second fundamental forms in the original constant ambient. No quotient bundle is assigned a connection.

## 2. The actual partial-coefficient comparison at orders seven and eight

The actual original scalar line has full constant span V18, so dual evaluation on its global sections gives the actual injective coefficient map

    alpha:V18* -> H0(O(18))=Sym18 W.

The complete actual coefficient comparison of PR1212 identifies its quotient:

    0 -> V18* -> Sym18 W -> P -> 0.                 (6)

At order j the complete degree-eighteen evaluation sequence is

    0 -> Sym^(17-j) W(-j-1) -> Sym18 W O
      -> P^j(O(18)) -> 0.                          (7)

The left term is universal: at the variable source point its forms are precisely the degree-eighteen forms divisible by the (j+1)-st power of that point's vanishing linear form. This construction needs no selected point or coefficient evaluation.

By (5), the actual evaluation V18* O->P^j(O(18)) is everywhere onto for j<=9, with kernel B_j. Comparing it with (7) and using (6), the snake lemma gives exact bundle sequences

    0 -> B7 -> Sym10 W(-8) -> P O -> 0,
    0 -> B8 -> Sym9 W(-9) -> P O -> 0.              (8)

In particular the rightmost maps are everywhere onto, not merely generically onto. These sequences retain the distinction between the actual partial system and the complete system. Their ranks and degrees agree with rank B7=7, deg B7=-88, rank B8=6, deg B8=-90.

## 3. The unique invariant section gives an actual saturated line

Twist the first sequence in (8) by ten and take invariant global sections. Left exactness of global sections and exactness of taking invariants for a finite group over C give

    H0(B7(10))^G
      =ker[(Sym10 W tensor Sym2 W)^G
             -> (P tensor Sym10 W)^G]
      =C.                                          (9)

Indeed the source has dimension one because A occurs once in Sym10 W, while the target is zero because P does not occur there. No H1 vanishing or surjectivity on global sections is assumed.

Choose only the nonzero map class supplied by (9); its image is independent of the scalar representative. Let its saturation in B7 be a line bundle M. If its zero divisor has degree e, then

    M=O(-10+e), e>=0.

The map and its saturation are G-equivariant, so its zero divisor is invariant. The inclusion M->B7->Sym10 W(-8) forces -10+e<=-8, hence e<=2. The invariant-divisor minimum forces e=0. Thus the map itself is an everywhere line subbundle of B7, with image L10=O(-10).

Since B7 is saturated in the constant ambient, L10 is also saturated there: the ambient quotient by L10 is an extension of the locally free bundles B7/L10 and V18* O/B7. This proves the asserted existence, uniqueness up to scalar, and saturation without a chosen actual coefficient line or evaluated matrix.

## 4. Pairing with the original scalar curve identifies a universal biform

Let v18 denote the original scalar map O(-18)->V18 O and let ell10 denote O(-10)->V18* O just constructed. On X_x times X_y their actual pairing is a G-invariant section

    b(x,y)=<v18(x),ell10(y)> of O(18,10).           (10)

It is nonzero. Otherwise every fiber of ell10 would annihilate the constant span of v18, which is all V18, and ell10 would be zero.

Let Omega(x,y) be the determinant biform cutting out the diagonal; it has bidegree (1,1) and is invariant because det W=1. The inclusion L10 subset B7=ann(T7) says that the derivatives of (10) in the x direction through order seven vanish along the diagonal. Equivalently b belongs to the eighth power of its ideal. This can be checked in local trivializations: a local transverse diagonal coordinate divides the biform to order at least eight, independently of the trivialization. The diagonal is Cartier, so globally

    b=Omega^8 q,  q in H0(O(10,2))^G.              (11)

By (9) and (4), this invariant space has dimension one. The Cartan polarization polar_(10,2)(f12) is a nonzero element of it. Here Cartan polarization means the canonical SL2-equivariant map Sym12 W->Sym10 W tensor Sym2 W, normalized, if desired, by restriction to the diagonal recovering the original form. The normalization is immaterial. Consequently

    b=c Omega^8 polar_(10,2)(f12), c nonzero.       (12)

This is an identification of the entire actual pairing as a universal biform up to scalar, derived from invariant multiplicity and diagonal contact. It does not select a representative of an actual HM coefficient system.

## 5. The coefficient operator is the second transvectant

For an arbitrary binary form f of degree twelve, the construction

    f |-> Omega^8 polar_(10,2)(f)

is a nonzero SL2-equivariant linear map Sym12 W->Sym18 W tensor Sym10 W. It is nonzero since Cartan polarization is injective and multiplication by the nonzero polynomial Omega^8 is injective. Using determinant-one duality on the second factor, its adjoint is an SL2-equivariant bilinear map

    Sym12 W tensor Sym10 W -> Sym18 W.

Clebsch-Gordan gives multiplicity one for this target, with transvectant order r determined by 12+10-2r=18, hence r=2. The second transvectant is nonzero; for example its defining differential operator has the nonzero universal leading term derived below. Therefore the coefficient operator of (12), under this canonical duality, is a nonzero scalar multiple of

    T_f12:Sym10 W -> Sym18 W,
    g |-> (f12,g)_2.                               (13)

The exponent eight in (12) is the diagonal exponent, not the transvectant order. Choices of normalized versus unnormalized transvectant alter only the nonzero overall scalar.

We now prove injectivity of (13) structurally. For homogeneous forms F(X,Y) and G(X,Y) of degrees twelve and ten use the unnormalized second transvectant

    F_XX G_YY - 2 F_XY G_XY + F_YY G_XX.

Write f(t)=F(t,1), g(t)=G(t,1), using a formal affine coordinate t, not a selected source point. Homogeneity and the chain rule give its exact dehomogenization

    132 f g'' - 198 f' g' + 90 f'' g.              (14)

For completeness, F_XY=11 f'-t f'' and F_YY=132 f-22t f'+t^2 f'', with the analogous degree-ten formulas G_XY=9g'-t g'' and G_YY=90g-18t g'+t^2 g''. Substitution cancels every positive power of t outside f and g and gives (14).

Consider any homogeneous second-order linear equation

    a h''+b h'+c h=0

over the differential field C(t), with a nonzero. Its rational solution space has C-dimension at most two. If there is a nonzero rational solution h0, write h=h0 u. Subtracting u times the equation for h0 gives

    a h0 u''+(2a h0'+b h0)u'=0.

Thus u' satisfies a first-order homogeneous equation with nonzero leading coefficient. The rational solution space of that first-order equation has dimension at most one, because the ratio of two nonzero solutions has derivative zero and is therefore constant. The linear map h |-> (h/h0)' has kernel C h0. This proves the bound; if no nonzero h0 exists the bound is immediate. The argument is entirely in C(t) and chooses no point.

Apply this to (14), whose leading coefficient 132 f12 is nonzero. Dehomogenization embeds degree-ten forms into C[t], so

    dim ker T_f12 <=2.                             (15)

Because f12 is G-invariant and the transvectant is equivariant, this kernel is a G-subrepresentation of Sym10 W=A+V+D. Semisimplicity and the irreducible dimensions 3,3,5 exclude every nonzero subrepresentation of dimension at most two. Hence

    ker T_f12=0.                                   (16)

This excludes the root cause of an incomplete auxiliary coefficient system without evaluating any actual curve, universal invariant at a point, or coefficient matrix.

## 6. The eleven-dimensional span is a complete degree-ten Veronese system

The scalar map ell10 induces a coefficient map

    gamma:H0(O(10))*=Sym10 W* -> V18*.

Its composite with the injective alpha of (6) is the flattening of b, hence is injective by (12)-(16). Therefore gamma is injective. Put

    R11=im gamma subset V18*.

This is the constant span of L10, is G-stable, has dimension eleven, and is isomorphic to Sym10 W*=Sym10 W=A+V+D. It is canonical as the span of the unique line image; under alpha its image is precisely im T_f12, independently of the nonzero scalar normalization.

The coefficient map Sym10 W*->R11 is an isomorphism. Consequently L10 in R11 O is the complete degree-ten scalar system, equivalently a rational normal degree-ten Veronese curve after a constant linear change of ambient coordinates. This does not assert completeness in the larger fifteen-dimensional ambient.

For the complete degree-ten system, evaluation onto principal parts of order j is everywhere surjective for 0<=j<=10: locally a length-(j+1) jet is supplied by degree-ten sections, or equivalently by the universal complete-system exact sequence (7) with eighteen replaced by ten. Dualizing gives an everywhere subbundle injection into R11 O. The universal principal-parts identity from PR1199 identifies its source as

    P^j(O(10))*=Sym^j W(j-10).

This proves (1). The complete system's consecutive forward osculating steps have full coherent image, with no intrinsic ramification. At order ten the jet bundle is the entire R11 O; no assertion of rank j+1 is made for larger orders.

## 7. The normal derivative has reduced D12 zeros but the intrinsic tangent does not vanish

Twist the second inclusion in (8) by ten. It gives

    H0(B8(10))^G subset (Sym9 W tensor W)^G.

The Clebsch-Gordan identity and (4) show

    Sym9 W tensor W=Sym10 W+Sym8 W,
    Hom_G(O(-10),B8)=H0(B8(10))^G=0.               (17)

Only equivariant Hom vanishes here; no vanishing of ordinary Hom(O(-10),B8) is claimed or needed.

If beta_(B7) restricted to the equivariant line L10 were zero, its map O(-10)->B7 would factor equivariantly through the exact kernel B8 in (5), contradicting (17). Thus the restriction is a nonzero equivariant line map

    beta_(B7)|L10:O(-10)->O(2).

Its section belongs to H0(O(12))^G=C f12, so it is a nonzero scalar multiple of f12 and has zero divisor exactly D12. In particular every zero is simple.

The intrinsic derivative beta_(L10) in R11 O, and hence in V18* O, is everywhere nonzero by Section 6. Its composition with the natural quotient from the ambient modulo L10 to the ambient modulo B7 equals beta_(B7)|L10. This is naturality of the second fundamental form for nested actual subbundles; it differentiates only actual local sections in a constant ambient.

Therefore vanishing of the latter map at q means that the nonzero intrinsic tangent class lies in (B7/L10)(q) tensor Omega_X^1(q), rather than that the tangent vanishes. Since L10(q) already lies in B7(q), this is exactly the fiber inclusion (3). This proves the normal-incidence interpretation and distinguishes it from intrinsic ramification without assigning any derivative to a quotient.

## 8. Contribution and exact stopping point

The actual seventh-annihilator comparison canonically produces a degree-ten line. Its pairing with the original scalar curve is forced by eighth-order diagonal contact and one invariant multiplicity. A universal second-order differential-equation bound, together with the absence of small subrepresentations in Sym10 W, proves that this line has a complete eleven-dimensional coefficient system. Its full intrinsic osculation is therefore independent of the reduced twelve-point zeros of its normal derivative through B7.

The new conclusion concerns the canonical auxiliary line and its incidence with the actual original annihilator. It does not promote original tenth jets, choose between e9=0 and e9=12, determine the separate local defect delta, identify either with the original t=0, resolve any retained F18 or extension alternative, or prove realization, algebraicity, or a whole-branch/profile exclusion. The verifier checks only exact complete-source pins, fixed small characters, universal degree bookkeeping, and the formal differential identity (14); it is not an evaluation of the actual maps or a substitute for this geometric proof.
