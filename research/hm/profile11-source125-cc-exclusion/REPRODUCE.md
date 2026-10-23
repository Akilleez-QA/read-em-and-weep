# Reproduction

Run `python3 verify.py` in this directory using Python3 and its standard library.

Place the exact UTF-8 bytes of these files in `audit-inputs/`:

- Akilleez-QA/read-em-and-weep at commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json. Expected Git blob: fe0afa410d89340d3082dc814277f89fbb582c19.
- The same commit and directory, rank-three-quotient-frontier-144.json. Expected Git blob: 8b5971092f9ef762584912609fd5e9301c4e271d.

The verifier recomputes their Git blob hashes before reading source125 and the one named label. It performs no current-frontier count, model construction, coefficient evaluation, point evaluation, or instance-rank calculation. Its finite kernel filter considers only nine universal irreducibles, degrees3..19, and the fixed rank8/degree40/cohomology16 budget. The subsequent two-kernel classification is the elementary multiplicity argument in PROOF.md.

The character table is represented exactly in Q(sqrt5), and the verifier first checks orthonormality of all nine irreducible characters. The universal representation checks do not certify the sheaf-theoretic proof by themselves; read the whole PROOF.md.
