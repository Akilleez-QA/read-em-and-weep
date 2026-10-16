# Seed-4 carrier-block order comparison

The new direct-F curvature contraction vanishes for all 256 potentially nonzero intra-carrier swap assignments. All 512 A/B multiplier certificates separate with normal (-1,-1,0,1); minimum gap 30. This proves a conditional order-independent zero theorem for the same refined seed-4 E12 functional, within its stated edge and curvature domains. Historical source identification and scalar-41 equivalence remain outside this result.

Read `carrier-block-order-invariance.md` for the theorem, complete 884736-assignment partition, source/frame conventions, derivative signs and domain conditions.

## Immutable dependencies

Use the public `research/hm/null-support-certificates` directory from Akilleez-QA/read-em-and-weep commit `ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18`. `immutable-source-pins.json` records Git blobs fetched at that exact ref and checked against local public bytes. `dependency-hashes.json` records their SHA256 hashes. Additional inert source authentication files are used by the existing public dependency validators.

The prior reviewed order-defect theorem is at commit `9a4eda0d2251f0a89a677018188d5f9ea9269c5e`, directory `research/hm/null-source-integration/order-comparison`.

## Verify without regeneration

With this package in its published `order-comparison/curvature-addendum` directory:

```sh
python -B prepare_certificate.py
python -B test_direct_curvature.py ../../../null-support-certificates
```

Alternatively pass the path of a separate unchanged checkout of `null-support-certificates`. The verifier rebuilds the new factored roots, checks all 512 associations and recomputes support bounds using independent bounded-simplex vertex enumeration. It does not rerun the old support scans.

## Regenerate the new certificate

```sh
python -B probe_direct_curvature.py ../../../null-support-certificates
```

This regenerates only the new 256-tuple certificate and dependency hashes. The distributed deterministic gzip is restored by `prepare_certificate.py`, which validates both compressed and decompressed hashes. The decompressed JSON is generated and gitignored.

The three verification groups pass. Only finite labels, exact integer support metadata, hashes, and factored syntax are manipulated. No physical polynomial operations or execution admission occur.
