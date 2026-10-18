"""Independent integer support audit; no physical polynomial operations."""
from pathlib import Path
import hashlib,itertools,json,unittest
import lower_primary_carrier_sector as lowering
import preflight_primary_carrier_sector as scan
import test_selected_support_separation_independent as independent
ROOT=Path(__file__).parent

class PrimaryCarrierTests(unittest.TestCase):
    def test_source_first_domain_partition(self):
        full=active=anchor_two=0;carrier_counts={}
        for keys in itertools.combinations_with_replacement(tuple(itertools.product(range(1,5),range(16))),3):
            full+=1
            cs,ms=zip(*keys)
            eligible=all(c<=sum(map(int,format(t,'04b'))) and (t!=15 or c==4) and all(int(l)<=int(s) for l,s in zip(format(m,'04b')[::-1],format(t,'04b'))) for c,m,t in zip(cs,ms,(3,11,15)))
            if eligible:
                active+=1;anchor_two+=int(cs[0]==2);carrier_counts[cs]=carrier_counts.get(cs,0)+1
        self.assertEqual((full,active,anchor_two),(45760,2176,832))
        self.assertEqual(carrier_counts,{(1,1,4):320,(1,2,4):512,(1,3,4):512,(2,2,4):320,(2,3,4):512})
        model=lowering.source.authenticate()
        self.assertTrue(all(not p for p in model['charts'][2]['I'][12]))
        self.assertTrue(all(not r[6] for r in model['charts'][2]['P']))

    def test_each_inactive_outer_owner_literal_zero(self):
        vs=tuple(lowering.owned.VertexLabel(4,o,c,m,t) for o,(c,m,t) in enumerate(((1,12,3),(2,13,11),(4,15,15))))
        lo=lowering.Lower(vs)
        for o,t in enumerate((3,11,15)):
            for c,m in itertools.product(range(1,5),range(16)):
                v=lowering.owned.VertexLabel(4,o,c,m,t)
                eligible=c<=sum(map(int,format(t,'04b'))) and (t!=15 or c==4) and all(int(l)<=int(s) for l,s in zip(format(m,'04b')[::-1],format(t,'04b')))
                self.assertEqual(lo.quotient(v)==lo.g.c(0),not eligible)

    def test_parameterized_source_changes_only(self):
        source=(ROOT/'lower_legal_mask_sector.py').read_text()
        expected=source.replace('def build(masks=(12,13,15)):', 'def build(masks=(12,13,15), carriers=(1,2,4)):').replace('    outer.authenticate_public_sources()',"    if len(carriers)!=3 or any(type(b) is not int or b not in range(1,5) for b in carriers):raise ValueError('primary carriers 1..4 only; star5 not implemented')\n    outer.authenticate_public_sources()",1).replace('((1,masks[0],3),(2,masks[1],11),(4,masks[2],15))','zip(carriers,masks,(3,11,15))').replace("'scope':'one concrete structurally active candidate source-first full-owner tuple, all four E12 terms; not the entire symbolic label sum'", "'scope':'one parameterized source-first primary-carrier full-owner tuple, seed4 row2 standards(3,11,15), all four E12 terms; star5 excluded'")
        self.assertEqual(expected,(ROOT/'lower_primary_carrier_sector.py').read_text())
        with self.assertRaises(ValueError):lowering.build((0,0,0),(1,3,5))
        with self.assertRaises(ValueError):lowering.build((4,0,0),(1,1,4))

    def test_every_saved_separator_independently(self):
        saved=json.loads((ROOT/'primary-carrier-sector-support.json').read_text())
        self.assertEqual(saved['counts'],{'active_tuples':832,'certified_zero':832,'unresolved':0})
        seen=set()
        for r in saved['results']:
            cs=tuple(r['carriers']);ms=tuple(r['legal_masks']);key=(cs,ms)
            self.assertNotIn(key,seen);seen.add(key)
            a=lowering.build(ms,cs)
            self.assertEqual(json.loads(json.dumps(a['owners'])),r['owners'])
            self.assertEqual(hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':')).encode()).hexdigest(),r['dag_sha256'])
            independent.nodes=a['dag'];independent.bound.cache_clear()
            for t in r['multipliers']:
                cert=t['certificate'];self.assertIsNotNone(cert)
                w=tuple(cert['normal']);b=independent.bound(t['root'],w)
                self.assertEqual(list(b),cert['multiplier_bounds'])
                shift=[int(t['kind']=='B' and i==t['derivative']) for i in range(4)]
                M=[(0,0,-2,-2)[i]+sum(5321+2*int(format(ms[o],'04b')[3-i]) for o in t['edge']) for i in range(4)]
                self.assertEqual(M,t['complete_numerator_degree'])
                target=sum(w[i]*((-1,-2,-2,-2)[i]+shift[i]) for i in range(4))
                lo=sum(w[i]*(shift[i] if w[i]>=0 else M[i]) for i in range(4))
                hi=sum(w[i]*(M[i] if w[i]>=0 else shift[i]) for i in range(4))
                self.assertEqual([lo,hi],cert['full_numerator_projection'])
                gap=max(target-b[1]-hi,lo-target+b[0]);self.assertGreater(gap,0);self.assertEqual(gap,cert['gap'])
        expected={(cs,ms) for cs in ((1,1,4),(1,3,4)) for ms in itertools.product(*(scan.active_masks(t) for t in (3,11,15))) if list(zip(cs,ms))==sorted(zip(cs,ms))}
        self.assertEqual(seen,expected)

if __name__=='__main__':unittest.main()
