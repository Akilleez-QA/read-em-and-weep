"""Reproduce the documented forged-producer boundary, not a mathematical run."""
import json
from pathlib import Path
import tempfile
from fixture_support import EXPECTED_OUTPUT, Fixture, verify_pins


def main():
    verify_pins()
    with tempfile.TemporaryDirectory(prefix='q65-synthetic-boundary-') as directory:
        fixture = Fixture(Path(directory) / 'SYNTHETIC-ONLY')
        # One changed log; the other 72 fabricated receipts remain self-consistent.
        log = b'SYNTHETIC: no checks were run\nERROR before forged marker\n' + fixture.marker() + b'\n'
        fixture.replace_log(log, refresh_digest=True)
        result = fixture.run()
    verify_pins()
    observation = {
        'scope': 'Fabricated metadata only; no mathematical execution or real receipt',
        'changed_log': log.decode(), 'returncode': result.returncode,
        'validator_stdout': result.stdout.strip(), 'validator_stderr': result.stderr,
        'conclusion': 'Log hashing plus a final marker cannot authenticate producer honesty; this boundary is documented by PR827.',
    }
    print(json.dumps(observation, indent=2))
    if result.returncode != 0 or json.loads(result.stdout) != EXPECTED_OUTPUT:
        raise SystemExit('Observed behavior differs from the pinned boundary characterization')


if __name__ == '__main__':
    main()
