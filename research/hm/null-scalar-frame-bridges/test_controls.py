"""Run only packaged static/formal checkers; never execute supplied source files."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent

def require(ok, message):
    if not ok:
        raise ValueError(message)

def main():
    require(len(sys.argv) > 1, 'Supply the same source path arguments as the scalar checker.')
    results = []
    with tempfile.TemporaryDirectory(prefix='bridge-controls-') as tmp:
        staging = Path(tmp)
        for name in ('scalar', 'frame'):
            (staging/name).mkdir()
            shutil.copyfile(ROOT/name/'check.py', staging/name/'check.py')
        shutil.copyfile(ROOT/'inputs.py', staging/'inputs.py')
        original_pins = (ROOT/'pins.json').read_text()
        original_scalar = (staging/'scalar/check.py').read_text()
        def run(mode, checker, case, expected_success, expected_error=None):
            command = [sys.executable, '-B'] + (['-O'] if mode == 'optimized' else [])
            command += [str(staging/checker/'check.py')] + sys.argv[1:]
            result = subprocess.run(command, capture_output=True, text=True)
            require((result.returncode == 0) == expected_success, case+' unexpected exit status')
            if expected_error:
                require(expected_error in result.stderr, case+' failed for an unexpected reason')
            if expected_success:
                require(json.loads(result.stdout)['status'] == 'PASS', case+' missing PASS')
            results.append({'mode':mode,'checker':checker,'case':case,'exit_code':result.returncode,
                            'expected_outcome_verified':True})
        for mode in ('normal','optimized'):
            (staging/'pins.json').write_text(original_pins)
            (staging/'scalar/check.py').write_text(original_scalar)
            for checker in ('scalar','frame'):
                run(mode,checker,'unaltered packaged checker',True)
            changed = json.loads(original_pins)
            changed[0]['sha256'] = '0'*64
            (staging/'pins.json').write_text(json.dumps(changed))
            for checker in ('scalar','frame'):
                run(mode,checker,'deliberately incorrect raw-engine pin',False,'SHA-256 mismatch: raw_engine')
            (staging/'pins.json').write_text(original_pins)
            require(original_scalar.count('F(15, 8)') == 1, 'polynomial mutation anchor changed')
            (staging/'scalar/check.py').write_text(original_scalar.replace('F(15, 8)','F(15, 4)',1))
            run(mode,'scalar','deliberately incorrect expected gerbe coefficient',False,'static/formal check failed')
    print(json.dumps({'status':'PASS','production_execution':False,'tests':results},indent=2))

if __name__ == '__main__':
    main()
