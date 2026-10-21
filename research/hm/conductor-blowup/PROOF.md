# The conductor blowup, embedded resolution, and removal of the determinantal node defect

Status: structural mathematical proof; independent review recorded in REVIEW.md. Not formally checked. Work over C. No selected actual HM/source coefficients, matrices, point evaluations, numerical rank tests, numerical search, or large computation are used. The local coordinates below describe the universal transverse two-branch singularity, not a chosen source instance.

## 1. Pinned inputs and statement

Let P=C[x0,...,x4]. Let S⊂P4 be the actual integral primary surface, ν:X→S its finite normalization, and Z⊂S its thirty reduced nonnormal double points. Write script I=I_(S/P4), script J=I_(Z/P4), and script c=I_(Z/S). Let W=ν^(-1)(Z) with its reduced structure.

The inputs are:

1. PR574, commit 3c92fdc469f6870520e7a9d905b5ab9199a5bf37, Sections 1–2: X is smooth, S is smooth off Z, W consists of sixty distinct points, and at each z∈Z the completed ambient and surface local rings are

   Q=C[[u1,u2,v1,v2]], n=(u1,u2,v1,v2),
   A0=Q/K, K=(u_i v_j:1≤i,j≤2),
   A0=C[[u1,u2]] ×_C C[[v1,v2]].                         (1)

   Its normalization is B0=C[[u1,u2]]⊕C[[v1,v2]], and the conductor is m_u⊕m_v. Globally script c·O_X=I_(W/X), and script c is an ideal of both O_S and ν_*O_X. The same source gives H=ν*O_S(1), H²=15.

2. PR599, commit f8154d28e5c56ca96dc4e41cdf3097aaeba3b1a4, Sections 3 and 5: if L is the actual linear primary syzygy map, then

   I_9(L)=I_Z I_S.

   Consequently D=Proj(P/I_9(L)) has reduction S and fits into

   0→E→O_D→O_S→0,  E=script I/(script J script I),
   E²=0, script J E=0, length(E)=120.                    (2)

3. PR600, commit 90f29113ae2d3a53cd8816ad7d32c96634be5b4a, Sections 2–3: the last cubic column g of the actual primary resolution generates I_Z as a homogeneous ideal, and its image in P/I_S is exactly the homogeneous conductor I_Z/I_S. Thus the ten cubics generate script c(3).

Exact source links:

- https://github.com/Akilleez-QA/read-em-and-weep/blob/3c92fdc469f6870520e7a9d905b5ab9199a5bf37/research/hm/primary-conductor/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/f8154d28e5c56ca96dc4e41cdf3097aaeba3b1a4/research/hm/linear-adjugate/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/90f29113ae2d3a53cd8816ad7d32c96634be5b4a/research/hm/primary-syzygy-geometry/PROOF.md

All blowups below use the Rees algebra ⊕_(n≥0) a^n t^n, not the symmetric algebra. A sheaf ideal extended to another scheme means its image ideal. In particular script c·O_X is not asserted invertible before blowing up.

**Theorem.** There are canonical isomorphisms over S

   Y:=Bl_(script c) S ≅ Bl_W X ≅ Bl_(script J·O_D) D.     (3)

The last scheme's map to D factors through the closed reduced subscheme S. The surface Y is smooth. Over each z∈Z its scheme-theoretic fiber is the disjoint union of two reduced copies of P1, one for each point of W over z. The strict transform of S in Bl_Z P4 is canonically Y; its two exceptional curves at z are skew lines in the ambient exceptional P3. The same Y is the strict transform of D. None of these assertions identifies a total transform with a strict transform.

## 2. A conductor-Rees lemma with an actual chart proof

Let A⊂B be a finite birational extension of Noetherian domains with common fraction field F. Let a⊂A be a nonzero ideal that is also a B-ideal. Thus aB=a as subsets of F. For every n≥1, its nth powers computed over A and over B agree: a product with a B-coefficient absorbs that coefficient into one of its factors in a. Consequently

   R_A(a)=A⊕a t⊕a²t²⊕...,
   R_B(a)=B⊕a t⊕a²t²⊕....                               (4)

These graded rings need not be equal: their degree-zero pieces differ. They nevertheless have canonically identical Proj.

Choose A-generators a1,...,ar of a. They also generate a as a B-ideal. For any nonzero ai, the standard affine charts are, inside F,

   (R_A(a)[(ai t)^(-1)])_0=A[a/ai],
   (R_B(a)[(ai t)^(-1)])_0=B[a/ai].

For every b∈B, the element bai lies in a, so b=(bai)/ai belongs to A[a/ai]. Thus

                    A[a/ai]=B[a/ai].                    (5)

The inclusions into F make these equalities compatible on chart intersections. The charts cover both Proj, giving an isomorphism over Spec A

              Bl_a Spec A ≅ Bl_a Spec B.                 (6)

This is not an assertion that Proj is always unchanged by an arbitrary degree-zero modification. The B-stability of a is what supplies every missing b as a degree-zero fraction on every chart.

