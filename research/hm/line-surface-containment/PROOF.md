# All twenty-five rank-nine lines lie in the smooth surface locus

## Statement and pinned inputs

Work over C. Let e:E=3Q(-1) -> 10O on P4 be the actual primary Euler-quotient evaluation, and D=D_9(e) its maximal-minor scheme. The following inputs concern this scheme, not the fixed-beta surfaces X_B or the primary-bad eightfold of quadratic parameters.

- PR555, ff5a3164337016e96e3a29a9ad37891130a66e29: dim D<=2.
- PR562, 86b643fe2adecbd321d1c8f98be84fe2082bcd10: D contains twenty-five pairwise disjoint lines L, all everywhere rank nine, forming a transitive orbit under projective Heisenberg translations preserving D.
- PR563, 56c3c4c37bd51fc710eec4b80662c5506f357f8f: dim T_xD=2 at every point of these lines; the intrinsic normal derivative has kernel M=O_L(-5), and its full tangent kernel is O_L(2) direct-sum O_L(-5).
- PR564, a230d0c03c2ed0927643275cf50a9babc9d65a07: each L admits an equivariant closed embedding S_6 -> D, where S_n=Spec_L(direct-sum_{j=0}^n M^{-j}) with truncated multiplication. Its induced first normal derivative identifies M with the preceding normal kernel.

**Theorem.** Every one of the twenty-five lines is contained in a two-dimensional irreducible component of D. The scheme D is smooth of dimension two at every point of their union. On its smooth neighborhood, each line has normal bundle O(-5), self-intersection -5, and canonical degree 3. Each of the constructed equivariant embeddings S_6 -> D extends compatibly through every finite order, and induces an equivariant isomorphism of formal neighborhoods with the zero section of Tot(O(-5)). No analytic convergence or algebraic neighborhood isomorphism is asserted.

## 1. Isolated degeneracy points have total length at most 105

Fix any hyperplane H=P3. Put G=E*|H=3Omega_P4(2)|H, a globally generated rank-twelve bundle. Global generation follows from the standard exterior-Euler presentation: the sections of Omega(2) represented by x_i dx_j-x_j dx_i generate its fiber at every point. Restriction preserves global generation.

Consider the vector space P=H0(H,G)^{10} of morphisms 10O_H -> G. Its evaluation onto Hom(C^10,G_x) is surjective for every x. Consequently the universal rank strata on H times P are smooth over the corresponding ordinary matrix rank strata. The rank-nine stratum has codimension three, while rank at most eight has codimension eight. Generic smoothness and dimension counting show that a general morphism has a reduced zero-dimensional rank-drop scheme, with no rank-at-most-eight points (or potentially an empty degeneracy scheme). The expected-codimension Porteous formula rules out emptiness and computes its length as

integral_H c_3(G) = [h^3](1+h)^15/(1+2h)^3 = 455-630+360-80 = 105.

Let phi_0 be the actual dual evaluation restricted to H. Choose a general phi_1 so that the affine pencil phi_t=phi_0+t(phi_1-phi_0) has generic point in this good open set. Its projective degeneracy family Z subset H times A1 has generic fiber of length 105.

Let p be any isolated point of the special fiber Z_0. At p, take the regular local ring R of H times A1, of dimension four, and let I be the maximal-minor ideal. The ideal (I,t) is maximal-primary because p is isolated in Z_0, so height(I)>=3. The universal determinantal height bound gives height(I)<=3. Thus I has grade three. The Eagon-Northcott theorem gives R/I Cohen-Macaulay of dimension one. Since its quotient by t has dimension zero, t is a parameter and hence a nonzerodivisor. In particular the family is flat at p.

