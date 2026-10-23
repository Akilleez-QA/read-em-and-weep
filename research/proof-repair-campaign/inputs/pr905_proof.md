# A high-only D block excludes the source127 a-c-f-f edge

## Result and scope

The entire original source

    G3.11.cce6e3ba4eeb, source_index127,
    (1,0,1,0,0,2,0,0),
    E=2D O(-2)+Wp O(-3)+V O(-4)+2O(-8),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6), original defect zero

is impossible. This is a whole-source exclusion, not a whole-label exclusion or a necessary-pair count. It does not use any unpublished cubic-block reduction or assert anything about the separate c-d-f abstract family.

The new ingredient is the unique kernel of a forced high-only D(-2) subblock. Its complete internal-image alternatives leave either a constant seven-space or a linear block with a constant A summand. Each captures the saturated high quotient and traps a negative Wp(-3) subsystem. In the latter case the contradiction uses its actual coefficient span, not a horizontal interpretation of an abstract splitting.

No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, models, scans or large computation are used. The only checks are fixed abstract characters and exact original source identity.

## 1. Original actual input and derivative images

The four original inputs are pinned at db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

They are the actual-presentation note, strict-top theorem and two original catalogs; the manifest records all exact URLs and Git blob hashes. They give a saturated full-span E in H O, with

    H=2A+2V+2P+2D, rank E=17, degree E=-54,
    Q=H O/E, H0(E)=0, H0(E^-(2))=0,
    A2=E^+/E=O(-6)+O(4)+L, L=O(18) saturated in Q.  (1)

Work over C with binary icosahedral G. Its defining representation is W, with A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; Wp,V,P are the other irreducibles of dimensions2,3,4. All irreducibles are self-dual and G has no nontrivial line characters. Every nonempty invariant effective divisor has degree at least twelve.

We use actual image sheaves throughout. If the internal derivative image J is saturated in (E/F)(-2) and the external image L0 is saturated in Q(-2), then the full derivative image I in (H O/F)(-2) is saturated. Indeed the quotient by I is an extension of the two locally free quotients by J and L0. Thus the raw first span M is already saturated and has exact sequences

    0 -> J -> I -> L0 ->0,
    0 -> F -> M -> I(2) ->0.                    (2)

For a quadratic F=U O(-2), the raw first span is the image of U W O(-1). Differentiation produces the first polars and Euler's identity includes the values. It is therefore generated after twist one. As a subbundle of a constant bundle, M has only degrees zero and minus one. Its degree-zero coefficient is an actual constant subspace.

## 2. Strict-top forces a high-only D subblock with no divisor

The twist-two sections of E are exactly 2D. By strict-top they inject into

    H0(A_q(2))=Sym4 W+Sym18 W
               =A+V+2P+2D.                    (3)

On the two D multiplicity spaces this is an isomorphism. Consequently the low O(2) and high O(16) rows on the top 2D are independent. Let F=D O(-2) be the constant multiplicity kernel of the low row. This is an abstract forced kernel construction, not a choice of actual coefficients. Its high row is nonzero and injective on coefficient sections.

That row is a degree-eighteen D covariant. A common divisor has degree at most fourteen, because the five coefficient sections are independent. Among positive invariant degrees in that range only twelve is possible: odd degrees have no invariant and Sym14 W=A+V+P+D has none. A degree-twelve divisor would leave D in Sym6 W=V+P, absent. Hence

    0 -> K -> D O(-2) -> O(16) ->0              (4)

is onto everywhere. Its negative row vanishes by degree and its low row is zero by definition, so (4) is the complete external derivative of F.

## 3. The high-D kernel is unique

Equation (4), strict-top and fixed characters give

    rank K=4, degree K=-26,
    H0(K(2))=0,
    H1(K(2))=A+V+2P,
    chi_G(K(3))=-W-Wp-T.                       (5)

Here Sym18 W=A+V+2P+D and Sym19 W=W+Wp+S+2T. All degrees of K are at most minus three. For a degree-minus-j atom B O(-j), j>=4, the H1 at twist two is B Sym^(j-4) W. The bounds

    dim B<=4, (j-3)dim B<=14

and central parity, together with support in A+V+2P, leave exactly

    atom          H1 at twist2       H1 at twist3
    A(-4)              A                    0
    V(-4)              V                    0
    P(-4)              P                    0
    Wp(-5)             P                   Wp
    O(-6)              A                    W
    O(-10)             V+P                  T. (6)

For explicit exhaustiveness, at j=5 the W and S coefficients introduce a trivial or D constituent, leaving only Wp. At j=6 the nonscalar even coefficients introduce a trivial or D constituent, leaving only the scalar. At j=7 the W and Wp products introduce D; at j=8 the scalar itself gives D. At j=9 both possible odd two-spaces again introduce D. After j=10 odd degrees exceed the dimension bound, while the possible scalar degrees12,14,16 respectively introduce D, D, and a trivial constituent. Larger degrees exceed the bound. Degree-minus-three atoms contribute only nonnegative coefficients to chi(K(3)).

The negative T in (5) forces one O(-10); it consumes the sole V and one P. The negative W forces one O(-6), consuming the sole A. The remaining P forces Wp(-5), which supplies the negative Wp. These three atoms already fill rank four, leaving no degree-minus-three atom. Thus the exact unique kernel is

    K=O(-6)+Wp O(-5)+O(-10).                    (7)

Its twist-one character also agrees with the original exact sequence:

    chi_G(K(1))=-Sym17 W=-Wp-S-2T.

No actual map or source instance is enumerated in this finite support argument.

## 4. Complete internal images and the two surviving first spans

The internal target of (7) is

    (E/F)(-2)=D O(-4)+Wp O(-5)+V O(-6)+2O(-10).

