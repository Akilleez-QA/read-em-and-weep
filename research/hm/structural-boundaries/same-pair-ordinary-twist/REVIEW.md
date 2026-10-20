# Independent review: same-pair ordinary scalar-twist exclusion

## Verdict

**Accepted at the stated, source-bound scope.** There is no blocking algebraic, sign, normalization, legal-open, or quantifier issue in the reviewed proof. The fixed ordinary scalar-twist descent prescription cannot extend through the repeated-pair second order for either source pair. This is an associativity compatibility failure of that prescription, not a calculation of the mixed obstruction class or a frame-invariant obstruction to other deformation formulations.

Reviewed artifact:

- `../same-pair-ordinary-twist-exclusion-20261018/PROOF.md`
- SHA256: `587f953427e40b33c2758e221dfb4f7cdde1798c9ab9bb09a180c78ba4b127cc`
- Review date: 2026-10-18

I independently derived the one-parameter associator before reading the finalized proof. The independent derivation is in `DERIVATION.md`. A separately written invented-freeword control is in `check_freeword.py`, with successful normal and optimized transcripts. No actual source/model/matrix/polynomial/point/jet/residual was executed or evaluated.

## 1. One-parameter identity and all quantifiers

For the row convention `g_jk g_ij=g_ik` and ordinary right-hand scalar multiplication, put

    T_ij = g_ij + ε U_ij + ε² W_ij,
    h_ijk = 1 + ε b_ijk + ε² c_ijk,
    T_jk*T_ij − h_ijk T_ik = ε² D_ijk mod ε³.

Allow arbitrary scalar c, every valid first lift U, and arbitrary matrix-valued second edge W. Direct associativity gives

    0 = g_kl D_ijk − D_jkl g_ij + D_ikl − D_ijl
        + S_ijkl g_il + A_ijkl,

    S_ijkl = c_ijk+c_ikl−c_jkl−c_ijl
             +b_ijk b_ikl−b_jkl b_ijl,
    A_ijkl = μ(g_kl,b_ijk)g_ik − g_jl μ(b_jkl,g_ij).

Thus, with left normalization M_ijk=g_ik⁻¹D_ijk,

    δ_row M = S Id + g_il⁻¹ A,
    δ_row tf(M) = tf(g_il⁻¹ A).

This independently confirms the proof's sign and normalization side. S is permitted to be nonzero: imposing a scalar second-order cocycle is unnecessary. The entire dependence on c is scalar, so no scalar c can cancel a nonzero trace-free anomaly. The formula contains no first lift and no second edge. The second edge's contribution to M is an ordinary row Čech boundary; the explicit freeword control also retains all six second edges independently and checks their cancellation.

There is one product U_jk U_ij, one μ term at each endpoint and one negative b_ijk U_ik term. Importing the mixed sector's doubled coefficients would be wrong. The standard repeated-pair ν coefficient is 1/8, but the no-go deduction uses only associativity and μ, not the particular ν. The reviewed proof's slightly broader quantifier over associative second-order products with this same μ is justified.

## 2. Positive coefficient and cyclic negative control

On the same accepted carrier, P_c I_c=Id gives the actual transition g_ij=D(ν_j/ν_i), with D(z)=diag(z,z⁻¹). For the increasing masks

    00, 10, 01, 11,       a<b,

one has g_23=D(r_a), g_02=D(r_b), g_03=D(r_a r_b), b_012=(15/4)r_a r_b, and b_123=0. Consequently

    g_03⁻¹ A_0123 = +(15/8)(V_a r_a)(V_b r_b) diag(1,−1).

The sign is positive because the final edge increases the a-bit. The factor 15/8 consists of 15/4 from b and the single 1/2 in μ. No second same-pair term doubles it.

The curve relation and quotient rule, without point evaluation, give

    V(y/x) = [x(3x²−1)/2−(x³−x)]/x² = (x²+1)/(2x).

Therefore the exact normalized witness is

    +15(x_a²+1)(x_b²+1)/(32 x_a x_b) diag(1,−1).

For the separate cyclic ordering 00,10,11,01, the final edge is D(r_a⁻¹) and the same calculation changes only the sign. The proof correctly uses the increasing order for its primary certificate. These are distinct increasing source masks when the unaffected bits are zero, so the certificate does not depend on an all-ordered extension of the source's owner convention.

