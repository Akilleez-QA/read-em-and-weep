"""Stdlib-only checks. Never call a mathematical factory."""
import ast
import builtins
import hashlib
import importlib.util
import json
from pathlib import Path
import symtable
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
PAYLOAD = HERE.with_name('q-middle-candidate-interface')
RECORD = json.loads((HERE / 'provenance.json').read_text())
CODE = (HERE / 'safe_context.py').read_text()


def original_blocks():
    blocks = []
    for name, record in RECORD['blocks'].items():
        tree = ast.parse((PAYLOAD / name).read_text())
        if name.startswith('verify_'):
            nodes = [n for n in tree.body[1:] if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name) and n.value.func.id == 'print')]
        else:
            start = next(i for i, n in enumerate(tree.body) if isinstance(n, ast.Assign) and ast.unparse(n.targets[0]) == 'G')
            nodes = tree.body[start:-1]
            assert isinstance(tree.body[-1], ast.If)
            assert ast.unparse(tree.body[-1].test) == "__name__ == '__main__'"
        assert [[n.lineno, n.end_lineno] for n in nodes] == record['lines']
        blocks.append(nodes)
    return blocks


def exact(candidate):
    tree = ast.parse(candidate)
    factory = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_construct')
    branch = next(n for n in factory.body if isinstance(n, ast.If))
    actual = [factory.body[2:factory.body.index(branch)], branch.body]
    for got, want in zip(actual, original_blocks()):
        if ast.dump(ast.Module(body=got, type_ignores=[])) != ast.dump(ast.Module(body=want, type_ignores=[])):
            raise ValueError('Extraction differs')
    return factory


def bindings(candidate):
    """Compare every function/lambda/comprehension scope against combined exec globals."""
    reference = 'from math import comb\n' + '\n'.join(ast.unparse(n) for block in original_blocks() for n in block)
    old = symtable.symtable(reference, '<reference>', 'exec')
    new = next(t for t in symtable.symtable(candidate, '<candidate>', 'exec').get_children() if t.get_name() == '_construct')
    bound = {s.get_name() for s in old.get_symbols() if s.is_assigned() or s.is_imported()}
    def compare(a, b):
        assert a.get_name() == b.get_name()
        assert set(a.get_identifiers()) <= set(b.get_identifiers())
        # A nested global becomes a cell transitively threaded through its parents.
        descendants = []
        def collect(t):
            descendants.extend(x.get_name() for x in t.get_symbols() if x.is_global())
            for child in t.get_children():
                collect(child)
        collect(a)
        for name in set(b.get_identifiers()) - set(a.get_identifiers()):
            assert name in bound and name in descendants and b.lookup(name).is_free()
        for name in a.get_identifiers():
            left, right = a.lookup(name), b.lookup(name)
            if left.is_global() and name in bound:
                assert right.is_free(), (a.get_name(), name)
            else:
                assert (left.is_local(), left.is_free(), left.is_global()) == (right.is_local(), right.is_free(), right.is_global()), (a.get_name(), name)
        assert len(a.get_children()) == len(b.get_children())
        for aa, bb in zip(a.get_children(), b.get_children()):
            compare(aa, bb)
    # The factory's dictionary comprehension is infrastructure, outside the copied blocks.
    children = new.get_children()
    if children and children[-1].get_name() == 'dictcomp':
        children = children[:-1]
    assert len(old.get_children()) == len(children)
    for a, b in zip(old.get_children(), children):
        compare(a, b)


class StaticTests(unittest.TestCase):
    def test_pins(self):
        for name, digest in RECORD['inputs'].items():
            self.assertEqual(hashlib.sha256((PAYLOAD / name).read_bytes()).hexdigest(), digest)
        for block, record in zip(original_blocks(), RECORD['blocks'].values()):
            self.assertEqual(hashlib.sha256('\n'.join(ast.dump(n, include_attributes=False).replace(', type_params=[]', '') for n in block).encode()).hexdigest(), record['ast_sha256'])

    def test_exact_and_bindings(self):
        exact(CODE)
        bindings(CODE)

    def test_complete_exports_and_obligations(self):
        reference = 'from math import comb\n' + '\n'.join(ast.unparse(n) for block in original_blocks() for n in block)
        table = symtable.symtable(reference, '<reference>', 'exec')
        class ModuleBindings(ast.NodeVisitor):
            def __init__(self):
                self.names = set()
            def visit_Name(self, node):
                if isinstance(node.ctx, ast.Store):
                    self.names.add(node.id)
            def visit_FunctionDef(self, node):
                self.names.add(node.name)
            def visit_Import(self, node):
                self.names.update(a.asname or a.name.split('.')[0] for a in node.names)
            def visit_ImportFrom(self, node):
                self.names.update(a.asname or a.name for a in node.names)
            def visit_ListComp(self, node):
                pass
            visit_DictComp = visit_SetComp = visit_GeneratorExp = visit_Lambda = visit_ListComp
        collector = ModuleBindings()
        collector.visit(ast.parse(reference))
        exports = sorted(collector.names)
        self.assertEqual(exports, RECORD['exports'])
        for path in PAYLOAD.glob('*.py'):
            for node in ast.walk(ast.parse(path.read_text())):
                if isinstance(node, ast.ImportFrom) and node.module == 'universal_source_balance_helpers':
                    for alias in node.names:
                        if alias.name != '*':
                            self.assertIn(alias.name, exports, str(path))
        obligations = []
        def visit(node, filename, scope=()):
            if isinstance(node, ast.Assert):
                obligations.append(dict(file=filename, line=node.lineno, scope=list(scope), expression=ast.unparse(node.test)))
            for child in ast.iter_child_nodes(node):
                visit(child, filename, scope + ((node.name,) if isinstance(node, ast.FunctionDef) else ()))
        for filename, block in zip(RECORD['blocks'], original_blocks()):
            for node in block:
                visit(node, filename)
        self.assertEqual(obligations, RECORD['assertions'])

    def test_negative_extraction(self):
        with self.assertRaises(ValueError):
            exact(CODE.replace('assert M * M == Q * s.eye(2)', 'assert True'))
        with self.assertRaises((AssertionError, SyntaxError)):
            bindings(CODE.replace('return [scale(v[i], contract(coords, tau))', 'return [scale(v[i], contract(missing_coords, tau))'))

    def test_import_guard(self):
        real = builtins.__import__
        def guarded(name, *args, **kwargs):
            if name.startswith(('sympy', 'universal_', 'verify_', 'derive_')):
                raise ImportError('Forbidden symbolic/historical import: ' + name)
            return real(name, *args, **kwargs)
        with patch('builtins.__import__', guarded):
            spec = importlib.util.spec_from_file_location('safe_context', HERE / 'safe_context.py')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.validate_inputs()
            with self.assertRaises(ImportError):
                guarded('sympy')
            with tempfile.TemporaryDirectory() as tmp:
                for name in RECORD['inputs']:
                    (Path(tmp) / name).write_bytes((PAYLOAD / name).read_bytes() + b'\n# tampered\n')
                with self.assertRaises(ValueError):
                    module.validate_inputs(tmp)

    def test_no_dynamic_or_historical_edges(self):
        for node in ast.walk(ast.parse(CODE)):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, ('exec', 'eval', 'compile', '__import__'))
            if isinstance(node, ast.ImportFrom):
                self.assertFalse((node.module or '').startswith(('universal_', 'verify_', 'derive_')))
            if isinstance(node, ast.Attribute):
                self.assertNotIn(node.attr, ('modules', 'path_hooks'))


if __name__ == '__main__':
    unittest.main()
