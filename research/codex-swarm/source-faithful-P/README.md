# PB01 source-faithful P binding

`p_binding.py` binds the exact reviewed INS153-node constructor and physical Catalog to the actual CLR/PH finite and homogeneous whole-source P for both pairs. Its coefficient-free proof covers primitive clearing including auxiliary v0, ordered matrix operations, elementary substitution before differentiation, source ordering, and exact owner-dependent homogeneous degrees. It supplies the P-side identity required by the later source-domain application; it does not accept an arbitrary callback as P.

Public API:

```python
from p_binding import ActualPBinding, FullOwner
binding = ActualPBinding(repo=None)  # repo only; no catalog/callback/mode
certificate = binding.describe(ordered_owners, pair=(0,1))
degree = binding.degree_upper(ordered_owners, pair=(0,1))
program = binding.symbolic_program_definition(pair=(2,3))
pins = binding.source_pins()
```

Owners are INS `FullOwner` instances in strict increasing source order, with one seed and distinct occurrences. The auxiliary carrier is5 and sorts first. Representation charts do not reassign owner tags. F34 is the raw target formula with axes renamed and slots unchanged; no inverse-image sorting identity is asserted. Metadata returns are fresh copies, not arbitrary user proof assertions or physical execution capabilities.

`coefficient` and `alternating_coefficient` always raise `PhysicalAdmissionMissing`, including malformed and apparent out-of-support requests. ActualCatalog polynomials are never constructed, differentiated or evaluated. The constructor reads/authenticates source bytes and inspects only shapes, denominator literals and exponent metadata. The accepted physical contraction/frame premises are explicit in `PROOF.md`; their historic physical checkers are not rerun.

Seven bounded controls pass in ordinary and optimized modes. They use artificial polynomial catalogs and independent direct matrix calculations, malformed byte controls and metadata-only actual construction:

```
python -B research/codex-swarm/source-faithful-P/test_binding.py -v
python -BO research/codex-swarm/source-faithful-P/test_binding.py -v
```

The first development run corrected one test's expected mixed-mask degree from203 to201; the owner-specific implementation formula was unchanged. No physical source coefficients, scans or actual fibers were evaluated. Tests stay below existing generic Ring caps and do not create a physical budget.

`source-pins.json` binds PR86 baseline7d73d540981a3a152d807c39844ec63bc9913b89 and inherited source revisions. `contract.json` describes the consumer API. `producer-ready.json` hashes producer files only and grants no admission. Reserved independent reviewer files are `test_independent.py` and `review-independent.md`.
