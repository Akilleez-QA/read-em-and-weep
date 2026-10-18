import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from inputs import load_inputs, require
'Read/parse production source only. No production import or execution.\nInterprets the restricted raw scalar AST in an invented free trace-symbol ring.\n'
import ast, copy, hashlib, json
from fractions import Fraction as F
from pathlib import Path
HERE = Path(__file__).resolve().parent

class P:

    def __init__(self, terms=None):
        self.t = {k: v for k, v in (terms or {}).items() if v}

    @staticmethod
    def scalar(c):
        return P({(): F(c)})

    @staticmethod
    def atom(s):
        return P({(s,): F(1)})

    def __add__(self, b):
        d = self.t.copy()
        for k, v in b.t.items():
            d[k] = d.get(k, F(0)) + v
        return P(d)

    def __neg__(self):
        return P({k: -v for k, v in self.t.items()})

    def __sub__(self, b):
        return self + -b

    def __mul__(self, b):
        d = {}
        for k, v in self.t.items():
            for l, w in b.t.items():
                m = tuple(sorted(k + l))
                d[m] = d.get(m, F(0)) + v * w
        return P(d)

    def __eq__(self, b):
        return self.t == b.t

def tr(*word):
    return P.atom('tr(' + ','.join(word) + ')')

def path(n):
    if isinstance(n, ast.Name):
        return n.id
    if isinstance(n, ast.Attribute):
        return path(n.value) + '.' + n.attr
    raise ValueError(ast.dump(n))

def ev(n, e):
    if isinstance(n, ast.Constant):
        return n.value
    if isinstance(n, ast.Name):
        return e[n.id]
    if isinstance(n, ast.Tuple):
        return tuple((ev(x, e) for x in n.elts))
    if isinstance(n, ast.Subscript):
        return ev(n.value, e)[ev(n.slice, e)]
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
        return -ev(n.operand, e)
    if isinstance(n, ast.BinOp):
        a, b = (ev(n.left, e), ev(n.right, e))
        if isinstance(n.op, ast.Add):
            return a + b
        if isinstance(n.op, ast.Sub):
            return a - b
        if isinstance(n.op, ast.Mult):
            return a * b
    if isinstance(n, ast.Call):
        args = []
        for a in n.args:
            if isinstance(a, ast.Starred):
                args.extend(ev(a.value, e))
            else:
                args.append(ev(a, e))
        name = path(n.func)
        if name == 'Q':
            return F(*args)
        if name == 'mat.ex.scalar':
            return P.scalar(*args)
        if name == 'zip':
            return tuple(zip(*args))
        if name == 'mat.mul':
            return tuple(args)
        if name == 'mat.trace':
            word = args[0] if isinstance(args[0], tuple) else (args[0],)
            return ((tr(*word),),)
    raise ValueError('Unapproved AST: ' + ast.dump(n))

def assign(n, v, e):
    if isinstance(n, ast.Name):
        e[n.id] = v
        return
    if isinstance(n, ast.Tuple):
        require(len(n.elts) == len(v), 'static/formal check failed at original checker line 68')
        for x, y in zip(n.elts, v):
            assign(x, y, e)
        return
    raise ValueError('Unapproved assignment')

def run_statements(body, e):
    for n in body:
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str):
            continue
        if isinstance(n, ast.Assign):
            require(len(n.targets) == 1, 'static/formal check failed at original checker line 76')
            assign(n.targets[0], ev(n.value, e), e)
        elif isinstance(n, ast.For):
            require(not n.orelse, 'static/formal check failed at original checker line 78')
            for v in ev(n.iter, e):
                assign(n.target, v, e)
                run_statements(n.body, e)
        elif isinstance(n, ast.Return):
            return ev(n.value, e)
        else:
            raise ValueError('Unapproved statement: ' + ast.dump(n))

def interpret(fn):
    e = {'qa': P.atom('qa'), 'qb': P.atom('qb'), 'blocks_i': (tuple(('Ai' + str(k) for k in range(4))), tuple(('Bi' + str(k) for k in range(4)))), 'blocks_j': (tuple(('Aj' + str(k) for k in range(4))), tuple(('Bj' + str(k) for k in range(4))))}
    return run_statements(fn.body, e)

def expected():
    qa, qb = (P.atom('qa'), P.atom('qb'))
    out = -P.scalar(F(15, 8)) * qa * qb
    for n, (weight, sign) in enumerate([(-1, -1), (1, 1), (3, -1), (5, 1)]):
        ai, bi, aj, bj = [prefix + str(n) for prefix in ('Ai', 'Bi', 'Aj', 'Bj')]
        out = out + P.scalar(F(sign, 4)) * (tr(ai, bj) - tr(bi, aj))
        out = out + P.scalar(F(sign * weight, 8)) * (qa * tr(bi) + qa * tr(bj) - qb * tr(ai) - qb * tr(aj))
    return out

def main():
    pins, sources = load_inputs(('raw_engine', 'source_formulas', 'first_order', 'denotation', 'field', 'compiler'))
    raw = sources['raw_engine']
    tree = ast.parse(raw)
    fn = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'raw_scalar_formula'))
    got = interpret(fn)
    want = expected()
    require(got == want, 'static/formal check failed at original checker line 101')
    require(len(got.t) == 25, 'static/formal check failed at original checker line 102')
    changes = [('gerbe coefficient', 'Q(15,8)', 'Q(15,4)'), ('outer factor', 'Q(1,4)', 'Q(1,2)'), ('theta half', 'Q(1,2)', 'Q(1,1)'), ('block weight', '(-1,1,3,5)', '(-1,1,3,4)'), ('supertrace sign', '(-1,1,-1,1)', '(1,1,-1,1)'), ('j endpoint trace', 'mat.trace(b_j)[0][0]', 'mat.trace(b_i)[0][0]'), ('ordered wedge word', 'mat.mul(a_i,b_j)', 'mat.mul(b_j,a_i)')]
    segment = ast.get_source_segment(raw, fn)
    rejected = []
    for name, old, new in changes:
        require(old in segment, 'static/formal check failed at original checker line 111')
        mutant = ast.parse(segment.replace(old, new, 1)).body[0]
        require(interpret(mutant) != want, name)
        rejected.append(name)
    result = {'status': 'PASS', 'scope': 'AST-only free ordered-trace polynomial identity; no physical execution', 'source_files_hashed': len(pins), 'independent_monomials': len(got.t), 'negative_controls_rejected': rejected, 'physical_execution': False, 'whole_model_correctness': False, 'ID0_zero_claim': False}
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()