The O(-6) term has no map to any target. The Wp(-5) term maps only to the equal-degree Wp(-5) row. The O(-10) term maps only to the two scalar rows. Indeed D is absent from Sym6 W, Wp from Sym5 W=T, and V from Sym4 W=D. The Wp-to-D map vanishes because D W=S+T.

Each nonzero equal-degree row is saturated, and the two targets are separate direct summands. Consequently the exact possible internal images are

    J=0, Wp O(-5), O(-10), Wp O(-5)+O(-10).     (8)

Here O(-10) denotes any nonzero scalar multiplicity line, with no coefficient selected. Since the external O(16) is saturated, (2) applies. The first two cases in (8) give deg M=8 or2 and are impossible in a constant bundle. The remaining cases give exactly

    J=O(-10): M=(A+P) O;
    J=Wp(-5)+O(-10): M=A O+T O(-1).             (9)

For completeness, the first case has rank7, degree0 and chi(M)=A+P. The second has rank9, degree-6 and chi(M)=A, while chi(M(1))=W+S+T. Since A W=W+S, its linear coefficient is T. These are actual constant and linear subbundles, not merely virtual characters.

## 5. The constant seven-space alternative is impossible

Suppose M=(A+P) O. Its image in Q is the saturated L. Thus for N=E intersect M,

    N/F=O(-8), rank N=6, degree N=-18.

The quotient N/F is exactly a scalar multiplicity line in the original 2O(-8), as seen in the complete internal-image list. Therefore constant projection by M gives a saturated actual bundle

    E/N=D O(-2)+Wp O(-3)+V O(-4)+O(-8)
          subset (H/M) O,

with derivative image O(2)+O(-8). The high image has been removed coherently, since M/N=L is saturated in Q.

The Wp O(-3) summand now has zero external derivative: Wp is absent from Sym5 W=T, and the negative target is too low. Its internal target is D(-4)+V(-6)+O(-10), also too low. It is therefore preserved by the trivial connection. Being a saturated negative subbundle, it cannot be horizontal: a generic constant subspace extends as the constant saturated bundle on P1. This contradiction excludes the first alternative in (9).

## 6. The constant A in the remaining first span captures the high quotient

Now let M=A O+T O(-1). The constant A is canonical as H0(M). It is contained in E^+, and its maps to the lower rows of (1) vanish: A is absent from Sym4 W=D, and the negative target is too low. Its map to L is nonzero, or it would be a constant subspace of E, contrary to H0(E)=0.

This degree-eighteen A covariant is onto. Its three independent coefficient sections bound any common divisor by degree sixteen. The only possible invariant positive degree in that range is twelve, since Sym14 W and Sym16 W have no invariants and odd degrees are excluded by the center. A degree-twelve divisor would leave A in Sym6 W=V+P, absent. Hence

    A O -> L=O(18) is onto,
    N_A=E intersect A O has rank2, degree-18.    (10)

In particular the constant A, not just all M, captures the saturated high quotient. Projection by A gives a saturated actual E'=E/N_A in (H/A) O, with derivative image O(2)+O(-8).

Let N=E intersect M. The exact internal images show

    N/F=Wp O(-3)+O(-8),
    E/N=D O(-2)+V O(-4)+O(-8).                 (11)

The first row is the entire original Wp(-3) summand and a scalar multiplicity line in 2O(-8). This follows from the preimage of the internal image inside E/F; there are no additional channels. Since A already maps onto the image L of M, the whole M is contained in E+A as a coherent sheaf. Its quotient by A is therefore an actual saturated linear subbundle of E', with

    T O(-1)=M/A subset E',
    E'/T O(-1)=D O(-2)+V O(-4)+O(-8).           (12)

## 7. The Wp cubic block cannot remain inside that linear bundle

The projection of F=D(-2) to T(-1) is nonzero, because F has rank five and cannot lie in A of rank three. Its unique linear map is the universal multiplication by the formal line l, D O(-2)->T O(-1); it is injective everywhere. Differentiating F stays in M=F^+, so the derivative of the projected T(-1) kills this D(-2).

For a linear inclusion T(-1) in a constant bundle, the derivative kernel is the coefficient kernel of T W->C_T, twisted by -2. Since

    T W=V+P+D,

that kernel contains D, and its constant span C_T is a quotient of V+P. It has dimension at least seven: a saturated negative rank-six linear bundle cannot span only six constants. Hence

    C_T=V+P.                                   (13)

Write R=Wp O(-3) for the original cubic summand. By (11) it lies in M. It has zero map to the constant A summand, since Hom_G(Wp,A Sym3 W)=0 and A Sym3 W=W+S+T. Thus its constant projection by A is still an injected R inside T(-1). Its constant coefficient span is both a quotient of

    Wp Sym3 W=V+D

and a subrepresentation of (13). It is therefore exactly V, of dimension three. The actual saturated first span of this rank-two R in the constant V is all V: a nonconstant hyperplane family in a three-space has generic first span three, and saturation supplies the entire constant three-space.

On the other hand, R has zero external derivative in E', since its original only possible external row was the high row, removed by (10). By (12), its derivative toward the quotient E'/T(-1), twisted by -2, is a map

    Wp O(-3) -> D O(-4)+V O(-6)+O(-10),

which is zero by degree. Therefore all derivatives of R stay inside T(-1) as actual sheaves. Its saturated first span V O would be contained in that saturated linear bundle, contradicting H0(T O(-1))=0.

This excludes the last alternative in (9), completing the whole a-c-f-f source exclusion. The argument retained every possible kernel internal image and used the actual saturated high quotient before projecting; no splitting was assumed horizontal.
