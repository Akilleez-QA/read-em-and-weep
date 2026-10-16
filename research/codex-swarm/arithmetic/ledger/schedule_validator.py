"""Metadata-only global schedule replay. No execution authorization is emitted.
Only synthetic evidence is supported; physical certificates require later review.
"""
COUNTERS = ('products', 'coefficient_multiplications', 'additions', 'exact_divisions', 'reductions')


def need(ok, message):
    if not ok:
        raise ValueError(message)


def fields(record, names):
    need(type(record) is dict and set(record) == set(names.split()), 'unknown/missing fields: ' + names)


def nat(value):
    need(type(value) is int and value >= 0, 'unknown/noninteger/negative physical count or byte bound')
    return value


def ident(value):
    need(type(value) is str and bool(value), 'missing identifier/source binding')
    return value


def counts(record):
    fields(record, ' '.join(COUNTERS))
    return {k: nat(record[k]) for k in COUNTERS}


def ids(values):
    need(type(values) is list, 'ID list required')
    for value in values:
        ident(value)
    need(len(set(values)) == len(values), 'duplicate IDs')
    return set(values)


def validate(record):
    fields(record, 'schema evidence ledger_id revision global_complete source_pin caps spent reservations allocations operations events')
    need(record['schema'] == 'a06-global-schedule-v1', 'unsupported schema')
    need(record['evidence'] == 'synthetic-only', 'physical proof bindings unsupported; admission closed')
    need(record['global_complete'] is True, 'unreconciled global state')
    ident(record['ledger_id']); nat(record['revision'])
    need(record['source_pin'] == 'synthetic:no-physical-source', 'unknown source binding')
    fields(record['caps'], 'counts bytes metric')
    need(record['caps']['metric'] == 'synthetic-live-plus-workspace-bytes', 'unsupported byte metric')
    cap, byte_cap = counts(record['caps']['counts']), nat(record['caps']['bytes'])
    spent = counts(record['spent'])
    for name in ('reservations', 'allocations', 'operations', 'events'):
        need(type(record[name]) is list and len(record[name]) <= 4096, 'bounded metadata lists required')
    need(bool(record['events']), 'nonempty event schedule required')
    reservations, allocs, ops = {}, {}, {}
    for r in record['reservations']:
        fields(r, 'id owner remaining bytes first_event last_event authorization')
        rid = ident(r['id']); need(rid not in reservations, 'duplicate reservation')
        ident(r['owner']); need(r['authorization'] == 'synthetic', 'unknown reservation binding')
        counts(r['remaining']); nat(r['bytes']); nat(r['first_event']); nat(r['last_event'])
        need(r['first_event'] <= r['last_event'] < len(record['events']), 'reservation interval')
        reservations[rid] = r
    for a in record['allocations']:
        fields(a, 'id owner bytes initial last_use reservation binding')
        aid = ident(a['id']); need(aid not in allocs, 'duplicate global allocation')
        ident(a['owner']); nat(a['bytes'])
        need(type(a['initial']) is bool, 'initial flag')
        need(type(a['last_use']) is int and a['last_use'] >= -1, 'last use')
        need(a['reservation'] is None or a['reservation'] in reservations, 'allocation reservation')
        need(a['binding'] == 'synthetic', 'unknown allocation byte/source proof')
        allocs[aid] = a
    producers = {}
    for o in record['operations']:
        fields(o, 'id owner inputs outputs counts workspace reservation source_binding')
        oid = ident(o['id']); need(oid not in ops, 'duplicate operation')
        ident(o['owner']); ins, outs = ids(o['inputs']), ids(o['outputs'])
        need(not ins & outs and ins | outs <= allocs.keys(), 'unknown/in-place allocation')
        need(o['source_binding'] == 'synthetic', 'unknown operation source binding')
        counts(o['counts']); nat(o['workspace'])
        need(o['reservation'] in reservations, 'operation reservation required')
        for aid in outs:
            need(aid not in producers and not allocs[aid]['initial'], 'output ID reused')
            need(allocs[aid]['reservation'] == o['reservation'], 'output backing reservation mismatch')
            producers[aid] = oid
        ops[oid] = o
    need(set(producers) == {a for a in allocs if not allocs[a]['initial']}, 'unproduced allocation')
    begins, ends, frees = {}, {}, {}
    for i, e in enumerate(record['events']):
        fields(e, 'begin end free')
        for key, table, universe in [('begin', begins, ops), ('end', ends, ops), ('free', frees, allocs)]:
            for obj in ids(e[key]):
                need(obj in universe and obj not in table, 'unknown or repeated event ID')
                table[obj] = i
    need(begins.keys() == ends.keys() == ops.keys(), 'operation schedule incomplete')
    for oid, o in ops.items():
        need(begins[oid] < ends[oid], 'operation must end after begin')
        r = reservations[o['reservation']]
        need(r['first_event'] <= begins[oid] <= ends[oid] <= r['last_event'], 'reservation expired')
        for aid in o['inputs']:
            if aid in producers:
                need(ends[producers[aid]] < begins[oid], 'input unavailable before output completion')
    for aid, a in allocs.items():
        uses = [ends[o] for o in ops if aid in ops[o]['inputs'] or aid in ops[o]['outputs']]
        need(a['last_use'] == max(uses, default=-1), 'incorrect last use')
        if aid in frees:
            need(frees[aid] >= a['last_use'], 'free before last use')
    # Replace each used reservation by certified candidate remaining cost once.
    planned = {r: {k: 0 for k in COUNTERS} for r in reservations}
    for o in ops.values():
        for k in COUNTERS:
            planned[o['reservation']][k] += o['counts'][k]
    remaining = {r: dict(reservations[r]['remaining']) for r in reservations}
    for r in reservations:
        for k in COUNTERS:
            need(planned[r][k] <= remaining[r][k], 'reservation overrun')
    # Unused allowance stays reserved; no worker receives a fresh global cap.
    for k in COUNTERS:
        need(spent[k] + sum(remaining[r][k] for r in remaining) <= cap[k], 'global count cap')
    live = {a for a in allocs if allocs[a]['initial']}
    active, completed = set(), set()
    peak, trace = 0, []

    def charge(i):
        nonlocal peak
        live_bytes = sum(allocs[a]['bytes'] for a in live)
        workspace = sum(ops[o]['workspace'] for o in active)
        unbacked = 0
        for rid, r in reservations.items():
            if r['first_event'] <= i <= r['last_event']:
                backing = sum(allocs[a]['bytes'] for a in live if allocs[a]['reservation'] == rid)
                backing += sum(ops[o]['workspace'] for o in active if ops[o]['reservation'] == rid)
                unbacked += max(0, r['bytes'] - backing)
        total = live_bytes + workspace + unbacked
        need(total <= byte_cap, 'global byte cap (outputs before frees)')
        peak = max(peak, total)
        trace.append({'event': i, 'live_bytes': live_bytes, 'workspace': workspace,
                      'unbacked_commitments': unbacked, 'charged_bytes': total})
    charge(-1)
    for i, e in enumerate(record['events']):
        for oid in e['begin']:
            o = ops[oid]
            need(set(o['inputs']) <= live, 'freed/missing input')
            need(not set(o['outputs']) & live, 'output overwrite')
            live.update(o['outputs']); active.add(oid)
            for k in COUNTERS:
                spent[k] += o['counts'][k]
                remaining[o['reservation']][k] -= o['counts'][k]
                need(spent[k] + sum(r[k] for r in remaining.values()) <= cap[k], 'global count cap')
        charge(i)  # New outputs and all concurrent workspaces precede end/free.
        for oid in e['end']:
            need(oid in active, 'end without active operation')
            active.remove(oid); completed.add(oid)
        for aid in e['free']:
            need(aid in live, 'free absent allocation')
            need(not any(aid in ops[o]['inputs'] + ops[o]['outputs'] for o in active), 'free while active')
            live.remove(aid)
    need(not active and completed == ops.keys(), 'unfinished operations')
    return {'release_pin': '6e28c6b59f8245779f6c03a20798e4de6842ae19',
            'source_pin': '08b73637d4136f91606aad332c46cafd064417f8',
            'domain': 'finite integer/Boolean synthetic global ledger only; no physical source operations',
            'evidence': 'event replay with explicit global IDs, reservations, costs and byte bounds',
            'reviewer': ['Codex-V06', 'Codex-I01'], 'artifact_review': 'pending',
            'gap': 'physical source/pole/cost proof authentication unsupported; actual global state unavailable',
            'next_step': 'review controls and supply authenticated global state and operation costs',
            'actual_source_admitted': False, 'source_pole_domain_proved': False,
            'synthetic_schedule_consistent': True, 'arithmetic_admission': False,
            'execution_release': False, 'peak_charged_bytes': peak, 'spent_after': spent,
            'remaining_reservations': remaining, 'live_after': sorted(live), 'trace': trace}
