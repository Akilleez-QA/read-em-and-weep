# Twisted endomorphism trace class: the exact remaining comparison

## Result

**Update:** [FORMAL-TORSOR.md](FORMAL-TORSOR.md) now closes the independent torsor premise under the stipulated differential, symplectic, flat and complete DQ hypotheses. Earlier conditional wording below records the original intermediate stage. Module existence and the period comparison remain unproved.

Conditional on a genuine all-order locally free twisted module and on its matrix-Weyl formal-coordinate Harish–Chandra torsor, the universal characteristic class DOES vanish above degree four on the symplectic fourfold. This implication needs no prior neutralization of the original algebroid. It does not yet identify that class in terms of the given bundle and gerbe coefficient, and it supplies no detection theorem for the thirty retained obstruction coordinates.

No model, source-coordinate, finite-jet, physical-matrix, or repository experiment was performed. The algebra calculations below concern universal conventions only.

## Primary-source anchors

1. Baranovsky, *Chern classes of quantizable coisotropic bundles* (2024), §3.3 equation (6), Lemma 3.5, §4.2, Lemma 4.3:
   https://ems.press/content/serial-article-files/42628
   The matrix-Weyl central extension is
   0 → h^(-1)k[[h]] → h^(-1)D_p + Mat_e(D_p) → Der(Mat_e(D_p)) → 0.
   Its universal class τ belongs to relative cohomology for Der(Mat_e(D_p)) and pgl_e⊕sp_(2p), and vanishes in degrees greater than 2p. The scalar constant overlaps gl_e; the auxiliary central complement omits h^0. Lemma 4.3 identifies the class pulled back to the algebra/module-pair torsor. Step 4 explicitly accounts for the right-module/opposite sign and obtains c=θ there. The neutral formula is A-hat exp(−c)ch(E), with ordinary matrix trace, not the Chern character of End(E).

2. Bressler–Gorokhovsky–Nest–Tsygan, *Deformation quantization of gerbes I*, §2 and §4:
   https://math.colorado.edu/~gorokhov/preprints/BGNT1.pdf
   Its descent equations coincide with ours. In the symplectic case, §4 converts descent to curved Weyl data ∇²=ad(R), ∇R=0. §4.2 shows that period components and their holomorphic projections can involve nonlinear corrections. This supplies a construction framework, not an identification of our coefficient b with a particular period component.

3. Ryszard Nest, 2011 primary lecture notes, slides 39 and 45–47:
   https://monge.u-bourgogne.fr/gdito/scalea2011/Notes_%26_Photos_files/nest.pdf
   These explicitly state the central-curvature characteristic class [tilde∇²−R] and Riemann–Roch for perfect twisted modules over symplectic algebroid stacks. They use iℏ and an exponential e^θ; their characteristic-factor convention is not copied here. They corroborate that an algebroid trace comparison exists in the literature, but do not fix the conversion to our row and period conventions.

4. BGNT, *Chern character for twisted complexes*, especially §3.4:
   https://math.colorado.edu/~gorokhov/preprints/reznikov-volume.pdf
   This constructs the Chern character for perfect twisted complexes through twisted matrix algebras and cyclic complexes. Existence of this character is distinct from its numerical identification with our matrix-Weyl Gelfand–Fuks class.

## What follows without any gerbe-period substitution

Let C_h denote the honest algebra glued using right-action matrices, if the conditional module exists. Assume its formal completions are Mat_e(D_2), and let P_C be the corresponding transitive Harish–Chandra torsor. Define

    T(C_h) := GF_(P_C)(τ).

The Gelfand–Fuks construction is a map on cohomology and preserves cohomological degree. Since τ_j=0 for j>4, necessarily

    T(C_h)_6 = T(C_h)_8 = 0.

This is a complete conditional implication once the stated torsor hypotheses are checked. The partner established exact algebra gluing, not yet these formal-coordinate torsor hypotheses; that geometric step remains conditional. It is not circular as a necessary condition: existence of the sought module is assumed only to derive a consequence of existence. It would be circular to infer module existence from the construction of C_h.

The trace in τ is the trace of an e-by-e matrix acting on the rank-e local module. Its degree-zero value is e. Substituting ch(End(E)), whose degree-zero value is e², fails this normalization immediately. Dividing the trace by e changes the entire class and must be declared, although it does not affect a zero statement.

## Exact missing comparison lemma

Here is a usable target rather than an assertion that it has been proved for this presentation.

**Descent/period/trace comparison.** Starting with the fixed differential DQ-algebroid descent (μ_i,F_ij,A_ijk), together with the conditional row-module transitions G_ij, construct central-curvature descent data and a class c_𝒜 in H²_dR(X)((h)), normalized by the neutral case and the chosen parameter h. Prove, compatibly with the actual Morita identification furnished by G, that

    GF_(P_C)(τ) = A-hat(TX) exp(−c_𝒜) ch(E)

