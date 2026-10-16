"""Translate selected dual classes to weighted Laurent requests; no source values."""
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SELECTION_SHA = '54603e2e3634d73da740837081297800f3b2b3bb219aeccd22141ac27e58368d'
ZERO = (0, 0, 0, 0)

def need(ok, message):
    if not ok:
        raise ValueError(message)

def multiply(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            w = tuple(s + t for s, t in zip(u, v))
            out[w] = out.get(w, 0) + x * y
    return {m: c for m, c in out.items() if c}

def elementary(k):
    return {tuple(int(i in subset) for i in range(4)): 1
            for subset in itertools.combinations(range(4), k)}

def index(m):
    need(len(m) == 4 and all(type(x) is int and 0 <= x <= 2 for x in m),
         'dual monomial outside O(2)^4')
    return sum((2 - x) * 3 ** (3 - i) for i, x in enumerate(m))

def build(raw=None):
    raw = (HERE / 'selection.json').read_bytes() if raw is None else raw
    need(hashlib.sha256(raw).hexdigest() == SELECTION_SHA, 'selection drift')
    selected = json.loads(raw)
    q = {(1, 1, 0, 0): 1, (0, 0, 1, 1): 1}
    v = [elementary(k) for k in range(5)]
    records = []

    def add(i, b, block, monomial, weight):
        terms = [{'dual_monomial': list(m), 'coefficient': c,
                  'laurent_exponents': [-x - 1 for x in m], 'output_index': index(m)}
                 for m, c in sorted(weight.items(), key=lambda item: index(item[0]))]
        records.append({'id': len(records), 'scalar_map': {'i': i, 'b': b},
                        'block': block, 'base_monomial': monomial, 'terms': terms})

    for i, b in selected['I20']:
        add(i, b, 'Q^2', [], multiply(q, q))
    for label in selected['selected']['minus1']['labels']:
        k, = label['base_monomial']
        add(label['i'], label['b'], 'v_k Q', [k], multiply(v[k], q))
    for label in selected['selected']['zero']['labels']:
        k, l = label['base_monomial']
        add(label['i'], label['b'], 'v_k v_l', [k, l], multiply(v[k], v[l]))
    need(len(records) == 32, '32 weighted pairings required')
    return {'schema': 'codex-weighted-scalar-requests-v1',
            'selection_sha256': SELECTION_SHA,
            'comparison': {'commit': '08b73637d4136f91606aad332c46cafd064417f8',
                           'path': 'research/hm/current-scalar-proof/map-and-comparison.md',
                           'rule': 'e=-m-1; k=sum_i (2-m_i)*3^(3-i), i=0..3'},
            'normalization': 'v_k=e_k(x1,x2,x3,x4); v0=1; Q=x1*x2+x3*x4; unscaled',
            'scalar_map_convention': 'L_i,b=X13[i,b]-sum gamma[i,a,k]*X02[a,5*b+k]',
            'required_frame': 'original frame, deck product removed, internal degree -2 factor tau^-4',
            'interpretation': '32 weighted sums of scalar Laurent outputs, not 32 individual positions',
            'requests': records,
            'gates': {'complete_corrected_source_bound': False, 'regular_transport_bound': False,
                      'physical_source_evaluated': False, 'execution_release': False},
            'obstruction': 'undecided'}

if __name__ == '__main__':
    print(json.dumps(build(), sort_keys=True, indent=2))
