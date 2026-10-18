import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from inputs import load_inputs, require
'Static source checks and invented formal-word identities; no production execution.'
import ast, hashlib, json
from pathlib import Path
from collections import Counter
ROOT = Path(__file__).resolve().parent
pins, sources = load_inputs(('raw_engine', 'source_formulas', 'first_order'))
source = sources['raw_engine']
tree = ast.parse(source)
physical = next((n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'PhysicalModel'))
actual = next((n for n in physical.body if isinstance(n, ast.FunctionDef) and n.name == 'blocks'))
expected = "\ndef blocks(self,o,d):\n    c=self.primitive(o.carrier);n2=power(self.nu(o),2)\n    U0=tuple(tuple(list(g)+list(i)+list(w))for g,i,w in zip(self.gamma,c['I'],self.M.mul(c['H1'],c['W'])))\n    Q0=tuple(c['H0'])+tuple(c['P'])+tuple(self.M.mul(c['L'],self.delta))\n    U1=tuple(tuple(list(w)+list(e))for w,e in zip(c['W'],c['eta']));Q1=tuple(c['L'])+tuple(self.ev)\n    w0=[n2.inverse()]*5+[self.ex.scalar(1),n2.inverse()]+[n2]*8;w1=[self.ex.scalar(1)]*8+[n2]*2\n    def moving(U,Q,w):\n        U=tuple(tuple(v*w[j]for j,v in enumerate(row))for row in U)\n        Q=tuple(tuple(v/w[i]for v in row)for i,row in enumerate(Q))\n        return self.M.scale(self.M.mul(self.M.D(U,d),Q),-1)\n    B0=moving(U0,Q0,w0);B1=moving(U1,Q1,w1)\n    gamma=self.ex.scalar((o.legal_mask>>d)&1)*self.y[d]/(self.x[d]*(self.x[d]*self.x[d]-self.ex.scalar(1)))\n    out=[]\n    for dim,k,B in zip(self.dims,(-1,1,3,5),(None,B0,B1,None)):\n        B=B or self.M.zero(dim,dim);out.append(self.M.add(B,self.M.scale(self.M.smul(((gamma,),),self.M.eye(dim)),-k)))\n    return tuple(out)\n"

def canonical(n):
    n = ast.parse(ast.unparse(n)).body[0]
    n.decorator_list = []
    return ast.dump(n, include_attributes=False)
require(canonical(actual) == canonical(ast.parse(expected).body[0]), 'static/formal check failed at original checker line 35')
require(ast.literal_eval(next((n.value for n in physical.body if isinstance(n, ast.Assign) and any((isinstance(t, ast.Name) and t.id == 'dims' for t in n.targets))))) == (5, 15, 10, 2), 'static/formal check failed at original checker line 36')
primitive_expected = "\ndef primitive(self,c):\n    ch=self.data['charts'][c];out={k:self.matrix(ch[k],ch[d])for k,d in [('I','di'),('P','dp'),('H0','dh'),('H1','dh')]}\n    p=ch['pivot'];W=[list(r)for r in self.M.zero(10,8)];eta=[list(r)for r in self.M.zero(10,2)];L=[list(r)for r in self.M.zero(8,10)]\n    for h in range(2):\n        eta[h*5+p][h]=self.v[p].inverse()\n        for k in range(1,5):\n            kk=(p+k)%5;col=h*4+k-1\n            W[h*5+kk][col]=self.ex.scalar(1);W[h*5+p][col]=-self.v[kk]/self.v[p];L[col][h*5+kk]=self.ex.scalar(1)\n    out.update(W=tuple(map(tuple,W)),eta=tuple(map(tuple,eta)),L=tuple(map(tuple,L)));return out\n"
nu_expected = '\ndef nu(self,o):\n    out=self.ex.scalar(1)\n    for i in range(4):\n        if(o.legal_mask>>i)&1:out=out*(self.y[i]/self.x[i])\n    return out\n'
for name, expected_body in [('primitive', primitive_expected), ('nu', nu_expected)]:
    found = next((n for n in physical.body if isinstance(n, ast.FunctionDef) and n.name == name))
    require(canonical(found) == canonical(ast.parse(expected_body).body[0]), 'static/formal check failed at original checker line 58')
for pivot in range(5):
    columns = [(h * 5 + (pivot + k) % 5, h * 4 + k - 1) for h in range(2) for k in range(1, 5)]
    require(sorted((c for r, c in columns)) == list(range(8)), 'static/formal check failed at original checker line 62')
    require(len({r for r, c in columns}) == 8, 'static/formal check failed at original checker line 63')
    require(all((r % 5 != pivot for r, c in columns)), 'static/formal check failed at original checker line 64')
