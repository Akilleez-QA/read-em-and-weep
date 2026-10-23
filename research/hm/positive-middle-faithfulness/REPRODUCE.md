# Bounded reproduction

Run python verify.py and python -O verify.py from this folder. Both outputs
must agree with RESULT.json. The checker uses exact rational arithmetic in
the fixed nine-class character ring of SL2(F5), finite Koszul-index and
shift bookkeeping, and Git-blob/SHA256 authentication of four complete inputs.
It does not read or evaluate any actual HM multiplication coefficients,
source parameters, selected points, derivatives, jets, tensors or matrices.
No scan or large computation occurs.

The written actual-map argument is essential: the checker does not prove
regular Koszul exactness, symmetric-evaluation exactness, or the inherited
natural multiplication identifications. The values in RESULT.json are
written-theorem consequences; their appearance is not an independent rank
computation or proof-assistant certificate. REVIEW.md supplies the independent
whole-proof review and binds the reviewed final bytes.
