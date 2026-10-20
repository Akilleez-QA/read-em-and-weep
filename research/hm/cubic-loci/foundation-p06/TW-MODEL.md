# Regular TW model and multiplicative comparison

This excerpt supplies only the regular model, simplex contraction and multiplicative comparison needed for the ordinary cubic defining cocycle. It does not import or assert the orbit-reduced Massey formula.

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

Then I and W are chain maps and IW=id. Use the simplex-natural Dupont homotopy with the sign convention id−WI=dK+Kd. More precisely, if h_D denotes Construction 3.6 and Theorem 3.8 of Lunardon, whose convention is dh_D+h_Dd=WI−id, set K=−h_D componentwise. Face naturality makes this an operator on the compatible families. Its side conditions give K²=IK=KW=0, though the primitive construction needs only id−WI=dK+Kd.

Reference for the exact polynomial formula, signs, naturality, and side conditions: Luigi Lunardon, *Some remarks on Dupont contraction*, §§3–4, especially Construction 3.6, Theorem 3.8, and Remark 3.9, https://arxiv.org/pdf/1807.02517 . This specifies K rather than leaving an arbitrary homotopy to choose. The semicosimplicial passage to I,W,K is also recorded by Fiorenza–Iacono–Martinengo, *Differential graded Lie algebras controlling infinitesimal deformations of coherent sheaves*, §3, https://ems.press/content/serial-article-files/31821 . Their homotopy sign likewise requires negation for id−WI=dK+Kd.


## 6. Multiplicative comparison, without misusing I or W

For completeness, there is a DGA zigzag from this algebraic model to the smooth Dolbeault model:

    TW_alg(E) → TW_hol(E^an) → TW_Dol(E^an) ← A_global^(0,•)(E^an).

The first two arrows are induced componentwise by analytification and inclusion of holomorphic sections into their Dolbeault resolutions. In the middle-right term use Ω_I⊗A^(0,•)(U_I,E^an), with total differential d_Ω+(−1)^p bar-partial on simplex degree p, and product sign (−1)^(qr) when Dolbeault degree q crosses simplex degree r. The last arrow restricts a global smooth form to each intersection and makes it constant in simplex variables. All these arrows are genuinely multiplicative and preserve twists and trace.

Here is why they are quasi-isomorphisms. Integration supplies natural quasi-isomorphisms of underlying complexes to the corresponding alternating Čech total complexes, by the same simplex contraction, extended with the displayed total signs. For the algebraic-to-holomorphic arrow, affine acyclicity, Stein acyclicity of the analytic intersections, and proper GAGA identify the two Čech cohomologies. For the holomorphic-to-Dolbeault arrow, each intersection is Stein, and the spectral sequence in Dolbeault degree proves the Čech total comparison. For the global-Dolbeault arrow, the fine sheaves of smooth bundle-valued forms have acyclic augmented Čech complexes, giving the other spectral-sequence comparison. The Čech/simplex directions are finite, so no completion or convergence issue arises. These arguments apply separately in each twist.

The standard scalar vanishing and ordered pair/indeterminacy vanishings therefore hold in TW as well. DGA quasi-isomorphisms preserve defined triple Massey products and their indeterminacy. Consequently an ordinary triple defining-system cocycle represents the same canonical Massey class in these models, including the algebraic ordered Čech model. The zigzag, rather than the nonmultiplicative integration map, justifies the comparison of Massey operations.

If an ordinary algebraic Čech cocycle representing the final class is wanted, I(C) is one, and δI(C)=0. It has finite regular intersection coefficients. This does not make I(C) a strict multiplicative integration formula, or give a preferred Čech defining system. Its canonical class is identified by the comparison above; integration is used here only as the compatible cohomology identification.