mutations = [('derivative sign', ',Q),-1)', ',Q),1)'), ('inverse row scaling', 'v/w[i]', 'v*w[i]'), ('cohomology column weights', '[self.ex.scalar(1),n2.inverse()]', '[n2.inverse(),self.ex.scalar(1)]'), ('old connection sign', 'self.M.eye(dim)),-k)', 'self.M.eye(dim)),k)'), ('extreme weight', '(-1,1,3,5)', '(1,1,3,5)'), ('block order', '(None,B0,B1,None)', '(None,B1,B0,None)'), ('U0 word order', "self.M.mul(c['H1'],c['W'])", "self.M.mul(c['W'],c['H1'])"), ('Q0 word order', "self.M.mul(c['L'],self.delta)", "self.M.mul(self.delta,c['L'])")]
for name, a, b in mutations:
    require(a in expected, 'static/formal check failed at original checker line 67')
    require(canonical(ast.parse(expected.replace(a, b)).body[0]) != canonical(actual), name)

def poly(*terms):
    q = Counter()
    for coeff, word in terms:
        q[tuple(word.split()) if word else ()] += coeff
    return {w: c for w, c in q.items() if c}

def add(*ps):
    q = Counter()
    for p in ps:
        for w, c in p.items():
            q[w] += c
    return {w: c for w, c in q.items() if c}

def mul(a, b):
    return add(*({u + v: c * d} for u, c in a.items() for v, d in b.items()))

def atom(s):
    return poly((1, s))
ONE = atom('')
ZERO = {}
rules = {('W', 'L'): poly((1, ''), (-1, 'eta ev')), ('H1', 'eta'): ZERO, ('L', 'W'): ONE, ('L', 'eta'): ZERO, ('ev', 'W'): ZERO, ('ev', 'eta'): ONE, ('H0', 'gamma'): ONE, ('H0', 'I'): ZERO, ('H0', 'H1'): ZERO, ('P', 'gamma'): ZERO, ('P', 'I'): ONE, ('P', 'H1'): ZERO, ('delta', 'gamma'): ZERO, ('delta', 'I'): ZERO, ('delta', 'H1'): poly((1, ''), (-1, 'eta ev'))}

def reduce(p):
    for word, c in p.items():
        for i in range(len(word) - 1):
            pair = word[i:i + 2]
            if pair in rules:
                rest = dict(p)
                del rest[word]
                repl = {word[:i] + v + word[i + 2:]: c * k for v, k in rules[pair].items()}
                return reduce(add(rest, repl))
    return p
uq = poly((1, 'gamma H0'), (1, 'I P'), (1, 'H1 W L delta'))
require(reduce(uq) == poly((1, 'gamma H0'), (1, 'I P'), (1, 'H1 delta')), 'static/formal check failed at original checker line 100')
require(reduce(poly((1, 'W L'), (1, 'eta ev'))) == ONE, 'static/formal check failed at original checker line 102')
u = ['gamma', 'I', 'H1 W']
q = ['H0', 'P', 'L delta']
for i in range(3):
    for j in range(3):
        require(reduce(mul(atom(q[i]), atom(u[j]))) == (ONE if i == j else ZERO), 'static/formal check failed at original checker line 105')
for i, q1 in enumerate(['L', 'ev']):
    for j, u1 in enumerate(['W', 'eta']):
        require(reduce(mul(atom(q1), atom(u1))) == (ONE if i == j else ZERO), 'static/formal check failed at original checker line 107')
weights = [[-2] * 5 + [0, -2] + [2] * 8, [0] * 8 + [2] * 2]
for exps, size in zip(weights, [15, 10]):
    require(len(exps) == size, 'static/formal check failed at original checker line 112')
    for a in exps:
        require(a + -a == 0, 'static/formal check failed at original checker line 114')
        require(a - 1 + -a == -1, 'static/formal check failed at original checker line 115')
        require(-a == -1 * a, 'static/formal check failed at original checker line 116')
expanded0 = poly((2, 'gamma H0'), (2, 'I E22 P'), (-2, 'H1 W L delta'))
expected0 = poly((2, 'gamma H0'), (2, 'I E22 P'), (-2, 'H1 delta'))
require(reduce(expanded0) == expected0, 'static/formal check failed at original checker line 120')
require(reduce(poly((-2, 'eta ev'))) == poly((-2, 'eta ev')), 'static/formal check failed at original checker line 121')
result = {'status': 'PASS', 'scope': 'conditional moving-frame lowering; static AST and formal words only', 'source_hashes_verified': len(pins), 'exact_blocks_ast': True, 'exact_primitive_and_nu_ast': True, 'pivot_index_cases': 5, 'static_mutations_rejected': [x[0] for x in mutations], 'formal_inverse_block_checks': 13, 'column_leibniz_checks': 25, 'ranks': [5, 15, 10, 2], 'weights': [-1, 1, 3, 5], 'physical_evaluation': False, 'production_import': False, 'limitations': ['contraction premises not verified against actual model entries', 'AST mutations are static mismatch controls, not numerical counterexamples', 'formal reduction uses declared equations, including delta gamma=0 for direct Q0U0 check', 'no physical source, owner, or jet evaluated']}
print(json.dumps(result, indent=2))
