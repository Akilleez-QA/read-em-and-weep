#!/usr/bin/env python3
"""Match the bound graph to pinned public source formulas, without generating a DAG."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def function(text, name):
    start = text.index('function ' + name + '(')
    cursor = text.index('{', start) + 1
    depth = 1
    # These pinned function excerpts have no braces in strings or comments.
    while depth:
        depth += (text[cursor] == '{') - (text[cursor] == '}')
        cursor += 1
    return text[start:cursor]


def verify(public_generator=None):
    pins = json.loads((ROOT / 'pins.json').read_text())
    source = (ROOT / 'data/source-formulas.js').read_text()
    abstract = (ROOT / 'checks/compute_pole_bounds.js').read_text()
    if public_generator is not None:
        raw = public_generator.read_bytes()
        if hashlib.sha256(raw).hexdigest() != pins['publicGeneratorSHA256']:
            raise ValueError('Public generator hash mismatch')
        public = raw.decode()
        for name in pins['sourceExcerptFunctions']:
            if function(public, name) != function(source, name):
                raise ValueError('Public excerpt mismatch: ' + name)
    for name in ('crossResidual', 'globalCross'):
        if function(source, name) != function(abstract, name):
            raise ValueError('Residual formula mismatch: ' + name)
    source_global = function(source, 'globalBuild2')
    # Each replacement is a separately stated upper-bound interpretation.
    replacements = [
        ('[...new Set(vertices.map(v=>v[0]))]', '[0,1,2,3,4]'),
        ('rf=X.map(x=>jd(ja(jm(x,x),jo),jscale(jm(x,js(jm(x,x),jo)),R(2n)))),ga=X.map(x=>ji(jm(x,js(jm(x,x),jo))))',
         'rf=X.map((x,a)=>lineJet(a)),ga=X.map((x,a)=>lineJet(a))'),
        ('mul(mask[a],rf[a][0])', '(mask&(1<<a))?rf[a][0]:z'),
        ('gamma=jscale(ga[a],mask[a])', 'gamma=mask&(1<<a)?ga[a]:jz'),
        ('const q=(i,j,a)=>jd(jc(sub(charts[j].mask[a],charts[i].mask[a])),X[a]);',
         'const q=(i,j,a)=>lineJet(a);'),
        ('mtraceProduct(Ai.B,Bj.B)', 'mtrace(mtimes(Ai.B,Bj.B))'),
        ('mtraceProduct(Bi.B,Aj.B)', 'mtrace(mtimes(Bi.B,Aj.B))'),
        ('return{g,u12,u34,charts,bcoef};}',
         'return{g,u12,u34,charts,bcoef,gamma:base.gamma,delta:base.delta,ev:base.ev};}'),
    ]
    for before, after in replacements:
        if source_global.count(before) != 1:
            raise ValueError('Unexpected source replacement count: ' + before)
        source_global = source_global.replace(before, after)
    if source_global != function(abstract, 'globalBuild2'):
        raise ValueError('Unaccounted source/bound-graph difference')
    construction = ('const U0=horiz(gamma,I,mtimes(H1,W)),Q0=vert(H0,P,mtimes(L,delta)),')
    construction += 'U1=horiz(W,eta),Q1=vert(L,ev);'
    if construction not in function(source, 'build2') or construction not in function(abstract, 'build2'):
        raise ValueError('Physical split-block construction mismatch')
    trace = 'function mtraceProduct(A,B){let sum=jz;for(let i=0;i<A.length;i++)for(let j=0;j<A[i].length;j++)sum=ja(sum,jm(A[i][j],B[j][i]));return sum}'
    if function(source, 'mtraceProduct') != trace:
        raise ValueError('Trace-product identity mismatch')
    return {'status': 'PASS', 'identicalResidualFunctions': ['crossResidual', 'globalCross'],
            'explicitGlobalBuildReplacements': len(replacements), 'physicalBlockConstructionMatched': True,
            'publicGeneratorSHA256': pins['publicGeneratorSHA256'],
            'publicFileCompared': public_generator is not None,
            'scope': 'Formula alignment; primitive and line upper bounds are checked separately.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--public-generator', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.public_generator), indent=2))
