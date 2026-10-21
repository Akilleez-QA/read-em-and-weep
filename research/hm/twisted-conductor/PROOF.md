# Picard twists: descent, conductor defects and residual direct images

Status: authored structural proof, independently mathematically reviewed (PASS), conditional on the pinned inputs; not formally checked. Work over C. No selected actual HM/source coefficient, matrix, rank or numerical instance is evaluated.

## 1. Exact inputs and notation

Let ν:X→S be the normalization of the actual primary surface, π:X→B=P¹ the modular elliptic fibration, h:B→Γ the normalization of the six-nodal canonical decic, and g:S→Γ the residual morphism, with gν=hπ. Use:

- PR574, commit **3c92fdc469f6870520e7a9d905b5ab9199a5bf37**, `research/hm/primary-conductor/PROOF.md`: the actual normalization sequence 0→O_S→ν_*O_X→T→0, where T is supported with length one at each of thirty double points Z; their sixty preimages W are reduced. Also h¹(O_X)=0 and h²(O_X)=4.
- PR577, commit **563fc7036faa4965e55bda3bec5b82ae5360fa6c**, `research/hm/residual-fibration-defect/PROOF.md`: each node q of Γ has two preimages a_q,b_q∈B and a block Z_q of five points of Z, each gluing one point over a_q to one point over b_q. The residue-difference formula is actual, and Rπ_*O_X has cohomology O_B and N=O_B(−5) in degrees zero and one.
- PR579, commit **78746b35576c319dd6100c2ec6d4f628100b2200**, `research/hm/residual-direct-image-splitting/PROOF.md`: the point-restriction factorization that annihilates the elliptic derived summand before finite pushforward along h.
- PR581, commit **7c78b3fe1612934aa0c1ed0a41b9c941b7fa7497**, `research/hm/picard-averaging/PROOF.md`: Pic⁰(S) is the thirty-dimensional gluing torus, Pic⁰(Γ) is the six-dimensional gluing torus, and actual pullback repeats each ratio five times in its block.

Fix an arbitrary L∈Pic⁰(S). Its pullback ν*L is trivial. Choose a trivialization, orient each pair a_q,b_q, and let t_z∈C* be its thirty gluing ratios in the induced orientations. These choices only write the maps in coordinates. The conditions and sheaves below are intrinsic.

Call q **uniform for L** if the five t_z for z∈Z_q are equal. Let r(L) be the number of nonuniform nodes, so 0≤r(L)≤6. Put

    A_L=g_*L,     V_L=g_*(T⊗L),
    d_L:h_*O_B→V_L,     J_L=im(d_L),     K_L=coker(d_L).

Here V_L is the sum of thirty residue-field lines. The map d_L follows from the chosen trivialization and the tensor product of the normalization sequence with L. Its image, kernel and cokernel are well-defined up to the induced intrinsic identifications.

## 2. The local gluing matrix and the descent criterion

At q, complete the local ring and write

    R=C[[s,t]]/(st),     Rbar=C[[s]]⊕C[[t]].

Choose compatible bases in the five target residue lines. The actual local map is

    d_L(f,g)=(f(0)−t_z g(0))_{z∈Z_q}.                 (1)

It depends only on the two residues, and its two columns are the constant vector 1 and the vector −(t_z). Thus

    dim_C(J_L)_q = 1 if q is uniform, and 2 otherwise. (2)

If q is uniform with common value t_q, the kernel is

    {(f,g): f(0)=t_q g(0)}.

Rescaling the second branch identifies this R-module with R. Hence A_L is invertible at q. If q is nonuniform, two unequal ratios in (1) force f(0)=g(0)=0. Its kernel is then

    sC[[s]]⊕tC[[t]]=m_R⊂Rbar.                       (3)

This module is not free of rank one: its quotient by m_R times itself has dimension two, whereas a free rank-one module has one generator. Faithful flatness of completion transfers the assertion to the algebraic stalk.

Away from the six nodes, h is an isomorphism and A_L is locally O_Γ. It is a rank-one torsion-free sheaf everywhere, as a subsheaf of h_*O_B. Therefore

    A_L is locally free exactly when all six blocks are uniform.

By the exact pullback dictionary of PR581, all blocks are uniform precisely when there is a line bundle M∈Pic⁰(Γ) whose six ratios are their common values and g*M≅L. Such M is unique, since g*:Pic⁰(Γ)→Pic⁰(S) is injective. Projection formula and g_*O_S=O_Γ then give A_L≅M. We have proved the intrinsic equivalence

    L∈g*Pic⁰(Γ)  ⇔  r(L)=0  ⇔  g_*L is invertible.  (4)

Thus local freeness of the residual direct image detects actual descent, not merely a numerical necessary condition.

## 3. Degree and the finite defect

The sequence

    0→A_L→h_*O_B→J_L→0                              (5)

and (2) give length(J_L)=6+r(L). Since χ(O_B)=1 and Γ has arithmetic genus six,

    χ(A_L)=−5−r(L),
    deg(A_L):=χ(A_L)−χ(O_Γ)=−r(L).                  (6)

The degree here is the standard degree of a rank-one torsion-free sheaf, defined by Euler characteristic. It does not assert invertibility at nonuniform nodes.

Likewise

    length(K_L)=30−(6+r(L))=24−r(L).                 (7)

