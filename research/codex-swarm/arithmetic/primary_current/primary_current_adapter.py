"""A05 review candidate: primary current DAGs; no admitted weighted kernel.
Run Python with -B: the authenticated public directory must remain untouched.
No seed selector, prefix kernel, polynomial evaluator or certificate scan here.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from package_snapshot import package_path
from itertools import combinations
import hashlib
import importlib
import importlib.util
import json
import sys

RELEASE = '6e28c6b59f8245779f6c03a20798e4de6842ae19'
SOURCE = '08b73637d4136f91606aad332c46cafd064417f8'
PUBLIC = package_path()
MANIFEST_SHA256 = 'ec0746ba0d537ec3edeb96f396a02e426225e904227e4c500dad0f5e0d3fbb64'
MODULES = ('owned_scalar_denominator_binding', 'physical_current_source_binding',
           'outer_partition_source_binding', 'lower_selected_kernel_denominators')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def authenticate_directory(directory=PUBLIC):
    directory = Path(directory).resolve()
    require(directory == PUBLIC.resolve(), 'unsupported public directory')
    raw = (directory / 'release-manifest.json').read_bytes()
    require(hashlib.sha256(raw).hexdigest() == MANIFEST_SHA256, 'manifest hash')
    manifest = json.loads(raw)
    require(manifest['public_source_commit'] == SOURCE, 'source pin')
    # Read-only authentication, including witnesses; no certificate generation.
    for name, digest in manifest['files_sha256'].items():
        require(Path(name).name == name, 'manifest filename')
        require(hashlib.sha256((directory / name).read_bytes()).hexdigest() == digest,
                'public hash mismatch: ' + name)
    return manifest

def load_public():
    manifest = authenticate_directory()
    require(sys.dont_write_bytecode, 'use python -B to keep public directory read-only')
    for name in MODULES:
        if name in sys.modules:
            require(Path(sys.modules[name].__file__).resolve() == PUBLIC / (name + '.py'),
                    'foreign preloaded public module: ' + name)
    old_path = list(sys.path)
    try:
        sys.path.insert(0, str(PUBLIC))
        result = []
        for name in MODULES:
            spec = importlib.util.find_spec(name)
            require(spec is not None and Path(spec.origin).resolve() == PUBLIC / (name + '.py'),
                    'foreign public import: ' + name)
            result.append(importlib.import_module(name))
        return result
    finally:
        sys.path[:] = old_path

owned, source, outer, selected = load_public()


def parse_owners(records):
    require(isinstance(records, (list, tuple)) and len(records) == 3, 'three owners')
    fields = {'seed', 'owner', 'carrier', 'legal_mask', 'standard_tag'}
    vertices = []
    for record in records:
        require(isinstance(record, dict) and set(record) == fields, 'exact owner fields')
        require(all(type(record[k]) is int for k in fields), 'integer owner fields only')
        require(record['carrier'] in range(1, 5), 'exceptional tail rejected; primary1..4 only')
        vertices.append(owned.VertexLabel(**record))
    vs = tuple(vertices)
    require(len({v.seed for v in vs}) == 1, 'one source occurrence family')
    require(len({v.owner for v in vs}) == 3, 'distinct owner occurrences')
    keys = [(v.carrier, v.legal_mask, v.standard_tag) for v in vs]
    require(keys == sorted(keys) and len(set(keys)) == 3, 'distinct source-sorted owners required')
    return vs


def factor_identity_metadata():
    """Monomial exponent metadata in formal v0..v4; no polynomial execution.

    A product is represented by its five factor multiplicities only. These
    checks witness the two identities used for primary pole conversion.
    """
    all_v = [1] * 5
    a = [1, 1, 0, 1, 1]
    v2_a = [n + int(i == 2) for i, n in enumerate(a)]
    require(v2_a == all_v, 'v2*a product factors')
    records = []
    for j in range(1, 5):
        vj = [int(i == j) for i in range(5)]
        fourth = [4 * x for x in vj]
        other = [int(i != j) for i in range(5)]
        require([x + y for x, y in zip(vj, fourth)] == [5*x for x in vj],
                'vj*fourth factors')
        require([x + y for x, y in zip(vj, other)] == all_v, 'vj*other factors')
        records.append({'carrier': j, 'F_positive_factors': fourth,
                        'F_negative_factors': other, 'H_positive_factors': [5*x for x in vj],
                        'H_negative_factors': all_v[:]})
    return {'representation': 'five formal generator multiplicities only',
            'identities': ['H_j=v_j*F_j', 'v_j^5=H_j+v_2*a'],
            'a_factors': a, 'v2_a_factors': v2_a, 'primary': records,
            'physical_polynomial_expansion': False, 'physical_polynomial_evaluation': False}


class PrimaryLower(selected.Lower):
    """Legitimate replacement initializer; inherited invariant methods audited in proof.

    Global finite normalized currents only. Their physical meaning is D_a R D_a^-1.
    Standard tags restrict owners; they do not change the derivative frame.
    """
    def __init__(self, records):
        authenticate_directory()
        self.vs = parse_owners(records)
        self.model = source.authenticate()
        self.inverse_certificate = selected.contraction_certificate()
        self.factor_certificate = factor_identity_metadata()
        outer.authenticate_public_sources()
        require((outer.CARRIER_POWER, outer.LEGAL_POWER, outer.STANDARD_BOUND) == (54, 29, 5251),
                'outer clearance constants')
        self.g = selected.DAG()
        self.factors, self.blocks = {}, {}
        g = self.g
        self.x = [g.node('coordinate', i) for i in range(4)]
        self.v = [g.c(1)] + [g.add(*(g.mul(*(self.x[i] for i in inds))
                  for inds in combinations(range(4), k))) for k in range(1, 5)]
        # Match sparse stored metadata, not polynomial evaluation or expansion.
        for v in self.vs:
            for name in ('di', 'dp', 'dh'):
                pairs = self.model['charts'][v.carrier][name]
                got = {tuple(map(int, e.split(','))): c for e, c in pairs}
                exponent = tuple(5 if i == v.carrier - 1 else 0 for i in range(4))
                require(len(pairs) == 2 and got == {(1, 1, 1, 1): 1, exponent: -1},
                        'pinned denominator must be -H')
            self.factors[self.key(v, 'H')] = g.add(g.pow(self.v[v.carrier], 5),
                                                         g.mul(g.c(-1), *self.v))
            for i in range(4):
                self.factors[self.key(v, 'L', i)] = g.mul(self.x[i],
                                                  g.add(g.pow(self.x[i], 2), g.c(-1)))
                self.factors[self.key(v, 'Z', i)] = self.x[i]

    def _owner(self, v):
        require(v in self.vs, 'unbound owner')

    def _axis(self, d):
        require(type(d) is int and d in range(4), 'coordinate index0..3')

    def rat(self, n, den=None):
        require(type(n) is int and 0 <= n < len(self.g.nodes), 'DAG numerator')
        require(den is None or isinstance(den, dict), 'denominator map')
        for k, e in (den or {}).items():
            require(k in self.factors, 'unmatched denominator owner')
            require(type(e) is int and e >= 0, 'nonnegative integer denominator count')
        return super().rat(n, den)

    def block(self, v, name):
        self._owner(v)
        require(name in ('I', 'P'), 'current block I/P only')
        return super().block(v, name)

    def log(self, v, d):
        self._owner(v)
        self._axis(d)
        return super().log(v, d)

    def diff(self, r, d):
        self._axis(d)
        self.rat(*r)
        return super().diff(r, d)

    def current(self, kind, d):
        require(kind in ('L', 'U'), 'current kind L/U')
        self._axis(d)
        return super().current(kind, d)

    def edge_inverse(self, edge):
        require(type(edge) is tuple and edge in ((0, 1), (1, 2)), 'tail edge01/12')
        return super().edge_inverse(edge)

    def quotient(self, v):
        self._owner(v)
        return super().quotient(v)

    def ledger(self, r):
        self.rat(*r)
        result = []
        for v in self.vs:
            H = r[1].get(self.key(v, 'H'), 0)
            L = [r[1].get(self.key(v, 'L', i), 0) for i in range(4)]
            Z = [r[1].get(self.key(v, 'Z', i), 0) for i in range(4)]
            require(H <= 54 and max(L) <= 29 and max(Z) <= 5251, 'outer clearance exceeded')
            require(all(not e or bit for e, bit in zip(L, owned.decode_legal_mask(v.legal_mask))),
                    'unowned legal divisor')
            require(all(not e or bit for e, bit in zip(Z, owned.decode_standard_tag(v.standard_tag))),
                    'unowned standard divisor')
            result.append({'owner': list(v.data()), 'carrier': H, 'legal': L, 'standard': Z,
                           'clearance': {'carrier': 54, 'legal': 29, 'standard': 5251}})
        return result

    def cancel(self, r):
        """Conditional algebraic outer quotient only; no weighted derivative permission."""
        self.ledger(r)
        return super().cancel(r)

    def admitted_weighted_derivative(self, *args, **kwargs):
        raise ValueError('unbound inner N14 combined quotient/physical selector; derivative admission false')

    def normal_order(self, pair):
        require(type(pair) is tuple and len(pair) == 2 and all(type(d) is int for d in pair)
                and pair in ((0, 1), (2, 3)), 'explicit pair01/23')
        i, j = pair
        # E_pair(f)=sum sign/2 * R * partial_d(f_edge / D_edge).
        # A+B*partial applies to unweighted f. Inner T and its rho MUST remain combined.
        terms = []
        for edge, d, kind, c, sign in (
            ((1, 2), i, 'L', j, 1), ((1, 2), j, 'L', i, -1),
            ((0, 1), j, 'U', i, 1), ((0, 1), i, 'U', j, -1)):
            R = self.tracefree(self.current(kind, c))
            inv = self.edge_inverse(edge)
            dinv = self.diff(inv, d)
            scale = self.rat(self.g.c(sign, 2))
            def matrix_coeff(weight):
                out = [[self.mul(scale, self.mul(r, weight)) for r in row] for row in R]
                return [[{'numerator': r[0], 'denominators': r[1],
                          'owner_ledger': self.ledger(r)} for r in row] for row in out]
            terms.append({'edge_owner_indices': list(edge), 'derivative_index': d,
                          'current_kind': kind, 'current_index': c, 'sign': sign,
                          'character_conversion': owned.character_conversion(
                              pair, (2, 3) if pair == (0, 1) else (0, 1), d),
                          'A': matrix_coeff(dinv), 'B': matrix_coeff(inv)})
        return terms


def build(request):
    require(isinstance(request, dict) and set(request) == {'schema', 'owners', 'pair'},
            'exact request fields; no selectors/flags/carrier maps')
    require(request['schema'] == 'a05-primary-current-request-v1', 'schema')
    pair = request['pair']
    require(type(pair) is list and len(pair) == 2 and all(type(x) is int for x in pair),
            'explicit integer pair indices')
    lo = PrimaryLower(request['owners'])
    terms = lo.normal_order(tuple(pair))
    return {'schema': 'a05-primary-current-review-v1', 'source_pin': SOURCE, 'release_pin': RELEASE,
            'owners': [list(v.data()) for v in lo.vs], 'pair': pair,
            'input_pair': [2, 3] if pair == [0, 1] else [0, 1],
            'composition': 'E12(T34 F34)' if pair == [0, 1] else 'E34(T12 F12)',
            'domain': 'characteristic zero; distinct source-sorted primary tails; global finite frame restricted to owned standard intersections',
            'frame': 'normalized at first tail owner; physical current=D_a R D_a^-1; matching selector conjugation remains external',
            'dag': lo.g.nodes, 'four_terms': terms,
            'normal_order_semantics': 'A*f_edge+B*partial_d(f_edge), unweighted input only; pending rational coefficients, not coefficient atoms',
            'evidence': {'manifest_sha256': MANIFEST_SHA256, 'model_sha256': source.MODEL_SHA256,
                         'inverse_certificate': lo.inverse_certificate,
                         'factor_identities': lo.factor_certificate},
            'reviewer': ['V03', 'A01'], 'artifact_review': 'pending',
            'gap': 'combined inserted N14 quotient and weighted derivative binding; physical selector; outer pullback review; schedule',
            'next_step': 'V03/A01 review current/frame recurrence and bind combined regularized inner product before differentiation',
            'actual_source_admitted': False, 'source_pole_domain_proved': False,
            'weighted_derivative_admitted': False, 'Laurent_admitted': False,
            'actual_factorization_accepted': False, 'execution_release': False,
            'physical_polynomial_expansion': False, 'physical_polynomial_evaluation': False}


def validate_result(request, result):
    require(json.dumps(result, sort_keys=True, separators=(',', ':')) ==
            json.dumps(build(request), sort_keys=True, separators=(',', ':')),
            'artifact fields, owners, DAG, or gate mutation')
    return True

if __name__ == '__main__':
    require(len(sys.argv) == 2, 'usage: python -B primary_current_adapter.py request.json')
    path = Path(sys.argv[1])
    require(path.stat().st_size <= 8192, 'bounded request')
    print(json.dumps(build(json.loads(path.read_text())), sort_keys=True, separators=(',', ':')))
