# Independent review: cone source-row matching

Reviewed on 2026-10-23. Structural mathematics only; no actual source instance, coefficient, parameter, point, derivative, matrix, primitive, rank, or response was selected or evaluated. No external write or publication was performed.

## Verdict

PASS as a conditional written theorem. I found no mathematical blocker in the new cone-only comparison or in its use of regular divisibility. The conclusion removes the need to assume that the independent cone contraction extends ambiently; it does not assert or construct an example of a nonextendable contraction.

The reviewed PROOF.md was 10,914 bytes, with SHA-256:

d5805f030eab27138adc250b98700749419e246cc7b1f5652a4c73647861a29e

I read the proof and all four provided input copies in full. Their hashes matched all four pins in the proof:

- cone908.md: aafd5ee2b8a0a1d0876886b4db361c05d2a34cc41ab59e44ecec54580061cfcc
- divisor909.md: 824b6fdb62f835a21f42ad50b038c038a5c035a677f7a6cb454a31328fff1a35
- normalization866.md: a7f6afe41fe569cb9a061a047b1d0a140fd198950cda6fe3bace6978f3cf0b14
- pr815.md: 78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236

## Independent algebra check

Write d for the monad differential on the cone and d' for its tensor twist. The cohomology targets are concentrated in degree zero. For g = p_B i_A, the claimed inverse k = p_A i_B satisfies

k g = p_A (1 - d H_B - H_B d) i_A = 1,
g k = p_B (1 - d H_A - H_A d) i_B = 1.

Only p d = 0 and d i = 0 are needed to remove the error terms. Thus the inverses exist as regular compositions of the supplied maps, not by inverting a source coefficient. The same argument applies at every twist. No normalization such as H squared = H i = p H = 0 is used.

For a degree-zero u, including a nonclosed u, set v = delta u = d' u - u d. The B contraction gives

i_B g_0 = i_A - d H_B i_A.

Consequently p_B' u i_B g_0 = p_B' u i_A + p_B' v H_B i_A. This independently reproduces C2 with its positive sign. The A contraction gives

g_t p_A' = p_B' - p_B' H_A' d',

so g_t p_A' u i_A = p_B' u i_A - p_B' H_A' v i_A, reproducing C3. Subtracting, applying g_t inverse on the target, and taking trace-free parts gives exactly

P_B(u) - P_A(u) = (g_t inverse p_B' (v H_B + H_A' v) i_A)_0.

The direction of frame transport and both homotopy summands therefore agree with C4 and the pinned PR866 convention. All these operations occur on the cone. They do not require an ambient extension of B_Q.

PR908 supplies the global exact source s before choosing W or an ambient E. Applying the identity to an existential global primitive e with delta e = s gives C5 by the two authenticated factor-row identities. It is essential that e is not treated as closed. The derivation never differentiates s, and no delta s term has been omitted. C1 supplies closure independently, while delta squared e = 0 is a second consistency check. The actual global-cone coefficient theorem, rather than a vanishing of all cone adjoints, supplies independence from the choice of global primitive.

## Divisibility and gluing check

The full-domain operator R is defined on rY whether or not that input belongs to the exact-source image. O-linearity and compatible tensor twists give R_4(a rY) = a R_2(rY) for each fixed a. This uses more than an isolated q-compatibility identity. No derivative of a appears in a Hom differential of O-linear complexes.

Under the explicitly retained physical marking and cover-weight-zero condition for a, extraction yields eta_i = a_i xi_i with regular xi_i in Sym^12(U) tensor O_L(-2). The type is the trace coefficient type at twist four tensored by O_L(-2); the positive binary degree does not change. Regularity across every zero of a follows from construction by regular maps, not division by a value.

If eta glues, the overlap discrepancies of xi are annihilated by the nonzero section a. Since L is integral and the coefficient sheaf is locally free, multiplication by a is injective on stalks, including at repeated zeros. Hence the extracted xi glue. The vanishing H0(P1,O(-2)) = 0 then forces xi = eta = 0. This establishes C7 without assuming globality of R_2(rY), and without representing eta as a closed global cone adjoint.

C8 has the correct negative source-response sign because Q_A and the full y_A are fixed in both expressions. The nonzero global multiplier a^3 h is an injective map from the trace coefficient sheaf to the scalar target sheaf. Therefore, given the separate paired-global rho_A prerequisite, mixed scalar gluing is equivalent to gluing of eta. Combining with the preceding vanishing proves C9.

## Scope and packaging

The proof appropriately keeps the actual contraction/extraction certificates, global source membership, full ambient lower packet, paired scalar globality, and mixed scalar gluing as separate requirements. It proves trace matching only on the certified source, or on a family for which all gates and gluing are established. It does not infer whole-row operator equality or matrix equality from one scalar/source check.

The final INPUTS.json is present. I checked all four local byte counts, SHA-256 hashes, and Git blob hashes against it; all agree. Its immutable commit/path URLs also agree with the proof. I re-read the final proof after the notation-only correction from C_Q^0(4) -> C_Q^1(4) to C_Q^0 -> C_Q^1, appropriate because PR908 already incorporates twist four in C_Q. I did not re-fetch the upstream GitHub blobs or re-audit the earlier geometric ancestry; this review verifies the supplied exact inputs and the deduction from them.
