# Verification details and exact mathematical limits

These arguments supplement [the proof](PROOF.md). They retain the signed, domain and effectivity qualifications of the statements, without adding a selected-instance conclusion.

## 1. Local lifts exist and can be normalized

For the algebraic rank-two bundle H on P^4, the Atiyah sequence

    0 → End(H) → At(H) → T(P^4) → 0

is an exact sequence of coherent sheaves. On each standard affine chart U_i, taking sections is exact. Every restricted global projective vector field X therefore has a regular first-order lift D_i(X). Choosing lifts for a basis of sl_5 and extending C-linearly makes the choice linear in X without requiring a Lie algebra splitting.

Fix an algebraic identification det(H) ≅ O(-1). The SL_5-linearization of O(-1) gives a regular determinant lift of X. The induced determinant operator of an arbitrary D_i differs from it by a regular scalar function f_i. Replacing D_i by D_i − (f_i/2) Id gives the desired determinant. The factor 2 is the rank of H. This correction preserves the symbol and regularity.

These are local algebraic lifts. Their existence does not imply a global holomorphic lift of X, and does not kill the orbit Kodaira–Spencer map.

## 2. Interpolation genuinely belongs to a compatible simplicial model

For an increasing nonempty index set I, use polynomial differential forms on the standard simplex with barycentric coordinates t_i, i ∈ I. The relations are Σt_i=1 and Σdt_i=0. Put

    D_I(X)=Σ_{i∈I} t_i D_i(X)|_{U_I}.

Setting a barycentric coordinate and its differential to zero gives exactly the corresponding face restriction. Consequently these operators are compatible with the Thom–Whitney face conditions. No partition of unity is needed.

The operator a_I=d_ΔD_I=Σdt_i D_i is order zero: its symbol is (Σdt_i)X=0. Its trace is zero, since every D_i has the same determinant lift and the same cancellation applies to the determinant operators. Hence a=(a_I) is a closed trace-free degree-one Thom–Whitney cochain.

On an oriented edge i<j, integration gives D_j−D_i. This is the Čech connecting cocycle for the Atiyah extension, with the declared δD_{ij}=D_j−D_i convention. Its identification with the orbit tangent has the usual common sign convention for pullback by automorphisms; any imported convention must be kept consistent.

## 3. The twist action has one base derivative

The operator on End(H)⊗O(k) is the balanced tensor combination of the induced End(H) operator and the canonical infinitesimal SL_5 action on O(k). In local frames it is

    L_X = X + ad(Γ_I(X)) + λ_{X,k},

not a sum containing two copies of X. The line action is compatible with multiplication in k. Its coefficient has no simplex dependence. Therefore L_X is a degree-zero derivation of the entire twist-graded Thom–Whitney DGA, preserves trace-free cochains, and satisfies

    dL_X−L_Xd=ad(a_X),     da_X=0.

The operator does not generally commute with d. It therefore does not induce an sl_5 action on fixed-fiber cohomology by itself.

## 4. The scalar primitive is a finite regular algebraic operation

Let I be simplex integration, W the Whitney extension, and K the Dupont homotopy with sign normalized by

    IW=id,     id−WI=dK+Kd.

