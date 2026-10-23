# Conditional radical-image reduction of the source2 obstruction pencil

## Theorem and precise scope

Work over C. Retain the actual-source hypotheses and the same fixed negative
pencil identifications of PR790–794 and the invariant multiplication Q of the
pinned actual rank theorem. Write J for the two-dimensional square-zero
radical of the fixed negative-pencil endomorphism algebra. Let

    0 != j=(j2,j3,j4) in J,       Q j2 = j4 Q,
    I_i = im j_i,                barN_i = N_i/I_i.

Existence of such a j is NOT asserted. PR949 proves that all compatible
radical elements, if any, span at most one line. This theorem describes the
remaining represented alternatives without identifying that line.

1. If j is not the pure V-channel direction, Q:I2 -> I4 is an isomorphism
   between two copies of P+D, of dimension nine. For every negative quadratic
   a, the image is a subcomplex of the actual two-term pencil Q+tT_a.
   Its quotient is a 32-to-28 two-term pencil with kernel A+D, cokernel P,
   and invariant rank 24. The natural quotient is a filtered homotopy
   equivalence over C[[t]], so it preserves formal cohomology and every
   t-adic Bockstein page and differential, with their natural identifications.

2. This conclusion includes the unique exceptional mixed radical direction.
   The full three-space quotient dimensions are (32,42,28) there and
   (32,36,28) at every other non-V direction. Only the middle dimension
   changes; it does not compromise the two-term cancellation.

3. If j is pure V, then I2 is exactly the actual D in ker Q and
   im Q=ker j4. Its image two-term Q complex has zero differential
   D -> P, not an invertible differential. The genuine quotient has dimensions
   (36,48,33), invariant rank 29, kernel A+P, and cokernel P.
   The natural kernel map kills D and has image A. It is not an isomorphism
   even on the initial kernel/cokernel page; no Bockstein equivalence is claimed.

These are conditional reductions of the actual specified two-term problem,
not a complete repair, source exclusion, catalogue-pair cut, proof-assistant
certificate, or identification of a general smooth-quadric obstruction.
No actual tensor, coefficient, endpoint, radical slope, matrix or rank at a
selected source instance is evaluated.

## 1. Immutable dependencies and all rank strata

INPUTS.json gives public immutable commits, paths, Git blobs and SHA-256
checksums; inputs/ contains exact originals. The sources are:

- PR790, af0e03d26da5e47d18ae732291aca46f4d448dc5,
  research/hm/source2-first-constant-block/PROOF.md: genuine splitting and
  Section 6 identification with the original fixed negative pencils.
- PR791, 2cd033a4a5ba549d07330427cd779364cb83c0fb,
  research/hm/source2-pencil-endomorphism-algebra/PROOF.md: full radical,
  square-zero property, and contravariant reconstruction orientation.
- PR792, 2f01f18960ce56b8b2a0c1260c277de3c5f916bf,
  research/hm/source2-radical-rank-profile/PROOF.md: the pure V image pencil.
- PR793, ba9234964af5d879675d19ae97847a9475792f98,
  research/hm/source2-a-channel-rank/PROOF.md: the A-channel image maps.
- PR794, 7fd254100b83bb03f41b776ea3119690aa51f671,
  research/hm/source2-radical-rank-locus/PROOF.md: the complete projective
  radical stratification, including its exceptional mixed direction.
- eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c,
  research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md:
  the actual embedded kernel, image and cokernel of Q.
- PR949, e8d9943ed8402be90a6f249a1ad3dd51dcc3c628,
  research/hm/source2-invariant-compatibility/PROOF.md: the compatible radical
  has dimension at most one. Only this description of the remaining frontier
  uses PR949; the conditional image-reduction proof below needs only the
  existence hypothesis on the particular j and the earlier pinned inputs.

Use the inequivalent irreducibles A,V,P,D of dimensions 3,3,4,5, and W',S,T
of dimensions 2,4,6. The relevant actual endpoint types are

    N2=A+2V+3P+4D,  dim41;
    N3=3W'+3S+6T,  dim54;
    N4=2V+4P+3D,   dim37;
    kerQ=A+D, imQ=2V+3P+3D, cokerQ=P.

