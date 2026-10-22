# Exact ambient adjoint deformation cohomology and its parity

## Theorem

For the normalized HM bundle F on P4 and B=End_0(F),

    H1(B) is isomorphic to sl5 as an actual normalizer representation,
    h1(B)=24,   h2(B)=2,
    H0(B)=H3(B)=H4(B)=0.

For the standard HM inversion, their parity dimensions are

    H1(B): (12,12),
    H2(B): (0,2).

Consequently, for every smooth inversion-even quadric Q, the actual twist-two restriction sequences are

    0 -> H0(B_Q(2))_+ -> C^12 --m_q,+--> C^41
      -> H1(B_Q(2))_+ -> 0,

    0 -> H0(B_Q(2))_- -> C^12 --m_q,--> C^44
      -> H1(B_Q(2))_- -> C^2 -> 0.

The last two-dimensional quotient in the odd sequence is the actual ambient H2(B), not an expected-dimension correction. No injectivity of either multiplication block is asserted.

## 1. A finite-stabilizer lemma for the actual normalizer

Let V be the five-dimensional Schrödinger representation defining the actual projective HM action. Under conjugation by H5, End(V) is the sum of all25 characters of H5/center, each with multiplicity one. This follows either from the standard deck-operator basis or from its character: the identity has trace25 and every nonidentity element of the projective Heisenberg group has trace0. The scalar summand is the trivial character. Therefore sl(V) is the sum of the24 distinct nontrivial characters.

The normalizer quotient N5/H5=SL2(F5) acts transitively on those24 characters. Every N5-invariant subspace of sl(V), first decomposed into its H5-character spaces, must consequently be either zero or all of sl(V). Thus sl(V) is irreducible as an N5-module.

Let Z be a proper nonempty N5-invariant closed subscheme of P(V), and let G_Z be its projective stabilizer. It is a closed algebraic subgroup of PGL(V), and its Lie algebra is an N5-invariant subspace of sl(V). If that Lie algebra were all sl(V), then the identity component of G_Z would be PGL(V). A proper nonempty subscheme cannot be invariant under the transitive PGL(V) action. Hence Lie(G_Z)=0. In characteristic zero a finite-type algebraic group with zero Lie algebra is finite.

Apply this to the actual25-line evaluation-degeneracy scheme C. The HM bundle is N5-equivariant, so C is N5-invariant. Any projective transformation preserving the isomorphism class of F also preserves C: evaluation and its degeneracy scheme are intrinsic to F(3). The projective HM stabilizer is therefore a subgroup of the finite G_C, and is finite as well.

This proves the finiteness needed below from the actual normalizer representation and intrinsic evaluation geometry. It does not assume that N5 is the entire projective stabilizer, and does not require coordinates for any HM line or differential.

## 2. The projective orbit saturates the tangent space

The stable bundle F is simple. The tangent space to its deformation functor is

    Ext1(F,F)=H1(End F)=H1(B),

since H1(O_P4)=0. Pullback by projective transformations defines an orbit map whose tangent at the identity is the natural normalizer-equivariant map

    sl5 -> H1(B).

Its kernel is the Lie algebra of the projective stabilizer. Section1 makes that kernel zero, so h1(B)>=24.

PR455 Section3 proves h2(B)<=2, using the normalized symmetric-square monad, a universal exterior-image lower bound, and the24-character normalizer orbit. It makes no no-quartic assumption. The actual ambient resolution calculation in LOWER-TWIST-EVEN-QUADRIC-PARITY.md gives H0(B)=H3(B)=H4(B)=0 and chi(B)=-22. Thus

    h1(B)-h2(B)=22,
    h1(B)<=24.

Together with the orbit injection this forces h1(B)=24 and h2(B)=2. The equivariant injection between equal-dimensional spaces is an isomorphism, proving the stated actual N5-module identification of H1(B).

## 3. The inversion characters

The ambient involution on V has eigenspace dimensions3 and2. Its conjugation trace on End(V) is

    trace(iota|V) trace(iota|V*)=(3-2)^2=1.

Subtracting the scalar summand gives trace(iota|sl5)=0. Hence H1(B) has parity(12,12).

