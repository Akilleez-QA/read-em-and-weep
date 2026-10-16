import copy
import unittest
from schedule_validator import validate, COUNTERS


def c(n=0):
    return dict(zip(COUNTERS, (n, 0, 0, 0, 0)))


def fixture():
    return {'schema': 'a06-global-schedule-v1', 'evidence': 'synthetic-only',
            'ledger_id': 'one-global-ledger', 'revision': 1, 'global_complete': True,
            'source_pin': 'synthetic:no-physical-source',
            'caps': {'counts': c(10), 'bytes': 20, 'metric': 'synthetic-live-plus-workspace-bytes'},
            'spent': c(3),
            'reservations': [
                {'id': 'A', 'owner': 'workerA', 'remaining': c(2), 'bytes': 0,
                 'first_event': 0, 'last_event': 1, 'authorization': 'synthetic'},
                {'id': 'other', 'owner': 'workerB', 'remaining': c(2), 'bytes': 0,
                 'first_event': 0, 'last_event': 1, 'authorization': 'synthetic'}],
            'allocations': [
                {'id': aid, 'owner': 'global', 'bytes': size, 'initial': initial,
                 'last_use': last, 'reservation': reservation, 'binding': 'synthetic'}
                for aid, size, initial, last, reservation in
                [('other-live', 4, True, -1, None), ('input', 3, True, 1, None),
                 ('other-worker', 6, True, -1, None), ('output', 5, False, 1, 'A')]],
            'operations': [{'id': 'opA', 'owner': 'workerA', 'inputs': ['input'], 'outputs': ['output'],
                            'counts': c(2), 'workspace': 2, 'reservation': 'A', 'source_binding': 'synthetic'}],
            'events': [{'begin': ['opA'], 'end': [], 'free': []},
                       {'begin': [], 'end': ['opA'], 'free': ['input']}]}


class Controls(unittest.TestCase):
    def test_output_before_free_and_no_refund(self):
        out = validate(fixture())
        self.assertEqual(out['peak_charged_bytes'], 20)
        self.assertEqual(out['spent_after']['products'], 5)
        self.assertEqual(out['remaining_reservations']['A']['products'], 0)
        self.assertFalse(out['arithmetic_admission'])

    def reject(self, mutate):
        f = fixture(); mutate(f)
        with self.assertRaises(ValueError): validate(f)

    def test_caps(self):
        self.reject(lambda f: f['caps'].update(bytes=19))
        self.reject(lambda f: f['caps']['counts'].update(products=6))

    def test_unknowns_and_booleans(self):
        self.reject(lambda f: f['operations'][0]['counts'].update(products=None))
        self.reject(lambda f: f['operations'][0]['counts'].update(products=True))
        self.reject(lambda f: f['allocations'][0].update(bytes=None))
        self.reject(lambda f: f['operations'][0].update(source_binding=None))
        self.reject(lambda f: f.update(global_complete=False))
        self.reject(lambda f: f.update(guessed_occupancy=0))

    def test_duplicate_global_ids(self):
        self.reject(lambda f: f['allocations'].append(copy.deepcopy(f['allocations'][0])))
        self.reject(lambda f: f['reservations'].append(copy.deepcopy(f['reservations'][0])))

    def test_last_use(self):
        self.reject(lambda f: f['allocations'][1].update(last_use=0))
        self.reject(lambda f: f['events'][0]['free'].append('input'))

    def test_reservation_and_binding(self):
        self.reject(lambda f: f['operations'][0]['counts'].update(products=3))
        self.reject(lambda f: f['reservations'][0].update(last_event=0))
        self.reject(lambda f: f.update(evidence='physical'))

    def test_unbacked_commitment(self):
        self.reject(lambda f: f['reservations'][1].update(bytes=7))
        f = fixture(); f['reservations'][0]['bytes'] = 7
        self.assertEqual(validate(f)['peak_charged_bytes'], 20)  # output5 + workspace2 back7 once

    def test_concurrency(self):
        f = fixture()
        f['allocations'].append({'id': 'outB', 'owner': 'B', 'bytes': 1, 'initial': False,
                                 'last_use': 1, 'reservation': 'other', 'binding': 'synthetic'})
        f['operations'].append({'id': 'opB', 'owner': 'B', 'inputs': ['other-worker'],
                                'outputs': ['outB'], 'counts': c(2), 'workspace': 1,
                                'reservation': 'other', 'source_binding': 'synthetic'})
        f['allocations'][2]['last_use'] = 1
        f['events'][0]['begin'].append('opB'); f['events'][1]['end'].append('opB')
        with self.assertRaises(ValueError): validate(f)
        f['caps']['bytes'] = 22
        self.assertEqual(validate(f)['peak_charged_bytes'], 22)

    def test_shared_ids_count_once(self):
        f = fixture(); f['operations'][0]['inputs'].append('other-live')
        f['allocations'][0]['last_use'] = 1
        self.assertEqual(validate(f)['peak_charged_bytes'], 20)

    def test_reservations_are_not_spent_or_worker_caps(self):
        f = fixture(); f['reservations'][1]['remaining'] = c(6)
        with self.assertRaises(ValueError): validate(f)  # 3+2+6 exceeds10, not a fresh worker cap

    def test_missing_or_unfinished_output(self):
        self.reject(lambda f: f['events'][1]['end'].clear())
        self.reject(lambda f: f['operations'][0]['outputs'].clear())

    def test_input_completion(self):
        f = fixture()
        f['operations'][0]['inputs'] = ['output']
        with self.assertRaises(ValueError): validate(f)


if __name__ == '__main__':
    unittest.main()
