# Independent review: equivariant pencil commutant

**PASS** for the final source and separate imported-module axiom check.
The reviewer inspected all mathematical statements, exact source repair,
copied dependency artifacts, and completed root-run evidence. No compiler was
rerun by the reviewer. Comparator and an independent second kernel were not run.

## Exact files and source correspondence

All digests are SHA-256; paths and receipt names are portable logical names.

| Artifact | Digest |
| --- | --- |
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/PencilCommutantEquivariant.lean` | `5d600bdb6b31365e19e9fa4f9731873df33858792eaf0bb7e905af524ba77f56` |
| Unchanged `Check.lean` | `559245925d001216dbba891d59513381302c7976409746c063005385c5e59079` |
| Compiled `PencilCommutantEquivariant.olean` | `4cdf4e97930a94925c1508bf4e4ca6ad154681d67158cab445b971856c3123e7` |
| Compiled `PencilCommutantEquivariant.olean.private` | `930ddbbda6b762c8e9013f2f1b9df1524e30505ac4bf2b65db826a6c3114219f` |
| Independent static review | `84b050502c6d3fc984daed6679e5f27fe31d7c4de04480b37571fd4276679c76` |
| Historical producer `SCOPE.md` | `fe53010a15ec9905793b1b2aee83ec2d909ba27f4404888820a4f78e68de1ecc` |
| I dependency source | `71ed8339d4ffa55cbc0a6d22e488cd1f0e411a065ede0eb938e365a30443eeda` |
| PR808 written proof | `316ef592bc74f29de4698e740b90ad760ef7ad6cc09777ae3d913fc69043a5d2` |

The dependency is PR879 commit `634ca192ab8f64cf3d779a9194382e1458cdad7a`,
`lean/OAI/AlgebraicGeometry/HorrocksMumford/PencilCommutant.lean`.
Its source matches the previously reviewed and published I bytes.
The written source is PR808 commit
`3c2d80d5bbae109f810b1919fb0adbc2a1d0e392`, section 2, equation (4),
`research/hm/source2-commutant-gate/PROOF.md`. Its earlier independent I
review authenticated Git blob `cd5adb3b98fc3df08154d2cb7dbd578e125f187f`.
This review checked the pinned local text and planning reports; it did not
perform a fresh network authentication.

The reconnaissance and independent design reports have digests
`29365ee3871a2ddb6c664ca6564690948eb62e576c80427132ed362277af23d9`
and `055ac6a0c2568a7e12784ed5bf4fc01732d003f453aa7cbc03cf01b25444e1b1`.
The implementation preserves their distinction between I's unrestricted
linear defect and the equivariant domain/target of equation (4).

## Mathematical audit

The four actions are genuine monoid homomorphisms into linear endomorphisms.
`tensorAction` constructs the diagonal action with its unit and multiplication
laws. Endomorphism multiplication is composition in the same order as
`TensorProduct.map_mul`; no inverse or commutativity of G is used.
`equivariantHom` is a linear submodule whose full intertwining condition holds
for every monoid element. Its zero/add/scalar closure uses R-linearity, not
commutativity of the endomorphism ring.

The domain includes the three vertex commutants in I's product order
`(X2,(X3,X4))`; the target includes both tensor Hom channels with the full
diagonal actions on `W ⊗ M2` and `W ⊗ M3`. Neither submodule depends on the
pencil maps. The action on W is retained, even though I's defect fixes that
factor by `id_W`. The unknown triple can be zero, singular, or any other
equivariant endomorphism triple; no unit or isotypic-scalar restriction occurs.

The channel lemma proves that
`y.comp a - a.comp (TensorProduct.map id x)` is equivariant from three explicit
hypotheses: equivariance of `a`, commutation of `x` with the source action, and
commutation of `y` with the target action. On each pure tensor, it moves both
actions through `a`, uses both vertex commutations, and distributes the target
action over subtraction. `TensorProduct.ext'` extends equality on every pure
tensor to the full linear map. Applying it to alpha and beta retains both
channels and both tensor-equivariance hypotheses.

`pencilDeltaEquivariant` uses `LinearMap.restrict` on I's existing defect,
with both source and target genuine submodule types. Its application theorem
recovers the ambient defect exactly. Its intrinsic kernel is the comap of the
generic commutant along the domain inclusion, a submodule of the restricted
domain. For an input already in that subtype, its membership property supplies
equivariance. For an ambient input, mapping the kernel through the inclusion
requires both generic commutant membership and equivariance of all three
components. `map_comap_subtype` gives the intersection in the correct order.

The final pure-tensor statement retains both pencil equations for every W
input and every appropriate vertex input, together with three equivariance
equations for every monoid element and every vertex input. No generating-set,
basis, single-element, or one-direction reduction is introduced.

All twelve explicit theorem statements were inspected. The only direct public
import is I; its public tensor and kernel imports provide the required APIs.
The pinned definitions of `TensorProduct.map_mul`, `map_tmul`, `ext'`,
`LinearMap.restrict`, `ker_restrict`, and `Submodule.map_comap_subtype` agree
with their use. The source retains module mode, public declarations, and
disabled auto-implicit variables. No unfinished proof, custom axiom, unsafe
declaration, or native decision procedure occurs.

## Exact repair and retained failure history

The original source digest was
`976ee0122eee5d087da6b89f05234e7137dc973b6151f0f9dd137e91f8b2e2e5`.
The final source adds exactly `include hAlpha hBeta in` before the
documentation comment of `pencilDelta_mem_equivariantTarget`. Removing that
line reproduces the original bytes. The line explicitly retains both intended
section hypotheses; Lean does not infer theorem parameters from their use
only in its proof. The restricted map and downstream declarations consequently
retain these proofs as arguments. No formula, proof body, definition, or Check
file changed, and no assumption was weakened. Original producer files and
the static review remain preserved.

