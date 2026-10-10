#!/usr/bin/env python3
"""One portable exact-Q edge: at most two attempts, guarded wall time and memory."""
import argparse
import json
import os
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import sys
import time
import evaluate_quotient as E
from validate_quotient import validate

if sys.flags.optimize:
    raise RuntimeError('Assertion-enabled Python is required')
ROOT = Path(__file__).resolve().parent


def run(sources, roles, output):
    assert len(roles) == 4 and sorted(roles) == [0, 1, 2, 3]
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    assert not list(output.iterdir()), 'Output directory must be new and empty'
    pair = ''.join(map(str, roles[:2]))
    pair_dir = Path(sources).resolve() / 'pairs' / ('pair-' + pair)
    config = {'roles': roles, 'input': os.path.relpath(pair_dir / 'graded-jet.compact.json', output),
              'clearingMetadata': os.path.relpath(pair_dir / 'integer-clearing.json', output),
              'outputDirectory': '.'}
    config_path = output / 'config.json'
    config_path.write_text(json.dumps(config, indent=2) + '\n')
    cfg, d, k, contract = E.contract_and_inputs(config_path)
    def limits():
        os.setsid()
        resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    env = dict(os.environ)
    env.pop('PYTHONOPTIMIZE', None)
    history = []
    for attempt in (1, 2):
        start = time.monotonic()
        with (output / 'stdout.log').open('x') as stdout, (output / 'stderr.log').open('x') as stderr:
            process = subprocess.Popen([sys.executable, str(ROOT / 'evaluate_quotient.py'),
                                       '--config', str(config_path), '--seconds', '840'],
                                       stdout=stdout, stderr=stderr, preexec_fn=limits, env=env)
            try:
                code = process.wait(timeout=900)
                status = 'FINISHED' if code == 0 and (output / 'quotient.json').exists() else 'CHECKPOINTED' if code == 0 else 'FAILED'
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                code = process.wait()
                status = 'HARD_TIMEOUT'
        record = {'attempt': attempt, 'status': status, 'returnCode': code,
                  'elapsedSeconds': time.monotonic() - start, 'contract': contract,
                  'hardWallSeconds': 900, 'checkpointSeconds': 840,
                  'addressSpaceLimitBytes': 2 * 1024**3, 'maximumAttempts': 2}
        history.append(record)
        if status == 'FINISHED':
            record['validation'] = validate(config_path)
        elif status == 'CHECKPOINTED':
            checkpoint = output / 'checkpoint.json'
            state = E.decode_checkpoint(checkpoint.read_bytes())
            assert state['reason'] == 'budget' and state['contract'] == contract
            den = {j: 1 for j in roles[1:]}
            den.update({row['sourceSymbol']: int(row['denominator']) for row in k['nodes']})
            E.validate_frontier(state, d['sumNodes'], d['root'], den, contract)
            record['checkpointSHA256'] = E.sha(checkpoint)
            if attempt == 2: record['status'] = status = 'CHECKPOINTED_MAX_ATTEMPTS'
        (output / 'run-report.json').write_text(json.dumps({'attempts': history}, indent=2) + '\n')
        print(json.dumps(record), flush=True)
        if status != 'CHECKPOINTED':
            return status
        archive = output / ('attempt-' + str(attempt))
        archive.mkdir()
        for name in ('stdout.log', 'stderr.log', 'progress.jsonl', 'checkpoint.json', 'run-report.json'):
            source = output / name
            shutil.copyfile(source, archive / name)
            assert E.sha(source) == E.sha(archive / name)
        for name in ('stdout.log', 'stderr.log', 'progress.jsonl'):
            (output / name).unlink()
    raise AssertionError('Unreachable attempt bound')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sources', required=True)
    parser.add_argument('--roles', required=True, help='Permutation such as 0123')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    assert len(args.roles) == 4 and args.roles.isdigit()
    status = run(args.sources, list(map(int, args.roles)), args.output)
    sys.exit(0 if status == 'FINISHED' else 2)
