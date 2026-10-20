> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# A conditional rank-eight pencil discriminant of degree sixty

## Result and scope

Work over C on X=P(V)=P^4, with L=O(-1), U=(V tensor O)/L, and det U=O(1) as an ordinary line bundle. Retain the existing N-equivariant quadratic map

    Q: L tensor Sym^2 U -> C,
    C=(J tensor O)/A,  A=L^2 tensor U.

Assume only the surviving conditional branch: generic rank Q=8, det F=O(-6), and zero divisorial saturation defect d=0. Thus the saturation I of im Q has det I=O(1), and det(im Q)=det I. The additional established numbers c2(F)=19 and c2(R)=17 are compatible background but are not needed here.

There is a canonically constructed discriminant section, up to the fixed nonzero scalar normalization of the classical discriminant,

    Delta in H^0(X, (det K*)^12 tensor (det U)^12)
          = H^0(X,O(60)),
    K=(ker Q)(1),  rank K=2,  det K=O(-4).

It is equivariant for the natural N-linearization. In particular its zero divisor is N-invariant. Exactly one of the following holds:

1. Delta is identically zero. The generic determinant quartic is identically zero or has a multiple geometric root. No regular-pencil hypothesis follows.
2. Delta is nonzero. Its zero scheme is a nonempty effective Cartier divisor of degree sixty. On the genuine pencil locus its support is the locus where the determinant quartic has a multiple root, together with the possibility that the whole quartic is zero. On the genuine-pencil open Xp off that divisor, the four singular pencil members form a finite étale cover of degree four.

This is a conditional geometric consequence, not an exclusion of rank eight or a determination of the actual generic rank.

## 1. The rank-two reflexive sheaf

The source E=L tensor Sym^2 U has rank ten and determinant O(-5): for a rank-four bundle, det(Sym^2 U)=(det U)^5. Since c1(im Q)=c1(I)=1, the kernel KQ satisfies

    rank KQ=2,  det KQ=det E tensor det(im Q)^(-1)=O(-6).

Consequently K=KQ tensor L* has determinant O(-4), and the kernel inclusion gives a morphism

    j: K -> Sym^2 U.

The sheaf KQ is reflexive. For completeness, im Q is torsion-free, being a subsheaf of the bundle C. At a point of local dimension at least two, the depth lemma applied to

    0 -> KQ -> E -> im Q -> 0

gives depth KQ at least two. At local dimension one it is free, and it is torsion-free everywhere. This is the S2 criterion for reflexivity on smooth X. Twisting preserves reflexivity.

Let X0 be the locally free locus of K. A reflexive sheaf on a smooth variety is locally free in codimension at most two, so codim(X minus X0)>=3. The locus X0 is N-invariant. On X0, j is a morphism of bundles. It need not be a subbundle inclusion at every point; that stronger statement is not assumed.

There is, however, an N-invariant open Xp contained in X0, containing every codimension-one point, on which j is a subbundle inclusion and Q has rank eight. Indeed at a codimension-one point the saturated I is a direct summand of C over a discrete valuation ring, and d=0 says im Q=I there. Hence E -> I is a surjection of free modules, with rank-two kernel. Removing the corresponding closed failure loci yields Xp. On Xp the fiber P(K_x) really is a projective line of distinct symmetric tensors in Sym^2 U_x. Possible codimension-two failures do not change any divisorial conclusion below.

## 2. The determinant binary quartic

A symmetric tensor q in Sym^2 U_x determines a symmetric linear map

    q#: U_x* -> U_x.

Its determinant belongs to

    Hom(det U_x*,det U_x)=(det U_x)^2.

The determinant is a homogeneous polynomial of degree four in q. Restricting it along j on X0 therefore produces the binary quartic

    f in H^0(X0, Sym^4 K* tensor M),  M=(det U)^2.

Equivalently, using the convention that P(K) parametrizes lines in K, it is a section of O_(P(K))(4) tensor pi* M. The coefficient construction is polynomial, so it is valid even where j fails fiberwise injectivity. Neither a nonsingular member nor a nonzero determinant polynomial is needed to define f.

At a point of Xp where f_x is nonzero, its zeros, counted with multiplicity, are precisely the singular members of that pencil. If f_x is identically zero, every member is singular, and one must not describe this as an ordinary four-point root scheme.

## 3. The discriminant line and its weights

For a two-dimensional vector space W and a line M, the discriminant of a degree-n binary form in Sym^n W* tensor M takes values in

    (det W*)^(n(n-1)) tensor M^(2n-2).

One way to verify both weights is to split a form formally as a product of n linear factors. Its discriminant is, up to scalar, the product over i<j of the squares of the wedges of those factors. There are n(n-1)/2 pairs, each wedge lies in det W*, and each square contributes exponent two. Rescaling the whole form multiplies the discriminant by the (2n-2)-th power. The resulting symmetric polynomial expression descends from the splitting presentation and extends polynomially to all forms, including the zero form.

For n=4 this gives

    Delta0=Disc(f)
       in H^0(X0,(det K*)^12 tensor M^6)
       = H^0(X0,(det K*)^12 tensor (det U)^12).

