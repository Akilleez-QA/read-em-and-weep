"""CO-R: independent request grouping and abstract scalar-value reconstruction."""
import json, unittest
from collections import Counter
from pathlib import Path
import preflight as p

class Independent(unittest.TestCase):
    def test_complete_weighted_reconstruction(self):
        source=json.loads((Path(__file__).parent.parent/'detector-selection/weighted-requests.json').read_bytes())
        pairs=Counter()
        expected={}
        def value(i,b,k):return (i+1)**2*97+(b+1)*13+k*k-3*k
        for r in source['requests']:
            i,b=r['scalar_map']['i'],r['scalar_map']['b'];total=0
            for term in r['terms']:
                k=term['output_index']
                # Decode output order independently; do not use producer index helpers.
                digits=[(k//place)%3 for place in (27,9,3,1)]
                exponents=tuple(d-3 for d in digits)
                self.assertEqual(exponents,tuple(term['laurent_exponents']))
                pairs[(i,b,exponents)]+=1
                total+=term['coefficient']*value(i,b,k)
            expected[r['id']]=total
        self.assertEqual((len(expected),sum(pairs.values()),len(pairs)),(32,127,121))
        report=p.build();recovered={k:0 for k in expected}
        for group in report['coefficient_demands']:
            e=group['coordinate'];k=0
            for exponent in e:k=3*k+exponent+3
            for use in group['uses']:
                recovered[use['request_id']]+=use['weight']*value(group['map']['i'],group['map']['b'],k)
        self.assertEqual(recovered,expected)
        self.assertEqual(report['totals']['coordinate_reuses'],6)

    def test_metadata_never_authenticates_resources(self):
        # Even a syntactically convincing dossier is untrusted without actual authorities.
        fake={x:True for x in ('source_cleared','transport_proved','current_ledger','execution_release')}
        fake.update(spent=0,cap=10**100,live=[],commitments=[],cost_upper=0)
        gate=p.build(evidence=fake)['preflight']
        self.assertIs(gate['arithmetic_admission'],False)
        self.assertIs(gate['execution_release'],False)
        for key in ('cost_upper','physical_peak_bytes','occupied_support'):
            self.assertEqual(gate[key],'UNKNOWN')

if __name__=='__main__':unittest.main()
