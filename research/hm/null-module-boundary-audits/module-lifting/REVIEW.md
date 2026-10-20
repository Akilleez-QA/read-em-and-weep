# Independent audit: module small-extension obstruction

## Verdict and scope

The central formulas in RESULT.md are correct under its stated small-extension, unitality, locally free row-presentation, and coefficientwise lifting hypotheses. In particular, the row order, exact four-index identity, ambient variation, and the primitive for ambient boundaries all pass a direct formal check. No sign correction is needed.

One cover qualification should be kept explicit throughout: on an arbitrary fixed cover the obstruction and torsor are Čech objects; identification with derived global Ext and sheaf H¹ requires an acyclic trivializing cover or a justified comparison/refinement. RESULT.md expressly states this for H²; its subsequent H¹ torsor statement should be read under the same hypothesis (or relabeled Čech H¹ on the fixed cover). The original ambient product cover is not by itself a verified E-trivializing cover.

This audit read only the supplied static RESULT.md, the ambient LEMMA.md, and the static the pinned PR16 source (see README). It performed no actual model, source-coordinate, jet, physical matrix, repository, or obstruction-coordinate evaluation. All thirty retained values remain unknown.

## 1. Row-frame convention

A row map from chart j to chart i has the classical expression v ↦ v g_ij. Composition therefore gives g_jk g_ij=g_ik. An endomorphism represented by right multiplication by x_j in frame j is represented in frame i by

τ_ij(x_j)=g_ij⁻¹ x_j g_ij.

Indeed, (v x_j)g_ij=(v g_ij)τ_ij(x_j). This establishes the transport independently of any column convention. Also τ_ij τ_jk=τ_ik, since g_jk g_ij=g_ik. Thus the displayed twisted Čech differential squares to zero.

The defect D_ijk is a map from the k row frame to the i row frame. Its normalization C_ijk=g_ik⁻¹D_ijk represents an endomorphism in the i frame, since D_ijk=g_ik C_ijk. This is why the inverse is on the left. Reversing its placement would change both transport and correction formulas.

## 2. Exact four-index coherence

Set H=F_ij F_jk(G_kl) and expand

Q=F_ij(F_jk(G_kl)⋆G_jk)⋆G_ij.

Using the jkl defect and then the ijl defect gives

Q=F_ij(A_jkl)⋆A_ijl⋆G_il
  +F_ij(A_jkl)⋆D_ijl+F_ij(D_jkl)⋆G_ij.

Using first the ijk defect gives

Q=H⋆A_ijk⋆G_ik+H⋆D_ijk.

The inner-gluing equation implies H⋆A_ijk=A_ijk⋆F_ik(G_kl). Hence the ikl defect gives

Q=A_ijk⋆A_ikl⋆G_il+A_ijk⋆D_ikl+H⋆D_ijk.

The pentagon equates the two leading terms. Subtraction gives exactly

A_ijk⋆D_ikl+F_ij F_jk(G_kl)⋆D_ijk
−F_ij(A_jkl)⋆D_ijl−F_ij(D_jkl)⋆G_ij=0.

No commuting of a triple unit through a transition occurs. The formula therefore does not assume A is central.

Reduction on I gives D_ikl+g_kl D_ijk−D_ijl−D_jkl g_ij=0. Using both g_il=g_kl g_ik and g_il=g_jl g_ij after multiplication by g_il⁻¹ gives

C_ikl+C_ijk−C_ijl−τ_ij(C_jkl)=0.

This is the negative of the displayed alternating-deletion expression δC; equivalently δC=0, exactly as asserted.

## 3. Corrections and the obstruction sheaf

For ΔG_ij=g_ij x_ij, linearization yields

ΔD_ijk=g_ik x_ij+g_jk x_jk g_ij−g_ik x_ik.

Thus ΔC_ijk=x_ij+τ_ij(x_jk)−x_ik=δx_ijk. Solving δx=−C is necessary and sufficient for genuine transition descent for the fixed ambient extension and chosen row presentation. I²=0 and maximal-ideal annihilation of I make this linearization exact, not an approximation.

The coefficient sheaf is End(E)⊗I. There is no scalar-only reduction and no identification of this module obstruction complex with the shifted ambient Hochschild complex. Local free modules over each lifted algebra supply local lifts of the locally free module presentation; this is the reason no separate local action obstruction appears here.

