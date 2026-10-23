# A second reduction from the zero-arrow space of the regular source2 quotient

## Result and boundaries

Work over C, retaining the actual-source hypotheses of the pinned source2
results. Suppose a nonzero radical endomorphism j is compatible with the
actual invariant quadratic Q, and its projective direction is neither pure V
nor the unique exceptional mixed direction. These existence and direction
hypotheses are not asserted to hold. Let barN=N/im(j) and barQ be induced by Q.

The intrinsic common kernel Z of the first negative arrows on barN has
character V+D and dimension8. Every induced negative quadratic T_a kills Z.
Exactly two representation-theoretic alternatives remain:

1. rank(barQ|Z)=8. A further constant acyclic cancellation reduces the
   already reduced32-to-28 complex to a24-to-20 linear pencil. Its invariant
   kernel remains A+D, cokernel P, and rank16. The natural quotient preserves
   the formal cohomology and every t-adic Bockstein of the original41-to-37
   pencil Q+tT_a, for every negative quadratic a.

2. rank(barQ|Z)=3. The whole D in Z is a constant kernel of barQ+tT_a for
   every a. There is a filtered homotopy equivalence to the direct sum of
   D in degree zero and an active24-to-25 linear pencil. The active invariant
   kernel is A, cokernel P, and rank21. The original41-to-37 pencil therefore
   has rank at most36 on the entire affine family Q+Sym²W of negative-
   quadratic perturbations. In particular it is never onto on that family.

Thus surjectivity anywhere in this particular affine family would force
rank(barQ|Z)=8. No surjectivity is assumed or proved, and no source or
catalogue pair is excluded. The statement concerns precisely q0+t a with a
in the fixed negative quadratic space; it does not identify this family
with all positive or all smooth quadrics.

This reduction does not assume barQ preserves any decomposition of the
negative pencil. Its off-diagonal blocks are retained and explicitly removed
only by valid two-term chain operations. No actual coefficient, parameter,
slope, derivative, tensor, matrix or source-instance rank is selected.

## 1. Exact inputs and recovery of the zero-arrow space

INPUTS.json records the immutable public URLs, commits, Git blobs and hashes
of five original proof files copied in inputs/:

- PR790, af0e03d26da5e47d18ae732291aca46f4d448dc5,
  research/hm/source2-first-constant-block/PROOF.md.
- PR794, 7fd254100b83bb03f41b776ea3119690aa51f671,
  research/hm/source2-radical-rank-locus/PROOF.md.
- PR795, 3f811311d76914a555c7e7d0c5b887b41805aa6c,
  research/hm/source2-radical-filtration/PROOF.md.
- PR950, 54c7e78bd5351b3ecbdcc4b3b558a0012eb79566,
  research/hm/source2-radical-image-reduction/PROOF.md.

- PR953, 9c12c02a601cc380e2e2cf233e7b37dddd46d563,
  research/hm/source2-radical-quotient-normal-form/PROOF.md.

