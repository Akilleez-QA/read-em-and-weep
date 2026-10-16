**D03 verdict: the bridge is mathematically valid conditional on the selected quotient-basis certificates and the authenticated geometric comparison. It supplies 32 separating functionals, not 32 computed source values. The corrected obstruction remains undecided.**

I inspected the requested documents, current selection reviews and artifacts, and bounded paths at pins P, S, H and the underlying model pin. No source computation, rank replay, writes, or GitHub mutation occurred.

1. **Degree and duality checks pass.** Put \(B=\operatorname{End}(K)\), \(Y=(\mathbf P^1)^4\), and \(T=\mathcal O_Y(-2,-2,-2,-2)\). A constant scalar chain map is
   \[
   L:B\longrightarrow\mathcal O_{\mathbf P^4}(-2)[2],
   \qquad [L]\in\mathbb H^2(B(-2)).
   \]
   The target term lies in internal degree \(-2\). Pullback and tensoring by \(T\) give the scalar target \(\mathcal O_Y(-4,-4,-4,-4)[2]\), hence output in \(H^4\), of dimension 81.

   The product deck generator is permutation-invariant; the canonical bundle carries the additional permutation sign. Equivariant Serre duality therefore identifies the rational epsilon dual with
   \[
   W^\vee\simeq
   \mathbb H^2(B)\oplus
   \mathbb H^2(B(-1))Q\oplus
   \mathbb H^2(B(-2))Q^2,
   \]
   of dimensions \(2+10+20\). Consequently the proposed tests have the correct degrees: \(20Q^2\), ten \(v_kQ\), and two \(v_kv_l\). Here all three polynomial types are sections of \(\mathcal O_Y(2,2,2,2)\). These conclusions use [S, §§1–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md).

2. **Variable normalization must remain explicit.** The pinned model uses \(v_0=1,\ v_k=e_k(x_1,\ldots,x_4)\) on the finite chart. Homogeneously,
   \[
   v_k=\sum_{|I|=k}\prod_{i\in I}X_i\prod_{j\notin I}Y_j.
   \]
   These are unscaled elementary symmetric sections, without binomial denominators or alternating coefficient signs. With this normalization,
   \[
   Q=X_1X_2Y_3Y_4+Y_1Y_2X_3X_4
   \]
   has the stated cubic resolvent and gives
   \(R^{D_8}=A\oplus AQ\oplus AQ^2\). A compiler using signed quartic coefficients or normalized symmetric averages needs an explicit substitution. Dehomogenizing \(v_0\) does not remove the associated line-bundle degree.

3. **Trace orientation checks pass, subject to the pinned basis convention.** For \(j=15b+i\), the positive kernel cycle \(K_j\) has free entry \(B[b,i]=1\). Reversing the Hom directions gives
   \[
   \operatorname{str}(XK_j)
   =\sum_{a,k}\gamma[i,a,k]X_{02}[a,5b+k]-X_{13}[i,b]
   =-L_{i,b}(X).
   \]
   Thus the selected representative for \(L_{i,b}\) is \(c_{i,b}=-K_j\). Polynomial multiplication introduces no additional Hom sign. A uniform complex shift can change the common trace sign; rank checks cannot detect that error. The Laurent-output convention must therefore retain the declared orientation. The ten relations are hypercohomology boundaries and hence relations of derived morphisms, rather than pointwise row identities. See [H, conventions and result](https://github.com/Akilleez-QA/read-em-and-weep/blob/e6e8d272e760a432dbbc1053b88c8eae03a47304/research/hsd/twist-minus2-d5/NOTE.md).

4. **The “missing twelve labels” statement is now stale locally.** [selection.json](../detector-selection/selection.json) contains ten labels \((i,b,k)\):
   \[
   (5,0,0),(5,0,1),(5,0,4),(6,0,0),(6,0,1),
   (6,0,2),(7,0,1),(7,0,2),(8,0,3),(9,0,4),
   \]
   and two labels \((i,b,k,l)=(5,0,0,0),(5,0,1,4)\).

   The receipt and current producer hashes match. This establishes artifact consistency only. I leave independent rank acceptance to the separate reviewer. The valid lift requires exact rational cycles, authenticated rational boundary upper ranks \(240/848\), and verified modular augmented ranks \(250/850\) in the same bases. Modular boundary ranks alone are insufficient.

5. **The required source evaluations are weighted Laurent pairings.** For an authenticated scalar output \(s_{i,b}\), the functional is
   \[
   D_{i,b;f}([R^\sharp])
   =[x_1^{-1}x_2^{-1}x_3^{-1}x_4^{-1}]
      \bigl(f\,s_{i,b}\bigr).
   \]
   Writing \(f=\sum_m f_mx^m\), this means
   \[
   D_{i,b;f}=\sum_m f_m\,c_{i,b}[k(m)],
   \qquad
   k(m)=\sum_{\nu=1}^4(2-m_\nu)3^{4-\nu}.
   \]
   Thus “32 output detectors” means 32 specified linear combinations of Laurent outputs. It does not mean 32 individual Laurent positions or point evaluations. A compiler may compute these weighted sums directly; computing all 81 coordinates of every map is unnecessary.

   The scalar must first be transported into the authenticated original frame, including division by the deck product and the internal-degree-\(-2\) factor \(\tau^{-4}\). These conventions and indexing are fixed in [P, map-and-comparison §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/map-and-comparison.md).

**The exact remaining application gap** is the source-to-functional binding and evaluation for the complete corrected \(R^\sharp\). The constant-row classification explicitly does **not** supply the old map’s first-carrier merger, pole bounds, or inexpensive geometric numerator for the other maps. Consequently the old scalar compiler and its 78 summands cannot automatically evaluate this family. Each requested pairing needs a valid regular comparison or an authenticated full finite-model input. Previously computed scalar zeros transfer only after proving they concern the same corrected class and conventions. See [P, structural-relations §3](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/structural-relations.md).

A publication-ready conditional theorem is:

> Over \(\mathbf Q\), assume the pinned perfect-complex, invariant-splitting and geometric epsilon-membership identifications, and verify that the selected classes form bases of the three small cohomology quotients. Then the twenty \(Q^2\) pairings and selected ten \(v_kQ\) and two \(v_kv_l\) pairings define an isomorphism \(W\to\mathbf Q^{32}\). For an authenticated representative of the complete corrected obstruction, its class vanishes exactly when all 32 assembled rational pairings vanish; any authenticated nonzero pairing proves nonvanishing.

The existing artifacts specify these mathematical labels. They do not yet certify compiled source outputs or any of those 32 values.

Publication note: this report records its inspection snapshot; subsequent corrections and review dispositions are recorded in STATUS.md and the relevant package README.
