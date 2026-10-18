#!/usr/bin/env python3
"""Bind the consumed generator excerpts and exact normalization to public pins."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def function(text, name):
    start = text.index('function ' + name + '(')
    cursor = text.index('{', start) + 1
    depth = 1
    # The five pinned excerpts contain no braces in strings or comments.
    while depth:
        depth += (text[cursor] == '{') - (text[cursor] == '}')
        cursor += 1
    return text[start:cursor]


def verify(geometric, public_generator=None):
    pins = json.loads((ROOT / 'pins.json').read_text())
    for name in ('model','sourceExcerpts'):
        entry = pins['dependencies'][name]
        if sha((geometric / entry['relativePath']).read_bytes()) != entry['sha256']:
            raise ValueError('Dependency hash mismatch: ' + name)
    text = (geometric / pins['dependencies']['sourceExcerpts']['relativePath']).read_text()
    for name, digest in pins['sourceFunctions'].items():
        if sha(function(text, name).encode()) != digest:
            raise ValueError('Function mismatch: ' + name)
    normalization = (ROOT / 'data/final-normalization.js').read_text().strip()
    if sha((normalization+'\n').encode()) != pins['normalizationSHA256']:
        raise ValueError('Final normalization mismatch')
    if public_generator is not None:
        raw = public_generator.read_bytes()
        if sha(raw) != pins['publicGenerator']['sha256']:
            raise ValueError('Complete public generator hash mismatch')
        public = raw.decode()
        for name in pins['sourceFunctions']:
            if function(public,name) != function(text,name):
                raise ValueError('Public function differs: '+name)
        if public.splitlines().count(normalization) != 1:
            raise ValueError('Final normalization line not uniquely matched')
    # Function hashes bind the whole formulas. These annotations explicitly
    # identify the key constants/order choices used in the written dictionary.
    first = function(text, 'first')
    for fragment in ['jscale(sum,R(1n,4n))', 'R(15n,8n)', 'R(-1n,2n)',
                     'return mtimes(G,Z)', 'mtrace(Bi.B),mtrace(Bj.B)',
                     'mtrace(Ai.B),mtrace(Aj.B)']:
        if fragment not in first:
            raise ValueError('First-order formula anchor missing: '+fragment)
    if 'C=mm(GI,globalCross(D,0,1,2))' not in normalization:
        raise ValueError('Expected left normalization not found')
    return {'status':'PASS','sourceFunctions':list(pins['sourceFunctions']),
            'exactFirstOrderAnchors':6,'finalLeftNormalizationMatched':True,
            'completePublicGeneratorCompared':public_generator is not None,
            'scope':'Exact source binding plus mathematical dictionary; no DAG regeneration.'}
