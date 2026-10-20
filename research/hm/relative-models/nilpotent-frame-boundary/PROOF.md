> Publication scope: Exact reduced-set fixed-W boundary uses N intersect closure(X), not all N; algebraic DVR degenerations and finite kernel maps. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Regular-nilpotent limits and the fixed-three-plane rank-one boundary

## Scope and main conclusions

Work over C. Fix a three-dimensional space W and a linear map T on E_W=sl(W)⊗det(W), with the universal tensor τ and frame criterion of ../../cubic-loci/global-kernel-incidence/general-three-plane-kernel/PROOF.md. Trivialize det(W), put K=ker T⊂sl(W), and assume K contains no nonzero rank-one endomorphism. Set

    X={ [A]∈P(K): det A=0, tr(A²)≠0 },
    Y=closure(X) in P(K), with reduced structure,
    N={ [A]∈P(K): det A=tr(A²)=0 }, with reduced structure,
    N_Y=N∩Y, with reduced structure.

Every point of N is regular nilpotent. Let Z_ind⊂W³ be the independent zero-frame locus and let R_1^×⊂W³ denote triples (a u,b u,c u) with u≠0 and a,b,c≠0.

**Exact fixed-W boundary theorem.** As sets of complex points,

    closure(Z_ind) ∩ R_1^×
      = { (a u,b u,c u): a,b,c≠0, [u]∈κ(N_Y) },

where κ([A])=ker A∈P(W). In particular every point on the right has an actual algebraic DVR degeneration from independent zero frames, after a finite extension of the DVR. No assertion of equality of scheme structures is made.

The morphism κ:N→P(W) is finite onto its image. On N, if M=O_N(1), then

    κ*O_P(W)(3) ≅ M³.

For every integral curve C⊂N, writing Γ=κ(C) and δ=degree(C→Γ), this implies

    δ·degree(Γ)=degree(C).

The same conclusions hold for the map sending A to its kernel hyperplane ker A² in P(W*).

If dim K=3 and det|K≡0, then Y=P(K), N is a smooth conic, and κ identifies it with a smooth conic in P(W). The displayed boundary therefore has dimension four.

If dim K=4, then Y=V(det|K), N is the reduced support of a complete-intersection (2,3) curve, and κ(N) is a projective curve of degree at most six. The displayed boundary again has pure dimension four. If q|K has rank one, the degree bound improves to three. These are conditional statements for an actual structural K_W, not claims that such a K_W exists.

Only universal families are used. No actual HM/source/model matrices, products, ranks, selected input evaluations, jets, residues, or Massey values are computed. All writes are local proof artifacts.

## 1. Curve selection and a nonvanishing representative

Let [A₀]∈N_Y. The standard algebraic curve-selection lemma supplies an integral curve through [A₀] whose generic point belongs to X; equivalently there is a DVR R, with residue field C, a morphism Spec R→Y taking its closed point to [A₀] and its generic point into X. One may obtain it by taking an integral curve through the point meeting the dense open X in an irreducible component of Y, and normalizing at a point over [A₀]. This is applicable because X is open in Y and dense in each of its irreducible components. A zero-dimensional component of Y cannot contain a point of N_Y.

Trivializing the pullback of the tautological line produces A∈K⊗R whose reduction is a nonzero representative of [A₀]. Its determinant is zero and q(A)=tr(A²) is nonzero in the fraction field F and zero in the residue field.

Adjoin to F a root λ of λ²=q(A)/2 and take a DVR R' above R in the normalization of this finite field extension. These DVRs arise from curves of finite type, so this normalization is finite. The residue field remains C. The root λ is integral and belongs to R', and λ reduces to zero. Replace R by R' and F by its fraction field. The generic eigenvalues of A are the distinct elements λ,0,−λ.

## 2. Primitive eigenvectors and prescribed limits

For each generic eigenline V_+,V_0,V_-⊂W⊗F, its intersection with the lattice W⊗R is a saturated free rank-one R-module. Indeed any F-line admits a vector whose coordinates have minimum valuation zero; such a primitive vector generates the intersection, and has nonzero reduction. Choose these generators x,y,z in the order λ,0,−λ.

The generic eigenvector equations hold over R, since both sides are integral. Reducing modulo the maximal ideal gives

    A₀ x̄=A₀ ȳ=A₀ z̄=0.

Because A₀ is regular nilpotent, ker A₀ is a line; all three reductions are nonzero and lie on that line. For any prescribed nonzero vectors x₀,y₀,z₀ on that line, multiply x,y,z independently by nonzero complex constants so that their reductions are x₀,y₀,z₀.

The generic triple is independent. By the universal spectral frame criterion its τ belongs to K⊗F, hence Tτ=0 generically. Since Tτ is integral over the domain R, it vanishes over R. This proves the required family, with exactly the prescribed all-nonzero special triple.

The three integral eigenline submodules need not form a direct-sum decomposition over R: their special fibers coincide. This does not obstruct the construction. No extension of the étale spectral cover across q=0, or splitting by spectral idempotents over R, has been assumed.

## 3. Necessity and exactness

