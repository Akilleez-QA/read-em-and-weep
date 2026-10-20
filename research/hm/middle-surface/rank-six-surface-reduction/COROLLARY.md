# Integrated rank-six bound and the remaining rank-at-most-five locus

## Hypotheses and dependencies

Work over C. Assume:

1. dim V=5 and f:V x V x V -> J is trilinear, outer symmetric, and cyclic-zero.
2. For every nonzero a, [b] -> f(a,a,b) is injective on V/Ca.
3. The projective middle residual-rank-drop support has dimension at most two.

Let E_u=V/Cu, let Q_u be the established residual symmetric map on
Sym^2 E_u, and let K_u=ker Q_u. The source of Q_u has dimension ten.
All zero triples considered here have three linearly independent inputs.

The proof combines:

- ./PROOF.md: the exhaustive full-support rank-six surface reduction;
- /research/hm/normalizer-rank-five/rank-six-cubic-web/PROOF.md and REDUCIBLE.md: every supported-ternary
  four-dimensional kernel has compatible rank-two locus of dimension at most one;
- /research/hm/middle-surface/extremal-surface-geometry/GENERALIZATION.md: finiteness of C_{1,3}
  and C_{2,2}, and the cross-block compatibility reconstruction;
- /research/hm/middle-surface/extremal-surface-geometry/PROOF.md: the rank-seven bound;
- ../rank-nine-independent-incidence/PROOF.md: ordered-factor reconstruction,
  the rank-nine and rank-eight bounds, and the rank-ten exclusion.

This is an integration corollary. It does not replace the hypotheses or
prove any occurrence of the residual ranks under discussion.

## 1. Every rank-six middle fiber has dimension at most two

Fix [u] with rank Q_u=6, so dim K_u=4. The total tensor support of K_u has
dimension three or four: support dimension at most two would give

    dim K_u <= dim Sym^2(C^2)=3,

a contradiction.

If the support has dimension three, the completed supported-ternary
proof gives compatibility-locus dimension at most one.

If the support has dimension four, ./PROOF.md proves that the compatible
rank-two locus has dimension at most two. When its dimension is two, [u]
belongs to the fixed finite set

    F = image(C_{1,3}->P(V)) union image(C_{2,2}->P(V)).      (1)

The ordered-factor cover is finite of degree two and reconstructs the
separately projectivized independent-zero fiber, with no further
parameters. Thus the projective fiber has dimension at most two at
every rank-six middle line, and at most one outside F.

This is a pointwise assertion for all rank-six middle lines, so it does
not assume a constant support type on the whole middle stratum.

## 2. The entire rank-six independent-zero locus has affine dimension at most six

Let S_6 be the residual-rank-exactly-six middle stratum. Its dimension
is at most two by the middle rank-drop hypothesis. Over S_6 outside F,
the preceding pointwise bound and the fiber-dimension theorem give

    projective independent-zero dimension <= 2+1=3.

Over the finite set S_6 intersect F, the projective dimension is at most
two. Therefore the entire separately projectivized rank-six independent-
zero locus has dimension at most three. Restoring the three independent
nonzero input scalings adds exactly three, yielding

    affine independent-zero dimension over S_6 <= 6.       (2)

The assertions concern support dimensions. Nilpotents or multiplicities
in the determinantal schemes do not affect them.

## 3. A component of dimension at least seven lies entirely over rank at most five

The established bounds, now including (2), are:

    residual rank ten:  no independent zero triples;
    residual rank nine: affine independent-zero dimension at most five;
    residual rank eight: affine independent-zero dimension at most six;
    residual rank seven: affine independent-zero dimension at most six;
    residual rank six: affine independent-zero dimension at most six.

Let Y be an irreducible affine independent-zero component with dim Y>=7.
The largest residual rank attained on Y occurs on a nonempty open subset:
the locus where a bundle map has rank at least a specified value is open,
and the residual map is an algebraic bundle map on the middle projective space. If that largest rank were at
least six, this open subset would have dimension dim Y>=7 while lying
in one of the strata just bounded by at most six, a contradiction.
Consequently every point of Y has middle residual rank at most five:

    Y maps into { [u] : rank Q_u <= 5 }.                   (3)

Thus the rank-six surface analysis sharpens the earlier rank-at-most-six
reduction to rank at most five. It does not prove that the locus in (3)
is empty, and it does not establish a universal independent-zero dimension
bound six in the absence of additional control on residual ranks at most
five.

## Audit scope

The integration uses only abstract tensor kernels and the established
middle-support hypothesis.
