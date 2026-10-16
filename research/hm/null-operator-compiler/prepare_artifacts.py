#!/usr/bin/env python3
"""Verify archive hashes, decompress, then verify public bytes before writing."""
from pathlib import Path
import gzip,hashlib,json
ROOT=Path(__file__).resolve().parent

def prepare():
    records=json.loads((ROOT/'artifact-archives.json').read_text())
    for rec in records:
        raw=(ROOT/rec['archive']).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=rec['archive_sha256']:
            raise ValueError('archive hash mismatch: '+rec['archive'])
        data=gzip.decompress(raw)
        if len(data)!=rec['uncompressed_bytes'] or hashlib.sha256(data).hexdigest()!=rec['uncompressed_sha256']:
            raise ValueError('uncompressed artifact mismatch: '+rec['file'])
        (ROOT/rec['file']).write_bytes(data)
    return records

if __name__=='__main__':
    if not __debug__:raise SystemExit('optimized Python refused')
    for rec in prepare(): print('verified '+rec['file'])
