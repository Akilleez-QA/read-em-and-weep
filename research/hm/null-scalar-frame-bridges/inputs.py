"""Read-only, fail-closed pin verification. Never import or execute source inputs."""
import argparse
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def require(condition, message='formal/static check failed'):
    if not condition:
        raise ValueError(message)

def load_inputs(ids):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, help='Root containing the exact source_root_path layout in pins.json')
    for name in ('raw-engine', 'source-formulas', 'first-order', 'denotation', 'field', 'compiler'):
        parser.add_argument('--'+name, type=Path, help='Explicit path; overrides --source-root for this input')
    args = parser.parse_args()
    manifest = json.loads((ROOT/'pins.json').read_text())
    selected = [p for p in manifest if p['id'] in ids]
    require(len(selected) == len(ids), 'missing or duplicate pin identifier')
    sources = {}
    for pin in selected:
        supplied = getattr(args, pin['id'])
        if supplied is None:
            if args.source_root is None:
                parser.error('provide --source-root or --'+pin['id'].replace('_','-'))
            supplied = args.source_root / pin['source_root_path']
        raw = supplied.read_bytes()
        require(hashlib.sha256(raw).hexdigest() == pin['sha256'], 'SHA-256 mismatch: '+pin['id'])
        sources[pin['id']] = raw.decode('utf-8')
    return selected, sources
