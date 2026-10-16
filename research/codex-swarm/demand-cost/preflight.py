"""CO01: bounded stdlib demand metadata, never a physical arithmetic executor."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import resource
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MAX_BYTES = 4_000_000
MAX_NODES = 20_000


def need(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load(path):
    need(path.stat().st_size <= MAX_BYTES, 'metadata byte bound')
    return json.loads(path.read_bytes())


def authenticate():
    pins = load(HERE / 'source-pins.json')
    for name, sha in pins['local'].items():
        p = ROOT / name
        need(p.stat().st_size <= MAX_BYTES, 'pinned metadata size')
        need(digest(p.read_bytes()) == sha, 'local source drift: ' + name)
    for name, pin in pins['git'].items():
        raw = subprocess.check_output(['git', 'show', pin['commit'] + ':' + name],
                                      cwd=ROOT, timeout=10)
        need(len(raw) <= MAX_BYTES and digest(raw) == pin['sha256'], 'Git source drift')
    return pins


def requests():
    obj = load(ROOT / 'detector-selection/weighted-requests.json')
    rows = obj['requests']
    need(len(rows) == 32 and [r['id'] for r in rows] == list(range(32)), '32 request IDs')
    for r in rows:
        need(set(r['scalar_map']) == {'i', 'b'}, 'actual map required')
        for t in r['terms']:
            m = t['dual_monomial']
            need(len(m) == 4 and all(type(x) is int and 0 <= x <= 2 for x in m), 'monomial')
            need(t['laurent_exponents'] == [-x-1 for x in m], 'Laurent coordinate')
            need(t['output_index'] == sum((2-x)*3**(3-i) for i,x in enumerate(m)), 'index')
            need(type(t['coefficient']) is int and t['coefficient'] != 0, 'integer weight')
    return rows


def demand_join(rows):
    groups = {}
    for r in rows:
        for t in r['terms']:
            key = (r['scalar_map']['i'], r['scalar_map']['b'], tuple(t['laurent_exponents']))
            groups.setdefault(key, []).append({'request_id': r['id'], 'weight': t['coefficient']})
    return [{'map': {'i': i, 'b': b}, 'coordinate': list(e), 'uses': uses}
            for (i,b,e),uses in sorted(groups.items())]


def owner(v):
    need(isinstance(v, list) and len(v) == 5 and all(type(x) is int for x in v), 'full owner')
    need(v[0] >= 0 and v[1] >= 0 and v[2] in range(6) and v[3] in range(16)
         and v[4] in range(16), 'owner range')
    return tuple(v)


def grammar_join(groups, grammar):
    """Explicit coefficient-demand DAG only. No interpretation of source formulas.

    Every group must have its own exact map+coordinate entry. References in a
    topologically ordered DAG may be reused only within an identical scope.
    A scope is (map, coordinate, ordered full owners, source branch ID, frame).
    Formula equality across scopes never creates sharing.
    """
    need(grammar['schema'] == 'co01-demand-grammar-v1', 'grammar schema')
    nodes = grammar['nodes']; entries = grammar['entries']
    need(len(nodes) <= MAX_NODES and len(entries) <= MAX_NODES, 'grammar node bound')
    known = {}; counts = {}; scopes = {}; refs = Counter()
    for n in nodes:
        need(set(n) == {'id','map','coordinate','owners','source_branch_id','frame','op','inputs'}, 'node keys')
        nid = n['id']
        need(isinstance(nid, str) and nid and nid not in known, 'unique node ID')
        need(set(n['map']) == {'i','b'} and all(type(v) is int for v in n['map'].values()), 'map')
        need(len(n['coordinate']) == 4 and all(type(x) is int for x in n['coordinate']), 'coordinate')
        need(isinstance(n['source_branch_id'], str) and n['source_branch_id'], 'source branch ID')
        need(isinstance(n['frame'], str) and n['frame'], 'frame')
        need(n['owners'] and len(n['owners']) <= 64, 'owner list bound')
        full = [owner(v) for v in n['owners']]
        need(len(set(full)) == len(full), 'duplicate owner occurrence')
        scope = canonical([n['map'],n['coordinate'],n['owners'],n['source_branch_id'],n['frame']])
        need(n['op'] in ('leaf','add','multiply','differentiate','contract','transport'), 'formal op')
        need(isinstance(n['inputs'], list) and len(n['inputs']) <= 64, 'fan-in bound')
        need((n['op'] == 'leaf') == (not n['inputs']), 'leaf arity')
        need(all(x in known and scopes[x] == scope for x in n['inputs']), 'forward/cyclic/cross-scope reference')
        # Tree size computed by DP; integer bit bound prevents an enormous counter.
        size = 1 + sum(counts[x] for x in n['inputs'])
        need(size.bit_length() <= 128, 'formal traversal counter bound')
        known[nid] = n; scopes[nid] = scope; counts[nid] = size
    expected = {canonical([g['map'],g['coordinate']]) for g in groups}
    seen = set(); roots = []
    for e in entries:
        need(set(e) == {'map','coordinate','roots'}, 'entry keys')
        key = canonical([e['map'],e['coordinate']])
        need(key in expected and key not in seen and e['roots'], 'exact entry coverage')
        seen.add(key)
        for r in e['roots']:
            need(r in known and known[r]['map'] == e['map'] and known[r]['coordinate'] == e['coordinate'], 'root scope')
            roots.append(r)
    need(seen == expected, 'missing actual map/coordinate grammar; no Phi78 substitution')
    reachable = set(); stack = list(roots)
    while stack:
        nid = stack.pop(); refs[nid] += 1
        if nid in reachable:
            continue
        reachable.add(nid); stack.extend(known[nid]['inputs'])
    tree = sum(counts[r] for r in roots)
    return {'status':'supplied formal grammar only; source semantics unverified',
            'root_references':len(roots), 'tree_node_visits':tree,
            'reachable_unique_nodes':len(reachable), 'reuse_visits_avoided':tree-len(reachable),
            'dag_edge_references':sum(len(known[x]['inputs']) for x in reachable),
            'scopes':len({scopes[x] for x in reachable}),
            'op_nodes':dict(sorted(Counter(known[x]['op'] for x in reachable).items())),
            'owner_source_groups':[json.loads(s) for s in sorted({scopes[x] for x in reachable})],
            'physical_arithmetic_counts':'UNKNOWN', 'occupied_support':'UNKNOWN'}


REQUIRED = [
    'authoritative CURRENT global ledger identity, revision, freshness and reconciliation',
    'global caps, measured spent, globally identified live allocations and all commitments',
    'actual whole-F source-clearing proof and full-sum numerator realization',
    'actual transport/frame/domain and complete corrected scalar compiler binding for all maps',
    'actual coefficient bounds, representation, operation upper bounds and allocation last-use schedule',
    'independent root review of certificates and schedule; existing allowances are not fresh budget',
]


def admission(evidence=None):
    # This producer has no authority/freshness verifier or physical schedule checker.
    # In particular JSON booleans, old caps and file lengths cannot open this gate.
    return {'arithmetic_admission':False, 'execution_release':False,
            'cost_upper':'UNKNOWN', 'physical_peak_bytes':'UNKNOWN',
            'occupied_support':'UNKNOWN', 'cancellation_savings_charged':0,
            'fresh_budget_granted':0, 'old_allowances_are_spent':False,
            'required_inputs':REQUIRED,
            'evidence_status':'unverified metadata only' if evidence is not None else 'absent'}


def build(grammar=None, evidence=None):
    pins = authenticate(); rows = requests(); groups = demand_join(rows)
    by_map = []
    for i,b in sorted({(r['scalar_map']['i'],r['scalar_map']['b']) for r in rows}):
        selected = [r for r in rows if r['scalar_map'] == {'i':i,'b':b}]
        gs = [g for g in groups if g['map'] == {'i':i,'b':b}]
        by_map.append({'map':{'i':i,'b':b}, 'requests':len(selected),
                       'weighted_term_occurrences':sum(len(r['terms']) for r in selected),
                       'unique_coordinates':len(gs)})
    terms = sum(len(r['terms']) for r in rows)
    formal = grammar_join(groups, grammar) if grammar is not None else {
        'status':'UNKNOWN: complete actual-map coefficient-demand grammar not supplied',
        'owner_source_groups':None, 'tree_node_visits':None, 'reachable_unique_nodes':None,
        'reuse_visits_avoided':None,
        'required_input':'co01-demand-grammar-v1 with each exact map/coordinate, ordered full owners, source branch IDs and explicit DAG roots'}
    return {'schema':'co01-demand-cost-report-v1',
            'source_pins_sha256':digest((HERE/'source-pins.json').read_bytes()),
            'totals':{'weighted_requests':len(rows), 'actual_maps':len(by_map),
                      'weighted_term_occurrences':terms, 'unique_map_coordinates':len(groups),
                      'coordinate_reuses':terms-len(groups),
                      'distinct_coordinates_ignoring_map':len({tuple(g['coordinate']) for g in groups}),
                      'sum_absolute_weights':sum(abs(t['coefficient']) for r in rows for t in r['terms'])},
            'by_map':by_map, 'requests':rows, 'coefficient_demands':groups,
            'formal_circuit':formal,
            'v5_scope':'seed12/30 fixed-owner E34 metadata only; no all-map reuse authorized',
            'null_lemma':{'commit':'10810ee877fdaf291399198ad60d7dd0c316a42d',
                'conditional_full_sum_only':True, 'max_derivatives':1,
                'branches':[{'id':'standard','term':'C_a C_b Z_ab B_ab','complete_B_required':True},
                            {'id':'prism1','term':'Z_ab sum_u Qhat_u P_[u,a,b]','padding':'Z_ab'},
                            {'id':'prism2','term':'-C_a Z_ab sum_uv Qhat_u Qhat_v P_[u,v,b]','padding':'C_a Z_ab'}],
                'source_clearing_proved_here':False,
                'order_comparison':'reindexing does not identify ordered E prescriptions; retain curvature defects and full-source comparison'},
            'preflight':admission(evidence), 'physical_source_evaluated':False,
            'obstruction':'undecided'}


def main():
    resource.setrlimit(resource.RLIMIT_AS, (256*1024**2,256*1024**2))
    resource.setrlimit(resource.RLIMIT_CPU, (15,15))
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--grammar', type=Path); p.add_argument('--evidence',type=Path)
    a = p.parse_args()
    report = build(load(a.grammar) if a.grammar else None, load(a.evidence) if a.evidence else None)
    print(json.dumps(report,sort_keys=True,indent=2,allow_nan=False))


if __name__ == '__main__':
    main()
