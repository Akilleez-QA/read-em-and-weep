#!/usr/bin/env python3
"""Fixed offline byte authentication and small universal arithmetic, not proof.

No source-instance coefficients, parameters, points, jets, tensors, matrices,
eigenlines, scalar normalizations, or ranks are computed. All representations
below are fixed formal character types. No network, subprocess, search,
historical enumerator, external imports, or optional computation is available.
"""

from pathlib import Path
from collections import Counter
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
PROOF_SHA256 = "4819cebda47b3ef7a48ecbcb1fe01295a3a3a7ea7986df540421e1433d547b21"
PINS = (
    (1235, "first-kernel-span", "7152e94cedbab18036b5e032d4e97934c4c061b7",
     11977, "66f8040b87f3d193fbd7e6eecb42a1457a59aa6f2cf3f10f29e7ac7b1aa1b6c9",
     "b846834f8451e7202721d9669b43df294f7a96d3"),
    (1236, "first-kernel-forward-closure", "092fc5f31dfaa5553ee5ea687f175ecba1878a2a",
     18052, "90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137",
     "f77cfb52743be86e46e0c40570ec036e69aebaf3"),
    (1240, "orthogonal-top-incidence", "3fbaa182b1aceb6915be88088ef158d6d15e34fb",
     28094, "407d35049bb17ab4b8f4e270627adb416fc5601eab1445a21685f2cc27bcb637",
     "f00b059695615d9b8ab6d315798940e3ab0a58d4"),
    (1207, "shared-d-gluing", "af136934955f1bcc700ee768e2debb983e75451d",
     20361, "7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7",
     "3d051410e80a33f1c4d78d3403bb186595bb72c3"),
    (1241, "f18-row-resolution", "fc43b0a6da1fc5e281284fc3b09e46acb97bec95",
     15616, "cd28b6dba69d23ef905f4816dcd1a7a3165bd8b337169ab0a6acb10a15ac06dc",
     "429c462fe6ba5f2b99770b9cabb35440130c807b"),
)
CORE = {"PROOF.md", "README.md", "INPUTS.json", "INPUTS.md",
        "PROVENANCE.md", "verify.py"} | {"inputs/" + p[1] + ".md" for p in PINS}
REPOSITORY = "Akilleez-QA/read-em-and-weep"
checks = 0


def require(condition, message):
    global checks
    if not condition:
        raise RuntimeError(message)
    checks += 1


