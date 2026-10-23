# The three-channel monad torus has one fixed-negative-pencil isomorphism type

Draft for independent review. No actual monad coefficient, tensor entry, point, derivative, matrix, or source-instance rank has been selected or evaluated.

## Result

Work over C with the fixed group G=SL2(F5), the fixed coordinate representation H=V⊕W, and the fixed negative two-space W. Use the irreducible channel maps and determinant-valued monad of PR643. For a triple t=(a,b,c) with abc≠0, let F_t be its middle cohomology and B_t=End_0(F_t). Define

    N(t)_2=H^1(B_t(2))_+,
    N(t)_3=H^1(B_t(3))_-,
    N(t)_4=H^1(B_t(4))_+.

The subscripts denote the same actual inversion linearization as in the pinned HM Gauss gate. For every l∈W, let A_l(t):N(t)_2→N(t)_3 and B_l(t):N(t)_3→N(t)_4 be actual multiplication by l.

**Theorem.** For any two triples t,t′∈(C*)³, the systems N(t) and N(t′) are isomorphic by a single triple of G-equivariant linear isomorphisms that intertwines every A_l and B_l with the identical l. No change of the two pencil variables remains in the resulting intertwining equations.

Consequently their complete degree-preserving G-equivariant fixed-pencil endomorphism algebras are isomorphic as algebras, including singular endomorphisms. The entire representation of this algebra on the three spaces is transported simultaneously. In particular the commutant dimension, radical structure, image/kernel incidence, idempotent image-pencil types, and any intrinsically constructed radical subquotient are invariant across this actual monad family.

The theorem gives no value for any of these invariants. It does not assert that an arbitrary abstract common-pencil system with the same characters belongs to this family, nor that a truncated endomorphism extends to the full HM module or bundle.

## 1. Exact inputs

1. **PR643, three-channel family**, commit

       356a3b8d2da36f5b3e2034cc5c6adf82757a33cc,

   [research/hm/three-channel-monad-family/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/356a3b8d2da36f5b3e2034cc5c6adf82757a33cc/research/hm/three-channel-monad-family/PROOF.md).

   This supplies the actual G-equivariant monad

       N O(-1) --alpha_t--> W′ Ω²(2) --alpha_t†--> N* Δ,
       N=A⊕W′, A=Sym²W, Δ=det(H),

   and its fixed three irreducible coefficient channels. It proves that the subbundle locus is exactly abc≠0, that the actual normalized HM monad lies there, and that the whole torus is transitive under G-equivariant source gauges and block coordinate pullbacks. In its conventions source gauges act as

       (a,b,c) ↦ (sa,sb,rc),

   while a coordinate-function pullback g* with g*|V=λ id and g*|W=μ id acts as

       (a,b,c) ↦ (λ³a,λμ²b,λ²μc).

   The right arrow transforms by the determinant-compatible adjoint; the assertion is an isomorphism of the full monads, not an identification of left-arrow representation types alone. The fixed coefficient channels remain the same throughout.

2. **The actual cohomological origin**, commit

       063216038f3aefd65617651c2426721efafc7f9b,

   [research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md).

   This identifies the fixed actual M2,+→M3,-→M4,+ arrows as multiplication by the same negative linear form on H^1(B(j)), with dimensions41,54,37. It also identifies their actual Koszul middle cohomology and Gauss derivative. We use its origin of the spaces and arrows, not an inference from those dimensions.

3. **For application to the source2 constraint only**, PR790, commit

       af0e03d26da5e47d18ae732291aca46f4d448dc5,

   [research/hm/source2-first-constant-block/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md), Section6, identifies its conditional source2 reconstruction with those same actual tensors. This input is unnecessary for the theorem about the monad torus itself; it is necessary before applying a source2 consequence to the actual system.

PR643's upstream actual-monad and restricted-G conventions are pinned there at `8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4` and `78053cfaec46a334c8714da084948356e467259e`. No unpublished coefficient table is an input to this proof.

