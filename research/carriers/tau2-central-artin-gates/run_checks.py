#!/usr/bin/env python3
"""Run the standalone exact checks without optimization disabling assertions."""
from pathlib import Path
import os
import subprocess
import sys

root = Path(__file__).resolve().parent
env = dict(os.environ)
env.pop('PYTHONOPTIMIZE', None)
for name in ('verify_central.py', 'verify_artin_weighted.py'):
    print(f'== {name} ==', flush=True)
    subprocess.run([sys.executable, str(root/name)], check=True, env=env)
print('ALL CHECKS PASSED')