The complete PR794 image-character list is

    pure V:               (D, T, P),                 ranks(5,6,4);
    exceptional mixed:    (P+D, W'+S+T, P+D),        ranks(9,12,9);
    all other directions: (P+D, W'+S+2T, P+D),       ranks(9,18,9).

The exceptional mixed direction is neither coordinate axis; it is defined
by the split extension in PR794 Section 4, not by a selected scalar value.
Sections 5–6 prove the endpoint ranks uniformly: the A- and V-channel first
D images are independent, and their final P functionals are independent.
Thus no endpoint cancellation occurs at that exceptional direction. Both
residual coupling classes and every balanced endpoint are covered. We make
no assertion about excluded nonbalanced endpoints.

## 2. Image preservation and the forced invertible block

Every j intertwines the two fixed linear pencils. Their compositions and
linear combinations therefore give

    j4 T_a = T_a j2

for every negative quadratic a. Consequently T_a(I2) is contained in I4,
and the analogous linear-arrow containments make I a genuine three-space
subpencil. The extra compatibility hypothesis gives Q(I2) contained in I4.
This uses actual induced subspaces, not a chosen abstract bundle splitting.

Suppose j has nonzero A-channel component. Both I2 and I4 have character
P+D, by the exhaustive rank list. The restriction of Q to the P in I2
is injective, since the actual ker Q=A+D contains no P. It maps onto the
P in I4 by equivariance and equality of their irreducible dimensions.

To treat D, the map induced by j4 is a well-defined equivariant surjection

    N4/imQ -> I4/j4(imQ),      [y] |-> [j4 y].

The source is P. Hence the target has no D constituent. Since I4=P+D,
its entire D is contained in j4(imQ). Compatibility gives the exact equality

    j4(imQ)=Q(j2(N2))=Q(I2).

Thus Q(I2) contains the D in I4 as well as its P. Therefore Q:I2 -> I4
is onto and, both spaces having dimension nine, is an isomorphism.
In particular I2 has zero intersection with kerQ, and I4 is contained in
imQ. This is stronger than a matching-character assertion: the actual
restricted map is forced invertible.

The ordinary two-term quotient long exact sequence, with this acyclic
subcomplex, identifies ker barQ naturally with kerQ and coker barQ with
cokerQ. Its dimensions are32 and28; its rank is32-8=28-4=24.
All assertions so far include the exceptional mixed slope.

## 3. Explicit formal cancellation, including the filtration

Fix any negative quadratic a and put R=C[[t]], M=Q+tT_a. There is an exact
sequence of complexes of free R modules

    0 -> [I2[[t]] --M_I--> I4[[t]]]
      -> [N2[[t]] --M--> N4[[t]]]
      -> [barN2[[t]] --barM--> barN4[[t]]] -> 0.

The constant coefficient M_I(0)=Q|I2 is invertible. Thus M_I is invertible
in R, with inverse obtained by the formal geometric series. No convergence
or evaluation of t is needed.

For completeness choose arbitrary constant vector-space complements to I2
and I4, only to display the proof. In these coordinates the differential is

    M = [ B(t)  C(t) ]
        [  0    D(t) ],       B(0) invertible, D=barM.

The absence of a lower-left block is exactly image preservation. The domain
change (x,y) -> (x-B(t)^(-1)C(t)y,y) transforms this differential into
B(t) direct-sum D(t), without altering the quotient coordinate. Every entry
of this change and of its inverse lies in R; both preserve every t^m level.
The B summand contracts by B(t)^(-1). More explicitly the quotient projection
p has filtered chain section

    s0(y)=(-B^(-1)C y,y),      s1(z)=(0,z),

and the degree-minus-one filtered homotopy is

    h(v,z)=(B^(-1)v,0).

Direct multiplication gives M s0=s1 D, p s=1,

    h M = 1-s0 p0,        M h = 1-s1 p1.

All maps commute with multiplication by t and preserve its filtration.
These equations prove a filtered homotopy equivalence, not merely an
unfiltered quasi-isomorphism. They remain true after reduction modulo t^m
for every positive m. Consequently the t-adic exact couples and their
successive Bockstein pages/differentials are naturally identified by p.
Equivalently, the induced associated graded chain map is a homotopy
equivalence, and the same identities identify every subsequent page.

The proof works for every a, and also over the formal power-series ring in
finitely many formal negative-quadratic deformation variables, with maximal-
ideal filtration. This optional multivariable statement does not identify
its spectral sequence with any different geometric obstruction construction.
No claim is made that the chosen complements are horizontal, that the
constant block remains a direct summand of the entire module, or that the
quotient pencil has no extra endomorphisms. The preserved Bocksteins are
precisely those of the displayed actual two-term family.

## 4. The pure V alternative and its different quotient

Now assume j is pure V. Then I2=D and I4=P. By equivariance and inequivalence,
Q:I2 -> I4 is zero. Hence I2 is a D contained in kerQ=A+D and must be the
whole D-isotypic summand of that actual kernel. Compatibility gives j4Q=0,
so imQ is contained in kerj4. Their dimensions both equal33, since j4 has
rank4 on N4 of dimension37. Therefore

    I2=(kerQ)_D,              imQ=kerj4.

Square-zero implies I4=imj4 is contained in kerj4=imQ. In the two-term image
complex at t=0 the differential is zero, and its cohomology is D in degree
zero and P in degree one. The quotient long exact sequence becomes

    0 -> D -> A+D -> ker barQ -> P -> P -> coker barQ -> 0.

The middle map P=I4 -> P=cokerQ is ZERO because I4 is contained in imQ.
Thus there are natural exact sequences

    0 -> A -> ker barQ -> P -> 0,       coker barQ = cokerQ=P.

Representations over C of this finite group are semisimple, so ker barQ
has type A+P, without asserting a canonical splitting of the short exact
sequence. Its dimension is7. The quotient endpoints have dimensions36
and33, so rank barQ=36-7=33-4=29. Its middle space has dimension54-6=48.
The natural kernel map A+D -> ker barQ kills D and maps its A onto the
indicated subspace A. It therefore is not an isomorphism. This explicit
failure at the initial cohomology page rules out claiming the acyclic
cancellation or its Bockstein conclusion in the pure V case.

## 5. Meaning of the reduction and reproducible checks

When the compatible radical is zero, this theorem supplies no radical-image
quotient. When it is a line, its projective type falls into exactly one of
the three imported rank strata. The non-V two-term reduction eliminates nine
source and nine target dimensions without losing any formal obstruction
information for Q+tT_a; the exceptional middle rank is fully retained.
The pure V alternative instead forces exact kernel/image alignments and a
different, non-equivalent quotient. None of these alternatives is asserted
to occur, and the four necessary catalogue pairs remain unchanged.

verify.py checks source digests, character subtraction for all three strata,
all constituent rank possibilities in the forced invertibility argument,
and exact bounded formal-series block cancellation and homotopy identities
in universal synthetic models. It also tests a pure V negative-control model
with the forced endpoint types and verifies the quotient kernel change.
These are reproducible checks of the new algebraic reduction, not sampled
actual-source computations or substitutes for the cited geometric proofs.
