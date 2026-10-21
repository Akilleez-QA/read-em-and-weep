# Independent review: residual derived direct image

Verdict: **Pass**, conditional on the explicitly pinned geometric inputs of PR572, PR574 and PR577. This is an independent mathematical audit, not formal verification. No selected HM/source evaluation or numerical computation was used.

Reviewed `PROOF.md` SHA-256: `a1ea4e4dbced6f8d786b142b25f3df529c7e55dc16ab9b1dc1599aee82b72d67`. The reviewed version contains the dimension-48 torsor consequence and has status “awaiting independent mathematical review”. A subsequent status-only replacement recording this review does not change the mathematical verdict.

## Checks

1. **The actual map, not only its H⁰, factors through points.** The conductor quotient map factors through the reduced sixty-point scheme W on X. Applying derived direct image therefore supplies a factorization through π_*O_W on B, followed by exact finite pushforward and the residue-difference map. No inference from a degree-zero map to a derived map is needed.

2. **The elliptic summand maps to zero for the correct reason.** On B=P¹, the truncation obstruction for Rπ_*O_X lies in Ext²_B(N,O_B)=0. For any resulting inclusion N[-1]→Rπ_*O_X, its composite to π_*O_W belongs to Ext¹_B(N,π_*O_W)=H¹(B,N^∨⊗π_*O_W)=0. Exact finite pushforward preserves this zero morphism. The proof does not assume Ext¹ vanishing on the singular target Γ.

3. **Cone shifts and extension compatibility are correct.** With cohomological shifts, Cone(d)[-1] is the complex with h_*O_B in degree zero and g_*T in degree one. The direct-sum decomposition of the cone of (d,0) yields C⊕h_*N[-1]. It can be taken as an isomorphism of the associated triangles, so taking H¹ splits the specific PR577 extension, respecting its canonical K inclusion and h_*N quotient. An abstract isomorphism of the middle sheaf alone would not have sufficed, but the cone construction gives the stronger compatibility.

4. **The global Postnikov obstruction vanishes.** A one-dimensional Gorenstein local ring has self-injective dimension one, so local Ext in degree at least two vanishes even when K is not perfect. Sheaf-Ext¹ has finite support, hence zero H¹. The remaining total-degree-two term has H² on a curve and vanishes. Thus the global Ext²_Γ(K,O_Γ) vanishes. This proves the claimed second splitting; local vanishing alone is not being mistaken for global vanishing.

5. **Unit compatibility and scope.** The O_Γ inclusion is the canonical degree-zero truncation, identified with the adjunction unit using g_*O_S=O_Γ. Both split-triangle constructions can be chosen to retain that inclusion. No uniqueness, canonical complementary summand, multiplicative formality, flatness, or flat base-change result follows or is claimed. Nonsplitting of the dualizing complexes on S and the incidence scheme is compatible with this splitting on Γ; these are different derived objects.

6. **The dimension-48 consequence is correct.** Sections of the fixed split surjection R¹g_*O_S→B' form a torsor under Hom_Γ(B',K). At each node, B'/mB' has dimension two and K is a four-dimensional residue-field module, giving a local Hom space of dimension eight. The target support is the six reduced nodes, so the global Hom space is the direct sum of these six spaces. Its dimension is 48. This describes all sheaf sections, not a claimed dimension of all derived or multiplicative splittings.

7. **Cohomology check.** The derived decomposition gives h¹(O_S)=6+24=30 and h²(O_S)=h¹(P¹,O(-5))=4, consistent with PR574. These are checks rather than new numerical results.

No mathematical correction is required. The new contribution is the splitting of the previously unresolved extension in PR577, the module-level derived decomposition, and the exact dimension of the ambiguity in choosing the sheaf complement.
