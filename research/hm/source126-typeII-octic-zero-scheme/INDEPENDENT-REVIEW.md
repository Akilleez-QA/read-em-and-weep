# Independent review: canonical octic target zero scheme

The complete proof and bounded checker were independently read and replayed. No mathematical blocker found in the stated universal section theorem, local scheme description, or graded resolution.

## Frozen bytes

- PROOF.md: 97c734b913f4603a4bb1f34e36d66bc3dfb46929ef48ae5beeb7dce5617ee7a3
- verify.py: 82233490033be4bd0252d39eaa359d62c8f804e11afc23cce38db2762ccba43c
- INPUTS.json: abdc631b34aab94813fe3fa8344bac3dd4c090ca197f11082b976b89375f206d
- RESULT.json: b9086b55736530fbe0db5964fae5434cdc6ff438bea0122e5b8637e7b6e3c81d

Both `python verify.py` and `python -O verify.py` passed 92 checks, with identical stdout and RESULT.json. The two immutable source files authenticate against their SHA256 and Git blob identifiers. Their proof hashes match the previously independently reviewed PR982 and PR995 packets.

## Independent mathematical checks

1. The invariant zero divisor, if present, has an invariant equation because the effective group A5 has no characters. Dividing it out produces a forbidden invariant section of a lower twist. Negative twists have no sections by the defining presentation and plane H1 vanishings. Thus there is no divisorial zero. A regular rank-two section on the smooth surface has finite local-complete-intersection zero scheme of length c2(E(4)) = 6 + 12 + 16 = 34.
2. The conic restriction is identified by the actual first-derivative evaluation map, not by degrees alone. Its kernel is precisely the quartics divisible by the square of the vanishing linear form, and its target is W O(3). Twisting yields W O(11). Vanishing restriction would contradict H0(E(2))^G = 0. The unique invariant degree-12 binary form has one reduced size-12 orbit as its divisor; its gradient has no projective common zero. This proves that the entire conic is disjoint from the section's zero scheme.
3. Independently, the explicit public Wronskian polynomial was checked to have gcd one with its derivative over Q(sqrt(5)), and nonzero leading coefficient. This corroborates, but is not needed for, the orbit-based squarefreeness argument.
4. Off-conic projective stabilizers containing order 3 or 5 fix the corresponding non-isotropic rotation axis and equal its cyclic-subgroup normalizer. Each axis orbit is unique. Other stabilizers have exponent two and order at most four, so the exhaustive sizes are 6,10,15,30,60. The only nonnegative orbit-length solution of total 34 is 6 times 4 plus 10 times 1. This argument uses the present section, not prior degeneracy schemes of other maps.
5. At an order-five axis the tangent and fiber character pairs are ±1 and ±2 modulo five. Equivariant formal coordinates and a local frame exist in characteristic zero. The quotient by (u²,v²) has only characters 0,±1, so both full section components belong to this ideal. Their ideal has colength four by the global orbit argument, forcing equality with (u²,v²). This proves the completed ideal, not just the tangent cone.
6. The regular section O(-4) into E has determinant quotient I_Z(7). Pulling back the presentation of E gives an extension of O(-4) by A O(-1), split since H1(O(3)) = 0. The resulting resolution is 0 → A O(-8) ⊕ O(-11) → D O(-7) → I_Z → 0. All matrix entries have positive degree. Plane H1 vanishings make its graded global sections an exact minimal resolution of the saturated ideal. The asserted five septic generators, three linear syzygies, one quartic syzygy, Hilbert series, and stabilization at length 34 follow.

## Scope boundary

This identifies the zero scheme of the canonical invariant target factor sigma only. It does not compute additional source-covector zeros, choose the actual octic scalar, establish source occurrence, exclude a catalogue pair, or repair the original proof. The checker is bounded universal algebra and representation verification, not actual HM evaluation or proof-assistant verification.
