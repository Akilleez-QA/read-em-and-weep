# Constant P4 detector selection preflight

This new directory contains a constant-matrix runner only. Nothing evaluates the geometric residual, a source-polynomial circuit, the full harmonic oracle, or physical coefficients.

`extract_constants.js` authenticates blob `7adc1d6a733636204b1dd613870c168717be6277` at commit `f968b53943ba2312f09fbc3e8f9d462e86bcaa34`, evaluates exactly its prefix before `function rankExact(input,ncols){`, and checks the precise constructor suffix. Thus no original rank functions, driver or zigzag execute. It emits gamma, the three positive degree-two bases and five ordinary matrices. The global polynomial differential-square check in that prefix is elementary constant algebra.

Dimensions: E50x80, B1 400x245, C1 150x400, B0 1200x1225, C0 350x1200. Published ordinary nonzero counts are 100,680,500,3400,1500 respectively. Positive scalar cycles are built by the authenticated supertrace formula, not copied coefficients. Twenty exact integer cycle checks and all ordinary boundary/candidate cycle equations run before finite-field selection.

Selection uses sparse elimination modulo101. Pivot count240/848 is checked; 10/2 new independent columns give modular augmented rank250/850. A modular nonzero minor gives a rational lower bound. The separate source-pinned rational boundary ranks240/848 give the upper bounds needed to infer independence in the rational quotients. No characteristic3 statement is inferred. The twenty-class quotient premise is PR76 NOTE, explicitly not regenerated here.

Enforcing bounds:20million coefficient-update cap,500000-byte extraction output,2MiB final output; node heap64MiB; extraction subprocess10s. Outer supervisor must enforce60s wall and512MiB aggregate descendant RSS, kill the process group on cap, and emit a receipt. Sparse elimination worst stored field entries <=850*1200=1020000; Python dictionary overhead is runtime-measured and is not treated as zero. No claim that a successful run occurred until a receipt exists. Final output is written only inside this directory. No scratch/cache files; use python -B. No execution release follows from this preflight alone.

Certificate exposes source blob/prefix, ordered bases policy via pinned source, I20, exact20-cycle checks, candidate label triples/quadruples, boundary/augmented modular ranks, complete deterministic pivot log, matrix digests and physical-evaluation=false. An independent verifier must regenerate matrices/labels and verify the modular pivots or replay elimination; hashes alone are not rank proofs.
