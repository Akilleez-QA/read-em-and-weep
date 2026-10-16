"""TR-R independent tiny formal controls. No physical source evaluator imports.

Run with python -B -m unittest discover -s research/codex-swarm/transport-binding
    -p test_independent.py -v
Synthetic matrices below are deliberately artificial, not HM coefficients.
"""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PIN = '10810ee877fdaf291399198ad60d7dd0c316a42d'
OLD = '08b73637d4136f91606aad332c46cafd064417f8'
NULL = '43193bc8badf3f29a1363132135d956cc12d46ad'
RANKS = (5, 15, 10, 2)


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def add(a, b, scale=1):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0) + scale * value
        if not out[key]:
            del out[key]
    return out


def multiply(a, b):
    out = {}
    for (i, k), x in a.items():
        for (l, j), y in b.items():
            if k == l:
                out[(i, j)] = out.get((i, j), 0) + x * y
    return {k: v for k, v in out.items() if v}


OFFSETS = (0, 5, 20, 30)
# Artificial chain complex with the source's ranks and two selected row identities.
DK = {(OFFSETS[1] + 10, OFFSETS[0]): 2,
      (OFFSETS[3], OFFSETS[2]): 2,
      (OFFSETS[3] + 1, OFFSETS[2] + 1): 3}


def dend(f, degree):
    return add(multiply(DK, f), multiply(f, DK), -1 if degree % 2 == 0 else 1)


def scalar_l(f):
    return f.get((OFFSETS[0], OFFSETS[2]), 0) - f.get((OFFSETS[1] + 10, OFFSETS[3]), 0)


def delta(cochain, q, n=7):
    out = {}
    for face in itertools.combinations(range(n), q + 2):
        value = {}
        for i in range(q + 2):
            value = add(value, cochain.get(face[:i] + face[i + 1:], {}), (-1) ** i)
        if value:
            out[face] = value
    return out


def vertical(cochain, degree):
    return {face: x for face, f in cochain.items() if (x := dend(f, degree))}


def require_top_closure(j2, j3):
    if delta(j2, 4) != vertical(j3, -3):
        raise ValueError('delta J2 must equal d_End J3')
    if delta(j3, 5):
        raise ValueError('delta J3 must vanish')


def frame_value(value, tau, degree, conversions=1, deck_removed=True):
    if conversions != 1 or not deck_removed:
        raise ValueError('remove deck product and convert original frame once')
    return value * tau ** (degree - 2)


def require_standard_owner(source_tags, target_tags):
    if not set(source_tags) <= set(target_tags):
        raise ValueError('same actual standard owner required before Z is a unit')


def packet_for_controls(module):
    """Syntactically complete FAKE witnesses, never authenticated source proof."""
    owners = [[0, 0, 5, 0, 3], [0, 1, 1, 2, 11], [0, 2, 2, 1, 15]]
    return {'schema': 'tr01-actual-source-packet-v1',
            'source_components': module.source_components(),
            'lift': module.closed_lift_schema(), 'frame': copy.deepcopy(module.FRAME),
            'projection_terms': [{'owners': owners, 'outer_weight_owners': copy.deepcopy(owners),
                                  'target_standard_tags': [3, 11, 15],
                                  'source_sorted_owners': copy.deepcopy(owners), 'sorting_sign': 1}],
            'source_order': 'synthetic-order', 'intended_order': 'synthetic-order',
            'order_witness': {'kind': 'same_defined_alternating_source',
                              'proof_sha256': 'a' * 64, 'source_definition_sha256': 'b' * 64},
            'closure_witnesses': {eq: {'proof_sha256': 'c' * 64, 'domain_sha256': 'd' * 64}
                                  for eq in module.closed_lift_schema()['closure_equations']},
            'whole_standard_extension_witnesses': [{
                'scope': 'whole_lift_component_and_all_prism_restrictions_on_standard_target',
                'denominator_owners': copy.deepcopy(owners), 'target_standard_tags': [3, 11, 15],
                'identity_sha256': 'e' * 64, 'domain_sha256': 'f' * 64}],
            'projection_mode': 'complete_Rsharp_only'}


