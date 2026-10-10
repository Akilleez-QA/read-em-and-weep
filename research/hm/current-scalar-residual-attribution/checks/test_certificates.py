#!/usr/bin/env python3
"""Small altered-input rejection checks; original files are never modified."""
import copy
import json
from pathlib import Path
import tempfile

from verify_character_report import verify as verify_rank_report
from verify_determinants import verify_model
from verify_source import verify as verify_source


def verify(geometric, ranks):
    rejected = []

    def reject(label, action):
        try:
            action()
        except (ValueError, KeyError):
            rejected.append(label)
        else:
            raise ValueError('Altered fixture accepted: '+label)

    model = json.loads((geometric/'data/model.json').read_text())
    bad = copy.deepcopy(model)
    bad['charts'][0]['P'][0][0][0][1] += 1
    reject('changed transition numerator', lambda: verify_model(bad))
    bad = copy.deepcopy(model)
    bad['charts'][0]['dp'] = []
    reject('zero transition denominator', lambda: verify_model(bad))
    bad = copy.deepcopy(ranks)
    bad['perCharacterH1BySupportSize'][2] = 1
    reject('changed weight-two Ext1', lambda: verify_rank_report(bad))
    bad = copy.deepcopy(ranks)
    bad['classicalMatrixEntryIdentities'] -= 1
    reject('incomplete classical matrix tie', lambda: verify_rank_report(bad))
    with tempfile.TemporaryDirectory(prefix='residual-fixture-') as directory:
        fixture = Path(directory)
        (fixture/'data').mkdir()
        for name in ['model.json','source-formulas.js']:
            (fixture/'data'/name).write_bytes((geometric/'data'/name).read_bytes())
        source = fixture/'data/source-formulas.js'
        source.write_text(source.read_text().replace('R(15n,8n)','R(15n,4n)',1))
        reject('changed transgression normalization', lambda: verify_source(fixture))
        source.write_bytes((geometric/'data/source-formulas.js').read_bytes())
        (fixture/'data/model.json').write_text(json.dumps(bad))
        reject('replaced geometric model', lambda: verify_source(fixture))
    return {'status':'PASS','rejectedAlterations':rejected,'count':len(rejected)}
