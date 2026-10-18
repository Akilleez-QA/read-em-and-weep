"""Independent text/AST review only; never imports or executes reviewed source."""
from pathlib import Path
import argparse, ast, difflib, hashlib, json
ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root', type=Path, required=True, help='Directory containing pinned codex-swarm source subdirectories')
BASE = parser.parse_args().source_root.resolve()

def need(ok, message):
    if not ok:
        raise ValueError(message)

manifest = json.loads((ROOT / 'public-pins.json').read_text())
patch = ''
for row in manifest['changed_files']:
    old = (BASE / row['path']).read_text()
    new = (ROOT / row['candidate_text']).read_text()
    patch += ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                       fromfile='a/' + row['path'], tofile='b/' + row['path']))
need(patch == (ROOT / 'candidate.patch').read_text(), 'patch does not equal candidate diff')
for row in manifest['frozen_sources']:
    raw = (BASE / row['path']).read_bytes()
    need(len(raw) == row['bytes'], 'source length mismatch')
    need(hashlib.sha256(raw).hexdigest() == row['sha256'], 'source SHA mismatch')
    need(hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == row['git_blob'], 'source blob mismatch')
record = manifest['id0']
raw = (ROOT / record['path']).read_bytes()
need(hashlib.sha256(raw).hexdigest() == record['sha256'], 'retained record digest mismatch')
need(json.loads(raw)['requests'][0] == record['id0'], 'retained ID0 payload mismatch')
for term in record['id0']['terms']:
    m = term['dual_monomial']
    need(term['laurent_exponents'] == [-v - 1 for v in m], 'Serre exponent mismatch')
    need(term['output_index'] == sum((2-v)*3**(3-i) for i, v in enumerate(m)), 'output index mismatch')
field = ast.parse((ROOT / 'candidate-text/exact-curve-field/field.py.txt').read_text())
program = ast.parse((ROOT / 'candidate-text/detector-realization/program.py.txt').read_text())
def definition(tree, name):
    return next(n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name == name)
entry = definition(program, 'actual_id0')
need(not entry.decorator_list and not entry.args.kw_defaults, 'entry signature executable addition')
need(len(entry.args.defaults) == 1 and isinstance(entry.args.defaults[0], ast.Constant) and entry.args.defaults[0].value is None, 'entry default changed')
need(isinstance(entry.body[0], ast.Raise), 'entry first statement changed')
# A yield anywhere in the public function scope would defer refusal. The only
# nested function is independently excluded, since its yield does not do that.
def public_walk(node):
    yield node
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
            continue
        yield from public_walk(child)
need(not any(isinstance(n, (ast.Yield, ast.YieldFrom, ast.Await)) for n in public_walk(entry)), 'public refusal deferred')
cert = definition(field, 'LaurentCertificate')
context = definition(field, 'LaurentContext')
for cls in (cert, context):
    decoration = cls.decorator_list[0]
    need({k.arg: ast.literal_eval(k.value) for k in decoration.keywords} == dict(frozen=True, slots=True, init=False, eq=False), 'immutable class convention changed')
check = definition(cert, '_check')
need(ast.unparse(check.body[0]) == 'self.ex.check()', 'poison check absent')
need('rational is not self.rational or context is not self.context' in ast.unparse(check), 'identity checks absent')
need('rational.ex is not self.ex or context.ex is not self.ex or self.quotient.ex is not self.ex' in ast.unparse(check), 'Execution identity absent')
method = definition(definition(field, 'Rational'), 'certify_laurent')
need('quotient, remainder = self.numerator.divide(residual)' in ast.unparse(method), 'complete division changed')
need('if not remainder.is_zero():' in ast.unparse(method), 'remainder rejection absent')
need('return LaurentCertificate(_LAURENT_SEAL, self, context, d, quotient)' in ast.unparse(method), 'retention changed')
print('PASS: exact patch/candidate equivalence; frozen lengths, SHA256 and Git blob IDs; retained record digest.')
print('PASS: public function has inert defaults, no decorators or public-scope yield/await; direct first raise.')
print('PASS: frozen certificate/context convention; poison, rational/context/Execution identity and quotient retention checks.')
print('LIMIT: static verification only; no candidate/production execution, numeric result, source authentication or physical release.')
