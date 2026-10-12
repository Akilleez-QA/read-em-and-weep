# Supplied-value audit of draft #74 at ba63172d

Scope is PR #1 comment 6124754293, applied to draft #74
(`research/f3-cartier-component-23615-r41`, commit
`ba63172d059cc41dd84ca1491f014802d5a1dffa`). The package under
`research/hm/f3-cartier-component-23615-r41/` was not modified.
This note and the two scripts next to it are the audit.

A pass means the supplied value and its encoding are self-consistent
and match the stated hashes and counts. It does not rerun the source
DAG, assemble the nine signed queries, evaluate a detector or ell(O2),
or say anything about the obstruction.

## Order of work

1. Read PR #74's body and PR #1 comment 6124754293.
2. Read `README.md`, `ATTRIBUTION.md`, `spec.json`, `frames/HEAD.json`,
   `component-receipt.json`, `held-state-receipt.json`, `value-files.json`,
   `SHA256SUMS`, and the frame headers. The checker sources were not opened.
3. A repository search for the schema name printed four lines of
   `verify_component.py` and `test_verify_component.py` (the `F3SLICE1`
   magic, the 4-byte header length, and that a header stores keep bounds
   and a semantic hash). Those lines repeat bytes already read from the
   frames. They were not used as the decoder.
4. `decode_component.py` was written and run. It reported 95,082 nonzero
   rows, 659,344 trits, and logical-row SHA256
   `ab8a327f73a88c781f377925b54ad6496cc20825ef9b83808f50bc0af916b426`
   before either checker source was read in full.
5. The checker sources were then read for comparison. The unchanged
   commands below were run, and `test_mutations.py` was run.

## How to rerun

From the repository root:

```
python3 -I -S -B research/hsd/receipt-audit-r41/decode_component.py research/hm/f3-cartier-component-23615-r41
python3 -I -S -B research/hsd/receipt-audit-r41/test_mutations.py
```

From the package directory:

```
python3 -I -S -B verify_component.py .
python3 -I -S -B test_verify_component.py -f
```

Both audit scripts use the Python 3 standard library only.

## Item 1 — file set and checksums

**Pass.**

The directory contains exactly these 38 files: `README.md`,
`ATTRIBUTION.md`, `SHA256SUMS`, `component-receipt.json`,
`held-state-receipt.json`, `spec.json`, `value-files.json`,
`verify_component.py`, `test_verify_component.py`, `frames/HEAD.json`,
and 28 `frames/*.f3s` files.

`SHA256SUMS` has 37 lines, in lexicographic path order, each
`digest<two spaces>name`, with a trailing newline. It does not list
itself. Every listed digest matches the file bytes. SHA256 of
`SHA256SUMS` is
`18f2e45ec39b204aa30c914dc57216b84d2b2e45039a013e40547d42913cdbbe`.
SHA256 of `component-receipt.json` is
`8eff7b2f7745d2b8131df6ab5e87fe0d41f2449fa43faee40ab4d84ca4ec136a`.

`spec.json` and `frames/HEAD.json` are canonical JSON with no trailing
newline. The other JSON files are canonical JSON with one trailing
newline. `value-files.json` lists 32 files (the 28 frames, `HEAD.json`,
`spec.json`, and the two public receipts). All 32 sizes and digests match.

## Item 2 — frames, padding, and commitments

**Pass.**

Each frame is `F3SLICE1\n`, a 4-byte big-endian header length, canonical
JSON, then the payload. The filename is the SHA256 of the file. Payload
SHA256 matches the header. Digits are 23,548 and the payload is 5,887
bytes on every frame.

Trits are packed two bits each, least-significant pair first. A stored
pair equal to 3 is rejected. When `2 * digits` is not a multiple of 8,
the leftover high bits of the last byte are padding and must be zero.
Every supplied frame has `23548 % 4 == 0`, so the padding width is 0
and that check holds. The same rule rejects the one-byte vector
`digits=1`, body `0x04`, and accepts body `0x24` with `digits=3` as
trits `0,1,2`.

The previous-hash chain is a single path of sequences 1..28. It matches
`store.orderedFrameSHA256`. Transactions are batches `[13, 13, 2]`,
matching `store.batches`. Inside a batch, `transactionFirst`,
`transactionCount`, and `transactionPreviousSHA256` are constant, and
the ordinal is the index in the batch. The first batch's transaction
previous hash is 64 zero digits. Each later batch points at the last
frame of the previous batch.

