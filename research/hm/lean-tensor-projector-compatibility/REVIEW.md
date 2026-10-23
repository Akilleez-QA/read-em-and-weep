# Independent review: tensor projector compatibility

**PASS** for the final source and separate imported-module axiom check. The
reviewer checked the mathematics, pinned APIs, exact source delta, dependency
copies, and completed root-run evidence. No additional compiler run was
performed. Comparator and an independent second kernel were not run.

## Exact files and dependency

All digests are SHA-256; paths and receipt names are portable logical names.

| Artifact | Digest |
| --- | --- |
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/TensorProjectorCompatibility.lean` | `eee485ec9987c5d63d0528987737fff4af8e0f01ef13df870ad3aed9eef579cf` |
| Final `Check.lean` | `600e45f9eab4ed7524480ee64c89bddac94d99e5bebfee4f0f8e3c41b4edc6d9` |
| Compiled `TensorProjectorCompatibility.olean` | `d65a5242b26b269dccb3e066065a8cad419b3332907abcb5ef0e0b7bcca359a7` |
| Compiled `TensorProjectorCompatibility.olean.private` | `c158ab411fc4d16484b3a5065ed2332fa6cc0d19d946561e893e632928515145` |
| Original static review | `22ad40106774bf089af73e675862ec0d898d1defcb83a689980472e310d128dc` |
| Historical producer `SCOPE.md` | `37f9d5ebd1c39fcd8367f9b163f73d6907f6800da2cfb15e28f45c30e8490840` |
| PR865 dependency source | `1bc07ce1ca444f822abc5a6c344d099475c9b6e45cc024ae2985878bb5b7ba32` |
| PR818 written input | `7525df1e58ac8683a5a0b828209f4f35cc79a09527307ee47b35025d5c2ad636` |

The imported dependency is
`OAI.AlgebraicGeometry.HorrocksMumford.QuadraticProjectorCompatibility` from
PR865 commit `80f241711bcd3a053268de6a83c8aee68403ebbf`. Its full local source
was independently matched to primary Git blob
`c86192dc79250cba0cfcd4f93d8d26e9a2d624ea`. The written motivation is PR818
commit `f4a73af666900ad2cb34a756d24b88e19dd6feaa`, section 5 of
`research/hm/negative-truncation-extension/PROOF.md`.

The dependency's five build artifacts copied into the tensor unit's build
root are byte-identical to the already-reviewed D build:

| Artifact | Digest |
| --- | --- |
| `QuadraticProjectorCompatibility.olean` | `e158122df3c4f2104061e5a322870d0817b549db632c22a4f356d55c8b2b001c` |
| `.olean.private` | `b84699da97057e25ce19cf4eedb1a25c378ecf50c5f9dfdee7d348c091487cd6` |
| `.olean.server` | `1f6cf8f1bc7cc409717adcefac492a0236e51663e05cadf250af6241aa8f197f` |
| `.ir` | `29beb2323ea10499ee45e44395e20a76508e25ba3b813fd9fcfd98eb790ceaa7` |
| `.ir.sig` | `cd07901ccbd9dcd31e7714797f7a5ecf097689297eb6a813b539eda64e34db25` |

The successful compile receipt records the dependency `.olean` and
`.olean.private`; the importing check records its `.olean`. The other three
copies were compared independently after the run. This is an exact dependency
reuse, not a duplicate source theorem or a new trust assumption.

## Mathematical and API review

Over a commutative ring, independent additive commutative group modules
`W`, `V`, and `N` have genuine tensor product `W ⊗[R] V`.
`tensorProjector p` is exactly `TensorProduct.map LinearMap.id p`.
On a pure tensor, its square is `w ⊗ p (p v)`, which equals `w ⊗ p v` using
the explicit hypothesis `p.comp p = p`. `TensorProduct.ext'` extends this
pointwise result to equality of linear maps; it requires neither flatness
nor injectivity of the pure-tensor map.

`tensorProjectorSlice q w` is `q.comp (TensorProduct.mk R W V w)`, so it is
the actual linear map `v ↦ q(w ⊗ v)`. Evaluating bundled intertwining on a
pure tensor gives the family condition. Conversely, the family condition
gives equality on all pure tensors, and `ext'` proves bundled equality by
spanning. No assertion that arbitrary tensors are pure is used. The slice
equivalence has no unnecessary idempotence hypothesis.

The final theorem directly instantiates D's
`quadraticProjectorCompatibility_iff_crossTerms` with domain `W ⊗[R] V`,
codomain `N`, domain projector `P = id ⊗ p`, and target projector `r`.
Both off-diagonal terms remain, with the correct composition orders:

```
(r.comp q).comp (LinearMap.id - P) = 0,
((LinearMap.id - r).comp q).comp P = 0.
```

