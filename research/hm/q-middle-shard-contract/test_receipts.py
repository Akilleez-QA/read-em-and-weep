"""Synthetic metadata rejection fixtures only; never import symbolic payload."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from q65_shards import HELPER_COVERAGE, canonical, digest, validate_receipts


def run():
    contract = json.loads(Path(__file__).with_name('CONTRACT.json').read_text())
    lock = {'execution_ready': True, 'contract_sha256': contract['contract_sha256'],
            'adapter_sha256': 'a' * 64, 'initializer_sha256': 'b' * 64,
            'initializer_provenance_sha256': 'c' * 64,
            'helper_assertion_coverage': {
                'scopes': {scope: 'separately-certified' for scope in HELPER_COVERAGE},
                'coverage_manifest_sha256': 'e' * 64, 'independent_review_sha256': 'f' * 64},
            'python': 'synthetic-fixture-only', 'sympy': 'not-imported'}
    records = []
    for unit in contract['units']:
        records.append({'schema': 'q65-shards-v1/receipt', 'fixture_only': True,
                        'unit_id': unit['unit_id'], 'contract_sha256': contract['contract_sha256'],
                        'runtime_lock_sha256': digest(canonical(lock)),
                        'input_before_sha256': contract['input_bundle_sha256'],
                        'input_after_sha256': contract['input_bundle_sha256'],
                        'status': 'passed', 'exit_code': 0, 'timed_out': False,
                        'terminated': False, 'assertions_enabled': True,
                        'checks': {c: 'passed' for c in unit['check_ids']},
                        'terminal_marker': 'Q65_UNIT_COMPLETE ' + unit['unit_id'],
                        'elapsed_seconds': 0, 'log_sha256': 'd' * 64})
    assert validate_receipts(contract, lock, records, fixture=True)['status'] == 'fixture_metadata_pass'
    tested = []

    def reject(name, mutate, mutate_lock=None, fixture=True):
        rs, lk = copy.deepcopy(records), copy.deepcopy(lock)
        mutate(rs)
        if mutate_lock:
            mutate_lock(lk)
        try:
            validate_receipts(contract, lk, rs, fixture=fixture)
        except ValueError:
            tested.append(name)
        else:
            raise AssertionError('accepted invalid fixture: ' + name)

    reject('missing_map', lambda rs: rs.pop())
    reject('missing_global_completeness', lambda rs: rs.pop(3))
    reject('duplicate_map', lambda rs: rs.append(rs[-1]))
    reject('unexpected_map', lambda rs: rs[-1].update(unit_id='q65/unknown'))
    reject('changed_input', lambda rs: rs[-1].update(input_after_sha256='e' * 64))
    reject('wrong_contract', lambda rs: rs[-1].update(contract_sha256='e' * 64))
    reject('wrong_runtime', lambda rs: rs[-1].update(runtime_lock_sha256='e' * 64))
    reject('missing_check', lambda rs: rs[-1]['checks'].pop('rho_laplacian_over6'))
    reject('failed_check', lambda rs: rs[-1]['checks'].update(rho_laplacian_over6='failed'))
    reject('nonzero_exit', lambda rs: rs[-1].update(exit_code=1))
    reject('timeout', lambda rs: rs[-1].update(timed_out=True))
    reject('terminated', lambda rs: rs[-1].update(terminated=True))
    reject('assertions_disabled', lambda rs: rs[-1].update(assertions_enabled=False))
    reject('missing_terminal_marker', lambda rs: rs[-1].update(terminal_marker='partial'))
    reject('unready_lock', lambda rs: None, lambda lk: lk.update(execution_ready=False))
    reject('missing_helper_coverage', lambda rs: None, lambda lk: lk.pop('helper_assertion_coverage'))
    reject('incomplete_helper_coverage', lambda rs: None, lambda lk: lk['helper_assertion_coverage']['scopes'].pop('build_module:all_assertions'))
    reject('unreviewed_helper_coverage', lambda rs: None, lambda lk: lk['helper_assertion_coverage'].pop('independent_review_sha256'))
    reject('fixture_as_production', lambda rs: None, fixture=False)

    # CLI failures are checked before receipt completeness/fixture gating.
    # Assert the precise log rejection, not merely a nonzero process exit.
    with tempfile.TemporaryDirectory(prefix='q65-receipt-fixture-') as td:
        root = Path(td)
        r = copy.deepcopy(records[0])
        r['log_path'] = 'fixture.log'
        lock_path = root / 'lock.json'
        lock_path.write_text(json.dumps(lock))
        receipt_path = root / 'receipt.json'
        marker = r['terminal_marker'].encode()
        for name, logbytes, hashbytes, reason in [
            ('cli_trailing_error', marker + b'\nERROR: incomplete later work\n', None, 'log terminal marker is not final'),
            ('cli_partial_log', b'partial\n', None, 'log terminal marker is not final'),
            ('cli_log_byte_tamper', marker + b'\n', b'wrong bytes', 'log bytes mismatch'),
        ]:
            (root / r['log_path']).write_bytes(logbytes)
            r['log_sha256'] = digest(logbytes if hashbytes is None else hashbytes)
            receipt_path.write_text(json.dumps(r))
            result = subprocess.run([sys.executable, str(Path(__file__).with_name('q65_shards.py')),
                                     'aggregate', str(Path(__file__).with_name('CONTRACT.json')),
                                     str(lock_path), str(receipt_path)], capture_output=True, text=True, timeout=5)
            assert result.returncode != 0 and reason in result.stderr, (name, result.stdout, result.stderr)
            tested.append(name)
    print(json.dumps({'status': 'metadata-fixtures-pass', 'negative_cases': tested,
                      'payload_imported': False, 'mathematical_maps_checked': 0}, indent=2))


if __name__ == '__main__':
    run()
