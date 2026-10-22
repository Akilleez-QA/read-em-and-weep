# Independent review: the exact source2 pencil endomorphism algebra

## Verdict and reviewed bytes

**PASS, conditional on the published structural and actual-source inputs
explicitly stated in the proof.** The argument determines the entire
degree-preserving, G-equivariant endomorphism algebra of the two fixed-variable
negative pencils in the stated source2 normal-form class. It includes singular
endomorphisms and does not merely determine the units or construct selected
idempotents.

Reviewed artifact: `PROOF.md` in this directory.

Reviewed proof SHA-256:

`8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290`

No correction to these proof bytes is required by this review. For zero
residual quotient coupling the algebra is `C times T(J)`, of dimension five;
for nonzero residual quotient coupling it is `T(J)`, of dimension four. In
both cases its Jacobson radical is exactly the two-dimensional square-zero
ideal J. The semisimple quotients are respectively C^3 and C^2.

This is a deductive written mathematical review, not proof-assistant
certification. It does not calculate the algebra of the fixed actual HM
tensors, decide their residual class, establish an HM realization, or exclude
source2. The result concerns the two specified pencils, not the full HM
module or bundle.

## 1. Direct published dependencies and their roles

The three direct public proofs were retrieved at the immutable commits below.
The complete UTF-8 contents have the following SHA-256 values:

