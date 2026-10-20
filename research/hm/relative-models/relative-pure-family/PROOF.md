> Publication scope: Algebraic relative formal lift on each affine good-base open with a fixed pure two-jet; no global gluing or mixed theorem. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Pure-direction joint quantization over every affine good-base open

## Verdict and precise statement

The fiberwise theorem extends to an algebraically coherent family over **each affine open** U of the good base B°. It does not establish that independently chosen lifts for different U agree on their overlaps or descend to B°.

Let Y=C×C, with C the smooth projective elliptic curve in the supplied geometry, X_U=Y×U, r:X_U→U, A=Γ(U,O_U), and F the restriction of the actual rank-two bundle family. Use H=(Z/2)² acting on the two Y factors and trivially on U, and χ=ε₁ε₂. Assume the standing identification F=N⊗f*HM and its genuine H-linearization, the good-fiber simplicity established in the localization audit, and the supplied normalized first-order trace/gerbe identities. Fix the supplied **pure π₁₂ ambient two-jet**, as a regular relative differential algebroid over U. Give h character χ.

Then there exist, on an H-equivariant affine refinement of its cover:

1. A formal relative differential algebroid on X_U over A[[h]], preserving the prescribed ambient coefficients through h² literally after restriction.
2. A compatible formal locally free rank-two module reducing to the entire family F on X_U.

Higher local products, overlap maps, and triple units are allowed to change. Every coefficient is algebraically regular and is differential only in the Y directions. The family F can vary nontrivially with U; it need not be pulled back from Y or U. No source matrix, detector, actual obstruction value, or model rank has been evaluated.

## Sources and accepted premises

- Fiberwise joint theorem: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260293233 (read 2026-10-19).
- Localization: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260145920 and the independent local SOURCE_AUDIT.md.
- Literal ambient small-extension identities: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725.
- Module small-extension and characteristic variation: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259871686 and MODULE_SOURCE_AUDIT.md.
- Fixed two-jet: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md, especially §§2–4 and 8. This presentation was read, not evaluated on module transition matrices.
- Algebraic differential-cochain background: Yekutieli, https://arxiv.org/html/0905.0488, §3. The relative HKR step needed here is justified below, rather than inferred merely by substituting an arbitrary coefficient ring into a theorem stated over a field.

The exceptional-fiber proof is compatible with this theorem but gives no extension across the complement of B°: its nonzero tracefree H² is precisely what is excluded here.

## 1. Cohomology on the whole affine-base family

Put G=End₀(F). Proper cohomology and base change, using fiberwise simplicity and Serre duality, give on B°

    r_*G=0,  R²r_*G=0,  R¹r_*G locally free.

Since the relative dimension is two, all higher direct images vanish as well. Leray therefore gives

    H²(X_U,G)=H¹(U,R¹r_*G)=0

because U is affine. This is a statement about F on all of X_U, not merely about its individual fiber restrictions.

In characteristic zero trace splits the coefficient bundle:

    End(F)=O_X·Id ⊕ G,
    tr(f·Id)=2f.

Hence scalar inclusion is an isomorphism

    H²(X_U,O_X) → H²(X_U,End(F)) = Ext²_X_U(F,F).

Product cohomology and affine U identify

    H²(X_U,O_X)=A⊗_C H²(Y,O_Y)=A⊗χ.

Here the last notation records the H representation on the one-dimensional factor, not a choice of normalized basis. Trace is twice the inverse of scalar inclusion. In particular there is no tracefree obstruction on X_U, and H acts trivially on A. We use ordinary global Ext on X_U: this is exactly the cohomology controlling transition-matrix lifting over the fixed underlying scheme and relative algebra. It is not necessary to replace it with an unrelated Ext theory on the base.

## 2. The actual relative differential complex and HKR

Let C^m_diff(X_U/U) be the sheaf of regular O_U-multilinear polydifferential cochains of finite order in each argument. For m=0 this is O_X. For m>0 take normalized cochains (zero if any input is 1). Put D^q=C^(q+1)_diff for q≥−1, including arity zero, with Hochschild differential b.

These are genuinely vertical cochains. A coefficient can be any regular function of both fiber and base coordinates; O_U-linearity means that derivatives of functions pulled back from U are zero. Composition, restriction, the Hochschild differential, and the universal descent-defect formulas preserve this condition.

