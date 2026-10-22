# Independent review of the global first-subleading residue theorem

## Verdict and scope

**PASS, subject to the stated upstream theorems.** The global residue argument is valid: the first-subleading coefficient of the actual invariant nilpotent defines a regular invariant section of the specific equivariant quotient C, and that section vanishes because H0(C)=V has no invariant vector. This supplies regular local weight-four gauges along every point of L. It does not supply a single global gauge, erase the remaining normal coefficients, or determine the fifth obstruction.

Reviewed proof: `PROOF.md` in this directory, final frozen SHA256 `43200eeebb2ec4b4809433d1568e4f244219be899f9a20a3e3d4afbe016f54ea`.

The audit independently read the exact immutable source files and checked the mathematical interfaces, rather than relying on filenames or a generic quotient analogy. No actual source coefficient, selected point, matrix rank, model experiment, or large computation was evaluated. This is a deductive review, not proof-assistant verification.

## 1. Exact upstream interfaces

At commit `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`, under `research/hm/order-four-quadratic-load/`:

- `INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md`, especially §5, constructs the actual nonzero Γ-invariant N in H0(Q,End0(F)(2)) by symmetric squaring the saturated equivariant spinor inclusion. Thus invariance is an actual input, not inferred merely from the dimensions of a space of sections.
- `VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md`, §§1–3, gives uniform flat Loewy layers, coprime cubic/quintic leading forms at every base point, K3=O(-2) in Sym3 U O(1), and the nonsplit quintic-generator extension. No global quintic lift is assumed.
- `NO-PRESERVING-POSITIVE-CONE-EXCESS.md`, §§2–3, explicitly supplies the relative local regular-pair construction, including the local Koszul description, and the actual presentation 0→U O(-5)→Sym4 U O(-2)→G2→0.
- `UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md` proves this exact quotient is equivariantly V O, with V=Sym2 U the positive nontrivial three-space. Its theorem is not a statement about the different cubic quotient A O(2). The proof uses an everywhere-injective cubic multiplication map, exact cohomology, and the representation-dimension gap; it leaves no unidentified quotient character.

I also read the exact published proofs at PR774 commit `eec909bef4a7e6998737773d5eadd0ad562e79d9`, PR775 commit `af2fc052d3da2c4abc315dca268ed65b62f5cde5`, and PR776 commit `c885531e345cc67d1848b0cd8baa0f02ca786f47`. They respectively supply the physical filtration, the complete fifth-norm formula/global quotient, and the local nilpotent tangent exact sequence.

## 2. Regularity over the whole base

The local algebra is applied to the leading pair, not to an assumed homogeneous full pair. Relative regularity permits shrinking around any point of L so that the degree-seven multiplication map fS4⊕gS2→S7 is an isomorphism. All coefficient modules are locally free.

Fiberwise the tangent equation has kernel dimension 18 and the weight-four commutator map has injective rank 15. Constant rank therefore gives a vector-bundle quotient of rank three. The scalar map v↦[vn] factors through S4/fS1 by the displayed explicit commutator identity, and is a fiberwise isomorphism onto that quotient by PR776. Consequently its inverse ν is regular over the base. No rational inverse or saturation across an unverified exceptional fiber is used.

The leading multiplier u is a unit. In the local Koszul model, the actual spinor inclusion identifies the spinor module with the kernel by an isomorphism, not a map with a base-zero factor. Endomorphisms of the rank-one reflexive spinor module are scalar functions, and an isomorphism has a unit multiplier. Squaring and the line/determinant identifications preserve invertibility. Taking its leading term gives a base unit. This is compatible with the construction off the vertex and reflexive extension; it is not an extra nonvanishing assumption on an unknown coefficient.

Since N²=0, its weight-twenty coefficient is n8D12+D12n8=0. Vanishing of its residue thus implies D12=[X,n8] with X regular locally. Injectivity of the commutator map makes X unique in a fixed local homogeneous frame, but does not make the chartwise choices a global gauge.

## 3. Canonical descent and scalar twists

The physical transition has weight-zero part T0=[[a,0],[c2,d]], where a,d are base units and c2 has cover degree two, followed by a weight-four correction. Its weight-zero part is genuinely invertible in the weighted graded algebra. It sends the leading pair to (af,c2f+dg), up to the expected invertible normalizing factor. In particular the cubic principal ideal is preserved, without choosing a global quintic generator.

Conjugation by T0 transports both the tangent equation and its commutator image. Crucially it transports vn to v times the new leading n, so the normalized scalar isomorphism transports the quotient class without an extra factor. The weight-four transition contributes only a commutator and is killed by ν. Its scalar trace part, if present, commutes and has no effect.

The standard negative-coordinate changes are homogeneous in transverse variables. The O_Q(2) transition is a base-only unit, so it multiplies n8 and D12 equally and cancels in the scalar comparison. There is no additive residue term from a positive-weight scalar transition in this atlas.

Cover-degree-four scalar coefficients have bundle Sym4 U O(-2). The cubic relation has coefficient tensor in Sym3 U O(3), since its source is O(-2) and target Sym3 U O(1). Its linear multiples inside Sym4 U O(-2) therefore have source U O(-5), exactly as claimed. This identifies the descended scalar target with the precise upstream equivariant quotient, not merely a rank-three bundle with matching generic fibers.

All these constructions are natural for Γ and its homogeneous action on the negative-coordinate atlas. The standard scalar-coordinate linearization is retained. The actual invariant N consequently gives a section of H0(C)^Γ. Since C≅V O equivariantly and V is nontrivial irreducible, this section is zero. No equivariant trivializing frame or canonical splitting of the nilpotent jet filtration is asserted or needed.

## 4. Fifth-norm application and retained boundaries

The harmonic lift of the regular even entries of X produces an allowed local ambient gauge. To the indicated order, B0 changes by s(D12−[X,n8]) and therefore vanishes. Every other Bj must undergo the same conjugation. Trace cyclicity preserves the complete bilinear norm pairing before harmonic extraction, so the argument does not discard compensating terms.

The subsequent local q4 correction removes B4 only modulo the already established source-multiplied relation image. The remaining index set 1≤j≤3, 0≤i≤3, i+j≤4 contains 4+3+2=9 ordered terms. This count is correct.

The proof retains the scalar-reference subtraction, the full source divisor with its multiplicities, the unsaturated relation image at source zeros, and the final transported beta2 quotient from PR775. It asserts no global frame change and no global B4 correction. Thus the simplification does not evaluate beta4, establish beta2-image membership, prove fifth-neighborhood lifting, or settle algebraicity.

## Final review status

No substantive mathematical blocker found. The requested source-hardening edits are incorporated in the final frozen proof: the local theorem is pinned to immutable PR776; the relative regular-pair source is explicit; and the unit normalization is justified through the actual Koszul-kernel isomorphism. The final hash was verified after those edits. The verdict remains PASS.
