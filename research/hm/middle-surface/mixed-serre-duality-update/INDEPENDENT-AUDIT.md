# Independent audit: marked opposite-return sign obstruction

## Verdict

The intrinsic first-order argument in PROOF.md is valid. Its conclusion is a necessary condition for precisely marked algebra returns and the explicitly right-free rank-one bimodule returns. It is not an existence theorem and does not compute any mixed obstruction, detector pairing, or source coefficient.

For a square-zero extension of a commutative algebra by a symmetric module, the commutator of lifts is intrinsic. A return inducing identity on the classical algebra transports this bracket by its coefficient map. Passing to the opposite negates the bracket. Therefore a scalar-sign coefficient return must negate each nonzero pure bracket. The product of the two forced negative signs is positive.

The elementary gauge calculation agrees: the antisymmetric part of a Hochschild coboundary of a linear map into symmetric coefficients vanishes. An identity-reduction gauge cannot reverse a nonzero first-order Poisson bracket.

## Required qualifications

1. **Nonzero mixed coefficient.** The mixed-character assertion requires a specified nonzero product coefficient line. A suitable parameter model is R = k[s,t]/(s²,t²), with I = (s,t), J = I² = k·st. On R/I² one proves only the first-order constraint; st itself vanishes there. The full coefficient multiplication must identify the mixed line with the tensor product of the two pure lines.
2. **General linear parameter actions.** With fixed coefficient trivializations, write the first-order bracket as sπ_z + tπ_h and a semilinear parameter return as φ(q_i) = Σ_j M_ji q_j modulo I². Identity classical reduction of an opposite return gives −Σ_i M_ji π_i = π_j for each j. Independence of the two factor-supported tensors forces M = −Id. This uses more than mere nonzeroness if arbitrary axis mixing is allowed. If φ exists on the full displayed ring, its multiplicativity then gives φ(st) = st. Higher terms in I² do not alter that equality because I³ = 0.
3. **Permutations.** A bracket-compatible exchange of the two factors, together with the matching coefficient permutation, forces minus that permutation. Its mixed action is positive for ordinary commuting/even parameters. This statement does not cover an exchange composed with an additional anti-Poisson base map, independent signed coefficient transport, or odd coefficient lines.
4. **Local statement.** Local exclusion holds on opens where both restricted pure bracket maps are nonzero (and independent for the general linear formulation). The smooth-plane external-product model has this property on the usual nonempty product charts. Mere global nonzeroness for an arbitrary sheaf does not imply nonzeroness on every open.
5. **Base and coefficient marking.** For classical reduction α, the equation is β_target(αa,αb) = λβ_source(a,b). A nontrivial, including anti-Poisson, α is not excluded. Nor is an identification with an opposite/sign-changed coefficient extension when the fixed marking is abandoned. An additional independently negative map on an obstruction or determinant line is not ruled out by the positive parameter character alone. Applying the character to a defect operator requires verifying that its band action is exactly the stipulated multiplicative coefficient action.
6. **Module scope.** The draft's locally right-free rank-one invertible bimodule reduction to an algebra map is valid, provided all the stated classical and coefficient markings hold. These properties cannot be inferred from a classical determinant line alone. The proof does not, as written, settle arbitrary matrix algebra returns, general Morita equivalences, or derived equivalences. Such extensions require their own invariant-bracket or Hochschild naturality argument.
7. **Characteristic.** Characteristic zero suffices; the scalar-sign obstruction only needs 2 invertible. The argument requires symmetric kernel actions and an associative square-zero pure extension.

## Proof checks

The bracket is lift-independent because the two induced classical actions on the kernel agree, and products of kernel elements vanish. Its Leibniz identity follows from the associative commutator identity. Algebra-map naturality is immediate by applying the map to a commutator. The opposite bracket is exactly the negative, without a choice of splitting. For a right-free rank-one module, the endomorphism algebra is identified with the coefficient algebra by choosing a right generator; an invertible bimodule supplies the local algebra identification, and the ordinary classical line action supplies identity classical reduction. Inverting a scalar sign leaves the sign unchanged, so reversal of the direction of that algebra map causes no issue.

## Boundary of this audit

This audit evaluates only the formal sign lemma and its scope. It does not independently verify the external source comments or the previously computed Serre-dual operator, and it performs no mixed-class evaluation, detector pairing, or external write.

## Final revision check

The revised PROOF.md explicitly incorporates the nonzero mixed coefficient model, higher mixed-term irrelevance, local nonzero-bracket scope, fixed product marking, and the distinction between the coefficient character and the total obstruction-band action. It passes this audit as a deliberately axis-preserving scalar-sign theorem. It intentionally does not classify arbitrary parameter mixing or factor exchanges; the conditional linear-parameter calculation in item 2 and the carefully marked exchange case in item 3 above are separate extensions, not claims that the draft has proved a broader theorem. No mathematical defect remains in the stated bounded result.
