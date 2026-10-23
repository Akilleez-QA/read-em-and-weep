# Independent finite-base-support review

Result: PASS. No mathematical blocker found.

Read the complete final proof, checker, manifest, retained immutable inputs,
and result. The following arguments were checked independently.

## Orbit and mirror geometry

The off-conic stabilizer classification leaves only the known six and ten
axes, the unique fifteen-axis orbit, cyclic-order-two orbits of size thirty,
and free orbits. A Klein four has exactly three projective eigenaxes in A,
which are the axes of its three involutions. Thus there is no extra orbit
of size fifteen omitted by the proof. Each involution mirror contains two
axes from each of the six-, ten-, and fifteen-point orbits. A thirty-point
orbit contributes two points to each mirror, with a unique mirror through
each point. The normalizer and centralizer enumeration correctly checks
these counts without any actual source evaluation.

The fixed base imposes orders totaling at least six on each mirror, and
at least eight on either jet line. Degree nine and absence of a common
curve therefore exclude coexistence of fifteen- and thirty-point extra
orbits, two thirty-point orbits, and every off-conic extra orbit on a jet
line. Free orbits are independently excluded by the Bezout budget.

## Ambient local schemes and budgets

The general fixed contribution is 34, giving residual intersection budget
47. On either jet line the fixed orders give contribution at least 64,
leaving 17. These use local intersection multiplicities, not merely the
length of the prescribed subscheme. Two general members can satisfy all
needed local generation and no-common-component conditions simultaneously.

A simple intersection with the conic does NOT alone imply an ambient
reduced point. It supplies an element of the ideal with nonzero derivative
along the conic, hence a smooth local equation. The finite quotient is then
a quotient of a one-dimensional regular local ring, yielding a curvilinear
complete intersection of length k. Equivariance makes k uniform. Residual
47 bounds k by three off the jet lines; residual 17 forces k=1 on either
jet line when the twelve-point orbit is present. The proof correctly
separates these two conclusions.

At a fifteen-axis point, the two genuine mirror equations have independent
Klein-four characters. The total mirror budget first excludes an ideal
contained in the square of the maximal ideal. If the ideal has a unique
linear character, equivariant averaging gives a series of that character.
Every such monomial is divisible by the corresponding mirror coordinate,
and its linear coefficient is nonzero. Thus the series is that coordinate
times a unit, not a bending branch with only the same tangent. The ideal
is (u,v^l). Its two mirror restrictions have orders one and l; summing over
all fifteen points bounds l by two. This is a valid all-orders argument,
not just a quadratic-jet computation. Thirty-point orbits are reduced by
uniform length and residual budget 47.

The resulting support alternatives and necessary length catalogue follow.
They assert neither occurrence nor a selected actual gate, and they do not
identify the conic line with either jet line.

## Source authentication

Fresh direct GitHub reads in this review session matched the declared
immutable blobs, including the 1030 read made during the immediately
preceding conic-base review:

- PR1030, commit 418a7d9ebedaae9b5d00db9f69e449b5d8767108,
  blob aec4e3f550d3dc4bedb2911019de65e61852c436.
- PR1033, commit 7065160df56ffa7de1bea7e02c01dd98a6219781,
  blob 5625cb9e0a6ee2a53470616b82b3c93d76f0042b.
- PR1000, commit 260cd6a777b23dc7ccd5ed956fcf65e17ff56145,
  blob 0ca1301de04a630cb184c4429f5b59e09698c6c9.

The input path and URL details are retained in INPUTS.json. The imported
finiteness, conic restriction, and old length-34 scheme are not counted as
new results. The new claims reviewed here are the mirror exclusions and
ambient local-length constraints.

## Reproduction and frozen hashes

Independently ran python verify.py and python -O verify.py. Both passed
45 checks, with byte-identical outputs matching RESULT.json. The checker
verifies exact finite group arithmetic, parity, and budgets. The written
proof supplies the geometric interpretation and local algebra.

SHA256:

- PROOF.md: 5bdd5fecb8a680946604394d3ef3f15c953517b920840dd8eeaa4582d9a31fb7
- verify.py: 1bb0f6b9da4067ed76d523e81e80a3c8bac581fd61e86608f6c3acaa3b1d1b9e
- INPUTS.json: b6d33e6ae18de68e1ca28b4a3a2369da77c8e64ac3d276e748d79b931786ef2a
- RESULT.json: 853df102942bdf14dfb7240ac9fda597aaf59793335d318ee1d94e271716cda7

No actual HM coefficient, selected parameter, source instance, or matrix
rank was evaluated. No public files were changed.
