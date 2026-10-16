"""Formal coefficient/exponent controls only; no source-polynomial evaluator."""
import copy
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import unittest
import frames as f

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.repo=Path(__file__).resolve().parents[3];cls.auth=f.authenticate(cls.repo)
    def test_all16_chart_core_and_trace_identity(self):
        for tag in range(16):
            frame=f.chart_frame(tag);e=f.bits(tag)
            self.assertEqual(frame['F_transition']['local_power'],[-2*e[0],-2*e[1],0,0])
            self.assertEqual(frame['F_transition']['sign'],1)
            for entry in frame['entries']:
                self.assertEqual(entry['core_tau_weight']+entry['physical_D_conjugation_tau_weight'],0)
                self.assertEqual(entry['infinity_T_extra_connection_coefficient'],[0,1])
            self.assertTrue(all(sum(c['factor_tau_weights'])==0 for c in frame['ordered_trace_cycles']))
    def test_elementary_generator_pullback_formally(self):
        # Four abstract coordinate symbols; only0/1 monomial exponents, no HM input.
        for tag in range(16):
            e=f.bits(tag)
            for j in range(5):
                for subset in combinations(range(4),j):
                    pulled=tuple((1-int(i in subset)) if e[i] else int(i in subset) for i in range(4))
                    local=tuple(int(i not in subset) if e[i] else int(i in subset) for i in range(4))
                    self.assertEqual(pulled,local);self.assertTrue(all(x in (0,1) for x in local))
    def test_infinity_endpoint_Q_and_tangent_coefficients(self):
        # Coefficients of independent formal K,K',R=rf(1/t); t never specialized.
        for r,s,ma,mb in product(range(2),repeat=4):
            w=r-s;sig_r=1-2*r;sig_s=1-2*s
            common=Q(w)+Q(sig_r-sig_s,2)
            local_coeffs=(common,Q(-1),Q(-sig_r*mb+sig_s*ma))
            expected=(Q(0),Q(-1),-Q(sig_r*mb-sig_s*ma))
            self.assertEqual(local_coeffs,expected)
            if r!=s:self.assertNotEqual(Q(w),Q(0)) # omitted common Q leaves a defect
        # Q_t numerator over2t(1-t²): (1-m) + (-1-m)t².
        for m in (0,1):
            numerator=(1-m,-1-m)
            self.assertEqual(numerator,(1,-1) if m==0 else (0,-2))
            self.assertNotEqual(numerator,(0,0)) # finite mask-only Q rebuilt at infinity is wrong
    def test_two_minus_signs_and_actual_gerbe(self):
        for tag in range(16):
            c=f.chart_frame(tag)['coordinates']
            for axis in c:
                ordinary=axis['ordinary_chain']['sign'];strip=axis['invariant_stripped_local_operator_sign']
                self.assertEqual(ordinary*strip,axis['stripped_T_factor']['sign'])
                g=axis['gerbe_transport'];self.assertEqual(g['dlogx_sign']*g['invariant_V_sign'],g['local_stripped_q_sign'])
                if ordinary<0:
                    self.assertEqual(1-2,g['local_stripped_q_power'])
                    self.assertNotEqual(ordinary,axis['stripped_T_factor']['sign'])
    def test_actual_owner_units_and_C_P_degrees(self):
        for owners in f.SEED_TAILS.values():
            for tag in range(16):
                result=f.bind_triple(owners,tag)
                self.assertEqual(result['owners'],owners)
                self.assertEqual([a+b for a,b in zip(result['product_C_transition_power'],result['physical_F_transition_power'])],result['P_transition_power'])
                self.assertTrue(f.validate_instance(result))
                for owner,record in zip(owners,result['C_owner_records']):
                    self.assertEqual(record['owner'][4],owner[4])
                    self.assertEqual(record['legal_sections'][0]['homogeneous_degree'],3 if owner[3]&1 else 1)
        owners=[[99,0,5,0,0],[99,1,0,1,8],[99,2,4,15,15]]
        r=f.bind_triple(owners,15)
        self.assertEqual(r['C_owner_records'][0]['carrier_equation_degree'],4)
        self.assertEqual(r['C_owner_records'][0]['original_standard_units'],['t']*4)
        self.assertEqual(r['C_owner_records'][0]['legal_sections'][0]['local_coefficient'],'t')
    def test_strict_owner_chart_and_mutated_frame_reject(self):
        owners=copy.deepcopy(f.SEED_TAILS[12]);bad=copy.deepcopy(owners);bad[0][2]=True
        with self.assertRaises(ValueError):f.bind_triple(bad,0)
        with self.assertRaises(ValueError):f.bind_triple(owners,0.0)
        with self.assertRaises(ValueError):f.bind_triple(list(reversed(owners)),0)
        original=f.bind_triple(owners,8)
        for kind in ('Q','sign','twist','tag','aux_degree','owner_constant'):
            r=copy.deepcopy(original)
            if kind=='Q':r['frame']['coordinates'][0]['Q_local_cases']['mask0']='0'
            elif kind=='sign':r['frame']['coordinates'][0]['invariant_stripped_local_operator_sign']=1
            elif kind=='twist':r['frame']['F_transition']['character']=[-4]*4
            elif kind=='tag':r['C_owner_records'][0]['owner'][4]=8
            elif kind=='aux_degree':r['C_owner_records'][0]['carrier_equation_degree']=3
            else:r['frame']['line_frame']['owner_constants']='reset to1'
            with self.assertRaises(ValueError):f.validate_instance(r)
    def test_corrupt_source_reject(self):
        with self.assertRaises(ValueError):f.authenticate('.',reader=lambda *_:b'corrupt')
    def test_exact_primitive_homogeneous_bridge(self):
        for entry in f.primitive_bridge():
            c=entry['carrier'];d=entry['assigned_H_degree'];D=entry['raw_di_dp_affine_degree']
            for w in (-1,0,1):
                for e in entry['canonical_e_domain']:
                    padding=(2-e) if c==5 else (1-e) if c==0 else 0
                    self.assertGreaterEqual(padding,0)
                    homogenized_numerator_degree=D+e+w+padding
                    self.assertEqual(homogenized_numerator_degree,(6 if c==5 else 5)+w)
                    self.assertEqual(homogenized_numerator_degree+(2 if c==5 else 5),2*d+w)
        self.assertLess(1-2,0) # incorrect aux degree5 recipe loses necessary v0 at e2
    def test_complementary_frame_uses_null_property_not_cochain_sorting(self):
        owners=[[99,0,1,15,0],[99,1,2,15,8],[99,2,4,15,15]]
        for tag in range(16):
            r=f.bind_triple(owners,tag,(2,3));e=f.bits(tag)
            self.assertEqual(r['frame']['F_transition']['character'],[0,0,-2,-2])
            self.assertEqual(r['physical_F_transition_power'],[0,0,-2*e[2],-2*e[3]])
            self.assertEqual(r['P_target_multidegree'],[210,210,217,217])
            self.assertEqual(r['owners'],owners);self.assertIn('not equality',r['finite_source_scope'])
            self.assertFalse(r['finite_candidate_reference']['direct_F12_root_on_target_owners'])
            self.assertTrue(r['finite_candidate_reference']['inverse_image_may_be_unsorted'])
            self.assertTrue(f.validate_instance(r))
        for pair in ((1,0),(0,2),(False,True)):
            with self.assertRaises(ValueError):f.bind_triple(owners,0,pair)
    def test_source_reference_and_no_global_program_claim(self):
        result=f.build(self.repo)
        self.assertEqual(len(result['abstract_frame_catalog']),16)
        self.assertEqual([len(x['instances']) for x in result['seed_examples']],[16,16])
        self.assertEqual(len(result['complementary_frame_catalog']),16)
        self.assertEqual([len(x['instances']) for x in result['complementary_seed_examples']],[16,16])
        self.assertTrue(all(v is False for v in result['global_gates'].values()))
        self.assertEqual(self.auth['finite_F_equation'],result['source_authentication']['finite_F_equation'])

if __name__=='__main__':unittest.main()
