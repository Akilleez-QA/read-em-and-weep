# Reproduction and publication boundary

This packet is stacked on `null/rankfour-extremal-plateau`, commit `ba6b3ef9f1a2ca79f9491025560e2a074a42dbbd` (#1173). All additions are under `research/hm/rankfour-adjacent-plateau`.

## Reproduce

From the repository root:

```sh
python3 research/hm/rankfour-adjacent-plateau/verify.py > /tmp/rankfour-adjacent-normal.json
python3 -O research/hm/rankfour-adjacent-plateau/verify.py > /tmp/rankfour-adjacent-optimized.json
cmp /tmp/rankfour-adjacent-normal.json /tmp/rankfour-adjacent-optimized.json
cmp /tmp/rankfour-adjacent-normal.json research/hm/rankfour-adjacent-plateau/RESULT.json
python3 research/hm/rankfour-adjacent-plateau/independent/check_package.py
```

All scripts resolve inputs relative to their own files. They use only the Python standard library and work from an unrelated current directory. The portable package authenticates 17 files and replays both independent and author verifiers under normal and optimized Python; it also reruns six genuine negative controls. The publication manifest includes every other publication file and binds both the exact text and Git blob identity.

The author checker records 724 explicit checks, including 142 rejected mutations. The independent checker records 222 checks; its six genuine mutations test source bytes, endpoint parity, defect weights, quotient twist, physical marking, and the line-tail H1 correction. Normal and optimized outputs agree byte-for-byte.

## Frozen identities

- Author proof SHA-256: `de3bacb2f5a548637363e5a0f646123457c07dd5cbdaa3976c7a8e6c326db4eb`.
- Author verifier SHA-256: `38f132ea39b348e2fe87d593a27077b6c7faf6f757e4d2b79fdb8763b1e13988`.
- Independent review SHA-256: `93bbd87d4cfa7560b18a6952eda72b5c9714fc4342c8bcccf98b71ab602be5ff`.
- Independent package manifest SHA-256: `3052acd97658e9b248f9cea124745abeefdb24e61e5460aa2e67fa7c56f971e9`.

The public original source is `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md` at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, pinned in INPUTS.json. The exact portable review is preserved under independent/ without changing its manifest or any reviewed file.

## Boundaries

The written proof supplies the geometric argument, conditional on the explicit actual-input ledger. Hash authentication does not prove transitive geometric premises. Arithmetic tests are not proof-assistant verification. No quotient-shape enumeration is used. No rank-at-least-five theorem, square-map surjectivity, full-adjoint invertibility, or original repair is claimed.