For completeness, relative differential HKR here can be reduced to the usual local polynomial computation without assuming a formality theorem over A. The smooth product morphism X_U→U has relative principal-parts modules obtained by base change from Y→Spec C. At each finite differential-order bound these modules are locally finite locally free; the sheaves of bounded polydifferential operators are their duals/tensor constructions. Taking their filtered union gives the differential-cochain sheaves, which are quasi-coherent. Normalization is the standard split normalization, compatible with this base change.

On relative étale-coordinate neighborhoods, the antisymmetrization map from relative multiderivations to normalized polydifferential cochains is the HKR quasi-isomorphism. One can check it using the Koszul resolution of the relative diagonal for a polynomial algebra over A, where the diagonal differences form a regular sequence; localization and étale base change preserve this calculation. Equivalently, on product coordinate neighborhoods it is the C-linear differential HKR calculation tensored with the flat C-algebra A. These local maps agree under restriction, giving the natural H-equivariant sheaf quasi-isomorphism of complexes

    (⊕_j Λ^j T_X_U/U [−j], zero differential)
          → C^•_diff(X_U/U).

Only the cochain-complex quasi-isomorphism is asserted; no strict compatibility with the Gerstenhaber bracket is needed. Thus on any affine-intersection cover the shifted Čech total complex L satisfies

    H²(L)=HH³_diff(X_U/U)
          = ⊕_(j+q=3) H^q(X_U,Λ^j T_X_U/U)
          = A⊗_C HH³_diff(Y/C).

The last equality uses the product relative tangent bundle, flat scalar extension from C, and affine-base cohomology, not that F is a product bundle.

Let ι=(-1,-1)∈H be simultaneous fiber deck inversion. On invariant vertical vector fields it acts by −1 and on H^q(Y,O_Y) by (−1)^q. Consequently every total degree-three HKR summand has sign −1. The only potentially nonzero summands for a surface are (j,q)=(1,2),(2,1). Hence

    HH³_diff(X_U/U)^ι=0.

Because χ(ι)=+1, every h^n has trivial ι action, so this vanishing holds with every small-extension coefficient A·h^n. Relative HKR introduces no base tangent directions and no extra base-cohomology summands when U is affine. Using absolute HH³(X_U/C) instead would be incorrect for this argument.

## 3. The fixed two-jet is a relative object, not a fiberwise choice

Select the P={1,2} part of the prescribed two-parameter/pure presentation, not the restriction of the full π₁₂+π₃₄ algebra to a fiber. Its first product is π₁₂/2; its second product uses only V₁,V₂; its gerbe is b_P and its overlap correction is T_P. The pinned formula for T_P is a sum of regular coefficient functions multiplying V₁ or V₂. It therefore annihilates pullbacks of base functions. The scalar functions a and q appearing in that formula are regular on the cover members or overlaps where they are used. All coefficients remain regular after restriction to X_U and further refinement.

More generally, a regular base-dependent coefficient in T_P causes no difficulty: f(y,u)V_i remains an O_U-linear vertical differential operator. No inference from fiberwise values to a global differential operator is being made. The operator is already supplied on the family. One must not retain T_Q or an arbitrary transverse derivative in a claimed relative two-jet. The pinned pure presentation satisfies this prerequisite; if a different prescribed presentation contained transverse derivatives, this theorem would not apply while preserving it literally.

The given parity remains literal: π₁₂ and b_P have character χ, while μ₂ and T_P are H-invariant. With h of character χ the entire supplied two-jet is equivariant. The descent identities hold as relative identities on X_U. Nothing requires U to be stable under the other two deck involutions or a factor swap: the H used here fixes the base pointwise.

## 4. A cover that both preserves the two-jet and trivializes the family

X_U is a quasi-compact separated scheme. Refine the restricted ambient cover by a finite affine open cover on which F is free. Refine inside the original ambient opens, so each has a specified parent chart and the old coefficients are pulled back literally. Separatedness makes finite intersections affine.

For equivariance, replace the index set by freely H-labeled translates of these opens. Transport the frames through the genuine H-linearization of F and transport the parent-chart labels through the H action of the ambient cover. Distinct labels may represent the same geometric open; this is harmless. The full Čech nerve with ordered tuples supports an honest action by relabeling and its affine-intersection Čech complex computes the required cohomology. One does not impose a global ordering incompatible with the H action, nor require an individually H-stable open to carry an invariant frame.

This construction does not make the bundle a pullback from Y and does not choose independent frames separately at each base point. Its transition functions are regular matrices on opens of the whole X_U. All later solutions are cochains in this fixed algebraic cover.

## 5. First-order cancellation on X_U

