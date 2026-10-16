"""PB01: pinned denotation of the INS P oracle; physical coefficients refuse.

No actual Catalog primitive polynomial is constructed or evaluated. Source
arrays are parsed only for shape/exponent metadata and denominator identities.
"""
from pathlib import Path
import copy
import hashlib
import importlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PR86 = '7d73d540981a3a152d807c39844ec63bc9913b89'
PINS_SHA = '0ac211d49398b2d64b1dac25f19e304d473890aa8d74188eca76a7de5f371fab'
INS = 'research/codex-swarm/inserted-coefficients/'
PH = 'research/codex-swarm/physical-homogenization/'
CLR = 'research/codex-swarm/whole-source-clearing/'
MODEL = 'research/hm/null-operator-compiler/hm-pinned-model.json'
MODEL_REV = '10810ee877fdaf291399198ad60d7dd0c316a42d'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def _pin_manifest():
    raw = (HERE/'source-pins.json').read_bytes()
    need(sha(raw) == PINS_SHA, 'PB01 immutable pin manifest drift')
    return json.loads(raw)


def _shared_interfaces():
    row = next(r for r in _pin_manifest()['sources'] if r['path'] == INS+'interfaces.py')
    path = BASE/'inserted-coefficients/interfaces.py'
    need(sha(path.read_bytes()) == row['sha256'], 'shared INS interface drift')
    sys.path.insert(0, str(path.parent))
    module = importlib.import_module('interfaces')
    need(Path(module.__file__).resolve() == path.resolve(), 'foreign interfaces import')
    return module


_interfaces = _shared_interfaces()
FullOwner = _interfaces.FullOwner
PhysicalAdmissionMissing = _interfaces.PhysicalAdmissionMissing


def _authenticate(repo, reader=None):
    """Reader injection is a test-only byte-authentication control, not an oracle."""
    pins = _pin_manifest()
    reader = reader or (lambda rev, path: subprocess.check_output(
        ['git', 'show', rev+':'+path], cwd=repo, timeout=15))
    values = {}
    for row in pins['sources']:
        raw = reader(row['commit'], row['path'])
        need(type(raw) is bytes and sha(raw) == row['sha256'], 'source bytes drift: '+row['path'])
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        need(blob == row['git_blob'], 'source Git blob drift')
        values[(row['commit'], row['path'])] = raw
    # Runtime dependencies must be these reviewed bytes, not merely same names.
    for name in ['source_program.py', 'polynomial_coefficients.py', 'interfaces.py']:
        need((BASE/'inserted-coefficients'/name).read_bytes() == values[(PR86, INS+name)],
             'local INS dependency drift: '+name)
    return pins, values


def _pair(pair):
    need(type(pair) in (tuple, list) and len(pair) == 2 and
         all(type(i) is int for i in pair) and tuple(pair) in ((0, 1), (2, 3)),
         'ordered pair01 or23 required')
    return tuple(pair)


def _owners(owners):
    need(type(owners) in (tuple, list) and len(owners) == 3 and
         all(type(o) is FullOwner for o in owners), 'three literal FullOwners required')
    need(len({o.seed for o in owners}) == 1, 'source seed mismatch')
    need(len({o.occurrence for o in owners}) == 3, 'source occurrence reused')
    keys = [o.source_key for o in owners]
    need(keys[0] < keys[1] < keys[2], 'strict increasing source triple required')
    return tuple(owners)


def rename_pair(nodes, pair):
    """Exactly INS pair_nodes: axes only; owner slots never permuted/sorted."""
    pair = _pair(pair)
    out = copy.deepcopy(nodes)
    if pair == (0, 1):
        return out
    sigma = (2, 3, 0, 1)
    for row in out:
        op = row[0]
        if op == 'owned_polynomial_factor' and row[1][1] == 'ell':
            row[1][2] = sigma[row[1][2]]
        elif op == 'mask_times_x_squared_plus_one_over_two':
            row[2] = sigma[row[2]]
        elif op == 'binary_mask_q_numerator':
            row[3] = sigma[row[3]]
        elif op == 'polynomial_partial_after_elementary_substitution':
            row[2] = sigma[row[2]]
    return out


