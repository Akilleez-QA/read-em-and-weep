#!/usr/bin/env python3
"""Independent decoder for the supplied residue-41 F3 component package.

The packing and row format below were read from README.md, spec.json,
frames/HEAD.json, the public receipt JSON, and the commitments inside each
frame header. This module does not import the package verifier.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


RESIDUE = (2, 1, 1, 1)
EXPECTED_ROW_HASH = (
    "ab8a327f73a88c781f377925b54ad6496cc20825ef9b83808f50bc0af916b426"
)
EXPECTED_NONZERO = 95082
EXPECTED_TRITS = 659344
EXPECTED_SHA256SUMS = (
    "18f2e45ec39b204aa30c914dc57216b84d2b2e45039a013e40547d42913cdbbe"
)
EXPECTED_RECEIPT = (
    "8eff7b2f7745d2b8131df6ab5e87fe0d41f2449fa43faee40ab4d84ca4ec136a"
)
HISTORICAL_RECEIPT = (
    "89462eec704f08f26bcf5efd2291d375ff1ca512e45051dcd1bddcd82ae27271"
)
ZERO_HASH = "0" * 64
FINAL_WEIGHTED_TERMS = [[1, 133169, []], [2, 133173, [[9, 1], [13, 1]]]]


class DecodeError(Exception):
    pass


def residue_code(residue: tuple[int, ...]) -> int:
    """Pack residue digits with the first coordinate least significant."""
    total = 0
    weight = 1
    for digit in residue:
        total += digit * weight
        weight *= 3
    return total


def logical_exponent(quotient: tuple[int, ...], residue: tuple[int, ...] = RESIDUE) -> tuple[int, ...]:
    if len(quotient) != len(residue):
        raise DecodeError("quotient rank does not match residue")
    return tuple(3 * quotient[i] + residue[i] for i in range(len(quotient)))


def coords_last_fastest(index: int, shape: tuple[int, ...]) -> tuple[int, ...]:
    """Dense index with the last coordinate changing fastest."""
    coords = [0] * len(shape)
    for axis in range(len(shape) - 1, -1, -1):
        coords[axis] = index % shape[axis]
        index //= shape[axis]
    if index:
        raise DecodeError("index outside shape")
    return tuple(coords)


def coords_first_fastest(index: int, shape: tuple[int, ...]) -> tuple[int, ...]:
    """Dense index with the first coordinate changing fastest."""
    coords = [0] * len(shape)
    for axis, size in enumerate(shape):
        coords[axis] = index % size
        index //= size
    if index:
        raise DecodeError("index outside shape")
    return tuple(coords)


def row_line(exponent: tuple[int, ...], coefficient: int) -> bytes:
    """ASCII '[[e0,e1,e2,e3],c]' plus one newline, with no spaces."""
    body = "[" + ",".join(str(part) for part in exponent) + "]"
    return f"[{body},{coefficient}]\n".encode("ascii")


def spaced_row_line(exponent: tuple[int, ...], coefficient: int) -> bytes:
    """Same row with spaces after commas. README does not choose this."""
    body = "[" + ", ".join(str(part) for part in exponent) + "]"
    return f"[{body}, {coefficient}]\n".encode("ascii")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(obj: object) -> bytes:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True).encode("ascii")


def check_conventions() -> None:
    if residue_code(RESIDUE) != 2 + 3 + 9 + 27 or residue_code(RESIDUE) != 41:
        raise DecodeError("residue packing did not reproduce code 41")
    if logical_exponent((0, 0, 0, 0)) != RESIDUE:
        raise DecodeError("logical map does not fix the residue at the origin")
    shape = (2, 2, 2, 2)
    last = [coords_last_fastest(i, shape) for i in range(16)]
    first = [coords_first_fastest(i, shape) for i in range(16)]
    if last[1] != (0, 0, 0, 1) or first[1] != (1, 0, 0, 0) or last == first:
        raise DecodeError("dense traversal orders are not distinct")


def iter_trits(payload: bytes, n_digits: int):
    """Yield trits packed two per digit, least-significant pair first.

    Bits past the last trit in the final byte are padding and must be zero.
    A stored pair equal to 3 is not a trit.
    """
    if n_digits < 0:
        raise DecodeError("negative digit count")
    bit_count = n_digits * 2
    if len(payload) * 8 < bit_count:
        raise DecodeError("payload shorter than the digit count")
    pad_bits = len(payload) * 8 - bit_count
    if pad_bits >= 8:
        raise DecodeError("payload has a whole extra byte beyond padding")
    if pad_bits:
        mask = ((1 << pad_bits) - 1) << (8 - pad_bits)
        if payload[-1] & mask:
            raise DecodeError("padding bits are not zero")
    for index in range(n_digits):
        byte = payload[index // 4]
        shift = 2 * (index % 4)
        trit = (byte >> shift) & 3
        if trit == 3:
            raise DecodeError(f"digit {index} is not a trit")
        yield trit


def parse_frame(path: Path) -> dict:
    raw = path.read_bytes()
    if len(raw) < 13 or raw[:9] != b"F3SLICE1\n":
        raise DecodeError(f"{path.name}: missing frame magic")
    header_len = int.from_bytes(raw[9:13], "big")
    header_end = 13 + header_len
    if header_end > len(raw):
        raise DecodeError(f"{path.name}: header length exceeds the file")
    header_raw = raw[13:header_end]
    try:
        header = json.loads(header_raw.decode("ascii"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise DecodeError(f"{path.name}: header is not JSON") from exc
    if canonical_json(header) != header_raw:
        raise DecodeError(f"{path.name}: header is not canonical JSON")
    payload = raw[header_end:]
    digest = sha256_bytes(raw)
    if path.stem != digest:
        raise DecodeError(f"{path.name}: filename is not the file SHA256")
    return {
        "path": path,
        "raw": raw,
        "header": header,
        "payload": payload,
        "sha256": digest,
    }


def in_keep(quotient: tuple[int, ...], keep_bounds: list[int]) -> bool:
    if len(keep_bounds) != 10 or len(quotient) != 4:
        raise DecodeError("keep bounds are not a 4-axis window plus degree pair")
    for axis in range(4):
        if not keep_bounds[axis] <= quotient[axis] <= keep_bounds[4 + axis]:
            return False
    degree = sum(quotient)
    return keep_bounds[8] <= degree <= keep_bounds[9]


def load_json(path: Path, trailing_newline: bool) -> tuple[object, bytes]:
    raw = path.read_bytes()
    if trailing_newline:
        if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
            raise DecodeError(f"{path.name}: expected exactly one trailing newline")
        body = raw[:-1]
    else:
        if raw.endswith(b"\n"):
            raise DecodeError(f"{path.name}: unexpected trailing newline")
        body = raw
    try:
        obj = json.loads(body.decode("ascii"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise DecodeError(f"{path.name}: not canonical JSON text") from exc
    if canonical_json(obj) != body:
        raise DecodeError(f"{path.name}: JSON is not canonical")
    return obj, raw


def list_package_files(root: Path) -> list[str]:
    files = []
    for path in root.rglob("*"):
        if path.is_symlink():
            raise DecodeError(f"unexpected symlink {path.name}")
        if path.is_file():
            files.append(path.relative_to(root).as_posix())
    return sorted(files)


def check_sha256sums(root: Path, files: list[str]) -> None:
    sums_path = root / "SHA256SUMS"
    raw = sums_path.read_bytes()
    if sha256_bytes(raw) != EXPECTED_SHA256SUMS:
        raise DecodeError("SHA256 of SHA256SUMS does not match the published digest")
    if not raw.endswith(b"\n"):
        raise DecodeError("SHA256SUMS has no trailing newline")
    lines = raw.decode("ascii").splitlines()
    if len(lines) != 37:
        raise DecodeError(f"SHA256SUMS has {len(lines)} lines, expected 37")
    listed = []
    for line in lines:
        digest, separator, name = line.partition("  ")
        if not separator or "  " in name or not name:
            raise DecodeError("SHA256SUMS line is not 'digest<two spaces>name'")
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise DecodeError("SHA256SUMS digest is not 64 lowercase hex characters")
        if name == "SHA256SUMS":
            raise DecodeError("SHA256SUMS lists itself")
        data = (root / name).read_bytes()
        if sha256_bytes(data) != digest:
            raise DecodeError(f"SHA256 mismatch for {name}")
        listed.append(name)
    if listed != sorted(listed):
        raise DecodeError("SHA256SUMS is not in lexicographic path order")
    expected = sorted(name for name in files if name != "SHA256SUMS")
    if listed != expected:
        missing = sorted(set(expected) - set(listed))
        extra = sorted(set(listed) - set(expected))
        raise DecodeError(f"SHA256SUMS file set mismatch missing={missing} extra={extra}")
    if len(files) != 38:
        raise DecodeError(f"package has {len(files)} files, expected 38")


def decode_package(root: Path) -> dict:
    check_conventions()
    root = root.resolve()
    files = list_package_files(root)
    check_sha256sums(root, files)
    spec, spec_raw = load_json(root / "spec.json", trailing_newline=False)
    head, head_raw = load_json(root / "frames" / "HEAD.json", trailing_newline=False)
    receipt, receipt_raw = load_json(root / "component-receipt.json", trailing_newline=True)
    held, _held_raw = load_json(root / "held-state-receipt.json", trailing_newline=True)
    value_files, _value_raw = load_json(root / "value-files.json", trailing_newline=True)
    if sha256_bytes(receipt_raw) != EXPECTED_RECEIPT:
        raise DecodeError("component-receipt.json SHA256 mismatch")
    if sha256_bytes(spec_raw) != head["contractSHA256"]:
        raise DecodeError("HEAD contract does not match spec.json")
    if head["schema"] != spec["schema"] or head["count"] != spec["shape"][0]:
        raise DecodeError("HEAD does not match the spec schema or plane count")

    frame_paths = sorted((root / "frames").glob("*.f3s"))
    if len(frame_paths) != 28:
        raise DecodeError(f"found {len(frame_paths)} frames, expected 28")
    frames = [parse_frame(path) for path in frame_paths]
    by_hash = {frame["sha256"]: frame for frame in frames}
    if len(by_hash) != len(frames):
        raise DecodeError("duplicate frame hash")

    # Walk the previous-hash chain. Sequence order must agree with that walk.
    cursor = ZERO_HASH
    chained = []
    for _ in range(len(frames)):
        found = [
            frame for frame in frames
            if frame["header"]["previousSHA256"] == cursor
        ]
        if len(found) != 1:
            raise DecodeError("frame previous-hash chain is not a single path")
        frame = found[0]
        chained.append(frame)
        cursor = frame["sha256"]
    if head["lastSHA256"] != chained[-1]["sha256"]:
        raise DecodeError("HEAD lastSHA256 is not the last frame")
    if [frame["header"]["sequence"] for frame in chained] != list(range(1, 29)):
        raise DecodeError("chain order is not sequence 1..28")

    order = [frame["sha256"] for frame in chained]
    if receipt["store"]["orderedFrameSHA256"] != order:
        raise DecodeError("receipt frame order does not match the hash chain")
    if receipt["store"]["headSHA256"] != sha256_bytes(head_raw):
        raise DecodeError("receipt head hash does not match frames/HEAD.json")
    if receipt["store"]["specSHA256"] != sha256_bytes(spec_raw):
        raise DecodeError("receipt spec hash does not match spec.json")
    if receipt["store"]["planes"] != 28:
        raise DecodeError("receipt plane count is not 28")

    shape = tuple(spec["shape"])
    if len(shape) != 4 or shape[0] != 28:
        raise DecodeError("spec shape is not 28 planes")
    plane_shape = shape[1:]
    plane_digits = 1
    for size in plane_shape:
        plane_digits *= size
    if plane_digits * shape[0] != EXPECTED_TRITS:
        raise DecodeError("shape volume is not 659344")
    keep_bounds = spec["keepBounds"]
    pins_hash = sha256_bytes(canonical_json(spec["sourcePins"]))
    batch_sizes = []
    batch_start = 0
    while batch_start < len(chained):
        count = chained[batch_start]["header"]["transactionCount"]
        batch = chained[batch_start:batch_start + count]
        if len(batch) != count:
            raise DecodeError("transaction extends past the last frame")
        anchor = ZERO_HASH if batch_start == 0 else chained[batch_start - 1]["sha256"]
        first_sequence = batch[0]["header"]["sequence"]
        for ordinal, frame in enumerate(batch):
            header = frame["header"]
            if header["transactionOrdinal"] != ordinal:
                raise DecodeError("transaction ordinal is not the index in the batch")
            if header["transactionCount"] != count or header["transactionFirst"] != first_sequence:
                raise DecodeError("transaction bounds are not constant across the batch")
            if header["transactionPreviousSHA256"] != anchor:
                raise DecodeError("transaction previous hash does not match the prior batch")
        batch_sizes.append(count)
        batch_start += count
    if receipt["store"]["batches"] != batch_sizes:
        raise DecodeError("receipt batches do not match the transaction chain")

    logical_rows = []
    nonzero = 0
    trit_count = 0
    padding_trits = 0
    padding_bits = 0
    ones = 0
    twos = 0
    degree_min = None
    degree_max = None
    logical_degree_min = None
    logical_degree_max = None
    logical_axis_min = None
    logical_axis_max = None
    for frame in chained:
        header = frame["header"]
        payload = frame["payload"]
        if header["schema"] != spec["schema"]:
            raise DecodeError("frame schema mismatch")
        if header["contractSHA256"] != sha256_bytes(spec_raw):
            raise DecodeError("frame contract does not match spec.json")
        if header["sourceNode"] != spec["sourceNode"] or header["sourceNode"] != receipt["componentNode"]:
            raise DecodeError("frame source node mismatch")
        if header["keepBounds"] != keep_bounds or header["keepMask"] != spec["keepMask"]:
            raise DecodeError("frame keep bounds or mask differ from spec.json")
        if header["sourcePinsSHA256"] != pins_hash:
            raise DecodeError("frame source-pin hash mismatch")
        if tuple(header["shape"]) != plane_shape or header["digits"] != plane_digits:
            raise DecodeError("frame shape or digit count mismatch")
        if header["origin"] != [header["x0"], 0, 0, 0]:
            raise DecodeError("frame origin is not [x0,0,0,0]")
        if header["x0"] != header["sequence"] - 1:
            raise DecodeError("frame x0 is not sequence-1")
        if header["complete"] is not True:
            raise DecodeError("frame is not marked complete")
        if len(payload) != header["payloadBytes"]:
            raise DecodeError("payload byte count mismatch")
        if sha256_bytes(payload) != header["payloadSHA256"]:
            raise DecodeError("payload SHA256 mismatch")
        pad_here = len(payload) * 8 - header["digits"] * 2
        if pad_here < 0:
            raise DecodeError("negative padding")
        padding_bits += pad_here
        semantic = hashlib.sha256()
        plane_ones = 0
        plane_twos = 0
        x0 = header["x0"]
        for local_index, trit in enumerate(iter_trits(payload, header["digits"])):
            trit_count += 1
            local = coords_last_fastest(local_index, plane_shape)
            quotient = (x0, local[0], local[1], local[2])
            kept = in_keep(quotient, keep_bounds)
            if not kept:
                padding_trits += 1
                if trit != 0:
                    raise DecodeError("padding trit outside keep bounds is nonzero")
                continue
            if trit == 0:
                continue
            if trit not in (1, 2):
                raise DecodeError("coefficient outside {1,2}")
            exponent = logical_exponent(quotient)
            logical_rows.append((exponent, trit))
            semantic.update(row_line(quotient, trit))
            nonzero += 1
            if trit == 1:
                plane_ones += 1
                ones += 1
            else:
                plane_twos += 1
                twos += 1
            degree = sum(quotient)
            logical_degree = sum(exponent)
            degree_min = degree if degree_min is None else min(degree_min, degree)
            degree_max = degree if degree_max is None else max(degree_max, degree)
            logical_degree_min = logical_degree if logical_degree_min is None else min(logical_degree_min, logical_degree)
            logical_degree_max = logical_degree if logical_degree_max is None else max(logical_degree_max, logical_degree)
            logical_axis_min = exponent if logical_axis_min is None else tuple(map(min, logical_axis_min, exponent))
            logical_axis_max = exponent if logical_axis_max is None else tuple(map(max, logical_axis_max, exponent))
        if semantic.hexdigest() != header["semanticSHA256"]:
            raise DecodeError(f"frame {header['sequence']} semantic hash mismatch")
        if plane_ones != header["ones"] or plane_twos != header["twos"]:
            raise DecodeError(f"frame {header['sequence']} one/two counts mismatch")
        if plane_ones + plane_twos != header["terms"]:
            raise DecodeError(f"frame {header['sequence']} term count mismatch")

    if trit_count != EXPECTED_TRITS or nonzero != EXPECTED_NONZERO:
        raise DecodeError(
            f"counts are trits={trit_count} nonzero={nonzero}, expected 659344 and 95082"
        )
    if ones + twos != nonzero:
        raise DecodeError("one and two counts do not add up to the nonzero rows")
    ordered = sorted(logical_rows)
    if ordered != logical_rows:
        raise DecodeError("last-coordinate-fastest traversal is not lexicographic")
    row_hash = hashlib.sha256()
    spaced_hash = hashlib.sha256()
    for exponent, coefficient in logical_rows:
        row_hash.update(row_line(exponent, coefficient))
        spaced_hash.update(spaced_row_line(exponent, coefficient))
    row_digest = row_hash.hexdigest()
    if row_digest != EXPECTED_ROW_HASH:
        raise DecodeError("logical-row SHA256 mismatch")
    if receipt["logicalCanonicalRowsSHA256"] != row_digest:
        raise DecodeError("receipt logical hash does not match the decoded stream")
    if receipt["nonzeroTerms"] != nonzero or receipt["denseTrits"] != trit_count:
        raise DecodeError("receipt counts do not match the decoded stream")
    if tuple(receipt["quotientShape"]) != shape:
        raise DecodeError("receipt quotient shape mismatch")
    if tuple(receipt["coordinateMap"]["residue"]) != RESIDUE:
        raise DecodeError("receipt residue is not (2,1,1,1)")
    if receipt["coordinateMap"]["rule"] != "3*q+r":
        raise DecodeError("receipt coordinate rule is not 3*q+r")
    if receipt["residueCode"] != 41:
        raise DecodeError("receipt residue code is not 41")
    logical_bounds = receipt["coordinateMap"]["bounds"]
    for exponent, _coefficient in logical_rows:
        if not in_keep(exponent, logical_bounds):
            raise DecodeError("logical exponent lies outside the receipt bounds")
    if held["logicalRowsSHA256"] != row_digest or held["parkedEntries"] != nonzero:
        raise DecodeError("held-state projection does not match the decoded rows")
    if held["componentReceiptSHA256"] != EXPECTED_RECEIPT:
        raise DecodeError("held-state receipt does not point at the public projection")
    if receipt["verification"]["componentReceiptSHA256"] != HISTORICAL_RECEIPT:
        raise DecodeError("historical anchor text is not the published 89462eec digest")
    file_hashes = {sha256_bytes((root / name).read_bytes()) for name in files}
    historical_in_package = HISTORICAL_RECEIPT in file_hashes
    if receipt["source"]["finalWeightedTerms"] != FINAL_WEIGHTED_TERMS:
        raise DecodeError("receipt final weighted terms are not the stated 1,2 / 9,13 labels")

    for name, size, digest in value_files["files"]:
        data = (root / name).read_bytes()
        if len(data) != size or sha256_bytes(data) != digest:
            raise DecodeError(f"value-files.json mismatch for {name}")

    permuted = hashlib.sha256()
    permuted_rows = 0
    # Rebuild the dense grid from decoded planes. Traversal here is the permuted
    # convention, and the hash is NOT re-sorted into lexicographic order.
    planes = []
    for frame in chained:
        header = frame["header"]
        planes.append(list(iter_trits(frame["payload"], header["digits"])))
    volume = 1
    for size in shape:
        volume *= size
    for index in range(volume):
        q0, q1, q2, q3 = coords_first_fastest(index, shape)
        local = coords_last_fastest_index((q1, q2, q3), plane_shape)
        trit = planes[q0][local]
        if trit:
            permuted.update(row_line(logical_exponent((q0, q1, q2, q3)), trit))
            permuted_rows += 1
    if permuted_rows != nonzero:
        raise DecodeError("permuted traversal dropped or duplicated a nonzero row")
    permuted_digest = permuted.hexdigest()
    if permuted_digest == row_digest:
        raise DecodeError("permuted traversal produced the same row hash")

    return {
        "files": len(files),
        "frames": len(chained),
        "nonzero": nonzero,
        "ones": ones,
        "twos": twos,
        "trits": trit_count,
        "padding_trits": padding_trits,
        "padding_bits": padding_bits,
        "row_sha256": row_digest,
        "spaced_row_sha256": spaced_hash.hexdigest(),
        "permuted_row_sha256": permuted_digest,
        "quotient_degree": [degree_min, degree_max],
        "logical_degree": [logical_degree_min, logical_degree_max],
        "logical_axis_min": logical_axis_min,
        "logical_axis_max": logical_axis_max,
        "batches": batch_sizes,
        "historical_bytes_in_package": historical_in_package,
        "final_weighted_terms": receipt["source"]["finalWeightedTerms"],
        "first_row": logical_rows[0],
        "last_row": logical_rows[-1],
    }


def coords_last_fastest_index(coords: tuple[int, ...], shape: tuple[int, ...]) -> int:
    index = 0
    stride = 1
    for axis in range(len(shape) - 1, -1, -1):
        index += coords[axis] * stride
        stride *= shape[axis]
    return index


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: decode_component.py PACKAGE_DIR", file=sys.stderr)
        return 2
    try:
        report = decode_package(Path(argv[1]))
    except DecodeError as exc:
        print(f"fail: {exc}")
        return 1
    print("pass")
    for key in (
        "files",
        "frames",
        "nonzero",
        "ones",
        "twos",
        "trits",
        "padding_trits",
        "padding_bits",
        "row_sha256",
        "spaced_row_sha256",
        "permuted_row_sha256",
        "quotient_degree",
        "logical_degree",
        "logical_axis_min",
        "logical_axis_max",
        "batches",
        "historical_bytes_in_package",
        "final_weighted_terms",
        "first_row",
        "last_row",
    ):
        print(f"{key}: {report[key]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
