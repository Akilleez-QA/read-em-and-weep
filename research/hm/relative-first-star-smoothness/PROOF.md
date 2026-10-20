# Relative cohomology and the full first-star forgetful lifting property

## Scope and hypotheses

Work over C. Let Y=(P1)^4, M=O_Y(1,1,1,1), and q:X=C^4→Y be the fixed product of elliptic double covers, with deck group G=(Z/2)^4. Let H be the specified stable rank-two bundle on P4 and F=End H. Assume the pinned presentation and cohomology premises used in PR125 and PR179, in particular H0(F(t))=0 for t<0 and H1(F(t))=0 for t≤−2. These are imported complex-model premises, not new source evaluations.

Let U be the open neighborhood of the coefficient base point in P(H0(Y,M)^5)=P79 where the five sections generate M. Each tuple defines f_u:Y→P4. The ordinary bundle family is E_u=q*f_u*H tensor the fixed line N. Its endomorphism bundle is q*f_u*F. Use the deck-linearized ordinary miniversal atlas of PR312 at commit10822272068aac302e635b963810f300c29eaac8.

All lifting statements are local near the coefficient base point. On projective coefficient space the universal pullback of O(1) includes the parameter-line factor M tensor O_U(1). Every complex fiber still has pullback M, which is all the splitting calculation below uses. For the actual tuple formulas and formal atlas, restrict to an affine coefficient chart and normalize a nonzero coefficient, trivializing that parameter line. No global root or simultaneous splitting over projective U is asserted.

For the first-star consequence assume, separately, Q: the arbitrary-tuple regular first-lift theorem pinned in PR252 at commit92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f. Thus the normalized coefficient atlas carries a regular first-order star lift, with fixed ordered scalar gerbe c=1+epsilon b, for either inherited Poisson branch separately. The source model, determinant normalization and regularity premises of Q remain explicit.

The new conclusion has two steps. First, every relative End cohomology group of this ordinary coefficient family is locally free near the base point and commutes with arbitrary parameter base change. In particular H1 over an Artin base surjects onto H1 over every Artin quotient. Second, this supplies the missing difference-class lifting step: the forgetful functor from ALL first-star structures with this fixed gerbe to marked G-equivariant ordinary deformations is formally smooth, not only the distinguished source-formula atlas. Star structures themselves are not asserted G-equivariant with trivial star parameter. No second-star-order, mixed two-star lifting, or algebraicity conclusion follows.

## 1. Every generating tuple gives a finite flat map

Since f_u*O(1)=M and M is ample, f_u has no positive-dimensional fiber: a positive-dimensional projective fiber would contain a curve, on which the ample M has positive degree while f_u*O(1) has degree zero. Thus f_u is finite onto its image. Its image has dimension four and is closed in P4, hence is P4. Its degree is M^4=24.

Both Y and P4 are smooth of dimension four. The finite map is flat by the local Cohen–Macaulay/regular equal-dimension flatness criterion. Equivalently, a system of parameters in the target pulls back to a system of parameters in each finite source local ring and is a regular sequence. Thus each B_S(u)=f_(u)* L_S is a vector bundle of rank24, where L_S=O_Y(-2 on S,0 elsewhere).

## 2. Pushforward splitting depends only on the subset size

For every integer n, projection formula and Kunneth give

    H^j(P4,B_S(u)(n))=H^j(Y,O(n-2 on S,n elsewhere)).

The right side is independent of u. When 1≤r=|S|≤3, its sole intermediate cohomology in all twists is H^r(B_S(u))=C. It is acyclic at twists1 and−1; for n≥2 only H0 occurs, and for n≤−2 only H4 occurs.

The Euler exterior sequences and H^j(B_S(u)(i))=0 for j>0 and i≥1 lift the unique H^r class to a map Omega^r→B_S(u). Finite duality gives

    B_S(u)^*(-5)=B_(S complement)(u).

Applying the same lift to the complementary subset, then dualizing, gives a retraction up to a nonzero scalar: Serre duality makes its map on H^r nonzero, and End(Omega^r)=C. Consequently

    B_S(u)=Omega^r direct-sum R_S(u).

This is an underlying-bundle splitting, not a canonical, multiplicative or family-equivariant splitting. The remainder has no intermediate cohomology in any twist, so Horrocks splitting gives a sum of line bundles. H0(B_S(u)(1))=0 forces each summand to be O(-a) with a≥2. Applying the same vanishing to the complementary bundle and the displayed duality forces a≤3. Thus R_S(u) is a sum only of O(-2) and O(-3). Its rank and Hilbert polynomial fix their multiplicities uniquely; these are independent of u. No choices of the actual splitting are needed below.

For S empty, all intermediate cohomology of B_empty(u) vanishes. It splits into lines. H0(B_empty(u)(-1))=0 implies a≥0. Its dual twisted by−5 is B_all(u), whose H0 at twist1 is zero; hence a≤3. The Hilbert function (n+1)^4 at n=0,1,2,3 successively gives

    B_empty(u)=O direct-sum O(-1)^11 direct-sum O(-2)^11 direct-sum O(-3).

Finite duality then determines B_all(u)=B_empty(u)^*(-5). The degree24 rank agrees. Thus for every subset S the underlying bundle isomorphism type of B_S(u) is independent of u, even though no simultaneous splitting has been selected.

