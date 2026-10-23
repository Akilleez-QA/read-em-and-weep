"""Synthetic bounded fixtures only: no source2 realization or actual HM data."""

from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
import unittest

import template


# Independent mathematical inventory, deliberately not derived from compiler constants.
BLOCKS = {2: {"A": 1, "V": 2, "P": 3, "D": 4},
          3: {"Wp": 3, "S": 3, "T": 6}, 4: {"V": 2, "P": 4, "D": 3}}
PAIRS = {"alpha": [("A", "S"), ("V", "T"), ("P", "Wp"),
                   ("P", "T"), ("D", "S"), ("D", "T")],
         "beta": [("Wp", "P"), ("S", "D"), ("T", "V"),
                  ("T", "P"), ("T", "D")]}
DIMS = {"A": 3, "V": 3, "P": 4, "D": 5, "Wp": 2, "S": 4, "T": 6}


def apply(data, values, x):
    return [sum(x[col] * (constant + sum(values[s] * c for s, c in terms))
                for col, constant, terms in row["entries"]) for row in data["rows"]]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


class TemplateTests(unittest.TestCase):
    def setUp(self):
        self.data = template.compile_template()

    def test_inventory(self):
        d = self.data
        self.assertEqual(d["delta_shape"], [153, 113])
        self.assertEqual(d["augmented_shape"], [156, 113])
        expected_columns = [dict(vertex=v, rep=r, i=i, j=j)
                            for v, blocks in BLOCKS.items() for r, n in blocks.items()
                            for i in range(n) for j in range(n)]
        self.assertEqual(d["columns"], expected_columns)
        self.assertEqual(len(d["columns"]), 113)
        self.assertEqual(len(d["rows"]), 156)
        self.assertEqual(len(d["symbols"]), 153)
        self.assertEqual(len({s["name"] for s in d["symbols"]}), 153)
        for arrow, v, total in (("alpha", 2, 78), ("beta", 3, 75)):
            channels = [c for c in d["channels"] if c["arrow"] == arrow]
            self.assertEqual([(c["source_rep"], c["target_rep"]) for c in channels], PAIRS[arrow])
            self.assertEqual(sum(c["shape"][0]*c["shape"][1] for c in channels), total)
            for c in channels:
                self.assertEqual((c["source"], c["target"]), (v, v+1))
                self.assertEqual(c["shape"], [BLOCKS[v+1][c["target_rep"]], BLOCKS[v][c["source_rep"]]])
        cursor = 0
        for index, c in enumerate(d["channels"]):
            self.assertEqual((c["symbol_start"], c["row_start"]), (cursor, cursor))
            for i in range(c["shape"][0]):
                for j in range(c["shape"][1]):
                    self.assertEqual(d["symbols"][cursor], dict(
                        name=f'{c["arrow"]}_{c["source_rep"]}_{c["target_rep"]}_{i}_{j}',
                        channel=index, i=i, j=j))
                    row = d["rows"][cursor]
                    self.assertEqual({k: row[k] for k in ("kind", "channel", "i", "j")},
                                     dict(kind="channel", channel=index, i=i, j=j))
                    cursor += 1
        self.assertEqual([r["vertex"] for r in d["rows"][153:]], [2, 3, 4])

    def test_independent_rectangular_products(self):
        d = self.data
        for seed in range(3):
            values = [Fraction((k*7 + seed*3) % 11 - 5, seed+1)
                      for k in range(153)]
            # Sweep every coordinate to detect sign, indexing and transpose errors.
            for active in range(113):
                x = [int(k == active) for k in range(113)]
                blocks = {(v, r): [[0]*n for _ in range(n)]
                          for v, rs in BLOCKS.items() for r, n in rs.items()}
                for col, value in zip(d["columns"], x):
                    blocks[col["vertex"], col["rep"]][col["i"]][col["j"]] = value
                expected = []
                cursor = 0
                for arrow, v in (("alpha", 2), ("beta", 3)):
                    for r, s in PAIRS[arrow]:
                        m, n = BLOCKS[v+1][s], BLOCKS[v][r]
                        c = [values[cursor+i*n:cursor+(i+1)*n] for i in range(m)]
                        cursor += m*n
                        left = multiply(blocks[v+1, s], c)
                        right = multiply(c, blocks[v, r])
                        expected.extend(left[i][j]-right[i][j] for i in range(m) for j in range(n))
                expected.extend(sum(DIMS[r]*sum(blocks[v, r][i][i] for i in range(n))
                                    for r, n in rs.items()) for v, rs in BLOCKS.items())
                self.assertEqual(apply(d, values, x), expected)

    def test_formal_identity_and_canonicalization(self):
        d = self.data
        identity = [int(c["i"] == c["j"]) for c in d["columns"]]
        for row in d["rows"][:153]:
            terms = [(s, c*identity[col]) for col, constant, ts in row["entries"] for s, c in ts]
            self.assertEqual(template.canonical_terms(terms), [])
        self.assertEqual(apply(d, [0]*153, identity), [0]*153 + [41, 54, 37])
        self.assertEqual(template.canonical_terms([(7, 2), (1, -3), (7, -2), (1, 1)]), [[1, -2]])
        for row in d["rows"]:
            self.assertEqual([e[0] for e in row["entries"]], sorted({e[0] for e in row["entries"]}))
            for col, constant, terms in row["entries"]:
                self.assertEqual(terms, template.canonical_terms(terms))
                self.assertTrue(constant or terms)
        d["columns"].clear()
        self.assertEqual(len(template.compile_template()["columns"]), 113)

    def test_cli_and_inert_import(self):
        folder = Path(__file__).resolve().parent
        imported = subprocess.run([sys.executable, "-B", "-c",
            "import sys\n"
            "def guard(frame, event, arg):\n"
            "    if event == 'call' and frame.f_code.co_name in "
            "('compile_template', 'canonical_terms', 'main'):\n"
            "        raise AssertionError('computation during import')\n"
            "sys.setprofile(guard)\n"
            "import template\n"],
            cwd=folder, capture_output=True, check=True)
        self.assertEqual(imported.stdout, b"")
        self.assertEqual(imported.stderr, b"")
        command = [sys.executable, "-B", str(folder / "template.py"), "emit-json"]
        first = subprocess.check_output(command)
        self.assertEqual(first, subprocess.check_output(command))
        self.assertEqual(json.loads(first), self.data)
        self.assertEqual(first.decode(), json.dumps(self.data, sort_keys=True, separators=(",", ":")) + "\n")


if __name__ == "__main__":
    unittest.main()
