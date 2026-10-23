# Full ambient HM symmetry boundary for the fixed octic gate

The FULL projective HM stabilizer is the projective Heisenberg normalizer, by the verified primary theorem of Decker, Math.Z.188(1984), Theorem4.2.3. Its stabilizer of the chosen invariant rank-three quadric and fixed negative pencil is exactly the existing SL2(F5). Thus no additional ambient projective same-bundle symmetry can contribute a new character forcing the octic scalar.

Read FULL-SYMMETRY-CLOSURE.md for the current full-group conclusion and exact primary definitions/pages. PROOF.md is the frozen PartI computation inside the known normalizer. Its deliberately input-limited 'outside unclassified' boundary is SUPERSEDED by the separate closure note, not silently rewritten. Its historical RESULT.json likewise records only PartI; FULL-SYMMETRY-RESULT.json records the current conclusion.

Reproduce PartI with `python verify.py` and `python -O verify.py` (33 checks each). Reproduce the closure with `python verify_full_symmetry.py` and `python -O verify_full_symmetry.py`. Append `--primary-pdf PATH` to authenticate a separately downloaded public full-volume scan; its URL, digest and exact page locators are in PRIMARY-SOURCE.json. The copyrighted full-volume PDF is not redistributed. The closure checker checks provenance and group/order conversion, not a machine proof of Decker's theorem.

No actual coefficient or parameter is evaluated, no octic scalar is selected, and no source or pair is removed. Cone-only or nonambient automorphisms remain a different question and are not substituted into actual-pencil naturality.
