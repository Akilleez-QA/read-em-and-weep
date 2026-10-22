# Independent review: first discriminant neighborhood

## Verdict

**Pass, conditional on the explicitly cited PR696 inputs.** The universal geometric theorem, harmonic splitting, and reconstruction argument in `PROOF.md` are correct over C. No substantive mathematical correction is needed. The local PR696 proof was read for the representation definitions and multiplicities; its upstream HM claims and the remote pinned commit were not independently audited.

The updated verifier, including the infinitesimal SL2 commutator checks, was independently inspected and rerun. The bounded command `timeout 30s python verify.py` completed successfully with exit code 0. It checks formal universal polynomial identities only. No actual HM family coefficients, selected source instances, matrices, ranks, or derivatives of an actual HM family were computed in this review.

## Independent checks

1. **Restriction to the doubled conic.** For a smooth degree-two conic C in P2, the ideal of 2C is O(-4). After twisting by O(3), both H0(O(-1)) and H1(O(-1)) vanish. Thus restriction H0(P2,O(3)) -> H0(2C,O(3)) is an isomorphism, not merely injective. Its dimension is ten. This conclusion does not use representation theory.

2. **Correct conormal twist.** The kernel of O_(2C)(3) -> O_C(3) is (I_C/I_C^2) tensor O_C(3) = O_C(-2) tensor O_C(3) = O_C(1). Under the degree-two Veronese parametrization C = P(W), this is O_P(W)(2), whereas the reduced quotient is O_P(W)(6). Consequently the dimensions are three and seven. The residual is a conormal-valued coefficient of a cubic section, not an untwisted scalar function or a section of the normal bundle. The sheaf extension and its global-section extension must not be confused; the proof keeps them separate.

3. **Harmonic calculation.** For Delta = y^2 - xz and Box = partial_y^2 - 4 partial_x partial_z, the product rule gives Box(Delta L) = 6L + 4E(L) = 10L for linear L. Thus Box maps cubics surjectively to linear forms; its kernel has dimension seven. Every cubic has the unique decomposition f = H + Delta L with Box(H)=0 and L=Box(f)/10. A harmonic discriminant multiple is zero. Restriction therefore identifies harmonic cubics with all binary sextics on C.

4. **Reconstruction.** Given a section on 2C, lift its reduced restriction using the unique harmonic cubic, subtract that lift, identify the residual with O_C(1) using the fixed discriminant equation, and lift the residual to its unique ambient linear polynomial. This yields the unique cubic. The ambient linear restriction map is indeed an isomorphism: its kernel and cokernel are controlled by H0(O(-1)) and H1(O(-1)), respectively.

5. **First normal data versus Box.** Box is a second-order differential operator on homogeneous parameter polynomials. It is not a first transverse derivative. It computes the coefficient of the harmonic global splitting. First-neighborhood sufficiency instead follows from the ideal and cohomology sequences. For a section with nonzero reduced restriction, a normal component requires a chosen splitting; for a section vanishing on C, its conormal class is intrinsic. The proof states these distinctions correctly.

6. **Equivariance and canonicity.** Delta and Box are invariant under the stated binary SL2 action, so the harmonic projector is equivariant for its finite subgroup Gamma. Rescaling Delta by c and Box by c^(-1) leaves the projector unchanged and rescales L by c^(-1). Hence the splitting is canonical relative to the discriminant conformal geometry and the stated linearized setup, not a choice-independent scalar trivialization of the conormal line. It is also the unique SL2-equivariant splitting of the two nonisomorphic summands Sym^6(W*) and Sym^2(W*). No assertion of a canonical arbitrary-sheaf splitting is justified or made.

7. **The 23 = 16 + 7 statement.** Exactness after taking invariants follows because Gamma is finite and the field has characteristic zero. Using the imported PR696 multiplicities gives the claimed dimensions. These count spaces of possible equivariant families; they do not count independent values or establish the rank of any actual family. The local dependency explicitly supplies the needed finite-group hypothesis and the representations.

## Minor precision improvements incorporated

- In section 1, “taking Gamma invariants preserves exactness in characteristic zero” should preferably say “because Gamma is finite and the characteristic is zero.” Characteristic zero alone is insufficient for an arbitrary group. This is a presentation clarification, since finiteness is supplied by PR696.
- The statement that an intrinsic first normal class is “exactly L|C” is understood after the chosen generator Delta identifies the conormal-twisted kernel with O_C(1). Intrinsically the class is Delta L modulo Delta^2. The text already explains the scaling dependence; adding “under this identification” would make the statement fully explicit in isolation.
- The verifier tests a monomial basis, not a cubic with separately named free coefficient symbols. This is sufficient by linearity. The final description should say “universal monomial identities” or “all cubics by linearity,” rather than literally claiming that the script contains free coefficient symbols.
- The script does evaluate formal derivatives of universal polynomials. Its scope statements should consistently qualify the prohibited derivatives as derivatives of an actual HM/source family, so that “no derivative evaluated” cannot be read as denying the formal Box calculations.

## Verification limits and exact scope

The script verifies the Box normalization, the cubic decomposition on a complete monomial basis, preservation of square-conic restriction, the elementary linear restriction parametrization, invariance of Delta under the two stated infinitesimal SL2 generators, commutation of Box with those generators on every cubic basis monomial, and arithmetic using imported representation multiplicities. It does not computationally certify projective cohomology, the passage from infinitesimal equivariance to the connected group action, the representation multiplicities, or the upstream polynomial descent. Those parts are written arguments or explicit dependencies.

The conclusion is complete detection and reconstruction of arbitrary cubic parameter families from their doubled-discriminant restriction, including the seven possible equivariant channels invisible on the reduced conic. It supplies neither actual normal data nor actual reduced data for rho4. It proves no actual scalar vanishing or nonvanishing, vertex I^2 membership, fourth Bockstein value, higher-order unobstructedness, or algebraicity. The infinitesimal neighborhood is in parameter space, not in the physical quadric.

No external writes or GitHub modifications were made.
