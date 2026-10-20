# Regular algebraic Thom–Whitney reduction of the orbit Massey class

Reused context: §1, the opening I,W,K construction of §2, and the model comparison of §6 occur in [the ordinary TW model](https://github.com/Akilleez-QA/read-em-and-weep/blob/838dbe4a9ddaee5ca20eae14944e3908ea89079d/research/hm/cubic-loci/foundation-p06/TW-MODEL.md). They are retained here to prove the full reduced formula. The finite algebraic construction below is independent of choosing an inverse to analytification. See [Dependencies](DEPENDENCIES.md).

## 0. Result and scope

Let H be the given algebraic rank-two bundle on P^4 over C, with a fixed identification det(H)=O(-1). Use the standard ordered affine cover U_i=D_+(x_i), 0≤i≤4. Assume the already-established ordered pair-product vanishings and zero Massey indeterminacy for the lower and upper patterns. There is a regular algebraic Thom–Whitney (TW) model in which the reduced formula is literally valid:

    C(X;b,c)=−(1/2)B(b,L_X c)−t_bc a_X+t_Xb c,
    t_pq=(K+W h I)(tr(pq)/2).                         (A)

Here a_X is an algebraic TW representative of the orbit Kodaira–Spencer class, b,c are closed trace-free TW degree-one representatives, B(u,v)=(uv+vu)/2 for degree-one trace-free arguments, and h is the [regular scalar Čech contraction](https://github.com/Akilleez-QA/read-em-and-weep/blob/20ccf2fe64240e3c5d5c30f3d85455eca16aae04/research/hm/reduced-massey/regular-scalar-cech-contraction/PROOF.md) at twists 0,−1,−2. The operators I,W,K are specified below, with

    IW=id,       id−WI=dK+Kd.                         (B)

Formula (A) is a closed regular algebraic TW cochain representing the canonical triple Massey class. No End-valued pair primitive occurs in its prescription. A hypothetical such primitive is used only to prove the identity with the defining-system class.

This is an algebraic construction in a graded-commutative-coefficient model, not an assertion of strict identities in ordered Čech cochains. It gives a finite-expression procedure once algebraic local lifts and input representatives have been chosen and supplied. It does not supply their coordinates from the source bundle, any fixed complexity/degree bound, a source-matrix algorithm, or an evaluated Massey value. The model itself remains infinite-dimensional.

## 1. The precise model

For an increasing nonempty subset I={i_0<...<i_n}, put U_I=∩U_i and let

    Ω_I=C[t_i,dt_i : i∈I]/(Σt_i−1,Σdt_i),

with |t_i|=0, |dt_i|=1, d(t_i)=dt_i. The d in this section differentiates only simplex variables, not algebraic functions on U_I. For E_k=End(H)⊗O(k), let A_k be the set of families

    α_I ∈ Ω_I⊗_C Γ(U_I,E_k)

compatible with every face inclusion: restricting to t_j=dt_j=0 agrees with restricting the component on I\{j} to U_I. There are finitely many I. Define A=⊕_k A_k with componentwise wedge/composition and differential d. Scalar families define the analogous A^sc_k, acting centrally with the graded sign. All tensor products here are algebraic, so every component has finite polynomial simplex support. Trace and the splitting

    End(H)=End_0(H)⊕O·Id,    p_tf(z)=z−tr(z)Id/2

are maps of the corresponding complexes. Products add twists.

The coefficient ring Ω_I⊗O(U_I) is graded commutative; End(H) itself is not commutative. Thus graded trace cyclicity and the polarized rank-two matrix identity apply locally in a frame and hence globally. In particular, for trace-free degree-one u,v,

    uv−vu=tr(uv)Id,      (uv)_tf=(uv+vu)/2=B(u,v),
    tr(vu)=−tr(uv).

These are universal identities over the graded coefficient ring. They are not claimed for the ordered Alexander–Whitney Čech cup product.

## 2. Scalar contraction with fully fixed signs

Let C^q(k)=∏_{|I|=q+1}Γ(U_I,O(k)) with the ordinary alternating Čech differential δ. Define I:A^sc_k→C^•(k) by integrating the degree-q component on its q-simplex, oriented in increasing vertex order. Polynomial integration is algebraic in characteristic zero. Define W on a q-cochain z by

    (Wz)_I=Σ_{J⊆I, |J|=q+1} ω_J z_J|_(U_I),
    ω_J=q! Σ_{r=0}^q (−1)^r t_(j_r)
                    dt_(j_0)...omit(dt_(j_r))...dt_(j_q).

Then I and W are chain maps and IW=id. Use the simplex-natural Dupont homotopy with the sign convention (B). More precisely, if h_D denotes Construction 3.6 and Theorem 3.8 of Lunardon, whose convention is dh_D+h_Dd=WI−id, set K=−h_D componentwise. Face naturality makes this an operator on the compatible families. Its side conditions give K²=IK=KW=0, though the primitive construction needs only (B).

Reference for the exact polynomial formula, signs, naturality, and side conditions: Luigi Lunardon, *Some remarks on Dupont contraction*, §§3–4, especially Construction 3.6, Theorem 3.8, and Remark 3.9, https://arxiv.org/pdf/1807.02517 . This specifies K rather than leaving an arbitrary homotopy to choose. The semicosimplicial passage to I,W,K is also recorded by Fiorenza–Iacono–Martinengo, *Differential graded Lie algebras controlling infinitesimal deformations of coherent sheaves*, §3, https://ems.press/content/serial-article-files/31821 . Their homotopy sign likewise requires negation for (B).

Use h:C^q(k)→C^(q−1)(k) from the [scalar Čech proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/20ccf2fe64240e3c5d5c30f3d85455eca16aae04/research/hm/reduced-massey/regular-scalar-cech-contraction/PROOF.md): on a homogeneous Laurent monomial x^α of weight k∈{0,−1,−2}, insert j(α)=min{i:α_i≥0}, with alternating sign. It satisfies

    δh+hδ=id−ιπ,

where π is the scalar degree-zero projection described there. Set

    T_k=K+W h I : A^sc_k→A^sc_k[−1].

A direct calculation, with no multiplicativity assumption, gives

    dT_k+T_kd
      =(id−WI)+W(δh+hδ)I
      =id−WιπI.                                      (C)

The last term vanishes on every positive-degree input. Consequently, for a closed scalar two-cochain ρ,

    t=T_kρ,       dt=ρ.                               (D)

A closed scalar one-cochain w has w=dT_kw. Thus changing scalar primitives changes them by an explicitly algebraic scalar boundary. Linearity makes t_pq=T_k(tr(pq)/2) bilinear and t_qp=−t_pq for closed odd inputs. This antisymmetry is valid here because the TW scalar trace identity is strict before T is applied.

No step identifies I with an algebra map. In particular I(pq) must not be replaced by Ip∪Iq, nor W(z∪w) by Wz·Ww.

## 3. Algebraic local lifts with prescribed determinant

Let X∈sl_5 act as its projective algebraic vector field on P^4. Fix its genuine holomorphic/algebraic linearized differential operator D_X^(k) on O(k) for every k, compatible with tensor multiplication. In particular D_X^(−1) is the prescribed determinant-line lift. The use of sl_5 fixes the linear lift of the projective vector field. These line operators have symbol X; no Chern horizontal lift is involved.

The algebraic Atiyah sequence

    0→End(H)→At(H)→T_(P^4)→0

is an exact sequence of locally free sheaves: local frames split the symbol map. On an affine U_i, H¹(U_i,End(H))=0, so its section sequence is surjective on the right. Thus the restricted vector field X has a regular first-order bundle lift D^0_(i,X). Choose such lifts linearly in X, for example by lifting a vector-space basis of sl_5 and extending linearly. No Lie bracket preservation is required or asserted.

The induced determinant operator det(D^0_(i,X)) and D_X^(−1)|_(U_i) have the same symbol, so their difference is multiplication by a regular function f_(i,X). Define

    D_(i,X)=D^0_(i,X)−(f_(i,X)/2)Id_H.

Subtracting a scalar f/2 from a rank-two bundle operator subtracts f from its determinant operator. Hence

    det(D_(i,X))=D_X^(−1)|_(U_i).                      (E)

This establishes local existence without assuming the bundle is trivial on U_i and without requiring a global algebraic connection. Regularity of derivatives on intersections follows from the localization rule for derivations; X need not integrate to an action preserving each chosen U_i.

On U_I interpolate

    D_(I,X)=Σ_(i∈I) t_i D_(i,X).

Its symbol is X since Σt_i=1. On a face it is exactly the interpolated operator for the remaining indices. It is therefore a compatible simplex-polynomial bundle operator. There is no derivative of simplex variables in D_(I,X).

## 4. The global derivation and the KS cocycle

On End(H), D_(I,X) induces the usual commutator derivation. On its O(k) twist combine this with D_X^(k) by the balanced tensor rule. This gives a degree-zero derivation L_X of A, leaving the simplex forms fixed. Locally, in a bundle frame and a line frame, it reads

    L_X = X + ad(Γ_(I,X)) + λ_(X,k),
    Γ_(I,X)=Σ_i t_i Γ_(i,X).

There is exactly one base derivative X, not one per tensor factor. The λ_(X,k) are regular on the local frame domain and independent of simplex variables. They add under tensor products, so L_X is a derivation of the whole twist-graded algebra. It preserves trace in the precise sense

    tr(L_X z)=D_X^(k)(tr z)

on a twist-k cochain. In particular it preserves trace-free cochains.

Define the degree-one bundle operator

    a_(I,X)=[d,D_(I,X)]=Σ_i dt_i D_(i,X).

Its symbol vanishes because Σdt_i=0, so it is an End(H)-valued form rather than a first-order operator. Equivalently, after choosing any r∈I,

    a_(I,X)=Σ_i dt_i(D_(i,X)−D_(r,X)).

This makes its regularity and order-zero nature explicit. This expression is independent of r. It is also frame independent: the common inhomogeneous frame-change term in every Γ_(i,X) is multiplied by Σdt_i=0. Face compatibility follows directly. Equation (E) implies tr(a_X)=0 because the determinant operators are all the same. Thus a_X∈A^1_0(End_0 H) is globally defined. Direct differentiation gives

    da_X=0,       [d,L_X]=ad(a_X).                    (F)

Here ad(a_X)z=a_Xz−(−1)^|z|za_X. Locally (F) is simply [d,X+adΓ+λ]=ad(dΓ); dX=dλ=0 in the simplex differential. This also verifies the signs without treating a first-order operator as an ordinary scalar matrix.

On the oriented edge {i<j}, t_j is the positively oriented coordinate and

    a_X=dt_j(D_(j,X)−D_(i,X)),
    (Ia_X)_(ij)=D_(j,X)−D_(i,X).                     (G)

The right side is the Čech connecting cocycle for the Atiyah sequence and the vector field X. It is the orbit Kodaira–Spencer class with the convention that this connecting map defines the tangent of pullback; replacing the orbit parameter convention by its inverse reverses both occurrences consistently. Thus the construction represents exactly the intended orbit input, with an explicit sign convention. Normalizing the determinant has removed its scalar part, consistent with the globally lifted determinant line.

Changing the normalized local lifts changes a_X by d of the globally compatible interpolated order-zero difference. Therefore its class is independent of those choices. No claim that L_X commutes with d, or induces a Lie action on cohomology, is made.

## 5. The reduced algebraic Massey identity

Take a=a_X, and closed trace-free b,c∈A¹ in the required twists. For the lower pattern the remaining twists are 0,−1; for the upper pattern they are −1,−1. Scalar products needed below have twists in {0,−1,−2}. Define t_bc and t_ab by (D), and set

    h_ab=(1/2)L_Xb+t_ab Id.

From (F), dL_Xb=ab+ba. The rank-two identity therefore gives

    dh_ab=B(a,b)+tr(ab)Id/2=ab.

For proof only, choose any h_bc with dh_bc=bc, which exists by the imported pair-product vanishing in this DGA model. Replace its scalar part by t_bc; this preserves its differential. Write h_bc=q_bc+t_bc Id, where q_bc is trace-free and

    dq_bc=B(b,c).

The defining Massey cocycle with this convention is a h_bc+h_ab c. Its trace-free part is

    M_tf=B(a,q_bc)+(1/2)B(L_Xb,c)−t_bc a+t_ab c.       (H)

The scalar sign is forced by a·t_bc=−t_bc·a. Since the scalar target H²(O(k)) vanishes, trace-free projection preserves the full Massey class.

Using the degree-zero derivation property of L_X and (F),

    dL_Xq_bc
      =L_Xdq_bc+[a,q_bc]
      =B(L_Xb,c)+B(b,L_Xc)+2B(a,q_bc).

All arguments of B in this displayed formula are degree one and trace-free; no ungraded trace identity is being imported. Substitute into (H) to obtain the exact cochain identity

    M_tf=C(X;b,c)+(1/2)dL_Xq_bc.                      (I)

Thus C is closed and represents the defining Massey class, while its formula (A) has no End-valued pair primitive. The established zero indeterminacy makes this the canonical class, independent in cohomology of representatives and normalized local lift choices. Individual summands of C are not asserted to be closed.

## 6. Multiplicative comparison, without misusing I or W

For completeness, there is a DGA zigzag from this algebraic model to the smooth Dolbeault model:

    TW_alg(E) → TW_hol(E^an) → TW_Dol(E^an) ← A_global^(0,•)(E^an).

The first two arrows are induced componentwise by analytification and inclusion of holomorphic sections into their Dolbeault resolutions. In the middle-right term use Ω_I⊗A^(0,•)(U_I,E^an), with total differential d_Ω+(−1)^p bar-partial on simplex degree p, and product sign (−1)^(qr) when Dolbeault degree q crosses simplex degree r. The last arrow restricts a global smooth form to each intersection and makes it constant in simplex variables. All these arrows are genuinely multiplicative and preserve twists and trace.

Here is why they are quasi-isomorphisms. Integration supplies natural quasi-isomorphisms of underlying complexes to the corresponding alternating Čech total complexes, by the same simplex contraction, extended with the displayed total signs. For the algebraic-to-holomorphic arrow, affine acyclicity, Stein acyclicity of the analytic intersections, and proper GAGA identify the two Čech cohomologies. For the holomorphic-to-Dolbeault arrow, each intersection is Stein, and the spectral sequence in Dolbeault degree proves the Čech total comparison. For the global-Dolbeault arrow, the fine sheaves of smooth bundle-valued forms have acyclic augmented Čech complexes, giving the other spectral-sequence comparison. The Čech/simplex directions are finite, so no completion or convergence issue arises. These arguments apply separately in each twist.

The standard scalar vanishing and ordered pair/indeterminacy vanishings therefore hold in TW as well. DGA quasi-isomorphisms preserve defined triple Massey products and their indeterminacy. Consequently the class of (A) is the same canonical class as the smooth formula and, via the already-constructed ordered Čech–Dolbeault DGA zigzag, the algebraic ordered Čech Massey class. The zigzag, rather than the nonmultiplicative integration map, justifies the comparison of Massey operations.

If an ordinary algebraic Čech cocycle representing the final class is wanted, I(C) is one, and δI(C)=0. It has finite regular intersection coefficients. This does not make I(C) the same displayed strict formula interpreted with Čech cup products, or give a preferred Čech defining system. Its canonical class is identified by the comparison above; integration is used here only as the compatible cohomology identification.

## 7. Exact finite-regularity statement

There are only 31 nonempty standard-cover subsets and their simplex dimensions are at most four. A supplied TW cochain has finitely many polynomial simplex terms on every subset. Local lifts are regular differential operators; derivations take regular functions to regular functions on each affine intersection. Their interpolation, products, trace, and L_X therefore preserve finite polynomial support and regular coefficients.

I integrates only finite simplex polynomials. W is a finite sum over faces. Dupont's K is a finite sum of compositions of polynomial pullbacks along straight-line vertex contractions, integration in an auxiliary simplex parameter, and multiplication by Whitney forms. These operations produce polynomials with characteristic-zero scalar denominators; they introduce no poles in the base variables. In the scalar line components, integration leaves regular sections of O(k), expressible by finite homogeneous Laurent sums. The monomial h preserves their regularity by the nonnegative insertion-index argument. It does not introduce infinite series. Thus T_k and C preserve finite regular expressions on all intersections.

This is a finite algebraic operator construction relative to supplied lifts and representatives. Affine acyclicity proves that suitable lifts exist; this proof does not compute them from bundle presentation data. Given an ordinary algebraic Čech one-cocycle b_0 of weight 0 or −1, first set s_b=(1/2)h(tr b_0) and b′_0=b_0−δ(s_b Id). The scalar positive-degree contraction identity gives δh(tr b_0)=tr b_0, so b′_0 is closed, trace-free, and represents the same class as b_0. Apply the same preparation to c_0. Then b=Wb′_0 and c=Wc′_0 are closed trace-free TW inputs representing the supplied classes, because W commutes with differential and trace and IW=id. Thus supplied Čech representatives need not already be trace-free, and no inverse to analytification is needed. The orbit input a_X is built independently by (G). The required ordinary Čech representatives are not computed here either. No assertion of finite-dimensionality, universal bounds, multiplicativity of W, S-linearity of h or T, projective equivariance, or computation of actual operations is made.