when the classical gerbe has its specified trivialization and E is the resulting ordinary classical bundle. If changing that trivialization changes the symbol bundle, use the corresponding twisted Chern character instead, and prove the precise invariant product. The construction must identify the Čech degree-two piece coming from log A, the degree-one connection corrections from F, and local curvature pieces from μ as one TOTAL cocycle. Its central class must match the central extension in equation (6), including the scalar constant/gl_e overlap.

This statement still requires proof for the supplied presentation. It is more precise than “find a twisted index theorem”: the literature already has a twisted character and index framework. What is missing locally is the chain-level/characteristic-class comparison that connects this framework, our actual descent coefficients, and Baranovsky’s particular universal cocycle. The parameter and classical-gerbe trivialization must be tracked, not inferred from a theorem’s title.

A concrete proof strategy is to build the curved Weyl presentation of (μ,F,A), lift the connection to the central extension, and compare its central curvature minus curving with the extension class extracted from the matrix-algebra torsor. The module transitions furnish the comparison between the two descent presentations. Equality should be established modulo total Čech–de Rham coboundaries; no equality of individual local curvatures or of the isolated coefficient b is necessary or justified.

## Sign and normalization checks that the lemma must pass

These checks are derived directly and do not use a numerical model.

* For the usual opposite algebra at fixed h, the Poisson bracket changes sign. If δ=ad(a), then δ=ad_op(−a). Thus the natural map on central-extension lifts sends a to −a, including its central component. A comparison that changes to the opposite algebra without recording this central sign is incomplete. Replacing h by −h is a separate parameter operation and must not be silently conflated with taking the opposite algebra.
* For row right action R_H(v)=vH, composition gives R_H∘R_K=R_(KH). Consequently the right-action matrix algebra is the opposite of the conventional composition algebra End_left(M). Choose one throughout. The partner calculation fixes C_h=End_left(M)^op as the ordinary matrix algebra, while B_h=End_left(M) uses opposite multiplication. Classically C_h reduces to End(E)^op, canonically End(E^vee). Therefore the neutral comparison must also verify whether its frame convention produces ch(E) or ch(E^vee), together with the corresponding central/opposite sign. The displayed missing lemma uses the neutral-module normalization, not an unproved identification of the frame factor. For rank two and c1(E)=0, ch(E^vee)=ch(E), since the two formal Chern roots are x and −x; this removes the classical dual-character ambiguity in this specific case, but does not remove the central-extension sign issue.
* Classical End(E) alone cannot distinguish E from E⊗L. Under that change, ch(E⊗L)=exp(c1(L))ch(E). Therefore any proposed invariant expression exp(−c)ch(E) must compensate a change of symbol presentation by c→c+c1(L), whenever the compared Morita/trivialization change actually induces that tensoring. This is a consistency condition, not an assertion that arbitrary E⊗L quantizes over the same fixed algebroid.
* The first-order module defect has scalar contribution −b Id in the supplied row convention. That fixes a module-descent sign only. It does not prove that b occurs with either sign, or at any asserted h-power, in c_𝒜: b is one Čech component, while the period is a total de Rham class involving all descent components.

## Detection: why this will not automatically settle the retained sector

The companion semiregularity result states that, with the required classical S4-equivariance, the retained thirty-dimensional U_(2,2)-isotypic sector lies in the kernel of ordinary bundle semiregularity

    σ: Ext²(E,E) → ⊕_q H^(q+2)(X,Ω^q_X).

For any characteristic obstruction map proved to factor as L∘σ, the retained sector is therefore killed identically. This requires no injectivity hypothesis on L and no equivariance of subsequent cup products: L(0)=0. In particular multiplying the ordinary characteristic image by a period exponential or another characteristic class cannot recover information already lost by σ.

For a fixed ambient period, a comparison whose obstruction derivative is the ordinary Chern-character derivative followed by multiplication by A-hat exp(−c_𝒜) is of this blind form. A different twisted or higher-order obstruction map must be shown to escape that factorization before claiming detection. Neither the universal vanishing lemma nor an index identity alone proves such an escape.

If ambient data also vary, differentiating exp(−c)ch(E) adds the term −exp(−c)ch(E)·δc. That is a JOINT ambient/module variation term; it is not evidence that the fixed-ambient map detects a module class in ker σ. It must be compared with the allowed ambient characteristic map κ_E, and with the requirement that the given finite jet remain unchanged.

Hence even a fully established comparison can give a useful necessary condition for existence without resolving any retained coordinate. No nonzero obstruction, all-order module existence, or vanishing of the thirty coordinates follows from the work here.
