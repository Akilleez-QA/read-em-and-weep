#!/usr/bin/env python3
"""Replay all 18 supplied quotients for one selected L_minus coordinate; never evaluate a source DAG/checkpoint."""
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROLES = tuple(r for r in itertools.permutations(range(4)) if r[0] < 3)
EXPECTED = tuple(F(n, d) for n, d in (
    (8655, 16), (-2817, 16), (18831, 8), (-21601, 8), (1457, 8), (-803, 4),
    (15705, 16), (-5667, 16), (1953, 4), (-4313, 4), (407, 8), (-353, 4),
    (-41517, 16), (42869, 16), (-22917, 16), (21869, 16), (131, 2), (-169, 2)))
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
    require(manifest['schema'] == 'second-scalar-m2220-complete-manifest-v1', 'Manifest schema')
    files = manifest['files']
    require(set(files) == {'README.md', 'SOURCES.md', 'contributions.json', 'provenance.json', 'replay.py', 'test_replay.py'}, 'Manifest file set')
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
    require(type(terms) is list and len(terms) == (203 if roles[:2] in ((0, 1), (1, 0), (2, 3)) else 233), 'Wrong term count')
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
        'original_completion_receipt_sha256', 'configuration_sha256',
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
    expected_metadata = {'schema': 'second-scalar-m2220-complete-v1', 'scalar_map': 'X02[0,5]-X13[10,1]', 'field': 'Q', 'pairing_monomial': [2, 2, 2, 0], 'laurent_exponents': [-3, -3, -3, -1], 'active_target_orientations': 18, 'supplied_target_orientations': 18, 'remaining_target_orientations': 0, 'source_rows': 3258, 'distinct_source_exponents': 3258, 'nonzero_source_rows': 288, 'selected_coordinate': ['0', '1'], 'complete_selected_coordinate_replayed': True, 'whole_scalar_map_computed': False, 'full_obstruction_computed': False, 'source_attribution_reproduced': False}
    require({k: v for k, v in data.items() if k != 'edges'} == expected_metadata,
            'Wrong target/scope metadata')
    require(all(type(data[k]) is int for k in ('active_target_orientations',
        'supplied_target_orientations', 'remaining_target_orientations', 'source_rows',
        'distinct_source_exponents', 'nonzero_source_rows')), 'Invalid coverage counts')
    require(all(type(x) is int for x in data['pairing_monomial'] + data['laurent_exponents']),
            'Invalid target indices')
    require(data['complete_selected_coordinate_replayed'] is True, 'Selected coordinate scope')
    require(all(data[k] is False for k in ('whole_scalar_map_computed',
        'full_obstruction_computed', 'source_attribution_reproduced')), 'Overbroad scope')
    require(type(data['edges']) is list and len(data['edges']) == 18, 'Missing/extra edge')
    active = {r for r in itertools.permutations(range(4)) if M[r[0]] == 2}
    require(set(ROLES) == active and {tuple(e['roles']) for e in data['edges']} == active,
            'Incomplete or duplicated orientation coverage')
    weights = kernel()
    results = [verify_edge(e, roles, value, weights)
               for e, roles, value in zip(data['edges'], ROLES, EXPECTED)]
    rows = [row for edge in data['edges'] for row in edge['rows']]
    require(len(rows) == 3258, 'Wrong selected-row total')
    require(len({tuple(row['source_exponents']) for row in rows}) == 3258,
            'Repeated or missing physical source exponents')
    require(sum(rat(row['coefficient']) != 0 for row in rows) == 288,
            'Wrong nonzero selected-row count')
    require(sum(result['quotient_terms'] for result in results) == 4014,
            'Wrong full quotient term total')
    require(all(rat(result['signed_contribution']) != 0 for result in results),
            'Unexpected zero-filled oriented contribution')
    total = sum((rat(result['signed_contribution']) for result in results), F(0))
    require(total == rat(data['selected_coordinate']) == F(0), 'Wrong selected coordinate')
    return {'status': 'PASS_COMPLETE_SELECTED_COORDINATE_SUPPLIED_QUOTIENT_REPLAY',
        'scalar_map': MAP, 'field': 'Q', 'pairing_monomial': M,
        'selected_coordinate': enc(total), 'edges': results, 'verified_orientations': 18,
        'remaining_target_orientations': 0, 'source_rows': 3258,
        'distinct_source_exponents': 3258, 'nonzero_source_rows': 288,
        'full_quotient_terms': 4014, 'source_DAG_evaluated': False,
        'terminal_checkpoints_reconstructed': False, 'source_attribution_reproduced': False,
        'whole_scalar_map_computed': False, 'full_obstruction_computed': False}


def verify_provenance(data):
    expected = {'schema': 'second-scalar-m2220-historical-provenance-v1', 'historical_final_result_sha256': 'eb0b339e79d821b3fc40bfa047188a0d7442bdb7c3516c06e0c6e33cf8f5ea36', 'historical_final_manifest_sha256': '3c548b72900abfa125234017b97ab8067531c43c5ed340211168eab629a5d2f8', 'historical_primary_comparison_sha256': '3d4e2c7277b6c8752502f90ba2972905da82187fa02894376a2928003b4a0925', 'historical_final_seal_comparison_sha256': '2009dc3590b450a87b5219ed372e2fdbf38b6fd47984dcb48466a43965e75011', 'historical_audit_manifest_sha256': 'ac4715bbdbfc04448bc3e22a80998cb6620e20f561790d1fe3e8ae5f7dcfba81', 'historical_final_manifest_pins': 904, 'historical_frozen_audit_pins': 609, 'historical_source_nodes_reevaluated_by_comparison': 0, 'terminal_checkpoints_distributed': False, 'new_map_source_regeneration_distributed': False, 'historical_hashes_are_not_public_reproduction': True}
    require(data == expected, 'Historical provenance pins or evidence scope changed')
    require(data['terminal_checkpoints_distributed'] is False and
            data['new_map_source_regeneration_distributed'] is False and
            data['historical_hashes_are_not_public_reproduction'] is True,
            'Historical/public evidence distinction lost')


def replay(directory=HERE):
    verify_manifest(directory)
    verify_provenance(load(Path(directory) / 'provenance.json'))
    return verify(load(Path(directory) / 'contributions.json'))


if __name__ == '__main__':
    print(json.dumps(replay(), indent=2))
