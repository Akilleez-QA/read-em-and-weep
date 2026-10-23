# Construct the source-response leg on the global cone complex

The pinned monad termwise acyclicity at twists two and four proves a short
exact sequence of GLOBAL complexes, not just a sheaf restriction sequence:

    0 -> C_2 --q--> C_4 -> C_Q -> 0.

Consequently the entire global cone differential image equals the cone
restriction of the ambient differential image. This identifies the full
global cone model of PR904's domain; it does not enlarge that domain.

For the fixed/coherently compared canonical V and b, the prior raw-cubic
quotient identity puts s_Q=res_Q(a(V-bZ)) in that image without first
choosing W. The actual cone weight-four vanishing theorem makes the
physical source row well-defined on the whole image.

The constructive equivalence is exact: solve d_Q e_Q=s_Q, lift e_Q globally
to E, and recover W=(S-dE)/q. This W is a closed global cochain and satisfies
dE=S-qW. All steps admit equivariant linear sections on the entire
cubic-a/linear-h coefficient family, without pointwise parameter division.

Only the source-response leg is cone-only. The full ambient lower
projection y, physical contractions, markings, frame transport and their
normalization comparison are still required. The row is not zero merely
because closed global cone adjoints have zero weight-four coefficient.
It is not a map on cohomology or an evaluated physical response.

A supplied unrelated W still needs PR894's compatibility check. All its
corrected sources have the same cone restriction, including incompatible
ones. Recovering a new W is not validating a supplied packet.

## Reproduction

    python verify_global_cone_response.py
    python -O verify_global_cone_response.py
    sha256sum -c SHA256SUMS

Each Python command reports 108 exact integrity/character/q-cochain checks
and eight negative controls. They verify immutable source-copy integrity,
universal character arithmetic, the cited Bott inequalities and formal
q-division/differential signs. They do not prove the upstream geometric
theorems or compute an actual cochain, matrix, rank, source, primitive,
calibration or response value. Explicit comparisons remain active under -O.

PROOF.md supplies the bounded written theorem and strict physical gates.
REVIEW.md binds independent mathematical and reproducibility review to
final bytes. SOURCE-MANIFEST.json identifies eight immutable input copies;
REMOTE-AUTHENTICATION.json records fresh GitHub reads at their exact
commits. FINAL-MANIFEST.json and SHA256SUMS freeze the package.

PR889, PR894 and PR904 remain unchanged. No publication or new Lean
formalization was performed by this worker.
