# Independent mathematical and implementation review

Verdict: ACCEPT for the stated universal scope. Reviewed on 23 October 2026.

## Immutable reviewed bytes

- PROOF.md: SHA256 357419b6b6eab57dd52bceaa7fc8e1369a390656f335e84f61fc4debbfb04f3e.
- verify.py: SHA256 a0b0f7006c993cf8333094e4af0833651b548983d9860b4b54d6789cad839008.
- RESULT.json: SHA256 d4ba80ea9179ed456ef035f11b018b05761eb9dd01506e1171a15ccac941e17c.
- INPUTS.json: SHA256 a6d48b5fe5cee4d9868053f6c5a9ffaafd3bd8e913d06c664778d305daf0bede.

## Mathematical review

1. Kernel restriction is fully faithful for the two displayed everywhere-surjective linear coefficient pencils on the same projective line. The extension is unique because both H0(O(-1)) and H1(O(-1)) vanish. The descended target map is a genuine constant coefficient map, not a parameter-dependent lift. Restriction and extension are inverse; the equivariant restriction follows from uniqueness.
2. The standard bidiagonal pencil has the stated no-common-zero kernel generator and kernel O(-m). The direction of the Hom formula is correct: maps from E_n to E_m correspond to H0(O(n-m)). The boundary cases E_1 and E_2 are retained.
3. Under the expressly supplied coefficient-pencil direct sum, all long target components vanish, E_1 contributes no terminal target, and the E_2 terminal map is arbitrary. The sharp rank bound min(r,dim B2) is correct. The residual-complement bound is necessary only; no unwarranted sufficiency is asserted.
4. No actual HM decomposition is deduced from a character or a kernel degree. The specific PR1122 contradiction is explicitly credited as prior mathematics. The new contribution is the reusable solver and constructive full-coefficient certificates, not literature novelty or another actual catalogue exclusion.

## Implementation and execution

The reviewed solver constructs both x and y coefficient equations, uses exact Fraction arithmetic, produces full nullspace bases by RREF, and uses explicit exceptions rather than assertions. The final normal and optimized executions each produce 327 checks and byte-identical output matching RESULT.json. Input byte and Git-blob authentication succeeds; this authenticates the retained motivating text, not its entire mathematical ancestry.

The independently written direct-matrix-product test `independent/check_independent.py` runs 240 checks in both normal and optimized modes, with byte-identical outputs matching `independent/RESULT.json`. It locates `verify.py` relative to its own path, so it is relocatable with this packet. It compares assembled equations against literal B_x F-G A_x and B_y F-G A_y products for 70 source/target rectangles (including source size7), checks all returned bases and Hom dimensions, tests 20 multiple-source assemblies through r=8 and target size16, and verifies malformed-size, ragged-row, split-coefficient, empty-system, and zero-kernel controls. Both runs agree. No actual HM matrix, parameter value, source coefficient, or selected-direction rank was evaluated.

The packet is suitable for a focused universal test-artifact PR. It is not a proof-assistant certificate, a geometric realization, or a complete repair.

## Independent reproducibility files

- independent/check_independent.py: SHA256 90e2cfa48e19b3ae81607bb8119c6802c6d71600eef6170446f8a83cfbbd5169.
- independent/RESULT.json: SHA256 4433daa2ae934046fb700fec8f25687e8ea1337e5353530cccbc263e8b302c2c.

From this packet directory, run `python independent/check_independent.py` and `python -O independent/check_independent.py`. Both outputs must match `independent/RESULT.json`. The independent test checks full polynomial coefficient identities, not parameter samples. These supporting checks supplement rather than replace the mathematical argument in PROOF.md.
