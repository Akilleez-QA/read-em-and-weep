# Sharp connecting ranks on the fixed double conic

## Assumptions and precise result

Work over C, on the same fixed nonsplit ribbon E=2C⊂P², C≅P¹, with J=I(C/E)=O_C(−4), J²=0. Degrees on C are P¹ degrees; plane twists are labelled. Fix even d≥4, determinant D=O_E(−2 plane), and the restricted rank-two splitting

    F_C=O_C(a)⊕O_C(b),  a=(d−4)/2, b=(−d−4)/2.

For B=End₀(F), set G=B⊗O_E(−2 plane). Its boundary is

    ε:H⁰(O_C(d−4)) → H¹(O_C(d−8)⊕O_C(−8)⊕O_C(−d−8)).

The target order is positive root, Cartan, negative root. Every determinant-correct lift F to E is included; we make no assertion that such a lift extends to an HM bundle or even to P².

Results:

1. For d≥8, after choosing the reference splitting, ε is, up to a fixed nonzero scalar/sign, the binary catalecticant attached to e∈H¹(O_C(−d−4))=H⁰(O_C(d+2))*. Specifically, ⟨ε(s),t⟩=±⟨e,st⟩ for t∈H⁰(O_C(6)). Its target is the Cartan H¹(O_C(−8)).
2. The attainable ranks are exactly every integer 0,…,min(7,d−3). The same statement holds for d=4,6, although their full boundaries can also have a positive-root component.
3. For every d≥4, the maximal-degree line in F_C lifts to a line subbundle of F if and only if e=0. This is also equivalent to F being a direct sum of line bundles on E, and to the positive root P⊂End₀(F_C) lifting to a line subbundle of End₀(F).
4. For d≥8, ε=0 if and only if e=0, hence if and only if these splitting/lifting conditions hold. For d=4,6, ε=0 instead requires both e=0 and the diagonal reference-deformation class h=0. Thus a split bundle can have nonzero ε in these small cases.

These are classifications of ranks and lifting conditions for ribbon-local models, not of unframed bundle isomorphism classes and not of the actual HM connecting map.

## 1. A determinant-correct reference on E itself

Put L=O_E(d/2 plane). The square-zero units sequence gives

    0 → H¹(J) → Pic(E) → Pic(C) → 0.

Constants lift and H²(J)=0; multiplication by 2 is invertible on the kernel H¹(J). As deg((LD)|C)=d−4 is even, there exists A₀ with A₀²≅LD. Set Q₀=DA₀⁻¹ and F⁰=A₀⊕Q₀. Then det F⁰=D, Hom(Q₀,A₀)=L, and

    End₀(F⁰)=L E₊ ⊕ O_E H ⊕ L⁻¹ E₋,

where E₊,H,E₋ denote the usual root/Cartan matrix positions, H=diag(1,−1). This notation indicates their local generators with the displayed line-bundle weights. This reference exists on the actual nonsplit ribbon, not on a substitute split thickening.

Every quotient section of G⁰ lifts: its only section contribution is O_C(d−4), obtained by restricting O_E(d/2−2 plane), and conic restriction from P² is surjective since H¹(P²,O(m))=0 for every m. Consequently ε⁰=0.

## 2. All framed determinant-fixed deformations and their boundary

Fix an identification F_C≅F⁰_C compatible with determinants, and a determinant identification det F≅D. Affine locally, lift this identification to determinant-preserving bundle isomorphisms on E. Any determinant discrepancy in 1+J can be corrected locally. Their overlap discrepancies are 1+u_ij with

    u_ij∈J⊗End₀(F_C),
    u_ij = p_ij E₊ + h_ij H + e_ij E₋.

Because J²=0, their cocycle equation and gauge changes are additive. Conversely every such Čech cocycle modifies the reference transition functions to give a locally free rank-two bundle on this same E. Its determinant is unchanged: det(1+u)=1+tr(u)=1. Thus framed classes are parameterized by

    H¹(O_C(d−4)) ⊕ H¹(O_C(−4)) ⊕ H¹(O_C(−d−4)).

The first group vanishes for d≥4. We can therefore choose a representative with p=0, leaving h and e. This is a framed parameterization relative to F⁰; reduction automorphisms must be accounted for in any unframed classification.

Conjugation on End₀ gives 1+ad(u). Since

    [H,E₊]=2E₊,    [E₋,E₊]=−H,

comparison with the zero reference boundary gives

    ε(s) = (2h cup s, −e cup s, 0),                         (1)