The first theorem supplies idempotence of `P`; idempotence of `r` remains
explicit. No equality or vanishing required by an application is inferred.

The pinned mathlib APIs `TensorProduct.map`, `map_tmul`, `mk`, `mk_apply`, and
`ext'` were read directly in `TensorProduct/Map.lean`, `Defs.lean`, and
`Basic.lean`. The only direct imports are the tensor `Map` module and D.
The source uses module mode, public imports and an exposed public section,
with auto-implicit variables disabled. It contains no `sorry`, `admit`,
custom axiom, unsafe declaration, or native decision procedure.

## Final delta and preserved failures

The original static source digest was
`96914785d2b1935d01d90dff73d5264a7ffef507de18bbd88a59f74dcf8f436d`.
The final source removes the leading `UNCOMPILED` status word and replaces
one rewrite with an explicitly typed local equality:

```lean
have hpv : p (p v) = p v := LinearMap.congr_fun hp v
rw [hpv]
```

This is the same mathematical equality as before. The original direct
rewrite retained the presentation `(p.comp p) v`, which the rewrite tactic
did not match against the simplified goal `p (p v)`. The typed equality
resolves that elaboration detail. No theorem statement, assumption, import,
definition, or namespace changed. The pre-repair source is preserved with
digest `aae232683655f86790eed32d119a81b76b4ae9a1b401b833d3ff3d271ad089e9`.
The check changed only its leading status comment; its original digest was
`2f9685fb42ea0b212d6db4028961e9332a9fc50313b65c65e2fe626e7986a884`.

The first failed receipt, `compile-0001.json`, has digest
`0135a8c63b82be733af330ce5e79ee3f1b629c7d8e66633e57693a9272b29fe4`.
It stopped at dependency lookup under the selected tensor-unit namespace
root, before source diagnostics. The second, `compile-0002.json`, has digest
`0b209087bc787189895d8bba1ddbb4fd30ac94258bbb83c757904d92fdcaff23`.
It resolved the dependency and failed at the rewrite described above.
Their stdout digests are respectively
`b90be11e32a9f54e50caac2ad0e9e1305733a548388db38e44682599af685b5d`
and `4d9df81587956c89de3f4740415f0006deda9b941e77e39659f839298c835a5a`.
Both original receipts and outputs remain preserved; neither is reported as
a successful compilation.

## Completed verification

Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`, and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` were used. The final runs use the
same inspected launcher `run-module.py`, digest
`ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`,
which selects the pinned compiler and search path and passes `-j1 -M1200`.

| Final run | Exit | CPU seconds | Wall seconds | Sampled group peak RSS, bytes |
| --- | ---: | ---: | ---: | ---: |
| `compile-0003` | 0 | 1.09812 | 1.114415708 | 853295104 |
| `axioms-0001` | 0 | 1.437577 | 5.296535708 | 838729728 |

The raw receipt digests are respectively
`a6e38e76784de552e8ef8c41beb8977cdd2d89f575c6041d001f95f472aedfc6`
and `19825878279918df52b53e06316e2d85e79bda7bd6dd074d9fd8e3a7aac9ffc6`.
Both report success, unchanged recorded input hashes, completed cleanup, and
no termination signals. The reviewer recomputed all recorded input digests
and sizes. The compile binds the final source and D artifacts; the importing
check binds the final check and exact compiled tensor and D modules.

Compile stdout/stderr and check stderr are empty, digest
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The axiom output digest is
`8e4710d5841487915ee7d77714bb0c473752a8c4f0b14a189e973087a2f0277d`.
All three theorem names occur exactly once:

- `tensorProjector_idempotent`: `[propext, Quot.sound]`.
- `tensorProjectorCompatibility_iff_slices`: `[propext, Quot.sound]`.
- `tensorProjectorCompatibility_iff_crossTerms`:
  `[propext, Classical.choice, Quot.sound]`.

The guard limits remain 60 CPU seconds per process, 75 wall seconds, and
1610612736 bytes sampled aggregate RSS at 0.1-second intervals. No cap was
raised. This is not a hard Darwin address-space limit or a guaranteed
between-sample overshoot bound. These receipts attest to their listed inputs,
not an exhaustive bundle of every dependency binary. The reviewer inspected
the root's runs and did not run a separate compiler or second kernel.

## Application boundary

This proves the reusable tensor adapter and conditional cross-term test.
The modules, actual `q`, idempotents, and physical interpretation remain
application inputs. No symmetric-square action or actual positive quadratic
map is constructed, and neither cross term is shown to vanish for an actual
HM instance. No extension, lift, splitting, geometric descent, source2
exclusion, rank, or repaired main theorem follows from this unit alone.
