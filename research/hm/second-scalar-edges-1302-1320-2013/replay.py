#!/usr/bin/env python3
"""Replay three supplied exact quotients; never evaluate a source DAG/checkpoint."""
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROLES = ((1, 3, 0, 2), (1, 3, 2, 0), (2, 0, 1, 3))
EXPECTED = (F(407, 8), F(-353, 4), F(-41517, 16))
MAP = 'X02[0,5]-X13[10,1]'
M = [2, 2, 2, 0]
SHAPE = [9, 44, 23]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value):
    require(type(value) is str, 'Integers must be canonical decimal strings')
    result = int(value)
    require(str(result) == value, 'Noncanonical integer')
    return result


def enc(value):
    return [str(value.numerator), str(value.denominator)]


def rat(value):
    require(type(value) is list and len(value) == 2, 'Invalid rational pair')
    n, d = map(integer, value)
    require(d > 0, 'Nonpositive denominator')
    result = F(n, d)
    require(enc(result) == value, 'Unreduced rational')
    return result


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'Duplicate JSON key')
        result[key] = value
    return result


def load(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=unique)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify_manifest(directory):
    directory = Path(directory)
    require(not (directory / 'manifest.json').is_symlink(), 'Symlinked manifest')
    manifest = load(directory / 'manifest.json')
    require(manifest['schema'] == 'second-scalar-edges-1302-1320-2013-manifest-v1', 'Manifest schema')
    files = manifest['files']
    require(set(files) == {'README.md', 'contributions.json', 'replay.py', 'test_replay.py'}, 'Manifest file set')
    require({p.name for p in directory.iterdir()} - {'__pycache__'} == set(files) | {'manifest.json'}, 'Unexpected package entry')
    for name, record in files.items():
        p = directory / name
        require(p.is_file() and not p.is_symlink(), 'Invalid package file')
        require(record == {'sha256': sha(p), 'bytes': p.stat().st_size}, 'Package digest mismatch')


def kernel():
    """Exact binomial expansion of G(T,z)^(-70) modulo (T^9,z^23)."""
    h = {(0, 1): 1, (1, 0): 1, (1, 1): 3, (1, 2): 1, (2, 1): 1, (2, 2): 1}
    answer = {(0, 0): 1}
    power = {(0, 0): 1}
    for n in range(1, 32):
        following = {}
        for (a, b), c in power.items():
            for (i, j), d in h.items():
                if a + i < 9 and b + j < 23:
                    key = (a + i, b + j)
                    following[key] = following.get(key, 0) + c * d
        power = following
        factor = (-1) ** n * comb(69 + n, n)
        for key, c in power.items():
            answer[key] = answer.get(key, 0) + factor * c
    require(not power, 'Nilpotence bound failed')
    return answer