- [PR788, universal constant flag and common-pencil reconstruction](https://github.com/Akilleez-QA/read-em-and-weep/blob/941b7b3b77dc8ae8a19b1e000dddeb0438d05db7/research/hm/source2-universal-constant-flag/PROOF.md).
  Commit `941b7b3b77dc8ae8a19b1e000dddeb0438d05db7`;
  SHA-256 `81bb2d40705fa1e35f5719ef59323cd60af675ebe74015651dda9590a2488f29`.
- [PR789, residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md).
  Commit `2d1642ad40ae1111b84b50eeaca0426bfbfbb314`;
  SHA-256 `7eb626caae70e62613e8a3e318ac4c6a858502c4fdecfb44a6693e3ed85635c3`.
- [PR790, first constant block and fixed-pencil summand](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md).
  Commit `af0e03d26da5e47d18ae732291aca46f4d448dc5`;
  SHA-256 `0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4`.

PR788, Section 6, supplies the common-pencil construction, evaluation
presentation, and Koszul middle-cohomology recovery. It does not itself
identify its separately constructed split witness with the actual HM tensors.
The reviewed proof correctly uses PR790, Section 6, for that additional
identification under the actual-source hypotheses.

PR789 supplies the graph description of R, the two-dimensional coupling
space, the injective one-dimensional constant-shear image, and the exact
residual backward flag for every coupling at every balanced endpoint.
PR790 supplies the genuine constant splitting of the degree-ten block, the
one-dimensional restriction isomorphism to Hom_G(A0,Z), and the nonzero
restriction of its constant D channel. These are exactly the inputs used;
an ordinary bundle splitting is never substituted for a constant one.

The upstream actual-source hypotheses remain the pinned PR744, PR751, and
PR758 statements listed in Section 1 of the reviewed proof: respectively
commits `2348d4b6fb2afd67d66b15aad6037ab92c94f076`,
`e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169`, and
`063216038f3aefd65617651c2426721efafc7f9b`, with the exact file paths given
there. The balanced endpoint locus is the PR754 statement at
`044add76ebb14043a0edf73171517c90b9ef0c13`. The present audit checks the
new deduction and its use of the three direct published dependencies; it
does not claim a fresh foundational certification of their entire upstream
dependency graph.

## 2. Intrinsic preservation works for noninvertible maps

For a constant f preserving a subbundle S, the induced maps on S and its
ambient quotient intertwine the second fundamental form. This follows
directly from `d(f s)=f(ds)`. Consequently f preserves its kernel S^-.
Repeating the same argument preserves every backward kernel. The existence
of an inverse, injectivity of f, and constancy of its restriction's rank are
irrelevant. This is a sheaf statement and remains valid where a second
fundamental form has exceptional fiber behavior.

In the full normal form, the eighth backward kernel is U_0^10 and its
constant span is V0. Thus f preserves V0. The scalar lemma is particularly
effective here: an endomorphism of a line bundle over P1 is multiplication
by one global constant, including zero. Subtracting this scalar from f
kills the line bundle, hence its entire constant span. It follows that
f|V0 is scalar and that no map from V0 to the residual constant quotient
survives. If the scalar is zero, f kills V0, rather than acquiring any
additional lower off-diagonal freedom.

For the induced residual endomorphism d, the second backward kernel is
U_0^8. Its span similarly recovers V1, and d|V1 is scalar. The induced
map on the genuine constant quotient F_t preserves the endpoint line C;
its full span makes that map scalar as well. This justifies the complete
upper-triangular forms (8) and (10) for all endomorphisms, not only for
automorphisms preserving a flag chosen in advance.

## 3. The residual endomorphism equation is exhaustive

After quotienting by A0, R is the actual graph of alpha. An endomorphism
of the form (10) preserves this graph if and only if

`(a1-a2) alpha + sigma_t(p) = 0`.

The second component determines the graph parameter to be a2 times the
original one, even when a2 is zero. No division occurs. Conversely the
equation makes the graph invariant and therefore preserves its full inverse
image R. Thus it is both necessary and sufficient for arbitrary maps.

When the quotient class of alpha is zero, the allowed constant shear puts
alpha=0, after which the injectivity of sigma_t forces p=0. The two
diagonal scalars remain independent. When the quotient class is nonzero,
passing to the one-dimensional quotient coupling space forces a1=a2;
injectivity then again gives p=0. This proves the full residual algebras
C^2 and C, respectively. It is not an inference from a previously computed
invertible stabilizer. The constant change of gauge in the zero case
conjugates the full algebra and does not restrict which endomorphisms are
being counted.

## 4. Exactly the A and V channels survive above the residual

The multiplicity-free decompositions

`V0=A+V+D`, `V1=P+D`, and `F_t=A+V+P`

give precisely three possible constant maps Hbar->V0: one D channel
supported on V1, and one A and one V channel supported on F_t. There is
no fourth P channel. The remaining preservation condition is exactly the
kernel of restriction modulo U to Hom_G(R,Z).

The A and V channels vanish on V1, so their restrictions to R factor
through its sheaf quotient R/A0=C. Their compositions with Z vanish
because Hom_G(C,Z)=0. This does not say their images in V0 O vanish;
those images may be nonzero inside U. The proof keeps these two different
claims separate.

The D channel has nonzero restriction modulo U by PR790. That dependency
does not deduce the nonvanishing from character multiplicity: its universal
second-jet argument and annihilator comparison would otherwise identify
two backward kernels of different degrees, minus fourteen and minus
twenty-four. The one-dimensional target and this nonzero restriction,
together with the zero restrictions of the other two channels, show that
the kernel is exactly the A-plus-V space J. There can be no cancellation
that rescues a D component.

Each n_b for b in J kills V0 and maps the complementary space into V0.
Hence every product n_b n_b' is zero. The two independent channels are
actual independent ambient endomorphisms preserving the inclusion. Full
faithfulness below ensures they remain independent in the pencil algebra.

## 5. Multiplication and the exact Jacobson radical

With the rightmost map acting first, block composition gives the upper
term `a0 b' + b d'`. In the split residual gauge every b in J vanishes on
V1, so `b d'=a2' b`, not `a1' b`. Therefore the multiplication in (18)
is correct. The separate scalar a1 is an independent central factor;
the other two scalars and J have exactly the multiplication of T(J).
This gives dimension five in the zero-coupling case.

In the nonzero case the residual diagonal scalars coincide, leaving the
same triangular algebra without the additional central C factor and
giving dimension four. The classification of all possible ambient maps
in the preceding sections establishes these as exact dimensions, not
lower bounds obtained by displaying some endomorphisms.

In both cases J is a two-sided ideal with J^2=0. A nilpotent ideal in
a finite-dimensional algebra lies in its Jacobson radical. The quotient
by J is the displayed product of copies of C and is semisimple, forcing
the radical to be contained in J. These two inclusions prove equality.
No larger nilpotent ideal or unnoticed radical part remains in a diagonal
factor.

## 6. Full faithfulness for arbitrary pencil morphisms

The general reconstruction statement in Section 6 is valid under its
stated splitting hypotheses. Negativity gives H0(E)=0; positivity of Q
gives H1(Q(-2))=0 and global generation of Q(-1). The relevant evaluation
and Koszul sequences therefore have exactly the asserted consequences.

Given any triple (e2,e3,e4) intertwining the same two variables, its maps
on the Koszul complex induce h on the constant middle-cohomology space H.
Independently, compatibility with the A pencil gives a map of the exact
evaluation presentations and hence a unique bundle map q:Q->Q'. Its map
on H0(Q(-1)) is precisely e3. This uses the actual evaluation sequence,
not a separate presentation with merely matching ranks or characters.

For a cycle (x,y), applying q to its Q-section ux+vy produces exactly
the section represented by (e3(x),e3(y)). The resulting equality of
global sections gives the equality of bundle maps (25), so h preserves
E everywhere on X and q is its genuine induced quotient map. The
construction is not confined to the generic parameter.

It remains essential to recover all three specified maps, and the proof
does so. The induced N3 map is e3 by evaluation. Naturality of
multiplication and injectivity of multiplication by any nonzero formal
linear form then identify the induced N2 map with e2. Every section of
Q is ux+vy, and the connecting map delta is surjective because
H1(H O)=0. Equation (26) therefore identifies the induced N4 map with
e4, rather than only on a potentially proper image of one B map.

For faithfulness, evaluation determines q from e3, and the injection
H'->H0(Q') determines h from q and the original H map. Thus a pencil
triple recovers one and only one inclusion morphism. These constructions
are inverse on every Hom space and respect addition and composition.
Their equivariance follows from natural evaluation and cohomology; the
basis symbols merely express these maps under the fixed symplectic
determinant convention. No invertibility condition was used.

