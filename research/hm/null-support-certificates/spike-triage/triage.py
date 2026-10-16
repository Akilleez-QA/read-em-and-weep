#!/usr/bin/env python3
"""Offline deterministic intake. Structural validation never proves mathematics."""
import argparse
import hashlib
import json
import re
import sys

KINDS = {'proved_zero', 'proven_nonzero', 'candidate_overlap', 'counterexample', 'blocker'}
REVIEW = {'pending', 'needs_review', 'accepted', 'rejected'}
HEX = re.compile(r'^[0-9a-f]{64}$')
COMMIT = re.compile(r'^[0-9a-f]{40}(?:[0-9a-f]{24})?$')
PRIORITIES = ['correctness_conflict', 'reviewed_family_elimination', 'executable_candidate', 'review_required', 'unresolved_blocker', 'archive']

def nonempty(x):
    return isinstance(x, str) and bool(x.strip())

def one_of(value, choices):
    return isinstance(value, str) and value in choices

def scope_hash(scope):
    return hashlib.sha256(json.dumps(scope, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()

def validate(r):
    """Return structural errors, not a proof verdict. Fail closed on missing fields."""
    if not isinstance(r, dict):
        return ['result must be an object']
    errors = []
    for k in ('result_id', 'worker_identity', 'claim_id', 'changed_claim', 'unresolved_obligation', 'next_discriminating_test'):
        if not nonempty(r.get(k)):
            errors.append(k + ' must be nonempty text (use explicit none when applicable)')
    if 'parent_claim' not in r or (r['parent_claim'] is not None and not nonempty(r['parent_claim'])):
        errors.append('parent_claim must be null or nonempty text')
    if not isinstance(r.get('source_commit_hash'), str) or not COMMIT.fullmatch(r['source_commit_hash']):
        errors.append('source_commit_hash must be full lowercase Git SHA-1 or SHA-256')
    hashes = r.get('input_artifact_hashes')
    if not isinstance(hashes, dict) or not hashes or any(not nonempty(k) or not isinstance(v, str) or not HEX.fullmatch(v) for k, v in hashes.items()):
        errors.append('input_artifact_hashes must map nonempty artifact names to SHA-256 hashes')
    scope = r.get('scope')
    if not isinstance(scope, dict) or any(not nonempty(scope.get(k)) for k in ('domain', 'quantifiers', 'restrictions', 'family')):
        errors.append('scope must specify exact domain, quantifiers, restrictions, and family')
    if not one_of(r.get('scope_relation'), {'same', 'narrower', 'broader', 'new'}):
        errors.append('scope_relation must be same, narrower, broader, or new')
    if not one_of(r.get('conclusion_kind'), KINDS):
        errors.append('invalid conclusion_kind')
    for k in ('hypotheses', 'proof_artifacts', 'test_commands', 'receipts'):
        if not isinstance(r.get(k), list):
            errors.append(k + ' must be an explicit list')
    for k in ('hypotheses', 'test_commands'):
        if isinstance(r.get(k), list) and any(not nonempty(x) for x in r[k]):
            errors.append(k + ' entries must be nonempty text')
    for k in ('proof_artifacts', 'receipts'):
        if isinstance(r.get(k), list):
            for a in r[k]:
                if not isinstance(a, dict) or not nonempty(a.get('path')) or not isinstance(a.get('sha256'), str) or not HEX.fullmatch(a['sha256']):
                    errors.append(k + ' entries require path and sha256')
    if not one_of(r.get('evidence_kind'), {'proof', 'support_overlap_only', 'computation', 'none'}):
        errors.append('invalid evidence_kind')
    if not one_of(r.get('execution_status'), {'completed', 'not_run', 'resource_failure'}):
        errors.append('invalid execution_status')
    if not isinstance(r.get('eliminates_family'), bool):
        errors.append('eliminates_family must be boolean')
    review = r.get('review')
    if not isinstance(review, dict):
        errors.append('review must be an object')
    else:
        if not one_of(review.get('status'), REVIEW):
            errors.append('invalid review.status')
        if 'reviewer_identity' not in review or (review.get('reviewer_identity') is not None and not nonempty(review.get('reviewer_identity'))):
            errors.append('invalid reviewer identity')
        if not isinstance(review.get('reviewer_independence'), bool):
            errors.append('reviewer_independence must be boolean')
        if review.get('status') == 'accepted':
            if not nonempty(review.get('reviewer_identity')) or review.get('reviewer_identity') == r.get('worker_identity') or review.get('reviewer_independence') is not True:
                errors.append('accepted requires a different reviewer asserting independence')
            if not nonempty(review.get('review_receipt')):
                errors.append('accepted requires a review_receipt reference')
    if r.get('evidence_kind') == 'support_overlap_only' and r.get('conclusion_kind') == 'proven_nonzero':
        errors.append('support overlap alone cannot establish nonzero')
    if r.get('execution_status') == 'resource_failure' and r.get('conclusion_kind') != 'blocker':
        errors.append('resource failure is undecided; report blocker, not a mathematical conclusion')
    if one_of(r.get('conclusion_kind'), {'proved_zero', 'proven_nonzero', 'counterexample'}) and not r.get('proof_artifacts'):
        errors.append('claimed mathematical conclusion needs a proof/witness artifact')
    if r.get('eliminates_family') is True and r.get('conclusion_kind') != 'proved_zero':
        errors.append('family elimination requires a claimed proved_zero result')
    return errors

def classify(results, context=None):
    """Context is an optional trusted snapshot; supplied assertions are not verified."""
    context = context or {}
    known_ids = set(context.get('seen_result_ids', []))
    seen_inputs = set()
    out = []
    for r in results:
        errors = validate(r)
        row = {'result_id': r.get('result_id') if isinstance(r, dict) else None,
               'schema_valid': not errors, 'mathematical_truth': 'not_verified',
               'errors': errors, 'flags': [], 'priority': 'review_required'}
        out.append(row)
        if errors:
            row['flags'].append('quarantined')
            continue
        rid = r['result_id']
        if rid in known_ids:
            row['flags'].append('duplicate_result_id')
        known_ids.add(rid)
        identity = json.dumps({k: v for k, v in r.items() if k != 'result_id'}, sort_keys=True)
        if identity in seen_inputs:
            row['flags'].append('duplicate_input_result')
        seen_inputs.add(identity)
        current = context.get('current_claims', {}).get(r['claim_id'])
        if current is None:
            row['flags'].append('freshness_unverified')
        else:
            if current.get('source_commit_hash') != r['source_commit_hash'] or current.get('input_artifact_hashes') != r['input_artifact_hashes']:
                row['flags'].append('stale_inputs')
            if current.get('scope_hash') != scope_hash(r['scope']):
                row['flags'].append('scope_change_requires_review')
        if r['scope_relation'] == 'broader':
            row['flags'].append('scope_broadening_requires_review')
        row['reported_review_status'] = r['review']['status']
        row['effective_review_status'] = r['review']['status']
        if any(f in row['flags'] for f in ('scope_change_requires_review', 'scope_broadening_requires_review', 'stale_inputs')):
            row['effective_review_status'] = 'needs_review'
        if any(f in row['flags'] for f in ('duplicate_result_id', 'duplicate_input_result', 'stale_inputs')) or r['review']['status'] == 'rejected':
            row['priority'] = 'archive'
        elif row['effective_review_status'] == 'accepted' and r['eliminates_family']:
            row['priority'] = 'reviewed_family_elimination'
        elif r['conclusion_kind'] == 'candidate_overlap' and r['test_commands']:
            row['priority'] = 'executable_candidate'
        elif r['conclusion_kind'] == 'blocker':
            row['priority'] = 'unresolved_blocker'
        if r['execution_status'] == 'resource_failure':
            row['flags'].append('undecided_resource_failure')
    # Exact-scope/input contradictions only; no semantic equivalence inference.
    groups = {}
    for r, row in zip(results, out):
        if not row['schema_valid'] or row['priority'] == 'archive':
            continue
        key = (r['claim_id'], scope_hash(r['scope']), r['source_commit_hash'], json.dumps(r['input_artifact_hashes'], sort_keys=True), json.dumps(r['hypotheses'], sort_keys=True))
        groups.setdefault(key, []).append((r, row))
    for group in groups.values():
        kinds = {r['conclusion_kind'] for r, _ in group}
        if 'proved_zero' in kinds and ('proven_nonzero' in kinds or 'counterexample' in kinds):
            for _, row in group:
                row['priority'] = 'correctness_conflict'
                row['flags'].append('incompatible_claims_require_review')
                row['effective_review_status'] = 'needs_review'
    return sorted(out, key=lambda row: (PRIORITIES.index(row['priority']), str(row['result_id'])))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('results', help='JSON array or one envelope; use - for stdin')
    p.add_argument('--context', help='optional trusted current-claim and seen-ID JSON snapshot')
    args = p.parse_args()
    try:
        if args.results == '-':
            results = json.load(sys.stdin)
        else:
            with open(args.results, encoding='utf-8') as f:
                results = json.load(f)
        context = None
        if args.context:
            with open(args.context, encoding='utf-8') as f:
                context = json.load(f)
        if not isinstance(results, list):
            results = [results]
        if context is not None and (not isinstance(context, dict) or not isinstance(context.get('seen_result_ids', []), list) or any(not isinstance(v, str) for v in context.get('seen_result_ids', [])) or not isinstance(context.get('current_claims', {}), dict) or any(not isinstance(v, dict) for v in context.get('current_claims', {}).values())):
            raise ValueError('invalid context snapshot shape')
        report = {'warning': 'Schema-valid is not proved. Review assertions and artifact hashes are not authenticated or replayed.',
                  'roles': {'null': 'mathematical intake', 'mr.slop': 'proposed independent reviewer; assignment is not acceptance'},
                  'queue': classify(results, context)}
        print(json.dumps(report, indent=2))
        return 1 if any(not x['schema_valid'] for x in report['queue']) else 0
    except (ValueError, OSError, TypeError) as e:
        print('Input error: ' + str(e), file=sys.stderr)
        return 2

if __name__ == '__main__':
    sys.exit(main())
