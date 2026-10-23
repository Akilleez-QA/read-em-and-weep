"""Independent formal polynomial replay; no tensor assignment or rank test."""

import unittest
import template

blocks = {2: {"A": 1, "V": 2, "P": 3, "D": 4},
          3: {"Wp": 3, "S": 3, "T": 6},
          4: {"V": 2, "P": 4, "D": 3}}
dims = {"A": 3, "V": 3, "P": 4, "D": 5, "Wp": 2, "S": 4, "T": 6}
pairs = [(2, "A", "S"), (2, "V", "T"), (2, "P", "Wp"),
         (2, "P", "T"), (2, "D", "S"), (2, "D", "T"),
         (3, "Wp", "P"), (3, "S", "D"), (3, "T", "V"),
         (3, "T", "P"), (3, "T", "D")]
columns = [(v, r, i, j) for v, rs in blocks.items() for r, n in rs.items()
           for i in range(n) for j in range(n)]
assert len(columns) == 113


def padd(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0) + value
        if not out[key]:
            del out[key]
    return out


def pmul(a, b):
    # The direct rectangular products have one ordinary numeric factor.
    if isinstance(a, int):
        return {key: a * value for key, value in b.items() if a * value}
    assert isinstance(b, int)
    return {key: b * value for key, value in a.items() if b * value}


def multiply(a, b):
    out = [[{} for _ in b[0]] for _ in a]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                out[i][j] = padd(out[i][j], pmul(a[i][k], b[k][j]))
    return out


formal_channels = []
symbol = 0
for v, r, s in pairs:
    m, n = blocks[v + 1][s], blocks[v][r]
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append({symbol: 1})
            symbol += 1
        matrix.append(row)
    formal_channels.append((v, r, s, matrix))
assert symbol == 153

def verify(data):
    assert [(c["vertex"], c["rep"], c["i"], c["j"]) for c in data["columns"]] == columns
    actual = [{col: (constant, dict(terms)) for col, constant, terms in row["entries"]}
              for row in data["rows"]]
    checked = 0
    for active, (vertex, rep, ci, cj) in enumerate(columns):
        x = {(v, r): [[0] * n for _ in range(n)]
             for v, rs in blocks.items() for r, n in rs.items()}
        x[vertex, rep][ci][cj] = 1
        row_index = 0
        for v, r, s, c in formal_channels:
            left = multiply(x[v + 1, s], c)
            right = multiply(c, x[v, r])
            for i in range(len(c)):
                for j in range(len(c[0])):
                    expected = padd(left[i][j], {k: -val for k, val in right[i][j].items()})
                    assert actual[row_index].get(active, (0, {})) == (0, expected), (active, row_index)
                    checked += 1
                    row_index += 1
        assert row_index == 153
        for offset, v in enumerate(blocks):
            expected = dims[rep] if v == vertex and ci == cj else 0
            assert actual[153 + offset].get(active, (0, {})) == (expected, {})
            checked += 1

    return checked


class FormalReplayTests(unittest.TestCase):
    def test_all_independent_formal_coefficients(self):
        self.assertEqual(verify(template.compile_template()), 17628)

    def test_corruptions_are_rejected(self):
        for mode in ("sign", "symbol", "trace"):
            data = template.compile_template()
            if mode == "sign":
                data["rows"][0]["entries"][0][2][0][1] *= -1
            elif mode == "symbol":
                data["rows"][0]["entries"][0][2][0][0] += 1
            else:
                data["rows"][153]["entries"][0][1] += 1
            with self.subTest(mode=mode), self.assertRaises(AssertionError):
                verify(data)


if __name__ == "__main__":
    unittest.main()
