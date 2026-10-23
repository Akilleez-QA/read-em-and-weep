"""Static q65 catalogue and fail-closed receipt validation; no symbolic imports.

This module never imports or executes the frozen payload. It cannot run a
mathematical shard. The adapter/initializer execution lock must be frozen
separately before production receipt aggregation is enabled.
"""
import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path

VERSION = 'q65-shards-v1'
SOURCE_COMMIT = 'ad780e4a14cf7ac9c9f33140c05803b4c156fde8'
PINS = {
    'PAYLOAD.sha256': 'cbfb28f36c5a6b92281e3d6e7dca811c67077e99f52c7143677dd747134d1394',
    'Q-MIDDLE-55-PLUS-10-AUDIT-INPUT.sha256': 'a05dd6e00a203cafa908b611c002824072d3109da16b3103ac1c038eb1ecdb56',
    'Q-CUBIC-KERNEL-LIFT-AND-FULL-COMPLETION.sha256': '8a51729d04e922910d8b5e61e7651fbc7b006ae2a0f6a5597335660e3636e2d2',
    'verify_q_middle_quotient_coefficients.py': 'cee8781a4b9419d9fcc9cdd4c06e284356ad719f517025e5a55300c3e7424745',
}
SOURCES = [
    ('harmonic', 'a2h_tv0_D5', 'D5'),
    ('harmonic', 'a2h_tv0_P4', 'P4'),
    ('harmonic', 'a2h_tv1_A', 'A'),
    ('harmonic', 'a2h_tv1_P4', 'P4'),
    ('harmonic', 'a2h_tv2_D5', 'D5'),
    ('harmonic', 'a2h_tv3_V', 'V'),
    ('harmonic', 'a2h_tv4_1', '1'),
    ('trace', 'a_trace_h_D5', 'D5'),
]
GLOBAL = {
    'primitive-cg': ['nonzero_apolar_constants', 'gram_identities', 'left_inverses', 'all_cross_zero', 'full_tensor_reconstructions'],
    'cauchy-pairs': ['12_routes_and_types', 'nonzero_constant_grams', 'typed_left_inverse', 'inclusion_projector', 'both_cross_directions', 'symmetric_inclusions', 'sym9_reconstruction'],
    'outer-routes': ['13_routes', 'nonzero_constant_grams', 'typed_left_inverse', 'both_cross_directions', 'all_typed_reconstructions'],
    'target-templates': ['36_routes_and_types', 'literal_template_composite', 'typed_left_inverse', 'all_ordered_cross_zero', 'i3_sym9_reconstruction'],
    'harmonic-sources': ['seven_sources', 'nonzero_constant_grams', 'typed_right_inverse', 'both_cross_directions', 'i25_reconstruction'],
    'physical-section': ['positive_covector', 'quotient_frame_inverse', 'dr_identity', 'rd_czeta_identity', 'dc_zero', 'finv_f_identity', 'free234_c_factor_projection', 'projected_c_factor_zero'],
    'formal-source': ['a_square_harmonic', 'trace_rho_identity', 'all_marking_units_free', 'all_source_symbols_free'],
    'iterator-completeness': ['exact_unique_iterator_labels', '55_harmonic_10_trace', 'source_target_compatibility', '55_harmonic_matrix_units', '10_trace_matrix_units'],
}
MAP_CHECKS = ['literal_composite_tensor', 'intrinsic_symmetry', 'physical_inverse_on_both_indices', 'physical_symmetry', 'polynomial_regular_degree_1_2_1']
HELPER_COVERAGE = {'graded_module:all_assertions', 'build_module:all_assertions', 'transitive_initialization_helpers:all_assertions'}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def source_path(root, name):
    p = Path(name)
    require(not p.is_absolute() and '..' not in p.parts, 'unsafe payload path')
    resolved = (root / p).resolve()
    require(resolved.is_relative_to(root.resolve()), 'payload path escapes root')
    return resolved


