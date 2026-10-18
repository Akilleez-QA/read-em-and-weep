"""Portable static selector check. Production inputs are inert text only."""
import ast
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PINS = {
    'inputs/model.json': '635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926',
    'inputs/weighted_assignment.py.txt': '0305531da407de19fe40be7ceb7bfff76d94bbe8d2b05893dd1d76240dacf486',
}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def check_pin(data, expected):
    require(hashlib.sha256(data).hexdigest() == expected, 'input pin mismatch')

def check_model(model):
    zero = []
    require(model['gamma'][5] == [zero, [['0,0,1,0', -1]], zero, zero, [['0,1,0,0', -1]]], 'gamma selector row')
    require([row[3] for row in model['ev']] == [[['0,0,1,0', 1]], zero], 'ev column 3')
    require([row[2] for row in model['ev']] == [[['0,1,0,0', 1]], zero], 'ev column 2')

def dump(node):
    return ast.dump(node, include_attributes=False)

def check_selector(source):
    tree = ast.parse(source)
    require(len(tree.body) == 1 and isinstance(tree.body[0], ast.FunctionDef)
            and tree.body[0].name == 'weighted_assignment', 'source function')
    assignments = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            assignments.setdefault(node.targets[0].id, []).append(node.value)
    expected = {'X13': 'blocks[(3, 1)]', 'X02': 'blocks[(2, 0)]',
                'scalar': 'X13[5][0] + X02[1][3] + X02[4][2]'}
    for name, expression in expected.items():
        values = assignments.get(name, [])
        require(len(values) == 1 and dump(values[0]) == dump(ast.parse(expression, mode='eval').body), 'selector assignment ' + name)

def rejects(action):
    try:
        action()
    except ValueError:
        return
    raise ValueError('negative control accepted')

raw = {name: (ROOT / name).read_bytes() for name in PINS}
for name, expected in PINS.items():
    check_pin(raw[name], expected)
model = json.loads(raw['inputs/model.json'])
source = raw['inputs/weighted_assignment.py.txt'].decode()
check_model(model)
check_selector(source)
# Corruption is rejected by an anchored input hash.
rejects(lambda: check_pin(raw['inputs/model.json'] + b' ', PINS['inputs/model.json']))
# These separately exercise the semantic checks, without relying on a hash failure.
bad = copy.deepcopy(model)
bad['gamma'][5][1][0][1] = 1
rejects(lambda: check_model(bad))
bad_source = source.replace('X02[4][2]', 'X02[4][3]')
require(bad_source != source, 'source mutation occurred')
rejects(lambda: check_selector(bad_source))
print(json.dumps({
    'status': 'PASS',
    'scope': 'bundled selector source AST and pinned model literals only',
    'selector_identity': 'four scalar terms cancel by commutativity, as proved in PROOF.md',
    'negative_pin_rejected': True,
    'negative_model_mutation_rejected': True,
    'negative_selector_mutation_rejected': True,
    'full_composition_mechanically_verified': False,
    'geometric_premises_discharged': False,
    'production_imports': False,
    'physical_evaluation': False,
    'polynomial_products': 0,
}, indent=2, sort_keys=True))
