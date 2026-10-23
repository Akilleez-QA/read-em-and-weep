# Canonical octic normal lift

The canonical octic gate has a unique quotient-first-annihilated polynomial lift R=κψ, with R²=0. Its zero scheme is sixteen reduced axes; projection produces the known length46 scheme. Every polynomial lift of the gate has a unique form BU+αR. An explicit quadratic-remainder map kills every BU gauge term and specifies coefficient extraction for α without supplying or evaluating actual HM coefficients.

Run `python verify.py` and `python -O verify.py`. Both run186 checks and regenerate RESULT.json, UNIVERSAL-MATRIX.json and PINNED-OCTIC-MATRIX.json. UNIVERSAL-MATRIX.json is a universal determinantal recipe with formal placeholders, not a coordinate realization of the HM family. Exact family geometry is imported from the five immutable public proofs in INPUTS.json. No actual scalar is evaluated and no source or pair is removed.

scalar_extraction.py implements the symbolic remainder extractor, checks the entire quotient identity, and rejects an off-line candidate or zero generator quotient. Its tests use formal synthetic matrices only.

PINNED-OCTIC-MATRIX.json additionally instantiates the fixed universal representation matrix over Q(sqrt(5))[p,q,t], without parameter evaluations. Its exact q^8 coefficient gives alpha = -27 times the q^8 coefficient of entry(0,0) in any homogeneous lift, independent of multiplication gauge. build_universal_matrix.py reconstructs that artifact. No actual lift is supplied or evaluated.