def verify_payload(root):
    files = dict(PINS)
    for name, expected in PINS.items():
        require(digest(source_path(root, name).read_bytes()) == expected, 'pinned bytes changed: ' + name)
    for line in (root / 'PAYLOAD.sha256').read_text().splitlines():
        expected, name = line.split(None, 1)
        require(name not in files or files[name] == expected, 'conflicting input digest: ' + name)
        files[name] = expected
        require(digest(source_path(root, name).read_bytes()) == expected, 'payload bytes changed: ' + name)
    return files


def literal_assignment(path, name, function=None):
    tree = ast.parse(path.read_text())
    body = tree.body
    if function:
        matches = [n for n in body if isinstance(n, ast.FunctionDef) and n.name == function]
        require(len(matches) == 1, 'missing static function ' + function)
        body = matches[0].body
    matches = [n.value for n in body if isinstance(n, ast.Assign)
               and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)]
    require(len(matches) == 1, 'missing literal assignment ' + name)
    return ast.literal_eval(matches[0])


def build_contract(root):
    """Read bytes and literal route tables only; no payload import or exec."""
    files = verify_payload(root)
    pairs = literal_assignment(root / 'universal_q_middle_quotient_coefficients.py', 'specs', 'middle_pair_routes')
    choices = literal_assignment(root / 'universal_q_orthogonal_leg_coefficients.py', 'PAIR_OUTER_CHOICES')
    require(len(pairs) == 12, 'pair catalogue changed')
    routes = []
    for sector, inner, pair_kind in pairs:
        for outer, degree, kind in choices[pair_kind]:
            label = f'{sector}_cg{inner}_{pair_kind}_outer{outer}_B{degree}_{kind}'
            routes.append((label, kind))
    require(Counter(k for _, k in routes) == {'1': 1, 'A': 8, 'V': 8, 'P4': 9, 'D5': 10}, 'target catalogue mismatch')
    units = [{'unit_id': VERSION + '/global/' + name, 'category': 'global', 'check_ids': checks}
             for name, checks in GLOBAL.items()]
    for category, source, kind in SOURCES:
        for target, target_kind in routes:
            if target_kind != kind:
                continue
            label = source + '__' + target
            units.append({'unit_id': VERSION + '/' + category + '/' + label,
                          'category': category, 'source': source, 'target': target,
                          'kind': kind, 'label': label,
                          'check_ids': MAP_CHECKS + ['laplacian_zero' if category == 'harmonic' else 'rho_laplacian_over6']})
    require(Counter(u['category'] for u in units) == {'global': 8, 'harmonic': 55, 'trace': 10}, 'unit counts changed')
    require(len({u['unit_id'] for u in units}) == len(units), 'duplicate catalogue ID')
    contract = {'schema': VERSION, 'source_commit': SOURCE_COMMIT,
                'input_files': files, 'input_bundle_sha256': digest(canonical(files)),
                'runtime_status': 'disabled_pending_initializer_and_adapter_review',
                'source_names_basis': 'pinned harmonic_sources and typed_outputs code; no symbolic evaluation',
                'units': units}
    contract['contract_sha256'] = digest(canonical(contract))
    return contract


