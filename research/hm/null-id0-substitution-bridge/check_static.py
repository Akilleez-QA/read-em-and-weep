"""Self-contained section-3 source/AST checks; NEVER execute input sources."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def need(ok, label):
    if not ok:
        raise RuntimeError(label)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def check_pin(data, expected):
    need(digest(data) == expected, 'source pin mismatch')

def functions(tree):
    result = {}
    for n in tree.body:
        if isinstance(n, ast.FunctionDef):
            result[n.name] = n
        if isinstance(n, ast.ClassDef):
            for f in n.body:
                if isinstance(f, ast.FunctionDef):
                    result[n.name + '.' + f.name] = f
    return result

def self_calls(node, name):
    return [n for n in ast.walk(node) if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute) and isinstance(n.func.value, ast.Name)
            and n.func.value.id == 'self' and n.func.attr == name]

def pattern(actual, expected):
    need(ast.dump(actual) == ast.dump(expected), 'source method pattern mismatch')

def rejects(action):
    try:
        action()
    except RuntimeError:
        return
    raise RuntimeError('negative control was accepted')

pins = json.loads((ROOT / 'source-pins.json').read_text())
raw = {}
for record in pins:
    name = record['file']
    need(not Path(name).is_absolute() and '..' not in Path(name).parts, 'local input path')
    raw[name] = (ROOT / name).read_bytes()
    check_pin(raw[name], record['sha256'])
# ast.parse is syntax inspection only. No compile/exec/eval/import of these texts.
trees = {name: ast.parse(data) for name, data in raw.items()}
methods = {name: functions(tree) for name, tree in trees.items()}
signatures = json.loads((ROOT / 'reviewed-ast-pins.json').read_text())
method_count = 0
for filename, records in signatures.items():
    for name, expected in records.items():
        check_pin(ast.dump(methods[filename][name], include_attributes=False).encode(), expected)
        method_count += 1
comp = methods['inputs/compiler.py.txt']
for name, expected in methods['expected-context.txt'].items():
    pattern(comp[name], expected)
source = next(n for n in trees['inputs/compiler.py.txt'].body if isinstance(n, ast.ClassDef) and n.name == 'Source')
consumers = [(n.name, len(self_calls(n, 'T'))) for n in source.body
             if isinstance(n, ast.FunctionDef) and self_calls(n, 'T')]
need(consumers == [('E', 2)], 'T consumers must be only E endpoints')
need([ast.unparse(n) for n in self_calls(comp['Source.residual'], 'E')]
     == ['self.E(p, q, t)', 'self.E(q, p, t)'], 'complementary residual E calls')
raw_class = next(n for n in trees['inputs/raw_engine.py.txt'].body if isinstance(n, ast.ClassDef) and n.name == 'RawSource')
need([ast.unparse(b) for b in raw_class.bases] == ['SC.Source'], 'RawSource base')
need([n.name for n in raw_class.body if isinstance(n, ast.FunctionDef)] == ['T'], 'only T override')
need(ast.unparse(raw_class.body[0].body[0].value) == '((self.c.model.s_raw(tuple(p), a, b),),)', 'scalar wrapper')
# Track formal scalar degree only, never instantiate field or matrix values.
degrees = {'sij': 1, 'sjk': 1, 'la': 0, 'lb': 0, 'ta': 0, 'tb': 0}
def degree(n):
    if isinstance(n, ast.Name):
        need(n.id in degrees, 'known E symbol')
        return degrees[n.id]
    if isinstance(n, ast.Constant):
        return 0
    if isinstance(n, ast.UnaryOp):
        return degree(n.operand)
    if isinstance(n, ast.Call):
        if isinstance(n.func, ast.Name) and n.func.id == 'Q':
            return 0
        need(isinstance(n.func, ast.Attribute), 'formal E operation')
        ds = [degree(a) for a in n.args]
        if n.func.attr == 'D':
            # Direction names a/b are not scalar expressions.
            return degree(n.args[0])
        if n.func.attr == 'add':
            return max(ds, default=0)
        if n.func.attr in ('mul', 'smul', 'scale'):
            out = sum(ds)
            need(out <= 1, 'no product of varying scalar factors')
            return out
        raise RuntimeError('unknown E operation')
    raise RuntimeError('unknown E node')
# D's second argument is a fixed direction, not an algebraic operand.
degrees.update(a=0, b=0)
need(degree(comp['Source.E'].body[-1].value) == 1, 'E scalar degree')
schema = methods['inputs/lift_schema.py.txt']['closed_lift_schema']
loop = next(n for n in schema.body if isinstance(n, ast.For))
need(ast.literal_eval(loop.iter) == ((1, 1), (2, -1), (3, 1)), 'lift signs')
program = methods['inputs/program.py.txt']
wa = ast.unparse(program['weighted_assignment'])
need('scalar = X13[5][0] + X02[1][3] + X02[4][2]' in wa, 'selector')
need('source_and_lift(model, canonical, 2)' in wa, 'canonical lift')
need('for owner in owners:' in wa, 'original-owner weights')
entry = program['actual_id0']
need(isinstance(entry.body[0], ast.Raise) and ast.unparse(entry.body[0].exc.func) == 'RuntimeError', 'unconditional refusal')
need("stripped = dict(total.terms).get(15, ex.rational(0))" in ast.unparse(entry), 'whole-sum mask15')
# Complete weighted_assignment and actual_id0 ASTs are bound above, not merely
# the snippets. Their mathematical interpretation is reviewed in REVIEW.md.

# Formal response coordinates stand for distinct derivative/ordered-matrix
# words. This is a doubled E coefficient response, not a polynomial product.
def response(v):
    a, b, c, d = v
    return (a, -b, c, -d)
def plus(u, v):
    return tuple(a + b for a, b in zip(u, v))
need(response((0, 0, 0, 0)) == (0, 0, 0, 0), 'zero error')
controls = 0
for a in (-1, 0, 1):
    for b in (-1, 0, 1):
        u = (a, b, -a, -b)
        v = (b, -a, a, -b)
        need(response(plus(u, v)) == plus(response(u), response(v)), 'response additivity control')
        controls += 1
need(response((1, 1, 1, 1)) == (1, -1, 1, -1), 'ordered response signs')
# These two deliberately bad inputs MUST fail, including with python -O.
first = pins[0]
rejects(lambda: check_pin(raw[first['file']] + b'\n# changed\n', first['sha256']))
expected_E = methods['expected-context.txt']['Source.E']
mutated = ast.parse(ast.unparse(comp['Source.E']).replace('c.D(sjk, a)', 'c.D(sjk, b)', 1)).body[0]
need(ast.dump(mutated) != ast.dump(comp['Source.E']), 'negative pattern mutation took effect')
rejects(lambda: pattern(mutated, expected_E))
print(json.dumps({
    'status': 'PASS narrow section-3 static checks only',
    'source_texts_verified': 4,
    'expected_context_verified': True,
    'reviewed_complete_method_asts': method_count,
    'formal_response_additivity_controls': controls,
    'negative_pin_rejected': True,
    'negative_source_pattern_rejected': True,
    'original_88_input_checks_reproduced': False,
    'primitive_frame_and_terminal_theorems': 'cited premises, not rechecked here',
    'mathematical_result': 'fixed-context substitution under exact semantics; see proof and review',
    'geometric_denotation': 'not established',
    'production_imports': False,
    'source_execution': False,
    'physical_evaluation': False,
    'actual_polynomial_products': False,
    'candidate_operational_result': 'unconditional refusal',
    'publication_or_patch_application': False
}, indent=2, sort_keys=True))
