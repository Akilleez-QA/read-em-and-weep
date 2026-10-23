# Reproduction and source access

The proof uses five exact repository originals recorded in INPUTS.json. They were read from their immutable public versions. Their raw bytes, Git blob hashes, SHA256 hashes and byte counts are recorded. Earlier geometric dependencies of those originals remain in force; they are not replaced by dimension matching.

To reconstruct the omitted audit inputs, from a clone of Akilleez-QA/read-em-and-weep containing the pinned commits, run the following Python snippet from this package directory (or add git -C with that clone's directory):

    import pathlib, json, hashlib, subprocess
    out = pathlib.Path('audit-inputs')
    out.mkdir(exist_ok=True)
    for e in json.loads(pathlib.Path('INPUTS.json').read_text()):
        b = subprocess.check_output(['git', 'show', e['commit'] + ':' + e['path']])
        assert len(b) == e['bytes']
        assert hashlib.sha256(b).hexdigest() == e['sha256']
        assert hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest() == e['git_blob_sha1']
        (out / (e['key'] + '.md')).write_bytes(b)

Alternatively retrieve raw content from the immutable URLs in INPUTS.json and apply the same checks, with no newline normalization.

## Primary source check

Bănică--Manolache, Moduli space M_P3(-1,4): minimal spectrum, INCREST preprint19/1983:

https://www.imar.ro/~increst/1983/19_1983.pdf

The original non-www host failed during this audit; the official www host returned the complete 36-page, 25,238,240-byte scan. Its SHA256 is 1d0cf269d126050779bce67e41a5643b1789bc555378064bd89241bebe71c151. It is distinct from their 1981 preprint104. Section3 printed page5/PDFpage11 explicitly includes a conic plus a degree-four double of a possibly degenerate conic, including line-supported cases; the Ferrand lemma immediately below supplies lci and ideal containment. The checked repository classification proof records the exhaustive classification and the hypotheses excluding the additional doubled-plane-cubic case. The relevant scan page was visually read; OCR alone is not the source of formulas.

The scan is not republished in this package. The exact source is linked for independent inspection.

## Bounded universal checks

    python verify.py
    python -O verify.py

These use explicit RuntimeError checks. They check parity dimensions in fixed abstract coordinate representations, the elementary complete-intersection square Hilbert calculation, universal monomial colon identities in two formal regular parameters, and degree arithmetic. Reconstructed original inputs are hash-checked when present.

No actual HM/source coordinate, coefficient, point, parameter, matrix, derivative or instance rank is evaluated. These small checks are not a proof of the geometry. In particular the classification transfer, invariant support arguments, global Ferrand presentation, ordinary-square sheaf memberships and actual base-change application require PROOF.md and its independent mathematical review. No proof-assistant verification is claimed.
