#!/usr/bin/env python3
"""Reproduce the bounded ambient residual attribution checks, from any cwd."""
import argparse
import hashlib
import json
from pathlib import Path
import os
import subprocess
import sys
import tempfile

if sys.flags.optimize:
    raise RuntimeError('Run this verifier without Python -O or -OO.')
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'checks'))
from verify_source import verify as verify_source
from verify_character_report import verify as verify_rank_report
from test_certificates import verify as verify_fixtures


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest():
    manifest = json.loads((ROOT/'manifest.json').read_text())['sha256']
    actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()
              and '__pycache__' not in p.parts and p.name != 'manifest.json'}
    if actual != set(manifest):
        raise ValueError('Manifest file set does not match package')
    for name, expected in manifest.items():
        if sha(ROOT/name) != expected:
            raise ValueError('Package manifest mismatch: '+name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometric-package',type=Path,
                        default=ROOT.parent/'current-scalar-geometric-dependencies')
    parser.add_argument('--scalar-proof',type=Path,default=ROOT.parent/'current-scalar-proof')
    parser.add_argument('--public-generator',type=Path)
    args = parser.parse_args()
    geometric = args.geometric_package.resolve()
    proof = args.scalar_proof.resolve()
    public = args.public_generator.resolve() if args.public_generator else None
    verify_manifest()
    source = verify_source(geometric, public)
    pins = json.loads((ROOT/'pins.json').read_text())
    finite = proof/pins['dependencies']['finiteModel']['relativePath']
    if sha(finite) != pins['dependencies']['finiteModel']['sha256']:
        raise ValueError('Pinned finite model differs')
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='residual-attribution-') as directory:
        def run(command):
            completed = subprocess.run(command,cwd=directory,env=env,check=True,
                                       capture_output=True,text=True,timeout=300)
            return json.loads(completed.stdout)
        algebra = run([sys.executable,str(ROOT/'checks/verify_algebra.py')])
        determinants = run([sys.executable,str(ROOT/'checks/verify_determinants.py'),
                            '--model',str(geometric/'data/model.json')])
        ranks = run(['node','--max-old-space-size=768',
                     str(ROOT/'checks/verify_character_ranks.js'),str(finite),
                     str(geometric/'data/model.json')])
    verify_rank_report(ranks)
    fixtures = verify_fixtures(geometric,ranks)
    report = {'status':'PASS','packageManifestVerified':True,
              'checks':{'algebra':algebra,'determinants':determinants,
                        'source':source,'characterRanks':ranks,'fixtures':fixtures},
              'scope':'Bounded attribution to the declared noncentral second jet. No scalar or full obstruction evaluated.'}
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
