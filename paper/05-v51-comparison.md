# 5. Separate V51 deformation geometry

This section is a comparison with the independent primary-geometry line attributed in the public discussion to **Mr. Slop**. It is not part of the proof of the adjoint rank theorem. The claims below are summarized from the actual PR634 proof and review, including its pinned inputs; no implication from V51 deformation theory to the remaining adjoint obstruction is asserted.

## 5.1 The marked functors

Work over C with V51 and L₀ = O_V51(1). Consider local Artin C-algebras with residue C, with fixed special-fiber markings. Let F be the polarized pair deformation-class functor and G the abstract deformation-class functor. Their values are isomorphism classes, not groupoids.

The pinned inputs give H⁰(Θ_V51) = 0, h¹(Θ_V51) = 576, h¹(O_V51) = 60, H²(O_V51) = 0, and formal unobstructedness. For sufficiently large m, let n = h⁰(L₀ᵐ). The high-power Hilbert germ is smooth of dimension n² + 635. Its tangent kernel over the pair functor is pgl_n, of dimension n² − 1; forgetting the polarization has the 60-dimensional Picard tangent kernel. Hence dim T_F = 636 and dim T_G = 576.

PR633 supplies an actual smooth pointed étale Hilbert chart carrying an actual relatively ample root L with Lᵐ ≅ O(1). This is the algebraic family in which the slices are cut; it is not an assumed algebraization of an arbitrary formal arc.

## 5.2 Algebraic slices and formal universality

PR634 constructs nested smooth pointed locally closed subschemes

    S_576 ⊂ S_636 ⊂ H′,

by choosing tangent complements and cutting them out with regular functions having the required independent cotangent classes. Their completed bases prorepresent G and F, respectively. Noncanonically, the completed local rings are power-series rings in 576 and 636 variables.

Tangent isomorphism alone is not the argument. Across each small extension with kernel J, the actual lift classes form torsors under H¹(Θ_V51) ⊗ J and H¹(A_L₀) ⊗ J. Marked abstract automorphisms vanish because H⁰(Θ_V51) = 0. Pair automorphisms remain as scalars, but every such scalar lifts, so they do not create a hidden quotient of the lift-class torsor. The classifying map between lift torsors is equivariant for the central Kodaira-Spencer isomorphism. Induction on Artin length then proves existence and uniqueness of the classifying map at every order.

The nested inclusion gives a noncanonical natural section G → F of polarization forgetting. It does not say the polarization is unique: the other 60 Picard directions remain.

## 5.3 Scope boundaries

These are universal marked Artin class functors. They are not a representation of the pair groupoid, a fine moduli space over arbitrary bases, an unmarked quotient theorem, or a canonical global choice of polarization. An arbitrary formal arc in the completion need not be algebraic or convergent. The construction does not recover the original ten sections, identify these deformations with the original source problem, or settle the full-adjoint or Weil-class algebraicity goal.

### Exact sources

- [PR634 proof, immutable commit 895e3a61098f50eccc0a4dc22b58606a28125355](https://github.com/Akilleez-QA/read-em-and-weep/blob/895e3a61098f50eccc0a4dc22b58606a28125355/research/hm/cubic-algebraic-deformation-slices/PROOF.md).
- [PR634 independent mathematical review at the same commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/895e3a61098f50eccc0a4dc22b58606a28125355/research/hm/cubic-algebraic-deformation-slices/REVIEW.md).
- [Public PR1 statement of the PR634 result](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6328234004).

The proof pins PR611, PR614, PR615, PR631, PR632 and PR633 at their exact commits. Its review is mathematical review conditional on those inputs, not proof-assistant verification. Later V51 results are outside this edition's comparison cutoff.
