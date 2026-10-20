Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Independent audit: the declared product root and the actual source frames

## Verdict and evidence boundary

The product-root construction and its concrete source-frame arrow are correct for the explicitly declared model. The key identification is not the name Theta: the authenticated ext-model document explicitly declares N to be the exterior product of the four degree-one origin line bundles, and f to be the product x-map followed by the fourth symmetric quotient. The pinned scalar-proof README links that precise model. The actual source's unequal cohomology column scalings then give its exact reciprocal-root transition matrix.

This review independently reads the root proof, homogeneous primitive proof, full structural primitive-A proof, determinant-volume proof, first-order source, and raw source text. It also independently fetches the ext-model document through the GitHub connector at commit add03476d9055aa00e1e00778eea6332cf8e01cc. Its Git blob is fad0e87f0e30ec916e18fd47feea584c7d8eaae6; the exact fetched text is preserved here. The accompanying control script parses inert Python AST and performs integer exponent tests only. No source module is imported or executed, no physical source is evaluated, no actual matrix or polynomial product is computed, and no occurs.

The reviewed homogeneous and structural-A results remain dependencies, rather than being re-proved by this small checker. This does not identify an arbitrary earlier deformation problem with the declared one, prove a terminal obstruction value, or certify the entire arithmetic/jet/HPL pipeline.

## 1. The root line is specified, not inferred from its square

On C: y²=x³−x, let O be infinity and T_a=(a,0), a=0,±1. With the divisor-sheaf convention, the divisors are

    div(x)=2T_0−2O,
    div(y/x)=T_1+T_−1−T_0−O.

For N_C=O_C(O), e0=1 is a frame on U0=C minus O. The section e1=y/x has section divisor T_1+T_−1−T_0 and is a frame on U1=C minus {T_0,T_1,T_−1}. These opens cover C. Their overlap in the finite chart is the localization by x(x²−1); the full transition e1/e0=y/x is an invertible regular function there.

At infinity set t=1/x, z=y/x², so z²=t(1−t²). The parameter z has order one, t order two. With s=1−t², a genuine frame of N_C on U1 is n∞=1/z and e1=s n∞. Thus the pole of y/x as a rational function is precisely absorbed by the line bundle; e1 has no zero at infinity. At T_±1 e1 does have a zero, and at T_0 it has a pole. None of those points belongs to U1. Ignoring these exclusions would make the frame claim false.

The exact source frames and their exact transitions specify O_C(O). Knowledge of N_C² alone would not: two-torsion twists can have the same square. On X the authenticated external-product declaration specifies N, and the product e_m=∏e_(m_i) provides its actual frames. There is no residual inference from an unspecified symbol Theta.

## 2. The old squared frame and actual root square differ by a unit

For the x-map with x=X/Y, identify x*O(1) with O_C(2O) by Y↦1 and X↦x. Let ℓ0=1 and ℓ1=x. Then

    ℓ1=x ℓ0,
    e0²=ℓ0,
    e1²=(1−x⁻²)ℓ1.

The final factor h=1−x⁻² becomes s=1−t² and is a unit on U1. Setting it to 1 would incorrectly identify the refined e1-square with the old squared frame.

The connection induced by making ℓ_m flat has coefficient γ0=0 and γ1=(1/2)dlog h=dx/[x(x²−1)] in the actual e_m frame. Transporting to e0 subtracts dlog(y/x), giving −(1/2)dlog x. Therefore the product difference on N^k is

    −(k/2) Σ_r (m_jr−m_ir)dlog x_r.

Evaluation on the actual invariant V_r gives −k q_ij,r/2. In particular the source's old coefficient γ and logarithmic derivative of ν are genuinely different. At infinity γ1=−t dt/(1−t²); it is regular in the retained actual frame and must not be replaced with zero. The full vector field there includes its z-component; −z∂t alone is only shorthand on t-dependent functions.

## 3. The square-line and coefficient-map identification is global

On (P1)^4, the coefficients v_j of ∏(Y_i+X_i z) are sections of O(1,1,1,1) with no common zero: a product of four nonzero linear binary factors is a nonzero polynomial at every point. The morphism f consequently has

    f*O_P4(1) ≅ external-product x*O_P1(1) ≅ N².

This is an actual line-bundle isomorphism with the specified section conventions. Pulling back O(d) and tensoring N gives N^(2d+1), so the four homogeneous terms have powers −1,1,3,5.

On a standard chart with infinity subset S, let τ=∏_(i∈S)t_i and ℓ_S=(∏_(i∈S)x_i)e0². Then v_S=τv_finite and ℓ_S=τ⁻¹ℓ_finite. For a legal mask m define the actual squared ratio

    h_m,S=e_m²/ℓ_S.

It is a unit on the legal/standard-chart intersection. Its one-factor values are (1,(x²−1)/x) on a finite chart and (t,1−t²) on an infinity chart, in bit order 0,1. The factor t in bit 0 is only used on U0, which excludes infinity. Thus no zero at a permitted point is concealed.