Thus its underlying line bundle is

    O(4*12+1*12)=O(60).

This calculation uses contravariant symmetric tensors in Sym^2 U, not quadratic forms in Sym^2 U*. Confusing these would reverse the det U contribution.

Over an algebraically closed field of characteristic zero, a nonzero binary quartic has nonzero discriminant exactly when its four projective roots are distinct. The zero quartic has zero discriminant as well. In particular the construction does not silently exclude singular pencils whose determinant vanishes identically.

## 4. Global extension and equivariance

For the reflexive rank-two sheaf K, det K=(exterior^2 K)** is an invertible sheaf on X. Hence the discriminant line

    H=(det K*)^12 tensor (det U)^12

is defined globally. Since X is normal and X minus X0 has codimension at least three (codimension two would already suffice), restriction gives an isomorphism

    H^0(X,H) -> H^0(X0,H|X0).

This follows by trivializing H and applying the extension theorem for regular functions on a normal variety across codimension at least two. Accordingly Delta0 extends uniquely to a global section Delta. No assertion about symmetric powers of K* being reflexive is required: only the discriminant line is extended.

All ingredients, including Q, its kernel, twisting, determinant, and the classical discriminant polynomial law, are natural for bundle isomorphisms. They therefore commute with N. The section Delta0 is invariant in its naturally linearized line bundle, and uniqueness of extension makes Delta invariant in that same sense globally.

An arbitrary ordinary-bundle identification H≅O(60) may differ from a preferred standard N-linearization by a character. Accordingly the homogeneous degree-sixty polynomial representing Delta may be a semi-invariant rather than an invariant under that choice. Its zero scheme is N-invariant without any such choice. Degree sixty also satisfies the known divisibility-by-five requirement for an N-invariant effective divisor; no contradiction results from that requirement.

## 5. The dichotomy and its precise divisor interpretation

If Delta=0, its value at the generic point is zero. Over an algebraic closure of C(X), either f is the zero polynomial or f has a repeated root. These are logically separate possibilities; no choice between them is made.

If Delta is nonzero, its zero scheme D is an effective Cartier divisor because X is integral and smooth. Its divisor class is 60h, hence its degree is sixty. It cannot be empty: a nowhere-vanishing section would trivialize O(60), contrary to Pic(X)=Z[O(1)]. Its scheme multiplicities are discriminant multiplicities, not necessarily one.

Every divisorial generic point belongs to Xp. Therefore D is exactly the divisor obtained by closing the codimension-one discriminant locus of genuine pencils. At such a point a nonzero quartic has a multiple singular member precisely when Delta vanishes. If the quartic itself is zero there, the entire pencil is singular and it is also included in D. It would be unjustified to assume the quartic stays nonzero along every component of D, or to assert that every component generically corresponds to exactly one ordinary double root.

Since X minus X0 has codimension at least three, D necessarily meets X0. Thus even allowing the reflexive singularities of K, it is impossible for the determinant pencils to have four distinct roots at every point of X0. In the nonzero branch a genuine divisorial degeneration must occur.

## 6. The four-sheeted root cover on the good open set

In the nonzero branch set B=Xp minus Supp(D). This is a nonempty N-invariant open set. Let

    Z={f=0} subset P(K|B).

Then Z -> B is finite étale of degree four. Indeed each geometric fiber consists of exactly four reduced points, so the proper map is quasi-finite and hence finite. More explicitly, near any base point choose a point of the fiber projective line that is not a root and shrink the base so this remains true. In the resulting affine coordinate all roots are cut out by a monic degree-four polynomial. Its discriminant is invertible, so the root algebra is finite free of rank four and its derivative is invertible in that algebra. This proves étaleness directly.

Every singular member above B has corank exactly one. The determinant has zero differential at a symmetric map of corank at least two, since all its size-three cofactors vanish. Such a member would therefore give a multiple root on the pencil line, contrary to Delta being invertible.

Equivalently, over the generic field C(X) the singular members define a separable algebra of degree four. Its geometric monodromy is a subgroup of S4. The cover need not be connected, and neither transitivity, a rational root, complete splitting, nor full S4 monodromy has been established. The construction and this cover are N-equivariant. The degree-sixty divisor alone gives no splitting-field or monodromy determination.

## Sources and evidence boundary

Bundle and determinant conventions: ../rank-four-global-determinant/PROOF.md. Fiber-rank cautions: historical source rank-ten-fitting-strata/PROOF.md (ancillary to the present rank-eight assembly). Conditional rank-eight Chern background: ../full-support-equivariant-chern-congruences/PROOF.md, together with the stated surviving branch hypotheses. The distinction between conditional quadratic rank and actual generic local thickness is consistent with ../rank-one-even-normal-form/PROOF.md.

Only abstract bundle algebra, reflexive-sheaf extension, polynomial determinant/discriminant identities, and finite étale root-cover arguments were used. No actual source, operation, matrix, input, rank instance, jet, or residue was evaluated. The only write is this local proof deliverable.
