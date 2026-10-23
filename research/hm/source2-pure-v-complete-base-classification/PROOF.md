# Complete base-scheme stratification of the universal pure-V gate

## Theorem

Retain the conditional pure-V source2 gate and its fixed basis
R=alpha R1+beta R2. Its nonic component row is F=alpha F1+beta F2.
The base scheme is defined by the component IDEAL SHEAF, equivalently
the saturated homogeneous ideal, not the raw four-generated graded ideal.
Let Z have the six prescribed length-four C5 ideals (u^2,v^2) and
ten reduced C3 points, hence length34. Write E15 for the reduced
fifteen order-two axes and E12 for the reduced conic twelve-orbit.

For every NONZERO coefficient pair, the entire base scheme B(F) is
determined by exactly one of the following five disjoint strata:

| Coefficient condition | Complete scheme | Length |
|---|---|---:|
| beta=2alpha | m^3 at six C5 axes, m at ten C3 axes | 46 |
| beta=-2alpha | Z's six C5 ideals, m^2 at ten C3 axes | 54 |
| beta=-alpha | Z disjoint-union E15 | 49 |
| beta=0 | Z disjoint-union E12 | 46 |
| beta(beta+alpha)(beta-2alpha)(beta+2alpha) nonzero | Z | 34 |

Here m denotes the ambient smooth-surface maximal ideal at the indicated
point. The first four equations specify distinct projective points;
the last stratum includes [alpha:beta]=[0:1]. There are no additional
points, embedded thicknesses, divisorial components, or unlisted local
ideals for the nonic component scheme in any stratum.

The zero coefficient pair is separate: F=0, its ideal is zero, and its
base scheme is the entire plane. It has no finite length. No claim selects
whether the actual conditional gate is zero or which nonzero ratio it has.

## Exact inputs and what is newly completed

INPUTS.json retains seven immutable public proofs. PR1030 establishes
finite base schemes and exact prescribed local ideals off the two jet
lines; PR1035 bounds every possible extra orbit; PR1036 places the four
distinct lines. PR1037 determines both exceptional jet schemes exactly.
PR1040 determines the reduced fifteen-axis scheme and its occurrence line.
PR1042 excludes every thirty-point orbit. PR1043 determines the reduced
ambient conic scheme and its complete length46 case.

The separate special-case schemes are those earlier theorems, not new
claims of this packet. The new conclusion is their exhaustive scheme
stratification, especially equality B(F)=Z on the entire complement of
the four points, and elimination of all formerly possible extra-support
and multiplicity alternatives there. This is not a reclassification by
length alone: both length46 strata have different support and ideals.

## 1. Partition of the coefficient projective line

In characteristic zero the four homogeneous linear forms beta-2alpha,
beta+2alpha,beta+alpha,beta are pairwise independent. Their kernels
intersect only at the zero pair. Hence a nonzero pair is either on one
and only one of the four lines, or their product is nonzero. If alpha=0
and beta is nonzero, the product is beta^4, so infinity is included in
the last stratum. This is a symbolic exhaustive partition, not a test
of sampled coefficient values.

PR1037 proves the first two complete schemes, including exact local
ideals by whole-orbit Nakayama identities. PR1040 proves the third, and
PR1043 proves the fourth. Their support exclusions are part of those
proofs. It remains to determine the whole last stratum, not merely its
generic member.

## 2. Every member of the open stratum has exactly Z

Take any pair with the displayed product nonzero. It lies off both jet
lines, so PR1030 gives equality with the prescribed ideal at every point
of Z. It is off beta=0, so PR1036 and the conic theorem give no conic
basepoint. It is off beta=-alpha, so PR1040 gives no fifteen-axis point.
PR1042 excludes all thirty-point orbits for every nonzero member, not
just generically. PR1035 exhausts the possible additional support and
excludes free orbits and every other possibility. Thus the support is
precisely that of Z.

Equality of the local ideal sheaves at every point of this support,
and the unit ideal elsewhere, proves equality of ideal sheaves globally.
This excludes any additional embedded finite structure as well as new
support. Therefore B(F)=Z for EVERY pair in the open stratum and its
length is exactly34. No further exceptional coefficient ratio can be
hidden inside this stratum.

## 3. Boundaries of the completed classification

This theorem classifies the component ideal of the NONIC QUOTIENT-THIRD
gate s (equivalently F). It does not identify that ideal with the component
ideal of the original fourth, represented by composition with L. Although s vanishes identically if and only if the original fourth on D
vanishes identically, L fails to be onto at the ten C3 axes and composition
can change local base ideals there. The matrix
rank and rank-drop scheme of the quadratic lift R are a third object.

The coefficient ratios are universal coordinates, not actual HM values.
The theorem does not assert existence of a compatible pure-V radical,
realization of a source, nonvanishing of its gate, or a complete original
proof repair. It completes this universal base-scheme question conditional
on the pinned identifications and hypotheses. The four source-dual pairs
are not reduced by this classification alone.

## Reproducibility

The accompanying checker authenticates all seven inputs, verifies pairwise
independence of the four coefficient forms and the homogeneous infinity
condition, and checks the exact local-length accounting and scheme labels.
The geometric exhaustion is the written deduction from the imported
support and local-ideal theorems, not a claim that a finite test proves
them. No actual coefficient or parameter instance is evaluated.