def audit_shapes(nodes, root):
    """Formal ordered-operation induction, with no polynomial coefficients."""
    need(type(nodes) is list and type(root) is int and 0 <= root < len(nodes), 'DAG root')
    result = []
    for index, row in enumerate(nodes):
        need(type(row) is list and row and type(row[0]) is str, 'operation record')
        op, *a = row
        def child(j):
            need(type(j) is int and 0 <= j < index, 'topological node reference')
            return tuple(result[j]['shape'])
        def axis(i):
            need(type(i) is int and 0 <= i < 4, 'literal coordinate axis')
        def slot(i):
            need(type(i) is int and 0 <= i < 3, 'literal source slot')
        if op == 'catalog_cleared_primitive':
            need(len(a) == 2 and a[1] in ('P', 'I'), 'primitive block')
            slot(a[0]); shape = (2, 15) if a[1] == 'P' else (15, 2)
            semantic = 'H_owner^2 * actual primitive; stored numerator after elementary substitution'
        elif op == 'owned_polynomial_factor':
            need(len(a) == 1 and type(a[0]) is list and len(a[0]) == 3, 'owned factor')
            s, kind, i = a[0]; slot(s)
            need(kind in ('H', 'ell'), 'factor kind')
            if kind == 'H': need(type(i) is int and i == -1, 'H axis sentinel')
            else: axis(i)
            shape = (); semantic = 'owned H or legal ell, with full source slot preserved'
        elif op == 'mask_times_x_squared_plus_one_over_two':
            need(len(a) == 2, 'physical Q numerator arity'); slot(a[0]); axis(a[1])
            shape = (); semantic = 'm_owner,i*(x_i^2+1)/2; physical Q numerator'
        elif op == 'binary_mask_q_numerator':
            need(len(a) == 4, 'gerbe numerator arity'); slot(a[0]); slot(a[1]); axis(a[2])
            need(type(a[3]) is int and a[3] in (-1, 1), 'binary gerbe sign')
            shape = (); semantic = 'binary-mask gerbe rewrite; distinct from physical Q'
        elif op == 'polynomial_diagonal':
            need(len(a) == 1 and child(a[0]) == (), 'scalar diagonal')
            shape = (2, 2); semantic = 'diag(z,-z)'
        elif op == 'transpose':
            need(len(a) == 1 and len(child(a[0])) == 2, 'matrix transpose')
            shape = child(a[0])[::-1]; semantic = 'literal transpose'
        elif op == 'trace':
            need(len(a) == 1, 'trace arity'); s = child(a[0])
            need(len(s) == 2 and s[0] == s[1], 'square trace')
            shape = (); semantic = 'sum of diagonal entries, preserving product order'
        elif op == 'scale':
            need(len(a) == 3 and type(a[0]) is int and type(a[1]) is int and a[1] != 0, 'rational scale')
            shape = child(a[2]); semantic = 'literal exact rational scalar multiple'
        elif op == 'sum':
            need(bool(a), 'nonempty sum'); shape = child(a[0])
            need(all(child(j) == shape for j in a), 'same-shaped sum')
            semantic = 'entrywise sum'
        elif op == 'ordered_product':
            shape = ()
            for j in a:
                s = child(j)
                if not shape: shape = s
                elif s:
                    need(shape[1] == s[0], 'ordered product dimensions')
                    shape = (shape[0], s[1])
            semantic = 'left-to-right ordered matrix multiplication with scalar multiplication'
        elif op == 'power':
            need(len(a) == 2 and type(a[1]) is int and a[1] >= 0 and child(a[0]) == (), 'nonnegative scalar power')
            shape = (); semantic = 'nonnegative polynomial power'
        elif op == 'polynomial_partial_after_elementary_substitution':
            need(len(a) == 2, 'polynomial partial arity'); axis(a[1]); shape = child(a[0])
            semantic = 'differentiate entire polynomial AFTER v_k=e_k(x); entrywise'
        else:
            raise ValueError('unsupported source opcode: '+op)
        result.append({'node': index, 'shape': list(shape), 'denotation_rule': semantic})
    need(result[root]['shape'] == [], 'P root must be scalar')
    return result