`frames/HEAD.json` has `count` 28, `schema` equal to `spec.json`,
`contractSHA256` equal to the spec file digest
`6d773fab0c9ffa021dc4de57cf6cf3cc3c495325652fee900f23ec7f6d3b3b7b`,
and `lastSHA256` equal to the last frame
`635940cfb65634f29779b6ea9c949453a31cd1031b353f5ecd4b91048c973538`.
Every frame repeats that contract, the spec keep bounds and keep mask,
source node 133174, and the SHA256 of the canonical `sourcePins` JSON.
`store.headSHA256` and `store.specSHA256` match `frames/HEAD.json` and
`spec.json`.

`keepBounds` `[0,0,0,0,27,27,28,28,47,85]` is read as four minima, four
maxima, and a total-degree window. The README does not spell that
10-tuple out. Under that reading, 224,175 trits lie outside the window
and all of them are zero. Nonzero quotient degrees run from 51 through
81, inside 47..85. The receipt's logical bounds
`[0,0,0,0,83,83,85,85,146,260]` contain every decoded logical exponent.
Per-coordinate extremes are minima `(2,1,1,1)` and maxima
`(83,82,85,85)`. Those are separate axes, not one row. Logical total
degrees of nonzero rows run from 158 through 248. The second-axis
maximum 82 sits inside the stated enclosure 83.

`keepMask` `0x1ffffffffffffffffffff` (`2^81 - 1`) is the same on the
spec and every frame. The README gives it no predicate. It is checked
only as an equal string. The logical receipt mask `0x20000000000` equals
`2^41`. There are 2,785 nonzero rows of quotient degree 81, so this
audit does not treat the quotient mask as "bit d allows degree d".

## Item 3 — the two coordinate orders

**Pass.**

Residue digits `(2,1,1,1)` pack with the first coordinate least
significant: `2 + 3 + 9 + 27 = 41`. The receipt's `residueCode` is 41
and its rule is `3*q+r`. Logical exponent `e = 3q + (2,1,1,1)`.

Dense traversal uses the last coordinate fastest. On each plane of shape
`(28,29,29)`, linear index `j` is `(q1, q2, q3) = (j // 841, (j // 29) % 29, j % 29)`,
with the plane index as `q0`. Because each logical coordinate is
strictly increasing in the quotient coordinate, that traversal already
emits lexicographic exponent order. A direct sort of the decoded rows
does not reorder them. The opposite convention, first coordinate
fastest, is a different order. Its row hash is in discriminator (e).

## Item 4 — counts and logical-row hash

**Pass.**

Decoded nonzero rows: 95,082. Coefficients: 47,484 ones and 47,598 twos,
and no other nonzero trit. Trits including zeros: 659,344.

The logical-row digest streams those nonzero rows in lexicographic
exponent order. Each row is ASCII `[[e0,e1,e2,e3],c]` plus one newline,
with no spaces. The SHA256 is
`ab8a327f73a88c781f377925b54ad6496cc20825ef9b83808f50bc0af916b426`.
It is computed from the decoded rows, not from frame bytes. The first
row is `[[2,37,70,79],1]\n`. The last is `[[83,82,58,22],1]\n`.

The README states the digest and does not state the separators. The
spaced reading `[[e0, e1, e2, e3], c]\n` hashes to
`59900d9910f47dd679fe730df5875f15e6088aa2552300fd589d2df67e454374`
and does not match. The no-space reading is the one that reproduces the
published digest. PR #74's body writes the no-space form. The same
no-space form is what the package checker hashes, which was compared
only after the digest above had already been computed.

## Item 5 — source-attribution labels

**Pass.** Label check only. The source polynomial was not regenerated.

`component-receipt.json` field `source.finalWeightedTerms` is
`[[1,133169,[]],[2,133173,[[9,1],[13,1]]]]`.
That is coefficient 1 on node 133169 with no outside factor, and
coefficient 2 on node 133173 with outside factors 9 and 13, each to
the first power. `source.finalOriginalRow` is 6172.

`README.md` and `ATTRIBUTION.md` do not state coefficients 1 and 2, or
outside factors 9 and 13, for that final source row. They also do not
state different values for it. The labels are therefore consistent
across the three files: one statement, no conflicting statement.

`ATTRIBUTION.md` uses 1 and 2 as pairing weights and as a scalar in a
different sentence, and it says the direct module use
`142904=(15,133174)` has no ordinary outside-weight reference to source
`s23615`. That sentence is about that module use, not about
`finalWeightedTerms`. It was not read as a second value for factors 9
and 13.

