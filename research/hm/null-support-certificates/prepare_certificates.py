"""Unpack authenticated certificate bytes. No mathematical evaluator is invoked."""
import gzip
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def main():
    entries=json.loads((ROOT/'certificate-archives.json').read_text())['certificates']
    for entry in entries:
        for key in ('file','gzip'):
            if Path(entry[key]).name!=entry[key]:raise ValueError('Certificate names must be local basenames')
        archive=(ROOT/entry['gzip']).read_bytes()
        if hashlib.sha256(archive).hexdigest()!=entry['gzip_sha256']:raise ValueError('Archive hash mismatch')
        raw=gzip.decompress(archive)
        if len(raw)!=entry['bytes'] or hashlib.sha256(raw).hexdigest()!=entry['sha256']:raise ValueError('Certificate byte binding mismatch')
        target=ROOT/entry['file']
        if target.exists() and target.read_bytes()!=raw:raise ValueError('Existing certificate differs; refusing to overwrite '+entry['file'])
        target.write_bytes(raw)
        print('Verified and prepared '+entry['file'])
if __name__=='__main__':main()
