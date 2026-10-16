"""Bounded JSON binding/hash/owner tests only; no source-value oracle."""
import copy
from pathlib import Path
import unittest
import bind_requests as b

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.graph,cls.pins=b.authenticate(Path(__file__).resolve().parents[4])
    def test_exact_owner_prefix_frame_branch_binding(self):
        for sid,coeff in ((12,2),(30,1)):
            result=b.bind(b.request(sid),self.graph,self.pins)
            self.assertEqual(result['weighted_owners'],list(range(len(b.OWNERS[sid]))))
            self.assertEqual(result['deleted_prefix_owners'],[0] if sid==12 else [0,1])
            self.assertEqual([x['effective_scalar_coefficient'] for x in result['branches']],[[coeff,2],[-coeff,2],[coeff,2],[-coeff,2]])
            self.assertEqual([x['source_branch']['current_source_binding']['owners'] for x in result['branches']],[b.OWNERS[sid][-3:]]*4)
            self.assertTrue(all(v is False for v in result['gates'].values()))
            self.assertTrue(b.validate_result(b.request(sid),result,self.graph,self.pins))
            self.assertTrue(all(x['pending_null_lemma']['proof_reference'] is None for x in result['branches']))
    def test_omission_order_frame_rejection(self):
        base=b.request(12);bad=[]
        for key in base:
            x=copy.deepcopy(base);del x[key];bad.append(x)
        for key,value in (('frame','local-infinity'),('orientation',-1),('orientation',True),('prefix_mask_scope','prefix-summed'),('channel','E12(T34F34)'),('carrier_map',{})):
            x=copy.deepcopy(base);x[key]=value;bad.append(x)
        x=copy.deepcopy(base);x['owners'].reverse();bad.append(x)
        x=copy.deepcopy(base);x['owners'][0][2]=0;bad.append(x)
        x=copy.deepcopy(base);x['owners'][1][3]=9.0;bad.append(x)
        for x in bad:
            with self.assertRaises(ValueError):b.bind(x,self.graph,self.pins)
    def test_source_omission_and_frame_mutation_rejection(self):
        for name in ('selector_source_binding','outer_weight_source_bindings'):
            g=copy.deepcopy(self.graph);del g['seeds'][12][name]
            with self.assertRaises(ValueError):b.bind(b.request(12),g,self.pins)
        g=copy.deepcopy(self.graph);g['seeds'][12]['derivative_terms'][4]['current_source_binding']['moving_frame_log_terms_retained']=False
        with self.assertRaises(ValueError):b.bind(b.request(12),g,self.pins)
        pins=copy.deepcopy(self.pins);del pins['files']['hm-pinned-model.json']
        with self.assertRaises(ValueError):b.bind(b.request(12),self.graph,pins)
    def test_corrupt_and_missing_bytes(self):
        for raw in (b'',b'corrupt'):
            with self.assertRaises(ValueError):b.authenticate('.',reader=lambda _:raw)
    def test_result_cannot_release_gates(self):
        r=b.bind(b.request(30),self.graph,self.pins);r['gates']['execution_release']=True
        with self.assertRaises(ValueError):b.validate_result(b.request(30),r,self.graph,self.pins)
    def test_tracefree_semantics_not_only_hash(self):
        result=b.bind(b.request(12),self.graph,self.pins)
        for mutate in ('omit','raw','wrong_input','wrong_frame','claim_equivalence'):
            r=copy.deepcopy(result)
            if mutate=='omit':del r['branches'][0]['demand_current']
            elif mutate=='raw':r['branches'][0]['demand_current']['operator']='identity'
            elif mutate=='wrong_input':r['branches'][0]['demand_current']['input_ast']={}
            elif mutate=='wrong_frame':r['branches'][0]['demand_current']['frame']='local-infinity'
            else:r['gates']['raw_v5_projection_equivalence']=True
            with self.assertRaises(ValueError):b.validate_semantics(r)
    def test_projection_and_fixed_weight_toy_countercontrols(self):
        # Abstract matrices/scalars only; no HM values or imported source evaluator.
        from fractions import Fraction as Q
        raw=((Q(3),Q(0)),(Q(0),Q(1)))
        half_trace=(raw[0][0]+raw[1][1])/2
        tf=tuple(tuple(raw[i][j]-(half_trace if i==j else 0) for j in range(2)) for i in range(2))
        # W=diag(1,0): raw and projected contractions differ without a proof.
        self.assertEqual(raw[0][0],3);self.assertEqual(tf[0][0],1)
        self.assertNotEqual(raw[0][0],tf[0][0])
        # A two-term partition sums to1; neither fixed contribution is1.
        weights=(Q(2,5),Q(3,5))
        self.assertEqual(sum(weights),1);self.assertNotEqual(weights[0],1)
    def test_fixed_mask_semantics_not_only_hash(self):
        for sid in (12,30):
            result=b.bind(b.request(sid),self.graph,self.pins)
            self.assertNotIn('prefix_mask_merger',result['selector_source_binding'])
            self.assertIn('prefix_mask_merger',result['source_selector_provenance']['source_record'])
            for mutate in ('replace_by_one','remove_factor','apply_source','collapse_policy','leak_merger'):
                r=copy.deepcopy(result)
                if mutate=='replace_by_one':r['fixed_mask_legal_weights'][0]['replace_by_one']=True
                elif mutate=='remove_factor':r['fixed_mask_legal_weights'].pop(0)
                elif mutate=='apply_source':r['source_selector_provenance']['applied_to_fixed_mask_request']=True
                elif mutate=='collapse_policy':r['selector_source_binding']['prefix_mask_policy']['removed_combinations']=16 if sid==12 else 256
                else:r['selector_source_binding']['prefix_mask_merger']=copy.deepcopy(r['source_selector_provenance']['source_record']['prefix_mask_merger'])
                with self.assertRaises(ValueError):b.validate_semantics(r)

if __name__=='__main__':unittest.main()
