# Independent final review: source-family multiplier

**PASS** for the final source and separate imported-module axiom check.
The reviewer inspected all four statements, their proof arguments, pinned
library APIs, exact source changes and completed root-run evidence. No
compilation was rerun by the reviewer. Comparator and a second independent
kernel were not run.

## Exact correspondence

All digests are SHA256. Paths and attempt names below are portable logical
names; the original machine-specific receipts are retained in the run archive.

| Artifact | Digest |
|---|---|
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/SourceFamilyMultiplier.lean` | `3debef659b6085e55da8701490c05fde148f21a88961c48d5b7ff89a233a3be6` |
| `Check.lean` | `861b1010a93714269b95c160629048d924571b8f222b9130232a0e3620119b2e` |
| `SourceFamilyMultiplier.olean` | `a6a44aea78ec8cfb3fa54cca34b80b76e076d542e9e8d441ed67af9e0fe4c1c6` |
| `SourceFamilyMultiplier.olean.private` | `b4afa286fa803c2b9b9d966fce01ac92eb33cae7ac7189913b9fe771f96bafcd` |
| Independent static review | `7fa517b9ee8a1c1c049d8c1bd4abadf58e298b37518b2d16350f3850d91c1100` |
| Historical renamed `SCOPE.md` | `d29f14f6179fd1e9b3003fdd1b37e10b43dbb210724cf88d71bc04af9817375c` |
| PR889 written proof | `cf85d577d57f3b08369045b99599738498f0caf1fc0e45009a6d2bf227c95b22` |

The written source is PR889 commit
`72ac7ecc5447415fa8452f12ed6ec16921a600f4`,
`research/hm/physical-normalization-symmetry/PROOF.md`, Section 5/S10.
This review uses the pinned local packet and null's symbolic handoff; it
does not reauthenticate all of that written proof's geometric dependencies.
The independent Lean handoff has digest
`7cfeb5e775ea48b566bc251d4dc033e975af05c0d7da899ad3584ff070fe10b7`.

## Mathematical and API review

`BinaryForm k n` is mathlib's actual homogeneous-polynomial submodule, used
as a type through its sort coercion. The field assumption supplies a genuine
integral domain of binary polynomials. The definition uses
`QuadraticMap.linMulLin` on the quartic subtype inclusion and the degree-twelve
inclusion composed with L. Thus its h-dependence is quadratic and its value
is the actual product h*L(h), not an unspecified observation map.

The four declarations were inspected separately:

1. The evaluation formula is definitional. It is counted as one helper
   declaration, not an independent mathematical advance.
2. The homogeneous-degree theorem uses the two subtype certificates and
   `MvPolynomial.IsHomogeneous.mul`, with 4+12=16. It allows zero output;
   homogeneous membership does not assert nonzero exact total degree.
3. Injectivity uses equality of quadratic maps at arbitrary h. At h=0 both
   linear maps vanish. Otherwise subtype injectivity makes the underlying
   polynomial h nonzero, and `mul_left_cancel₀` gives equality of trace
   polynomials. Subtype and linear-map extensionality finish the proof.
   The varying h is retained, with no assumed injectivity or division by h.
4. Weighted injectivity proves `-(c^3) ≠ 0` from the explicit hypothesis
   `c ≠ 0`, applies its inverse scalar, and invokes the preceding theorem.
   This is legitimate field scalar cancellation; it gives no conclusion
   from the zero-weight observation.

This is four checked declarations: one evaluation formula plus three results.
The two direct public imports are
`Mathlib.RingTheory.MvPolynomial.Homogeneous` and
`Mathlib.LinearAlgebra.QuadraticForm.Basic`. Their relevant definitions were
read at mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. No OAI module
is imported or needed. Module mode, public declarations and disabled
auto-implicit variables are retained. No unfinished proof, custom axiom,
unsafe declaration, native decision procedure or trust override occurs.

The polynomial-valued QuadraticMap target plus its degree-sixteen theorem
is a valid focused realization of the multiplier interface. No separately
constructed symmetric-square Hom identification, polarization formula or
coefficient left inverse is claimed. The field statements themselves do
not require characteristic zero; the surrounding geometric application
retains its original complex hypotheses.

## Exact changes and retained failed attempt

The original source digest was
`d3b7d8fa6fa90ec17e5697dd0cff5ba75b85cc697a047731e178494796377f6a`,
with Check digest
`2d2d8b92711d12e9911c92f20c0f2fa460964daa0d84e9081468aef0a9ef6dc0`
and SCOPE digest
`a66a26b19abc0ecd03a6e9f232ca38ed241bd1bd846379b168e38fbd3f784c56`.
All three originals are preserved.

Root first renamed the generic J identifiers to descriptive
sourceFamilyObservation identifiers, producing source digest
`9a67ab3e5c95b2abd9d143fada5306a6b13ef969dd166862ce44a5cda894c0f6`.
`compile-0001` exited 1 with one `lean.dependsOnNoncomputable` diagnostic:
the observation definition depends on the noncomputable polynomial algebra
instance `AddMonoidAlgebra.nonUnitalNonAssocSemiring`. Its original receipt
digest is `e6528a9bb56a49781a98ddc3f1bb988f8a56ad294abf05a27b37881146a10d36`;
stdout digest is
`57834565cd1ef7c41b8ff6da9fc7528ee754d13b98856afb79ee6e1ec71cac0e`.
The exact failed source and receipt are retained and are not counted as a
successful verification.

The final repair adds only `noncomputable` before the observation definition.
It changes code-generation status, not formulas, hypotheses, proof steps or
kernel checking obligations. Independently removing that keyword and
reversing the identifier substitution reproduces the original source hash;
reversing the names in Check and SCOPE reproduces their original hashes.
The historical SCOPE's UNCOMPILED language describes delivery, while this
final review records the later successful runs.

## Completed execution evidence

The inspected launcher chooses Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and the pinned mathlib search
path, with `-j1 -M1200`. The compiler binary digest is
`1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554`.
The launcher digest is
`ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`,
and its dependency-path file digest is
`7a93dfc6d5ce598755ad214d49792c947f3a8fdc4609e424266793e46715bdad`.

| Final run | Exit | CPU seconds | Wall seconds | Sampled group peak RSS, bytes |
|---|---:|---:|---:|---:|
| `compile-0002` | 0 | 2.275211 | 8.935431 | 1157267456 |
| `axioms-0001` | 0 | 1.599275 | 3.66392625 | 1151565824 |

Original receipt digests are respectively
`58b6f269423beeadab153c76a3a9564545a48d8ea69ee57c33def999614ebf32`
and `899a590099ca7b6303fc2bfbc97fa7a95acd664283b1536ea75c083bac423d06`.
Both report success, unchanged recorded inputs, completed cleanup and no
termination signals. Current hashes of the recorded inputs, launcher,
supervisor, source, Check and imported module artifacts were independently
recomputed and match. These receipts bind their listed inputs; they are
not an exhaustive hash inventory of every transitive dependency binary.

The source compile has empty stdout and stderr, so no final warnings were
emitted. Import stderr is also empty. Each empty stream has digest
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The importing check's complete 477-byte stdout has digest
`a6e23418cc3926fb00cffc430951b71d7732981900e0d1139e7c11aa71b2121a`.
It names exactly these four exports in namespace `OAI.HorrocksMumford`:

- `sourceFamilyObservation_apply`
- `sourceFamilyObservation_mem_homogeneous16`
- `sourceFamilyObservation_injective`
- `weighted_sourceFamilyObservation_injective`

Every closure is exactly `[propext, Classical.choice, Quot.sound]`; there
are no repeated dependency theorem checks. Check.lean prints axiom closures,
not full theorem types. Source inspection and successful compilation establish
the reviewed statements, and the importing check confirms accessibility of
their exported names.

The guard uses 60 CPU seconds per process, 75 wall seconds and 1,610,612,736
bytes sampled aggregate process-group RSS at 0.1-second intervals. No cap was
raised. RSS sampling is not a hard Darwin address-space limit and provides
no guaranteed between-sample overshoot bound. This review consumes root's
evidence; it is not another compiler run or an independent second kernel.

The repository replay instructions in README were checked against the pinned
`lean/lakefile.lean` and `lean/lean-toolchain` configuration but were not
separately executed. The recorded runs used the isolated layout documented
by their launcher and receipts.

## Scope of the result

The unit derives injectivity of the concrete h-dependent observation rather
than assuming a generic calibration certificate. It does not construct the
actual source family, G-action, positive representation identification,
cubic-a/linear-h equivariance certificate, prior global gluing, physical
extraction, corrected `S-qW` image membership or independent reference.
It proves no 10/12/13 dimension count, orbit separation, selected evaluation,
actual HM exclusion or repair of the original theorem. No actual source,
point, coefficient, tensor, matrix or instance rank was evaluated.
