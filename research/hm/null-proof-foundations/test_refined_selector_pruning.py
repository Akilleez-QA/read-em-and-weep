import unittest
import prune_refined_selector_paths as p
from dataclasses import replace

class PruningTests(unittest.TestCase):
    def test_exact_counts(self):
        c=p.generate()
        self.assertEqual(c['counts']['raw'],4038)
        self.assertEqual(c['counts']['surviving'],78)
        self.assertEqual(sum(v for k,v in c['counts'].items() if k!='raw'),4038)

    def test_one_per_seed(self):
        c=p.generate()
        self.assertEqual([t['seed'] for t in c['paths']],list(range(78)))

    def test_no_cross_owner_zero(self):
        for kinds in [('H','H'),('H','E'),('E','H'),('H','I'),('P','H')]:
            self.assertFalse(p.zero_word(((kinds[0],0),(kinds[1],1))))
            self.assertTrue(p.zero_word(((kinds[0],0),(kinds[1],0))))

    def test_prefix_weight_retained(self):
        for t in p.generate()['paths']:
            self.assertTrue(set(t['deleted_prefix_owners'])<=set(t['weighted_owners']))
            self.assertFalse(set(t['deleted_prefix_owners'])&set(t['tail']))

    def test_lambda4_signs(self):
        seeds=p.spec.seed_records()
        for t in p.generate()['paths']:
            if t['row']>=7:
                self.assertEqual(t['coefficient'],seeds[t['seed']]['orientation'])

    def test_lambda3_branches(self):
        for t in p.generate()['paths']:
            if t['row'] in (3,4):
                self.assertEqual(t['left'],(('H',0),('I',1)))
                self.assertEqual(t['right'],(('P',1),))
            if t['row'] in (5,6):
                self.assertEqual(t['left'],(('E',0),('I',1)))
                self.assertEqual(t['right'],(('P',1),('H',0)))

    def test_lambda4_branches(self):
        for t in p.generate()['paths']:
            if t['row']==7:
                self.assertEqual(t['left'],(('H',0),('E',1),('I',2)))
                self.assertEqual(t['right'],(('P',2),('H',1)))
            if t['row']==8:
                self.assertEqual(t['left'],(('E',0),('E',1),('I',2)))
                self.assertEqual(t['right'],(('P',2),('H',1),('H',0)))

    def test_equal_carrier_different_masks_rejected(self):
        self.assertFalse(p.prefix_allowed(1,((1,0,0),(1,1,1),(2,0,2),(3,0,3))))
        self.assertFalse(p.prefix_allowed(2,((0,0,0),(1,0,1),(1,1,2),(2,0,3),(3,0,4))))

    def test_tail_carriers_can_repeat(self):
        self.assertTrue(p.prefix_allowed(0,((1,0,0),(1,0,1),(1,0,2))))
        self.assertTrue(p.prefix_allowed(1,((0,0,0),(1,0,1),(1,0,2),(1,0,3))))
        self.assertTrue(p.prefix_allowed(2,((0,0,0),(1,0,1),(2,0,2),(2,0,3),(2,0,4))))

    def test_frame_and_order_guard(self):
        with self.assertRaises(p.spec.ContractError):
            p.prefix_allowed(0,((1,0,0),(1,0,1),(1,0,2)),frame='physical-unconverted')
        with self.assertRaises(p.spec.ContractError):
            p.prefix_allowed(0,((1,0,2),(1,0,1),(1,0,0)))

    def test_prefix_mask_partition_rewrite(self):
        for depth in (0,1,2):
            result=p.sum_prefix_masks(depth)
            self.assertEqual(result['raw_mask_combinations_removed'],16**depth)
            self.assertEqual(result['carrier_weights_retained'],tuple(range(depth)))
            self.assertEqual(result['standard_owners_retained'],tuple(range(depth)))
            self.assertFalse(result['tail_masks_summed'])
            self.assertFalse(result['inner_T_masks_summed'])

    def test_mask_merger_preconditions(self):
        for args in ({'strict_carriers':False},{'common_frame':False},{'tail_masks':True}):
            with self.subTest(args=args),self.assertRaises(p.spec.ContractError):
                p.sum_prefix_masks(1,**args)
        with self.assertRaises(p.spec.ContractError):p.abstract_two_chart_sum((0,),'w0+w1=1')
        with self.assertRaises(p.spec.ContractError):p.abstract_two_chart_sum((0,1),'unknown')

    def test_mutations_rejected(self):
        for mutation in ('sign','prefix','tail','fourtail'):
            c=p.generate()
            if mutation=='sign':c['paths'][0]['coefficient']*=-1
            if mutation=='prefix':c['paths'][-1]['weighted_owners']=(2,3,4)
            if mutation=='tail':c['paths'][-1]['tail']=(0,1,2)
            if mutation=='fourtail':c['old_four_tail_assumed']=True
            with self.subTest(mutation=mutation),self.assertRaises(p.spec.ContractError):p.encode(c)

    def test_size_and_determinism(self):
        a=p.encode(p.generate())
        self.assertLessEqual(len(a),p.MAX_BYTES)
        self.assertEqual(a,p.encode(p.generate()))

if __name__=='__main__':unittest.main()
