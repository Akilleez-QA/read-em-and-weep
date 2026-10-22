# Independent review: self-adjoint pencil rigidity

## Verdict and frozen artifact

PASS, conditional on the explicitly imported actual-source/frame theorems. No mathematical corrections required. One nonmathematical process phrase was removed at the author's request before freezing.

Reviewed artifact: `PROOF.md` in this directory.

Frozen SHA-256:

    bd0da2b8772e67505bf7257c68c0e812763abe3d36a83ec52c5d63dd6399ce18

Review date: 2026-10-22 (UTC).

## Exact source verification

The reviewer fetched and read these exact repository files through the read-only GitHub connector, rather than relying only on the proposed proof's summaries:

1. [PR747 source-family exclusion proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md), commit `0a0ee30a5142477e54245b7c6f22d561abb4f5f1`, returned Git blob `41b907efbf58386bb1f03c5138d1abc2ac91aa37`.
2. [Actual canonical nonzero linear lifting correction](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md), commit `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`, returned Git blob `e2c4ae916ed77ee529ae87224c675a01567abeaa`.

PR747 explicitly supplies a fixed rational frame, a fixed k-vector space V, nonzero d, the identity K_actual(a,h)=a²(aK_h−L_can(a,h)d), the proper C-linear kernel, and the implication from nonzero immutable class to nonzero actual fourth-square scalar. The actual correction theorem, sections 2 and 6, supplies the globally linear correction and the identification L_can(a,h)=gamma S_h(a), with gamma nonzero and h mapped injectively to trace-free self-adjoint operators. These are precisely the structural inputs used here. Earlier computational sections of the source were not rerun; their established structural conclusion is imported, not independently reproved in this review.

## Independent checks

### Pairing normalization

The invariant symmetric form and quadratic apolar form are proportional in this irreducible three-dimensional representation, so their self-adjoint operators coincide. For u=ell², v=ell m, w=m², isotropy of (ell+t m)² gives, as a formal polynomial identity, 2B(u,w)+4B(v,v)=0. Thus B(v,v)=−B(u,w)/2, not its negative reciprocal or a same-sign ratio. The remaining four zero pairings follow from the other coefficients. Nondegeneracy forces B(u,w) nonzero. No actual source direction is evaluated by this formal basis argument.

### Rational pencil rigidity

The polar divisor of r must be bounded by the common divisor of the pencil. For two independent quadratics that divisor has degree zero or one, never two. Degree zero forces r constant on the projective line. In degree one, the pencil equals ell W and every allowed rational multiplier is p+q m/ell. Self-adjointness applied to u and v imposes −qc/2=qc, hence q=0 over C. This proves the previously missing common-basepoint case; ordinary regularity alone would not prove it. The argument never extends S k-linearly or mistakes a rational eigen-equation for an ordinary eigenvector equation before proving constancy.

### Kernel dimension and exact criterion

For a nonzero exceptional a, division by a in the common rational frame forces the unique equality K_h=t_h d. With two independent exceptional sections, the pencil lemma gives t_h/gamma=lambda in C, and then the whole kernel is exactly ker(S_h−lambda I). Conversely, a two-dimensional eigenspace and K_h=gamma lambda d give that exact actual kernel. Dimension three would make S_h a scalar; trace zero and h nonzero exclude it. Thus the criterion is genuinely if and only if, and simple spectrum implies dim E_h at most one. It does not imply that a one-dimensional exceptional kernel consists of an ordinary eigenline.

### Classification

For a nondegenerate two-dimensional eigenspace E, orthogonal splitting gives a one-dimensional invariant complement with eigenvalue −2lambda. Nonzero S forces lambda nonzero. Conversely, a diagonalizable self-adjoint operator of spectrum (lambda,lambda,−2lambda), lambda nonzero, has the stated nondegenerate repeated eigenspace.

For degenerate E, its orthogonal complement is a line Cu contained in E. The self-adjoint operator T=S−lambda I kills E and has image in Cu, hence T=c B(u,−)u. Since u is isotropic, T²=0 and trace T=0. Trace S=0 forces lambda=0, and nonzero S forces rank one. Conversely, a nonzero rank-one square-zero self-adjoint operator in dimension three has a two-dimensional kernel equal to its image's orthogonal plane; that plane is degenerate. Under binary-quadratic apolarity it is ell W. The canonical compatibility is K_h=0 in this case. A repeated characteristic root without a two-dimensional ordinary eigenspace is insufficient; in particular nonzero nilpotent operators with S² nonzero do not qualify.

### Conic incidence and logical scope

A nondegenerate restricted binary quadratic form has two distinct projective zeros over C. A degenerate orthogonal plane has restricted form of rank one, so its line meets the pure-square conic at one double point. Thus the two conditional incidence statements are correct. For simple spectrum the immutable exceptional locus has at most one projective point, so its conic intersection also has at most one point.

The unknown K_h is retained throughout: the spectral condition alone never asserts existence of a two-dimensional actual kernel. Zero immutable class is only necessary for zero full fourth-square scalar. No conclusion about the separate fourth Bockstein modulo im(beta2), selected surviving directions, or algebraicity follows.

## Audit limits

This is an independent mathematical derivation and exact-source compatibility audit, not a reproof of the full upstream geometric chain. No actual coefficients, source points, derivatives, actual-instance matrix ranks, selected model substitutions, executable symbolic algebra, or large computation were used. Local file operations and hashing only fixed the reviewed artifact. No external repository mutation was performed.
