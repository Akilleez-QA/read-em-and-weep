# Independent mathematical review of the determinantal excess factor

## Verdict and dependencies

The proof in PROOF.md is valid conditional on the pinned normalizer representations and the actual multiplication results of PR489 and PR495. I independently checked the module construction, identification of the actual multiplication map, exact annihilator, all degree-zero and ungraded endomorphisms, and indecomposability. This is a mathematical review, not formal proof-assistant verification.

The checked inputs are PR495 at b972aa22b72658b419e2c8948a56e0eec7f59e13, which gives Z=I/Fitt_0(H), its two nonzero components and surjective multiplication, and PR489 at 5637cdd610fc2ec8ffbbbbfc7627b2d6c54f6873, section 1, which explicitly gives the three tensor identities used here. The Heisenberg character-orbit argument is the usual one for the five-dimensional irreducible A: conjugation on End(A) contains each character of Gamma/Z(Gamma) exactly once, and the quotient normalizer permutes the twenty-four nontrivial characters transitively.

## Actual module structure, not just character equality

The nonzero projection T tensor A onto V tensor W is surjective because its target is an irreducible summand. Killing all products of two variables defines a genuine S-module C: every commutator of variables acts by zero. Its linear relation space is V tensor U-prime, of dimension fifteen. Adding all quadratic relations gives precisely the stated presentation; minimality of those quadratic relations is neither required nor claimed.

After tensoring with W-prime, the target V tensor T_4 occurs exactly once in T tensor A tensor W-prime. Both the constructed map and actual multiplication on Z are nonzero normalizer-equivariant maps into that irreducible target. Thus their ratio is one nonzero scalar. Rescaling only the target component identifies the entire two-step S-module, because there are no further products. This proves Z is C(-3) tensor W-prime, rather than merely proving equality in a representation ring.

Choosing a basis of W-prime gives two ordinary S-module copies. It does not give a normalizer-invariant splitting. The tensor-factor action is retained in the equivariant isomorphism; the grading shift does not assert any additional character twist or change of the variable representation.

## Exact annihilator and endomorphism rigidity

The linear annihilator of C is stable under the normalizer. Irreducibility of T and nonzero multiplication force it to be zero. Since C is nonzero and m squared annihilates it, its homogeneous annihilator is exactly m squared. The same holds for Z.

Restriction of a degree-zero endomorphism to A is injective because A generates C. Its image in End(A) is a normalizer-stable subspace containing the identity. Finite-group semisimplicity and End(A)=1 plus an irreducible twenty-four-dimensional summand give precisely the scalar or full alternatives. This uses the normalizer action on the space of all endomorphisms, not equivariance of an individual endomorphism.

If every endomorphism of A extended, every matrix unit on A would preserve the nonzero linear relation space. Applied to a relation sum_i t_i tensor a_i in a basis a_i, these units imply t_i a_j=0 for every j. Thus each t_i is in the linear annihilator, which is zero. This contradicts existence of the relation. Consequently the degree-zero endomorphism algebra is exactly the scalar field.

## Ungraded maps, multiplication and indecomposability

Every linear map from A to C_1 extends to a degree-one S-linear map, zero on C_1. Both sides of compatibility with multiplication by a variable are zero. There are fifty such maps. Generation in degree zero excludes negative-degree maps, and the support excludes degrees above one.

For a possibly ungraded S-linear map, project its values on each homogeneous component to their degree offsets. Comparing the homogeneous parts of f(sx)=s f(x) shows that every offset is itself S-linear. Thus the homogeneous calculation exhausts the ungraded endomorphism algebra. Composition of two degree-one maps is zero, while a degree-zero scalar acts by that scalar on either side. The full algebra is therefore the stated commutative local algebra of dimension fifty-one, with square-zero radical of dimension fifty. Its only idempotents are zero and one, proving indecomposability even without the grading.

Tensoring by the two-dimensional vector space W-prime gives the matrix algebra over this endomorphism algebra after choosing a basis. The degree-zero dimension is four, degree-one dimension is two hundred, and total dimension is two hundred four. Independently, every degree-one map on Z is an arbitrary linear map Z_3 to Z_4, giving 10 times 20 equals 200. The scalar grading shift leaves degree offsets unchanged. None of these endomorphism calculations imposes normalizer-equivariance.

## Scope

The result resolves the ordinary S-module decomposition of the determinantal excess and its full endomorphism algebra. It does not identify C with a Galois-twisted primary-cohomology module over the fixed S, determine its minimal resolution, select remaining Betti parameters, or settle the quintic Fitting-generator count. No selected HM/source-instance evaluation, numerical matrix or rank, coefficient search, generator/checker, or large computation was used. No first-order statement is promoted to a higher-order lifting or algebraicity conclusion.
