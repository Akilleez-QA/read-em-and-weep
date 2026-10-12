#!/usr/bin/env python3
"""Discriminators for the supplied residue-41 package.

Each package mutation is applied only to a temporary copy. The copy is checked
with this audit's decoder and with the unchanged package command
`python3 -I -S -B verify_component.py .`. This file does not import the
package verifier.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def load_decoder():
    path = Path(__file__).resolve().parent / "decode_component.py"
    spec = importlib.util.spec_from_file_location("hsd_decode_component", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load decode_component.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


decoder_mod = load_decoder()
EXPECTED_ROW_HASH = decoder_mod.EXPECTED_ROW_HASH
DecodeError = decoder_mod.DecodeError
canonical_json = decoder_mod.canonical_json
coords_last_fastest = decoder_mod.coords_last_fastest
iter_trits = decoder_mod.iter_trits
logical_exponent = decoder_mod.logical_exponent
residue_code = decoder_mod.residue_code
row_line = decoder_mod.row_line


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
PACKAGE = REPO / "research" / "hm" / "f3-cartier-component-23615-r41"
DECODER = HERE / "decode_component.py"
PYTHON = sys.executable


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def decoder(package: Path) -> subprocess.CompletedProcess[str]:
    return run([PYTHON, "-I", "-S", "-B", str(DECODER), str(package)], package.parent)


def verifier(package: Path) -> subprocess.CompletedProcess[str]:
    return run([PYTHON, "-I", "-S", "-B", "verify_component.py", "."], package)


def one_line(text: str) -> str:
    line = " ".join(text.split())
    return line[:500]


def split_frame(raw: bytes) -> tuple[dict, bytearray, bytes]:
    if raw[:9] != b"F3SLICE1\n":
        raise RuntimeError("frame magic missing on the copy")
    size = int.from_bytes(raw[9:13], "big")
    header = json.loads(raw[13:13 + size].decode("ascii"))
    payload = bytearray(raw[13 + size:])
    return header, payload, raw


def write_frame(path: Path, header: dict, payload: bytes) -> None:
    raw_header = canonical_json(header)
    blob = b"F3SLICE1\n" + len(raw_header).to_bytes(4, "big") + raw_header + payload
    path.write_bytes(blob)


def first_chain_frame(root: Path) -> Path:
    receipt = json.loads((root / "component-receipt.json").read_text(encoding="ascii"))
    digest = receipt["store"]["orderedFrameSHA256"][0]
    return root / "frames" / f"{digest}.f3s"


def logical_digest(root: Path) -> str:
    """Hash decoded nonzero logical rows, ignoring filename and claim pins."""
    receipt = json.loads((root / "component-receipt.json").read_text(encoding="ascii"))
    spec = json.loads((root / "spec.json").read_text(encoding="ascii"))
    plane = tuple(spec["shape"][1:])
    digest = hashlib.sha256()
    for name in receipt["store"]["orderedFrameSHA256"]:
        raw = (root / "frames" / f"{name}.f3s").read_bytes()
        header, payload, _raw = split_frame(raw)
        x0 = header["x0"]
        for local, trit in enumerate(iter_trits(payload, header["digits"])):
            if trit == 0:
                continue
            local_coords = coords_last_fastest(local, plane)
            exponent = logical_exponent((x0, *local_coords))
            digest.update(row_line(exponent, trit))
    return digest.hexdigest()


def flip_data_trit(root: Path) -> str:
    path = first_chain_frame(root)
    header, payload, _raw = split_frame(path.read_bytes())
    plane = (28, 29, 29)
    x0 = header["x0"]
    for local, trit in enumerate(iter_trits(payload, header["digits"])):
        if trit != 1:
            continue
        coords = (x0, *coords_last_fastest(local, plane))
        shift = 2 * (local % 4)
        payload[local // 4] ^= 1 << shift
        write_frame(path, header, bytes(payload))
        return f"flipped the low bit of coefficient 1 at quotient {coords}"
    raise RuntimeError("no coefficient-1 trit in the first frame")


def flip_padding_bit(root: Path) -> str:
    """Expose the spec's padding bits, then flip one.

    Every supplied frame has 23548 digits, a multiple of 4, so the supplied
    bytes contain no padding bit. Setting digits to 23547 makes the high pair
    of the last byte padding. That pair is 00 on the first frame; bit 6 is
    then flipped.
    """
    path = first_chain_frame(root)
    header, payload, _raw = split_frame(path.read_bytes())
    if header["digits"] != 23548 or (payload[-1] >> 6) != 0:
        raise RuntimeError("first frame does not have a zero final pair")
    header["digits"] = 23547
    payload[-1] ^= 1 << 6
    write_frame(path, header, bytes(payload))
    try:
        list(iter_trits(payload, header["digits"]))
    except DecodeError as exc:
        return f"digits 23548->23547 and flipped bit 6 of the last byte ({exc})"
    raise RuntimeError("padding rule accepted the flipped padding bit")


def alter_header_field(root: Path) -> str:
    path = first_chain_frame(root)
    header, payload, _raw = split_frame(path.read_bytes())
    header["ones"] = header["ones"] + 1
    write_frame(path, header, bytes(payload))
    return "incremented header field ones by 1 on the first frame"


def swap_two_frames(root: Path) -> str:
    receipt = json.loads((root / "component-receipt.json").read_text(encoding="ascii"))
    first, second = receipt["store"]["orderedFrameSHA256"][:2]
    path_a = root / "frames" / f"{first}.f3s"
    path_b = root / "frames" / f"{second}.f3s"
    data_a = path_a.read_bytes()
    data_b = path_b.read_bytes()
    path_a.write_bytes(data_b)
    path_b.write_bytes(data_a)
    return "swapped the bytes of the first two chain frames without renaming them"


def check_padding_vectors() -> None:
    if list(iter_trits(b"\x24", 3)) != [0, 1, 2]:
        raise RuntimeError("three-trit vector did not decode to 0,1,2")
    if list(iter_trits(b"\x01", 1)) != [1]:
        raise RuntimeError("one-trit vector did not decode to 1")
    try:
        list(iter_trits(b"\x04", 1))
    except DecodeError:
        return
    raise RuntimeError("padding vector digits=1 body=0x04 was accepted")


def expect_reject(kind: str, mutate) -> dict:
    parent = Path(tempfile.mkdtemp(prefix=f"hsd-r41-{kind}-"))
    copy = parent / "package"
    shutil.copytree(PACKAGE, copy)
    detail = mutate(copy)
    mine = decoder(copy)
    theirs = verifier(copy)
    shutil.rmtree(parent)
    return {
        "mutation": detail,
        "decoder_exit": mine.returncode,
        "decoder": one_line(mine.stdout or mine.stderr),
        "verifier_exit": theirs.returncode,
        "verifier": one_line(theirs.stderr or theirs.stdout),
        "both_reject": mine.returncode != 0 and theirs.returncode != 0,
    }


def permuted_digest() -> str:
    result = decoder(PACKAGE)
    if result.returncode != 0:
        raise RuntimeError(result.stdout + result.stderr)
    for line in result.stdout.splitlines():
        if line.startswith("permuted_row_sha256:"):
            return line.split(": ", 1)[1]
    raise RuntimeError("decoder did not report the permuted hash")


def data_trit_hash_change() -> dict:
    parent = Path(tempfile.mkdtemp(prefix="hsd-r41-hash-"))
    copy = parent / "package"
    shutil.copytree(PACKAGE, copy)
    before = logical_digest(copy)
    flip_data_trit(copy)
    after = logical_digest(copy)
    shutil.rmtree(parent)
    return {"before": before, "after": after, "changed": before != after}


def main() -> int:
    if residue_code((2, 1, 1, 1)) != 41:
        print("convention residue failed")
        return 1
    check_padding_vectors()
    print("padding_vectors: pass")
    pristine_decoder = decoder(PACKAGE)
    pristine_verifier = verifier(PACKAGE)
    pristine_tests = run([PYTHON, "-I", "-S", "-B", "test_verify_component.py", "-f"], PACKAGE)
    print("pristine_decoder_exit:", pristine_decoder.returncode)
    print(pristine_decoder.stdout.rstrip())
    print("pristine_verifier_exit:", pristine_verifier.returncode)
    print(pristine_verifier.stdout.rstrip())
    print(pristine_verifier.stderr.rstrip())
    print("pristine_tests_exit:", pristine_tests.returncode)
    print(pristine_tests.stderr.rstrip() or pristine_tests.stdout.rstrip())
    hash_change = data_trit_hash_change()
    print("data_trit_stream:", json.dumps(hash_change))
    results = {
        "a": expect_reject("a", flip_data_trit),
        "b": expect_reject("b", flip_padding_bit),
        "c": expect_reject("c", alter_header_field),
        "d": expect_reject("d", swap_two_frames),
    }
    for key, item in results.items():
        print(f"mutation_{key}:", json.dumps(item, sort_keys=True))
    permuted = permuted_digest()
    print("permuted_row_sha256:", permuted)
    print("permuted_differs:", permuted != EXPECTED_ROW_HASH)
    failed = [key for key, item in results.items() if not item["both_reject"]]
    if pristine_decoder.returncode != 0 or pristine_verifier.returncode != 0 or pristine_tests.returncode != 0:
        failed.append("pristine")
    if not hash_change["changed"] or permuted == EXPECTED_ROW_HASH:
        failed.append("hash_discriminator")
    if failed:
        print("failed:", ",".join(failed))
        return 1
    print("discriminators: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
