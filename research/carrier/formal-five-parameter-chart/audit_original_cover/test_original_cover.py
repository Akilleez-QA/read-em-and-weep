"""Small mutation tests of the new checker; no author producer is imported."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('original_cover_audit',ROOT/'check_original_cover.py')
audit=importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

class WitnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=json.loads((ROOT/'certificate.json').read_text())

    def test_exact_all_fifteen_matrix_witnesses(self):
        cert=self.cert
        D=sp.Matrix(cert['D2_hom']);detector=sp.Matrix(cert['detector'])
        self.assertEqual(len(cert['coefficients']),15)
        for label,item in cert['coefficients'].items():
            target=sp.Matrix(item['obstruction_vector']);pre=sp.Matrix(item['preimage_vector'])
            self.assertEqual(D*pre,target,label)
            self.assertEqual((detector.T*target)[0],0,label)

    def test_c_d_raw_terms_not_silently_discarded(self):
        for key in ['c','d','a*c','a*d','b*c','b*d']:
            self.assertTrue(self.cert['c_d_raw_stages'][key]['mixed_BCH'])
            self.assertTrue(self.cert['coefficients'][key]['original_cover_primitive']['mixed_W_primitive'])
        for key in ['c*c','c*d','d*d']:
            self.assertTrue(all(not p for p in self.cert['c_d_raw_stages'][key].values()))

    def test_lambda_inverse_and_each_matrix_witness(self):
        cert=self.cert['lambda_order_three']
        D=sp.Matrix(cert['D3_hom']);inverse=sp.Matrix(cert['D3_inverse'])
        self.assertEqual(D*inverse,sp.eye(9))
        for item in cert['coefficients'].values():
            target=sp.Matrix(item['target_vector']);pre=sp.Matrix(item['D3_inverse_preimage'])
            self.assertEqual(pre,inverse*target)
            self.assertEqual(D*pre,target)
        self.assertTrue(cert['coefficients']['1']['raw_stages']['mixed_BCH'])
        self.assertTrue(cert['coefficients']['a']['raw_stages']['mixed_BCH'])
        self.assertTrue(cert['coefficients']['b']['raw_stages']['mixed_BCH'])

    def test_wrong_relation_rejected(self):
        with self.assertRaisesRegex(ValueError,'nonzero remainder'):
            audit.relation_divide(audit.times(audit.f[0],audit.f[0]))

    def test_wrong_character_rejected(self):
        kappa=audit.mono((-1,0,0,0,0,2,0,0))
        audit.check_grading(kappa,2,'W',0,'good')
        with self.assertRaisesRegex(ValueError,'secondary character'):
            audit.check_grading(audit.shift(kappa,z=1),2,'W',0,'bad')

    def test_nonregular_primitive_rejected(self):
        # The c direction is regular on a mixed single-plane open only because
        # its sole plane exponent is nonnegative. A negative Y exponent outside
        # open 0 must not be accepted by a mere matrix test.
        p=audit.mono((-1,1,-1,0,0,2,0,0))
        with self.assertRaises(ValueError):
            audit.validate_cover({(0,):p},2,'W',2)

    def test_corrupted_preimage_detected(self):
        cert=self.cert
        D=sp.Matrix(cert['D2_hom']);item=cert['coefficients']['a*a']
        pre=sp.Matrix(item['preimage_vector']);pre[0]+=1
        self.assertNotEqual(D*pre,sp.Matrix(item['obstruction_vector']))

if __name__=='__main__':unittest.main()