## 3. Constant fiber cohomology implies arbitrary-base relative cohomology

The fixed double cover has character decomposition q_*O_X=direct-sum_S L_S. Since q and f_u are finite, projection formula gives, in each G-character,

    H^i(X,End E_u)_(chi_S)=H^i(P4,F tensor B_S(u)).

F is fixed, and Section2 gives a fixed isomorphism type for every B_S(u). Hence every dimension h^i(X,End E_u)_(chi_S) is constant on U. This uses neither S4 symmetry of a general tuple nor a multiplicative splitting. In particular the nontrivial singleton contributions and the invariant contribution cannot jump within this coefficient atlas.

Here is an algebraic base-change justification that includes nonreduced Artin bases. Let p:X×U→U. Proper smoothness of p and the vector bundle End E make Rp_*End E a perfect complex. Locally on U represent it by a bounded complex of finite free modules. The ranks of all fiber differentials are constant, by induction from the left end using the fixed ranks of the terms and the constant fiber cohomology dimensions. On an open where a maximal nonzero minor is invertible, Gaussian elimination makes that differential an identity block plus zero. Larger minors vanish identically because they vanish at every closed point of the reduced smooth parameter base U. Splitting off each contractible block successively makes the complex locally a direct sum of finite free cohomology modules with zero differential.

Tensoring this local split complex with any U-algebra therefore computes its cohomology by ordinary tensor product. Proper perfect base change identifies it with the End cohomology of the pulled-back family. Thus every R^i p_*End E is locally free and its formation commutes with arbitrary parameter base change. The same is true character by character using the finite-group idempotents in characteristic zero.

In particular, for any local Artin map Spec A'→U and quotient A'→A,

    H1(X_(A'),End E_(A')) → H1(X_A,End E_A)

is surjective. This is stronger than pointwise constancy of one numerical Ext dimension: the split-perfect-complex argument supplies the nonreduced base-change assertion actually required.

## 4. Lifting an arbitrary first-star object, not only the atlas object

Fix one Poisson branch and epsilon²=0. Work with the fixed scalar gerbe c=1+epsilon b supplied by Q. Objects consist of an ordinary marked G-equivariant deformation together with a first-star c-twisted right-module structure; no G-equivariance is required of the star structure itself. Morphisms reduce to the chosen ordinary equivariant identifications. The target forgets only the star structure.

Let A'→A be an Artin surjection, let E_A' be an ordinary lift, and let T_A be ANY first-star structure over its prescribed ordinary reduction E_A, with the fixed c. Ordinary formal versality of PR312 chooses compatible coefficient classifying maps and ordinary isomorphisms. Pulling back Q and applying the regular star-gauge transport gives a distinguished first-star structure T_A'^0 whose reduction is T_A^0 over the same ordinary transitions as T_A. This step uses Q, not ordinary smoothness alone.

On a common affine refinement write

    T_A=g+epsilon U,    T_A^0=g+epsilon U^0.

Since their ordinary transitions, bidifferential product and scalar b agree, subtracting the first-lift equations gives a homogeneous End(E_A)-valued Cech cocycle

    z_ij=g_ij^{-1}(U_ij-U_ij^0),    delta_row z=0.

By Section3 its H1 class lifts to H1(X_A',End E_A'). Choose a cocycle z' representing a lift on a common affine cover. Its reduction differs from z by a coboundary delta_row w. Sections of End E_A' on the affine opens surject onto the reduced sections because the bundle is locally free and affine cohomology is exact. Lift w to w' and replace z' by z'-delta_row w'. Then z' reduces exactly to z.

Now add the homogeneous correction g'_ij z'_ij to the first coefficient of T_A'^0. Its row cocycle identity ensures the same first-lift equation and same c, and its reduction is the given T_A exactly in these frames. First-star invertibility follows from invertibility of the ordinary transitions. The construction is compatible with the supplied reduction isomorphism, since the ordinary classifying isomorphisms were chosen compatibly and star-gauge transport includes its required bidifferential terms.

This proves the infinitesimal lifting criterion for formal smoothness of this fixed-gerbe forgetful functor. It lifts an arbitrary given first-star difference class, not just a zero difference class. No uniqueness is claimed. First-star structures over fixed ordinary transitions form an H1 torsor modulo epsilon-gauge; the new relative cohomology result is precisely what allows every such class to lift.

## 5. Limits

The target is the specified marked G-equivariant ordinary deformation problem and its miniversal coefficient atlas; the star object need not carry a trivial-parameter G action. The scalar gerbe is fixed, and the ambient first-order star operator is the inherited one. Changing the gerbe, adding algebra-overlap automorphisms, changing the ordinary target category, or lifting beyond epsilon²=0 is not addressed.

The theorem remains conditional on P/D and Q as separately stated. It supplies the extra difference-class lifting argument deliberately left open in the earlier all-background-orders/one-star-order theorem. It does not infer any second-star obstruction vanishing from ordinary unobstructedness, and does not settle the six pure diagonal conditions.

## Verification status

Authored structural proof. No source instance, scalar detector, matrix evaluation or large computation was executed. Independent mathematical review is required before publication, particularly for the relative splitting/base-change argument and the fixed-gerbe groupoid lifting criterion.
