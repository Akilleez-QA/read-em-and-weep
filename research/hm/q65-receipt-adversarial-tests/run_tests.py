"""Full-CLI regressions against unmodified PR827. Standard library only."""
import argparse
import json
from pathlib import Path
import platform
import sys
import tempfile
import time
from fixture_support import COMMIT, EXPECTED_OUTPUT, Fixture, PINS, PINNED, SCOPES, verify_pins


def cases():
    """Each negative starts with all 73 valid-looking synthetic receipts."""
    out = []
    def reject(name, mutate, reason):
        out.append((name, mutate, reason))
    def receipt(name, key, value, reason):
        reject(name, lambda f: f.receipts[0].__setitem__(key, value), reason)
    def lock(name, mutate, reason):
        def change(f):
            mutate(f.lock)
            f.refresh_lock_bindings()  # Isolate the prerequisite, not a stale lock hash.
        reject(name, change, reason)
    def log(name, create, reason='log terminal marker is not final', refresh=True):
        reject(name, lambda f: f.replace_log(create(f), refresh_digest=refresh), reason)

    out.append(('complete_synthetic_packet', lambda f: None, None))
    out.append(('order_independent_packet', lambda f: f.receipts.reverse(), None))
    out.append(('trailing_blank_lines', lambda f: f.replace_log(f.read_log() + b'\n \t\r\n'), None))
    out.append(('crlf_final_marker', lambda f: f.replace_log(f.read_log().replace(b'\n', b'\r\n')), None))
    out.append(('no_final_newline', lambda f: f.replace_log(f.read_log().rstrip(b'\n')), None))

    log('altered_stdout_stale_hash', lambda f: b'ALTERED\n' + f.read_log(), 'log bytes mismatch', False)
    log('line_ending_change_stale_hash', lambda f: f.read_log().replace(b'\n', b'\r\n'), 'log bytes mismatch', False)
    log('empty_log_with_matching_hash', lambda f: b'')
    log('whitespace_only_log', lambda f: b' \t\r\n\n')
    log('partial_log_with_matching_hash', lambda f: b'SYNTHETIC partial output\n')
    log('truncated_marker', lambda f: f.marker()[:-1])
    log('marker_then_error', lambda f: f.marker() + b'\nERROR: unfinished\n')
    log('marker_then_later_work', lambda f: f.marker() + b'\nnext unit started\n')
    log('marker_only_as_substring', lambda f: b'echo ' + f.marker() + b'\n')
    log('quoted_marker', lambda f: b'"' + f.marker() + b'"\n')
    log('marker_with_suffix', lambda f: f.marker() + b' forged\n')
    log('marker_for_other_unit', lambda f: f.marker(1) + b'\n')
    log('marker_with_leading_space', lambda f: b' ' + f.marker() + b'\n')
    log('marker_with_trailing_space', lambda f: f.marker() + b' \n')
    log('marker_with_nul', lambda f: f.marker() + b'\x00\n')
    log('marker_with_ansi_escape', lambda f: b'\x1b[32m' + f.marker() + b'\x1b[0m\n')
    receipt('false_matching_marker_metadata', 'terminal_marker', 'forged-marker', 'log terminal marker is not final')
    def spoof(f):
        f.receipts[0]['terminal_marker'] = 'forged-marker'
        f.replace_log(b'forged-marker\n')
    reject('self_consistent_wrong_terminal_marker', spoof, 'missing terminal marker')
    reject('missing_log', lambda f: (f.root / f.receipts[0]['log_path']).unlink(), 'log bytes mismatch')
    receipt('missing_log_path', 'log_path', '', 'log bytes mismatch')
    receipt('path_traversal', 'log_path', '../outside.log', 'unsafe payload path')
    reject('absolute_log_path', lambda f: f.receipts[0].update(log_path=str(f.root / 'logs/unit-00.log')), 'unsafe payload path')
    def escape(f):
        outside = f.root.parent / 'outside-synthetic.log'
        outside.write_bytes(f.read_log())
        link = f.root / 'escaping.log'
        link.symlink_to(outside)
        f.receipts[0]['log_path'] = 'escaping.log'
    reject('symlink_escapes_receipt_directory', escape, 'payload path escapes root')

    for index in range(8):
        reject(f'missing_global_{index}', lambda f, i=index: f.receipts.pop(i), 'missing units: 1')
    reject('missing_harmonic_unit', lambda f: f.receipts.pop(8), 'missing units: 1')
    reject('missing_trace_unit', lambda f: f.receipts.pop(), 'missing units: 1')
    for name, index in [('global', 0), ('harmonic', 8), ('trace', 72)]:
        reject('duplicate_' + name, lambda f, i=index: f.receipts.append(dict(f.receipts[i])), 'duplicate unit ID')
    receipt('unexpected_unit_id', 'unit_id', 'q65-shards-v1/global/unknown', 'unexpected unit ID')
    receipt('wrong_receipt_schema', 'schema', 'different/receipt', 'receipt schema mismatch')
    receipt('fixture_marked_as_production', 'fixture_only', True, 'fixture/production receipts cannot be mixed')
    receipt('wrong_receipt_contract', 'contract_sha256', '0' * 64, 'receipt contract mismatch')
    receipt('wrong_runtime_binding', 'runtime_lock_sha256', '0' * 64, 'receipt runtime lock mismatch')
    for key in ('input_before_sha256', 'input_after_sha256'):
        receipt('mismatch_' + key, key, '0' * 64, 'input changed during shard')
    for name, key, value in [('failed_status', 'status', 'failed'), ('nonzero_exit', 'exit_code', 1),
                             ('bool_exit_is_not_zero', 'exit_code', False), ('string_exit', 'exit_code', '0')]:
        receipt(name, key, value, 'shard did not exit successfully')
    for key in ('timed_out', 'terminated'):
        receipt(key, key, True, 'incomplete shard')
    receipt('disabled_assertions', 'assertions_enabled', False, 'assertions disabled')
    reject('missing_check', lambda f: f.receipts[0]['checks'].pop('gram_identities'), 'missing, extra, or failed check')
    reject('extra_check', lambda f: f.receipts[0]['checks'].update(extra='passed'), 'missing, extra, or failed check')
    reject('failed_check', lambda f: f.receipts[0]['checks'].update(gram_identities='failed'), 'missing, extra, or failed check')
    receipt('negative_elapsed_time', 'elapsed_seconds', -1, 'missing elapsed time')

    lock('unready_execution_lock', lambda x: x.update(execution_ready=False), 'execution lock is not ready')
    lock('wrong_lock_contract', lambda x: x.update(contract_sha256='0' * 64), 'lock contract mismatch')
    for key in ('adapter_sha256', 'initializer_sha256', 'initializer_provenance_sha256'):
        lock('missing_' + key, lambda x, k=key: x.pop(k), 'missing runtime pin: ' + key)
    lock('nonhex_runtime_pin', lambda x: x.update(adapter_sha256='g' * 64), 'missing runtime pin: adapter_sha256')
    lock('missing_coverage', lambda x: x.pop('helper_assertion_coverage'), 'missing helper assertion coverage')
    for index, scope in enumerate(SCOPES):
        lock(f'missing_helper_scope_{index}', lambda x, s=scope: x['helper_assertion_coverage']['scopes'].pop(s), 'missing helper assertion coverage')
    lock('extra_helper_scope', lambda x: x['helper_assertion_coverage']['scopes'].update(extra='preserved-transitively'), 'missing helper assertion coverage')
    lock('invalid_helper_scope_status', lambda x: x['helper_assertion_coverage']['scopes'].update({SCOPES[0]: 'unreviewed'}), 'unverified helper assertion scope')
    for key in ('coverage_manifest_sha256', 'independent_review_sha256'):
        lock('missing_' + key, lambda x, k=key: x['helper_assertion_coverage'].pop(k), 'missing helper coverage certificate: ' + key)
    for key in ('python', 'sympy'):
        lock('missing_' + key, lambda x, k=key: x.pop(k), 'unfrozen runtime versions')
    reject('contract_digest_mismatch', lambda f: f.contract.update(source_commit='altered'), 'contract digest mismatch')
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='optional machine-readable observed results')
    args = parser.parse_args()
    verify_pins()
    started = time.monotonic()
    observations = []
    failures = []
    with tempfile.TemporaryDirectory(prefix='q65-synthetic-cli-') as directory:
        root = Path(directory)
        for index, (name, mutate, reason) in enumerate(cases()):
            fixture = Fixture(root / f'SYNTHETIC-ONLY-{index:03d}')
            mutate(fixture)
            result = fixture.run()
            if reason is None:
                try:
                    actual = json.loads(result.stdout)
                except json.JSONDecodeError:
                    actual = None
                matched = result.returncode == 0 and result.stderr == '' and actual == EXPECTED_OUTPUT
            else:
                # Check the last error line, not just a nonzero exit, and require no
                # successful JSON output. Earlier unrelated rejection cannot pass.
                matched = (result.returncode != 0 and result.stdout == '' and
                           result.stderr.strip().splitlines()[-1] == 'ValueError: ' + reason)
            observation = {'case': name, 'expected': 'accept_synthetic_metadata' if reason is None else 'reject',
                           'returncode': result.returncode, 'matched': matched}
            if reason:
                observation['reason'] = result.stderr.strip().splitlines()[-1]
            else:
                observation['stdout'] = result.stdout.strip()
            observations.append(observation)
            if not matched:
                failures.append({'case': name, 'stdout': result.stdout, 'stderr': result.stderr})
        # Deliberately forged stdout with a fresh digest and correct final marker
        # can be accounted for. This is the documented untrusted-producer boundary,
        # not algebraic evidence and not classified as a validator defect.
        probe = Fixture(root / 'SYNTHETIC-ONLY-forged-producer')
        probe.replace_log(b'SYNTHETIC COUNTEREXAMPLE: CHECKS WERE NOT RUN\nERROR before forged marker\n' + probe.marker() + b'\n')
        result = probe.run()
        boundary = {'name': 'fabricated_producer_can_assert_completion',
                    'returncode': result.returncode, 'stdout': result.stdout.strip(),
                    'interpretation': 'Documented trust boundary: a self-consistent forged producer is not authenticated by receipt accounting.'}
        if result.returncode != 0 or json.loads(result.stdout) != EXPECTED_OUTPUT:
            failures.append({'case': boundary['name'], 'stdout': result.stdout, 'stderr': result.stderr})
    verify_pins()
    report = {
        'artifact': 'q65 full-CLI synthetic adversarial regressions',
        'status': 'all_expected_cli_outcomes_observed' if not failures else 'unexpected_cli_outcome',
        'source_commit': COMMIT, 'input_sha256': PINS,
        'python': platform.python_version(), 'elapsed_seconds': round(time.monotonic() - started, 4),
        'case_count': len(observations), 'accepted_synthetic_controls': sum(x[2] is None for x in cases()),
        'rejected_adversarial_cases': sum(x[2] is not None for x in cases()),
        'cases': observations, 'producer_trust_boundary': boundary, 'failures': failures,
        'production_validator_modified': False, 'production_execution_gate': 'disabled_and_unchanged',
        'symbolic_payload_imported': False, 'mathematical_shards_executed': 0,
        'fabricated_receipts_persisted': False,
    }
    output = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.write_text(output, encoding='utf-8')
    print(output, end='')
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