The matrix is already traceless. More generally det(g)=1 makes both normalized anomaly summands scalar linear combinations of conjugates of traceless logarithmic currents. Determinant one removes their trace; it does not make them zero.

## 3. Genuine common open and rational nonvanishing

The same auxiliary carrier D(v_0 v_1 v_3 v_4) is an existing source carrier. Its pullback is nonempty: the x-map C→P¹ is surjective and the coefficient map (P¹)⁴→P⁴ is surjective over C by factorization of binary quartics. Therefore the composite f is surjective. The carrier is nonempty and open in the integral X=C⁴.

The four masks' common legal locus is

    (U_0∩U_1)_a × (U_0∩U_1)_b × product_(d≠a,b) U_0.

It is a nonempty dense open. Its intersection with the carrier is nonempty by irreducibility. All four owners can use the same finite standard tag: every factor already lies in U_0, the finite chart. The draft's mention of a further finite-chart intersection is harmless and redundant, not an extra restriction that threatens nonemptiness.

In factors a,b, the common legal locus removes O and the three branch points, so x, y, r=y/x and r⁻¹ are regular where needed. The accepted carrier-localization theorem supplies regularity of the structural primitives and their physical transitions. Hence this is a genuine common four-owner intersection, not a formal empty intersection or an illicit localization added to a primitive.

Since x is nonconstant, x²+1 is not the zero rational function. The product variety is integral. Thus the displayed rational coefficient is nonzero, and its restriction to a nonempty open remains nonzero. Its possible zeros on proper divisors do not affect the argument. No numerical point, primitive entry, source polynomial, or physical matrix was evaluated.

## 4. Scope of the accepted conclusion

A successful extension would have D=0 and therefore tf(g_il⁻¹A)=0 on every common quadruple. The displayed nonzero section contradicts that necessary condition, independently of U, W and c. In fact the specified trace-free same-pair defect has nonzero Čech boundary; it is not a closed degree-two cochain to which the ordinary degree-two class argument could be applied.

The accepted statement is limited to the fixed g, the prescribed ordered b, the given μ, and ORDINARY scalar multiplication in h T. It establishes no nonzero mixed class, no same-pair degree-two cohomology class, no failure of arbitrary higher-order frames, no exclusion of star-multiplied or non-scalar twists, no obstruction to all quantizations, and no algebraicity result. The reviewed proof explicitly maintains these boundaries. No blocking overclaim was found.

The accepted mixed-closure theorem is unchanged: its complementary derivatives of the scalar coefficients vanish. The present repeated-pair derivatives do not vanish. Whether the already-closed mixed representative is exact remains unresolved by this packet.

## 5. Inherited display typo

The accepted structural-closure proof §6 has a displayed first-lift equation missing U_ik. Its preceding identity δ_row x=b Id−C gives the corrected equation

    U_jk g_ij + g_jk U_ij + μ(g_jk,g_ij) = U_ik+b_ijk g_ik.

The new proof explicitly records that typo and derives its correct equation from the preceding cochain identity. This is a non-blocking inherited display error, not an additional hypothesis and not a reason to import the incorrect equation. No accepted dependency was silently edited in this audit.

## 6. Independent controls and their evidentiary limit

`check_freeword.py` uses invented free noncommuting word labels and commuting scalar jet labels, with exact rational coefficients and formal commuting Leibniz derivations. It imports only Python's `fractions`; it reads, imports and executes no production module or physical model.

Its positive checks are:

- all four first-lift routes, with arbitrary adjacent lifts and an arbitrary scalar b cocycle;
- the complete ε² associator with arbitrary h₂ and independent W on all six edges;
- both scalar product-rule endpoint errors;
- the independent repeated-pair Moyal associativity identity with coefficient 1/8.

It rejects these deliberate mutations:

- reversal of the anomaly sign;
- importing a mixed-sector factor two;
- changing the repeated-pair ν coefficient from 1/8 to 1/4;
- omitting −b U;
- reversing the first anomaly's word order;
- dropping the ordinary scalar associator S.

Both `python check_freeword.py` and `python -O check_freeword.py` pass. The checks use explicit exceptions rather than assert statements. These controls test the universal ordered algebra and mutation sensitivity; the geometric carrier/nonvanishing argument and actual source binding are the handwritten arguments using the accepted source-bound geometric proofs. They are not source-value certificates.