Here is the precise conservation step, which does not presume global flatness of Z. Base-change the projective family to the complete henselian trait Spec C[[t]]. Each isolated special-fiber point is an open-and-closed component of that fiber. The proper henselian decomposition lemma (Stacks Project, Lemma 37.53.9, https://stacks.math.columbia.edu/tag/0CT9) splits off a corresponding open-and-closed proper summand Z_p of the family. Both its special and generic fibers are zero-dimensional, the latter being a subscheme of the length-105 generic fiber. Thus Z_p is proper and quasi-finite, hence finite (https://stacks.math.columbia.edu/tag/02LS). Its local rings over the special point have t a nonzerodivisor by the preceding calculation, so its finite C[[t]]-algebra is torsion-free, hence free. Its rank is exactly length(O_{Z_0,p}). Distinct isolated points yield disjoint summands: an intersection would be proper with empty special fiber, impossible over a local trait. Their generic fibers are therefore disjoint subschemes of the length-105 generic fiber. Therefore

sum_{p isolated in Z_0} length(O_{Z_0,p}) <= 105.        (1)

The proper henselian decomposition used here can equivalently be obtained by lifting the special-fiber idempotents to the proper formal completion and applying formal existence. It does not require flatness on the complementary summand, which can contain the positive-dimensional special-fiber components.

## 2. A hyperplane through the thickened lines gives a contradiction

Assume that no distinguished line lies in a surface component of D. There are finitely many irreducible components of D. Since dim D<=2, each distinguished line is then itself a one-dimensional component, and meets every other component in only finitely many points. Choose H general enough that it contains none of these lines, that each p_L=H intersect L avoids every other component, and that its intersection with L is transverse. Such choices exclude only finitely many proper hyperplane conditions. In particular the twenty-five p_L are distinct isolated points of D intersect H.

The embedding S_6 -> D remains a closed immersion after base change by H. At p_L its completed local ring before slicing is C[[y]][z]/(z^7), with y a parameter on L. The hyperplane equation restricts modulo z to a parameter with nonzero linear coefficient in y. A formal change of y therefore makes the equation y itself. The sliced thickening has local ring C[z]/(z^7), of length seven. Consequently

length(O_{D intersect H,p_L}) >= 7.

Apply (1) to the actual dual evaluation on H. Its determinantal scheme is exactly D intersect H, since formation of minors commutes with base change. We obtain 175=25 times 7 <=105, a contradiction.

Hence at least one distinguished line belongs to a surface component. The translation group preserves D, its components and their dimensions, and acts transitively on the twenty-five lines. Therefore every distinguished line belongs to a surface component.

## 3. Smoothness at every point, not only generic smoothness

For every point x on every distinguished line, a surface component through the whole line gives dim O_{D,x}>=2. The pinned global dimension bound gives equality. PR563 gives embedding dimension dim T_xD=2. The local ring is therefore regular. Over C this says that D is smooth of dimension two at x, including scheme-theoretic reducedness there and uniqueness of the local component. Smoothness is open, so D has a smooth surface neighborhood U of the union of the lines.

The intrinsic normal derivative of PR563 is now the actual normal bundle N_{L/U}=O_L(-5). Thus L^2=-5 on U. Adjunction gives (K_U+L).L=deg K_L=-2, hence K_U.L=3. These are local-neighborhood intersection statements and do not require that all of D be normal or irreducible.

## 4. All finite thickenings and the formal neighborhood

Fix one L and its stabilizer I. Choose an I-invariant smooth neighborhood by intersecting the finitely many translates of a smooth neighborhood. The tangent-normal sequence splits as an ordinary sequence because Ext^1(O(-5),O(2))=H^1(O(7))=0; averaging provides an equivariant splitting. Thus

T_U|L = O(2) direct-sum O(-5).

Start with any of the equivariant S_6 embeddings from PR564. Suppose an equivariant morphism f_{n-1}:S_{n-1}->U has been constructed for n>=7. The square-zero ideal of S_{n-1} in S_n is M^{-n}=O(5n), supported on L. Smoothness of U makes local lifts exist. Their gluing obstruction belongs to

H^1(L,T_U|L tensor M^{-n})
 = H^1(O(5n+2)) direct-sum H^1(O(5n-5)) = 0.

Therefore global lifts exist; the set of lifts is an affine torsor under H^0(T_U|L tensor M^{-n}). The finite group I acts on that affine torsor, and characteristic-zero averaging gives an I-fixed lift. Induction constructs a compatible equivariant sequence through every finite order, extending the chosen S_6.

Its first normal derivative remains an isomorphism onto N_{L/U}. The compatible maps therefore induce a morphism from the formal completion of Tot(M) along its zero section to the formal completion of U along L, identity on L and isomorphism on conormal line bundles. Both completed structure sheaves have associated graded algebra Sym(M^{-1}). The induced graded map is an isomorphism in every degree. Induction on the powers of the ideals, followed by completeness and separatedness, makes the formal morphism an isomorphism. In particular every finite map identifies S_n with the n-th infinitesimal neighborhood of L in U.

The formerly possible order-seven obstruction of PR564 is therefore zero for every chosen equivariant S_6 embedding under discussion: its next lift has just been constructed in D itself. This concerns the normal-thickening deformation problem only. It does not evaluate the distinct original-source or full-adjoint obstruction, establish algebraicity of the original research target, or prove convergence of this formal isomorphism.

## Scope and verification status

The proof uses only structural bundle deformation, expected-grade determinantal commutative algebra, group transitivity, and the already pinned tangent/thickening results. No selected actual source coefficients, numerical matrices, rank experiments, or large computations are used. The auxiliary general morphisms are used only to bound isolated lengths; they are not substituted for the actual evaluation map. The theorem does not imply that D is globally normal, reduced, irreducible, or degree 105.

Public dependency links: https://github.com/Akilleez-QA/read-em-and-weep/pull/555 ; https://github.com/Akilleez-QA/read-em-and-weep/pull/562 ; https://github.com/Akilleez-QA/read-em-and-weep/pull/563 ; https://github.com/Akilleez-QA/read-em-and-weep/pull/564 .
