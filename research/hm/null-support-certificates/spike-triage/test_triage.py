import copy
import json
import pathlib
import subprocess
import sys
import unittest
import triage


def envelope(**changes):
    r = dict(result_id='r1', worker_identity='worker-a', claim_id='claim-1', parent_claim=None,
             source_commit_hash='a'*40, input_artifact_hashes={'matrix.json': 'b'*64},
             scope={'domain':'integer matrices of size 2 by 2', 'quantifiers':'for every matrix in the supplied family', 'restrictions':'entries in {0, 1}', 'family':'F1'},
             scope_relation='same', conclusion_kind='candidate_overlap', hypotheses=['matrix is in F1'],
             proof_artifacts=[], test_commands=['python verify.py matrix.json'], receipts=[],
             evidence_kind='support_overlap_only', execution_status='completed', eliminates_family=False,
             review={'status':'pending','reviewer_identity':None,'reviewer_independence':False,'review_receipt':None},
             changed_claim='Candidate supports intersect.', unresolved_obligation='Prove noncancellation.',
             next_discriminating_test='Compute the signed coefficient exactly.')
    r.update(changes)
    return r


def proved(kind='proved_zero', **changes):
    r = envelope(conclusion_kind=kind, evidence_kind='proof', proof_artifacts=[{'path':'proof.txt','sha256':'c'*64}],
                 review={'status':'accepted','reviewer_identity':'reviewer-b','reviewer_independence':True,'review_receipt':'review-42'})
    r.update(changes)
    return r


class Tests(unittest.TestCase):
    def test_valid_is_not_truth(self):
        row = triage.classify([envelope()])[0]
        self.assertTrue(row['schema_valid'])
        self.assertEqual(row['mathematical_truth'], 'not_verified')
        self.assertEqual(row['priority'], 'executable_candidate')
        self.assertIn('freshness_unverified', row['flags'])

    def test_missing_scope_and_hashes(self):
        for field in ['scope', 'source_commit_hash', 'input_artifact_hashes']:
            r = envelope(); del r[field]
            self.assertTrue(triage.validate(r))

    def test_self_review(self):
        r = proved(); r['review']['reviewer_identity'] = r['worker_identity']
        self.assertTrue(triage.validate(r))

    def test_independence_required(self):
        r = proved(); r['review']['reviewer_independence'] = False
        self.assertTrue(triage.validate(r))

    def test_overlap_not_nonzero(self):
        self.assertTrue(triage.validate(envelope(conclusion_kind='proven_nonzero')))

    def test_resource_failure_undecided(self):
        self.assertTrue(triage.validate(proved(execution_status='resource_failure')))
        row = triage.classify([envelope(conclusion_kind='blocker', execution_status='resource_failure')])[0]
        self.assertIn('undecided_resource_failure', row['flags'])

    def test_broadening_needs_review(self):
        row = triage.classify([proved(scope_relation='broader', eliminates_family=True)])[0]
        self.assertEqual(row['effective_review_status'], 'needs_review')
        self.assertEqual(row['priority'], 'review_required')

    def test_duplicates(self):
        a = envelope(); b = envelope(result_id='r2')
        rows = triage.classify([a, copy.deepcopy(a), b])
        self.assertEqual(sum(r['priority']=='archive' for r in rows), 2)

    def test_stale_input(self):
        r = envelope()
        ctx = {'current_claims':{'claim-1':{'source_commit_hash':'d'*40,'input_artifact_hashes':r['input_artifact_hashes'],'scope_hash':triage.scope_hash(r['scope'])}}}
        row = triage.classify([r], ctx)[0]
        self.assertIn('stale_inputs', row['flags'])
        self.assertEqual(row['priority'], 'archive')

    def test_context_scope_change(self):
        r = proved(eliminates_family=True)
        ctx = {'current_claims':{'claim-1':{'source_commit_hash':r['source_commit_hash'],'input_artifact_hashes':r['input_artifact_hashes'],'scope_hash':'different'}}}
        self.assertEqual(triage.classify([r], ctx)[0]['effective_review_status'], 'needs_review')

    def test_queue_conflict_first(self):
        rows = triage.classify([envelope(), proved(result_id='zero'), proved('proven_nonzero', result_id='nonzero')])
        self.assertEqual(rows[0]['priority'], 'correctness_conflict')
        self.assertEqual(rows[1]['priority'], 'correctness_conflict')

    def test_different_hypotheses_not_conflict(self):
        rows = triage.classify([proved(), proved('proven_nonzero', result_id='n', hypotheses=['different premise'])])
        self.assertFalse(any(r['priority']=='correctness_conflict' for r in rows))

    def test_family_priority(self):
        rows = triage.classify([envelope(), proved(result_id='zero', eliminates_family=True)])
        self.assertEqual(rows[0]['priority'], 'reviewed_family_elimination')

    def test_cli_stdin(self):
        proc = subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('triage.py')), '-'], input=json.dumps([envelope()]), text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout)['queue'][0]['result_id'], 'r1')

    def test_updated_proof_not_duplicate(self):
        a = proved(); b = copy.deepcopy(a)
        b['result_id'] = 'new-proof'
        b['proof_artifacts'][0]['sha256'] = 'd'*64
        self.assertFalse(any('duplicate_input_result' in r['flags'] for r in triage.classify([a,b])))

    def test_invalid_enum_types(self):
        for k in ['scope_relation','conclusion_kind','evidence_kind','execution_status']:
            r = envelope(); r[k] = []
            self.assertTrue(triage.validate(r))

    def test_invalid_types(self):
        for r in [None, [], {}, envelope(scope=3), envelope(receipts=[1])]:
            self.assertTrue(triage.validate(r))

if __name__ == '__main__':
    unittest.main()