up to one consistent Čech sign convention. The twists are, respectively, O_C(d−8), O_C(−8), O_C(−d−8). There is no missing deformation term from the base: the two bundles are compared on the same fixed E, and their reference sections already lift on E.

For d≥8, H¹(O_C(d−8))=0. Hence ε depends only on e, with the asserted seven-dimensional target. This also proves that all possible effective boundaries in this range lie in this catalecticant family, not merely that an example family does.

## 3. Serre duality and the matrix

Let n=d−4≥0. Serre duality on P¹ identifies

    H¹(O_C(−n−8)) = H⁰(O_C(n+6))*,
    H¹(O_C(−8)) = H⁰(O_C(6))*.

Compatibility of Serre duality with multiplication gives

    ⟨e cup s,t⟩ = ⟨e,st⟩,
    s∈H⁰(O_C(n)), t∈H⁰(O_C(6)).                           (2)

Thus the Cartan component C_e is a binary catalecticant. In homogeneous coordinates X,Y, define moments μ_k by evaluating the functional e on X^(n+6−k)Y^k, 0≤k≤n+6. With monomial bases (no binomial normalization), its matrix is

    (C_e)_(i,j)=μ_(i+j),  0≤i≤6, 0≤j≤n.                  (3)

The full rank strata for d≥8 are therefore exactly the Hankel determinantal strata: rank≤r means all (r+1)-minors vanish, and rank=r additionally means some r-minor is nonzero. This is a rank classification, not a claim that every functional of rank r admits a sum of r distinct evaluations; degenerations can involve confluent evaluations.

The assignment e↦C_e is injective for every n≥0. Indeed products H⁰(O(n))H⁰(O(6)) span H⁰(O(n+6)): every degree-(n+6) monomial is a product of these degrees. Consequently C_e=0 iff e=0.

## 4. Universal evaluation construction: every rank occurs

Fix a formal integer r with 1≤r≤min(7,n+1). Work over the parameter scheme with variables z₁,…,z_r and w₁,…,w_r, with all weights and all differences z_i−z_j invertible. For homogeneous degree-(n+6) forms define the universal functional

    e(f)=Σ_(k=1)^r w_k f(1,z_k).

This is a symbolic family, not an evaluation of any selected HM map, rank instance, or source. Its moments are μ_l=Σ_k w_k z_k^l. Hence its matrix factors as

    C_e = V_6 diag(w₁,…,w_r) V_n^T,
    (V_m)_(i,k)=z_k^i, 0≤i≤m.

The first r rows of both Vandermonde matrices have determinant ∏_(i<j)(z_j−z_i), a unit on the parameter scheme. Thus V_6 is a split injection, V_n^T is a split surjection, and the middle diagonal map is invertible. Their composite has rank exactly r on every fiber. Equivalently its leading r×r minor is the product of the two Vandermonde determinants and all weights, and rank≤r follows from the factorization. The parameter scheme is nonempty over C. No particular values need be selected or computed. For r=0 use e=0. Since the maximal-rank stratum is nonempty and is defined by nonvanishing minors, it is a dense Zariski-open subset of the affine e-parameter space; for d≥8 the same holds after including the unconstrained h-parameters. This is genericity in the ribbon-local family only, not genericity in the HM family.

Choose h=0 and a Čech representative for this universal e in J⊗Hom(A₀|C,Q₀|C). Modify the transition functions of F⁰ by 1+e_ij E₋. The square-zero cocycle construction in §2 produces determinant-correct bundles with boundary (0,−C_e,0). The reference argument works uniformly, and (3) proves their ranks. This attains all permitted ranks on the fixed nonsplit E.

## 5. Small splittings

For d=4, n=0, the domain is one-dimensional. The Cartan component is the 7×1 column C_e, while the positive-root component is the class 2h∈H¹(O_C(−4)) of dimension three. Thus ε has rank zero exactly when e=h=0; every nonzero pair gives rank one. Setting h=0 in §4 realizes ranks zero and one.

For d=6, n=2, the domain is three-dimensional. The Cartan block is the 7×3 Hankel matrix C_e, while the positive-root block is a single row 2H_h with target H¹(O_C(−2)). By Serre duality H_h is precisely the functional h∈H⁰(O_C(2))* applied to the section. Thus the complete matrix is the vertical stack of −C_e and 2H_h. More precisely, rank ε equals rank C_e if H_h belongs to the row space of C_e, and equals rank C_e+1 otherwise. This includes the zero row-space case and cannot exceed three. Every rank 0,1,2,3 is attained with h=0 by §4. Zero rank requires e=h=0. In particular, among split models (e=0), the boundary has rank one exactly when h≠0.

