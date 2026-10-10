#!/usr/bin/env python3
"""Rejection tests for the published JSON resume guards.

Corrupt, truncated, and mismatched-pin inputs must fail before any
quotient product is formed. The published multiply, power, and add_shift
functions are replaced with raisers so a guard that fails open cannot
silently run the authors' arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EVALUATOR = ROOT / 'research' / 'hm' / 'current-scalar-evaluator'


def load_evaluator():
    sys.path.insert(0, str(EVALUATOR))
    spec = importlib.util.spec_from_file_location(
        'published_evaluate_quotient',
        EVALUATOR / 'evaluate_quotient.py',
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def install_arithmetic_tripwire(module) -> None:
    def trip(*_args, **_kwargs):
        raise RuntimeError('authors arithmetic was invoked')

    module.mul = trip
    module.power = trip
    module.add_shift = trip


def minimal_checkpoint(**overrides) -> dict:
    payload = {
        'schema': 'hm-portable-Q-JSON-checkpoint-v1',
        'rootDenominator': '1',
        'vals': [[1, [[0, '1']]]],
        'refs': [[1, 0]],
        'liveDenominators': [[1, '1']],
        'nextIndex': 0,
        'elapsedSeconds': 0,
        'operations': {'mul': 0, 'sparse': 0, 'packed': 0, 'monomial': 0,
                       'maxNonzeros': 0, 'maxCoefficientBits': 0,
                       'maxPackedDigitBits': 0, 'nonnegativePackedProducts': 0},
        'contract': {'schema': 'foreign'},
        'denominatorMetadataSHA256': '0' * 64,
        'reason': 'budget',
    }
    payload.update(overrides)
    return payload


def expect_reject(label: str, call) -> dict:
    try:
        call()
    except RuntimeError as error:
        if 'authors arithmetic was invoked' in str(error):
            raise AssertionError(label + ' reached quotient arithmetic') from error
        return {'label': label, 'requiredRejection': True, 'rejected': True,
            'exception': type(error).__name__}
    except Exception as error:
        return {'label': label, 'requiredRejection': True, 'rejected': True,
                'exception': type(error).__name__, 'message': str(error)[:180]}
    raise AssertionError(label + ' was accepted')


def write_config(directory: Path, compact: Path, clearing: Path, roles=(0, 1, 2, 3)) -> Path:
    output = directory / 'out'
    output.mkdir(parents=True)
    config = directory / 'config.json'
    config.write_text(json.dumps({
        'roles': list(roles),
        'input': str(compact),
        'clearingMetadata': str(clearing),
        'outputDirectory': str(output),
    }))
    return config


def run_structural(module) -> list[dict]:
    results = []
    results.append(expect_reject('corrupt-json', lambda: module.decode_checkpoint(b'{not-json')))
    results.append(expect_reject('truncated-json', lambda: module.decode_checkpoint(
        b'{"schema":"hm-portable-Q-JSON-checkpoint-v1","vals":[[')))
    results.append(expect_reject('truncated-utf8', lambda: module.decode_checkpoint(b'\xff{"schema":')))
    results.append(expect_reject('empty-file', lambda: module.decode_checkpoint(b'')))
    bad_integer = minimal_checkpoint()
    bad_integer['rootDenominator'] = '01'
    results.append(expect_reject('noncanonical-integer', lambda: module.decode_checkpoint(
        (json.dumps(bad_integer) + '\n').encode())))
    wrong_schema = minimal_checkpoint(schema='hm-exact-Q-integer-quotient-checkpoint-v1')
    results.append(expect_reject('wrong-schema', lambda: module.decode_checkpoint(
        (json.dumps(wrong_schema) + '\n').encode())))
    # A structurally valid document is decoded only so later pin tests have a
    # baseline. This is not an acceptance of a resume.
    decoded = module.decode_checkpoint((json.dumps(minimal_checkpoint()) + '\n').encode())
    if decoded['schema'] != 'hm-portable-Q-JSON-checkpoint-v1':
        raise AssertionError('baseline checkpoint did not decode')
    with tempfile.TemporaryDirectory(prefix='hsd-pin-') as temp:
        root = Path(temp)
        compact = root / 'compact.json'
        clearing = root / 'clearing.json'
        compact.write_text('{}\n')
        clearing.write_text('{}\n')
        config = write_config(root, compact, clearing)
        results.append(expect_reject('mismatched-compact-byte-pin', lambda: module.contract_and_inputs(config)))
    return results


def run_pinned_sources(module, sources: Path) -> list[dict]:
    install_arithmetic_tripwire(module)
    pair = sources / 'pairs' / 'pair-01'
    compact = pair / 'graded-jet.compact.json'
    clearing = pair / 'integer-clearing.json'
    results = []
    with tempfile.TemporaryDirectory(prefix='hsd-resume-') as temp:
        root = Path(temp)
        config = write_config(root, compact, clearing)
        cfg, _data, _clearing, contract = module.contract_and_inputs(config)
        if contract['inputSHA256'] != hashlib.sha256(compact.read_bytes()).hexdigest():
            raise AssertionError('live contract is not bound to the compact bytes')
        output = Path(cfg['outputDirectory'])

        def plant(name: str, raw: bytes) -> None:
            (output / 'checkpoint.json').write_bytes(raw)
            module.evaluate(config, 1)
            raise AssertionError(name + ' returned from evaluate')

        results.append(expect_reject('pinned-corrupt-checkpoint', lambda: plant('corrupt', b'{not-json')))
        results.append(expect_reject('pinned-truncated-checkpoint', lambda: plant(
            'truncated', b'{"schema":"hm-portable-Q-JSON-checkpoint-v1","rootDenominator":')))
        foreign = minimal_checkpoint()
        foreign['contract'] = dict(contract)
        foreign['contract']['inputSHA256'] = 'f' * 64
        results.append(expect_reject('mismatched-checkpoint-input-pin', lambda: plant(
            'input-pin', (json.dumps(foreign) + '\n').encode())))
        foreign_program = minimal_checkpoint()
        foreign_program['contract'] = dict(contract)
        foreign_program['contract']['arithmeticSHA256'] = 'e' * 64
        results.append(expect_reject('mismatched-checkpoint-arithmetic-pin', lambda: plant(
            'arithmetic-pin', (json.dumps(foreign_program) + '\n').encode())))
        if (output / 'quotient.json').exists():
            raise AssertionError('a rejected resume wrote quotient.json')

        # Observation, not a required rejection: a schema-valid checkpoint with
        # the live contract and a consistent frontier, but a tampered leaf
        # coefficient, is not a pin or syntax failure. Record whether the
        # resume guard stops it before arithmetic.
        uses = {}
        for node in _data['sumNodes']:
            for _coeff, _du, factors in node['terms']:
                for symbol, _exponent in factors:
                    uses[symbol] = uses.get(symbol, 0) + 1
        for symbol, _exponent in _data['root']['factors']:
            uses[symbol] = uses.get(symbol, 0) + 1
        tampered = {
            'schema': 'hm-portable-Q-JSON-checkpoint-v1',
            'rootDenominator': str(_clearing['root']['denominator']),
            'vals': [[1, [[0, '1']]], [2, [[0, '1']]], [3, [[0, '2']]]],
            'refs': sorted(uses.items()),
            'liveDenominators': [[1, '1'], [2, '1'], [3, '1']],
            'nextIndex': 0,
            'elapsedSeconds': 0,
            'operations': {'mul': 0},
            'contract': contract,
            'denominatorMetadataSHA256': hashlib.sha256(clearing.read_bytes()).hexdigest(),
            'reason': 'budget',
        }
        reached = False
        try:
            plant('tampered-leaf', (json.dumps(tampered) + '\n').encode())
        except RuntimeError as error:
            reached = 'authors arithmetic was invoked' in str(error)
            if not reached:
                raise
        except Exception as error:
            results.append({
                'label': 'tampered-leaf-coefficient',
                'requiredRejection': False,
                'rejected': True,
                'exception': type(error).__name__,
                'reachesArithmetic': False,
                'classification': 'rejected-by-guard',
            })
        else:
            raise AssertionError('tampered-leaf observation did not run')
        if reached:
            results.append({
                'label': 'tampered-leaf-coefficient',
                'requiredRejection': False,
                'rejected': False,
                'reachesArithmetic': True,
                'classification': 'missing-hypothesis',
            })

        mutated = root / 'mutated-compact.json'
        raw = bytearray(compact.read_bytes())
        raw[-2] ^= 0x01
        mutated.write_bytes(raw)
        bad_config = write_config(root / 'bad-compact', mutated, clearing)
        results.append(expect_reject('mismatched-regenerated-compact-pin',
                                     lambda: module.contract_and_inputs(bad_config)))
        mutated_clearing = root / 'mutated-clearing.json'
        shutil.copyfile(clearing, mutated_clearing)
        text = mutated_clearing.read_bytes()
        mutated_clearing.write_bytes(text[:-2] + b' \n')
        bad_clearing = write_config(root / 'bad-clearing', compact, mutated_clearing)
        results.append(expect_reject('mismatched-regenerated-clearing-pin',
                                     lambda: module.contract_and_inputs(bad_clearing)))
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--sources', type=Path)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    module = load_evaluator()
    results = run_structural(module)
    if args.sources:
        results.extend(run_pinned_sources(module, args.sources))
    required = [item for item in results if item.get('requiredRejection', True)]
    if not required or not all(item['rejected'] for item in required):
        raise SystemExit('a required resume guard accepted its input')
    receipt = {
        'schema': 'hsd-json-resume-guard-receipt-v1',
        'evidenceClass': 'published guard execution on crafted inputs; authors quotient arithmetic body not executed',
        'authorsArithmeticBodyExecuted': False,
        'results': results,
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({
        'status': 'PASS',
        'requiredRejections': [item['label'] for item in required],
        'observations': [item['label'] for item in results if not item.get('requiredRejection', True)],
    }, indent=2))


if __name__ == '__main__':
    main()
