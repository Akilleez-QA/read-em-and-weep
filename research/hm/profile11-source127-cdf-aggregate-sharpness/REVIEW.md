# Independent review of the quotient-support criterion and aggregate sharpness

Date: 2026-10-23.

## Verdict and exact scope

**PASS for the stated conditional aggregate-interface theorem.** I found no mathematical gap in the complete proof. The quotient-support criterion, both one-row criteria, and the three formal aggregate constructions are correct for the fixed represented negative pencil specified in the proof.

This verdict is not an actual-HM realization, a positive-linear factorization theorem, a full-window or full-module extension theorem, or an exclusion. It does not certify an unperformed actual-source calculation or change any source, label, pair, frontier, or rank bound. The limitation result is relative to the explicitly listed aggregate interface, not to all known or possible facts about the actual module.

I read the entire proposed proof, its complete checker and reproduction note, and all four immediate proof inputs in full. I independently authenticated the four inputs through the repository connector, both as original Git blobs and as files at the specified immutable commit/path pairs. I did not rely solely on the supplied manifest or on a previous checker's report. This is an audit of the new proof and its immediate imported interfaces, not a claim to have recursively re-proved every theorem cited by those four inputs.

## 1. Exact byte binding and source authentication

The verdict binds the following SHA-256 digests:

| Artifact | SHA-256 |
|---|---|
| `PROOF.md` | `30036ea1ac038e023ff3f147eb104c48585bf741adb19cb3b90022604df80a9b` |
| `verify.py` | `505e4f71fdbfc5041d753647544f2a64be8575cb0b559686fbac45fad950c064` |
| `REPRODUCE.md` | `c4939c03a919504f26a83065472ccb1b517f520fe944359cde0eb6638e6d3e8a` |
| `audit-inputs/manifest.json` | `2acb3c9824b1c5222aacecbe265abb5ab006a00fa247be3428d027ee7ad364c8` |

All repository sources below belong to `Akilleez-QA/read-em-and-weep`.