All three maps are maps of complexes or homotopies of complexes. Neither I nor W is asserted to preserve products. The Whitney–Dupont contraction is standard; see Fiorenza–Iacono–Martinengo, §3, [arXiv:0904.1301](https://arxiv.org/abs/0904.1301).

Lunardon, [Some remarks on Dupont contraction](https://arxiv.org/pdf/1807.02517), Definition 2.1, Construction 3.6, Theorem 3.8, and Remark 3.9, uses dh_D+h_Dd=WI−id. Thus K=−h_D has the required sign. Simplicial naturality gives face compatibility and the side conditions give K²=IK=KW=0. These side conditions are not needed for the primitive identity.

For the previously proved regular scalar Čech contraction h_k, at k=0,−1,−2, define

    T_k=K+W h_k I.

Using that I and W commute with the differentials gives

    dT_k+T_kd=id−WιπI.

The projection term is concentrated in degree zero. Thus dT_kρ=ρ for every closed scalar degree-two cochain ρ, and likewise for every closed scalar degree-one cochain. This proves both existence of the required primitives and scalar exactness of their differences.

Finite regularity is literal: there are only finitely many intersections; each coefficient has finite algebraic support; W uses finitely many face restrictions; I and K integrate polynomials in auxiliary simplex parameters; h_k uses the regular Laurent-monomial insertion rule. Auxiliary integration produces scalar rational constants and does not introduce poles in base coordinates. There are no analytic integrals, infinite series, completions, or Green operators in this construction.

The operator is C-linear. It is not claimed to be S-linear, multiplicative, invariant under all projective coordinate changes, or a natural canonical choice independent of normalization.

## 5. Rank-two identities and every sign in the elimination

For odd trace-free cochains x,y in the Thom–Whitney DGA, graded-commutativity of the scalar form coefficients and the rank-two matrix identity imply

    (xy)_tf = B(x,y) = (xy+yx)/2,
    tr(yx)=−tr(xy).

This assertion is local in any frame and hence glues. Its proof is a universal matrix identity over a graded-commutative coefficient ring, not an evaluation on bundle data.

Let a=a_X and let b,c be closed trace-free degree-one inputs. Write

    t_bc=T(tr(bc)/2),     t_ab=T(tr(ab)/2).

Then d(L_Xb/2)=B(a,b), so h_ab=L_Xb/2+t_ab Id is an ordered primitive of ab. When bc is exact, choose any primitive and take its trace-free part q_bc; it obeys dq_bc=B(b,c). Then h_bc=q_bc+t_bc Id is an ordered primitive of bc.

With the convention m(a,b,c)=[a h_bc+h_ab c], the trace-free defining cocycle is

    M_tf=B(a,q_bc)+(1/2)B(L_Xb,c)−t_bc a+t_ab c.

The negative sign is essential: a t_bc=−t_bc a because both factors are odd. The derivation and Cartan identities give

    dL_Xq_bc=B(L_Xb,c)+B(b,L_Xc)+2B(a,q_bc).

Subtracting half this exact differential gives

    C=−(1/2)B(b,L_Xc)−t_bc a+t_ab c,
    M_tf=C+(1/2)dL_Xq_bc.

Thus C is closed and represents the trace-free defining Massey class. Every freely selected End-valued pair primitive disappears from the final formula. The End-valued derivative L_Xc remains. The scalar target H^2(O(k)) vanishing identifies the trace-free class with the full class at the stated lower and upper target twists.

Zero indeterminacy is an additional imported hypothesis, not a consequence merely of the pair products being exact. Under that hypothesis the represented Massey class is the unique canonical one. The individual derivative and scalar summands need not be closed; no separate cohomology classes may be assigned to them without further proof.

## 6. Genuine multiplicative comparison

A safe comparison uses the following actual DGA maps:

    TW_alg → TW_hol → TW_Čech-Dolbeault ← A_global-Dolbeault.

The first two maps are induced by inclusions of coefficient sheaves. The last sends a global Dolbeault form to its compatible restrictions, constant in the simplex coordinates. All preserve products strictly. For coefficients with internal Dolbeault degree q and simplex degree p, the differential is d_Δ+(−1)^p bar-partial; the tensor product multiplication carries its usual Koszul sign.

Integration may be used to prove these arrows are quasi-isomorphisms of the underlying complexes. Weightwise affine algebraic Čech acyclicity, Stein analytic Čech acyclicity, GAGA, the Dolbeault resolution, and fine-sheaf Čech acyclicity prove the needed comparisons. The cover has five members and all relevant double complexes are bounded in the Čech direction, so no convergence or completion issue is hidden. The simplicial connection and extension-cocycle viewpoint also agrees with the construction in Lepri, §2, [Cyclic forms on DG-Lie algebroids and semiregularity](https://ems.press/content/serial-article-files/47074).

To identify with the pre-existing ordered algebraic Čech Massey product, append the genuine DGA zigzag already proved in the scalar note:

    A_global-Dolbeault → Tot_Čech-Dolbeault ← Čech_hol ← Čech_alg.

Preservation of Massey products under this DGA zigzag, with the imported zero-indeterminacy hypothesis, identifies the classes. No multiplicativity of simplex integration is used or needed.

After this identification, I(C) is a finite regular algebraic Čech two-cocycle representing the same natural cohomology class. It is not a formula obtained by integrating each factor separately and multiplying with the ordered Čech cup product.

## 7. Exact effectiveness boundary

The construction is a finite algebraic recipe once regular representatives b,c and determinant-normalized local lifts D_i are supplied. Ordinary algebraic Čech representatives can first be sent to TW by the linear Whitney map W; its failure to be multiplicative is irrelevant to choosing representatives.

The proof makes trace-free preparation explicit. For any closed ordinary Čech one-cochain b_0 at an allowed input twist, set s_b=h(tr b_0)/2 and b_0′=b_0−δ(s_b Id). Since δ tr b_0=0 and the scalar degree-one contraction gives δh tr b_0=tr b_0, the trace of b_0′ is zero. This is a cohomologous regular cocycle. Wb_0′ is closed and trace-free because W is a chain map commuting with trace. The same argument applies to c_0. This preparation uses no multiplication compatibility for W and evaluates no instance data.

The universal existence of local lifts is proved, but no particular source presentation, local trivialization, or input representative has been constructed here. No complexity bound, denominator bound, canonical coordinate-free contraction, strict S-linearity, PGL-equivariance, or executable implementation for the actual bundle follows from the formal recipe alone.

The result evaluates no Massey value and proves neither vanishing nor nonvanishing. It removes no symmetry-eligible coefficient or parameter. It strengthens the earlier abstract comparison by supplying a regular algebraic reduced cocycle with a finite scalar homotopy.