def validate_receipts(contract, lock, receipts, fixture=False):
    """Validate execution metadata, not the algebra reported by a producer."""
    body = {k: v for k, v in contract.items() if k != 'contract_sha256'}
    require(digest(canonical(body)) == contract['contract_sha256'], 'contract digest mismatch')
    require(lock.get('execution_ready') is True, 'execution lock is not ready')
    require(lock.get('contract_sha256') == contract['contract_sha256'], 'lock contract mismatch')
    for name in ('adapter_sha256', 'initializer_sha256', 'initializer_provenance_sha256'):
        value = lock.get(name, '')
        require(len(value) == 64 and all(c in '0123456789abcdef' for c in value), 'missing runtime pin: ' + name)
    coverage = lock.get('helper_assertion_coverage', {})
    require(set(coverage.get('scopes', {})) == HELPER_COVERAGE, 'missing helper assertion coverage')
    require(all(v in ('preserved-transitively', 'separately-certified') for v in coverage['scopes'].values()), 'unverified helper assertion scope')
    for name in ('coverage_manifest_sha256', 'independent_review_sha256'):
        value = coverage.get(name, '')
        require(len(value) == 64 and all(c in '0123456789abcdef' for c in value), 'missing helper coverage certificate: ' + name)
    require(bool(lock.get('python')) and bool(lock.get('sympy')), 'unfrozen runtime versions')
    lock_sha = digest(canonical(lock))
    expected = {u['unit_id']: u for u in contract['units']}
    seen = set()
    for r in receipts:
        unit_id = r.get('unit_id')
        require(unit_id in expected, 'unexpected unit ID')
        require(unit_id not in seen, 'duplicate unit ID')
        seen.add(unit_id)
        require(r.get('schema') == VERSION + '/receipt', 'receipt schema mismatch')
        require(r.get('fixture_only', False) is fixture, 'fixture/production receipts cannot be mixed')
        require(r.get('contract_sha256') == contract['contract_sha256'], 'receipt contract mismatch')
        require(r.get('runtime_lock_sha256') == lock_sha, 'receipt runtime lock mismatch')
        for name in ('input_before_sha256', 'input_after_sha256'):
            require(r.get(name) == contract['input_bundle_sha256'], 'input changed during shard')
        require(r.get('status') == 'passed' and type(r.get('exit_code')) is int and r['exit_code'] == 0, 'shard did not exit successfully')
        require(r.get('timed_out') is False and r.get('terminated') is False, 'incomplete shard')
        require(r.get('assertions_enabled') is True, 'assertions disabled')
        require(r.get('checks') == {c: 'passed' for c in expected[unit_id]['check_ids']}, 'missing, extra, or failed check')
        require(r.get('terminal_marker') == 'Q65_UNIT_COMPLETE ' + unit_id, 'missing terminal marker')
        require(isinstance(r.get('elapsed_seconds'), (int, float)) and r['elapsed_seconds'] >= 0, 'missing elapsed time')
        require(len(r.get('log_sha256', '')) == 64, 'missing log digest')
    require(seen == set(expected), 'missing units: ' + str(len(set(expected) - seen)))
    return {'status': 'fixture_metadata_pass' if fixture else 'execution_receipts_complete',
            'harmonic': 55, 'trace': 10, 'global': 8,
            'mathematical_claim': 'receipt accounting only; producer correctness requires independent review'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    cat = sub.add_parser('catalogue')
    cat.add_argument('--payload', type=Path, required=True,
                     help='explicit frozen q-middle-candidate-interface directory (read only)')
    cat.add_argument('--output', type=Path, required=True,
                     help='catalogue destination; its parent directory must already exist')
    agg = sub.add_parser('aggregate')
    agg.add_argument('contract', type=Path)
    agg.add_argument('lock', type=Path)
    agg.add_argument('receipts', nargs='+', type=Path)
    args = parser.parse_args()
    if args.command == 'catalogue':
        args.output.write_text(json.dumps(build_contract(args.payload), indent=2) + '\n')
        print('Static catalogue written: 65 map IDs + 8 global IDs; no mathematical checks executed.')
    else:
        receipts = []
        for p in args.receipts:
            r = json.loads(p.read_text())
            log = source_path(p.parent, r.get('log_path', ''))
            require(log.is_file() and digest(log.read_bytes()) == r.get('log_sha256'), 'log bytes mismatch')
            nonblank = [line for line in log.read_bytes().splitlines() if line.strip()]
            require(bool(nonblank) and nonblank[-1] == r.get('terminal_marker', '').encode(), 'log terminal marker is not final')
            receipts.append(r)
        result = validate_receipts(json.loads(args.contract.read_text()), json.loads(args.lock.read_text()), receipts)
        print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
