# Ordinary formal-local deformation bases

## Statement and inputs

For the specified determinant-trivial Horrocks–Mumford pullback E on the fixed abelian fourfold X, the ordinary miniversal base is
\[
\mathbf C[[t_1,\ldots,t_{87}]].
\]
With a chosen determinant trivialization compatible with the central fiber, the miniversal base is
\[
\mathbf C[[s_1,\ldots,s_{83}]].
\]

Inputs are the actual smooth family and injective Kodaira–Spencer map in [PR #3](https://github.com/Akilleez-QA/read-em-and-weep/pull/3), together with the exact Ext dimensions in [PR #5](https://github.com/Akilleez-QA/read-em-and-weep/pull/5). The independent [review and formal-local handoff](https://github.com/Akilleez-QA/read-em-and-weep/pull/3#issuecomment-6093574455) checks the distinction between this conclusion and quadratic obstruction vanishing.

Reviewed source commits:
- Family: 86251374e9c62528b9b9dbb35ef883bdfac30ad8.
- Ext certificate: add03476d9055aa00e1e00778eea6332cf8e01cc.

## Hull argument

The ordinary coherent-sheaf deformation category has a hull. A smooth formal family with an isomorphic Kodaira–Spencer map is miniversal; see [Talpo–Vistoli, Proposition 6.36](https://arxiv.org/pdf/1006.0497), with Theorem 6.33 and Proposition 6.26.

Here is the local-ring argument. Let R be a hull with tangent dimension n and T the completed local ring of the actual smooth family. Versality supplies R→T. Choose a minimal presentation S=C[[x₁,…,xₙ]]→R. The composite S→T has invertible linear term, hence is an isomorphism. Its kernel is zero, so the kernel of S→R is zero. Therefore R is a power-series ring.

Apply this with n=87. For fixed determinant, the section/translation subfamily has dimension 83 and its tangent is the trace-free Ext¹ subspace. The compatible determinant identification exists locally in that family, so the same argument applies with n=83.

## Automorphisms and limits

A hull does not erase stabilizers. Since H⁰(End E)=C, an induction over small Artin extensions shows End(E_A)=A: reduce an endomorphism, subtract a lifted scalar, and identify the remaining kernel with the scalar extension ideal. Ordinary scalar automorphisms remain.

For determinant-preserving automorphisms that induce the identity on the central fiber, the scalar c satisfies c²=1 and c≡1. In characteristic zero this forces c=1. Without the central-fiber framing, the stabilizers remain G_m, respectively μ₂.

This is a formal-local ordinary deformation result, not a global coarse-moduli identification. It does not imply that Ext² or the associative Ext product vanishes. It does not establish unobstructed ambient-category, Poisson, gerbe, or Weil-family deformation.

The actual tangent-isomorphic smooth family is essential. Vanishing quadratic obstructions alone would not exclude higher-order equations such as x³=0. This corollary is a standard consequence of the checked inputs, not a novelty claim.
