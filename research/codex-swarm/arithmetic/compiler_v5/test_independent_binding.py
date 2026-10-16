"""V09R bounded metadata controls; never import or evaluate the source compiler.

Run with python -B [-O] -m unittest discover -s
research/codex-swarm/arithmetic/compiler_v5 -p test_independent_binding.py -v.
Assertions use unittest so optimization cannot disable them. No third-party packages.
"""
import copy
import gzip
import hashlib
import json
from pathlib import Path
import unittest

import bind_requests as b

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
REV = 'ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18'
OWNERS = {
    12: [[12, 0, 5, 8, 1], [12, 1, 1, 9, 9], [12, 2, 2, 11, 13], [12, 3, 4, 15, 15]],
    30: [[30, 0, 0, 0, 0], [30, 1, 1, 1, 8], [30, 2, 2, 3, 12],
         [30, 3, 3, 7, 14], [30, 4, 4, 15, 15]],
}
GATES = {'raw_v5_projection_equivalence', 'T12F12_realized',
         'combined_inner_poles_discharged', 'Laurent_admitted',
         'actual_detector_admitted', 'execution_release',
         'physical_source_evaluated', 'historical_order_audit_accepted'}


def specialize(value, owners):
    """Independent typed substitution; no producer substitute/bind calls."""
    if isinstance(value, list):
        if len(value) == 3 and isinstance(value[0], str) and value[0] in (
                'carrier', 'legal_mask', 'standard_tag'):
            if value[1] != owners[0][0]:
                raise ValueError('foreign seed')
            return owners[value[2]][{'carrier': 2, 'legal_mask': 3, 'standard_tag': 4}[value[0]]]
        return [specialize(x, owners) for x in value]
    if isinstance(value, dict):
        return {k: specialize(v, owners) for k, v in value.items()}
    return value


def nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)