On an End(E)-acyclic cover, the obstruction lies in H²(X,End(E))⊗I=Ext²(E,E)⊗I, and the usual H¹ torsor/H⁰ automorphism description follows. Without that cover condition, replace H¹ by fixed-cover Čech H¹ as well as replacing H² by fixed-cover Čech H².

## 4. Ambient variation

Write η=(u,v,a) for an I-valued change of product, overlap map, and triple unit. Keeping the chosen transition lifts fixed gives

ΔD_ijk=u_i(g_jk,g_ij)+v_ij(g_jk)g_ij−a_ijk g_ik.

The additional putative product term −u_i(1,g_ik) vanishes by normalization. All positive-order old coefficients disappear because they multiply I. Consequently the formula for κ_g(η)=g_ik⁻¹ΔD_ijk is correct, including the negative scalar contribution −a_ijk Id.

The ambient lemma gives ΔO=dη with O=(-S,H,K,-P). Therefore two genuine ambient extensions differ by a closed η; conversely any closed I-valued η added to a genuine extension preserves all ambient equations. This converse justifies using all closed corrections when no additional restrictions are imposed. The four-index proof then gives δκ_g(η)=0.

## 5. Boundary calculation, including the primitive sign

For a degree-zero ambient cochain (t,s), the declared total differential gives

u_i=bt_i,
v_ij=t_j−t_i−bs_ij,
a_ijk=s_jk−s_ik+s_ij.

In the actual classical algebra O_X, scalar s commutes with functions, so bs=0. Entrywise extension of t and the definition of b give

(bt_i)(g_jk,g_ij)
 =g_jk t_i(g_ij)−t_i(g_ik)+t_i(g_jk)g_ij.

Adding (t_j−t_i)(g_jk)g_ij cancels the last displayed t_i(g_jk) term. Therefore

κ_g(d(t,s))_ijk
 =g_ij⁻¹t_i(g_ij)
  +g_ij⁻¹g_jk⁻¹t_j(g_jk)g_ij
  −g_ik⁻¹t_i(g_ik)
  −(s_jk−s_ik+s_ij) Id.

For z_ij=g_ij⁻¹t_i(g_ij)−s_ij Id, the right-hand side is precisely z_ij+τ_ij(z_jk)−z_ik=δz_ijk. Thus the stated primitive has the correct positive t and negative s signs. This verifies descent of κ to cohomology; no gauge-convention inference is needed.

Identification of its source with HH² remains conditional on the applicable normalized Hochschild/Čech comparison, as RESULT.md appropriately states. The direct κ formula and obstruction calculation do not need that identification.

## 6. Cover and refinement requirements

The ambient lemma’s finite product affine cover is sufficient for its ambient statement, but the module derivation additionally requires local free row frames for E and the chosen reduced module. These should not be inferred merely from affine ambient charts or trivializations of N².

The static source explicitly distinguishes these issues in Sections 6–7: first use its affine refinement trivializing N, then refine further as needed to trivialize E and construct local contractions. For the universal module obstruction proof, local contractions and the finite RHom comparison are not needed. An affine E-trivializing refinement of the existing ambient cover suffices, together with restriction of all supplied ambient and reduced-module data. On the separated algebraic X in question, affine intersections are affine, so quasi-coherent End(E) is acyclic on them. Refining does not change the supplied finite-order coefficients; it restricts them.

An actual comparison to a fixed original-cover finite model would need the source’s explicit refinement comparison or another certified chain map. This audit supplies neither such a comparison nor any instantiated frames. The universal theorem must not be advertised as having supplied those computational inputs.

## 7. Consequences

For a fixed genuine ambient extension the criterion is [C]=0. For a joint choice the criterion is cancellation of [C] by an allowed κ_E class. Ambient H² in the shifted complex (ordinary HH³), differences of ambient extensions in shifted H¹ (ordinary HH²), and the module Ext² obstruction play distinct roles.

The all-order ambient extension theorem alone therefore proves no module quantization. Corrections starting above the supplied ambient two-jet cannot alter its order-two module obstruction. RESULT.md preserves both distinctions correctly. Its invariant conclusions are conditional on compatible equivariance of the module data and the allowed corrections, also correctly stated.

Recommended editorial clarification only: append “on the same acyclic cover; otherwise use fixed-cover Čech cohomology” to the H¹ torsor paragraph, and state explicitly at application time that an E-trivializing affine refinement is chosen. No algebraic formula correction is required.