The first-order module obstruction is the relative characteristic class

    o₁=ev_F,rel(π₁₂) − [b_P]Id ∈ H²(X_U,End(F)).

The characteristic construction uses the relative Atiyah class, or equivalently the vertical first-order transition defect, and commutes with restriction to a fiber. By the supplied normalized identity on every good fiber, o₁ restricts to zero on every closed fiber.

This fiberwise statement really does imply global vanishing here. By affine Leray,

    H²(X_U,End(F)) = Γ(U,R²r_*End(F)),

and trace/base change identifies R²r_*End(F) with the line bundle R²r_*O_X. This is the trivial bundle H²(Y,O_Y)⊗O_U. A section restricting to zero at every closed point is zero because U is a reduced complex variety. In particular no hidden tracefree or base-cohomology component survives. Alternatively, take trace first, apply the same argument to the scalar line, then use trace injectivity.

Thus the first-order obstruction is zero on the whole family. Solve its Čech coboundary equation on the fixed affine cover. The action of H on this equation is A-linear. Averaging the primitive, with h assigned χ, gives an equivariant first-order module lift. This is averaging new linear coefficients, not averaging products or nonlinear module descent data.

## 6. Preserve the fixed ambient two-jet

For that first-order module lift, the obstruction at degree two with the ambient two-jet fixed lies in

    (H²(X_U,End(F))⊗h²)^H
       = (A⊗χ⊗χ²)^H = 0.

Therefore an equivariant module lift through h² exists without any change to the prescribed ambient two-jet. Solve and average its new linear correction just as at first order.

## 7. Relative all-order induction

Assume joint equivariant data have been constructed through degree n−1, for n≥3. Work modulo h^(n+1) with small-extension ideal I=A·h^n, for which hI=I²=0.

Choose arbitrary normalized relative coefficientwise lifts of the ambient products, overlap maps, and triple units, equivariantly. The literal descent lemma applies verbatim: its operations are algebraic and relative O_U-linear, and every positive-order old coefficient kills I. Its defect is a closed degree-two cochain in L⊗h^n. Diagonal fiber inversion fixes this defect, whereas H²(L)⊗h^n has no invariant part. Thus there is a relative regular differential primitive; average it over H and repair the new coefficients. This produces a genuine equivariant ambient extension, not merely local associative products.

For this ambient extension the module descent defect is a Čech two-cocycle with coefficient End(F)⊗h^n, by the audited four-index identity. It is scalar in cohomology by Section 1.

- If n is even, its invariant cohomology group is zero because χ⊗χ^n=χ.
- If n is odd, scalar inclusion gives a unique scalar cohomology class representing the module obstruction. Choose a scalar Čech two-cocycle a in the required weighted invariant part; this is possible by equivariant averaging. Change only the newly chosen triple-unit coefficient by a. The relative total cochain (0,0,a) is closed: δa=0 and b(a)(f)=fa−af=0 at classical order. The module variation is exactly −a·Id, with the audited row-module convention, so this kills the module obstruction class.

After either step solve the remaining module Čech coboundary equation and average its new primitive. The resulting module is locally free of rank two, with invertible transition matrices in the h-adic sense because their classical reductions are the transition matrices of F. No coefficient below degree n is changed.

Induction gives compatible finite-order families and their coefficientwise h-adic inverse limit. Each coefficient has finite relative differential order, though no uniform bound in n is asserted. The limit is formal; no convergence or evaluation at nonzero h is claimed.

## 8. Exact advance and limitations

This promotes point-by-point existence to a single algebraic relative quantization and module for the whole family over any specified affine good-base open U. It does not merely select unrelated quantizations of its closed fibers. Restricting the constructed object to a smaller open provides a compatible restriction of that particular choice.

It does not choose a mutually compatible system for independently constructed lifts over every affine open of B°, provide descent isomorphisms on their overlaps, or solve global descent over B°. In particular, the group H¹(B°,R¹r_*End₀(F)) may remain relevant globally. It also does not handle exceptional fibers, the mixed π₁₂/π₃₄ problem, pair exchange, a fixed all-order Moyal product, characteristic periods, or retained global detector values. The only symmetries required here are the two fiber deck involutions; no literal factor-swap claim is made.

The necessary additional condition compared with a bare fiberwise existence statement is that the fixed pure two-jet and the bundle H-linearization are already defined relatively over the family. The supplied geometric family and pinned pure presentation meet this condition under the standing identification. Fiberwise existence alone, with no such relative data, would not suffice.
