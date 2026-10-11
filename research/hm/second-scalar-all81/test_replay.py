import copy
import json
import tempfile
import unittest
from pathlib import Path
import replay as r

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=r.load(r.HERE/'quotients.json');cls.expected=r.load(r.HERE/'expected.json')
        cls.duplicates=r.load(r.HERE/'duplicate-binding.json')

    def reject(self,change):
        d,e=copy.deepcopy(self.data),copy.deepcopy(self.expected);change(d,e)
        with self.assertRaises((ValueError,KeyError,TypeError)):r.verify(d,e)

    def test_complete_replay(self):
        result=r.replay();self.assertEqual(result['coordinates'],[['0','1']]*81)
        self.assertEqual(result['statistics'],r.STATS)
        self.assertEqual(result['duplicate_array_checks']['mapped_rows'],1086)

    def test_kernel_independent_positive_power(self):
        g={(0,0):1,(0,1):1,(1,0):1,(1,1):3,(1,2):1,(2,1):1,(2,2):1}
        def mul(a,b):
            out={}
            for (i,j),c in a.items():
                for (k,l),d in b.items():
                    if i+k<9 and j+l<23:out[i+k,j+l]=out.get((i+k,j+l),0)+c*d
            return {k:v for k,v in out.items()if v}
        power={(0,0):1}
        for _ in range(70):power=mul(power,g)
        self.assertEqual(mul(power,r.kernel()),{(0,0):1})

    def test_missing_quotient(self):self.reject(lambda d,e:d['quotients'].pop())
    def test_duplicate_quotient(self):self.reject(lambda d,e:d['quotients'].__setitem__(1,copy.deepcopy(d['quotients'][0])))
    def test_missing_target(self):self.reject(lambda d,e:e['targets'].pop())
    def test_missing_orientation(self):self.reject(lambda d,e:e['targets'][0]['edges'].pop())
    def test_wrong_sign(self):self.reject(lambda d,e:e['targets'][0]['edges'][0].update(sign=-1))
    def test_boolean_sign(self):self.reject(lambda d,e:e['targets'][0]['edges'][0].update(sign=True))
    def test_wrong_row_digest(self):self.reject(lambda d,e:e['targets'][0]['edges'][0].update(rows_sha256='0'*64))
    def test_wrong_total(self):self.reject(lambda d,e:e['targets'][0].update(value=['1','1']))
    def test_unreduced_zero(self):self.reject(lambda d,e:e['targets'][0].update(value=['0','2']))
    def test_lost_grading(self):self.reject(lambda d,e:d['quotients'][0].update(homogeneous_degrees_separated=False))
    def test_old_window(self):self.reject(lambda d,e:d['quotients'][0].update(shape=[7,36,21]))
    def test_wrong_empty_boundary(self):self.reject(lambda d,e:e['targets'][0].update(empty_boundary=True))
    def test_wrong_target(self):self.reject(lambda d,e:e['targets'][0].update(m=[2,2,2,1]))
    def test_wrong_counts(self):self.reject(lambda d,e:e['statistics'].update(rows=114047))
    def test_full_obstruction_claim(self):self.reject(lambda d,e:e.update(full_obstruction_computed=True))
    def test_source_regeneration_claim(self):self.reject(lambda d,e:e.update(source_regeneration_reproduced=True))
    def test_coefficient_change_rehashed(self):
        def change(d,e):
            q=d['quotients'][0];row=next(row for row in q['coefficients'] if row[1]==41);row[3]=str(int(row[3])+1)
            q['array_sha256']=r.digest(q['coefficients'])
        self.reject(change)
    def test_duplicate_json_keys(self):
        with self.assertRaises(ValueError):json.loads('{"x":1,"x":2}',object_pairs_hook=r.unique)
    def test_source_symmetry_overclaim(self):
        d=copy.deepcopy(self.duplicates);d['sourceSymmetryProved']=True
        with self.assertRaises(ValueError):r.verify_duplicates(self.data,d)
    def test_duplicate_binding_reuse(self):
        d=copy.deepcopy(self.data);qs={''.join(map(str,q['roles'])):q for q in d['quotients']}
        qs['2301']['checkpoint_sha256']=qs['0123']['checkpoint_sha256']
        with self.assertRaises(ValueError):r.verify_duplicates(d,self.duplicates)
    def test_fixed_target_is_not_mapped_target(self):
        d=copy.deepcopy(self.duplicates);d['duplicatePairs'][0]['permutedTarget']=[2,2,2,0]
        with self.assertRaises(ValueError):r.verify_duplicates(self.data,d)
    def test_integrity(self):
        with tempfile.TemporaryDirectory()as directory:
            for f in r.HERE.iterdir():
                if f.is_file():(Path(directory)/f.name).write_bytes(f.read_bytes())
            with(Path(directory)/'expected.json').open('a')as f:f.write(' ')
            with self.assertRaises(ValueError):r.verify_manifest(directory)

if __name__=='__main__':unittest.main()