def _primitive_bridges(model):
    """Inspect literal shapes/exponent bounds; never operate on physical values."""
    need(type(model['charts']) is list and len(model['charts']) == 6, 'six actual carriers')
    result = []
    for c, chart in enumerate(model['charts']):
        if c == 0: expected = {(1,1,1,1): 1, (0,0,0,0): -1}
        elif c < 5: expected = {(1,1,1,1): 1, tuple(5 if i == c-1 else 0 for i in range(4)): -1}
        else: expected = {(2,0,1,1): -1}
        entries = []
        for block, den, size in [('I','di',(15,2)), ('P','dp',(2,15))]:
            got = {tuple(map(int, e.split(','))): value for e, value in chart[den]}
            need(len(chart[den]) == len(expected) and got == expected, 'actual denominator identity')
            need(len(chart[block]) == size[0] and all(len(row) == size[1] for row in chart[block]), 'actual primitive shape')
            for r, row in enumerate(chart[block]):
                for s, poly in enumerate(row):
                    w = s if block == 'I' else -r
                    bound = (6 if c == 5 else 5)+w
                    for key, _coefficient in poly:
                        exps = tuple(map(int, key.split(',')))
                        need(len(exps) == 4 and min(exps) >= 0 and sum(exps) <= bound, 'weighted source numerator degree')
                    entries.append({'block':block,'row':r,'column':s,'weight':w,
                                    'stored_numerator_homogenization_degree':bound})
        result.append({'carrier':c,'assigned_H_degree':4 if c == 5 else 5,
            'finite_H':'v1*v3*v4' if c == 5 else 'h'+str(c),
            'finite_di_dp':'-v1^2*v3*v4' if c == 5 else '-H',
            'finite_H_squared_primitive':'-v3*v4*stored_num(e1,e2,e3,e4)' if c == 5 else '-H*stored_num(e1,e2,e3,e4)',
            'homogeneous_H':'v0*v1*v3*v4' if c == 5 else 'v'+str(c)+'^5-v0*v1*v2*v3*v4',
            'homogeneous_H_squared_primitive':'-v3*v4*hom_(6+w)(stored_num)' if c == 5 else '-H*hom_(5+w)(stored_num)',
            'auxiliary_v0_control':'hom_4(di)=-v1*a/v0; the polynomial expression is -v1^2*v3*v4' if c == 5 else None,
            'entry_degrees':entries,'catalog_block_sha256':sha(canonical(chart).encode())})
    return result


