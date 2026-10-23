# Reproduce the exact source125 ten-row coverage audit

## Purpose and limits

Run with Python 3 and its standard library only. The verifier reads exactly one original source-catalog entry, its stable-label identity, eight published proof files covering nine source rows, the bb/bc exact-version review, and three original foundational notes. Together with the two catalogs, those are fourteen fixed immutable input files. It checks the ten explicitly listed tuples, not a source enumeration or a current frontier tally.

The only representation computation is fixed exact arithmetic on the nine abstract binary-icosahedral conjugacy classes, with symmetric powers no higher than 18. It checks the two characters and multiplicity obstruction used in the direct ff argument. No selected HM/source instance, parameter, coefficient, point, derivative, matrix or instance rank is constructed or evaluated.

The verifier establishes identities and coverage, not the mathematical correctness of a proof by its hash. Read PROOF.md and the matching whole-source statements. The published dependency proofs remain responsible for their own saturation, connection and branch-exhaustion arguments. A separate exact-version review of this coverage deduction is required before recommending it for publication.

## Immutable inputs and provenance

Repository: Akilleez-QA/read-em-and-weep.

The original catalog and foundational notes are pinned to commit db51525015bb7c5e825833d550d08dedf6f6ea96 under research/hm/order-four-quadratic-load/:

- one-one-endpoint-necessary-pairs.json: Git blob fe0afa410d89340d3082dc814277f89fbb582c19.
- rank-three-quotient-frontier-144.json: Git blob 8b5971092f9ef762584912609fd5e9301c4e271d.
- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: Git blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: Git blob d7506dae49b4be43230450c4132bd5db91f137ef.
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md: Git blob dcacf0bcdef8377c1ed7654e5b82659ea409456e.

COVERAGE.json and verify.py independently specify the eight exact proof commit/path/blob pins. COVERAGE.json also gives direct canonical GitHub URLs. The ee dependency is Section 6 of research/hm/profile11-o16-six-source-exclusions/PROOF.md, not a source125-ee folder. The bb and bc rows both use research/hm/profile11-source125-bb-bc-exclusion/PROOF.md at commit d679aa09811f821505254572a51e65b2904d03c9.

During assembly, each published proof and the three foundational notes were fetched through the GitHub connector at its exact commit and path. The bb/bc review was independently fetched at the same publication commit. All fetched proof bytes matched the pinned Git blobs. The bb/bc proof additionally matched its independently reviewed SHA256, 9d0ac1a9bfbd0bb1f30b42721d456f0ee7776b215c07b52648e62f416f90758c. These readbacks establish the publication provenance used here; hashes alone would not establish an arbitrary claimed commit-to-path association.

The offline audit-inputs/ files are exact cached copies for checking, not new exclusion proofs or files to republish. Their original wording, including spacing inside quoted source material, is intentionally preserved byte-for-byte.

## Run directly from an existing authenticated checkout

The following mode reads each immutable commit:path with git show. It does not fetch, alter the checkout, use its current working-tree files, or trust mutable branch names. The named commits must already exist in that repository.

    python3 verify.py --repository /path/to/read-em-and-weep

This also binds every checked blob to its exact recorded commit and path. No network operation is performed by the verifier. A missing commit, missing file, changed pin, absent scope marker, catalog mismatch, omitted row or incorrect tuple-to-proof mapping fails closed with a nonzero exit status.

## Run using exact cached audit inputs

Place the original five files above under audit-inputs/ with their original basenames. Place the eight proof files there as ee.md, ef.md, bf.md, cf.md, be.md, ce.md, cc.md and bb_bc.md, according to COVERAGE.json. Place the published bb/bc REVIEW.md there as bb_bc-review.md.

Then run:

    python3 verify.py

The script verifies every Git blob before parsing its content. The exact bb/bc review SHA256 is also checked and the review must name the exact reviewed proof SHA256.

To prepare these cached copies from an existing checkout, run this small standard-library script beside verify.py, replacing the repository path:

    from pathlib import Path
    import subprocess
    import verify as v

    repository = Path('/path/to/read-em-and-weep')
    destination = Path('audit-inputs')
    destination.mkdir(exist_ok=True)

    def copy_at(commit, path, name):
        content = subprocess.check_output(
            ['git', '-C', str(repository), 'show', commit + ':' + path])
        (destination / name).write_bytes(content)

    for name in v.INPUTS:
        copy_at(v.ORIGINAL, v.PREFIX + name, name)
    for key, (_, commit, folder, _) in v.PINS.items():
        copy_at(commit, 'research/hm/' + folder + '/PROOF.md', key + '.md')
    copy_at(v.PINS['bb_bc'][1],
            'research/hm/profile11-source125-bb-bc-exclusion/REVIEW.md',
            'bb_bc-review.md')

Run the verifier afterward; the copy step does not itself certify any identity.

## Expected output

For the cached-copy mode:

    PASS: exact source125 identity and complete ordered ten-row coverage.
    PASS: eight pinned whole-source proof files cover nine rows; direct strict-top covers ff.
    PASS: five original input pins, bb/bc exact-version review, ten decodings/rank-degrees, and fixed ff characters.
    Input mode: hash-checked immutable audit copies.
    Boundary: dependency/coverage audit, not formal proof certification or a current frontier count.
    No selected actual source evaluation, source scan, or large computation.

The repository mode instead prints “Input mode: immutable commit:path readback.” The verifier uses explicit checks, not Python assert statements; python3 -O verify.py runs the same checks rather than disabling them.

## Publication boundary

This package is separate from the bb/bc exclusion package. Its intended publication artifacts are PROOF.md, COVERAGE.json, verify.py, REPRODUCE.md and the independently written exact-version REVIEW.md when available. Do not duplicate the audit-inputs/ dependency copies in a new publication. Do not update an original catalog or infer a current frontier count from this package. Publication and any broader catalog accounting belong to the parent task, not this verifier.
