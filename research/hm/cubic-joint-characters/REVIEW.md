# Independent mathematical review: joint cubic characters

**Verdict: PASS**, relative to the stated pinned geometric inputs. No mathematical blocker was found in the new argument. This is a mathematical review, not formal verification and not a fresh re-proving of the dependency chain.

## Materials and method

Read the proposed `PROOF.md`, together with the local proofs for eigenline interpolation, cubic embedding locus, and cubic fixed directions. The main proof states immutable pins for its dependencies. This review checks the mathematics against those supplied dependency statements and local texts; it does not independently certify remote commit/file identity. No actual HM/source coefficient, selected point, matrix, evaluation, numerical rank, search, or computer-algebra calculation was used. The residue arithmetic below concerns universal abstract character labels only.

## Checks

1. **Honest lifts and normalization.** For the chosen order-five lift, the nondegenerate central commutator makes the five eigenvalues a full fifth-root orbit, so the indexing is legitimate. The diagonal maps with eigenvalues zeta^i and zeta^(i^2) commute and have fifth power one. If g^a h^b were scalar, the polynomial ai+bi^2 would be constant for all five residues, forcing a=b=0. Hence both the linear group D and its projective image have order 25. On L_i the conjugate h s h^(-1) has scalar zeta^(2i+1) relative to s, which agrees with zeta^(-1)g^2s. Thus h really normalizes the Heisenberg group and induces a nonidentity unipotent shear fixing G.

2. **Free 25-point orbit.** The shear cycles the other five projective directions. The projective subgroup G acts transitively on the five eigenlines for any such direction by the nontrivial commutator. These facts make D transitive on the 25-point complement. Since D has order 25, all stabilizers there are trivial. The natural O(3) linearization is honest because the chosen group acts linearly on A. Transporting a nonzero fiber vector along this free orbit gives the regular representation, regardless of initial trivializations; the dual is regular as well. There is no omitted stabilizer or scalar character.

3. **Equality with the actual kernel.** The interpolation dependency proves surjectivity on the 25-node complement, not just a lower bound on the full 30-node restriction. The same theorem works for any chosen G by choosing the corresponding Schrödinger eigenbasis. Its kernel has dimension ten. The complete actual cubic ideal W lies inside that kernel and has dimension ten by the geometric dependency, so equality of actual subspaces follows. No matching-character or matching-dimension argument has replaced the required inclusion. D-invariance follows because D preserves the actual eigenline node configuration.

4. **Dual convention and character subtraction.** Functions belong to Sym^3(A*), whereas the dual quotient is Sym^3(A) onto W*. Dualizing the surjective restriction map gives precisely the displayed exact sequence. Over C the character-summand functor is exact for this finite abelian group. Every character occurs once in the injected regular module, so its multiplicity in W* is its multiplicity in Sym^3(A) minus one. Inverting characters on the function side does not change this conclusion or the tensor-side labels.

5. **Multiplicity exactly two.** The affine reduction to S=Q=1 preserves equality of both joint weights. An all-equal triple fails the square-sum equation. For a distinct-entry triple the complementary pair would have sum 4 and product 1, giving nonsquare discriminant 2, hence cannot exist in F5. For a repeated-entry triple the equation is a(a+1)=0. Thus exactly the two listed unordered multisets occur. They are different and each spans one symmetric tensor line. The repeated-index weight therefore has multiplicity two in Sym^3(A), and exactly one in W*.

6. **Nonvanishing and geometric evaluation.** The polarization expansion uses arbitrary vectors on the abstract lines, not selected geometric coefficient evaluation. Since cubics vanish at the node, the exceptional value is represented by q(u^2v), up to the nonzero scalar 3 and fiber trivializations. Generation of 3H-E guarantees that this vector is nonzero for every exceptional direction; the proved exceptional linear embedding is stronger than necessary. The same applies to the partner tensor. Thus the one-dimensional target character space forces equality of the actual projective values, rather than merely permitting equality or forcing both vectors to vanish.

7. **Conclusion and completeness.** The partner base index 2i-j differs from i, and its direction index 3i-2j differs from 2i-j, when i differs from j. The two points lie on distinct exceptional divisors and are genuinely distinct. This already rules out an embedding. With the fixed-directions dependency's exhaustive alternatives r=0 or r=1 and its implication r=0 => closed immersion, r=1 follows. The sixty reduced double fibers, their presence on Y, and the exact reduced singular/nonnormal loci are then justified by that dependency. The pairing formula is an involution with no fixed mark. For each of the six directions it pairs twenty marks into ten pairs, agreeing with sixty pairs overall; the dependency's exact fiber classification excludes additional fibers.

## Scope

No assertion of transverse image branches, completed local rings, conductor lengths, full-adjoint membership, higher lifting, or algebraicity has been inferred. In particular, normalizer invariance of the actual cubic ideal follows from node preservation and does not require an equivariant presentation of the selected primary matrix. The new proof closes the r=0 versus r=1 alternative without any forbidden selected-instance computation.

## Reviewed version

The substantive proof, including the explicit scalar-polynomial proof of the projective order of D, was reviewed at SHA256 `48a815a6a8ab961d986c19b162092de9313f59711890ce2e86c24c261971d6c6`. A subsequent status-only edit recording this PASS does not change the mathematical assessment.
