"""Pinned finite quotient-frontier assembly, not a map or realization test."""
from pathlib import Path
from collections import Counter
from copy import deepcopy
import hashlib,json
ROOT=Path(__file__).resolve().parent
HASHES={'one-one-endpoint-necessary-pairs.json': '6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb', 'one-two-finite-quotient-pairs.json': '2d370a48816184483aae90908daab024d632d988622e609213eb7fa3ead89229', 'one-two-endpoint-orbit-constraints.json': 'af45a62b5a21ae386e240352a924740f62fc75796c34dd1f0afa024052fbc376', 'two-one-primal-interior-quotient-summary.json': '33c37ec7fe996888465d7950ebab02100c73177fceb85e9fde5434edcbbd575c'}
DIMS={'one':1,'W':2,'Wp':2,'A':3,'V':3,'P':4,'S':4,'D':5,'T':6}
PINS={'11':'4c147e95217f0900fa13f195662d95e933412c3c',
      '12':'857cd414252618a53a79ddce72982c6d91341db9',
      '21':'f7071d29886c83151028576bf32e001c347cafc9'}
def read(name):
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==HASHES[name], ('input changed',name)
    return json.loads(raw)
def normal(blocks):
    return sorted([[int(e),n] for e,n in blocks])
def degree(blocks):return sum(e*DIMS[n] for e,n in blocks)
def row(profile,index,pair,defect):
    A,B=normal(pair['A']),normal(pair['B'])
    identity=json.dumps([profile,A,B],separators=(',',':'))
    return dict(id='G3.'+profile+'.'+hashlib.sha256(identity.encode()).hexdigest()[:12],
                profile=profile,A=A,B=B,original_defect=defect,
                source_index=index,source_commit=PINS[profile])
def validate(rows):
    assert len(rows)==182
    assert Counter(p['profile'] for p in rows)=={'11':159,'12':10,'21':13}
    keys=[]
    for p in rows:
        assert p['profile'] in PINS and p['source_commit']==PINS[p['profile']]
        for blocks in (p['A'],p['B']):
            assert sum(DIMS[n] for e,n in blocks)==3
            assert all((e%2==0)==(n in ('one','A','V')) for e,n in blocks)
        assert p['original_defect']==-6-degree(p['A'])-degree(p['B'])
        assert p['original_defect'] in {'11':{0,12,20,24},'12':{0},'21':{0,12}}[p['profile']]
        keys.append(json.dumps([p['profile'],normal(p['A']),normal(p['B'])],separators=(',',':')))
    assert len(set(keys))==182 and len({p['id'] for p in rows})==182
    assert Counter(p['original_defect'] for p in rows)=={0:101,12:63,20:5,24:13}
    return True
one=read('one-one-endpoint-necessary-pairs.json')
two=read('one-two-finite-quotient-pairs.json')
end=read('one-two-endpoint-orbit-constraints.json')
dual=read('two-one-primal-interior-quotient-summary.json')
assert len(one)==159 and len(two['pairs'])==25 and len(dual['pairs'])==13
assert end['remaining_pair_ids']==[0,2,4,6,7,8,12,14,20,21]
rows=[row('11',i,p,p['defect']) for i,p in enumerate(one)]
rows += [row('12',i,two['pairs'][i],0) for i in end['remaining_pair_ids']]
rows += [row('21',i,p,p['original_defect']) for i,p in enumerate(dual['pairs'])]
assert validate(rows)
# Fail closed on duplicate, defect, rank or profile corruption.
for mutation in ('duplicate','defect','rank','profile'):
    bad=deepcopy(rows)
    if mutation=='duplicate':bad[1]=deepcopy(bad[0])
    elif mutation=='defect':bad[0]['original_defect']+=1
    elif mutation=='rank':bad[0]['A']=bad[0]['A'][:-1]
    else:bad[0]['profile']='22'
    try:validate(bad)
    except (AssertionError,KeyError):pass
    else:raise AssertionError('corruption accepted: '+mutation)
out=dict(scope='Remaining rank-three maximal-profile-labelled ordered quotient splitting pairs only',
    total=182,by_profile={'11':159,'12':10,'21':13},
    by_original_defect={0:101,12:63,20:5,24:13},
    mutually_exclusive_labels=True,exhaustive_necessary_overlist=True,
    realizations_claimed=False,global_proof_completion_fraction=None,
    source_hashes=HASHES,cases=rows)
(ROOT/'rank-three-quotient-frontier-182.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS: 182 distinct profile-labelled necessary quotient cases =159+10+13.')
print('PASS: original defect counts101/63/5/13; rank, parity, degree, pins and four corruption tests.')
print('Not a count of actual configurations, work remaining, or a proof-completion fraction.')