## 2. A monad isomorphism after a scalar block pullback

Let t=(a,b,c) and t′=(a′,b′,c′) have all entries nonzero. PR643 gives a block coordinate automorphism g and a G-equivariant isomorphism between the monad for t′ and the naturally pulled-back monad for t. Its construction can take λ=1 and any nonzero μ satisfying

    μ²=(b′/a′)/(b/a),

followed by the source gauges s=a′/a and r=c′/(μc). Such μ exists over C. This is an existence argument for arbitrary symbolic triples; it does not determine any actual coefficient.

Passing to middle cohomology yields a G-equivariant vector-bundle isomorphism

    F_t′ ≅ g*F_t.                                      (1)

Every block scalar commutes with G on H. The source gauges are scalars on the fixed irreducible source summands, hence G-equivariant. The middle pullback uses the natural linearization on Ω²(2), and the right arrow retains Δ. Thus (1) is compatible with the original G action and its central inversion, rather than an unmarked bundle isomorphism.

Taking trace-free endomorphisms in (1), and fixing the indicated orientation of the resulting isomorphism, gives

    θ:g*B_t → B_t′.                                    (2)

Conjugation preserves trace, so (2) involves no chosen determinant trivialization or additional scalar normalization. In particular the constant determinant factor present in the monad does not twist B_t.

## 3. Naturality of all multiplication maps

For every integer j, let θ_j:g*(B_t(j))→B_t′(j) be (2) tensored with the natural compatible twist identification. Pullback along the projective automorphism g, followed by θ_j, induces the isomorphism

    Φ_j=H^1(θ_j)∘g*:H^1(B_t(j))→H^1(B_t′(j)).          (3)

Use the natural compatible identifications g*O(j)≅O(j) obtained from the same linear coordinate pullback for every j. Compatibility with tensor powers is essential. With this choice, cohomological multiplication is natural: for any coordinate linear form l and class x,

    Φ_(j+1)(l·x)=(g*l)·Φ_j(x).                        (4)

Indeed multiplication by l is the sheaf morphism B_t(j)→B_t(j+1). Pulling back this sheaf morphism gives multiplication by g*l, and (2), tensored by the compatible O(j) identifications, gives a commuting diagram of these sheaf morphisms. Functoriality of H^1 proves (4). This argument uses the actual cohomological action and does not infer it from matching representations or a reconstruction theorem.

For all l in the fixed negative W, the same scalar μ satisfies g*l=μl. Therefore

    Φ_(j+1) m_l(t)=μ m_l(t′) Φ_j                      (5)

simultaneously for every l∈W and every j. The scalar does not depend on l, and in particular cannot differ between the two chosen basis variables or between the first and second arrows.

All maps in (3) are G-equivariant. They preserve the inversion eigenspaces because g and the monad isomorphisms commute with that inversion. A negative l reverses parity as in the original HM gate. Thus (5) restricts to exactly the even/odd/even spaces defining N(t).

## 4. Removing the common scalar without changing variables

On these three spaces put

    Ψ_2=Φ_2,
    Ψ_3=μ^(-1) Φ_3,
    Ψ_4=μ^(-2) Φ_4.                                 (6)

These are G-equivariant vector-space isomorphisms. Equation(5) gives, for each identical l∈W,

    Ψ_3 A_l(t)=A_l(t′) Ψ_2,
    Ψ_4 B_l(t)=B_l(t′) Ψ_3.                          (7)

For the second identity, for example,

    μ^(-2) Φ_4 B_l(t)
      =μ^(-1) B_l(t′) Φ_3
      =B_l(t′) Ψ_3.

This proves an isomorphism in the fixed-variable pencil category. We do not accept an arbitrary GL(W) coordinate change or separately chosen conjugacies for individual arrows. The coordinate pullback used above is scalar on all of W, and the single graded rescaling(6) removes that scalar from both arrow families at once. There is no residual relabeling of l in(7).