Locally K_L has dimension four at a uniform node and three at a nonuniform node. Both J_L and K_L are annihilated by the reduced ideal of the six nodes; these are actual semisimple skyscraper sheaves, not arbitrary finite-length modules.

## 4. The full module splitting persists without an Ext² shortcut

Tensoring the surface normalization sequence with L gives

    0→L→ν_*ν*L→T⊗L→0.

Under ν*L≅O_X its last map factors through restrictions to the same sixty reduced points W. Therefore the precise argument of PR579 still applies: split Rπ_*O_X as O_B⊕N[−1] on the smooth curve B. Its map to π_*O_W has zero component on N[−1], since

    Ext¹_B(N,π_*O_W)=H¹(B,N^∨⊗π_*O_W)=0.

Composing with the weighted residue map defining L and applying the exact functor h_* preserves that zero. Thus, as complexes of O_Γ-modules,

    Rg_*L ≅ C_L ⊕ h_*N[−1],
    C_L=[h_*O_B --d_L--> V_L],                       (8)

with the two terms of C_L in degrees zero and one. The isomorphism is an existence statement; no canonical choices of cones or null-homotopies are asserted.

There is a direct splitting argument for C_L even when A_L is not invertible. The sequence of skyscraper sheaves

    0→J_L→V_L→K_L→0

splits as O_Γ-modules: independently at each node it is an exact sequence of vector spaces on which the maximal ideal acts by zero. Choose a complement and identify V_L=J_L⊕K_L. The differential d_L lands in J_L, so

    C_L ≅ [h_*O_B→J_L] ⊕ K_L[−1].

The first complex has only degree-zero cohomology A_L by (5), and its natural inclusion from A_L is a quasi-isomorphism. Consequently

    Rg_*L ≅ A_L ⊕ K_L[−1] ⊕ h_*O_B(−5)[−1].         (9)

In particular

    R¹g_*L ≅ K_L⊕h_*O_B(−5),     R^ig_*L=0 (i≥2).   (10)

The torsion subsheaf in R¹g_*L is exactly K_L, because the other summand is torsion-free. This is an intrinsic torsion statement even though the complementary summand is not selected canonically.

Importantly, (9) does **not** follow by asserting Ext²_Γ(K_L,A_L)=0. At nonuniform nodes A_L is the conductor module (3), not the invertible dualizing coefficient used in PR579's Gorenstein argument. The actual semisimple image splitting above proves vanishing of this particular Postnikov class without requiring vanishing of its ambient Ext group. Nor is (9) a multiplicative or flat-base-change splitting.

## 5. Cohomology conceals the descent strata

The thirty-point normalization sequence immediately computes all cohomology of L. After the chosen trivialization, its degree-zero map on global sections is

    C→C³⁰,     c↦((1−t_z)c)_z.                     (11)

It is zero exactly when every ratio is one, equivalently L≅O_S. For every nontrivial L it is injective. Using h¹(O_X)=0, h²(O_X)=4 and vanishing of positive cohomology of the finite quotient gives

    (h⁰(S,L),h¹(S,L),h²(S,L)) = (0,29,4) if L≠O_S,
                                  (1,30,4) if L=O_S. (12)

In particular ordinary cohomology dimensions do not distinguish a nontrivial descended line bundle from a non-descended one.

The derived description explains the cancellation. For nontrivial L, h⁰(A_L)=h⁰(S,L)=0, so (6) gives h¹(A_L)=5+r(L). The contribution of K_L to H¹ has dimension24−r(L), while H⁰(B,O_B(−5))=0. Hence (9) gives

    h¹(S,L)=(5+r(L))+(24−r(L))=29,
    h²(S,L)=h¹(B,O_B(−5))=4.

For L=O_S the terms are h¹(O_Γ)=6 and length(K_L)=24, giving30 as before.

More precisely, specify a subset R₀ of the six nodes and require exactly those nodes to be nonuniform. The corresponding Picard stratum is a product of copies of Gm at its 6−|R₀| uniform blocks and copies of (Gm)^5 minus the diagonal at its |R₀| nonuniform blocks. It is smooth, irreducible and locally closed of dimension

    6+4|R₀|.                                        (13)

Thus the descent subtorus is the dimension-six closed stratum; on the open dense r=6 stratum, g_*L has degree−6 and fails to be locally free at all six nodes, while the torsion in R¹g_*L has length18. The intermediate strata carry the precise transition between these extremes.

These are fiberwise statements. Across a change in r(L), the Euler characteristic of g_*L changes by (6), so the collection of these individual sheaves cannot be the fibers of a flat coherent family on Γ over a connected parameter neighborhood crossing that change. This does not assert that taking g_* of a universal Picard bundle commutes with specialization there. A universal base-change or derived-family description would require its own proof; (8)–(13) do not assume it.

## 6. Contribution and scope

This supplies an exact descent test and a complete local/direct-image classification for all algebraically trivial twists of the actual primary surface. It shows why constant global cohomology away from the identity does not detect descent: a growing curve-cohomology contribution is canceled by a decreasing finite conductor defect. It also proves that the specific derived module splitting persists beyond the locally free descent locus by a semisimple image argument, rather than by an invalid extension of the invertible-coefficient duality vanishing.

No identification is made with the full-adjoint twenty-dimensional boundary or with the original HM deformation functor. No full-Q4, prescribed-source, higher-lifting or algebraicity conclusion follows. No selected actual evaluation or large computation is used.
