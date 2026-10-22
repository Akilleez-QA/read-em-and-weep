# N-W supported coefficients give a fully U-annihilating source family

## 1. Full exterior identity, not a principal-column approximation

Use the normalized physical conventions of public [PR741](https://github.com/Akilleez-QA/read-em-and-weep/commit/eace951d98b0c5adb0462cb2d93c09eac5b08b8b) and the coefficient embeddings of public [PR730](https://github.com/Akilleez-QA/read-em-and-weep/commit/a79c896439bc141dcb07a8891ba391ee8b38fcc9). All its source/Clifford dependencies remain unchanged. Put j=(-w,u), N=-2j(u,w), and let E_r denote positive wedge by the polar covector r. Here K is in the **physical** six-space coordinates of the exterior forms. For an arbitrary such coefficient K set

    Q_r(K)=K E_r+E_r up Adj_6(K) low.

For any closed rank-two-valued two-form F, the **entire** supported action of K tensor N is

    L_N(K,r)F = -2 {i_v Q_r(K)(i_v F_VV)} wedge j.       (1)

The braces mean: identify i_v F_VV with its six-vector, apply Q_r(K), recover the positive two-form, and contract by v. No derivative acts on K or on r.

Proof. The full assembly before contraction is

    Q_r(K) sum_i N[j,i]Y_i,

because tr(N)=0. Closure gives sum_i w_iY_i=i_v F_VV, so the primitive is -2 Q_r(K)(i_v F_VV) wedge j. Contracting by x gives (1) since i_w j=0. This retains both K and its determinant adjoint. It holds before taking any source quotient.

The generic verifier uses all36 independent K entries, all3 polar entries, and an arbitrary20-coefficient contracted three-form. It verifies (1) and both full source vanishings below. No actual matrix is evaluated.

## 2. Exact source balance and composition

The normalized actual A column satisfies i_v A=0, and B has no VV part. Therefore

    L_N(K,r)A = L_N(K,r)B = 0.                           (2)

The exact c-column change is (1) with F=C, multiplied by its physical c_m and by any common k_At/probe scaling of the entire operator. There is no induced U-source or Euler correction. The output is mixed VW only, with no VV or WW piece.

Moreover, any two such supported actions have zero composition on closed inputs: the first output is closed, being a contraction, and has zero VV component. Applying (1) again gives zero, irrespective of the second K and polar. This is an exterior-operator identity on closed inputs, not an obstruction-vanishing claim.

Since the full U columns remain unchanged, adding these actions does not change the canonical principal-U, full-B, or mixed-U reconstruction of a previously chosen operator. It also leaves the reconstructed **low** c companion unchanged. Its own c contribution has positive/negative bidegree(3,2): the positive polar has degree1, i_v C_VV has degree(1,1), the outer contraction adds positive degree1, and j adds negative degree1. The K coefficients used below have no coordinate dependence. Thus only the retained high mixed c equation is changed. The principal-c quotient and all earlier necessary scalar tests remain separate.

## 3. Explicit18+5 coefficient channels

Let D be the negative binary quadratic parameter, H the positive D5 input, and f the actual invertible G-equivariant cubic marking with no scale assigned. The base-degree-two coefficient N is already provided by the negative coordinates. Consequently the remaining K coefficient spaces are

    Rq: Hom_G(D5 tensor Sym²A, End(C+U)),
    Rh: Hom_G(Sym²A, End(C+U)).

Here Rq uses the physical q-polar r, and Rh uses the matching H-polar r_H. Since

    Sym²A = 1+D5,
    D5 tensor Sym²A = 1+A+V+2P4+3D5,
    End(C+U) = 2·1+A+4V+P4+3D5,

their dimensions are18 and5. These are supported **coefficient** dimensions. No independence after exterior action or on the actual monad is asserted.

The companion helper constructs them explicitly. Write

    d=kS²-2hST-lT²,   Delta=h²+kl,
    qD=quartic(f op4(d²) f^-1),   qH=quartic(H0).

Conjugation by the symplectic marking preserves the trace-free adjoint-even5-space, so op4(qD)=f op4(d²)f^-1. This full polynomial identity is checked with all three nonzero marking scales unassigned.

For Rh use the two scalar embeddings of Delta and the three D5 embeddings of qD. For Rq use the three D5 embeddings of Delta qH; additionally take every transvectant (qH,qD)_r for r=0,...,4, project/bridge its binary degree8,6,4,2,0 to the canonical G-types using the public PR730 maps, and apply every six-space coefficient embedding. The counts are

    3 + (4+2+3+4+2) = 18,       2+3=5.

Completeness follows without a numerical rank. The negative scalar Delta and Cartan square d² realize the two inequivalent summands of Sym²A. Transport of the latter is an isomorphism onto the positive D5 realization. Clebsch decomposition of B4 tensor B4 gives all degrees8,6,4,2,0; the pinned nonzero multiplicity-free bridges and sextic projections supply every G-component, including both P4 copies and both D5 copies from that product. Distinct Clebsch summands remain independent as source maps. Adding the Delta qH summand supplies the third D5 copy. Applying all pinned target embeddings gives the stated Hom-spaces.

The emitted K matrices are in balanced Cartan4+Spin2 coordinates, whereas equation(1) uses physical positive-form coordinates. Retain the fixed conversion

    B6=(Kinc Pstd | spin),
    K_physical=B6 K_balanced B6^-1,
    B6^t J6 B6=diag(-J3/2,-J1/3).

The helper `physical_six_coefficient` implements this conversion, and `n_w_balanced_closed_action` performs it before equation(1). The physical `n_w_closed_action` must not receive a balanced matrix directly. The test checks the generic36-entry adjoint transport, not just the two coordinate dimensions.

All23 coefficients have exactly degree2 in D; Rq is linear in H and Rh independent of H. Multiplying by N supplies precisely negative coordinate degree2. The helper emits their6×6 K matrices and evaluates their full closed-input action by (1), avoiding a principal-only truncation.

## 4. Scope and reproducibility

Run `python verify_n_w_source_balanced_family.py`. The checker proves the all-free-symbol exterior identity, full A/B zero, exact transported quartic, all23 nonzero coefficient formulas and degrees, and character counts. It checks the displayed square-zero composition consequence; the proof gives pairwise zero composition.

This is a constructive family available for the remaining high c equation. It does not claim that its image survives source equivalence, that it is independent of the existing140 supported operators on the monad, that it solves that remaining equation, or that it computes the fourth Bockstein. All physical scalar multipliers must be retained when this family is combined with an actual ambient operator.
