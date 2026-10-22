# Independent review: endpoint square fiber and secant reconstruction

## Scope and verdict

The universal representation-theoretic endpoint lemma and the subsequent secant-restriction strengthening are correct under the assumptions below. This review uses abstract representation theory and symbolic transvectants only. It does not perform any selected actual HM/source-instance evaluation, large computation, or repository write.

The source context supplied for this review is commit `c9c54d50c94fc17cad7a14fce93b31bb22b9ea5f`, file `research/hm/order-four-quadratic-load/LOWER-FAMILY-IS-DETERMINED-BY-SECANT-RESTRICTION-AND-TRACE.md`. The source file itself was not independently retrieved; the statements reviewed are the explicit mathematical statements supplied by the parent.

Work over C. Let G=SL2(F5), with its faithful binary icosahedral module W. Put A=Sym²W and D=Sym⁴W; let P be the 4-dimensional A5 irreducible and V the other 3-dimensional irreducible. The representations used for the channel spaces factor through A5; W itself is the binary representation and does not. Take the given decompositions Sym²A=1⊕D and M=Hom(D,P)=A⊕V⊕P⊕(D⊗C²). In particular Hom_G(D,P)=0.

## 1. Polynomial duals and evaluation

A homogeneous quadratic polynomial q:A→M is an element of M⊗Sym²A*. Its polarization is a linear map Sym²A→M. Thus

Q=Hom_G(D_source,P⊗Sym²A*) ≅ Hom_G(Sym²A,M) ≅ Hom_G(D_parameter,M).

The trivial summand contributes nothing because M^G=0. This uses the primal parameter module D in the last Hom, not D*. No extra dual or character twist is needed in evaluation.

For a=u², the invariant quadratic on A vanishes. Consequently a⊙a lies in the harmonic D summand of Sym²A. Fix the Cartan normalization identifying this vector with v=u⁴. Scaling that identification changes the formula for T inversely, not the resulting quadratic family.

## 2. Stabilizer convention and exact fiber

Assume [u] has projective stabilizer C5 in A5. This is a special square direction: it is not a property of every nonzero square. Choose a binary lift with eigenvalues η,η⁻¹ on W, where η is primitive of order 10, and choose u of eigenvalue η. Then a has eigenvalue η² and v has eigenvalue η⁴. The lift acts on the even modules with order 5; replacing the lift by its negative does not change those actions.

Equivariance gives q(ga)=g·q(a), where g·f=ρ_P(g)fρ_D(g⁻¹). Since q is quadratic, q(η²a)=η⁴q(a). Thus f=q(a) belongs to F=M[η⁴]. The weights are:

- A: 1,η²,η⁻², hence no η⁴ weight;
- V: 1,η⁴,η⁻⁴, hence one η⁴ weight;
- P: all four nontrivial C5 characters, hence one η⁴ weight;
- D: 1,η²,η⁻²,η⁴,η⁻⁴, hence one η⁴ weight in each copy.

Therefore dim F=4. Evaluation Q→F sends T to T(v). It is injective because a nonzero v generates the irreducible D. Its image is exactly F∩M_D, of dimension 2: under M_D≅D⊗C², T(v) runs over v⊗C². Equivalently, on the stipulated fiber F, the necessary and sufficient conditions are π_Vf=π_Pf=0. These conditions are not asserted to suffice on unrestricted M without the fiber assumption.

## 3. Projector formula

The character of D on the A5 classes of orders 1,2,3,5,5 is (5,1,−1,0,0). Hence the central isotypic projector is

π_D=(1/12)(5I+Σ_{g of order 2}ρ_M(g)−Σ_{g of order 3}ρ_M(g)).

The two sums have 15 and 20 terms respectively. This formula sums over A5, not over all 120 binary-group elements with the same prefactor. It projects onto both D copies at once.

## 4. Explicit intrinsic inverse

Choose any λ∈D* with λ(v)=1. For f∈F define

T_f(x)=(5/60)Σ_{g∈A5}ρ_M(g)f · λ(ρ_D(g⁻¹)x).

This is the Reynolds average, multiplied by dim D, of the rank-one map x↦fλ(x). It is equivariant. On an irreducible summand not isomorphic to D, the averaged map vanishes. On M_D≅D⊗C², the fiber vector has form v⊗m, and Schur averaging sends x↦vλ(x) to (λ(v)/5)Id_D. Consequently T_f(v)=π_Df.