Three unsuccessful attempts are retained distinctly:

| Attempt | Status and cause | Original receipt SHA-256 |
| --- | --- | --- |
| `compile-0001` | Child exit 1: omitted hAlpha/hBeta parameters, then cascading application errors | `ef6f6b633855e42b6ca408fed780271dcace4b3134dfda432b82696dc290067d` |
| `compile-0002` | Child exit 1: `include` placed after the documentation comment, causing a parser error | `f23aa7c86c2f02bf3053a1797d15182aca5a1310e070deedc93ed8c471f13527` |
| `axioms-0001` | `invalid_configuration`: missing compiled K module; no child launched and no Lean axiom check ran | `72181bbd395c7c213dfb63ff8f27ced84ca6b8e84e1456509a6f6e8ae31f5beb` |

The first two stdout digests are respectively
`9e8430ad495bf471fed7277abb0d36477f964692d0a88b92420e641c2e6c7a03`
and `722f04801ceedcc60b87c4bb3adc57099d3f05133ee1e658771482b4413cfad3`.
The rejected prelaunch import has no child output files. None of these
attempts is counted as successful verification.

## Dependency artifacts and successful evidence

All five I artifacts copied into K's build root are byte-identical to the
already reviewed I build:

| Artifact | SHA-256 |
| --- | --- |
| `PencilCommutant.olean` | `c99cacbe534c89b7fce52cb41a220210f872c2cf372c3d118498c0bb8c137b8f` |
| `.olean.private` | `a1b4f9ca66ce578d27d54804f8afd9790ac3db37aa487d3ca94fd31570606183` |
| `.olean.server` | `249297ce90b2418aa883ba2d5cbb8be60889381eb108f2b46d40afa0192fb644` |
| `.ir` | `1d9312bf7090d927adbcfb2b1a5c2b5bef748d60b19b76573988ed2dff5560ff` |
| `.ir.sig` | `c3bc06acd2d342c166729b3171443e8bb2f074af7a9b686b450a190e81b3f915` |

The final compile receipt records I's `.olean` and `.olean.private`; the
import receipt records its `.olean`. The other three copies were independently
compared after the runs. The reviewer also recomputed the digests and sizes
of every recorded input in both final receipts.

The environment is Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The inspected launcher
`run-module.py`, digest
`ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`,
selects the pinned compiler/search path and passes `-j1 -M1200`.

| Successful run | Exit | CPU seconds | Wall seconds | Sampled group peak RSS, bytes |
| --- | ---: | ---: | ---: | ---: |
| `compile-0003` | 0 | 2.506922 | 4.154551 | 895647744 |
| `axioms-0002` | 0 | 0.931055 | 1.003842958 | 840941568 |

The original receipt digests are respectively
`0b7ad9aac7b41821193c2ccfc5589ada42c6a26015165b6b40c9762e9be14185`
and `92deeec415efa6cbd8395e860ebb47231c63f1b4699e35fb0b05db4c06ab31be`.
Both report success, unchanged recorded inputs, completed cleanup, and no
termination signals. The compile binds the repaired source and I artifacts;
the import binds the unchanged Check, the exact compiled K module, and I's
`.olean`. These receipts attest to listed inputs, not an exhaustive bundle of
every dependency binary.

The successful source compile emits exactly two nonblocking unused-bound-variable
warnings for `X` and `F` in the submodule scalar-closure definitions. Its stdout
digest is `b214524de30b9a98a2e955319ea366ffe20c658568c8c45ae7c69dc1bf7a4cfb`.
The import stdout digest is
`eb720f607440ea14173da76588bd657e21532621eab40f2326040b0a8aa65d3f`.
Both stderr files are empty, digest
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The final importing check reports 16 distinct names: 12 new K theorems plus
the four I dependency theorems. The five new names with closure exactly
`[propext, Quot.sound]` are:

- `tensorAction_apply`
- `mem_equivariantHom_iff`
- `mem_equivariantHom_iff_apply`
- `mem_pencilEquivariantDomain_iff`
- `mem_pencilEquivariantTarget_iff`

The seven new names with closure exactly
`[propext, Classical.choice, Quot.sound]` are:

- `tensorDefect_mem_equivariantHom`
- `pencilDelta_mem_equivariantTarget`
- `pencilDeltaEquivariant_apply`
- `ker_pencilDeltaEquivariant`
- `mem_ker_pencilDeltaEquivariant_iff`
- `mem_map_ker_pencilDeltaEquivariant_iff`
- `mem_map_ker_pencilDeltaEquivariant_iff_tmul`

All names are in `OAI.HorrocksMumford`. The four dependency checks
`mem_pencilCommutant_iff`, `mem_pencilCommutant_iff_tmul`, `pencilIdentity_mem`,
and `pencilCompose_mem` each have closure `[propext, Quot.sound]`. They are
not counted as new exported K theorems. The check prints axiom closures, not
full theorem types; source inspection and successful compilation establish
the reviewed statements and exported name accessibility.

The guard limits remain 60 CPU seconds per process, 75 wall seconds, and
1610612736 bytes sampled aggregate RSS at 0.1-second intervals. No cap was
raised. Sampled RSS is not a hard Darwin address-space limit or a guaranteed
between-sample overshoot bound. This review inspected the root's compiler
evidence; it is not a new compiler or second-kernel run.

## Application boundary

This proves a conditional equivariant restriction and its kernel
characterization. Actual HM actions, original tensors, their equivariance
proofs, action conventions, and geometric identifications remain application
inputs. It establishes no dimensions 113/153, numerical rank, Schur
decomposition, trace-radical classification, actual family membership,
source2 exclusion, or repaired main theorem.
