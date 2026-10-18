"""Independent enumeration and pinned metadata replay; never evaluate polynomials."""
import itertools,json,unittest
from pathlib import Path
import lower_exceptional_carrier_sector as L

class ExceptionalCarrierTests(unittest.TestCase):
    def test_independent_domain(self):
        # Independently iterate physical labels, applying the canonical comparison.
        counts={'full':0,'prior':0,'remaining':0,'outer_zero':0,'outer_other':0};anchors={}
        for cs in itertools.product(range(6),repeat=3):
            bs=tuple(-1 if c==5 else c for c in cs)
            if list(bs)!=sorted(bs):continue
            for ms in itertools.product(range(16),repeat=3):
                keys=list(zip(bs,ms,(3,11,15)))
                if keys!=sorted(keys):continue
                counts['full']+=1
                if not set(cs)&{0,5}:counts['prior']+=1;continue
                counts['remaining']+=1
                self.assertIn(cs[0],(0,5));anchors[str(cs[0])]=anchors.get(str(cs[0]),0)+1
                zero=False
                for c,m,t in zip(cs,ms,(3,11,15)):
                    infinity={i for i in range(4) if (t>>(3-i))&1}
                    if any((m>>i)&1 for i in set(range(4))-infinity):zero=True
                    if c!=5 and (c>len(infinity) or (len(infinity)==4 and c!=4)):zero=True
                counts['outer_zero' if zero else 'outer_other']+=1
        self.assertEqual(counts,{'full':152096,'prior':45760,'remaining':106336,'outer_zero':101962,'outer_other':4374})
        result=L.partition();self.assertEqual(result['anchor_counts'],anchors)
        saved=json.loads(Path(__file__).with_name('exceptional-carrier-domain-partition.json').read_text())
        self.assertEqual(json.loads(json.dumps(result)),saved)

    def test_denominators_and_transpose_selector(self):
        model=L.base.source.authenticate()
        for c,expected in ((0,{'1,1,1,1':1,'0,0,0,0':-1}),(5,{'2,0,1,1':-1})):
            for name in ('di','dp','dh'):self.assertEqual(dict(model['charts'][c][name]),expected)
            self.assertEqual(model['charts'][c]['pivot'],0)
            # (I transpose(R) P)[12,6] = sum I[12,u] R[w,u] P[w,6].
            # Vanishing right column does not assume any R trace identity.
            for u,w in itertools.product(range(2),repeat=2):self.assertEqual(model['charts'][c]['P'][w][6],[])
            self.assertTrue(any(model['charts'][c]['I'][12])) # discriminates incorrect row-zero proof
        self.assertNotEqual(dict(model['charts'][5]['di']),{'1,0,1,1':-1})
        # Exact exponent addition proves (v1)*(v3*v4)=a, hence v1 unit on D(a).
        self.assertEqual(tuple(x+y for x,y in zip((1,0,0,0),(0,0,1,1))),(1,0,1,1))

    def test_current_ast_all_exceptional_carrier_sectors(self):
        sectors=0
        for cs in itertools.combinations_with_replacement(L.CARRIERS,3):
            if not set(cs)&{0,5}:continue
            sectors+=1
            vs=tuple(L.base.owned.VertexLabel(4,o,c,0,t) for o,(c,t) in enumerate(zip(cs,(3,11,15))))
            lo=L.ExceptionalLower(vs)
            for kind,d in itertools.product(('L','U'),range(2)):
                r=lo.selected_contraction(kind,d)
                self.assertEqual(lo.g.nodes[r[0]],['rational',0,1])
            for method in (lo.edge_inverse,lo.cancel,lo.quotient):
                with self.assertRaises(ValueError):method(None)
        self.assertEqual(sectors,36)

    def test_mask_and_order_guards(self):
        for c in (5,0):
            for mask in range(16):
                vs=tuple(L.base.owned.VertexLabel(4,o,c,mask,t) for o,t in enumerate((3,11,15)))
                lo=L.ExceptionalLower(vs)
                for kind,d in (('L',0),('U',1)):
                    self.assertEqual(lo.g.nodes[lo.selected_contraction(kind,d)[0]],['rational',0,1])
        vs=tuple(L.base.owned.VertexLabel(4,o,c,0,t) for o,(c,t) in enumerate(zip((0,5,4),(3,11,15))))
        with self.assertRaises(ValueError):L.ExceptionalLower(vs)

if __name__=='__main__':unittest.main()