1. `ALGEBRA.md`: commit `c6c25eaf0e5a67c27eee7c3ba4f000df55997692`, path `research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md`, Git blob `83f5aee293995257459229e6b323522224ce8f3d`, 18,095 bytes, SHA-256 `0d740d6f70de924b0442af71cb37e050165efbe9ab984a76f0e1e40b5d27a599`.
2. `NEGATIVE-SQUARE.md`: commit `3d9e1f3949241a6b2bbb48781c056b72b7262dd7`, path `research/hm/profile11-source127-cdf-negative-square/PROOF.md`, Git blob `bdcb7d5b14f7477bcd616e0e682fa5f45e250a5d`, 9,019 bytes, SHA-256 `c52e1e13f81d891a8dc835b37ec47b225e64882a79c9ba4a462d09dc9c43f058`.
3. `FULL-MODULE.md`: commit `f4a73af666900ad2cb34a756d24b88e19dd6feaa`, path `research/hm/negative-truncation-extension/PROOF.md`, Git blob `2ba0a7eee6ef2eb5413683e85618d7902dca3970`, 16,647 bytes, SHA-256 `7525df1e58ac8683a5a0b828209f4f35cc79a09527307ee47b35025d5c2ad636`.
4. `ACTUAL.md`: commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, path `research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`, 9,672 bytes, SHA-256 `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.

For each source, the connector's original blob content was converted to its UTF-8 bytes, the Git object digest was independently recomputed as SHA-1 of `blob <byte-length>\0` followed by those bytes, and the resulting bytes were compared exactly with the local audit input. The connector's separate immutable commit/path fetch returned the same blob SHA and the identical content. All four checks passed. The frozen proposal hashes also matched before and after the audit.

## 2. Imported interface is sufficient and correctly typed

PR924 supplies the entire covariantly represented fixed-variable commutant, not merely its units, a character-level candidate, or the opposite algebra. Its Section 4 authenticates simultaneous reconstruction of both actual negative arrows; Sections 2-3 include singular endomorphisms and rightmost-first multiplication. Section 6 gives the exact two source blocks, three target blocks, zero radical action on `N2`, and the nonzero radical map from the quotient's `P` to the `P` inside the `F` target. This is precisely the represented information used here.

PR926 identifies the actual negative-square map as the boundary following ordinary symmetric multiplication. It proves its image is the entire `F+B` target, its intrinsic quotient is `Pi=V+P`, and its restricted kernel has dimension 93. Its Section 5 imports the actual generation theorem and proves quotient surjectivity of the actual aggregate positive map. The proposed proof does not infer the negative-square image or an embedding merely by subtracting characters.

PR818 supplies the actual coordinate parity decomposition and grading `N2=K3^+`, `N3=K4^-`, `N4=K5^+`. Its distinctions between aggregate compatibility, a five-variable window, marked submodule extension, and full-module lifting are maintained. No source2-specific commutant or filtration dimensions are imported into this c-d-f argument.

The original actual-equivariant-splitting note supplies the binary-icosahedral representation conventions and self-duality. Together with the fixed complete character check, these justify the center-even dimension list used for `T_+`. No unproved identification of the actual positive three-space with one particular irreducible is needed.

The normal-form complement `Y_L` is used only as a chosen equivariant section of the intrinsic quotient. The proof consistently distinguishes `Pi=N4/im(q_-)` from that noncanonical complement.

## 3. Faithful source restriction and algebra classification

Every element of `C_N` intertwines `q_-`: this follows by composing its two negative-arrow equations and using the symmetric product. If a compatible element has `e2=0`, its `e4` annihilates both `im(q)` and `im(q_-)`. Aggregate generation makes their sum all of `N4`, so `e4=0`.

The two nonzero source blocks then give `a=b=0`. The target action gives `d=0`, and injectivity of `w -> eta_w` gives `w=0`. This proves faithfulness of source restriction without dividing by any scalar or assuming invertibility.

I independently checked the commutator identity

    Theta_q(ef) = e4 Theta_q(f) + Theta_q(e)(1 tensor f2).

It proves closure under multiplication, while linearity and the identity element give a unital complex subalgebra. Its source restriction is an injective algebra map to `C^2` with the scalar diagonal in its image. A complex linear subalgebra containing that diagonal has dimension one or two; in the latter case it is all of `C^2`. This justifies the scalar/`C^2` dichotomy without a semisimplicity assumption about the ambient triangular algebra.

In the nonscalar case, the unique preimage of `(0,1)` is an idempotent by injectivity. Substituting into the authenticated multiplication gives `d^2=d` and `dw=w`. Its possibilities are exactly `(0,1,0,0)` and `(0,1,1,w)`. All singular cases are included.

## 4. Independent full component calculation

With subscripts denoting target followed by source, the six components of `Theta_q(a,b,d,w)=0` are exactly

    F/F: eta_w chi_F = 0,
    F/B: (a-b) Q_FB + eta_w chi_B = 0,
    B/F: (b-a) Q_BF = 0,
    B/B: 0 = 0,
    L/F: (d-a) chi_F = 0,
    L/B: (d-b) chi_B = 0.

This calculation checks the shear direction and both cross-component signs. In particular the diagonal `F/F` term is not identically absent: its radical contribution is retained.

If both quotient rows are nonzero, the last two equations force `a=b=d`. Subtracting that scalar identity produces a compatible zero-source element, which vanishes by the previous section. The claimed scalarness follows. Neither row has to be onto for this argument.

For `(0,1,0,0)`, the six equations reduce precisely to `chi_B=0`, `Q_FB=0`, and `Q_BF=0`.

For `(0,1,1,w)`, the `L/F` equation first forces `chi_F=0`, so the `F/F` radical equation then vanishes for a proved reason. The remaining conditions are exactly `Q_BF=0` and `Q_FB=eta_w chi_B`. The diagonal components of `q` impose no additional condition.

Surjectivity of `chi` excludes simultaneous vanishing of both quotient rows. When one vanishes, the other is onto, so the incompatible idempotent type is excluded. In the `chi_F=0` case, surjectivity of `chi_B` and injectivity of `w -> eta_w` prove uniqueness of `w` in the cross-component equation. The indicated set of possible cross maps is genuinely a one-dimensional linear subspace, including zero.

These checks establish both necessity and sufficiency: necessity follows from the unique idempotent in any nonscalar algebra, and sufficiency follows from the explicitly compatible nontrivial idempotent. No assumption about actual positive-linear factors or a window lift enters either direction.

## 5. Invariant functional and three constructions

Over `C`, semisimplicity and the complete center-even irreducible dimension list imply that a center-even representation of dimension three is `A`, `V`, or `1^3`. There are no even two-dimensional constituents or additional one-dimensional characters to create another possibility.

For an irreducible self-dual three-space, an invariant bilinear form is nondegenerate. By Schur's lemma, its transpose is a scalar multiple of it; transposing twice forces that scalar to be `+1` or `-1`. The latter would be a nondegenerate alternating form on an odd-dimensional space, which is impossible in characteristic zero. The form is therefore symmetric and descends to a nonzero invariant functional on `Sym^2(T_+)`. The trivial case is immediate. This supplies the needed `epsilon` without assuming the actual type of `T_+` or selecting an actual coordinate quadratic.

Both source characters contain genuine `V` and `P` summands. Semisimplicity therefore supplies equivariant surjections `r_F` and `r_B` onto `Pi`. A chosen normal-form section supplies `i_L`. Each displayed construction is linear, equivariant, and well-defined on the symmetric-square domain.

Since a nonzero linear functional to `C` is onto, each surviving row `epsilon tensor r_X` is onto `Pi`. Each constructed map has image precisely `i_L(Pi)`, so its image plus the unchanged negative-square image is exactly `N4`. In the two-row construction both quotient rows are nonzero; in the other two constructions exactly the named row survives. All cross-target components vanish.

The decision criterion consequently gives exactly:

- `q^both`: the scalar algebra;
- `q^F`: `C^2`, with the unique source-`(0,1)` idempotent `(0,1,0,0)`;
- `q^B`: `C^2`, with the unique source-`(0,1)` idempotent `(0,1,1,0)`.

For the last construction, the only possible shear is zero because `chi_B` is onto and `eta` is injective. For each construction, composition of its surjective quotient map with any nonzero radical map is onto the target `P`. Thus the radical obstruction and the scalar-target/quotient projected surjectivity are preserved, rather than evaded by killing the relevant channel.

The negative arrows, `q_-`, its actual restricted kernel embedding, its image, and its intrinsic quotient are all held fixed. Only the additional formal aggregate positive map varies. The proof does not assert that any unmodeled actual positive or Euler relation embedding is held fixed.

## 6. Conditional nonimplication and nonvacuity boundary

The construction is a statement over every fixed negative pencil satisfying the displayed hypotheses. Conditional on such a pencil being given, its aggregate extension space contains all three specified alternatives. This is enough for the stated relative, aggregate-interface limitation: within that fixed-pencilled interface, aggregate generation and projected surjectivity do not choose the algebra or force two-sided quotient support.

It is not an assertion that an actual HM c-d-f occurrence exists. Nor is it an unconditional counterexample satisfying every actual-HM hypothesis. The proof's repeated fixed-pencil and formal-aggregate qualifications are essential and adequate. An additional nonemptiness theorem for the actual-HM fiber is neither used nor established. No PR876 existence dependency is needed for this conditional theorem; such a dependency would become necessary only for a different assertion of nonempty realized examples.

The omission of positive-linear factors, mixed window squares, the degree-zero cover, and actual Euler/relation embeddings is explicit. Those extra structures may determine the actual answer. Likewise a nonscalar aggregate-compatible idempotent need not extend to a full-module projector. The proof does not combine aggregate compatibility with full-module scalar rigidity to manufacture an exclusion.

## 7. Checker, reproduction, and permitted computation

I inspected the complete checker before running it. It uses only the Python standard library, authenticates the four expected blob hashes independently of the manifest, and performs fixed exact arithmetic in `Q(sqrt(5))`. It contains no selected actual parameter, coefficient, derivative, matrix, actual-instance rank test, large search, or external mutation.

I ran both commands independently:

    python3 verify.py
    python3 -O verify.py

Both exited successfully and printed the stated PASS lines. The substantive checks use explicit exceptions through `require`, so optimization does not remove them.

I also checked the fixed character identity `P=Sym^8(W)-Sym^4(W)`. This expresses the hardcoded `P` row as a virtual character of the authenticated defining representation. Together with the checked orthogonality and positive degrees, it confirms that the norm-one rows are genuine irreducibles, not merely an orthonormal numerical table. The dimension-square sum and central parity then support the claimed completeness and center-even list. This was another small abstract character check, not an actual-source evaluation.

The checker does not by itself prove covariance, bilinear-form symmetry, algebra faithfulness, the six component equations, necessity/sufficiency, or the formal constructions. Those arguments were independently audited above. The reproduction note accurately separates these roles and provides an exact-object retrieval procedure. The four original source files need not be duplicated in the focused publication because the manifest and reproduction procedure identify their immutable bytes.

## Final assessment

The new contribution is a complete exact decision criterion for the aggregate-compatible algebra, together with uniform formal constructions proving that the stated aggregate information cannot resolve its alternatives over a fixed admissible negative pencil. The actual quotient-support/factorization question remains open. All reviewed frozen files were left unchanged.
