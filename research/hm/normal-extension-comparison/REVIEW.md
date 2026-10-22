# Independent structural review

Verdict: PASS.

Reviewed artifact: PROOF.md
SHA256: 302e9075e866599bcc40e02c65e7284a050d9e0bfbfce8dc958922a1c808228b

The frozen proof includes the explicit vector-level physical-parity argument. The earlier adjoint-commutation wording alone did not justify an even vector marking; the unequal-degree physical eigenlines now supply the required bridge.

## Checks

1. The whole-cone variation space is physically even: squaring the reflection derivative gives identity, and the discrepancy between the squared cone marking and physical inversion is a scalar automorphism by H0(End0(F_Q))^Γ=0. Scalars act trivially on the adjoint deformation space. Averaging is legitimate in characteristic zero.
2. In physical frames there are no negative-weight even adjoint terms. The weight-zero coefficient quotient is therefore a genuine filtered Čech-complex map, not an arbitrary associated-graded splitting. Higher conic corrections and weight-four normalizing gauges cannot change it.
3. The coefficient bundle agrees with the pinned J_eta through its actual triangular transport and common-spinor-twist invariance of End0. Its lower kernel is V O(-10), not the inequivalent negative three-dimensional representation. Nonvanishing uses the existing square-shadow map and β≠0, not equal dimensions. Diagonal detection follows from the exact sequence and vanishing invariant H1 of the lower kernel.
4. On 2Q, multiplication by I+q c changes the normalized coefficient by c_0 exactly at the relevant weight; products with positive-weight terms are higher, and q²=0. The same source-frame convention gives the stated plus sign. This proves the affine law for all first-normal extensions, without assuming extension to 3Q.
5. For the reference origin, adjoint commutation must first be strengthened to an even vector marking. A scalar commutator with physical inversion is ±1; the negative possibility would exchange the two physical eigensubbundles on L. This is impossible because an isomorphism preserves the unique maximal-degree O(5) subline of O(5)⊕O(-2). Thus the regular marking has the asserted nonnegative even weighted expansion.
6. With both N12 terms zero, the weight-twelve intertwining identity forces the trace-free weight-four marking term into the kernel of ad_n. The cited injection kills it. Independently, the generic centralizer of the rank-one nilpotent is scalar plus a multiple of n; coprimality of f and g excludes a nonzero regular multiple at this smaller weight, consistent with that injection.
7. The weight-zero lower-triangular marking lifts exactly and multiplicatively to the ambient transverse-linear matrices. Hence it introduces no affine reference error. Arbitrary local lifts of the remaining cone marking have trace-free weight-four part qZ0; their effects are precisely J-coboundaries. No global lift of the marking is assumed.
8. The reflection acts negatively on the diagonal ideal coefficient. Concretely, on a negative chart u≠0, its ideal generator q/u² transforms by μ^(-2)=-1 although homogeneous q itself is fixed. The base coordinate v/u is unchanged and lower-triangular conjugation fixes the diagonal. Diagonal detection thus gives φ_J=-1 on invariant H1(J).
9. Naturality with no offset implies κ(m)=0 at the fixed midpoint. Affine bijectivity and the actual endpoint's extension to 3Q, contrasted with the midpoint's nonzero third-normal obstruction, imply κ(E_actual)≠0.

## Source checks

Read the proof and its PR778 dependency in full. Independently fetched the exact pinned files MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md and ACTUAL-NORMAL-CLASS-HAS-A-NONZERO-LOWEST-VERTEX-DIAGONAL.md at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04. They explicitly state the reflection, N eigenvalue -1, midpoint obstruction, and the actual leading-component comparison used here.

## Scope

This is an independent mathematical review of a structural argument, conditional on its explicitly cited geometric inputs, not formal proof-assistant verification. The result determines a reference origin and nonvanishing of the first normalized ambient transition class. It does not compute an Euler-normalized scalar, β4, an algebraicity obstruction, or the entire fifth-section obstruction. No selected actual HM/source coefficients, points, derivatives, ranks, scans, or large computations were performed. No repository content was changed by this review.
