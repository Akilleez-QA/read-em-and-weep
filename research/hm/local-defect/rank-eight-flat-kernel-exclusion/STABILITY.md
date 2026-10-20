> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Stability of the remaining rank-eight normalized residual kernel

## Result

Under the hypotheses of `PROOF.md`, after the flat branch is excluded, the reflexive rank-two sheaf

    B = K(2),       c1(B)=0,       c2(B)=5

is slope-stable. Moreover,

    H⁰(B)=0,
    H⁰(Ktilde(2)) = C·(u ↦ u²).

These are conditional restrictions at generic rank eight, not a determination or exclusion of that rank.

## 1. A section bound for a semistable reflexive rank-two sheaf

Let E be slope-semistable and reflexive of rank two on P⁴, with det E=O and c2(E)≠0. Then h⁰(E)≤1.

First suppose two global sections are generically linearly independent. Their exterior product, followed by the natural map Λ²E→det E=O, is a nonzero global section of O, hence a nonzero constant. Thus the induced map O²→E is an isomorphism wherever E is locally free. The complement has codimension at least three because E is reflexive on a smooth variety. Both O² and E are reflexive, so the isomorphism extends across the complement. This gives E≅O², contradicting c2(E)≠0.

It follows that all global sections together have generic rank at most one. If there is a nonzero section, let L be the saturation of their image in E. It is a rank-one reflexive subsheaf, hence a line bundle O(d). For reflexivity: E/L is torsion-free by saturation; the depth lemma applied to 0→L→E→E/L→0 gives the S₂ condition, and L is torsion-free. Semistability gives d≤0, while the existence of a nonzero section of L gives d≥0. Therefore L=O and all global sections belong to its one-dimensional space of sections. This proves the bound.

Apply this to B. If h⁰(B)>0, then h⁰(B)=1.

## 2. Symmetry excludes even one section

Twisting the canonical kernel sequence by O(2) gives an equivariant exact sequence

    0 → O → Ktilde(2) → B → 0.

Since H¹(O)=0, its global-section sequence is exact:

    0 → C → T → H⁰(B) → 0,
    T := H⁰(Ktilde(2)).

If h⁰(B)=1, then dim T=2. As in `PROOF.md`, the kernel inclusion gives an injective N-map

    T → H⁰(S⊗O(2)) = End(S),       S=Sym²V.

The central subgroup Z(H5) acts trivially on End(S), hence on T. The 24-character-orbit argument in `PROOF.md`, §3, applies in dimension two as well as dimension three: a nontrivial character of H5/Z(H5) would force at least 24 independent weight spaces. Thus H5 acts trivially on T, and

    T ⊂ End_H5(S) = 1 ⊕ 3 ⊕ 5.

The right-hand side is a direct sum of irreducible G=SL₂(F5)-modules, with each of the displayed constituents occurring once. It has no two-dimensional submodule. This contradiction proves

    H⁰(B)=0.

The global-section exact sequence now also proves that the canonical square section spans H⁰(Ktilde(2)).

## 3. Vanishing of sections gives stability

Suppose B were semistable but not stable. Saturate a rank-one subsheaf of slope zero. Its slope remains zero: saturation cannot lower degree, and semistability prevents it from becoming positive. The saturated subsheaf is reflexive by the same depth-lemma argument as in §1, and therefore is O(d). Slope zero gives d=0. Its inclusion O→B is a nonzero global section, contradicting §2.

Hence B is slope-stable.

## Scope and evidence

The semistability and Chern identities are imported from the companion rank-eight Chern argument. The exact sequence and representation decomposition are those proved or explicitly sourced in `PROOF.md`. The additional steps use only universal reflexive-sheaf geometry, elementary cohomology, and finite-group semisimplicity. No actual operation, matrix, chosen input, rank instance, jet, residue, or polynomial-instance computation occurs.