Apply the lemma on affine open subsets of S, using the finite normalization and its conductor. Restriction to a smaller open preserves the chart identifications, so they glue globally. Input 1 identifies script c·O_X=I_W. Therefore

                    Bl_(script c) S ≅ Bl_W X.             (7)

For completeness, the equality of the pulled ideal with I_W is scheme-theoretic: on the completed normalization of (1) the extended ideal is m_u⊕m_v, the radical ideal of the two origins. Equality of these finite ideal modules descends by faithful flatness of completion; away from W both ideals are the unit ideal.

The map in (7) is also the map supplied by the blowup universal property: on Bl_W X the image of script c is the invertible exceptional ideal. Equation (5) proves this map is an isomorphism, rather than merely a proper birational morphism. In the other direction the same charts include B, giving the factorization Y→X→S. No appeal to generic smoothness or to an unproved algebraization of a formal isomorphism occurs here.

## 3. Universal local charts and the exceptional curves

We check the asserted geometry directly in (1). Powers of the maximal ideal of A0 are m_u^n⊕m_v^n for n≥1. A standard blowup chart D_+(u1 t) has degree-zero ring given by the image of A0[m_(A0)/u1] in A0[1/u1]. In that localization v1=v2=0. Hence the chart is exactly

             C[[u1,u2]][a]/(u2-u1 a),  a=u2/u1.           (8)

This presentation is injective into C[[u1,u2]][1/u1]: if u1 f=(u2-u1a)h in the polynomial ring, reduction modulo u1 forces h divisible by u1 because u2 is a nonzerodivisor in C[[u2]][a]. Thus the displayed quotient has no u1-torsion, which verifies the image presentation rather than leaving an extra symmetric-algebra component.

The u2 chart is the other usual chart of the blowup of the smooth u-plane. The v1 and v2 charts similarly give the blowup of the smooth v-plane. Any u-chart is disjoint from any v-chart, since (u_i t)(v_j t)=0 in the Rees algebra, so the corresponding simultaneous homogeneous localization is zero. Thus the completed-base blowup is precisely the disjoint union of these two plane blowups, not two blowups still identified along their exceptional curves.

The ring in (8) is not silently replaced by C[[u1]][a]; unrestricted formal substitution would not justify that equality. At a closed exceptional point a=α its completed local ring is

                       C[[u1,a−α]],                      (9)

because u2=u1a eliminates u2 in the completed presentation. The exceptional ideal there is (u1), with reduced local quotient C[[a−α]]. The analogous charts show that each branch contributes a reduced P1 with its usual normal bundle O_(P1)(−1).

Equivalently, the whole scheme-theoretic fiber over the node is

   Proj(gr_(m_(A0)) A0)
    =Proj(C[U1,U2,V1,V2]/(U_i V_j))
    =P1 ⊔ P1.                                            (10)

There is no embedded structure in this fiber: the displayed homogeneous ideal is the intersection (U1,U2)∩(V1,V2), and the two projective linear subspaces are disjoint.

Globally, (7) identifies Y with the blowup of the smooth X at sixty distinct reduced points. This blowup is smooth: outside those points it is X, and at each point regular parameters give the same two regular surface charts as above (or their completed local rings (9)). Regularity is detected by completion for these Noetherian local rings. Over C a regular finite-type scheme is smooth. The sixty exceptional curves are pairwise disjoint and have self-intersection −1. The divisor

                       E_Y=Σ_(w∈W) E_w

is reduced Cartier and script c·O_Y=O_Y(−E_Y). Smoothness here uses the actual smooth normalization input, not a claim that an arbitrary conductor blowup must be smooth.

## 4. The ambient strict transform and its skew lines

Let π:M=Bl_Z P4→P4. The quotient O_(P4)→O_S induces a surjective map of Rees algebras

           ⊕ script J^n → ⊕ (script J·O_S)^n.

It yields a closed immersion Y→M over P4. On P4\Z this is the original S\Z. Since S is integral, its Rees algebra is a domain on each affine open, so Y is integral. The open Y\E_Y is dense and scheme-theoretically dense in Y. Its scheme-theoretic closure in M is therefore exactly Y. This proves the strict-transform statement, including the scheme structure.

For the local embedded picture, blow up the origin of Spec Q. The u1-chart has coordinate ratios

              a=u2/u1, b=v1/u1, c=v2/u1.

The extended surface ideal is

                       K·O_M=u1²(b,c).                   (11)

Saturating by the exceptional coordinate u1 gives the strict-transform ideal (b,c). Indeed the quotient by (b,c) is the domain in (8), so it has no u1-torsion. At u1=0 this strict transform is the line [U1:U2:0:0] in the exceptional P3. The v-charts give the line [0:0:V1:V2]. These lines have no intersection because their underlying two-dimensional vector subspaces have zero intersection. They are therefore skew, and each has the reduced structure already verified in (10).

