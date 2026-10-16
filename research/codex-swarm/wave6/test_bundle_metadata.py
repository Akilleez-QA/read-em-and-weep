"""Integration controls over explicit-owner descriptions, never coefficients."""
import json
from pathlib import Path
import unittest
import replay_bundle_metadata as replay


class BundleMetadata(unittest.TestCase):
    def test_canonical_RS_and_J3_metadata_compose(self):
        r=replay.build_receipt()
        self.assertEqual(len(r['explicit_owners']),6)
        self.assertEqual(r['RS']['boundary_sign'],1)
        self.assertEqual(set(r['RS']['source_component_ids']),{'baseline','Fk12','Fk34','E12','E34'})
        self.assertEqual(r['RS']['source_graph_reference_nodes'],4270)
        self.assertEqual(r['JC']['component'],'J3')
        self.assertEqual(r['JC']['face_terms'],120)
        self.assertEqual(r['JC']['source_leaf_bindings'],20)
        self.assertEqual(r['JC']['frame']['tau_power'],-5)
        self.assertEqual((r['JC']['scalar_maps'],r['JC']['weighted_tests']),(20,32))
        for key in ['RS','JC']:
            p=r[key]['profile']
            self.assertEqual(p['aggregate_stored_AST_nodes'],sum(x['nodes']for x in p['stored_AST_arrays']))
            self.assertFalse(p['physical_arithmetic_cost_or_memory_admission'])
        self.assertEqual(r['JC']['producer_profile']['aggregate_stored_AST_nodes'],r['JC']['profile']['aggregate_stored_AST_nodes'])
        self.assertFalse(r['actual_source_coefficients_evaluated'])
        self.assertFalse(r['actual_fibers_enumerated'])
        self.assertFalse(r['execution_release'])

    def test_profile_counts_occurrences_and_canonical_bytes(self):
        shared={'nodes':[1,2]};x={'a':shared,'b':shared,'dag':[1]}
        p=replay.profile(x)
        self.assertEqual(p['aggregate_stored_AST_nodes'],5)
        self.assertEqual(p['canonical_descriptor_bytes'],len(json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()))


if __name__=='__main__':unittest.main()
