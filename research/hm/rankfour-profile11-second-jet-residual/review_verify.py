#!/usr/bin/env python3
"""Independent fixed-character audit, with no import of author code.

Only the two forced doublets, five forced unordered scalar partitions of 22,
cohomology identities, and their two rank-two target Hom spaces are checked.
No actual coefficient, parameter, point, jet, tensor, matrix, or instance rank
is constructed or evaluated. The small tables are universal Hom dimensions.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
FROZEN_PROOF_SHA256 = '793c635439cf05c0234b4152aca4e9213780258d096d9036902b808a952f39e4'
CHECK_COUNT = 0

def require(condition, message):
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise RuntimeError(str(message))

@dataclass(frozen=True)
class Q5:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))
    @staticmethod
    def lift(x): return x if isinstance(x, Q5) else Q5(x)
    def __add__(self, other):
        o = self.lift(other)
        return Q5(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __neg__(self): return Q5(-self.a, -self.b)
    def __sub__(self, other): return self + (-self.lift(other))
    def __rsub__(self, other): return self.lift(other) - self
    def __mul__(self, other):
        o = self.lift(other)
        return Q5(self.a*o.a + 5*self.b*o.b, self.a*o.b + self.b*o.a)
    __rmul__ = __mul__
    def __truediv__(self, n): return Q5(self.a/F(n), self.b/F(n))
    def conjugate(self): return Q5(self.a, -self.b)
    def integer(self):
        require(self.b == 0 and self.a.denominator == 1, (self.a, self.b))
        return int(self.a)

# The nine binary-icosahedral conjugacy classes, independently encoded by
# their closed physical SU(2) trace and class sizes. No McKay recurrence,
# historical candidate list, author character code, or actual matrices used.
phi = Q5(F(1, 2), F(1, 2))
trace = tuple(map(Q5.lift, [2, -2, 0, 1, -1, phi, -phi, phi-1, 1-phi]))
sizes = (1, 1, 30, 20, 20, 12, 12, 12, 12)
require(sum(sizes) == 120, 'Check failed: sum(sizes) == 120')
one = tuple(Q5(1) for _ in sizes)
zero = tuple(Q5(0) for _ in sizes)
def add(*cs): return tuple(sum(v, Q5()) for v in zip(*cs))
def scale(n, c): return tuple(n*v for v in c)
def sub(a, b): return add(a, scale(-1, b))
def product(*cs):
    out = one
    for c in cs: out = tuple(a*b for a, b in zip(out, c))
    return out
def sym(n):
    require(0 <= n <= 18, 'Audit deliberately restricted to needed degrees.')
    if n == 0: return one
    prev, curr = one, trace
    for _ in range(2, n+1): prev, curr = curr, sub(product(trace, curr), prev)
    return curr
Wprime = tuple(x.conjugate() for x in trace)
V = sub(product(Wprime, Wprime), one)
reps = {
    '1': one, 'W': trace, 'Wprime': Wprime,
    'A_std': sym(2), 'V': V, 'S4': sym(3),
    'P': sub(sym(6), V), 'D': sym(4), 'T6': sym(5),
}
expected_dims = {'1':1, 'W':2, 'Wprime':2, 'A_std':3, 'V':3, 'S4':4, 'P':4, 'D':5, 'T6':6}
def inner(a, b): return (sum((s*x*y for s, x, y in zip(sizes, a, b)), Q5())/120).integer()
for na, ca in reps.items():
    require(ca[0].integer() == expected_dims[na], 'Check failed: ca[0].integer() == expected_dims[na]')
    for nb, cb in reps.items(): require(inner(ca, cb) == int(na == nb), 'Check failed: inner(ca, cb) == int(na == nb)')
require(sum(d*d for d in expected_dims.values()) == 120, 'Check failed: sum(d*d for d in expected_dims.values()) == 120')

def decompose(c):
    ans = {name:inner(c, r) for name, r in reps.items()}
    require(add(*(scale(n, reps[name]) for name, n in ans.items())) == c, 'Check failed: add(*(scale(n, reps[name]) for name, n in ans.items())) == c')
    return {name:n for name,n in ans.items() if n}
def linear(**kwargs): return add(*(scale(n, reps[name]) for name,n in kwargs.items()))
def h1(blocks): return add(*(product(reps[r], sym(j-2)) for r,j in blocks))
def hom(r,j,t,k):
    return 0 if j < k else inner(one, product(reps[r], reps[t], sym(j-k)))

require(sym(5) == reps['T6'], "Check failed: sym(5) == reps['T6']")
require(sym(6) == linear(V=1,P=1), 'Check failed: sym(6) == linear(V=1,P=1)')
require(sym(7) == linear(Wprime=1,T6=1), 'Check failed: sym(7) == linear(Wprime=1,T6=1)')
require(product(reps['W'],sym(6)) == linear(Wprime=1,T6=2), "Check failed: product(reps['W'],sym(6)) == linear(Wprime=1,T6=2)")
require(product(reps['A_std'],reps['A_std']) == linear(**{'1':1,'A_std':1,'D':1}), "Check failed: product(reps['A_std'],reps['A_std']) == linear(**{'1':1,'A_std':1,'D':1})")
hS = linear(A_std=1,V=2,P=3,D=4)
hM = product(reps['A_std'], sym(6))
require(hM == linear(V=1,P=2,D=2), 'Check failed: hM == linear(V=1,P=2,D=2)')
hR = sub(hS, hM)
require(hR == linear(A_std=1,V=1,P=1,D=2), 'Check failed: hR == linear(A_std=1,V=1,P=1,D=2)')
require(hS[0].integer() == 41 and hM[0].integer() == 21 and hR[0].integer() == 20, 'Check failed: hS[0].integer() == 41 and hM[0].integer() == 21 and hR[0].integer() == 20')

# EXACTLY the partitions forced by rank two, negativity, degree -22,
# and center-even physical linearization. The j=2 row is kept although
# the stronger top-degree bound independently excludes it.
forms = {
    'W(-11)': [('W',11)],
    "Wprime(-11)": [('Wprime',11)],
    'O(-2)+O(-20)': [('1',2),('1',20)],
    'O(-4)+O(-18)': [('1',4),('1',18)],
    'O(-6)+O(-16)': [('1',6),('1',16)],
    'O(-8)+O(-14)': [('1',8),('1',14)],
    'O(-10)+O(-12)': [('1',10),('1',12)],
}
require([j for j in range(2,12,2)] == [2,4,6,8,10], 'Check failed: [j for j in range(2,12,2)] == [2,4,6,8,10]')
characters = {}
for label, blocks in forms.items():
    require(sum(expected_dims[r] for r,j in blocks) == 2, 'Check failed: sum(expected_dims[r] for r,j in blocks) == 2')
    require(sum(-j*expected_dims[r] for r,j in blocks) == -22, 'Check failed: sum(-j*expected_dims[r] for r,j in blocks) == -22')
    require(all(reps[r][1] == Q5((-1)**j * expected_dims[r]) for r,j in blocks), 'Check failed: all(reps[r][1] == Q5((-1)**j * expected_dims[r]) for r,j in blocks)')
    c = h1(blocks)
    characters[label] = {'H1':decompose(c), 'matches_residual':c==hR}
survivors = [label for label in forms if characters[label]['matches_residual']]
require(survivors == ['W(-11)', 'Wprime(-11)', 'O(-4)+O(-18)', 'O(-6)+O(-16)', 'O(-10)+O(-12)'], "Check failed: survivors == ['W(-11)', 'Wprime(-11)', 'O(-4)+O(-18)', 'O(-6)+O(-16)', 'O(-10)+O(-12)']")
for label in ['O(-2)+O(-20)', 'O(-8)+O(-14)']:
    require(characters[label]['H1']['1'] == 1, "Check failed: characters[label]['H1']['1'] == 1")

# Universal Hom dimensions: target blocks label rows, source blocks columns.
# A wholly zero target row, or wholly zero scalar source column, precludes
# full generic rank. A remaining form is NOT asserted to be realized or to
# admit a full-rank actual derivative map.
targets = {'scalar_Q':[('1',4),('1',6)], 'balanced_Q':[('W',5)]}
tables = {}
for q, target in targets.items():
    tables[q] = {}
    for label in survivors:
        tables[q][label] = [[hom(r,j,t,k) for r,j in forms[label]] for t,k in target]
expected = {
    'scalar_Q': {
        'W(-11)': [[0],[0]],
        'Wprime(-11)': [[1],[0]],
        'O(-4)+O(-18)': [[1,0],[0,1]],
        'O(-6)+O(-16)': [[0,1],[1,0]],
        'O(-10)+O(-12)': [[0,0],[0,0]],
    },
    'balanced_Q': {
        'W(-11)': [[0]],
        'Wprime(-11)': [[1]],
        'O(-4)+O(-18)': [[0,1]],
        'O(-6)+O(-16)': [[1,1]],
        'O(-10)+O(-12)': [[0,0]],
    },
}
require(tables == expected, tables)

# Only extension groups for the three surviving residual forms are checked.
# Ext^1_G(R(-j),A_std(-8)) = H^1(R*A_std*(j-8))^G.
def extension_dimension(r,j):
    return 0 if j >= 7 else inner(one, product(reps[r],reps['A_std'],sym(6-j)))
extensions = {
    'Wprime(-11)': extension_dimension('Wprime',11),
    'O(-4)': extension_dimension('1',4),
    'O(-6)': extension_dimension('1',6),
    'O(-16)': extension_dimension('1',16),
    'O(-18)': extension_dimension('1',18),
}
require(extensions == {'Wprime(-11)':0,'O(-4)':1,'O(-6)':0,'O(-16)':0,'O(-18)':0}, "Check failed: extensions == {'Wprime(-11)':0,'O(-4)':1,'O(-6)':0,'O(-16)':0,'O(-18)':0}")
require(3*(-8) == 4*(-7)-(-4), 'Check failed: 3*(-8) == 4*(-7)-(-4)')  # Canonical cubic evaluation kernel degree.
require(hom('1',4,'S4',7) == 0, "Check failed: hom('1',4,'S4',7) == 0")  # The cubic evaluation extension cannot split.

# Simple structural arithmetic only, not computational validation of geometry.
require(3*(2-10) == -24, 'Check failed: 3*(2-10) == -24')
require(-46 - (-24) == -22, 'Check failed: -46 - (-24) == -22')
require(-28 - (-6) == -22, 'Check failed: -28 - (-6) == -22')
require(-16 - (-6) == -10, 'Check failed: -16 - (-6) == -10')
require(-10 - (-22) == 12, 'Check failed: -10 - (-22) == 12')

report = {
    'status':'PASS',
    'method':'Independent exact closed conjugacy-class characters in Q(sqrt(5)); no author imports.',
    'scope':'Only forced two doublets, five scalar partitions, cohomology identities and tiny universal Hom spaces.',
    'irreducible_dimensions':expected_dims,
    'H1_S0':decompose(hS), 'H1_M':decompose(hM), 'H1_R':decompose(hR),
    'forced_forms':characters,
    'character_survivors':survivors,
    'universal_Hom_dimensions':tables,
    'necessary_scalar_Q_forms':['O(-4)+O(-18)','O(-6)+O(-16)'],
    'necessary_balanced_Q_forms':['Wprime(-11)','O(-6)+O(-16)'],
    'fixed_extension_dimensions':extensions,
    'necessary_S0_forms':['A_std(-8)+Wprime(-11)','A_std(-8)+O(-6)+O(-16)','A_std(-8)+O(-4)+O(-18)','S4(-7)+O(-18)'],
    'warning':'These are necessary possibilities only. Geometry and source authenticity require separate review.',
}
proof = ROOT/'PROOF.md'
report['proof_sha256'] = hashlib.sha256(proof.read_bytes()).hexdigest()
require(report['proof_sha256'] == FROZEN_PROOF_SHA256, 'Proof changed: repeat full independent review.')
report['checker_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
manifest = ROOT/'INPUTS.json'
require(manifest.is_file(), 'INPUTS.json is required for a complete audit.')
entries = json.loads(manifest.read_text())
expected_inputs = {
    'inputs/endpoint-jet.md': ('bbe7c05e9055b70ba511c77ebc0514a0fdf89d75844199f971e7e774355c08c6',13548),
    'inputs/pair-defect.md': ('95cc7824898dd0bffe13f86ab1ede2947451eb3d4632e189baa608ad0de3fdec',15519),
    'inputs/principal-parts.md': ('09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26',12085),
}
require(len(entries) == 3, 'The complete three-source manifest is required.')
require({item['file'] for item in entries} == set(expected_inputs), 'Unexpected or missing source files.')
report['inputs_manifest_sha256'] = hashlib.sha256(manifest.read_bytes()).hexdigest()
checked = []
for item in entries:
    require((item['sha256'],item['bytes']) == expected_inputs[item['file']], 'Source differs from independently reviewed immutable input.')
    data = (ROOT/item['file']).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    require(digest == item['sha256'], "Check failed: digest == item['sha256']")
    require(len(data) == item['bytes'], "Check failed: len(data) == item['bytes']")
    git_sha = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if 'git_blob_sha1' in item: require(git_sha == item['git_blob_sha1'], "Check failed: git_sha == item['git_blob_sha1']")
    checked.append({'file':item['file'],'sha256':digest,'bytes':len(data),'git_blob_sha1':git_sha})
report['input_local_integrity'] = checked
report['checks_passed'] = CHECK_COUNT
print(json.dumps(report, indent=2))
