"""Authenticate the immutable public dependency snapshot before importing it."""
import hashlib
import json
import os
from pathlib import Path

REVISION = '6e28c6b59f8245779f6c03a20798e4de6842ae19'
MANIFEST = 'ec0746ba0d537ec3edeb96f396a02e426225e904227e4c500dad0f5e0d3fbb64'


def package_path():
    default = Path(__file__).resolve().parents[2] / 'hm' / 'null-support-certificates'
    folder = Path(os.environ.get('NULL_SUPPORT_PACKAGE', default)).resolve()
    raw = (folder / 'release-manifest.json').read_bytes()
    if hashlib.sha256(raw).hexdigest() != MANIFEST:
        raise ValueError('expected the pinned PR79 release manifest')
    manifest = json.loads(raw)
    for name, digest in manifest['files_sha256'].items():
        if Path(name).name != name:
            raise ValueError('nonlocal dependency name')
        if hashlib.sha256((folder / name).read_bytes()).hexdigest() != digest:
            raise ValueError('dependency drift: ' + name)
    return folder
