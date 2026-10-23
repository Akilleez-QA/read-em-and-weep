"""Static/provenance tests first; optional bounded universal namespace smoke."""
import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import symtable
import builtins
import sys
import tempfile
import time
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / 'q-middle-candidate-interface'
sys.dont_write_bytecode = True

def load():
    spec = importlib.util.spec_from_file_location('explicit_initializer', HERE / 'initializer.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def nodes(path):
    return ast.parse(path.read_text()).body

def digest_ast(body):
    return hashlib.sha256('\n'.join(ast.dump(n, include_attributes=False) for n in body).encode()).hexdigest()

class StaticTests(unittest.TestCase):
    def test_01_provenance(self):
        self.assertEqual(load().validate_dependencies(), 80)
        manifest = json.loads((ROOT / 'HANDOFF-MANIFEST.json').read_text())
        self.assertEqual(load().PINNED_FILES, {r['path']: r['sha256'] for r in manifest['files']})

    def test_02_import_side_effect(self):
        # Import must succeed even when all symbolic and historical imports fail.
        code = '''import builtins, importlib.util, sys
sys.dont_write_bytecode=True
original=builtins.__import__
def guard(name,*a,**kw):
    if name == 'sympy' or name.startswith(('universal_', 'verify_', 'derive_')):
        raise AssertionError('forbidden import: '+name)
    return original(name,*a,**kw)
builtins.__import__=guard
spec=importlib.util.spec_from_file_location('candidate',sys.argv[1])
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
assert 'sympy' not in sys.modules
'''
        r = subprocess.run([sys.executable, '-B', '-c', code, str(HERE / 'initializer.py')], capture_output=True, text=True, timeout=10)
        self.assertEqual((r.returncode, r.stdout, r.stderr), (0, '', ''))
        # The deterministic negative fixture proves the guard rejects symbolic imports.
        bad = code.replace("spec.loader.exec_module(m)", "spec.loader.exec_module(m)\nimport sympy")
        r = subprocess.run([sys.executable, '-B', '-c', bad, str(HERE / 'initializer.py')], capture_output=True, text=True, timeout=10)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn('forbidden import: sympy', r.stderr)

    def test_03_exact_statement_extraction(self):
        receipt = json.loads((HERE / 'receipt.json').read_text())
        functions = {n.name: n for n in nodes(HERE / 'initializer.py') if isinstance(n, ast.FunctionDef)}
        body = functions['build_namespace'].body
        cursor = 5  # docstring, validation, sympy, combinations, comb
        for item in receipt['comparison']:
            expected = nodes(ROOT / item['path'])[item['body_start']:item['body_stop']]
            self.assertEqual(digest_ast(expected), item['ast_sha256'])
            if item['path'].startswith('derive_'):
                self.assertEqual(ast.unparse(body[cursor]), 'ns = _complete_symbols()')
                cursor += 1
            actual = body[cursor:cursor + len(expected)]
            self.assertEqual(digest_ast(actual), digest_ast(expected), item['path'])
            cursor += len(expected)
        self.assertIsInstance(body[cursor], ast.Return)
        item = receipt['complete_symbols']
        expected = nodes(ROOT / item['path'])[item['body_start']:item['body_stop']]
        self.assertEqual(digest_ast(expected), item['ast_sha256'])
        self.assertEqual(digest_ast(functions['_complete_symbols'].body[1:-1]), digest_ast(expected))
        # Constructor equality under the documented self/API renames only.
        source = next(n for n in nodes(ROOT / receipt['constructor']['path']) if isinstance(n, ast.ClassDef))
        expected = source.body[0].body[2:]
        api_names = set(receipt['constructor']['api_names'])
        class Rename(ast.NodeTransformer):
            def visit_Name(self, n):
                if n.id == 'self':
                    return ast.Name(id='instance', ctx=n.ctx)
                if n.id in api_names:
                    return ast.Attribute(value=ast.Name(id='api', ctx=ast.Load()), attr=n.id, ctx=n.ctx)
                return n
        expected = [Rename().visit(n) for n in expected]
        self.assertEqual(digest_ast(functions['initialize_sparse'].body[3:-2]), digest_ast(expected))

    def test_04_no_dynamic_execution_or_jobs(self):
        tree = ast.parse((HERE / 'initializer.py').read_text())
        for n in ast.walk(tree):
            if isinstance(n, ast.Call):
                self.assertNotIn(ast.unparse(n.func), ('exec', 'eval', 'compile', '__import__', 's.linsolve'))
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                names = [a.name for a in n.names] if isinstance(n, ast.Import) else [n.module]
                self.assertFalse(any(x.startswith(('universal_', 'verify_', 'derive_')) for x in names))
        # Only definitions, literal constants and the inert Path expression at import.
        for n in tree.body:
            self.assertIsInstance(n, (ast.Expr, ast.Import, ast.ImportFrom, ast.Assign, ast.FunctionDef))
        frozen = (ROOT / 'verify_sparse_q_middle_source_adapter.py').read_text()
        self.assertIn('sp.SourceMap.source_map=forbidden', frozen)
        self.assertIn('Old supported source_map must not receive new qB middle data.', frozen)

    def test_05_no_unbound_constructor_globals(self):
        table = symtable.symtable((HERE / 'initializer.py').read_text(), 'initializer.py', 'exec')
        allowed = set(vars(builtins)) | set(table.get_identifiers())
        def check(table):
            for symbol in table.get_symbols():
                if symbol.is_referenced() and symbol.is_global():
                    self.assertIn(symbol.get_name(), allowed)
            for child in table.get_children():
                check(child)
        check(table)

    def test_06_tampered_dependency_and_legacy(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            # First pinned input is enough: validation must stop before any construction.
            name = next(iter(module.PINNED_FILES))
            path = Path(directory) / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b'tampered dependency\n')
            with self.assertRaisesRegex(ValueError, 'Dependency hash mismatch'):
                module.build_namespace(directory)
        with self.assertRaisesRegex(AssertionError, 'Old supported source_map'):
            module.forbidden_legacy_call(None)
        self.assertEqual(len(module.error_schemas()), 26)

def smoke():
    # Limits are established before any SymPy import or construction.
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (1536 * 1024**2, 1536 * 1024**2))
    import sympy as s
    m = load()
    ns = m.build_namespace()
    assert ns['cliff'] * ns['spin'] == s.eye(2)
    assert ns['Kinc'] * ns['extract'] == ns['Pi']
    assert ns['B6'].T * ns['J6'] * ns['B6'] == ns['JB']
    assert ns['fmat'] * ns['finv'] == s.eye(4)
    assert ns['theta'].is_nonzero and all(ns[n].is_nonzero for n in ('FB', 'FC', 'FD'))
    assert ns['ns']['build_symbols'].__closure__ is not None
    assert len(m.error_schemas()) == 26
    assert not any(n in ns for n in ('rq_symbols', 'rh_symbols', 'Theta', 'sol', 'pars', 'Q6', 'spsol'))
    # Inventory every mathematical local; retained helper functions are not invoked here.
    inventory = {k: type(v).__name__ for k, v in ns.items() if k not in ('root',)}
    print(json.dumps({'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(), 'sympy': s.__version__, 'sympy_file': s.__file__, 'namespace_inventory': inventory, 'complete_namespace_inventory': sorted(ns['ns']), 'checks': 'universal namespace assertions only; no sparse adapter execution'}, sort_keys=True))

if __name__ == '__main__':
    if '--child-smoke' in sys.argv:
        smoke()
    elif '--smoke' in sys.argv:
        command = [sys.executable, '-B', str(Path(__file__).resolve()), '--child-smoke']
        start = time.monotonic()
        r = subprocess.run(command, capture_output=True, text=True, timeout=75, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
        usage = resource.getrusage(resource.RUSAGE_CHILDREN)
        record = {'command': command, 'elapsed_seconds': time.monotonic()-start, 'exit_status': r.returncode, 'peak_rss_native': usage.ru_maxrss, 'peak_rss_units': 'bytes' if sys.platform == 'darwin' else 'KiB', 'cpu_limit_seconds': 60, 'address_space_limit_bytes': 1536*1024**2, 'stdout': r.stdout, 'stderr': r.stderr, 'code_hashes': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (HERE/'initializer.py', HERE/'test_initializer.py')}, 'input_hashes': load().PINNED_FILES}
        receipt = json.loads((HERE/'receipt.json').read_text())
        receipt['executions'].append(record)
        (HERE/'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
        print(json.dumps(record, indent=2))
        sys.exit(0 if r.returncode == 0 else 1)
    else:
        unittest.main()
