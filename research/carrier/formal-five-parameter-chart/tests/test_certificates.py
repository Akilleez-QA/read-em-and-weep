"""Regression checks; run replay.py first to regenerate build outputs."""
from pathlib import Path
import hashlib
import importlib.util
import json
import tempfile
import unittest
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('replay', ROOT/'replay.py')
replay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replay)


def read(name):
    return json.loads((ROOT/'certificates'/name).read_text())


class FormalChartTests(unittest.TestCase):
    def test_integrity(self):
        self.assertGreater(replay.verify_integrity(), 10)

    def test_integrity_rejects_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'sample').write_text('original')
            digest = hashlib.sha256(b'original').hexdigest()
            (root/'SHA256SUMS').write_text(digest+'  sample\n')
            self.assertEqual(replay.verify_integrity(root), 1)
            (root/'sample').write_text('changed')
            with self.assertRaises(ValueError):
                replay.verify_integrity(root)

    def test_regenerated_outputs(self):
        for name in replay.CERTIFICATES:
            path = ROOT/'build'/name
            self.assertTrue(path.is_file(), 'Run python replay.py first.')
            self.assertEqual(json.loads(path.read_text()), read(name))

    def test_four_plus_one_coordinates(self):
        early = read('early_parameters.json')
        self.assertEqual((early['1']['source_dimension'],early['1']['D_rank'],
                          early['1']['kernel_dimension'],early['1']['evaluation_rank']),
                         (22,19,3,1))
        self.assertEqual(early['1']['fixed_beta_kernel_dimension'], 2)
        self.assertEqual(early['2']['kernel_dimension'], 0)
        weights = read('weight_certificate.json')['H1_W_prescribed_monomials']
        self.assertEqual(len(weights['1']), 2)
        self.assertEqual(weights['2'], [[-1,0,0,0]])

    def test_symbolic_quadratic_preimage(self):
        certificate = read('quadratic_certificate.json')
        params = dict(zip(('a','b','c','d'),s.symbols('a b c d')))
        matrix = s.Matrix(certificate['D2_hom']).applyfunc(s.Rational)
        vector = s.Matrix([s.sympify(x,locals=params) for x in certificate['obstruction_vector']])
        preimage = s.Matrix([s.sympify(x,locals=params) for x in certificate['polynomial_preimage']])
        detector = s.Matrix(certificate['left_cokernel_detector']).applyfunc(s.Rational)
        self.assertEqual((matrix*preimage-vector).applyfunc(s.expand), s.zeros(16,1))
        self.assertEqual(detector.T*matrix, s.zeros(1,15))
        self.assertEqual(s.expand((detector.T*vector)[0]), 0)
        for value in vector:
            self.assertLessEqual(s.Poly(value,*params.values()).total_degree(),2)

    def test_constant_higher_right_inverses(self):
        for k,size in [('3',9),('4',5),('5',2),('6',1)]:
            block = read('higher_certificate.json')['blocks'][k]
            matrix = s.Matrix(block['matrix']).applyfunc(s.Rational)
            inverse = s.Matrix(block['right_inverse']).applyfunc(s.Rational)
            self.assertEqual(matrix.shape, (size,size))
            self.assertEqual(matrix.det(), 1)
            self.assertEqual(matrix*inverse, s.eye(size))
            self.assertEqual(inverse*matrix, s.eye(size))

    def test_complete_late_relation_columns(self):
        blocks = read('higher_certificate.json')['blocks']
        for k,columns in [('5',[532,540]),('6',[664])]:
            self.assertEqual(blocks[k]['raw_prescribed_columns'], columns)
            self.assertTrue(blocks[k]['prescribed_C_columns_identically_zero'])
            self.assertTrue(blocks[k]['every_C_row_weight_homogeneous'])

    def test_section_units_are_rational_units(self):
        sections = read('higher_certificate.json')['sections']
        for k,rank,det in [('2',84,'16'),('3',112,'-512'),('4',144,'-16384')]:
            self.assertEqual(sections[k]['exact_rank'], rank)
            self.assertEqual(sections[k]['minor_determinant'], det)
            self.assertTrue(sections[k]['unit_over_Q_parameters'])

    def test_uniform_all_order_bounds(self):
        certificate = read('weight_certificate.json')
        self.assertEqual(len(certificate['W_filtration']), 10)
        self.assertEqual(len(certificate['U_filtration']), 4)
        self.assertEqual(certificate['H2_W_and_H2_U_prescribed_zero_from_order'], 7)
        self.assertEqual(certificate['section_prescribed_zero_from_order'], 5)
        self.assertEqual(certificate['parameter_dependence'], 'none')


if __name__ == '__main__':
    unittest.main()