We repeat PR953's short regular-quotient argument to identify its intrinsic
zero-arrow space explicitly. PR790 gives a genuine negative-pencil splitting
N=N0+NR. PR795 gives the genuine exact sequence0->NC->NR->N8->0.
For the projective directions retained here, PR794 identifies I=im(j)
inside NC, with ranks(9,18,9) and characters(P+D,W'+S+2T,P+D).
NC has characters(V+P+2D,W'+S+2T,P+D), ranks(17,18,9).
Consequently NC/I=(V+D)[2], an isolated initial vertex, and

    0 -> (V+D)[2] -> NR/I --p--> N8 -> 0.

Here p3,p4 are isomorphisms. Take any equivariant section s2 of p2,
which exists by semisimplicity over C, and s3=p3^-1,s4=p4^-1. Naturality
and the invertibility of p3,p4 show that these commute with each fixed
linear pencil arrow. Thus, as actual fixed negative pencils,

    barN is isomorphic to N0 + N8 + (V+D)[2].                  (1)

The isomorphism is not canonical and need not intertwine barQ with a
block-diagonal map. It also does not split the original residual bundle.

Every nonzero first arrow on N0 is the injective multiplication
Sym^8(W)->Sym^8(W) tensor W by its fixed nonzero linear form. Every nonzero
first arrow on N8 is injective multiplication A tensor Sym^4(W) ->
A tensor Sym^5(W), as in PR795 Section8. It follows from(1) that

    Z = intersection over l of ker(barA_l)
      = ker(barA_l) for each nonzero l,
    Z has character V+D.                                       (2)

This definition is intrinsic, independent of the chosen splitting. Since
negative quadratics are compositions and linear combinations of these
fixed linear arrows, every barT_a kills Z. It follows that for all a,t,

    (barQ+t barT_a)|Z = barQ|Z.                                (3)

The non-V image cancellation theorem PR950 applies to our j and identifies
the formal two-term original with barN2->barN4, preserving its Bocksteins.
It also gives the actual embedded kernel/cokernel types

    ker barQ=A+D, coker barQ=P,
    barN2=A+2V+2P+3D,  dim32,
    barN4=2V+3P+2D,    dim28.                                 (4)

All of its upstream hypotheses remain in force.

## 2. Exactly two ranks on the intrinsic zero-arrow space

Let F=barQ|Z. Since ker barQ has no V constituent, F is injective on the V
in Z. Since D in Z is irreducible, F on that D is either zero or injective.
The V and D images cannot overlap, being inequivalent irreducible G
representations. Therefore rank F is exactly3 or8. No character count is
being substituted for an evaluated actual rank: we retain both alternatives.
Put L=ker F and Y=im F. Then the two cases are

    rank8: L=0, Y=V+D;
    rank3: L=D, Y=V.

In the second case, L is exactly the D in the actual kernel of barQ,
by its uniqueness in the multiplicity-free kernel A+D. Equation(3) shows
that L is killed by the entire deformed pencil, not only its first-order
obstruction. This is the extra force supplied by the zero-arrow condition.

## 3. Quotient construction and explicit filtered chain equivalence

Define the active pencil without a choice of complements by

    C2=barN2/Z,     C4=barN4/Y,
    M_C(t)[x]=[(barQ+t barT_a)x].                               (5)

It is well defined because(3) sends Z into Y. It is still linear in t.
No projection onto a supposedly Q-stable block is used.

Here is a general elementary cancellation proving the precise relationship.
Choose constant vector-space complements Z=L+Z', barN2=Z+X and
barN4=Y+W. The restriction F:Z'->Y is an isomorphism. With domain ordered
L,Z',X and target Y,W, the entire pencil has the form

    M(t) = [ 0  F  C(t) ]
           [ 0  0  D(t) ],      D(t)=M_C(t).                  (6)

The zero first two lower blocks follow from (3); the first column is zero
because L is killed by(3). C(t) need not vanish and includes every permitted
off-diagonal contribution of barQ and barT_a. The change of domain

    (l,z,x) |-> (l,z-F^-1 C(t)x,x)

is invertible over C[t] and C[[t]], with inverse obtained by changing the
minus sign to plus. It preserves every t^m filtration level. It transforms
(6) into the direct sum of the zero differential on L in degree zero, the
constant invertible block F, and D(t). Contract F with F^-1. This gives a
filtered homotopy equivalence

    [barN2[[t]] -> barN4[[t]]]
          equivalent to L[[t]][0] + [C2[[t]] -> C4[[t]]].    (7)

The argument works modulo t^m for every m, so it identifies the t-adic
Bockstein pages/differentials of these complexes. Combined with PR950,
(7) applies to the original complex as well. It is not an assertion that
the original three-vertex pencil or the whole HM module splits this way.

If L=0, (7) is exactly the natural active quotient equivalence and loses
no obstruction information. If L=D, it identifies a separate permanent
kernel summand with zero Bockstein differentials at every order; the active
complex alone is not equivalent to the original, and that D must be retained.

## 4. Exact sizes and invariant cohomology of the active pencil

In both cases the active source has character

    C2=(A+2V+2P+3D)-(V+D)=A+V+2P+2D,    dimension24.

For rank8, C4=V+3P+D has dimension20. Acyclic cancellation identifies its
invariant kernel with A+D and cokernel with P, so its rank is24-8=20-4=16.

For rank3, C4=V+3P+2D has dimension25. The kernel of the removed complex
Z->Y is exactly D, and it is surjective. Its long exact sequence gives

    ker(M_C(0))=(ker barQ)/D=A,     coker(M_C(0))=P.

Hence the active rank is24-3=25-4=21. These character statements follow
from exact sequences, not a guessed block-diagonal structure on(1).

## 5. Rank-three restriction obstructs surjectivity along the whole family

In the rank3 case, equation(7) supplies a free rank-five formal kernel from
D. Thus over C((t)), barQ+t barT_a has rank at most32-5=27. The original
complex differs by the formally invertible nine-dimensional image block of
PR950, so Q+tT_a has rank at most9+27=36 over C((t)).

For a fixed arbitrary a, every37-by-37 minor of the original linear matrix
Q+tT_a is a polynomial in t. Its vanishing in C((t)) means that polynomial
is identically zero. Therefore the original rank bound36 holds at EVERY
complex scalar t, even at values where the previously cancelled image block
might cease to be invertible. This last step is a polynomial identity,
not an extension of formal invertibility to those values. Since a was
arbitrary, the bound holds along each allowed negative-quadratic family.

The same statement has a simultaneous multivariable formulation. Use formal
coordinate symbols z1,z2,z3 on the fixed negative-quadratic space Sym²W,
without selecting any actual parameter values. Over R=C[[z1,z2,z3]],
the pencil Q+sum z_i T_i still preserves I, its nine-dimensional image
block still has invertible constant term, and its induced quotient kills
the same D because every T_i kills Z. Over the fraction field of R this
gives original rank at most36. Each37-by-37 minor is a polynomial in the
three variables; the natural injection C[z1,z2,z3] into R makes it
identically zero. Thus rank at most36 holds at every point of the entire
affine family Q+Sym²W, including points outside the formal neighborhood.
This is only a polynomial-identity consequence; no actual point is evaluated.

The original target has dimension37. Therefore surjectivity anywhere in
this affine family forces the rank8 alternative for F. The theorem does not
supply surjectivity or an actual value of F, so no source is eliminated.
The scalar-compatible-algebra alternative with no nonzero j, the pure V
radical line, and the exceptional mixed line lie outside this conditional
regular-direction theorem and remain untreated by it.

## Verification boundary

The checker verifies input digests, the two Schur rank alternatives,
character/dimension subtraction and exact constant-block elimination for
bounded synthetic matrix families. It also confirms the persistent kernel
and the two invariant cohomology profiles in synthetic controls. The
universal proof, not a finite sample, establishes(2)–(7) and the all-t rank
bound. No actual-source evaluation, experiment restart, or proof-assistant
certification is claimed. The original repair and four-pair frontier remain
open.
