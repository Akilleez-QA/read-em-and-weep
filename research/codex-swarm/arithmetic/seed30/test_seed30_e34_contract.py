"""Integer/Boolean metadata controls only; no physical source arithmetic."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest
import seed30_e34_contract as contract


class ContractControls(unittest.TestCase):
    def test_request_rejection(self):
        bad = []
        for key, value in [('carrier_map', {}), ('execution_release', True),
                           ('seed', 4), ('channel', 'E12(T34F34)')]:
            request = copy.deepcopy(contract.EXPECTED)
            request[key] = value
            bad.append(request)
        for value in (False, 0.0, -1, None):
            request = copy.deepcopy(contract.EXPECTED)
            request['owners'][0][2] = value
            bad.append(request)
        request = copy.deepcopy(contract.EXPECTED)
        request['owners'][1] = request['owners'][0]
        bad.append(request)
        for request in bad:
            with self.assertRaises(ValueError):
                contract.build(request)

    def test_metadata_emission(self):
        program = str(Path(contract.__file__).resolve())
        normal = subprocess.check_output([sys.executable, '-B', program])
        optimized = subprocess.check_output([sys.executable, '-B', '-O', program])
        self.assertEqual(normal, optimized)
        self.assertLess(len(normal), 1024*1024)
        result = json.loads(normal)
        self.assertEqual(len(result['owner_ledger']), 5)
        for term in result['terms']:
            leaf = term['scalar_leaf']
            self.assertEqual(leaf['inserted_label_domain']['legal_mask'], list(range(16)))
            self.assertEqual(leaf['inserted_label_domain']['standard_tag'], list(range(16)))
            self.assertIs(leaf['inserted_label_domain_is_enclosure'], True)
        self.assertEqual(result['terminal']['effective_word_coefficient'], 1)
        self.assertEqual([(t['coefficient'], t['scalar_edge'],
                           t['derivative_coordinate'], t['current_kind'],
                           t['current_coordinate']) for t in result['terms']],
                         [([1,2],[3,4],2,'L',3), ([-1,2],[3,4],3,'L',2),
                          ([1,2],[2,3],3,'U',2), ([-1,2],[2,3],2,'U',3)])
        inventory = result['selector']['block_occurrences']
        counts = {}
        for item in inventory:
            key = (item['owner'][1], item['denominator_reference'])
            counts[key] = counts.get(key, 0) + item['multiplicity']
        self.assertEqual(counts, {(0,'dh'):1, (1,'di'):1, (1,'dp'):1,
                                  (1,'dh'):1, (2,'di'):1, (2,'dp'):1})
        self.assertEqual(result['review_status'], 'pending')
        self.assertEqual(len(result['admission_failures']), 5)
        for key in ('actual_source_admitted', 'source_pole_domain_proved',
                    'Laurent_admitted', 'execution_release',
                    'physical_polynomial_evaluation', 'physical_polynomial_expansion',
                    'actual_factorization_accepted', 'arithmetic_cost_certificate'):
            self.assertIs(result[key], False)


if __name__ == '__main__':
    unittest.main()
