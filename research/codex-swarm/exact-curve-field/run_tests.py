"""Linux bounded artificial-only runner. Run from this directory."""
import os
import resource
import subprocess
import sys
from pathlib import Path


def bounds():
    resource.setrlimit(resource.RLIMIT_AS, (768*1024*1024, 768*1024*1024))
    resource.setrlimit(resource.RLIMIT_CPU, (59, 59))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


if __name__ == '__main__':
    try:
        result = subprocess.run([sys.executable, '-B', 'test_field.py'],
                                cwd=Path(__file__).resolve().parent,
                                env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
                                preexec_fn=bounds, timeout=60, check=False)
        sys.exit(result.returncode)
    except subprocess.TimeoutExpired:
        print('FAIL CLOSED: artificial tests exceeded 60 wall seconds', file=sys.stderr)
        sys.exit(124)
