# Conditional projective CM exclusion

This note extends the conditional global-Hom obstruction to projectivizations and degree-zero line-bundle twists. Read [PROOF.md](PROOF.md) for the argument and the sources below for the pinned dependency and references.

Assuming the inherited historical A identity and the stated physical-bundle identification:

- P(F) is not isomorphic over X to P(sigma*F), so it has no global regular automorphism covering sigma.
- F has no nontrivial line-bundle self-twist.
- For every nontrivial L in Pic^0(X), both Hom_X(F,sigma*F tensor L) and Hom_X(F,F tensor L) vanish.

The argument uses the determinant of the four-term complex, projective-bundle line descent, and its hypercohomology amplitude. The untwisted CM Hom vanishing is inherited, not reproved here. The historical A premise is not independently reauthenticated by this note.

These are global regular statements. They do not exclude rational or meromorphic maps, and do not assert that every projective automorphism over the identity is trivial.

## Sources and inherited hypotheses

### Pinned global-Hom dependency

Repository: Akilleez-QA/read-em-and-weep. Dependency commit: `4659e4425c6b5ab6b1899e6af93656ac03ff0862` (PR #79).

- [Global-Hom proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md).
- [Independent review of the global-Hom dependency](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/REVIEW.md).
- [Source pins for the global-Hom dependency](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PINS.json).

The inherited objects are the elliptic curve C given by the smooth projective completion of y²=x³−x, its origin infinity, X=C^4, N the external product of O_C(infinity), and sigma acting by (x,y)↦(−x,iy) on each factor. The inherited physical identification is F=N tensor f*E, where E is the degree-zero cohomology of the specified homogeneous complex and f is the elementary-coefficient map to P^4.

The locally split physical complex has terms (N^(2a+1))^(r_a) in degrees a=−1,0,1,2 with ranks (5,15,10,2). Its exactness and the imported conclusion Hom_X(F,sigma*F)=0 retain the dependency's historical A-identity premise. Authentication of a historical receipt is not an independent proof of its arithmetic correctness. The independent review linked above concerns the dependency, not a separate audit of this extension.

### References used in the proof

- [Stacks Project, Projective bundles, tag 01OA](https://stacks.math.columbia.edu/tag/01OA): quotient convention and pushforward of O(1).
- [Vakil, Foundations of Algebraic Geometry, Proposition 2.4 and Exercise 2.6, PDF pages 50–51](https://math.stanford.edu/~vakil/0506-216/216Cjun2807.pdf#page=50): line descent and projectivization classification.
- [Conrad, Abelian Varieties, Remarks 4.2.11 and 5.2.3 and printed page 51](https://math.stanford.edu/~conrad/249CS15Page/handouts/abvarnotes.pdf): torsion-free Néron–Severi group and Pic^0 of a product.
- [Stacks Project, Künneth formula, tag 0BEC](https://stacks.math.columbia.edu/tag/0BEC): cohomology support on the elliptic product.
- [Stacks Project, Čech cohomology of complexes, tag 01FP](https://stacks.math.columbia.edu/tag/01FP): the hypercohomology spectral sequence.
