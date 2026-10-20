# Lean checking environment

Pinned release: Lean 4.19.0, x86_64 Linux, release commit 6caaee842e94.
Source: https://github.com/leanprover/lean4/releases/download/v4.19.0/lean-4.19.0-linux.tar.zst
Downloaded over HTTPS directly from official leanprover/lean4 GitHub release, following GitHub's release-asset redirect. No third-party mirror, installer script, or repository code used.
Archive SHA-256 (recorded after download, not independently publisher-authenticated): 6fe3ce97a58f44e2b3567d455b994eacec5bfe9ae7774f2a573444480ba813fe
Extracted with system tar --zstd into workspace toolchain directory.

Executable: ${ARTIFACT_ROOT}/lean-koszul/toolchain/lean-4.19.0-linux/bin/lean
Environment: source ${ARTIFACT_ROOT}/lean-koszul/env.sh
Lake: 5.0.0-6caaee8, bundled with Lean 4.19.0.
Initial validation dependencies: bundled Lean/Std only. The later Mathlib extension is recorded below.

Validation: `lean --version` returned pinned version/commit. `lean EnvironmentSmokeTest.lean` returned exit code 0 on 2026-10-18. This tests Std import and omega on a generic natural-number inequality only, and is not evidence that any Koszul theorem compiled.

No user computer was used. Installation is confined to ${ARTIFACT_ROOT}/lean-koszul/toolchain. No HM source/model/rank/polynomial-instance/point/jet/residual/Massey-value computations were performed.

## Mathlib extension

Added official mathlib4 tag v4.19.0 from https://github.com/leanprover-community/mathlib4.git at commit c44e0c8ee63ca166450922a373c7409c5d26b00b. Bundled lake-manifest.json pins all transitive repository revisions. Built the official Cache executable from that source. Its standard leantar 0.1.15 helper is fetched by the mathlib cache utility from https://github.com/digama0/leangz/releases/download/v0.1.15/leantar-v0.1.15-x86_64-unknown-linux-musl.tar.gz. Cache files are confined to ${ARTIFACT_ROOT}/lean-koszul/cache via MATHLIB_CACHE_DIR. Cache availability is separate from user theorem compilation.

For mathlib-dependent modules use `./check-lean.sh /absolute/path/to/File.lean`. This runs pinned Lake's `lake env lean` inside the mathlib checkout.

Mathlib cache completed: 1338 files in first batch, 2 additional files for RankNullity, all downloads successful. MathlibSmokeTest.lean imports Quotient.Basic, Dimension.Finrank, FiniteDimensional.Basic, Dimension.RankNullity and resolves Submodule.finrank_quotient_add_finrank and LinearMap.range; compiled exit code 0 on 2026-10-18. This confirms requested library interfaces are available, not that downstream proofs pass.
