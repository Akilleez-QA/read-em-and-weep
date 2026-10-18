#!/usr/bin/env python3
"""Independent adversarial contract checks, using metadata only."""
import sys
if not __debug__:
    print('ERROR: independent audit requires assertions enabled',file=sys.stderr)
    raise SystemExit(2)
import copy
import json
import subprocess
import unittest
from pathlib import Path
from dataclasses import replace
import compile_refined_detector_metadata as m

class IndependentContractAudit(unittest.TestCase):
    def test_canonical_seed_and_status_contract(self):
        c=m.build_certificate()
        self.assertEqual(c['status'],'finite_metadata_specification_only')
        for field in ('execution_release','physical_source_evaluated','complete_arithmetic_contract'):
            self.assertIs(c[field],False)
        self.assertEqual(len(c['seeds']),78)
        self.assertEqual([sum(s['lift_depth']==d for s in c['seeds']) for d in range(3)],[6,24,48])
        self.assertEqual(c['raw_kernel_path_bound_before_outer_labels'],6+24*2*4+48*2*5*2*4)
        self.assertEqual(len(c['unresolved_leaves']),8)

    def test_serialization_rejects_nested_mutations(self):
        cases={
            'wrong_outer_partition':lambda c:c['partitions'].__setitem__('outer',m.INNER),
            'wrong_inner_partition':lambda c:c['partitions'].__setitem__('inner',m.OUTER),
            'corrupt_seed_sign':lambda c:c['seeds'][0].__setitem__('coefficient',99),
            'duplicate_all_seeds':lambda c:c.__setitem__('seeds',[c['seeds'][0]]*78),
            'dropped_prefix_kernel':lambda c:c['owner_control'].__setitem__('kernel',[]),
            'dropped_prefix_weight':lambda c:c['owner_control'].__setitem__('weighted',['o2','o3','o4']),
            'readiness_status_string':lambda c:c.__setitem__('status','execution_ready_resource_pass'),
            'dropped_unresolved_leaves':lambda c:c.__setitem__('unresolved_leaves',[]),
            'altered_E_sign':lambda c:c['node_equations']['E_adjoint'][0].__setitem__(3,-1),
            'altered_outer_domain':lambda c:c['derivative_domain_control'].__setitem__('carrier_cap',14),
        }
        for name,change in cases.items():
            c=m.build_certificate();change(c)
            with self.subTest(case=name),self.assertRaises(m.ContractError):m.encode_certificate(c)

    def test_domain_rejects_forged_preparation(self):
        s=m.differentiate_regularized(m.cancel_inserted(m.raw_inner(),'N14-owned-polynomial-quotients'))
        cases={
            'missing_witness':replace(s,cancellation_witness=''),
            'wrong_partition':replace(s,partition=m.OUTER),
            'wrong_derivative_count':replace(s,derivative_count=0),
            'rational_pending':replace(s,phase='rational_pending'),
            'uncanceled_inserted':replace(s,inserted_carrier=1),
            'excess_carrier':replace(s,suffix_carrier=16),
            'excess_legal':replace(s,suffix_legal=3),
            'excess_standard':replace(s,standard_boundary=5252),
        }
        for name,state in cases.items():
            with self.subTest(case=name),self.assertRaises(m.ContractError):
                m.outer_domain_check(state,m.OUTER,(0,3,15),(0,3,15))

    def test_derivative_requires_inner_partition(self):
        s=m.cancel_inserted(m.raw_inner(),'N14-owned-polynomial-quotients')
        with self.assertRaises(m.ContractError):m.differentiate_regularized(replace(s,partition=m.OUTER))
        with self.assertRaises(m.ContractError):m.differentiate_regularized(m.raw_inner())

    def test_deleted_prefix_stays_owned(self):
        s,_=m.homotopy_adjoint(m.initial_owners(5),-1)
        s,_=m.cech_face(s,0)
        s,_=m.homotopy_adjoint(s,0)
        s,_=m.cech_face(s,0)
        self.assertEqual(s.active,('o2','o3','o4'))
        self.assertEqual(s.required_prefix,frozenset(('o0','o1')))
        self.assertTrue(s.required_prefix <= s.kernel_owners <= s.weighted_owners)

    def test_cli_fail_closed_before_stdout(self):
        path=Path(m.__file__)
        for flags in (['-O'],['-OO']):
            run=subprocess.run([sys.executable,*flags,str(path)],capture_output=True)
            with self.subTest(flags=flags):
                self.assertEqual(run.returncode,2);self.assertEqual(run.stdout,b'')
        for extra in (['--max-output-bytes','1'],['--max-output-bytes','24577'],['--execute']):
            run=subprocess.run([sys.executable,str(path),*extra],capture_output=True)
            with self.subTest(extra=extra):
                self.assertEqual(run.returncode,2);self.assertEqual(run.stdout,b'')

    def test_cli_matches_canonical_metadata(self):
        run=subprocess.run([sys.executable,m.__file__],capture_output=True)
        self.assertEqual(run.returncode,0)
        self.assertEqual(run.stdout,m.encode_certificate(m.build_certificate()))
        self.assertLessEqual(len(run.stdout),m.MAX_OUTPUT_BYTES)
        self.assertFalse(json.loads(run.stdout)['execution_release'])

if __name__=='__main__':unittest.main(verbosity=2)
