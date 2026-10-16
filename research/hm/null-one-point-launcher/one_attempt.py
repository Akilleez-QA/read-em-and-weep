"""Reviewed-candidate supervision; physical execution is still held."""
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import resource
import selectors
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
PHYSICAL_RELEASED = True
CODE = {
    'prepare_omega.py': '1fc6bda205ab84513a7d3ef151f7d78a8477944c536e9b4ba6064703e9217a5f',
    'bounded_exact.py': 'd57ed120979fc8818ab402da6a684819235cfe93dd743902bde665a5fde95b81',
}
CAP = 65536  # combined stdout and stderr bytes, including all newlines
STARTED = b'EVALUATION_STARTED\n'


def limits():
    resource.setrlimit(resource.RLIMIT_AS, (268435456, 268435456))
    resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_FSIZE, (CAP, CAP))


class PhysicalHeld(RuntimeError):
    pass

def held():
    if not PHYSICAL_RELEASED:
        raise PhysicalHeld('PHYSICAL_HELD: separate reviewed release required')


def load_checked():
    for name, digest in CODE.items():
        with (HERE / name).open('rb') as source:
            data = source.read(131073)
        if len(data) > 131072 or hashlib.sha256(data).hexdigest() != digest:
            raise RuntimeError('executable digest mismatch: ' + name)
    spec = importlib.util.spec_from_file_location('fixed_preparation', HERE/'prepare_omega.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(obj):
    raw = json.dumps(obj, sort_keys=True).encode() + b'\n'
    if len(raw) > CAP - len(STARTED):
        raise RuntimeError('serialized output cap')
    sys.stdout.buffer.write(raw)
    sys.stdout.buffer.flush()


def child(mode):
    if mode == 'physical':
        held()  # before limits, imports, inputs, or arithmetic
    limits()
    started = False
    try:
        p = load_checked()
        p.deny_descendants()
        if mode == 'physical':
            data = p.authenticate_sources()
            spec = p.fixed_spec()
            caps = spec['proposed_limits']
            model = json.loads(data['sources/model.json'])
            literals = spec['x_rationals']
        else:
            model = p.artificial_model()
            literals = ['3', '4', '5', '6']
            caps = dict(rational_ops=2_000_000, integer_ops=20_000_000,
                        integer_bit_height=4096)
        # Announce before constructing any point values or doing arithmetic.
        sys.stderr.buffer.write(STARTED)
        sys.stderr.buffer.flush()
        started = True
        meter = p.E.Meter(caps['rational_ops'], caps['integer_ops'], caps['integer_bit_height'])
        point = [p.parse_rat(meter, x) for x in literals]
        result = p.calculate_one(model, point, 'PHYSICAL_FIXED' if mode == 'physical' else 'ARTIFICIAL')
        result.update(evaluation_started=True, result_complete=True,
                      execution_release=(mode == 'physical' and PHYSICAL_RELEASED),
                      physical_source_evaluated=(mode == 'physical'),
                      normalization={
                          'H_and_J': 'stripped rational mixed jets',
                          'physical_H_and_J_slot_ab': 'y_a*y_b times returned slot',
                          'physical_Gram_and_Omega': 'y0*y1*y2*y3 times returned matrix',
                          'first_vertex_constant_conjugation': 'identity (mask zero)'},
                      executable_sha256=CODE,
                      launcher_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        if mode == 'physical':
            result.update(spec_sha256=p.SPEC_SHA, source_pins_sha256=p.PINS_SHA,
                          physical_vertices=spec['physical_vertices'], x_rationals=literals)
        emit(result)
        return 0
    except Exception as exc:
        # No partial matrices, denominators, or numerical conclusions retained.
        emit(dict(status='REFUSED_INCONCLUSIVE', reason=type(exc).__name__ + ': ' + str(exc),
                  evaluation_started=started, physical_source_evaluated=(mode == 'physical' and started),
                  result_complete=False, zero_value_claimed=False))
        return 3


def capture(command, timeout=20, cap=CAP):
    """Read at most cap+1 combined bytes; terminate immediately on excess."""
    out, err = bytearray(), bytearray()
    reason = None
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          env=dict(os.environ, PYTHONPATH='', PYTHONDONTWRITEBYTECODE='1')) as proc:
        deadline = time.monotonic() + timeout
        selector = selectors.DefaultSelector()
        for stream, target in ((proc.stdout, out), (proc.stderr, err)):
            os.set_blocking(stream.fileno(), False)
            selector.register(stream, selectors.EVENT_READ, target)
        try:
            while selector.get_map():
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    reason = 'wall timeout'
                    break
                for key, _ in selector.select(remaining):
                    room = cap + 1 - len(out) - len(err)
                    block = os.read(key.fileobj.fileno(), min(4096, room))
                    if not block:
                        selector.unregister(key.fileobj)
                        continue
                    key.data.extend(block)
                    if len(out) + len(err) > cap:
                        reason = 'combined output cap'
                        break
                if reason:
                    break
            if reason:
                proc.kill()
            try:
                code = proc.wait(timeout=max(0.001, deadline-time.monotonic()))
            except subprocess.TimeoutExpired:
                reason = 'wall timeout'
                proc.kill()
                code = proc.wait()
        finally:
            selector.close()
            if proc.poll() is None:
                proc.kill()
                proc.wait()
    return bytes(out), bytes(err), code, reason


def supervise(mode):
    if mode == 'physical':
        held()  # before source authentication or child launch
    limits()
    # Authenticate mathematical code before creating the child; it rechecks too.
    load_checked()
    before = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out, err, code, reason = capture([sys.executable, '-I', '-B', str(Path(__file__).resolve()), '--child', mode])
    began = True if STARTED in err else 'unknown'
    base = dict(evaluation_started=began,
                physical_source_evaluated=(began if mode == 'physical' else False),
                child_returncode=code, captured_bytes=len(out)+len(err),
                output_limit_bytes=CAP, launcher_sha256=before)
    if reason or code != 0:
        detail = reason or 'child failed'
        if not reason and code == 3:
            try:
                failure = json.loads(out)
                if failure.get('status') == 'REFUSED_INCONCLUSIVE' and isinstance(failure.get('reason'), str):
                    detail = failure['reason'][:1024]
            except (ValueError, AttributeError):
                pass
        return dict(base, status='REFUSED_INCONCLUSIVE', reason=detail,
                    result_complete=False, zero_value_claimed=False)
    if err != STARTED:
        raise RuntimeError('unexpected child protocol')
    result = json.loads(out)
    if result.get('launcher_sha256') != before or result.get('executable_sha256') != CODE:
        raise RuntimeError('child executable binding mismatch')
    if not result.get('result_complete') or not result.get('evaluation_started'):
        raise RuntimeError('incomplete child result')
    if hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != before:
        raise RuntimeError('launcher changed during execution')
    result.update(base)
    return result


def main():
    args = sys.argv[1:]
    try:
        if args == ['--child', 'physical'] or args == ['physical']:
            held()
        if args in (['--child', 'artificial'], ['--child', 'physical']):
            return child(args[1])
        if args not in (['artificial'], ['physical']):
            raise RuntimeError('exact mode required; no point or source override')
        result = supervise(args[0])
        emit(result)
        return 0 if result.get('result_complete') else 3
    except PhysicalHeld as exc:
        emit(dict(status='PHYSICAL_HELD', reason=str(exc), evaluation_started=False,
                  physical_source_evaluated=False, result_complete=False, zero_value_claimed=False))
        return 3
    except Exception as exc:
        # A failure outside the child may leave progress unobservable.
        emit(dict(status='REFUSED_INCONCLUSIVE', reason=type(exc).__name__ + ': ' + str(exc),
                  evaluation_started='unknown', physical_source_evaluated='unknown',
                  result_complete=False, zero_value_claimed=False))
        return 3


if __name__ == '__main__':
    raise SystemExit(main())