def verify_edge(edge, roles, expected, weights):
    require(edge['roles'] == list(roles) and all(type(x) is int for x in edge['roles']), 'Wrong orientation')
    require(edge['shape'] == SHAPE and all(type(x) is int for x in edge['shape']), 'Wrong quotient shape')
    require(edge['homogeneous_degrees_separated'] is True and edge['pairing_aggregated'] is False, 'Lost grading')
    require(integer(edge['common_denominator']) == 64, 'Wrong denominator')
    terms = edge['integer_coefficients']
    require(type(terms) is list and len(terms) == 233, 'Wrong term count')
    require(hashlib.sha256(json.dumps(terms, separators=(',', ':')).encode()).hexdigest() == edge['coefficient_array_sha256'], 'Coefficient digest mismatch')
    values, slots = {}, []
    for row in terms:
        require(type(row) is list and len(row) == 4, 'Malformed quotient row')
        slot = tuple(row[:3])
        require(all(type(x) is int and 0 <= x < bound for x, bound in zip(slot, SHAPE)), 'Invalid quotient slot')
        c = integer(row[3])
        require(c != 0 and slot not in values, 'Duplicate/zero quotient term')
        values[slot] = F(c, 64)
        slots.append(slot)
    require(slots == sorted(slots), 'Unsorted quotient')
    sign = (-1) ** sum(roles[a] > roles[b] for a in range(4) for b in range(a + 1, 4))
    require(type(edge['permutation_sign']) is int and edge['permutation_sign'] == sign, 'Wrong permutation sign')
    i, j, k, l = roles
    d, low, homogeneous = 6 + M[j], 22 - M[l], 35 + sum(M)
    derived = []
    for r in range(d + 1):
        for ell in range(low + 1):
            slot = [r, homogeneous, ell]
            c = values.get(tuple(slot), F(0))
            weight = weights[d-r, low-ell]
            exponents = [0] * 4
            exponents[i], exponents[j], exponents[k], exponents[l] = 272, 215-r, 157-sum(M)+r-ell, 47+ell
            require(sum(exponents) == 685, 'Physical grading mismatch')
            derived.append({'slot': slot, 'source_exponents': exponents, 'kernel_weight': str(weight),
                            'coefficient': enc(c), 'weighted_contribution': enc(c * weight)})
    for row in edge['rows']:
        require(all(type(x) is int for x in row['slot'] + row['source_exponents']), 'Invalid selector indices')
        integer(row['kernel_weight'])
        rat(row['coefficient'])
        rat(row['weighted_contribution'])
    require(edge['rows'] == derived, 'Selector rows differ from exact derivation')
    value = sign * sum((rat(r['weighted_contribution']) for r in derived), F(0))
    require(value == rat(edge['signed_contribution']) == expected, 'Contribution mismatch')
    provenance = edge['source_provenance']
    require(set(provenance) == {'original_quotient_sha256', 'original_result_sha256',
        'original_completion_receipt_sha256', 'configuration_sha256', 'execution_plan_sha256',
        'terminal_checkpoint_sha256', 'recorded_independent_terminal_reconstruction_pass',
        'source_nodes_reevaluated_by_original_completion_audit'}, 'Wrong provenance fields')
    require(provenance['recorded_independent_terminal_reconstruction_pass'] is True, 'Missing recorded audit')
    require(type(provenance['source_nodes_reevaluated_by_original_completion_audit']) is int and
            provenance['source_nodes_reevaluated_by_original_completion_audit'] == 0, 'Wrong historical audit scope')
    for key, value_ in provenance.items():
        if key.endswith('_sha256'):
            require(type(value_) is str and len(value_) == 64 and all(c in '0123456789abcdef' for c in value_), 'Invalid provenance digest')
    return {'roles': list(roles), 'signed_contribution': enc(value), 'quotient_terms': len(terms),
            'selector_rows': len(derived), 'nonzero_selected_coefficients': sum(rat(r['coefficient']) != 0 for r in derived)}


def verify(data):
    expected_metadata = {'schema': 'second-scalar-edges-1302-1320-2013-v1', 'scalar_map': MAP,
        'field': 'Q', 'pairing_monomial': M, 'active_target_orientations': 18,
        'package_target_orientations': 3, 'previously_published_orientations':
        [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1],
         [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3],
         [1, 0, 3, 2], [1, 2, 0, 3], [1, 2, 3, 0]],
        'cumulative_published_orientations': 13, 'remaining_after_these_and_pr43_pr46_pr50_pr51': 5,
        'complete_scalar_pairing_computed': False, 'full_obstruction_computed': False,
        'source_attribution_reproduced': False}
    require({k: v for k, v in data.items() if k != 'edges'} == expected_metadata, 'Wrong target/scope metadata')
    require(all(type(data[k]) is int for k in ('active_target_orientations', 'package_target_orientations',
                'remaining_after_these_and_pr43_pr46_pr50_pr51', 'cumulative_published_orientations')), 'Invalid coverage counts')
    require(all(type(x) is int for x in data['pairing_monomial'] + [x for roles in data['previously_published_orientations'] for x in roles]), 'Invalid target indices')
    require(all(data[k] is False for k in ('complete_scalar_pairing_computed', 'full_obstruction_computed', 'source_attribution_reproduced')), 'Overbroad completion scope')
    require(len(data['edges']) == 3, 'Missing/extra edge')
    require(len([r for r in itertools.permutations(range(4)) if M[r[0]] == 2]) == 18, 'Active orientation count')
    covered = {tuple(roles) for roles in data['previously_published_orientations']} | set(ROLES)
    require(len(covered) == data['cumulative_published_orientations'] == 13, 'Overlapping coverage')
    require(18 - len(covered) == data['remaining_after_these_and_pr43_pr46_pr50_pr51'], 'Wrong remaining coverage')
    weights = kernel()
    results = [verify_edge(e, roles, value, weights) for e, roles, value in zip(data['edges'], ROLES, EXPECTED)]
    return {'status': 'PASS_SUPPLIED_QUOTIENT_REPLAY', 'edges': results,
            'cumulative_published_orientations': 13, 'remaining_after_these_and_pr43_pr46_pr50_pr51': 5, 'source_DAG_evaluated': False,
            'terminal_checkpoints_reconstructed': False, 'complete_scalar_pairing_computed': False,
            'full_obstruction_computed': False}


def replay(directory=HERE):
    verify_manifest(directory)
    return verify(load(Path(directory) / 'contributions.json'))


if __name__ == '__main__':
    print(json.dumps(replay(), indent=2))
