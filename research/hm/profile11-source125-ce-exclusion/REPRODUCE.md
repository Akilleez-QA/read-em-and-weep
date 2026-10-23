# Reproduce the fixed checks

Run Python3 from this directory:

    python verify.py

Only the Python standard library is required. The two original audit inputs are read from audit-inputs and their Git blob hashes are checked before source identity is accepted.

Immutable original repository commit: db51525015bb7c5e825833d550d08dedf6f6ea96, Akilleez-QA/read-em-and-weep. Under research/hm/order-four-quadratic-load, download:

- one-one-endpoint-necessary-pairs.json, Git blob fe0afa410d89340d3082dc814277f89fbb582c19;
- rank-three-quotient-frontier-144.json, Git blob 8b5971092f9ef762584912609fd5e9301c4e271d.

Put these exact bytes in audit-inputs. The checker performs bounded fixed representation identities and Hom tests only. It does not evaluate any selected actual source, run experiments, scan sources or claim a frontier count. The connection and saturation arguments are in PROOF.md.