class IndependentSourceTests(unittest.TestCase):
    def test_staging_marker_hashes_are_only_handoff(self):
        marker = json.loads((HERE / 'producer-ready.json').read_text())
        self.assertIs(marker['actual_source_admitted'], False)
        self.assertIs(marker['execution_release'], False)
        for name, record in marker['files'].items():
            raw = (HERE / name).read_bytes()
            self.assertEqual(len(raw), record['bytes'])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), record['sha256'])

    def test_all_pinned_bytes_and_git_blobs(self):
        pins = json.loads((HERE / 'source-pins.json').read_text())['sources']
        self.assertEqual(len(pins), 15)
        for record in pins:
            path = record['path']
            expected = (OLD if path.endswith('map-and-comparison.md') else
                        NULL if '/scalar-family-transport/' in path or '/tracefree-currents/' in path else PIN)
            self.assertEqual(record['commit'], expected)
            raw = subprocess.check_output(['git', 'show', record['commit'] + ':' + record['path']], cwd=ROOT)
            self.assertEqual(len(raw), record['bytes'])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), record['sha256'])
            blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
            self.assertEqual(blob, record['git_blob'])

    def test_lift_degree_sign_direction_and_top(self):
        schema = load('lift_schema').closed_lift_schema()
        nodes = schema['nodes']
        self.assertEqual([(n['id'], n['cech_degree'], n['internal_degree']) for n in nodes],
                         [('J0', 2, 0), ('J1', 3, -1), ('J2', 4, -2), ('J3', 5, -3)])
        self.assertEqual([n['coefficient'] for n in nodes], [1, 1, -1, 1])
        self.assertEqual([n['homotopy_input_degree'] for n in nodes[1:]], [0, -1, -2])
        self.assertIn('delta J2-d_End J3=0', schema['closure_equations'])
        self.assertEqual([(b['source'], b['target'], b['shape']) for b in schema['HK_blocks']],
                         [(1, 0, [5, 15]), (2, 1, [15, 10]), (3, 2, [10, 2])])
        self.assertEqual(schema['top_component_required'], 'J3')

    def test_LdEnd_all_ten_formal_bottom_units(self):
        self.assertEqual(multiply(DK, DK), {})
        self.assertEqual(RANKS[0] * RANKS[3], 10)
        for i, j in itertools.product(range(5), range(2)):
            w = {(OFFSETS[0] + i, OFFSETS[3] + j): Q(1)}
            dw = dend(w, -3)
            self.assertEqual(scalar_l(dw), 0)
            self.assertEqual(dend(dw, -2), {})
        w = {(0, OFFSETS[3]): Q(1)}
        dw = dend(w, -3)
        # Opposite sign and the wrong source block projection are detected.
        self.assertEqual(dw[(0, OFFSETS[2])], 2)
        self.assertEqual(dw[(OFFSETS[1] + 10, OFFSETS[3])], 2)
        self.assertNotEqual(dw[(0, OFFSETS[2])] + dw[(OFFSETS[1] + 10, OFFSETS[3])], 0)

    def test_synthetic_closed_boundary_needs_J3(self):
        # Boundary of (3,-2) + (4,-3) cochains; nonzero scalar boundary.
        b = {(0, 1, 2, 3, 4): {(0, OFFSETS[3]): Q(7)}}
        a = {(0, 1, 2, 3): {(0, OFFSETS[2]): Q(3)}}
        j1 = {face: {k: -v for k, v in x.items()} for face, x in vertical(a, -2).items()}
        j2, j3 = vertical(b, -3), delta(b, 4)
        for face, value in delta(a, 3).items():
            j2[face] = add(j2.get(face, {}), value)
        j2 = {face: value for face, value in j2.items() if value}
        self.assertTrue(j3)
        self.assertTrue(delta(j2, 4))
        require_top_closure(j2, j3)
        self.assertEqual(delta(j1, 3), {face: {k: -v for k, v in x.items()}
                                     for face, x in vertical(j2, -2).items()})
        scalar_boundary = delta({face: {('scalar',): scalar_l(x)} for face, x in a.items()}, 3)
        self.assertTrue(scalar_boundary)
        self.assertEqual({face: {('scalar',): scalar_l(x)} for face, x in j2.items() if scalar_l(x)},
                         scalar_boundary)
        self.assertEqual(delta(scalar_boundary, 4), {})
        with self.assertRaises(ValueError):
            require_top_closure(j2, {})
        with self.assertRaises(ValueError):
            require_top_closure(j2, {f: {k: -v for k, v in x.items()} for f, x in j3.items()})

    def test_synthetic_frame_covariance_and_double_move_negative(self):
        # Artificial independent values, no physical section substituted.
        section, tau = Q(13), Q(3, 2)
        moved = frame_value(section, tau, -2)
        self.assertEqual(moved, Q(208, 81))
        self.assertEqual(frame_value(moved, 1 / tau, -2), section)
        self.assertNotEqual(section * tau ** (-2), moved)
        self.assertNotEqual(moved * tau ** (-4), moved)
        with self.assertRaises(ValueError):
            frame_value(section, tau, -2, conversions=2)
        with self.assertRaises(ValueError):
            frame_value(section, tau, -2, deck_removed=False)

    def test_row_transpose_inclusion_frame_covariance(self):
        transpose = lambda a: {(j, i): x for (i, j), x in a.items()}
        i = {(0, 0): Q(1), (0, 1): Q(2), (10, 0): Q(3), (14, 1): Q(5)}
        p = {(0, 2): Q(7), (1, 6): Q(11), (1, 9): Q(13)}
        r = {(0, 0): Q(17), (0, 1): Q(19), (1, 0): Q(23), (1, 1): Q(29)}
        n = {(0, 0): Q(2), (0, 1): Q(1), (1, 1): Q(1, 2)}
        ni = {(0, 0): Q(1, 2), (0, 1): Q(-1), (1, 1): Q(2)}
        self.assertEqual(multiply(n, ni), {(0, 0): 1, (1, 1): 1})
        include = lambda left, value, right: multiply(multiply(left, transpose(value)), right)
        ip, pp = multiply(i, transpose(n)), multiply(transpose(ni), p)
        moved_r = multiply(multiply(n, r), ni)
        self.assertEqual(include(ip, moved_r, pp), include(i, r, p))
        self.assertNotEqual(include(multiply(ip, transpose(n)), moved_r,
                                    multiply(transpose(ni), pp)), include(i, r, p))
        self.assertNotEqual(multiply(multiply(ip, moved_r), pp), include(i, r, p))

    def test_wrong_standard_projection_negative(self):
        require_standard_owner([3, 11, 15], [15, 3, 11])
        with self.assertRaises(ValueError):
            require_standard_owner([3, 11, 15], [3, 7, 15])

    def test_frozen_N_and_moving_Q_product_rule_control(self):
        # Jet pairs are artificial (value, derivative), not source jets.
        mul = lambda a, b: (a[0] * b[0], a[1] * b[0] + a[0] * b[1])
        frozen_n, moving_q = (Q(7), Q(0)), (Q(3), Q(5))
        self.assertEqual(mul(frozen_n, moving_q), (21, 35))
        self.assertNotEqual(mul(frozen_n, (3, 0)), (21, 35))
        self.assertNotEqual(mul((7, 1), moving_q), (21, 35))
        frame = load('transport_binding').FRAME
        self.assertIn('constant endpoint jets', frame['frozen_endpoint_rule'])
        self.assertIn('never drop moving frame derivatives', frame['frozen_endpoint_rule'])

    def test_packet_negative_controls_reach_structural_checks(self):
        module = load('transport_binding')
        adapters = copy.deepcopy(module.ADAPTER_SLOTS)
        base = packet_for_controls(module)
        # Byte authentication is exercised separately, not repeated for mutations.
        with patch.object(module, 'authenticate', return_value=None):
            with self.assertRaisesRegex(ValueError, 'pending independently reviewed'):
                module.validate_actual_packet(base, adapters)
            with self.assertRaisesRegex(ValueError, 'untrusted theorem adapter'):
                module.validate_actual_packet(base, {key: True for key in adapters})
            mutations = []
            p = copy.deepcopy(base)
            p['whole_standard_extension_witnesses'][0]['scope'] = 'common_localization_only'
            mutations.append((p, 'common-localized or directional-only'))
            p = copy.deepcopy(base)
            p['lift']['nodes'].pop()
            mutations.append((p, 'missing top J3'))
            p = copy.deepcopy(base)
            p['closure_witnesses'].pop('delta J3=0')
            mutations.append((p, 'all five closed-lift witness'))
            p = copy.deepcopy(base)
            p['order_witness']['proof_sha256'] = 'a' * 63
            mutations.append((p, 'order/source proof hashes'))
            p = copy.deepcopy(base)
            p['order_witness']['source_definition_sha256'] = 'b' * 63
            mutations.append((p, 'order/source proof hashes'))
            p = copy.deepcopy(base)
            p['source_order'] = 'historical-order-unknown'
            mutations.append((p, 'fresh/historical identification missing'))
            p = copy.deepcopy(base)
            p['frame']['deck_product_removed_count'] = 2
            mutations.append((p, 'original frame/deck product/tau'))
            p = copy.deepcopy(base)
            p['frame']['scalar_tau_exponent'] = -2
            mutations.append((p, 'original frame/deck product/tau'))
            p = copy.deepcopy(base)
            p['projection_terms'][0]['target_standard_tags'] = [3, 7, 15]
            mutations.append((p, 'owner standard is not a target unit'))
            p = copy.deepcopy(base)
            p['source_components'].pop()
            mutations.append((p, 'missing corrected source component'))
            p = copy.deepcopy(base)
            p['projection_mode'] = 'E12_only'
            mutations.append((p, 'projected directional source'))
            for packet, message in mutations:
                with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                    module.validate_actual_packet(packet, adapters)

    def test_owner_prefix_survives_and_projection_checks_independent_of_gate(self):
        module = load('transport_binding')
        term = packet_for_controls(module)['projection_terms'][0]
        self.assertTrue(module.validate_owner_term(term))
        bad = copy.deepcopy(term)
        bad['outer_weight_owners'].pop(0)
        with self.assertRaisesRegex(ValueError, 'deleted/prefix weight owner lost'):
            module.validate_owner_term(bad)
        bad = copy.deepcopy(term)
        bad['source_sorted_owners'].reverse()
        with self.assertRaisesRegex(ValueError, 'source owner permutation'):
            module.validate_owner_term(bad)

    def test_template_reproduces_and_has_no_admission(self):
        module = load('transport_binding')
        template = module.build_template()
        self.assertEqual(template, json.loads((HERE / 'transport-template.json').read_text()))
        self.assertEqual(len(template['requests']), 32)
        self.assertEqual(len(template['scalar_maps']), 20)
        self.assertIsNone(template['adapter_slots']['complete_source_and_closed_lift'])
        self.assertIsNone(template['adapter_slots']['source_order_identification_or_full_comparison'])
        self.assertEqual(template['adapter_slots']['all_twenty_row_regular_transport_domain']['commit'], NULL)
        self.assertIn('conditional', template['adapter_slots']['all_twenty_row_regular_transport_domain']['scope'])
        for key in ('physical_source_evaluated', 'actual_source_admitted', 'execution_release'):
            self.assertIs(template[key], False)

    def test_declared_frame_conversion_precedes_L(self):
        # Pinned map-and-comparison section 1 requires entries in the same
        # original frame before applying L. No commute/defer proof is supplied.
        template = load('transport_binding').build_template()
        for request in template['requests']:
            order = request['operator_order']
            conversion = 'original_frame_full_sign_deck_conversion_once'
            self.assertEqual(order.count(conversion), 1)
            self.assertLess(order.index(conversion), order.index('scalar_L_on_J2'),
                            'source pin requires original-frame conversion before L')


if __name__ == '__main__':
    unittest.main(verbosity=2)