For compatible f this is the unique equivariant map with T_f(v)=f, and it is independent of the choice of λ. The family is q_f(a')=T_f((a'⊙a')_0). Thus reconstruction is explicit and finite without selecting any actual source instance. Orbit interpolation gives the same inverse because the orbit of v spans D.

## 5. Secant-kernel strengthening

Assume the canonical map defining K_a is, up to a nonzero scalar, the order-two transvectant D⊗A→A. Choose a basis u,z of W with a=u². Then (h,u²)_2 is a nonzero multiple of ∂²h/∂z², so

K_a=span(u⁴,u³z).

The two parameter/source D slots can be symmetrized or antisymmetrized. As SL2 modules,

Sym²D=Sym⁸W⊕Sym⁴W⊕1,
Λ²D=Sym⁶W⊕Sym²W.

On restriction to the binary icosahedral group, Sym⁸W=D⊕P and Sym⁶W=V⊕P. Hence P occurs once in each symmetry sector. Two spanning endpoint bilinear channels are

B_+(x,h)=π_P^(8)(xh),
B_−(x,h)=π_P^(6)((x,h)_1).

These projections are on Sym⁸W and Sym⁶W respectively, not the central projector on M from Section 3.

At x=u⁴, one has B_−(u⁴,u⁴)=0 and B_+(u⁴,u⁴)=π_P^(8)(u⁸). Also B_−(u⁴,u³z) is a nonzero scalar multiple of π_P^(6)(u⁶), since the unnormalized first transvectant is 4u⁶.

Both projected pure powers are nonzero. Indeed the orbit of [u] consists of 60/5=12 distinct points of P(W). For n<12 their nth powers span SymⁿW: otherwise a nonzero degree-n homogeneous polynomial in the dual annihilates all 12 points, impossible on P¹. If π_P^(n)(uⁿ)=0 for n=6 or 8, equivariance would put the entire spanning orbit in the proper complementary summand. This is a contradiction.

It follows that B_+ and B_− restrict independently to K_a, by evaluating first on u⁴ and then on u³z. This is a triangular argument, not a numerical generic-rank argument.

Finally, K_a has weights η⁴ and η². An η⁴-weight map K_a→P must carry these lines into P[η⁸] and P[η⁶] respectively. Both output spaces are one-dimensional. The stabilizer-allowed secant fiber therefore has dimension 2, and restriction gives an isomorphism from Q to this fiber.

In particular every stabilizer-compatible secant map at this special square extends uniquely to a quadratic equivariant endpoint family. Explicitly its value on u⁴ fixes the symmetric-channel coefficient; subtract that channel, and its value on u³z fixes the alternating-channel coefficient. No additional compatibility equation remains on this 2-dimensional secant fiber.

## Assumptions and limits

The algebraic statements above use characteristic zero, the indicated binary-icosahedral realization, the given decompositions, and, for Section 5, identification of the canonical kernel with the stated transvectant kernel. They do not independently establish that a particular HM construction realizes those identifications, that a particular family takes prescribed values, or that a downstream geometric obstruction vanishes. The lemma supplies a universal exact fiber criterion, an explicit inverse, and a proof that secant restriction is already sufficient at a C5 square direction.

## 6. Closure of the canonical-kernel identification and independent verifier run

The kernel caveat in Section 5 is resolved at the actual interface, provided the established canonical map is the stated tracefree symmetric action L(h,a)=S_h a. Since A is self-dual and A⊗A=1⊕A⊕D, tensor-Hom adjunction gives

Hom_G(D⊗A,A) ≅ Hom_G(D,A⊗A*) ≅ C.

The tracefree symmetric action is nonzero: a nonzero symmetric operator S_h acts nontrivially on some a. The order-two transvectant is also nonzero; for example (z⁴,u²)_2=24z² in the unnormalized convention. Both are equivariant bilinear maps D⊗A→A, and therefore they differ by a single nonzero scalar. Their specialized kernels agree for every a, in particular K_(u²)=span(u⁴,u³z). This is an interface-uniqueness proof, not an evaluation of the selected quadratic endpoint family or a new source-instance computation.

The parent reports that the exact pinned source explicitly establishes the tracefree symmetric model. This review retains its limitation that the source file was not separately fetched by this reviewer; the mathematical implication from that established interface is independently verified here.

I independently inspected and executed the local `verify.py`; it passed. The script checks the character decompositions, the one-dimensional interface Hom, endpoint multiplicities and weight dimensions, symmetric/alternating channel multiplicities, and exact symbolic transvectant identities, including the complete rank-three image and two-dimensional kernel at a=u². Its scope is bounded universal representation algebra; the orbit-spanning and reconstruction arguments remain the analytic proofs given above.

Result: the canonical-kernel caveat is closed by uniqueness, leaving no additional kernel-identification computation to perform. The remaining boundary is application to any selected actual family's values or downstream geometric obstruction, neither of which is asserted here.

## 7. Canonical flag and all-square injectivity corollary

The canonical-flag formulation in PROOF.md is correct: Cv⊂K_a detects the symmetric channel first, and, conditional on that channel vanishing, K_a/Cv detects the alternating channel. The vanishing certificate needs no chosen normalized coefficients.

Moreover secant-restriction injectivity holds at every nonzero square a=u², without the C5 assumption. A finite subgroup of PGL2(C) fixing a point is cyclic: its derivative at that point gives an injective homomorphism into C*, since a finite-order Möbius transformation fixing a point with derivative 1 is the identity. The possible cyclic subgroup orders in A5 are 1,2,3,5. Therefore every projective orbit has at least 60/5=12 distinct points. The same degree-n zero-count argument for n=6,8 proves π_P^(6)(u⁶)≠0 and π_P^(8)(u⁸)≠0 for every u≠0. The triangular argument then proves Q→Hom(K_(u²),P) injective at every square.

The dimension-two stabilizer-allowed target and the dimension-four full allowed fiber with the stated exact projection conditions are specific to the C5 case as formulated above. The all-square corollary asserts injectivity, not surjectivity onto a larger stabilizer-allowed fiber.
