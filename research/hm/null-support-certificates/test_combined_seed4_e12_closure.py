"""Disjoint coverage and actual-term binding; no physical polynomial evaluation."""
import hashlib,itertools,json,unittest
from collections import Counter
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import lower_primary_carrier_sector as primary
import lower_permuted_standard_sector as permuted
import lower_legal_mask_sector as legal
import lower_exceptional_carrier_sector as exceptional
ROOT=Path(__file__).parent
def read(n):return json.loads((ROOT/n).read_text())
def key(cs,ms,ts):return tuple(zip(cs,ms,ts))
def rows():
    return [('legal',r,(3,11,15)) for r in read('legal-mask-sector-support.json')['active_results']]+[('primary',r,(3,11,15)) for r in read('primary-carrier-sector-support.json')['results']]+[('permuted',r,(11,3,15)) for r in read('permuted-standard-sector-support.json')['results']]
def validate_term_binding(job):
    kind,r,tags=job;ms=tuple(r['legal_masks']);cs=(1,2,4) if kind=='legal' else tuple(r['carriers'])
    a=legal.build(ms) if kind=='legal' else (primary if kind=='primary' else permuted).build(ms,cs)
    assert hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':')).encode()).hexdigest()==r['dag_sha256']
    assert json.loads(json.dumps(a['owners']))==r['owners']==[[4,o,c,m,t] for o,(c,m,t) in enumerate(zip(cs,ms,tags))]
    assert len(a['terms'])==4 and len(r['multipliers'])==8
    assert a['selector_terminal_coefficient_included_once']==-2
    assert a['sorting_sign']==(1 if tags==(3,11,15) else -1)
    assert a['frame']=='global finite; normalized current after matching physical conjugation cancellation; outer scalar weights pulled back once; no section twist on scalar rho'
    assert a['pinned_model_sha256']==primary.source.MODEL_SHA256
    shape=(((1,2),0,['L',1],1),((1,2),1,['L',0],-1),((0,1),1,['U',0],1),((0,1),0,['U',1],-1))
    for j,(term,expected) in enumerate(zip(a['terms'],shape)):
        assert (tuple(term['edge']),term['coordinate'],term['current'],term['E_sign'])==expected
        M=[(0,0,-2,-2)[i]+sum(5321+2*((ms[o]>>i)&1) for o in term['edge']) for i in range(4)]
        for k,ab in enumerate(('A','B')):
            saved=r['multipliers'][2*j+k]
            assert saved['root']==term[ab]['root'] and saved['edge']==list(term['edge']) and saved['kind']==ab
            assert saved['derivative']==(term['coordinate'] if ab=='B' else None)
            assert saved['complete_numerator_degree']==M and saved['status']=='certified_zero'
            cert=saved['certificate'];assert cert and cert['gap']>0
            w=cert['normal'];shift=[int(ab=='B' and i==term['coordinate']) for i in range(4)]
            assert cert['target_projection']==sum(w[i]*((-1,-2,-2,-2)[i]+shift[i]) for i in range(4))
            assert [list(x['owner']) for x in term[ab]['derived_denominators']]==r['owners']
            for d in term[ab]['derived_denominators']:
                assert 0<=d['carrier']<=54
                assert all(0<=x<=29 for x in d['legal']) and all(0<=x<=5251 for x in d['standard'])
                for i in range(4):
                    assert not d['legal'][i] or ((d['owner'][3]>>i)&1)
                    assert not d['standard'][i] or ((d['owner'][4]>>(3-i))&1)
    return key(cs,ms,tags)
class CombinedClosureTests(unittest.TestCase):
    def test_exhaustive_disjoint_assignment_partition(self):
        supported={key((1,2,4) if kind=='legal' else r['carriers'],r['legal_masks'],tags) for kind,r,tags in rows()}
        self.assertEqual(len(supported),2048);seen=set();counts=Counter();by_tags={}
        pairs=tuple(itertools.product(range(6),range(16)))
        for labels in itertools.product(pairs,repeat=3):
            ordered=tuple(sorted(((c,m,t) for (c,m),t in zip(labels,(3,11,15))),key=lambda v:(-1 if v[0]==5 else v[0],v[1],v[2])))
            tags=tuple(t for c,m,t in ordered);c=by_tags.setdefault(tags,Counter());c['full']+=1
            active=all(exceptional.outer_maybe_active(*v) for v in ordered)
            c['outer_active' if active else 'outer_inactive']+=1
            if any(v[0] in (0,5) for v in ordered):
                self.assertIn(ordered[0][0],(0,5));counts['exceptional_column_zero']+=1
                if active:c['exceptional_first']+=1
            elif not active:counts['primary_outer_zero']+=1
            elif ordered[0][0]==2:
                counts['primary_carrier2_zero']+=1;c['carrier2_first']+=1
            else:
                self.assertIn(ordered,supported);self.assertNotIn(ordered,seen);seen.add(ordered)
                counts['primary_support_zero']+=1;c['other_first']+=1
        self.assertEqual(seen,supported)
        self.assertEqual(dict(counts),{'exceptional_column_zero':622592,'primary_outer_zero':259072,'primary_carrier2_zero':1024,'primary_support_zero':2048})
        self.assertEqual(sum(counts.values()),884736)
        for r in read('permuted-standard-domain-inventory.json')['full_carriers_0_through_5']:
            self.assertEqual(dict(by_tags[tuple(r['standard_tags'])]),r['counts'])
        model=primary.source.authenticate()
        for carrier in (0,2,5):self.assertEqual([r[6] for r in model['charts'][carrier]['P']],[[],[]])
    def test_every_certificate_matches_actual_term_and_domain(self):
        jobs=rows();self.assertEqual(len(jobs),2048)
        with ProcessPoolExecutor(max_workers=4) as pool:keys=list(pool.map(validate_term_binding,jobs,chunksize=4))
        self.assertEqual(len(set(keys)),2048)
if __name__=='__main__':unittest.main()
