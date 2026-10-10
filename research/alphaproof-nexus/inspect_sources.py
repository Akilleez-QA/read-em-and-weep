#!/usr/bin/env python3
"""Byte/provenance and text-level target checks; never invokes Lean or the network."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SOURCE_SHA256 = 'd654c3dbdb006712418b30e8c43d1de45d32ba1a5c7d514033e47066f7b2ef26'
EXCERPT_SHA256 = '98ad3933011aef9f0c72ac830827e56ad9bd79a1a17f6775c02842f38a990fb4'
LOCAL_SHA256 = '05bbf726dd5eac8aac02279cf08af82a64476c492786665ba87f00be0918ded8'
LICENSE_SHA256 = 'cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30'
TARGET = ('def ProblemP5 : Prop := ∀ (P : PureOrderIdeal 3), typePO P = 2 → '
          'IsLogConcaveUpTo (socleDegree P) (pureOSequence P.ideal)')
FORBIDDEN = re.compile(r'(?<![\w\'])\b(sorry|admit|axiom|native_decide)\b(?![\w\'])')


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def code_only(text: str) -> str:
    """Mask ordinary Lean nested/line comments and strings, retaining whitespace.

    This small scanner is a review aid for the fixed sources, not a Lean parser
    or an adversarial-code safety guarantee. Byte pins remain the trust anchor.
    """
    out, i, depth = [], 0, 0
    while i < len(text):
        if depth:
            if text.startswith('/-', i):
                depth += 1; out.extend('  '); i += 2
            elif text.startswith('-/', i):
                depth -= 1; out.extend('  '); i += 2
            else:
                out.append('\n' if text[i] == '\n' else ' '); i += 1
        elif text.startswith('/-', i):
            depth = 1; out.extend('  '); i += 2
        elif text.startswith('--', i):
            end = text.find('\n', i)
            if end < 0: end = len(text)
            out.extend(' ' * (end - i)); i = end
        elif text[i] == '"':
            out.append(' '); i += 1
            while i < len(text):
                if text[i] == '\\':
                    out.extend('  '); i += 2
                elif text[i] == '"':
                    out.append(' '); i += 1; break
                else:
                    out.append('\n' if text[i] == '\n' else ' '); i += 1
            else:
                raise ValueError('Unterminated string')
        else:
            out.append(text[i]); i += 1
    if depth: raise ValueError('Unterminated block comment')
    return ''.join(out)


def inspect_text(text: str, *, full_target: bool) -> dict:
    code = code_only(text)
    forbidden = sorted(set(FORBIDDEN.findall(code)))
    if forbidden: raise ValueError('Disallowed proof placeholders/declarations: ' + ', '.join(forbidden))
    imports = re.findall(r'^\s*import\s+([^\n]+)', code, re.M)
    if imports != ['Mathlib']: raise ValueError('Unexpected import list')
    normalized = ' '.join(code.split())
    if full_target:
        # Match the entire definition up to the next declaration, not a prefix.
        pattern = r'\bdef ProblemP5 : Prop := (.*?) (?=(?:def|lemma|theorem|structure|class|instance|namespace|end|section)\b)'
        match = re.search(pattern, normalized)
        if not match or 'def ProblemP5 : Prop := ' + match.group(1) != TARGET:
            raise ValueError('ProblemP5 target statement changed')
        if len(re.findall(r'\btheorem P5\s*:\s*ProblemP5\s*:=\s*by\b', code)) != 1:
            raise ValueError('P5 theorem declaration changed or duplicated')
    return {'imports': imports, 'forbidden_tokens_found': forbidden,
            'target_statement_text_checked': full_target,
            'lean_kernel_validation_performed': False}


def inspect_package(root: Path = ROOT, upstream: Path | None = None) -> dict:
    local = (root / 'examples/LogConcaveCore.lean').read_bytes()
    if digest(local) != LOCAL_SHA256: raise ValueError('Vendored example hash mismatch')
    if digest((root / 'licenses/Apache-2.0.txt').read_bytes()) != LICENSE_SHA256:
        raise ValueError('Apache license hash mismatch')
    result = {'schema': 'alphaproof-nexus-static-check-v1',
              'example_sha256': digest(local), 'example': inspect_text(local.decode(), full_target=False),
              'upstream_source_inspected': False, 'lean_kernel_validation_performed': False}
    if upstream is not None:
        data = upstream.read_bytes()
        if digest(data) != SOURCE_SHA256: raise ValueError('Upstream P5 source hash mismatch')
        lines = data.decode().splitlines(keepends=True)
        excerpt = ''.join(lines[503:516]).encode()
        if digest(excerpt) != EXCERPT_SHA256 or excerpt not in local:
            raise ValueError('Vendored proof body differs from upstream lines 504-516')
        result.update(upstream_source_inspected=True, upstream_source_sha256=digest(data),
                      upstream=inspect_text(data.decode(), full_target=True),
                      original_proof_body_byte_identical=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upstream-proof', type=Path,
                        help='Optional local copy of the pinned full P5 source; read only')
    args = parser.parse_args()
    try:
        print(json.dumps(inspect_package(upstream=args.upstream_proof), indent=2))
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(1, f'Static check failed: {exc}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
