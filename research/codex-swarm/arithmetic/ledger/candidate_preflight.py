"""Pinned candidate metadata join only; python -B candidate_preflight.py."""
from pathlib import Path
import subprocess
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from package_snapshot import package_path
import hashlib
import importlib.util
import json
import sys
from schedule_validator import need

RELEASE = '6e28c6b59f8245779f6c03a20798e4de6842ae19'
SOURCE = '08b73637d4136f91606aad332c46cafd064417f8'
PUBLIC = package_path()
ROOT = Path(__file__).resolve().parents[2]
MANIFEST = 'ec0746ba0d537ec3edeb96f396a02e426225e904227e4c500dad0f5e0d3fbb64'
INPUTS = {'seed12-e34-request.json': '0208f95688e0b07e6320994713f807baf1e7e49c1938415bbe6b61d903fcfdb6', 'seed12-e34-demand.json': 'b9c1fcb399f525249515b4e70bffb8993eefb19b4f06a6818bca715a4680f776', 'primary_current_adapter.py': 'e6c38d9143b4b5ce55f0f4a25d71e885d41210fb74530dbc550ca8c565064287', 'Codex-V01-endpoint-support.json': '18faf702e382b1484ca6b3f8e08ff2f8500f615cc9d3c27227dee968306aa24e', 'Codex-V01-requests.json': '081f24fcce24a9e082269d370e7209796e606ca47ff4081a13e545d756aeb3ed', 'seed30_e34_contract.json': 'ef4c78a21957c1575ecdf15d34eb1cd8aaa31dd369a3c2e85c29aa9fc295dc52', 'example_e34_review.json': 'db724efc5ce603d22c9b0d897ea2d1995916af2d2393131a37eb876bee18597b'}
FILES = {'seed12-e34-request.json': 'arithmetic/seed12/seed12-e34-request.json', 'seed12-e34-demand.json': 'arithmetic/seed12/seed12-e34-demand.json', 'primary_current_adapter.py': 'arithmetic/primary_current/primary_current_adapter.py', 'Codex-V01-endpoint-support.json': 'certificates/endpoint-support.json', 'Codex-V01-requests.json': 'certificates/Codex-V01-requests.json'}

def input_bytes(label, digest):
    if label in FILES:
        return raw(ROOT / FILES[label], digest)
    if label == 'seed30_e34_contract.json':
        args = [str(ROOT / 'arithmetic/seed30/seed30_e34_contract.py')]
    elif label == 'example_e34_review.json':
        args = [str(ROOT / 'arithmetic/primary_current/primary_current_adapter.py'),
                str(ROOT / 'arithmetic/primary_current/example_e34_request.json')]
    else:
        raise ValueError('unknown metadata builder')
    data = subprocess.check_output([sys.executable, '-B', *args], timeout=30)
    need(len(data) <= 4_000_000, 'bounded symbolic metadata output')
    need(hashlib.sha256(data).hexdigest() == digest, 'generated metadata drift: ' + label)
    return data


def raw(path, digest):
    p = Path(path)
    need(p.stat().st_size <= 4_000_000, 'metadata input exceeds bound')
    data = p.read_bytes()
    need(hashlib.sha256(data).hexdigest() == digest, 'input changed: ' + str(path))
    return data