Essential surjectivity onto arbitrary pencil systems is neither proved
nor needed. PR790 supplies the separate identification of the reconstructed
pencils with the fixed original tensors under the actual-source
hypotheses. This closes the necessary bridge from a full ambient algebra
to the full fixed-pencil algebra, not just to selected projectors in it.

## 7. Duality reverses composition

The common-pencil functor is covariant on morphisms of E in H O. By
contrast, passage from an ambient f on H* preserving Q* to f* on H
preserving ann(Q*) is contravariant. The identity

`(f g)* = g* f*`

therefore yields E_P isomorphic to E_Q^op, exactly as stated in (28).
This reversal cannot be omitted when discussing the orientation of
the two radical channels.

The map `(a,d,b) -> (d,a,b)` is indeed an anti-isomorphism of T(J):
the upper component of the reversed product is `d' b + a b'`, equal
to the original upper component. Hence T(J)^op is abstractly isomorphic
to T(J), and the same is true after adjoining the independent C factor.
The opposite-algebra convention changes the displayed arrow direction,
not the two abstract algebra types or their radical assertions.

## 8. Uniformity and evidential limits

All arguments apply to each fixed balanced endpoint and to every coupling
in either quotient class. The endpoint is not allowed to vary within
an endomorphism, and the base X and both negative pencil variables remain
fixed. A problem allowing base automorphisms or reparametrizations would
have different morphisms and is correctly excluded.

Within the proved normal-form class, the dimensions distinguish the two
residual quotient classes. Dimension alone is not asserted sufficient to
place an arbitrary pencil system in that class. The result also does not
determine which class, if either, occurs for the actual HM tensors.

The proof and this review use universal structural algebra, constant
connections, representations, bundle exact sequences, and natural
cohomology. No actual coefficients, endpoint parameters, source points,
derivative values, matrices, source-instance ranks, scans, selected models,
or large computations were selected or evaluated. Hashing the reviewed
texts is a byte-integrity check, not an algebraic experiment or formal
certification.