class IndependentBindingTests(unittest.TestCase):
    rejected = 0

    @classmethod
    def setUpClass(cls):
        cls.graph, cls.pins = b.authenticate(REPO)
        cls.raw = {name: b.git_read(REPO, name)
                   for name in ['SHA256SUMS', *cls.pins['files']]}
        cls.results = {sid: b.bind(b.request(sid), cls.graph, cls.pins) for sid in OWNERS}

    @classmethod
    def tearDownClass(cls):
        print('V09R: {} adversarial rejections ({})'.format(
            cls.rejected, 'normal' if __debug__ else 'optimized'))

    def reject(self, label, action):
        with self.subTest(control=label):
            with self.assertRaises(ValueError):
                action()
            type(self).rejected += 1

    def test_raw_provenance_and_artifact_identity(self):
        self.assertEqual(self.pins['commit'], REV)
        manifest = self.raw['SHA256SUMS']
        self.assertEqual(hashlib.sha1(b'blob ' + str(len(manifest)).encode() + b'\0' + manifest).hexdigest(),
                         '7e4a18ed9fe8a9c32cc6cf3b710e276c69af5c79')
        sums = dict((line.split()[1], line.split()[0]) for line in manifest.decode().splitlines())
        for name, pin in self.pins['files'].items():
            raw = self.raw[name]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), sums[name])
            self.assertEqual(pin['sha256'], sums[name])
            self.assertEqual(pin['git_blob'], hashlib.sha1(
                b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest())
        raw_graph = gzip.decompress(self.raw['actual-scalar-differential-kernel.json.gz'])
        self.assertEqual(len(raw_graph), 3379185)
        self.assertEqual(hashlib.sha256(raw_graph).hexdigest(),
                         'cc21900c9071899dd1e607ba476451877e6ea3a92e44cd8dd926f5bfbdadd6fe')
        self.assertEqual(json.loads(raw_graph), self.graph)
        for sid, result in self.results.items():
            self.assertEqual(json.loads((HERE / f'seed{sid}-binding.json').read_text()), result)
            self.assertEqual(json.loads((HERE / f'seed{sid}-request.json').read_text()), result['request'])

    def test_explicit_tracefree_wrapper_and_raw_branch_provenance(self):
        for sid, result in self.results.items():
            owners = OWNERS[sid]
            source = specialize(self.graph['seeds'][sid], owners)
            raw_branches = [x for x in source['derivative_terms'] if x['derivative_pair'] == [2, 3]]
            self.assertEqual([x['source_branch'] for x in result['branches']], raw_branches)
            self.assertEqual(len(result['branches']), 4)
            self.assertIn('equality to raw v5 contraction unresolved', result['compiler_scope'])
            for branch in result['branches']:
                current = branch['source_branch']['current_source_binding']
                reference = branch['normal_order_source_reference']
                self.assertIs(reference['requires_demand_current_projection'], True)
                self.assertEqual(reference['template_application'],
                                 'C must contract demand_current; equivalence to raw v5 C is not asserted')
                self.assertEqual(branch['demand_current'], {
                    'operator': 'tracefree', 'formula': 'R-tr(R)/2*I_2',
                    'input_ast': current['normalized_source_ast'],
                    'frame': 'global-finite-product-frame', 'shape': [2, 2],
                    'raw_v5_projection_equivalence': 'unresolved; raw source AST retained for provenance'})
                self.assertIs(current['physical_matrix_identified_with_normalized'], False)
                self.assertIs(current['moving_frame_log_terms_retained'], True)
                logs = [x for x in nodes(current['normalized_source_ast'])
                        if x.get('op') == 'logarithmic_diagonal_frame']
                self.assertEqual(len(logs), 2)
                self.assertEqual({tuple(x['args'][0]) for x in logs},
                                 {tuple(o) for o in (owners[-3:-1] if current['kind'] == 'L' else owners[-2:])})
                self.assertEqual([x['args'][1] for x in logs], [current['coordinate']] * 2)

    def test_fixed_mask_weights_and_provenance_only_collapse(self):
        for sid, result in self.results.items():
            owners = OWNERS[sid]
            source = specialize(self.graph['seeds'][sid], owners)
            provenance = result['source_selector_provenance']
            self.assertEqual(provenance['source_record'], source['selector_source_binding'])
            self.assertEqual(provenance['usage'], 'provenance-only; collapsed-mask claims do not apply to this request')
            self.assertIs(provenance['applied_to_fixed_mask_request'], False)
            merger = provenance['source_record']['prefix_mask_merger']
            self.assertEqual(merger['legal_weight'], '1')
            self.assertEqual(merger['raw_mask_combinations_removed'], 16 if sid == 12 else 256)
            active = result['selector_source_binding']
            self.assertNotIn('prefix_mask_merger', active)
            self.assertEqual(active['prefix_mask_policy'], {
                'scope': 'fixed-mask-term', 'collapse_applied': False,
                'prefix_owner_positions': [0] if sid == 12 else [0, 1],
                'legal_weight_replaced_by_one': False, 'removed_combinations': 0})
            expected = copy.deepcopy(source['selector_source_binding'])
            del expected['prefix_mask_merger']
            self.assertEqual({k: v for k, v in active.items() if k != 'prefix_mask_policy'}, expected)
            self.assertEqual(result['fixed_mask_legal_weights'], [{
                'owner': o, 'legal_mask': o[3],
                'definition': 'product_i ell_(mask_i,i)^29 * Q_(i,mask_i)',
                'mask_bits_low_first': [(o[3] >> i) & 1 for i in range(4)],
                'component_of_existing_outer_weight': True,
                'multiply_as_extra_factor': False, 'replace_by_one': False} for o in owners])
            self.assertEqual(result['outer_weight_source_bindings'], source['outer_weight_source_bindings'])
            self.assertEqual([x['owner'] for x in result['outer_weight_source_bindings']], owners)

    def test_branch_signs_owners_and_closed_gates(self):
        for sid, result in self.results.items():
            owners = OWNERS[sid]
            self.assertEqual(result['request']['owners'], owners)
            self.assertEqual(result['weighted_owners'], list(range(len(owners))))
            self.assertEqual(result['deleted_prefix_owners'], [0] if sid == 12 else [0, 1])
            tail = list(range(len(owners) - 3, len(owners)))
            i, j, k = tail
            expected = [([j, k], 2, 'L', 3, 1), ([j, k], 3, 'L', 2, -1),
                        ([i, j], 3, 'U', 2, 1), ([i, j], 2, 'U', 3, -1)]
            for branch, (edge, d, kind, c, sign) in zip(result['branches'], expected):
                raw = branch['source_branch']
                self.assertEqual((raw['edge'], raw['coordinate'], raw['current']), (edge, d, [kind, c, tail]))
                self.assertEqual(raw['coefficient'], [sign, 2])
                self.assertEqual(branch['effective_scalar_coefficient'], [(2 if sid == 12 else 1) * sign, 2])
                self.assertEqual(raw['owned_edge_definition']['vertices'], [owners[x] for x in edge])
                self.assertEqual(raw['current_source_binding']['owners'], owners[-3:])
                self.assertIs(branch['pending_null_lemma']['discharged'], False)
                self.assertIsNone(branch['pending_null_lemma']['proof_reference'])
            self.assertEqual(set(result['gates']), GATES)
            self.assertTrue(all(x is False for x in result['gates'].values()))

    def test_legacy_adversarial_controls(self):
        # The earlier 68 controls, plus two checks for the newly added gate.
        for sid, base in self.results.items():
            req = b.request(sid)
            mutations = [
                ('missing branch', lambda r: r['branches'].pop()),
                ('branch permutation', lambda r: r['branches'].reverse()),
                ('missing prefix weight', lambda r: r['outer_weight_source_bindings'].pop(0)),
                ('drop prefix selector', lambda r: r['selector_source_binding']['owners'].pop(0)),
                ('wrong coefficient', lambda r: r['branches'][0].__setitem__('effective_scalar_coefficient', [1, 1])),
                ('wrong derivative', lambda r: r['branches'][0]['source_branch'].__setitem__('coordinate', 0)),
                ('wrong scalar edge', lambda r: r['branches'][0]['source_branch']['edge'].reverse()),
                ('drop Q/source AST', lambda r: r['branches'][0]['source_branch']['current_source_binding'].pop('normalized_source_ast')),
                ('physical=normalized', lambda r: r['branches'][0]['source_branch']['current_source_binding'].__setitem__('physical_matrix_identified_with_normalized', True)),
                ('claim discharged', lambda r: r['branches'][0]['pending_null_lemma'].__setitem__('discharged', True)),
                ('forge proof', lambda r: r['branches'][0]['pending_null_lemma'].__setitem__('proof_reference', 'claimed')),
                ('drop domain requirement', lambda r: r['branches'][0]['pending_null_lemma']['must_instantiate'].pop()),
                ('mutate provenance', lambda r: r['source_authentication'].__setitem__('commit', 'HEAD'))]
            for name, mutate in mutations:
                r = copy.deepcopy(base)
                mutate(r)
                self.reject((sid, name), lambda: b.validate_result(req, r, self.graph, self.pins))
            for gate in base['gates']:
                r = copy.deepcopy(base)
                r['gates'][gate] = True
                self.reject((sid, gate), lambda: b.validate_result(req, r, self.graph, self.pins))
            for key, value in [('orientation', True), ('seed', float(sid)),
                               ('prefix_mask_scope', 'prefix-summed'), ('frame', 'infinity-local')]:
                req_bad = copy.deepcopy(req)
                req_bad[key] = value
                self.reject((sid, key), lambda: b.bind(req_bad, self.graph, self.pins))
            req_bad = copy.deepcopy(req)
            req_bad['owners'][0][2] = -1
            self.reject((sid, 'sorting key as carrier'), lambda: b.bind(req_bad, self.graph, self.pins))
            graph = copy.deepcopy(self.graph)
            graph['seeds'][sid]['derivative_terms'].pop()
            self.reject((sid, 'graph branch omitted'), lambda: b.bind(req, graph, self.pins))
            pins = copy.deepcopy(self.pins)
            pins['files'].pop('physical_current_source_binding.py')
            self.reject((sid, 'missing provenance'), lambda: b.bind(req, self.graph, pins))
        for name in self.pins['files']:
            self.reject(('source bytes', name), lambda: b.authenticate(
                REPO, reader=lambda n: self.raw[n] + (b' ' if n == name else b'')))

    def test_new_semantic_adversarial_controls(self):
        # Exercise local semantics without relying solely on reconstruction hashes.
        for sid, base in self.results.items():
            for key, value in [('operator', 'identity'), ('formula', 'R'),
                               ('input_ast', {}), ('frame', 'infinity-local'), ('shape', [3, 3])]:
                r = copy.deepcopy(base)
                r['branches'][0]['demand_current'][key] = value
                self.reject((sid, 'wrapper', key), lambda: b.validate_semantics(r))
            for value in (False, None):
                r = copy.deepcopy(base)
                reference = r['branches'][0]['normal_order_source_reference']
                if value is None:
                    del reference['requires_demand_current_projection']
                else:
                    reference['requires_demand_current_projection'] = value
                self.reject((sid, 'normal order bypass', value), lambda: b.validate_semantics(r))
            for key in ('demand_current',):
                r = copy.deepcopy(base)
                del r['branches'][0][key]
                self.reject((sid, 'omitted', key), lambda: b.validate_semantics(r))
            for key, value in [('replace_by_one', True), ('multiply_as_extra_factor', True),
                               ('component_of_existing_outer_weight', False), ('legal_mask', -1),
                               ('mask_bits_low_first', [0, 0, 0, 0]), ('definition', '1')]:
                r = copy.deepcopy(base)
                # Seed30's first mask is already all zero: mutate the last factor.
                r['fixed_mask_legal_weights'][-1][key] = value
                self.reject((sid, 'factor', key), lambda: b.validate_semantics(r))
            for key, value in [('collapse_applied', True), ('removed_combinations', 16),
                               ('legal_weight_replaced_by_one', True), ('prefix_owner_positions', [])]:
                r = copy.deepcopy(base)
                r['selector_source_binding']['prefix_mask_policy'][key] = value
                self.reject((sid, 'policy', key), lambda: b.validate_semantics(r))
            r = copy.deepcopy(base)
            r['selector_source_binding']['prefix_mask_merger'] = copy.deepcopy(
                r['source_selector_provenance']['source_record']['prefix_mask_merger'])
            self.reject((sid, 'active merger leak'), lambda: b.validate_semantics(r))
            for key, value in [('applied_to_fixed_mask_request', True), ('usage', 'applied')]:
                r = copy.deepcopy(base)
                r['source_selector_provenance'][key] = value
                self.reject((sid, 'provenance', key), lambda: b.validate_semantics(r))
            # Reconstruction must also reject erasing disclosure or altering provenance.
            for target, key in [('demand_current', 'raw_v5_projection_equivalence'),
                                ('source_selector_provenance', 'source_record')]:
                r = copy.deepcopy(base)
                obj = r['branches'][0][target] if target == 'demand_current' else r[target]
                del obj[key]
                self.reject((sid, 'disclosure/provenance omission', key),
                            lambda: b.validate_result(b.request(sid), r, self.graph, self.pins))

    def test_published_schema_accepts_new_fields_and_gate(self):
        # Necessary draft-2020-12 constraints, not a replacement JSON Schema engine.
        schema = json.loads((HERE / 'binding-schema.json').read_text())
        branch_schema = schema['properties']['branches']['items']
        for result in self.results.values():
            if schema.get('additionalProperties') is False:
                self.assertFalse(set(result) - set(schema['properties']))
            self.assertEqual(schema['properties']['gates']['const'], result['gates'])
            self.assertIn('demand_current', branch_schema['required'])
            if branch_schema.get('additionalProperties') is False:
                self.assertFalse(set(result['branches'][0]) - set(branch_schema['properties']))


if __name__ == '__main__':
    unittest.main()
