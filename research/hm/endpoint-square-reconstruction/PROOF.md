# One C5-square secant fiber determines the entire endpoint family

## Scope and inputs

Work over C with G=SL2(F5); all representations used for the channel spaces descend to G/{±1}=A5, whereas W itself is the binary representation. Let W be the fixed binary representation, A=Sym²W, D=Sym⁴W, P the irreducible four-dimensional representation (the endpoint P4), and V the other irreducible three-dimensional representation. We use the invariant symmetric form on A and the canonical identification D=Sym²_0 A. The source copy of D is identified with this copy by the established canonical probe normalization. Write

Q=Hom_G(D_source,P⊗Sym²A*).

The pinned input is LOWER-FAMILY-IS-DETERMINED-BY-SECANT-RESTRICTION-AND-TRACE.md at c9c54d50c94fc17cad7a14fce93b31bb22b9ea5f, in research/hm/order-four-quadratic-load of Akilleez-QA/read-em-and-weep. It gives dim Q=2, automatic parameter trace zero, and the canonical secant kernel K_a=ker(D→A, h↦γ S_h a), γ≠0. The proof below gives NEW exact constraints in the four-dimensional square fiber, followed by an isomorphism onto its two-dimensional secant subfiber. It does not evaluate the actual endpoint family.


## 1. Exact intrinsic square-fiber compatibility

Set M=Hom(D_source,P). Polarization and invariant forms identify Q canonically with Hom_G(D_parameter,M): the scalar summand of Sym²A contributes M^G=0. Thus every family uniquely has the form

q(a,h)=T((a⊗a)_0)(h),  T:D_parameter→M equivariant.    (1)

Choose a square direction a=u² whose projective stabilizer is C5. This is one of the special twelve square directions, not an arbitrary square. Choose a lift of its generator with eigenvalues η,η⁻¹ on W, η primitive tenth root, and put v=u⁴=(a⊗a)_0. Let χ=η⁴. Since q is quadratic in a, f=q(a,-) belongs to M_χ under the action g·f=ρ_P(g)fρ_D(g⁻¹). This uses the primal evaluation vector v; the dual polynomial-coefficient convention introduces no additional twist.

The universal character decompositions and weights are

M=A⊕V⊕P⊕2D,
A: 0,±2; V: 0,±4; P: ±2,±4; D: 0,±2,±4,

where weights mean exponents of η. Consequently

M_χ=V_χ⊕P_χ⊕(M_D)_χ,       dimensions 4=1+1+2.    (2)

Let π_R denote the canonical central-isotypic projector. Then evaluation Q→M_χ has image EXACTLY

ker π_V ∩ ker π_P=(M_D)_χ.                            (3)

Indeed an equivariant T has image in M_D. Conversely write M_D≅D⊗E intrinsically as the D-isotypic module, with E=Hom_G(D,M). Since D_χ is one-dimensional and contains v≠0, evaluation T↦T(v) is an isomorphism E→(M_D)_χ. No basis of E is required. Hence (3) supplies two independent intrinsic line-valued compatibility constraints, not merely a dimension statement.

The projector onto the compatible plane, restricted to the allowed fiber, is explicitly

π_D=(1/12)(5I + Σ_{g of order2}ρ_M(g) − Σ_{g of order3}ρ_M(g)).    (4)

Here sums are over the fifteen and twenty respective elements of A5. Formula (4) follows from χ_D=(5,1,−1,0,0) and the central-idempotent formula (dim D/60)Σχ_D(g⁻¹)ρ_M(g). The other two summands of (2) are its kernel. Thus f is compatible if and only if π_D f=f.

## 2. Reconstruction without a chosen channel basis

For compatible f, there is a unique T with T(v)=f. Equivalently impose

T(gv)=ρ_M(g)f

on the orbit spanning D. All linear relations among the orbit vectors are then respected by (3). This is canonical reconstruction, not a choice of two unknown coefficient values.

An optional finite averaging expression makes the inverse explicit. Take any λ∈D* with λ(v)=1 and put

T_f(x)=(5/60)Σ_{g∈A5}ρ_M(g)f · λ(ρ_D(g⁻¹)x).          (5)

For arbitrary f∈M_χ, Schur averaging of the rank-one map x↦λ(x)f gives T_f(v)=π_D f. On each D-copy, write its component f_j=T_j(v). The average of v⊗λ on D is I/5 because its trace is1. All non-D components average to zero. Therefore, for compatible f, (5) is the unique reconstruction and is independent of λ. Formula (1) then recovers every parameter value.

## 3. Stronger minimal certificate: only the secant kernel at this square is needed

The restriction map

Q → Hom(K_a,P)_χ                                  (6)

is an isomorphism of two-dimensional vector spaces. The notation means maps f with ρ_P(g)fρ_{K_a}(g⁻¹)=χ(g)f. In particular, a whole endpoint family is zero if and only if its restriction to K_a is zero at ONE C5 square.

