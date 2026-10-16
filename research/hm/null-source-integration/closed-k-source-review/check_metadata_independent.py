"""Read authenticated sparse metadata only; no polynomial or point evaluator.

This independent review checker compares bytes, finite supports, coefficient
records, exponent shifts, and maxima of exponents. It never multiplies source
polynomials, constructs a source transition, differentiates one, or substitutes
coordinate values. The rational-function proof is in REVIEW.md.
"""
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
EXPECTED_MODEL_SHA = '635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def records(poly):
    out = {}
    for label, coefficient in poly:
        exponent = tuple(int(e) for e in label.split(','))
        require(len(exponent) == 4, 'four-coordinate sparse record')
        require(exponent not in out, 'no duplicate exponent records')
        require(type(coefficient) is int and coefficient != 0, 'nonzero integer coefficient')
        out[exponent] = coefficient
    return out


def degree(poly):
    return max(e[0] for e in records(poly))


def leading_records(poly):
    d = degree(poly)
    return {e[1:]: c for e, c in records(poly).items() if e[0] == d}


def shifted(poly, amount):
    return {tuple(e[k] + amount[k] for k in range(4)): c
            for e, c in records(poly).items()}


def repository_root():
    if len(sys.argv) == 2:
        return Path(sys.argv[1]).resolve()
    if len(sys.argv) != 1:
        raise RuntimeError('Usage: python check_metadata_independent.py [repository-root]')
    for root in (HERE, *HERE.parents):
        if (root / 'research/hm/null-operator-compiler/hm-pinned-model.json').is_file():
            return root
    raise RuntimeError('Cannot locate pinned repository inputs; pass the repository root explicitly.')


def main():
    root = repository_root()
    pins = json.loads((HERE / 'source-pins.json').read_text())['files']
    provenance = []
    raw_by_role = {}
    record_by_role = {}
    for item in pins:
        raw = (root / item['path']).read_bytes()
        require(git_blob(raw) == item['git_blob'], 'pinned Git blob: ' + item['path'])
        require(sha256(raw) == item['sha256'], 'pinned SHA-256: ' + item['path'])
        provenance.append(item)
        if item['role'] != 'review_note':
            require(item['role'] not in raw_by_role, 'unique source role')
            raw_by_role[item['role']] = raw
            record_by_role[item['role']] = item
    require(len(pins) == 8, 'six reviewed files plus model and source formulas')
    model_raw = raw_by_role['model']
    model_public = record_by_role['model']
    formula_public = record_by_role['source_formulas']
    require(sha256(model_raw) == EXPECTED_MODEL_SHA, 'canonical model SHA-256')
    model = json.loads(model_raw)
    require(len(model['charts']) == 6, 'six source carriers')
    connections = []
    for c, chart in enumerate(model['charts']):
        for key in ('I', 'P'):
            for row in chart[key]:
                for polynomial in row:
                    records(polynomial)
        for key in ('di', 'dp'):
            records(chart[key])
        a, b = (c, c + 5) if c < 5 else (5, 14)
        support = [[r for r in range(15) if chart['P'][i][r] and chart['I'][r][j]]
                   for i in range(2) for j in range(2)]
        require(support == [[a], [], [], [b]], 'complete connection support')
        require(records(chart['I'][a][0]) == records(chart['di']), 'first I entry is 1')
        require(records(chart['P'][0][a]) == records(chart['dp']), 'first P entry is 1')
        if c < 5:
            shift = tuple(int(c == k + 1) for k in range(4))
            require(records(chart['I'][b][1]) == shifted(chart['di'], shift), 'primary I entry')
            require(records(chart['P'][1][b]) == shifted(chart['dp'], tuple(-n for n in shift)), 'primary P entry')
        else:
            require(records(chart['di']) == {(2, 0, 1, 1): -1}, 'auxiliary I denominator')
            require(records(chart['dp']) == {(2, 0, 1, 1): -1}, 'auxiliary P denominator')
            require(records(chart['I'][b][1]) == {(0, 0, 1, 2): 1}, 'auxiliary I entry')
            require(records(chart['P'][1][b]) == {(4, 0, 1, 0): 1}, 'auxiliary P entry')
        connections.append({'carrier': c, 'support_row_major': support})
    c0, c1 = model['charts'][:2]
    require(c0['pivot'] == 0 and c1['pivot'] == 1, 'carrier 0/1 pivots')
    require(records(c0['di']) == {(1, 1, 1, 1): 1, (0, 0, 0, 0): -1}, 'exact d0 records')
    require(records(c1['di']) == {(5, 0, 0, 0): -1, (1, 1, 1, 1): 1}, 'exact d1 records')
    require(c0['di'] == c0['dp'] and c1['di'] == c1['dp'], 'pair denominator equality')
    expected = {(0, 0): [(1, 1), (4, -2), (7, -1)],
                (0, 1): [(4, 0), (7, -1)],
                (1, 0): [(1, 0), (4, -4), (5, -2), (7, -2)],
                (1, 1): [(4, -2), (5, -2), (7, -2)]}
    bounds = {}
    for (i, j), wanted in expected.items():
        actual = [(r, degree(c0['P'][i][r]) + degree(c1['I'][r][j])
                      - degree(c0['dp']) - degree(c1['di']))
                  for r in range(15) if c0['P'][i][r] and c1['I'][r][j]]
        require(actual == wanted, 'complete transition support-degree table')
        bounds[f'{i}{j}'] = actual
    require(leading_records(c0['P'][0][4]) == {(1, 0, 1): -1}, 'K01 first leading record')
    require(leading_records(c1['I'][4][1]) == {(1, 0, 1): 1}, 'K01 second leading record')
    require(leading_records(c0['P'][1][1]) == {(0, 2, 0): -1}, 'K10 first leading record')
    require(c1['I'][1][0] == c1['di'], 'K10 second factor is 1')
    receipt = {'status': 'PASS', 'source_values_evaluated': False,
               'source_polynomial_evaluator_used': False, 'source_point_selected': False,
               'source_transitions_constructed': False, 'source_jets_constructed': False,
               'omega_rerun': False, 'model_sha256': EXPECTED_MODEL_SHA,
               'model_git_blob': model_public['git_blob'], 'formula_git_blob': formula_public['git_blob'],
               'review_inputs': provenance, 'connections': connections,
               'transition_support_degree_bounds': bounds}
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
