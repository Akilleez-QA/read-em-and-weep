"""Bounded symbolic request producer. No evaluator, scan, or arithmetic admission."""
import hashlib
import importlib
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from package_snapshot import package_path
import sys

PUBLIC = package_path()
RELEASE = '6e28c6b59f8245779f6c03a20798e4de6842ae19'
SOURCE = '08b73637d4136f91606aad332c46cafd064417f8'
MANIFEST = 'ec0746ba0d537ec3edeb96f396a02e426225e904227e4c500dad0f5e0d3fbb64'
ENDPOINT = Path(__file__).resolve().parents[2] / 'certificates' / 'endpoint-support.json'
ENDPOINT_HASH = '18faf702e382b1484ca6b3f8e08ff2f8500f615cc9d3c27227dee968306aa24e'
MODULES = ('owned_scalar_denominator_binding', 'physical_current_source_binding',
           'compile_refined_detector_metadata', 'prune_refined_selector_paths',
           'resolution_selector_source_binding', 'outer_partition_source_binding')
EXPECTED = {'schema': 'a02-seed30-e34-request-v1', 'release_pin': RELEASE,
            'source_pin': SOURCE, 'seed': 30, 'channel': 'E34(T12F12)',
            'owners': [[30, i, i, m, t] for i, (m, t) in
                       enumerate(zip((0, 1, 3, 7, 15), (0, 8, 12, 14, 15)))]}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False)


def checked(path, digest):
    raw = path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == digest, 'hash mismatch: ' + str(path))
    return raw


def authenticate():
    manifest = json.loads(checked(PUBLIC / 'release-manifest.json', MANIFEST))
    # Authenticate every imported module and all public data they can consume.
    # Byte reads only: no certificate decompression or scans.
    for name, digest in manifest['files_sha256'].items():
        require(Path(name).name == name, 'unexpected manifest path')
        checked(PUBLIC / name, digest)
    for name in MODULES:
        require(name not in sys.modules, 'refuse preloaded public module: ' + name)
        require(name + '.py' in manifest['files_sha256'], 'unbound module')
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(PUBLIC))
    modules = {name: importlib.import_module(name) for name in MODULES}
    for name, module in modules.items():
        require(Path(module.__file__).resolve() == PUBLIC / (name + '.py'), 'module origin')
    return modules


def block_inventory(ast, path=(), context=()):
    """Exact AST occurrence ledger; deliberately not a derived pole envelope."""
    out = []
    if not isinstance(ast, dict) or 'op' not in ast:
        return out
    op = ast['op']
    if op in ('pinned_rational_block', 'pinned_resolution_rational_block'):
        _, owner, name, denominator = ast['args']
        out.append({'path': list(path), 'owner': owner, 'block': name,
                    'denominator_reference': denominator, 'multiplicity': 1,
                    'context': list(context)})
    new_context = context + ((op,) if op in ('partial', 'adjugate_over_determinant') else ())
    for i, child in enumerate(ast['args']):
        out.extend(block_inventory(child, path + (i,), new_context))
    return out