More generally, Ψ_j=μ^(2-j)Φ_j intertwines multiplication by every l∈W on all cohomological degrees where it is defined. This observation concerns the restriction to the polynomial ring Sym(W). It makes no assertion that multiplication by the positive V variables is preserved by the same rescaling when λ and μ differ.

## 5. The complete algebra and its action are preserved

Let C(t) be the algebra of all triples e=(e_2,e_3,e_4) of G-equivariant endomorphisms satisfying

    e_3 A_l(t)=A_l(t)e_2,
    e_4 B_l(t)=B_l(t)e_3

for every l∈W. By(7), simultaneous conjugation defines

    C(t) → C(t′),
    e ↦ (Ψ_2 e_2 Ψ_2^(-1), Ψ_3 e_3 Ψ_3^(-1),
         Ψ_4 e_4 Ψ_4^(-1)).                           (8)

The commuting equations are preserved term by term. Replacing Ψ by its inverse gives the inverse map. Componentwise composition and identity are preserved, so(8) is an algebra isomorphism. This proof uses all endomorphisms, not only invertible ones.

Moreover(8) together with Ψ identifies the action of C(t) on N(t) with that of C(t′) on N(t′). Hence the Jacobson radical is transported as an ideal, and its image sums and common kernels are transported as subspaces at all three vertices. Their arrow restrictions and quotients are preserved by(7). Idempotents are taken to idempotents, with their entire image-pencil systems isomorphic, not merely with equal dimensions. Every canonical radical-core construction made solely from these sums, intersections and induced arrows therefore transports as well.

No preferred isomorphism is claimed. Choices of μ and source gauges can change Ψ and the displayed algebra isomorphism. The resulting isomorphism type and all the stated invariant properties are independent of those choices.

## 6. Actual-source corollary and remaining interface

The actual normalized HM monad belongs to the nonzero torus by PR643. It follows that its negative cohomology system, and in particular its fixed-variable41→54→37 truncation, has the same isomorphism type as the formal unit-parameter member of that **same fixed-channel family**. Mentioning that member specifies a comparison object for the theorem; no coefficients or matrices of it are constructed or evaluated here.

Thus an unknown nonzero actual channel ratio is not an independent obstruction to a deductive invariant argument about this negative truncation. A proved invariant of the fixed-channel monad family transfers to the actual system through(7). In particular an eventual commutant argument must still be about the actual channel tensors and actual cohomology, not an arbitrary pencil with the same characters. PR790's separate actual-source bridge is still required to compare the actual invariant with the conditional source2 signatures.

This theorem alone supplies neither an exact tensor table nor a scalar-commutant theorem. A constructive certificate would additionally need an authenticated realization of the fixed G representations and all three nonzero intertwiner channels; the determinant-compatible right arrow; cohomology bases and simultaneous multiplication maps derived functorially from that monad; and exact verification of those identifications. Those steps are not executed here. A calculation on a normalized representative would remain an actual-instance invariant calculation for campaign-scope purposes and is not authorized by this structural reduction.

The comparison does not preserve arbitrary externally fixed positive-coordinate forms, marked numerical normalizations, or higher-boundary source values. It gives no extension of arbitrary truncated endomorphisms to the full five-variable module, no implication from full-bundle simplicity to a scalar truncation commutant, no source2 exclusion, and no change in the quotient-label frontier.

## Verification boundary

The new substantive step is the functorial multiplication diagram(4) and its simultaneous graded scalar removal(6)-(7). The three-channel existence and transitivity theorem is credited to PR643. The actual origin of the pencils is credited to the pinned Gauss gate. No common-pencil reconstruction is assumed in proving the monad-family comparison itself.

Independent review should attack: the variance of g*, the same μ in both arrow families, compatible O(j) linearizations, G and inversion preservation, the determinant line when passing to End_0, and the distinction between a fixed Sym(W)-module comparison and an unsupported full Sym(H)-module extension. No numerical check or artificial example is offered as a substitute for those arguments.
