#!/usr/bin/env python3
"""Restore the two frozen cochain inputs, without replacing existing files."""
import gzip
import hashlib
import io
import os
from pathlib import Path
import tempfile

RAW_SHA256 = '011ba80d06f7b47a077845f377e9b22a5a9e51d808804e88e2ba4bf66c2306cd'
RAW_BYTES = 23833465
GZIP_SHA256 = '5033872e143d1e93d650698659a13853af0d7332c405b5454aacab96cfa7196c'
GZIP_BYTES = 875342
NAME = 'THIRD_MIDDLE_COCHAINS.json'
DIRECTORIES = ('third-middle-construction', 'third-normal-comparison')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_target(root, directory):
    parent = root / directory
    require(not parent.is_symlink() and parent.is_dir(),
            'Expected an ordinary sibling package directory: ' + directory)
    require(parent.resolve().parent == root, 'Target directory escapes package root')
    target = parent / NAME
    require(not target.is_symlink(), 'Refusing a symbolic-link target')
    if target.exists():
        require(target.is_file(), 'Refusing a non-file target')
        require(target.stat().st_size == RAW_BYTES and
                digest(target.read_bytes()) == RAW_SHA256,
                'Existing cochain differs; refusing to overwrite: ' + directory)
    return target


def main():
    here = Path(__file__).resolve().parent
    root = here.parent
    source = here / (NAME + '.gz')
    require(not source.is_symlink() and source.is_file(),
            'Expected an ordinary compressed input file')
    require(source.stat().st_size == GZIP_BYTES, 'Compressed size mismatch')
    compressed = source.read_bytes()
    require(digest(compressed) == GZIP_SHA256, 'Compressed SHA-256 mismatch')
    with gzip.GzipFile(fileobj=io.BytesIO(compressed), mode='rb') as stream:
        raw = stream.read(RAW_BYTES + 1)
    require(len(raw) == RAW_BYTES and digest(raw) == RAW_SHA256,
            'Reconstructed cochain size or SHA-256 mismatch')

    # Validate both targets before writing either. Never accept a caller path.
    targets = [checked_target(root, name) for name in DIRECTORIES]
    for target in targets:
        checked_target(root, target.parent.name)
        if target.exists():
            print('Already verified:', target.parent.name + '/' + NAME)
            continue
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode='wb', prefix='.cochains-',
                                             dir=target.parent, delete=False) as out:
                temporary = Path(out.name)
                out.write(raw)
                out.flush()
                os.fsync(out.fileno())
            # Link creation is atomic and fails if the target appeared meanwhile.
            # Do not replace/rename over any existing target.
            os.link(temporary, target)
        finally:
            if temporary is not None:
                temporary.unlink()
        require(target.stat().st_size == RAW_BYTES and
                digest(target.read_bytes()) == RAW_SHA256,
                'Post-write verification failed')
        print('Restored and verified:', target.parent.name + '/' + NAME)


if __name__ == '__main__':
    main()
