"""Preserve the frozen 182-case baseline while recording proved exclusions."""
from pathlib import Path
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parent
HASHES={'rank-three-quotient-frontier-182.json': 'd4cdaa4dfd29b185d74f7ab34978df834aa39a60d96b339f7b0043c0fc4a2792', 'unrestricted-dual-splittings-and-pairs.json': '9aac29c629b7eb7d2e507eb663571221626a435b995809f05ecad627db126fab', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16'}
PIN='0b55b84466c62c24f05f7e691f3e7a3d528b7ebf'
def read(f):
    b=(R/f).read_bytes();assert hashlib.sha256(b).hexdigest()==HASHES[f],f
    return json.loads(b)
base=read('rank-three-quotient-frontier-182.json')
dual=read('unrestricted-dual-splittings-and-pairs.json')
end=read('two-one-rank-eleven-endpoint-splittings.json')
assert base['total']==182
assert dual['inputs']['one-one-endpoint-necessary-pairs.json']==base['source_hashes']['one-one-endpoint-necessary-pairs.json']
assert dual['inputs']['one-two-finite-quotient-pairs.json']==base['source_hashes']['one-two-finite-quotient-pairs.json']
assert dual['inputs']['one-two-endpoint-orbit-constraints.json']==base['source_hashes']['one-two-endpoint-orbit-constraints.json']
assert end['source_sha256']==base['source_hashes']['two-one-primal-interior-quotient-summary.json']
keep={}
for key,profile in [('one_one','11'),('one_two','12')]:
    records=dual['compatibility'][key]
    assert all(p['Q_ids'] and all(0<=i<len(dual['profiles']) for i in p['Q_ids']) for p in records)
    ids=[p['pair_id'] for p in records];assert len(ids)==len(set(ids))
    keep[profile]=set(ids)
keep['21']={p['source_pair_index'] for p in end['pairs'] if p['retained_second_defects']}
assert {p:len(ids) for p,ids in keep.items()}=={'11':126,'12':10,'21':12}
for profile,ids in keep.items():
    original={c['source_index'] for c in base['cases'] if c['profile']==profile}
    assert ids<=original
for p in end['pairs']:
    c=next(c for c in base['cases'] if c['profile']=='21' and c['source_index']==p['source_pair_index'])
    assert sorted(c['A'])==sorted(p['A']) and sorted(c['B'])==sorted(p['B'])
rows=[]
for c in base['cases']:
    survives=c['source_index'] in keep[c['profile']]
    rows.append(dict(c,status='not_excluded' if survives else 'excluded',
      refinement_commit=PIN,reason='necessary compatibility retained' if survives else
       'no common unrestricted dual source type' if c['profile']=='11' else
       'no rank-eleven endpoint splitting'))
surv=[c for c in rows if c['status']=='not_excluded']
ex=[c for c in rows if c['status']=='excluded']
assert len(rows)==182 and len(surv)==148 and len(ex)==34
assert Counter(c['profile'] for c in ex)=={'11':33,'21':1}
assert Counter(c['original_defect'] for c in surv)=={0:80,12:53,20:2,24:13}
assert len({c['id'] for c in rows})==182
out=dict(scope=base['scope'],baseline_total=182,excluded=34,not_excluded=148,
    remaining_by_profile={'11':126,'12':10,'21':12},
    excluded_by_profile={'11':33,'12':0,'21':1},
    baseline_commit='9b85030822b86ce6a304dd6fd886107404c8c5d7',refinement_commit=PIN,
    source_hashes=HASHES,realizations_claimed=False,global_proof_completion_fraction=None,cases=rows)
(R/'rank-three-quotient-frontier-148.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS: fixed182 baseline,34 excluded,148 not excluded=126+10+12; every stable ID preserved.')
print('PASS: exact source-index correspondence, nonempty common-source witnesses, and original defect counts80/53/2/13.')
print('This is a scoped quotient classification, not overall proof completion.')