def load_owned():
    need(sys.dont_write_bytecode, 'use python -B')
    m = json.loads(raw(PUBLIC / 'release-manifest.json', MANIFEST))
    need(m['public_source_commit'] == SOURCE and m['execution_release'] is False, 'public source/gate')
    name = 'owned_scalar_denominator_binding'
    path = PUBLIC / (name + '.py')
    raw(path, m['files_sha256'][path.name])
    need(name not in sys.modules, 'preloaded binder unsupported')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def run():
    owned = load_owned()
    data = {p: input_bytes(p, digest) for p, digest in INPUTS.items()}
    obj = {Path(p).name: json.loads(v) for p, v in data.items() if p.endswith('.json')}
    a = obj['seed12-e34-demand.json']; b = obj['seed30_e34_contract.json']
    endpoint = obj['Codex-V01-endpoint-support.json']
    need(endpoint['source_commit'] == RELEASE and endpoint['domain_is_flag_superdomain'] is True, 'endpoint scope')
    need(a['request'] == obj['seed12-e34-request.json'], 'A01 request mismatch')
    requests = obj['Codex-V01-requests.json']
    need(requests['source_commit'] == RELEASE and len(requests['records']) == 2, 'V01 request source/domain')
    candidates = []
    for artifact, row, q, request, source_terms, occurrence_key in [
        (a, 4, 3, a['request'], a['terms'], 'current_block_occurrences'),
        (b, 7, 4, b['request'], b['terms'], 'current_block_occurrences')]:
        need(request['release_pin'] == RELEASE and request['source_pin'] == SOURCE, 'candidate pin')
        owners = request['owners']; seed = request['seed']
        expected = ([[12,0,5,8,1],[12,1,1,9,9],[12,2,2,11,13],[12,3,4,15,15]] if seed == 12 else
                    [[30,0,0,0,0],[30,1,1,1,8],[30,2,2,3,12],[30,3,3,7,14],[30,4,4,15,15]])
        need(seed in (12,30) and owners == expected and len(source_terms) == 4, 'unsupported exact request')
        channel = request.get('operator', request.get('channel'))
        need(channel == 'E34(T12F12)', 'unsupported channel')
        demand = [r for r in requests['records'] if r['seed'] == seed]
        need(len(demand) == 1, 'exact V01 request required')
        demand = demand[0]
        need([r['owner'] for r in demand['owners']] == owners and demand['q'] == q
             and demand['cloud_row'] == row and demand['source_sort_sign'] == 1
             and demand['prefix_mask_collapse_applied'] is False, 'V01 exact fixed-mask scope')
        coefficient = a['selector_binding']['coefficient'] if seed == 12 else b['terminal']['effective_word_coefficient']
        need(coefficient == demand['effective_coefficient'] == (2 if seed == 12 else 1), 'effective coefficient sign')
        if seed == 30:
            need(b['terminal']['orientation'] == 1, 'q4 orientation')
        vs = [owned.VertexLabel(*v) for v in owners]
        records = [r for x in endpoint['results'] if x['q'] == q and x['row'] == row
                   for r in x['unknown_records'] if r['sorted_carriers'] == [v.carrier for v in vs]]
        need(bool(records), 'candidate absent from endpoint UNKNOWN flags')
        tail = vs[-3:]
        adapter_domain = all(v.carrier in range(1,5) for v in tail)
        adapter_domain &= len({(v.carrier,v.legal_mask,v.standard_tag) for v in tail}) == 3
        selector_counts = a['kernel_block_occurrences'] if seed == 12 else b['selector']['block_occurrences']
        candidates.append({
            'seed': seed, 'q': q, 'row': row, 'channel': channel, 'owners': owners,
            'orientation_and_coefficient': (a['selector_binding']['coefficient'] if seed==12 else b['terminal']),
            'classification': 'BOOLEAN_UNKNOWN carrier flag; no occupied-support or nonzero assertion',
            'endpoint_records': records,
            'owner_bits': [{'owner': v.data(), 'legal_low_first': owned.decode_legal_mask(v.legal_mask),
                            'standard_high_first': owned.decode_standard_tag(v.standard_tag)} for v in vs],
            'selector_block_occurrences': selector_counts,
            'current_block_occurrences_by_term': [t[occurrence_key] for t in source_terms],
            'fixed_mask_scope': demand['request_scope'],
            'full_owner_denominator_evidence': {
                'artifact': 'seed12-e34-demand.json' if seed == 12 else 'seed30_e34_contract.json',
                'location': 'dag combined_inner_regularization_request.suffix_denominators' if seed == 12 else 'owner_ledger and terms.scalar_leaf',
                'authenticated_by': 'metadata_footprints exact artifact SHA256',
                'owner_merging_permitted': False, 'derivative_poles_certified': False},
            'scalar_edges_by_term': [t['edge_owners'] if seed == 12 else t['scalar_edge'] for t in source_terms],
            'owner_denominator_scope': 'full owner occurrence counts copied without merging; not pole orders',
            'frame': artifact['frame'],
            'combined_cancellation_before_derivative': 'required, unresolved',
            'A05_tail_domain_compatible': bool(adapter_domain),
            'A05_sample_reused_as_candidate': False,
            'physical_operation_counts': None, 'physical_peak_bytes': None,
            'schedule_admitted': False, 'actual_source_admitted': False,
            'source_pole_domain_proved': False, 'execution_release': False})
    adapter = obj['example_e34_review.json']
    need(adapter['release_pin'] == RELEASE and adapter['source_pin'] == SOURCE, 'A05 pins')
    need(adapter['execution_release'] is False and adapter['actual_source_admitted'] is False, 'A05 gates')
    return {'schema':'a06-candidate-schedule-preflight-v1', 'release_pin': RELEASE, 'source_pin': SOURCE,
            'domain':'exact A01 seed12 q3 row4 and A02 seed30 q4 row7 owner tuples; E34(T12F12) only',
            'metadata_footprints': [{'path':p, 'sha256':INPUTS[p], 'serialized_bytes':len(v),
                                     'metric':'actual file length; excludes Python heap and physical arithmetic storage'}
                                    for p,v in data.items()],
            'A01_shared_symbolic_nodes':len(a['dag']), 'A05_sample_symbolic_nodes':len(adapter['dag']),
            'candidates':candidates,
            'global_state': {'caps':None, 'spent':None, 'reservations':None, 'live_allocations':None,
                             'complete':False, 'historical_149_is_spent':False,
                             'historical_294117_is_live':False},
            'gap':['authenticated current global caps/spent/reservations/live allocations absent',
                   'physical representation, operation counts, output/workspace bounds and last uses absent',
                   'combined source/pole certificates unresolved; metadata DAG nodes are not product costs'],
            'Rsharp_contributions_required': ['M(0)^0','F_q k_p','F_p k_q','E_p(T_q F_q)','E_q(T_p F_p)'],
            'Rsharp_coverage':'two E34 requests only; no all-five-contribution detector claim; Moyal alone is not Omega',
            'arithmetic_admission':False, 'execution_release':False,
            'evidence':'hash-pinned read-only artifact join, exact owner/endpoint match; no physical arithmetic or seed4 scan',
            'reviewer':['Codex-V06','Codex-I01'], 'artifact_review':'pending',
            'next_step':'V06/I01 review; supply actual global state and certified physical costs before schedule admission'}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