Formula (11) also makes the total/strict distinction explicit. The total transform has exceptional multiplicity and is not the smooth strict transform. The corresponding global ideal equality is

             script I·O_M=O_M(−2E_M)·I_(Y/M),             (12)

where E_M is the sum of the thirty ambient exceptional divisors. It holds on the displayed charts and their analogues, and away from E_M both sides are script I. Since blowups commute with flat completion and equality of finite ideal sheaves is faithfully flat local, the universal completed calculations prove this equality for the actual ambient blowup. In particular Y is a smooth codimension-two closed subvariety of the smooth M and hence a regular embedding.

## 5. Blowing up kills a center-annihilated thickening

Here is the general Rees-algebra fact needed to pass from the determinantal scheme D to S. Let B→A=B/T be a surjection of Noetherian rings, let b⊂B be a finite ideal, and set a=bA. Assume

                              bT=0.                       (13)

No square-zero assumption is needed for this lemma. There is a surjective graded homomorphism

                    R_B(b)→R_A(a)

whose degree-n kernel is (T∩b^n)t^n for n≥0, with b^0=B. Denote this kernel by K_R. Every positive-degree element of R_B(b) has coefficient in b, and therefore annihilates K_R by (13):

                          R_B(b)_+ K_R=0.                 (14)

Choose generators b1,...,br of b. On each standard chart D_+(bi t), the element bi t is inverted, while it annihilates K_R. Hence the localized kernel is zero. Localization preserves surjectivity, and taking degree-zero pieces now gives an isomorphism of chart rings. These charts cover the source and their images cover the target; a chart whose image generator is zero is empty on both sides, since the localized quotient and localized source are already isomorphic. Gluing proves the canonical closed immersion is an isomorphism:

                        Bl_a A ≅ Bl_b B.                  (15)

Thus the proof is by actual unit localization. It is not the false claim that an arbitrary nilpotent ideal, or an arbitrary degree-zero kernel, disappears under Proj.

Apply this sheafwise to (2), with T=E and

               b=script J·O_D=script J/(script J script I),
               a=script c=script J/script I.

Then bE=0 by Input 2. Formula (15) gives the last isomorphism in (3). In particular all of the length-120 nilpotent node sheaf disappears on the blowup, not just its support. The resulting morphism to D factors through S because this holds for the canonical isomorphism induced from the surjection to O_S.

Since D and S agree off Z, their scheme-theoretic strict transforms in M are the same closure, namely Y. This can also be checked directly: on the ambient u1-chart, script J pulls back to (u1), so script J script I pulls back to u1³(b,c). Saturation by u1 again gives (b,c). The total determinantal transform is instead

        (script J script I)·O_M=O_M(−3E_M)·I_(Y/M).        (16)

The multiplicities two in (12) and three in (16) are compatible with identical strict transforms and with the isomorphism of their intrinsic blowups; they must not be erased when discussing total transforms.

## 6. A small next consequence: the resolved cubic system

Let b:Y=Bl_W X→X be the morphism in (7). The ten conductor cubics from Input 3 pull back to sections vanishing along E_Y. Dividing by this fixed exceptional factor gives a globally generated line bundle

                   M_c=b*O_X(3H)⊗O_Y(−E_Y).              (17)

Global generation follows directly by pulling back the surjection O_S^10→script c(3) and then taking the image ideal script c·O_Y=O_Y(−E_Y). Thus the conductor column defines a morphism Y→P9 with no residual basepoints. This assertion is about the actual column, not an arbitrary ten-dimensional space with a matching Hilbert function.

Using H²=15, b*H·E_w=0, E_w²=−1, and disjointness of the sixty exceptional curves gives

                         c1(M_c)²=9·15−60=75.             (18)

A globally generated line bundle pulled back from a point or a curve has self-intersection zero. Therefore this morphism has a surface image and is generically finite onto it. The projection formula gives

                  degree(Y→image)·degree(image)=75.       (19)

No birationality, very ampleness, normality of the image, or specified degree of the morphism follows merely from (18). Those are separate questions about the actual cubic system.

## 7. Contribution and boundary

The conductor recovered from the last primary syzygy now gives a canonical smooth modification of the actual nonnormal primary surface. It factors through its normalization, blows up precisely the sixty preimages of the thirty nodes, and has an explicit embedded interpretation in the blowup of P4. The universal Rees-kernel argument extends the construction to the nonreduced 9-minor scheme and proves that its entire square-zero node defect is removed. The total-transform multiplicities and the resolved cubic system are further exact consequences.

All identifications are scheme-theoretic. Formal coordinates are used only for the universal local calculations, and the main global isomorphism is proved directly on algebraic Rees charts. These results use the actual input normalization, conductor, and determinantal equality; they do not follow from dimensions or Hilbert series alone. They neither settle the separate primitive-four/full-adjoint gate nor prove prescribed-source membership, a selected connecting-map nonvanishing, higher lifting, or algebraicity.