class ActualPBinding:
    """Repo-only constructor. No catalog, callable, proof string or mode input.

    Metadata methods return fresh serializable copies. Mutating their outputs
    never changes this object's source binding or grants physical execution.
    """
    def __init__(self, repo=None):
        repo = Path(repo) if repo is not None else HERE.parents[2]
        self._pins, raw = _authenticate(repo)
        self._finite = json.loads(raw[(PR86, CLR+'source-integration.json')])['finite_actual_source_clearing']
        need(self._finite['schema'] == 'whole-F-finite-factored-clearing-v1' and
             self._finite['pair'] == [0,1] and len(self._finite['dag']) == 153 and
             self._finite['cleared_P'] == 152 and self._finite['finite_carrier_orders'] == [5,6,5],
             'reviewed whole source identity')
        self._bridges = _primitive_bridges(json.loads(raw[(MODEL_REV, MODEL)]))
        self._node_proof = audit_shapes(self._finite['dag'], 152)

    @property
    def mode(self):
        return 'physical'

    def source_pins(self):
        return copy.deepcopy(self._pins)

    def symbolic_program_definition(self, pair=(0,1)):
        pair = _pair(pair)
        return {'schema':'source-faithful-P-symbolic-program-v1','pair':list(pair),
                'dag':rename_pair(self._finite['dag'], pair),'cleared_P':152,
                'root_denotation':'(product_slots C_owner)*actual_F_pair, evaluated once in increasing target source order',
                'coefficient_execution':False}

    def degree_upper(self, ordered_owners, pair=(0,1)):
        owners = _owners(ordered_owners); pair = _pair(pair)
        d = sum(4 if o.carrier == 5 else 5 for o in owners)
        return tuple(14*d + (sum(1+2*((o.legal_mask >> i)&1) for o in owners)-2 if i in pair else 0) for i in range(4))

    def describe(self, ordered_owners, pair=(0,1)):
        owners = _owners(ordered_owners); pair = _pair(pair)
        program = self.symbolic_program_definition(pair)
        degree = list(self.degree_upper(owners, pair))
        C = [{'owner':list(o.data()),'H_power':14,'H_degree':4 if o.carrier == 5 else 5,
              'pair_ell_axes':list(pair),'pair_ell_degrees':[1+2*((o.legal_mask >> i)&1) for i in pair]} for o in owners]
        return {'schema':'source-faithful-P-binding-v1','pair':list(pair),
            'ordered_owners':[list(o.data()) for o in owners],
            'source_identity':'P=(product_slots H_owner^14 product_pair ell_owner)*actual_F_pair',
            'actual_F':'b_pair-tr[K20(T12,p*T01,q-T12,q*T01,p)]/4',
            'physical_Q':'m*(x_i^2+1)/(2*x_i*(x_i^2-1))*diag(1,-1)',
            'gerbe_b':'(15/4)*((m1,p-m0,p)/x_p)*((m2,q-m1,q)/x_q)',
            'physical_Q_is_gerbe_q':False,
            'program':program,'ordered_operation_induction':audit_shapes(program['dag'],152),
            'primitive_bridges':copy.deepcopy(self._bridges),'owned_clearings':C,
            'P_homogeneous_multidegree':degree,
            'representation_chart_transition':{'chart_domain':list(range(16)),
                'standard_bits':'high bit3-i','owner_tags_reassigned':False,
                'formula':'P_local(t,x)=product_inverted t_i^D_i * P_finite(1/t,x)',
                'proof':'PH01 derives actual F_local=t_pair^-2 F_finite(pullback) before clearing; C has its actual homogeneous divisor degrees, so D=sum degree(C)+n_pair.',
                'auxiliary_H_contains_v0':True},
            'source_order':{'rule':'strict increasing source_key, auxiliary5 first, then numeric mask then original standard tag',
                'matrix_product_reordered':False,'repeated_physical_source_labels_zero':len({o.physical_key for o in owners}) < 3,
                'alternating_extension':'Sort the target triple ONCE, evaluate this raw formula on it, then apply permutation sign externally.',
                'F34_caveat':'Raw axes (0 2)(1 3) with target slots fixed. No sorting of raw inverse image and no equality of differently sorted nonlinear source cochains.'},
            'proof_dependencies':self.source_pins(),
            'physical_source_evaluated':False,'physical_execution_admitted':False,
            'semantic_scope':'Denotation of this exact pinned INS source constructor and Catalog, under the accepted CLR/PH contraction and physical-source premises; not an actual coefficient value.'}

    def coefficient(self, *args, **kwargs):
        raise PhysicalAdmissionMissing('PB01 binds physical P semantics; coefficient execution remains unadmitted')

    def alternating_coefficient(self, *args, **kwargs):
        raise PhysicalAdmissionMissing('PB01 physical alternating coefficient execution remains unadmitted')