def build(request):
    # Canonical JSON comparison distinguishes Boolean labels from integers and
    # rejects extra keys at every nesting level. Only this exact request is supported.
    require(canonical(request) == canonical(EXPECTED), 'unsupported request or fields')
    mods = authenticate()
    owned = mods['owned_scalar_denominator_binding']
    current = mods['physical_current_source_binding']
    selector = mods['resolution_selector_source_binding']
    outer = mods['outer_partition_source_binding']
    spec = mods['compile_refined_detector_metadata']
    model = selector.authenticate()
    outer.authenticate_public_sources()
    owners = tuple(owned.VertexLabel(*v) for v in request['owners'])
    record = spec.seed_records()[30]
    require(record['row'] == 7 and record['orientation'] == 1 and
            list(record['standard']) == [0, 8, 12, 14, 15], 'seed mismatch')
    endpoint = json.loads(checked(ENDPOINT, ENDPOINT_HASH))
    row = next(r for r in endpoint['results'] if r['q'] == 4 and r['row'] == 7)
    require(any(r['anchor'] == [0, 1, 2] and r['sampled_carriers'] == list(range(5))
                for r in row['unknown_records']), 'not an endpoint UNKNOWN demand')
    # Literal sparse denominator syntax checks, not polynomial evaluation.
    minus_h0 = [['1,1,1,1', 1], ['0,0,0,0', -1]]
    require(model['charts'][0]['dh'] == minus_h0, 'prefix0 exact dh not authenticated')
    for carrier in range(1, 5):
        exponent = ','.join(str(5 if i == carrier - 1 else 0) for i in range(4))
        expected = {('1,1,1,1', 1), (exponent, -1)}
        for name in ('di', 'dp', 'dh'):
            require({tuple(term) for term in model['charts'][carrier][name]} == expected,
                    'primary denominator mismatch')
    path = {'left': [('H', 0), ('E', 1), ('I', 2)],
            'right': [('P', 2), ('H', 1)]}
    left, right = selector.selector_matrices(path, owners)
    require(left.shape == (5, 2) and right.shape == (2, 10), 'selector shape')
    lr = current.Matrix('row', (left, 0), (1, 2))
    rc = current.Matrix('column', (right, 0), (2, 1))
    kernel = current.transpose(current.mul(rc, lr))
    # E34 four terms, coordinates here zero-based. Scalars remain residuals.
    terms = []
    for sign, edge, derivative, kind, coordinate in (
        (1, (3, 4), 2, 'L', 3), (-1, (3, 4), 3, 'L', 2),
        (1, (2, 3), 3, 'U', 2), (-1, (2, 3), 2, 'U', 3)):
        ast = current.normalized_current(kind, coordinate, owners[2:]).data()
        terms.append({'coefficient': [sign, 2], 'scalar_edge': list(edge),
                      'derivative_coordinate': derivative, 'current_kind': kind,
                      'current_coordinate': coordinate, 'normalized_current_ast': ast,
                      'current_block_occurrences': block_inventory(ast),
                      'scalar_leaf': {'type': 'ComplementaryDerivativeOfCanceledT12F12',
                          'edge_owners': [owners[o].data() for o in edge],
                          'coordinate': derivative, 'input_character': [-2, -2, 0, 0],
                          'inner_partition': {'carrier': 14, 'legal': 1},
                          'branches': ['H_rho12', 'Pi12 K_cov R', 'Pi12 S h12 A R'],
                          'inserted_owner': ['inner', 30, 'branch', 'insertion_occurrence'],
                          'inserted_label_domain': {'carrier': [5, 0, 1, 2, 3, 4],
                                                   'legal_mask': list(range(16)), 'standard_tag': list(range(16))},
                          'inserted_label_domain_is_enclosure': True,
                          'standard_owner_binding': 'branch-specific constraints unresolved; not an independent sum over all sixteen tags',
                          'phase': 'await_owned_quotient_before_derivative',
                          'large_composition_sums': 'symbolic_bound_indices_only'}})
    return {'schema': 'a02-seed30-e34-contract-v1', 'request': request,
        'release_manifest_sha256': MANIFEST, 'endpoint_sha256': ENDPOINT_HASH,
        'scope': 'one full five-owner tuple, one seed, E34(T12F12) only; request DAG with typed residual leaves',
        'reviewer': ['Codex-A01', 'Codex-V04'], 'review_status': 'pending',
        'domain': 'characteristic zero; source-first common overlap of all five literal owners; primitive and legal frames and transition determinants invertible',
        'classification': 'BOOLEAN UNKNOWN, neither occupied support nor nonzero value',
        'terminal': {'q': 4, 'row': 7, 'block': 'M20', 'entry': [0, 0],
                     'cell': 'CCCC', 'exponent': [-1, -2, -3, -4],
                     'orientation': 1, 'effective_word_coefficient': 1,
                     'sign_rule': 'lambda4 minus and J2 minus included once'},
        'owner_ledger': [{'owner': v.data(), 'prefix': i < 2,
                         'outer_partition': outer.bind_reference(v),
                         'N14_denominator_template_not_applied': owned.denominator(v).data(),
                         'legal_bits_low_first': owned.decode_legal_mask(v.legal_mask),
                         'standard_bits_high_first': owned.decode_standard_tag(v.standard_tag),
                         'edge_template_standard_powers': [5250*b for b in owned.decode_standard_tag(v.standard_tag)]}
                        for i, v in enumerate(owners)],
        'selector': {'word': 'H0_A E_B I_C Rbar^t P_C H1_B',
                     'left_ast': left.data(), 'right_ast': right.data(),
                     'dual_kernel_ast': kernel.data(),
                     'pairing': 'tr(dual_kernel * normalized_E34)',
                     'block_occurrences': block_inventory(left.data(), ('left',)) + block_inventory(right.data(), ('right',)),
                     'raw_denominator_counts': [
                         {'owner': owners[0].data(), 'dh': 1},
                         {'owner': owners[1].data(), 'di': 1, 'dp': 1, 'dh': 1},
                         {'owner': owners[2].data(), 'di': 1, 'dp': 1},
                         {'owner': owners[3].data()}, {'owner': owners[4].data()}],
                     'prefix0_dh': 'v1*v2*v3*v4-1=-h0; h0=1-v1*v2*v3*v4; retain minus sign',
                     'denominator_count_scope': 'selector before any cancellation; current occurrences and inverse/partial contexts separately inventoried',
                     'mask_merger_applied': False, 'owners_merged': False},
        'frame': {'transition': 'g_uv=D_v K_uv D_u^-1; K_uv=(P_u I_v)^t',
                  'current': 'normalized at C; physical=D_C normalized D_C^-1',
                  'inclusion': 'Iphys_C Rphys^t Pphys_C=I_C Rbar^t P_C exactly once',
                  'log_frame': 'Q_v,d=diag(ell,-ell), ell=m_v,d*(x_d^2+1)/(2*x_d*(x_d^2-1))',
                  'nu_absolute_constants': 'physical convention retained, not set to one as moving functions',
                  'legal_bits': 'low bit d', 'standard_bits': 'high bit 3-d',
                  'local_section_shift': 'tau^(r-2), r=-2 for q4 terminal: tau^-4 once; not per owner',
                  'scalar_weight_shift': 'rho twist0; fixed owner chart pullback once',
                  'derivative_conversion': [owned.character_conversion((2, 3), (0, 1), d) for d in (2, 3)]},
        'terms': terms,
        'inner_edge_rule': 'D_uv=d_u*d_v, each endpoint separately owns H^14, legal(bit1)^1, standard(bit1)^5250; derivative requires combined cancellation and suffix up to 15/2/5251',
        'outer_rule': 'five independent rho54,29 factors; identical owner only; no raw Leibniz piece independently admitted',
        'remaining_Rsharp_contributions': ['M0^0', 'B34(F12)', 'B12(F34)', 'E12(T34F34)'],
        'admission_failures': [
            {'type': 'UnloweredInnerSolver', 'detail': 'exact branch/frame/ordering and N14 owned numerator quotient circuits absent'},
            {'type': 'UnprovedCombinedPoleLedger', 'detail': 'current inverse determinants, source jets, prefix and scalar suffix not lowered into a joint owner pole vector'},
            {'type': 'UnloweredOuterFiniteFormula', 'detail': 'public outer binder is source-definition strings, not executable lowering'},
            {'type': 'MissingCoefficientConvolution', 'detail': 'no branch support/standard shifts with exact inner frame transport and source numerator'},
            {'type': 'MissingCostAndMemoryProof', 'detail': 'no arithmetic schedule, operation count or peak bytes'}],
        'next_step': 'A01/V04 review owner/sign/frame contract; independently lower N14 canceled inner branches and joint owner pole ledger before coefficient admission',
        'actual_source_admitted': False, 'source_pole_domain_proved': False,
        'Laurent_admitted': False, 'actual_factorization_accepted': False,
        'execution_release': False, 'physical_polynomial_evaluation': False,
        'physical_polynomial_expansion': False, 'arithmetic_cost_certificate': False}


if __name__ == '__main__':
    require(len(sys.argv) == 1, 'no CLI fields supported')
    print(json.dumps(build(EXPECTED), indent=2, sort_keys=True))
