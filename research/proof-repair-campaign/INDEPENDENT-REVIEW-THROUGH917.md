# Independent mathematical and accounting check of PR917

## Scope and immutable evidence

The checked statement is exclusion of original source index127, tuple
`[1,1,1,0,0,1,0,0]`, at `G3.11.cce6e3ba4eeb`, and not exclusion of that
stable label. The proof is conditional on the actual equivariant Gauss setup
and its pinned source data. It is not proof-assistant verification or a
complete repair of the original problem.

- PR917 commit: `c17aac695580fff0ff7dacd1247ce0b8adf01a8f`.
- PROOF.md SHA256: `c602fc27d75db4f386d00e8a65ced14888fc5f463f516b76e1c54f9306a909cc`.
- Author verifier SHA256: `416c76ff2422524d26c1b5ca4b6938c0deb8e089a951155e229471add936af79`.
- PR913 prerequisite: `b84ea860de5ebe38cff3c54054e80dd4be5ac77c`, proof Git blob `ac36f048fc0987a1c78fbd9a61bc18077963ce20`.
- PR905 prerequisite: `2db172b32dc014c06521a3fcba20261db5bb00fa`, proof Git blob `3448047b9f67b258955f0fe53c3368b6f7615d9e`.

The complete PR917 proof, its six pinned dependencies, and the PR913
reduction were read. All six dependency blob hashes authenticate. The
original proof verifier passes in ordinary Python. Its use of assert means
that optimized execution is not counted as an additional author-proof test.
The new accounting verifier uses explicit exceptions and its tests pass
both ordinarily and under `python3 -O`.

## Independent proof reconstruction

1. The positive Gauss preimage has equivariant Euler character
   `A - V - 2P - D`, forcing one actual constant A. Only the high degree18
   quotient carries A. A common divisor of the three coefficients could
   only have invariant degree12; the residual A is absent from Sym6 W.
   Consequently the map to the high line is surjective everywhere.
2. Its rank2 kernel has degree-18 and cohomology character V+2P+D.
   The pinned high-row classification leaves W(-9) or the scalar splitting
   O(-8)+O(-10); the latter cannot map into A because A is absent from
   Sym8 W. Thus the kernel is W(-9).
3. The negative external row is supplied only by the original O(-8),
   whereas differentiation inside the actual constant A can reach only
   the captured high line. This forces the kernel's original scalar
   component to vanish. Quotienting A therefore leaves the original
   scalar separated, rather than assuming an arbitrary horizontal split.
4. The low target pullback is an actual extension of O(2) by O(-10).
   Its equivariant Ext1 is Sym10(W)^G=0; Hom(O(2),O(-10))=0 gives a
   unique equivariant split. The remaining E0 has degrees in [-4,0],
   so it cannot map to O(-10). This proves the complete standalone
   external derivative is O(2), including the internal-scalar issue.
5. Cohomology bounds give five possible constant budgets. A degree-1
   summand would have zero external and internal derivative and hence be
   preserved and constant, which is impossible. The degree-2 coefficient
   map must inject into irreducible D, again by the preserved-negative
   subbundle contradiction. The resulting character equations leave
   precisely three residual bundles, not a guessed numerical shortlist.
6. With constant V+P the original D(-2) lies in the constants, contradicting
   PR913's nonzero low D row. With constant P, the original Wp(-3) is
   trapped as the entire residual Wp(-3); its external and internal
   derivatives vanish. With constant V, the unique triangular graph of
   T(-3) kills its low row, and its internal derivative to D(-4) vanishes
   by degree. The latter two are forbidden preserved negative bundles.

Conclusion: the exact source exclusion follows under the pinned actual
setup. No flaw found in the quotient/extension or the three final cases.
The new step beyond PR913 is the complete treatment of its nonzero-low-D
branch. No high-only hypothesis is silently restored. The separate c-d-f
source is not addressed, and the same tuple under source2 is not excluded.

## New append-only integration artifact

The new artifact is `frontier-source-through917.json`, SHA256
`486c673e7ddb1c0b427f4a819abd1b4854d775d1bbc1a90a3859574cd6995496`.
It removes an explicitly listed set of32 `(E_id, quotient_id)` pairs from
source127, not a count-only proxy. The preceding911 snapshot remains
unchanged at146. The new relation contains114 pairs and3 labels.

The new24 tests include exact disjoint union, preservation of the c-d-f
pairs, preservation of the same tuple under source2, wrong endpoints,
wrong tuple, missing proof scope, ambiguous source definitions, duplicate
labels/pairs, fabricated pair IDs, and repeat-application rejection.
Review supports verification; the new deliverable is the reproducible
source-aware integration code, exact relation artifact, and tests.
