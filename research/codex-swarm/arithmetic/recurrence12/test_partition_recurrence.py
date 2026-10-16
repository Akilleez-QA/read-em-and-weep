import itertools
import math
import unittest
import partition_recurrence as plan
from synthetic_affine_dp import bounded_affine_convolution as dp


class SyntheticControls(unittest.TestCase):
    def test_dp_against_independent_multinomial_enumerator(self):
        for total in range(1,7):
            for d in range(1,4):
                for threshold in range(1,min(3,total)+1):
                    for chosen in range(d):
                        bounds=[(0, min(total,threshold-1)) if i<chosen else (threshold,total) if i==chosen else (0,total) for i in range(d)]
                        columns=[(i-1,2-i) for i in range(d)]
                        offsets=[(-i,i%2) for i in range(d)]
                        kernels=[{n:{(0,0):1,(1,-1):(-1)**(i+n)} for n in range(lo,hi+1)} for i,(lo,hi) in enumerate(bounds)]
                        got=dp(synthetic=True,total=total,bounds=bounds,affine_columns=columns,offsets=offsets,kernels=kernels)
                        want={}
                        for ns in itertools.product(*(range(lo,hi+1) for lo,hi in bounds)):
                            if sum(ns)!=total:continue
                            multinomial=math.factorial(total)//math.prod(math.factorial(n) for n in ns)
                            for terms in itertools.product(*(kernels[i][n].items() for i,n in enumerate(ns))):
                                target=tuple(sum(ns[i]*columns[i][h]+offsets[i][h]+terms[i][0][h] for i in range(d)) for h in range(2))
                                c=multinomial*math.prod(t[1] for t in terms)
                                want[target]=want.get(target,0)+c
                        self.assertEqual(got,{k:v for k,v in want.items() if v})

    def test_empty_and_impossible_boundary(self):
        args=dict(synthetic=True,total=0,bounds=[(0,0)],affine_columns=[(1,)],offsets=[(0,)],kernels=[{0:{(0,):1}}])
        self.assertEqual(dp(**args),{(0,):1})
        args.update(total=1,bounds=[(0,0)])
        self.assertEqual(dp(**args),{})
        args.update(synthetic=False)
        with self.assertRaises(ValueError):dp(**args)


class SymbolicPlanControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.p=plan.build()

    def test_owner_binding_and_no_admission(self):
        self.assertEqual([tuple(w['owner']) for w in self.p['weights']],list(plan.OWNERS))
        self.assertEqual(self.p['selector_binding']['tail_owners'],list(plan.OWNERS[1:]))
        self.assertEqual(self.p['selector_binding']['coefficient'],2)
        self.assertEqual(self.p['sorting_orientation'],1)
        self.assertFalse(any(self.p['gate'].values()))
        for w in self.p['weights']:
            self.assertIsNone(w['source_denominator_orders'])
            self.assertFalse(w['source_denominator_orders_derived'])

    def test_unexpanded_compositions_and_shifts(self):
        weights=self.p['weights']
        self.assertEqual([len(w['composition']) for w in weights],[2,1,1,1])
        self.assertEqual([w['composition'][0]['total'] for w in weights],[1069,1603,2137,2671])
        self.assertEqual([w['scalar_clearing_pullback_shift'] for w in weights],
                         [[0,0,0,-303],[-357,0,0,-357],[-357,-357,0,-357],[-357]*4])
        for w in weights:
            sums=[n for n in w['dag'] if n[0]=='bounded_composition_sum']
            self.assertEqual(len(sums),len(w['composition']))
            for node in sums:
                self.assertEqual(node[1]['threshold'],535)
                self.assertEqual(node[1]['earlier_upper'],534)
                self.assertEqual(len(node[2]['powers']),2*node[1]['dimension'])
                self.assertTrue(all(c['actual_polynomial_term_count'] is None for c in w['composition']))

    def test_a01_request_is_exact_and_fail_closed(self):
        request=dict(self.p['a01_request_evidence']['request'])
        self.assertTrue(plan.validate_a01_request(request))
        request['seed']=4
        with self.assertRaises(ValueError):plan.validate_a01_request(request)
        request['seed']=12;request['extra']=False
        with self.assertRaises(ValueError):plan.validate_a01_request(request)
        request.pop('extra');request['orientation']=True
        with self.assertRaises(ValueError):plan.validate_a01_request(request)

    def test_full_ledger_rejections(self):
        records=[{'owner':list(o),'carrier':1,'legal':[int((o[3]>>i)&1) for i in range(4)],
                  'standard':[int((o[4]>>(3-i))&1) for i in range(4)]} for o in plan.OWNERS]
        self.assertFalse(any(plan.declared_clearing_ledger(records)['gate'].values()))
        records[0]['carrier']=55
        with self.assertRaises(ValueError):plan.declared_clearing_ledger(records)
        records[0]['carrier']=1;records[0]['extra']='D'
        with self.assertRaises(ValueError):plan.declared_clearing_ledger(records)
        records[0].pop('extra');records[0]['legal'][0]=1
        with self.assertRaises(ValueError):plan.declared_clearing_ledger(records)
        with self.assertRaises(ValueError):plan.declared_clearing_ledger(records[1:])


if __name__=='__main__':unittest.main()