Changing standard charts multiplies both the homogeneous coordinate vector and h by τ. All physical block combinations have homogeneous degree d and integer h exponent p with d+p=0. Consequently they agree as actual coefficients. This proves the required chart comparison without choosing a square-root function of τ. A formula such as ν_B=√τν_A is useful formal bookkeeping only; it is not the definition of an algebraic root-frame transition.

## 4. The exact source G is a quotient-frame transition

The homogeneous contraction is onto C0=O⊕O(−1). Pullback and tensor N gives genuine maps

    I_c:N⊕N⁻¹ → N^15,
    P_c:N^15 → N⊕N⁻¹.

The reviewed homogeneous primitive theorem makes these maps regular on their own carrier, and the reviewed structural-A theorem supplies the contraction and quotient identities. On carrier c and legal chart m, use the actual domain basis (e_m,e_m⁻¹). Its image under I_c is a genuine quotient basis β_c,m. This construction already works at branch points and infinity wherever the legal/carrier open contains them.

Relative to the finite rational reference e0, write e_m=ν_m e0. The source's degree-zero splitting has cohomology columns [I_c,0,ν_m⁻²I_c,1] in the ambient e_m frame. Multiplying by that ambient frame gives

    β_c,m = e0 I_c D_m,    D_m=diag(ν_m,ν_m⁻¹).

This is the crucial source-specific arrow. The source's two columns have different scalings. Replacing both by a common scaling would change the bundle frame and fail this identity.

The quotient identity I_j−I_iP_iI_j∈im γ now gives

    β_j=β_i G_ij,
    G_ij=D_i⁻¹(P_i I_j)D_j.

For row coordinates the transition is

    g_ij=G_ij^t=D_j(P_iI_j)^tD_i⁻¹,
    g_jk g_ij=g_ik.

This is exactly the inspected raw_engine.g expression, including transpose order and inverse placement. Equivalently, in each owner's ambient e frame the cross-comparison includes the scalar ν_j/ν_i; omitting that ambient change would give the wrong transition. The construction uses equality modulo im γ, not an unjustified literal equality of inclusion images.

The actual intrinsic basis construction proves regularity and invertibility on legal overlaps. The finite displayed formula identifies those regular transitions there and hence as rational functions. This is stronger than attempting to infer extension of an arbitrary rational matrix from its dense-open identity.

## 5. Determinant identification and normalization are separate

The determinant line of the physical complex has exponent

    −5(−1)+15(1)−10(3)+2(5)=0.

Fixed ordered bases for the constant vector spaces therefore give a determinant-line trivialization. This establishes triviality and fixes a reference; it does not by itself certify that arbitrary local quotient bases have unit volume.

For the actual stored bases, the reviewed sparse determinant-volume theorem proves the ordered split ratio det(U0)/det(U1)=1, after the structural contraction theorem has discharged its former A premise. The physical column-scale determinant exponents are both 4:

    U0: −2·5+0−2+2·8=4,
    U1: 0·8+2·2=4.

They cancel in that ratio. Likewise det D_m=1. Hence the actual quotient frames have the prescribed volume and det G_ij=det g_ij=1. No extra local determinant renormalization is introduced. The argument respects the specified cohomology-block order and inherits its orientation from the determinant-volume proof.

Trivial determinant alone would allow a local GL2 re-gauge of determinant 2 and would not force the stored transition determinant to be 1. The sparse normalization result, not the exponent count, excludes that counterexample.

## 6. Controls and scope of closure

check_formal_exponents.py passes both normally and with python -O. It uses explicit exceptions rather than removable assertions. It binds the exact raw g/w0/w1 AST, checks root ratio text, four term weights, 12 squared-ratio covariance pairs, both determinant exponents, and the exact independently fetched document blob. Eight deliberately wrong variants are rejected. It never instantiates a source matrix.

The producer's complete PROOF.md was subsequently read against this independent derivation. No mathematical correction is required. Its additional carrier-cover proof and bounded deck-line consequence also check: the odd one-factor basis has transition t², hence the full-sign degree-r coefficient line on (P1)^4 is O(r−2,r−2,r−2,r−2). A particular residual still needs independent membership and degree attribution. The producer correctly states this limitation and the ramification distinction between factor powers and divisor valuations on X.

The producer checker was inspected in full and independently replayed normally and under python -O. The two outputs are identical: all 13 source and 5 dependency pins pass, 5 Python AST contracts and 8 JavaScript contracts pass, all 8 active mutation controls reject, and the 256 legal/standard exponent cases pass. These are static/exponent checks, not 256 physical matrix evaluations. The outputs are producer-normal.json and producer-optimized.json here.

The newly closed arrow is the declared product geometry → actual N and N² identification → actual legal/source quotient frames → exact stored G, with the retained old connection and determinant normalization. The remaining arithmetic/jet semantics, higher source residual comparisons, terminal detector values and global deformation conclusions are not established here.