def same(actual, expected, message):
    require(actual == expected, message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def authenticate():
    frozen = json.loads((ROOT / "FROZEN.json").read_text(encoding="utf-8"))
    same(frozen["schema"], 1, "frozen schema")
    records = frozen["files"]
    same(set(records), CORE, "exact eleven-file frozen core")
    for path in sorted(CORE):
        data = (ROOT / path).read_bytes()
        data.decode("utf-8", errors="strict")
        same(len(data), records[path]["bytes"], "frozen byte length: " + path)
        same(sha256(data), records[path]["sha256"], "frozen SHA256: " + path)
        same(git_blob(data), records[path]["git_blob_sha1"], "frozen Git blob: " + path)
    digest_rows = "".join(path + "\t" + records[path]["sha256"] + "\t" +
                          str(records[path]["bytes"]) + "\n" for path in sorted(CORE))
    same(sha256(digest_rows.encode("utf-8")), frozen["core_digest_sha256"], "core digest")
    same(sha256((ROOT / "PROOF.md").read_bytes()), PROOF_SHA256, "fixed full proof pin")
    metadata = json.loads((ROOT / "INPUTS.json").read_text(encoding="utf-8"))
    same(metadata["repository"], REPOSITORY, "input repository")
    entries = metadata["complete_direct_originals"]
    same(len(entries), 5, "five complete direct originals")
    for entry, pin in zip(entries, PINS):
        pr, name, commit, size, digest, blob = pin
        path = "research/hm/rankfour-profile11-triplet-" + name + "/PROOF.md"
        local_path = "inputs/" + name + ".md"
        data = (ROOT / local_path).read_bytes()
        same((len(data), sha256(data), git_blob(data)), (size, digest, blob), "source bytes: " + name)
        for key, value in {"pr": pr, "commit": commit, "path": path,
                           "repository": REPOSITORY, "local_path": local_path,
                           "bytes": size, "sha256": digest, "git_blob_sha1": blob}.items():
            same(entry[key], value, "source metadata: " + name + "/" + key)
        same(entry["source_url"], "https://github.com/" + REPOSITORY + "/blob/" + commit + "/" + path,
             "immutable source URL")
        same(entry["file_call"]["arguments"], {"repository_full_name": REPOSITORY,
             "path": path, "ref": commit, "encoding": "base64"}, "exact file call")
        same(entry["blob_call"]["arguments"], {"repository_full_name": REPOSITORY,
             "blob_sha": blob}, "exact independent blob call")
        same(entry["file_call"]["tool"], "mcp__codex_apps__github_fetch_file", "file tool")
        same(entry["blob_call"]["tool"], "mcp__codex_apps__github_fetch_blob", "blob tool")
        require(entry["file_blob_utf8_bytes_equal"] is True, "recorded complete byte equality")
        for kind in ("file_call", "blob_call"):
            call = entry[kind]
            require(call["started_at"].endswith("Z") and call["completed_at"].endswith("Z"), "UTC retrieval")
            require(call["started_at"] <= call["completed_at"], "retrieval order")
        require(entry["file_call"]["completed_at"] <= entry["blob_call"]["started_at"], "returned-blob order")
    return frozen["core_digest_sha256"]


# The fixed physical McKay character multiplication by W, not an evaluated
# source tensor. These nine small formal rules are retained source data.
DIM = {"1": 1, "W": 2, "A": 3, "S4": 4, "D": 5, "T6": 6,
       "V": 3, "P": 4, "Wp": 2}
W_RULE = {"1": ("W",), "W": ("1", "A"), "A": ("W", "S4"),
          "S4": ("A", "D"), "D": ("S4", "T6"),
          "T6": ("D", "V", "P"), "V": ("T6",),
          "P": ("T6", "Wp"), "Wp": ("P",)}


def clean(value):
    return Counter({k: v for k, v in value.items() if v != 0})


def minus(a, b):
    return clean({k: a[k] - b[k] for k in DIM})


def times_w(value):
    result = Counter()
    for name, multiplicity in value.items():
        for target in W_RULE[name]:
            result[target] += multiplicity
    return clean(result)


def times_h(value, degree):
    require(0 <= degree <= 12, "fixed universal degree bound")
    if degree == 0:
        return value
    before, current = value, times_w(value)
    for _ in range(2, degree + 1):
        before, current = current, minus(times_w(current), before)
    return current


def universal_arithmetic():
    for name in DIM:
        same(sum(DIM[t] for t in W_RULE[name]), 2 * DIM[name], "formal W dimension")
        for target in W_RULE[name]:
            require(name in W_RULE[target], "fixed self-dual fusion reciprocity")
    H = [times_h(Counter({"1": 1}), n) for n in range(13)]
    for n, expected in {0: {"1": 1}, 1: {"W": 1}, 2: {"A": 1},
                        3: {"S4": 1}, 4: {"D": 1}, 5: {"T6": 1},
                        6: {"V": 1, "P": 1},
                        12: {"1": 1, "A": 1, "D": 1, "P": 1}}.items():
        same(H[n], Counter(expected), "fixed symmetric-power identity")
    same(times_h(Counter({"Wp": 1}), 3), Counter({"D": 1, "V": 1}), "Wp tensor H3")
    same(times_h(Counter({"V": 1}), 2), Counter({"P": 1, "D": 1}), "V tensor A")
    same(times_w(Counter({"T6": 1})), Counter({"D": 1, "V": 1, "P": 1}), "W tensor T6")
    same(times_w(Counter({"D": 1})), Counter({"S4": 1, "T6": 1}), "W tensor D")
    same(times_w(Counter({"Wp": 1})), Counter({"P": 1}), "W tensor Wp")
    same([H[n]["V"] for n in range(6)], [0] * 6, "first V occurrence bound")
    same([H[n]["D"] for n in range(4)], [0] * 4, "first D occurrence bound")
    same(times_w(Counter({"D": 1}))["Wp"], 0, "canonical N Hom vanishing")
    same(times_w(H[5])["D"], 1, "quartic quotient Hom multiplicity")
    same(times_h(Counter({"V": 1}), 2)["D"], 1, "D row Hom multiplicity")
    same(Counter({"D": 1, "V": 1}) & Counter({"A": 1, "P": 1}), Counter(), "pure Z coefficient span")
    same(max(-(-1) - 1, 0), 0, "H1 O(-1) vanishes")
    same(max(-(-2) - 1, 0), 1, "H1 O(-2) is one dimensional")
    same(max(-0 - 1, 0), 0, "H1 O vanishes")
    same(max(-1 + 1, 0), 0, "H0 O(-1) vanishes")
    same(3 * 2, 6, "universal maximal-minor degree")
    require(6 < 12, "invariant-divisor degree gap")
    require(-2 > -6 and -4 > -6, "universal d image-degree contradictions")
    same(6 + 4, 10, "universal b kernel-line degree bound")
    require(10 - 12 > -6, "universal b rank-two degree contradiction")
    same(2 * (-5) + 2 * (-3), 4 * (-4), "Euler formal degree")
    same(3 * (-4) + 2 * (-5) + 6 * (-5) + 2 * 3, -46, "R11 quotient formal degree")
    same(6 * (-3) + (3 + 4) * (-4), -46, "R13 type formal degree")
    same(5 * (-2) + (2 + 6) * (-3), -34, "F18 type formal degree")
    same(-34 - (-46), 12, "modification determinant degree")
    same(3 * 0 - 3 * (-4), 12, "T row determinant degree")
    same(10 - 4, 6, "complete order-three annihilator character degree")
    same((10 - 4 + 1) * (-4), -28, "complete order-three annihilator bundle degree")
    same((-6) - (-18), 12, "top symbol divisor degree")
    same((-4) - 2, -6, "complete sigma2 line degree")
    # With invariant orbit minimum twelve, determinant degree twelve admits
    # a single simple orbit. No actual orbit or local module is evaluated.
    same(12 // 12, 1, "universal orbit multiplicity degree")


def main():
    require(len(sys.argv) == 1, "no optional inputs or computation modes")
    core_digest = authenticate()
    universal_arithmetic()
    print(json.dumps({"status": "PASS", "runtime_checks": checks,
                      "complete_direct_originals": 5,
                      "core_digest_sha256": core_digest,
                      "boundary": "byte authentication and small universal arithmetic only; checker is not proof"},
                     sort_keys=True))


if __name__ == "__main__":
    main()