`README.md` names the held6173 representation. `held-state-receipt.json`
has `acceptedState` 6173 and points `componentReceiptSHA256` at the
public projection `8eff7b2f...`, not at the historical anchor. Those are
different fields from the final source-row labels.

## Bundled checker output

`python3 -I -S -B verify_component.py .` exited 0 and printed:

```
{"denseTrits":659344,"frames":28,"fullDetectorEstablished":false,"fullObstructionEstablished":false,"heldStateReconstructed":false,"logicalRowsSHA256":"ab8a327f73a88c781f377925b54ad6496cc20825ef9b83808f50bc0af916b426","nonzeroTerms":95082,"sourceDAGRecomputed":false,"status":"PASS_SUPPLIED_COMPONENT_VALUE","wholeBlindPairingKnown":false}
```

`python3 -I -S -B test_verify_component.py -f` exited 0:

```
Ran 6 tests in 0.355s
OK
```

The checker does not print the row stream. After the independent digest
was already in hand, its row text was compared with this decoder:
both use `[[e0,e1,e2,e3],c]\n` with no spaces, last-coordinate-fastest
indexing, and `e = 3q + (2,1,1,1)`. The published digest matches both.

## Discriminators

Mutations were applied only to temporary copies. Both the audit decoder
and the unchanged package checker reject (a)-(d). None was accepted.

| Case | What changed | Audit decoder | Package checker |
| --- | --- | --- | --- |
| (a) | Low bit of the coefficient-1 trit at quotient `(0, 12, 23, 26)`, which is logical row `(2, 37, 70, 79)` | exit 1, `SHA256 mismatch` for that frame | exit 1, `file hash` |
| (b) | Digits `23548` to `23547` on the first frame, then bit 6 of the last byte. That bit is padding only after the digit change. The padding rule reports `padding bits are not zero` | exit 1, `SHA256 mismatch` | exit 1, `file hash` |
| (c) | Header field `ones` incremented by 1 on the first frame | exit 1, `SHA256 mismatch` | exit 1, `file hash` |
| (d) | Bytes of the first two chain frames swapped, names left in place. Those files are 6,759 and 6,760 bytes | exit 1, `SHA256 mismatch` | exit 1, `bounded regular file` |
| (e) | Same decoded rows streamed with the first coordinate fastest, then hashed with the same ASCII | hash `b8e59db94ffdb9fe80e03573d7a8370c5a634b3dfd789df06a36cb39b1799826`, different from `ab8a327f...` | not a file mutation |

(a) also recomputes the logical-row digest from the edited trits, past
the filename pin. The digest changes from `ab8a327f...` to
`5d2b75ef90afebb1fd12edb8e432529cbd36bfa73c977a90f724b5bb6e73cdc5`.

(b) needs the digit change because every supplied frame has padding
width 0. The package checker pins `value-files.json` and each frame
digest, so its rejection of (a)-(c) is that pin (`file hash`) and its
rejection of (d) is the pinned size (`bounded regular file`). Those
runs do not show the checker reaching its row-digest or padding branch.
The audit decoder's own padding rule does reject the flipped bit, and
its recomputed row digest moves under (a). No mutated copy was accepted.

## Historical anchor

`verification.componentReceiptSHA256` in `component-receipt.json` is
`89462eec704f08f26bcf5efd2291d375ff1ca512e45051dcd1bddcd82ae27271`.

**Not verifiable from package.** No file in the package has that digest.
Rehashing the public projection `8eff7b2f...` is not a rehash of the
archival receipt. This audit does not mark the historical anchor checked.

## Residual shared-spec risk

Both readers share one specification. Agreement alone is not independent
corroboration: two implementations of one ambiguous rule fail together.
The concrete README gap is the logical-row ASCII. The published digest
selects the no-space form and rejects the spaced form, so that gap is
closed by the hash rather than by the other program. Bit order is closed
by each frame's `semanticSHA256`, which matches the least-significant-pair
packing and the compact quotient-row text; that commitment was matched
before the checker source was read.

What remains is a rule that neither the README nor those commitments
states. `keepMask` is the example: both readers require the spec string
and neither applies a bit predicate. A mask rule that was intended and
never written down would not be caught by this audit.

## Mismatches

No item failed. There is no minimal reproducing input for a bad file
set, checksum, count, padding fault, or row hash on the pinned package.
The spaced ASCII reading above is the reading that does not reproduce
the digest; it is an ambiguity, not a fault in the supplied bytes.