The independently checked ambient equivariant Euler characteristic is chi^iota(B)=-2. Since only H1 and H2 survive,

    -trace H1(B)+trace H2(B)=-2.

It follows that trace H2(B)=-2. Its dimension is2, so it is entirely odd. This also agrees with PR455's result that H2(B) is H5-trivial; its remaining normalizer action is not being replaced by a trivial representation.

## 4. Exact lower restriction, with the obstruction quotient retained

The actual restriction sequence

    0 -> B --q--> B(2) -> B_Q(2) -> 0

and the proved ambient cohomology give

    0 -> H0(B_Q(2)) -> H1(B) --m_q--> H1(B(2))
      -> H1(B_Q(2)) -> H2(B) -> 0.

Here H1(B(2)) has actual parity(41,44), while H2(B(2))=0. For even q all arrows preserve parity. Splitting the displayed exact sequence therefore gives exactly the two sequences stated in the theorem. In particular

    h1(B_Q(2))_+=29+h0(B_Q(2))_+,
    h1(B_Q(2))_-=34+h0(B_Q(2))_-,

now with the two odd ambient obstruction classes identified, not merely their index.

The identification H1(B)=sl5 does not replace m_q by a freely chosen map, by the action of vector fields on the equation q, or by a stabilizer calculation for Q. It remains the actual quadratic multiplication on adjoint cohomology. Its ranks require a separate proof.

## 5. Local moduli scope: nearby bundles add no new direction

Take the coarse moduli scheme M of O(1)-Gieseker-stable sheaves on the fixed P4 with the Hilbert polynomial of F. The slope-stable F is a point of this stable locus. Use the standard stable-sheaf local deformation identification T_[F]M=Ext1(F,F); scalar automorphisms act trivially, and locally free sheaves form an open locus. These hypotheses distinguish the statement from arbitrary coarse moduli problems where a tangent space need not equal the deformation space.

The projective orbit through[F] is locally closed of dimension24. Therefore the local dimension of M at[F] is at least24. Its embedding dimension equals dim Ext1(F,F)=24, and local dimension never exceeds embedding dimension. Equality holds, so the local ring of M at[F] is regular. Over C this says that M is smooth of dimension24 near[F]. The orbit map has an isomorphism on tangent spaces there; it follows that the orbit is open near[F].

Consequently every sufficiently nearby stable-bundle isomorphism class on the fixed P4 is projectively induced from F. Locally analytically, or after the appropriate etale base change for a family, one may choose such projective transformations. Thus simultaneously varying a nearby F and a quadric adds no local route beyond transporting the quadric while keeping F fixed. This is only a local statement, not a classification of other components or distant bundles.

The two-dimensional H2(B) is an available obstruction space, not proof of nonzero obstructions. The orbit/dimension argument proves the local smoothness just stated despite that nonzero space. It says nothing about the original abelian or spectral higher-lifting problem, nor about ranks of any quadric multiplication map.

## Boundary and sources

This proves exact ambient cohomology, its normalizer tangent representation, and the two genuine odd obstruction classes. It asserts neither lower-twist section vanishing on even quadrics nor full-adjoint invertibility. The local smoothness statement is confined to stable-sheaf deformations on the fixed P4 under the explicit hypotheses in Section5; it is not an assertion about the separate higher-lifting problem.

The upper bound h2(B)<=2 is PR455 at8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, research/hm/twist-one-structural-vanishing/PROOF.md, Section3:
https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md

Actual H5/N5 representations and normalized HM equivariance are in ADHPR Sections1 and3:
https://arxiv.org/pdf/alg-geom/9606013v2

The ordinary and equivariant Euler calculations, higher vanishings, and actual degree-two restriction data are in LOWER-TWIST-EVEN-QUADRIC-PARITY.md and FULL-ADJOINT-PENCIL-INVOLUTION-BLOCKS.md. No selected HM coefficients, matrices, or ranks have been evaluated.

For the standard first-order sheaf deformation identification, see Hartshorne, Lectures on Deformation Theory, Theorem2.6:
https://math.berkeley.edu/~robin/math274root.pdf
The local commutative-algebra criterion used in Section5 is the dimension/embedding-dimension criterion in Stacks Project, Section10.60:
https://stacks.math.columbia.edu/tag/00KD