Proof. Use a binary basis u,z and a=u². The actual interface really is the transvectant kernel: A⊗A=1⊕A⊕D implies dim Hom_G(D⊗A,A)=1. The established map (h,a)↦S_h a is nonzero. The second SL2 transvectant Sym⁴W⊗Sym²W→Sym²W is another nonzero G-map, so these maps differ by a nonzero scalar. Their kernels therefore agree; this is not an extra assumption about actual source values. Thus

K_a=span(u⁴,u³z).

Both indicated vectors are killed; the other three weight vectors map to the three distinct weights of A with nonzero coefficients. The two source weights are4 and2. Multiplication by χ shifts output weights to8≡−2 and6≡−4, respectively, each occurring once in P. Hence the target of (6) has dimension2.

The two channels of Q have an intrinsic parity splitting by interchange of the two D slots. Clebsch–Gordan gives

Sym²D=Sym⁸W⊕Sym⁴W⊕1,  Sym⁸W|_G=D⊕P;
Λ²D=Sym⁶W⊕Sym²W,       Sym⁶W|_G=V⊕P.

Thus the symmetric and alternating channels are each one-dimensional. Up to harmless nonzero normalizations their bilinear representatives are

B_+(b,h)=π_P^(8)(bh),
B_−(b,h)=π_P^(6)((b,h)_1),

where the projections are the canonical central-isotypic projections, followed by any nonzero identification of their P copy with the endpoint P. These identifications affect scales, not the intrinsic two channel lines or any injectivity assertion.

At b=v=u⁴,

B_−(v,u⁴)=0,  B_+(v,u⁴)=π_P^(8)(u⁸)≠0;
B_−(v,u³z)=4π_P^(6)(u⁶)≠0.                          (7)

The asserted nonvanishing does not use actual-source data. For n=6 or8, the twelve distinct projective orbit points of [u] imply their nth powers span SymⁿW: an annihilating covector would be a degree-n binary polynomial with twelve distinct zeros and hence zero. If π_P^(n)(uⁿ)=0, equivariance puts every orbit power in the proper complementary G-submodule, contradicting spanning. This proves (7).

The restrictions of B_+ and B_− are triangularly independent: evaluating a relation on u⁴ first kills its symmetric coefficient; evaluating next on u³z kills its alternating coefficient. Therefore (6) is injective and, by the target dimension, bijective.

This is coordinate-free in content. The kernel carries the canonical flag Cv⊂K_a; its line and quotient are the two stabilizer weight lines. Evaluation on Cv detects the symmetric family channel. Conditional on that channel being zero, evaluation on K_a/Cv detects the alternating channel. The coordinates in (7) prove the nonzero constants, but the vanishing certificate requires no basis or normalization choice.

### Corollary: detection at every square

The injectivity assertion in (6), without the two-dimensional target claim, holds for every nonzero square a=u². Indeed every finite subgroup of PGL2 fixing a point is cyclic in characteristic zero: its derivative at that point is faithful, since a finite-order Möbius transformation with derivative1 at a fixed point is the identity. Point stabilizers in A5 therefore have order at most5, so every orbit on P(W) has at least12 points. The pure-power spanning proof in degrees6 and8, and the triangular proof (7), apply unchanged. Thus any nonzero endpoint family restricts nontrivially to the secant kernel at EVERY square. The exact dimension-four full fiber and dimension-two secant allowed-fiber isomorphism above specifically concern C5 squares.

## 4. Contribution and limits

The earlier global K-restriction isomorphism required the WHOLE restricted family. Here one special square's two-dimensional secant fiber already suffices. Any prescribed stabilizer-allowed secant map there extends uniquely to an equivariant endpoint family. Its unique full four-dimensional fiber extension obeys the two constraints (3); there are no additional endpoint compatibility conditions on that two-dimensional secant datum.

This supplies a smallest possible linear certificate for the zero endpoint family: two independent scalar coordinates, or intrinsically the vanishing of K_a→P. A single scalar linear test cannot distinguish every element of the two-dimensional family space. It also explains exactly which two components of an arbitrary allowed full square fiber are forbidden.

No selected actual HM source, coefficient, matrix, rank, fourth-order value, secondary residue, Smith exponent, section count, repair, or algebraicity is computed or established. Null's actual endpoint calculation remains necessary. The generic binary variables above represent universal intertwiners, not a selected actual input evaluation.

## Verification

Run python3 verify.py. It uses only the five-row A5 character table, exact quadratic radicals, weight lists and small symbolic transvectants. It checks the decompositions, the fiber dimensions, the parity split and the secant-kernel/transvectant identities. The orbit span, invariant projections, Schur averaging and passage to the actual interface are mathematical proofs as stated, not proof-assistant certification.
