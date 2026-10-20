Historical audit of the source edition. Hashes below bind that source edition, not the normalized publication bytes. Mathematical formulas are retained; the current geometric dependency is specified in PROOF.md and DEPENDENCIES.json.

# Independent structural audit

This historical structural audit checks the module lifting and connecting-map argument for the source edition of 2026-10-18. It is not a fresh independent review of the normalized publication edition.

The claim holds, with an important distinction: the argument trivializes the relative Ext complex as a module complex, not necessarily as an algebra. That suffices to kill every graded commutator with a family KS class.

Let A=k[ε]/ε² and choose a direction c. Write τ=τ_{εc}:Y_A→Y_A, reducing to identity, and E_A=q_A^*(τ^*F)⊗N_A. Because N_A is fixed, End(E_A)=q_A^*End(τ^*F). Finite pushforward and projection formula give an actual decomposition

    q_{A*}End(E_A)=⊕χ τ^*End(F)⊗Lχ,A.

Each Lχ is an exterior product of O and O(−2). The translation subgroup of PGL₂ lifts to SL₂ through the unipotent matrices, so these bundles admit translation linearizations. Choose τ^*Lχ,A ≅ Lχ,A reducing to identity. Consequently τ^*End(F)⊗Lχ,A ≅ τ^*(End(F)⊗Lχ,A).

Since τ is an automorphism over Spec A, relative derived global sections are invariant under τ. Thus, compatibly with reduction,

    RΓ(X_A,End(E_A))χ ≅ RΓ(Y,End(F)⊗Lχ)⊗k A.

Equivalently, use End(K) in place of End(F). Therefore H^m(X_A,End(E_A))χ → Ext_X^m(E,E)χ is surjective in every degree.

This is genuinely a lift to End(E_A): finite pushforward identifies the relative cohomology groups themselves, and the χ summands above are actual summands of q_{A*}End(E_A). They are not merely unrelated twisted cohomology groups of equal dimension.

Let a=κ(c). The connecting map for 0→End(E)→End(E_A)→End(E)→0 is δ_a(b)=a∪b−(−1)^m b∪a, up to an immaterial overall convention sign. For the supplied fixed-term complex, d_A=d+ε·δd gives endomorphism differential D_A=D+ε[δd,−]. A lift satisfies D b₁+[δd,b]=0. Surjectivity forces [a,b]=0 in total Ext.

For m=1, ab+ba=0 for every b, so P_W=0. This does not assert that individual products ab vanish.

The branched cover causes no obstruction. Translations need not lift to X or preserve its branch divisor. They need only preserve the O_Y-modules Lχ. The multiplication maps between eigensheaves generally are not translation-equivariant; an algebra-level trivialization is neither claimed nor used.

The d5 and secondary-filtration issues cannot evade this proof: it establishes vanishing in the abutment, not merely its associated graded. No splitting of the Ext² filtration is needed. The stated E1 support is consistent with the sums of O(r−2,...,r−2): lower row r≥2, upper row r≤0.

Audit scope: the explicit degree-one Cech endpoint supplement was added after this independent report. It is separately verifiable by the two cocycle identities printed in that supplement. The all-degree connecting-map proof above independently certifies its cohomological conclusion.