Suppose v₀=(a u,b u,c u) belongs to closure(Z_ind), with a,b,c and u all nonzero. Curve selection in the affine space W³ provides a DVR family (x,y,z) specializing to v₀ and generically belonging to Z_ind. At the generic point [τ(x,y,z)] belongs to X. Properness of P(K) extends this projective point over the DVR; trivialize its tautological line and write A for a primitive integral representative. Its special value A₀ is nonzero, and its projective class lies in Y.

Generically the universal frame identity gives

    Ax=μx,    Ay=0,    Az=−μz

for some μ∈F*, with q(A)=2μ² and det A=0. Because x has a nonzero special value, one of its coordinates is a unit. The corresponding coordinate of Ax=μx shows μ∈R. Reducing Ay=0 gives A₀u=0. Reducing Ax=μx then gives μ̄=0, because a u≠0. Thus q(A₀)=0, and det A₀=0 by specialization. Rank-one-freeness forces the nonzero nilpotent A₀ to have rank two. Hence ker A₀=Cu and [A₀]∈N_Y.

This proves necessity. Together with Section 2 it proves the exact equality of complex-point sets. It does not extend this exact description to triples with one or more zero entries: such triples can arise by rescaling semisimple frames as well.

## 4. Finite kernel-line map and polarization

On the reduced projective scheme N, the universal map A:E→E⊗M, where E=W⊗O_N and M=O_N(1), has cube zero, rank two, and square of rank one. Since N is reduced, constant pointwise ranks imply local constant-rank bundle forms. Thus F₁=ker A and F₂=ker A² are subbundles, and the induced maps of successive line quotients are isomorphisms. Put L=F₁. The graded pieces of E are

    L, L⊗M, L⊗M².

Taking determinants gives L³⊗M³≅O_N. The kernel classifying map satisfies L=κ*O_P(W)(−1), proving κ*O(3)≅M³.

A positive-dimensional fiber of κ would contain an integral projective curve C. On that curve κ*O(3) is trivial, whereas M³ has positive degree, a contradiction. Thus κ is quasi-finite; it is proper, hence finite onto its closed image.

For an integral curve C, pull the identity to its normalization and take degrees. The degree formula for a finite morphism of projective curves gives δ·deg Γ=deg C, also when the original curves are singular.

For the kernel-hyperplane map η([A])=ker A², the tautological quotient bundle is E/F₂=L⊗M². The hyperplane map pulls back O_P(W*)(1) to this quotient. Its cube is M³, giving the identical finiteness and degree argument. The flag map (κ,η) is consequently finite too. These identities constrain the image curves, not the full flag variety or all rank-one triples in a varying ambient W.

## 5. Singular three-dimensional kernels

Import ../../cubic-loci/cubic-component-multiplicities/applications/constant-rank-kernel-nets/PROOF.md. If dim K=3, det|K≡0, and K is rank-one-free, the kernel-line map P(K)→P(W) is induced by a linear isomorphism K→W. The trace-square form has rank three. Therefore X is the complement of a smooth conic in P(K), Y=P(K), and N is that conic. Its image Γ under κ is another smooth conic.

The all-nonzero rank-one boundary is the product over Γ of three punctured copies of the tautological line bundle. It is smooth, irreducible, and four-dimensional. This description is only of the indicated locally closed rank-one stratum with its reduced structure, not of its scheme-theoretic embedding in closure(Z_ind).

## 6. Every four-dimensional rank-one-free kernel

Import the nonvanishing q|K≠0 from ../../cubic-loci/cubic-component-multiplicities/applications/isotropic-four-kernel-exclusion/PROOF.md and h=det|K≠0 from the constant-rank-four-space obstruction. If h is irreducible, no degree-two polynomial q can vanish identically on V(h); hence X is dense in V(h) and gcd(h,q)=1.

If h is reducible, ../../cubic-loci/cubic-component-multiplicities/applications/reducible-four-kernel/PROOF.md identifies V(h) with a reduced plane plus a smooth irreducible quadric, and proves q is not identically zero on either component. Again X is dense in the whole determinant surface, and gcd(h,q)=1.

Consequently Y=V(h), and N is the reduced support of V(h,q), a projective complete intersection of degrees three and two. Its scheme has pure dimension one and degree six; its reduced support is pure one-dimensional with degree at most six. Every point is regular nilpotent because K is rank-one-free. Thus every nilpotent point qualifies for the degeneration theorem.

Write C_i for the reduced irreducible curve components of N. Each κ(C_i) is a curve and has degree at most deg C_i by Section 4. Different image components may coincide; removing duplicates only reduces the degree sum. It follows that the reduced curve Γ=κ(N) satisfies

    deg Γ ≤ Σ_i deg C_i ≤ 6.

If rank(q)=1, write q=cℓ². The reduced support N is contained in the plane ℓ=0 and is the support of its cubic section h|_{ℓ=0}; this restriction is nonzero because gcd(h,q)=1. Thus deg N≤3 and deg Γ≤3. No reducedness or smoothness of that plane cubic is needed.

The exact boundary from Section 3 is three punctured tautological line bundles over Γ, so it has pure dimension four. This is a fixed-W conclusion. Taking all W, or determining which W actually have these kernels, is a separate problem. In particular this theorem neither covers all rank-one triples in the full ambient problem nor proves that an actual four-dimensional kernel exists.
