# Independent audit

The argument in `PROOF.md` is valid under its stated imported hypotheses. No substantive correction is needed. This audit also checked the pure/mixed-map claims imported from `../quaternion-rank-five-coupling-constraint/PROOF.md`.

## Ten-axis interpolation

For the four projective sign choices of `(1,1,1)`, the four cubic parity characters are independent. They force the three coefficient sums and the `xyz` coefficient to vanish. The coordinate-zero axes then give, for the x-parity coefficients,

    A b² + C a² = 0,
    A a² + B b² = 0,
    A + B + C = 0.

Their determinant is nonzero because `1-a²/b²-b²/a² < 0`. The y- and z-parity systems are cyclic copies. Thus the homogeneous cubic evaluation map on the ten axes is injective over C as claimed. Consequently cubic minors vanishing on the orbit vanish identically, so the imported conic odd-rank bound does imply odd rank at least three at every axis.

## Dic3 decompositions and ranks

The positive-central-action quotient is S3. Both three-dimensional representations restrict as `ε ⊕ ρ`, and taking the trace-free symmetric square gives `P5 = 1 ⊕ 2ρ`.

At a nonisotropic u, the pure F5 image is the four-dimensional `uu`-entry-zero hyperplane of P5. Its kernel is `Cu² ⊕ C(q|u-perp)`. The joint `(αF3,βF5)` map therefore has rank five when α and β are nonzero, with kernel `Cu²`, and its image has types `ε ⊕ 2ρ`. Its intersection with P5 is exactly the transverse trace-free plane `L_u ≅ ρ`.

The mixed evaluated source is `ε ⊗ T′ = 1 ⊕ ρ`. Its trivial component is nonzero in the one-dimensional trivial summand of P5 by cubic interpolation and the harmonic-cubic interpretation of the unique mixed map. The quotient of `T ⊕ P5` by the pure image has types `1 ⊕ ρ`. Hence the remaining mixed component adds either zero or two dimensions. The resulting even rank is exactly six or eight.

The coupling Γ(s) = projection_(u-perp)(g(s,u)u) is in fact D-equivariant on the untwisted rho part of T′: the two factors of ε arising from the two occurrences of u cancel. On the mixed rho image, its vanishing is equivalent to membership in L_u. This verifies the stated equivalence between Γ = 0 and even rank six, including the evaluation-twist bookkeeping.

When α = 0, the entire even image lies in P5; the pure image has dimension four and interpolation supplies an independent fifth direction. Thus even rank is exactly five without an additional local-type argument.

The negative-central-action irreducibles of Dic3 are E (dimension two) and η± (dimension one). The odd evaluated source is `2E ⊕ η+ ⊕ η−`. Repeated-input injectivity supplies an E in the image. Therefore odd rank three has exactly `E ⊕ η+` or `E ⊕ η−`, as claimed.

## Imported dependency

The fifteen-axis cubic interpolation lemma, the models F3 and F5 and their kernels, the nonvanishing arguments for β and the mixed scalar, and the multiplicity-one harmonic-cubic interpretation of g are consistent. The quaternion exact-rank conclusion is also valid.

## Universal nonvanishing of the transverse coupling

Both new proofs in Section 6 are valid.

For the short proof, the coordinate even-sign-change subgroup is V4, and T′ restricts to its three nontrivial characters once each. Its x-character cubic is necessarily

    C_x = x(Ax² + By² + Cz²),
    3A+B+C = 0.

The second equality is exactly the harmonicity condition. The chosen point u=(1,1,1) is one of the ten order-three axes. Full symmetry of the cubic embedding identifies the transverse derivative with a fixed nonzero multiple of Γ. If Γ vanishes on the rho constituent, all T′ cubics have radial gradient: the remaining order-three-invariant line has no possible invariant transverse derivative. But

    gradient C_x(1,1,1) = (0,2B,2C)

is radial only if B=C=0, hence A=0. This contradicts the nonzero x-character line. Thus Γ is nonzero at u, and equivariance gives nonvanishing at every axis.

For the independent angular-moment proof, P has rank three in the seven-dimensional irreducible SO3 representation H3. The two A5-invariant trace polynomials have degrees two and four; the cited Section 1 of `../order-four-rank-five-exclusion/PROOF.md` correctly proves that their only possible forms are multiples of q and q². SO3 averaging then gives

    trace(P L_u²) = 12,
    trace(P L_u⁴) = 84.

If Γ=0, the two nontrivial order-three eigenspaces of T′ are exactly the weight +2 and -2 lines. Their second- and fourth-moment contributions are 8 and 32. The remaining line lies in weights 0,+3,-3, where L_u⁴=9L_u². Its second moment must be 4, so its fourth moment is 36. The resulting total fourth moment is 68, contradicting 84. This independently confirms Γ≠0. Orthogonality and evaluation twists cause no issue.

## Final conclusion and scope

Consequently α≠0 forces even rank eight and odd rank at least three at every order-three axis, giving total rank at least eleven and residual rank at least seven. A residual-rank-five point would therefore require α=0 and parity ranks exactly (5,4).

Importing the separately established full-normalizer theorem α≠0 excludes O250. The present audit confirms that implication; it does not replace the separate audit of the full-normalizer theorem or re-audit the global finite-support classification. With those standing dependencies, the stated removal of O250 and O375 and the remaining alternatives empty support or M follows.

Minor editorial point only: Sections 4–5 still refer to “alternative 1” and “alternative 2” from the earlier result statement. They describe the two provisional local alternatives before Section 6 rules out the second. Numbering those two provisional alternatives explicitly would improve the current presentation; no mathematical change is needed.

No actual-operation coefficients or selected-input rank instances were evaluated, and no external state was changed.