For d=0 or 2, H⁰(B_C(−4))=0, so the only boundary rank is zero. No bundle splitting follows from that vacuous boundary. For d=2 the maximal-line lifting obstruction still has a negative-root description after choosing a reference, but it is invisible to ε. No intrinsic positive-root line is singled out when d=0.

## 6. Precise line lifting and splitting condition

Assume d≥4. The unique maximal-degree line A_C=O_C(a)⊂F_C has a canonical obstruction to lifting as a line subbundle of F:

    ob(A_C)∈H¹(J⊗Hom(A_C,F_C/A_C))=H¹(O_C(−d−4)).

Using the reference and local graph lifts, this obstruction is exactly e. The local graphs change it by coboundaries, so a global line subbundle exists iff e=0. Local lifted primitive vectors give line subbundles with locally free quotients, not just arbitrary rank-one subsheaves.

If e=0, choose a representative with its lower component zero; the upper component can also be killed since H¹(O_C(d−4))=0. The remaining diagonal transition modifications give F=A⊕Q, with A lifting A_C, Q lifting its complement, and AQ=D. Conversely, a splitting of F must restrict with one factor equal to the unique maximal line A_C, and hence forces e=0. One can alternatively split the extension after lifting A: the remaining extension class reducing to zero comes from H¹(J⊗Hom(Q_C,A_C))=H¹(O_C(d−4))=0.

For P=Hom(Q_C,A_C)⊂B_C, the obstruction to lifting P as a line subbundle of B is the class of ad(u)|P in

    H¹(J⊗Hom(P,B_C/P)).

Its Cartan component is the nonzero scalar multiple −e in H¹(O_C(−d−4)); its opposite-root component is zero. Thus it vanishes iff e=0. When e=0, the splitting F=A⊕Q supplies an isotropic positive-root line Hom(Q,A) on E. This proves equivalence even if the requested lift of P was not assumed isotropic.

The lift of A_C, when it exists, is unique as an embedded line subbundle because the difference torsor has H⁰(J⊗Hom(A_C,F_C/A_C))=H⁰(O_C(−d−4))=0. The same holds for the lift of P: its difference space is H⁰(O_C(−d−4)⊕O_C(−2d−4))=0.

A lift of P as some line bundle is different from a lift isomorphic to the fixed reference line L=O_E(d/2 plane). When e=0, the positive-root line is deformed relative to L by 2h∈H¹(J), as follows from the ratio of the diagonal transition factors. Therefore it is isomorphic to that reference L iff h=0 (with the chosen reference and determinant framing). Likewise F is isomorphic to the reference split bundle through a reduction-preserving determinant-fixed isomorphism iff e=h=0. These last statements retain their framing/reference qualification.

Combining this with injectivity of e↦C_e gives §1(4). In particular, for d≥8 a zero boundary forces splitting on E but does not force its two factors to be the chosen reference factors: diagonal deformations remain invisible. For d=4,6 the diagonal deformations can make the boundary nonzero even for split bundles.

## 7. Why ribbon-local arguments cannot improve the rank interval

For each permitted d, the models above have exactly the same fixed nonsplit E, determinant D, reduction splitting, and genuine tracefree rank-two endomorphism/trace structure as the input package. Their boundary ranks fill the entire interval already proved to contain all possible ranks. Consequently those data alone imply neither a larger lower bound nor a smaller upper bound nor exclusion of any intermediate integer. In particular, nonsplitness of E does not imply nonzero boundary, and existence of nonzero negative-root deformations does not imply a prescribed positive rank.

This sharpness statement is only about this explicitly listed ribbon-local package. Global extendability, HM monad conditions, ambient Chern classes, compatibility with component-image maps, or any extra already-known condition outside that package could exclude these models. We do not claim that a model realizes an actual HM restriction or determines any ambient source/obstruction. Establishing a stronger actual-HM rank statement therefore requires such additional input. No selected HM splitting, matrix, polynomial, source, retained class, or rank has been evaluated.

## Dependencies and scope

Input: ../ribbon-duality-constraints/PROOF.md and AUDIT.md, particularly the determinant-correct reference, zero reference boundary, and seven-dimensional bound. This derivation consists solely of square-zero descent, line-bundle cohomology, Serre-dual multiplication, and symbolic Vandermonde identities. No actual-source value or numerical rank is evaluated.
