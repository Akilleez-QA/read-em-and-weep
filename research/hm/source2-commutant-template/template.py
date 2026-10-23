"""Universal formal commutant template; no tensor specialization or rank code."""

import argparse
import json
import sys


SPACES = ((2, (("A", 1), ("V", 2), ("P", 3), ("D", 4))),
          (3, (("Wp", 3), ("S", 3), ("T", 6))),
          (4, (("V", 2), ("P", 4), ("D", 3))))
EDGES = {"A": ("W", "S"), "V": ("T",), "P": ("Wp", "T"),
         "D": ("S", "T"), "Wp": ("P",), "S": ("A", "D"),
         "T": ("D", "V", "P")}
DIMENSIONS = {"A": 3, "V": 3, "P": 4, "D": 5, "Wp": 2, "S": 4, "T": 6}


def canonical_terms(terms):
    """Combine integer coefficients of symbol indices, dropping zeros."""
    combined = {}
    for symbol, coefficient in terms:
        combined[symbol] = combined.get(symbol, 0) + coefficient
    return [[symbol, coefficient] for symbol, coefficient in sorted(combined.items())
            if coefficient]


def compile_template():
    """Return fresh JSON-compatible metadata and sparse rows, deterministically."""
    columns, symbols, channels, rows = [], [], [], []
    column_index = {}
    for vertex, blocks in SPACES:
        for rep, size in blocks:
            for i in range(size):
                for j in range(size):
                    column_index[vertex, rep, i, j] = len(columns)
                    columns.append(dict(vertex=vertex, rep=rep, i=i, j=j))

    for arrow, (source, sources), (target, targets) in (
            ("alpha", SPACES[0], SPACES[1]), ("beta", SPACES[1], SPACES[2])):
        for r, n in sources:
            for s, m in targets:
                if s not in EDGES[r]:
                    continue
                channel = len(channels)
                start = len(symbols)
                channels.append(dict(arrow=arrow, source=source, target=target,
                                     source_rep=r, target_rep=s, shape=[m, n],
                                     symbol_start=start, row_start=len(rows)))
                for i in range(m):
                    for j in range(n):
                        symbols.append(dict(name=f"{arrow}_{r}_{s}_{i}_{j}",
                                            channel=channel, i=i, j=j))
                for i in range(m):
                    for j in range(n):
                        terms = {}

                        def add(col, symbol, sign):
                            terms.setdefault(col, []).append((symbol, sign))

                        for k in range(m):
                            add(column_index[target, s, i, k], start + k*n + j, 1)
                        for k in range(n):
                            add(column_index[source, r, k, j], start + i*n + k, -1)
                        entries = []
                        for col, values in sorted(terms.items()):
                            coefficient = canonical_terms(values)
                            if coefficient:
                                entries.append([col, 0, coefficient])
                        rows.append(dict(kind="channel", channel=channel,
                                         i=i, j=j, entries=entries))
    for vertex, blocks in SPACES:
        entries = [[column_index[vertex, rep, i, i], DIMENSIONS[rep], []]
                   for rep, size in blocks for i in range(size)]
        rows.append(dict(kind="trace", vertex=vertex, entries=entries))
    return dict(format="source2-commutant-template-v1", delta_shape=[153, 113],
                augmented_shape=[156, 113], columns=columns, symbols=symbols,
                channels=channels, rows=rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["emit-json"])
    parser.parse_args()
    json.dump(compile_template(), sys.stdout, sort_keys=True, separators=(",", ":"))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
