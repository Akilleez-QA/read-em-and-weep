# Conditional polar-layer application

This is the preserved application of the conductor theorem. Its principal-parts and cohomological premises are explicit in unit06 INPUTS.md; it is not part of the unconditional conductor computation.

## Exact normalized test for a polar layer

Retain the preceding principal-parts notation from ../discriminant-pole-exclusion/PROOF.md. For either locally free retained coefficient sheaf F_i on Y and k≥1, let

    L=F_i(kD)|D,  G=ν*L,  Q_L=L⊗Q.

The top-pole layer of P_i,k is L. Its descent sequence is

    0→L→ν_*G→Q_L→0.                                 (16)

Thus normalized sections used in a pole-layer construction must satisfy precisely the conductor-square condition above. Moreover normalization alone can miss a cohomology class: the exact segment is

    H⁰(T,G)→H⁰(D,Q_L)→H¹(D,L)→H¹(T,G)→H¹(D,Q_L).

For a closed polar-symbol one-cochain s in L with class ξ, first test whether its normalized class vanishes. If it does, choose a regular normalized zero-cochain a with δa=ν*s. Its image dsc_L(a) is a closed zero-cochain and hence a global section of Q_L. The remaining invariant is

    γ(ξ)=[dsc_L(a)] in coker[H⁰(T,G)→H⁰(D,Q_L)].      (17)

It is independent of the normalized primitive a and of the representative s, and ξ=0 iff its normalized class is zero and γ(ξ)=0. Indeed the connecting map sends the class in (17) exactly to ξ; if (17) vanishes, subtract a global normalized section with the same quotient to make a descend to a zero-cochain on D. This proves the criterion constructively. No H¹ term or global-lifting condition has been discarded.

For reduction of a specified k-pole primitive allowing a closed k-pole correction, the actual condition remains

    ξ ∈ im[H¹(Y,F_i(kD))→H¹(D,L)].                    (18)

Equations (16)-(17) can test ξ after subtraction of any proposed image class; they do not remove the image ambiguity in (18). At the common universal bound k=3, the previously proved H¹(Y,F_i(3D))=0 makes (18) simply ξ=0 for that layer. Lower layers still have to be removed in turn, and vanishing of the top normalized class is insufficient unless the conductor quotient class (17) vanishes as well.

This resolves a geometric descent dependency for discriminant pole removal. It does not construct either retained source primitive, show a polar obstruction vanishes, or evaluate any of the thirty retained conditions. The finite regular Frobenius reconstruction preserves these pole and descent constraints and cannot cancel them between independent coordinates.

## Scope and dependencies

All computations here are universal divisor, local-ring, duality, Hilbert-series, and exact-sequence arguments. No actual mixed source, selected rank, polynomial instance, physical jet, or obstruction pairing was evaluated. 

- ../discriminant-pole-exclusion/PROOF.md: exact principal-parts obstruction and universal pole bounds.
- ../nullcone-normalization/PROOF.md: triple-root normalization and cusp comparison.
- ../normalization-gysin-factorization/PROOF.md: compatible finite duality and primitive-gluing conventions.
- AUDIT.md: independent audit.
