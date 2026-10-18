"""Whole-artifact and provenance checks; no source polynomial arithmetic."""
import hashlib,json,unittest
from pathlib import Path
import compile_actual_scalar_differential_kernel as compiler
import physical_current_source_binding as currents
import resolution_selector_source_binding as selectors
import traverse_selected_scalar_demand as demand
ROOT=Path(__file__).resolve().parent
class PublicTests(unittest.TestCase):
    def test_exact_public_rebuild(self):
        obj=compiler.build()
        self.assertEqual(json.loads(json.dumps(obj)),json.loads((ROOT/'actual-scalar-differential-kernel.json').read_text()))
        self.assertEqual(len(demand.build()['nodes']),199)
        self.assertEqual(obj['seed_count'],78)
        self.assertEqual(obj['edge_branch_count'],624)
        self.assertEqual(len({b['id'] for s in obj['seeds'] for b in s['derivative_terms']}),624)
        self.assertEqual(obj['unresolved_regularization_Laurent_groups'],78)
        self.assertFalse(obj['actual_factorization_accepted'])
        self.assertFalse(obj['actual_detector_authenticated'])
        self.assertFalse(obj['execution_release'])
        self.assertFalse(obj['physical_source_evaluated'])
    def test_public_provenance(self):
        self.assertEqual(hashlib.sha256((ROOT/'hm-pinned-source-formulas.js').read_bytes()).hexdigest(),currents.SOURCE_SHA256)
        for name,digest in selectors.PROOFS.items():
            self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),digest)
    def test_no_external_runtime_imports(self):
        # Every local project dependency is shipped in this standalone directory.
        import ast
        allowed={'argparse','hashlib','itertools','json','sys','dataclasses','pathlib','collections','fractions'}
        for name in ('compile_actual_scalar_differential_kernel','compile_refined_detector_metadata','prune_refined_selector_paths','owned_scalar_denominator_binding','physical_current_source_binding','resolution_selector_source_binding','outer_partition_source_binding','traverse_selected_scalar_demand','check_rectangular_jet_factorization'):
            for node in ast.walk(ast.parse((ROOT/(name+'.py')).read_text())):
                mods=[a.name for a in node.names] if isinstance(node,ast.Import) else [node.module] if isinstance(node,ast.ImportFrom) else []
                for mod in mods:self.assertTrue(mod in allowed or (ROOT/(mod+'.py')).is_file(),mod)
if __name__=='__main__':unittest.main(verbosity=2)
