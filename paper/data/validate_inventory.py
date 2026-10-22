#!/usr/bin/env python3
"""Validate local inventories, never sum across universes. Python stdlib only.

Run: python3 paper/data/validate_inventory.py [optional inventory.json]
This is a consistency check, not a proof or realizability certificate.
A future global partition requires mathematical review and a schema revision;
this schema deliberately fails closed on any non-null global total.
"""
import json
from collections import Counter
from pathlib import Path
import sys


def require(test, message):
    if not test:
        raise ValueError(message)


def validate(data):
    universes = data['universes']
    ids = [u['id'] for u in universes]
    require(len(ids) == len(set(ids)), 'Duplicate universe ID')
    by_id = {u['id']: u for u in universes}
    copies = {}
    aliases = {
        'unresolved_rank_three_profiles': ('not_excluded',),
        'compatible_higher_rank_outcomes': ('compatible_goal_satisfying',),
        'formal_extension_classes': ('realized',),
        'unresolved_formal_extension_classes': ('open', 'not_excluded', 'unevaluated'),
        'excluded_loci': ('excluded',),
        'unresolved_bad_cases': ('open', 'not_excluded', 'unevaluated'),
    }
    for universe in universes:
        name = universe['id']
        leaves = universe['leaves']
        local_ids = [leaf['id'] for leaf in leaves]
        require(len(local_ids) == len(set(local_ids)), f'{name}: duplicate leaf ID')
        statuses = Counter()
        for leaf in leaves:
            weight = leaf.get('multiplicity', 1)
            require(type(weight) is int and weight > 0, f'{name}: invalid multiplicity')
            statuses[leaf['status']] += weight
            # Repeated IDs are nested copies, not extra global cases.
            signature = (leaf['status'], weight, leaf.get('dimension'))
            require(leaf['id'] not in copies or copies[leaf['id']] == signature,
                    f'{name}: inconsistent nested copy {leaf["id"]}')
            copies[leaf['id']] = signature
        for key, value in universe.get('counts', {}).items():
            require(type(value) is int and value >= 0, f'{name}: invalid count {key}')
            if key == 'historical_formal_records':
                require(all(type(x.get('historical_formal_record_count')) is int and x['historical_formal_record_count'] >= 0 for x in leaves), f'{name}: missing historical record count')
                expected = sum(x['historical_formal_record_count'] for x in leaves)
                parent_universe = by_id[universe['nested_do_not_add_to']]
                require(expected in parent_universe['records']['record_history'], f'{name}: historical count absent from parent history')
                require(all(x['status'] == 'excluded' and x['formal_record_count'] == 0 for x in leaves), f'{name}: historical eliminated records misreported as current')
            elif key == 'formal_records':
                require(all(type(x.get('formal_record_count')) is int and x['formal_record_count'] >= 0 for x in leaves), f'{name}: missing or invalid leaf record count')
                expected = sum(x['formal_record_count'] for x in leaves)
                parent_universe = by_id[universe['nested_do_not_add_to']]
                require(expected == parent_universe['records']['remaining'], f'{name}: detailed records disagree with parent')
            else:
                expected = sum(statuses.values()) if key == 'total' else sum(
                    statuses[status] for status in aliases.get(key, (key,)))
            require(value == expected, f'{name}: {key}={value}, expected {expected}')
        if 'nested_do_not_add_to' in universe:
            require(universe['nested_do_not_add_to'] in by_id, f'{name}: unknown nesting universe')
        if 'records' in universe:
            records = universe['records']
            require(records['baseline'] == records['removed'] + records['remaining'],
                    f'{name}: record baseline drift')
            require(records['baseline'] >= records['intermediate'] >= records['remaining'] >= 0,
                    f'{name}: record history is not decreasing')
            require(records['remaining'] == records['remaining_defect_zero'] + records['remaining_defect_twelve'],
                    f'{name}: defect counts do not partition remaining records')
            rh = records.get('record_history', [])
            if rh:
                require(rh[0] == records['baseline'] and rh[-1] == records['remaining'], f'{name}: record history endpoints drift')
                require(all(a >= b >= 0 for a,b in zip(rh,rh[1:])), f'{name}: record history increases')
            history = records['pair_history']
            require(history[0] == universe['counts']['total'] and history[-1] == universe['counts']['not_excluded'],
                    f'{name}: pair history disagrees with fixed denominator')
            require(all(a >= b >= 0 for a, b in zip(history, history[1:])), f'{name}: pair history increases')
    # Exact rank-three copies are a subset of the broader rank inventory.
    parent = {leaf['id']: leaf for leaf in by_id['U.GAUSS']['leaves']}
    for leaf in by_id['U.GAUSS3']['leaves']:
        require(leaf['id'] in parent and parent[leaf['id']]['status'] == leaf['status'],
                'Gauss rank-three copy disagrees with parent')
    # Completed subbranches must agree with their named excluded parent case.
    for universe in universes:
        parent_id = universe.get('parent_id')
        if parent_id in copies and universe.get('counts', {}).get('excluded') == universe.get('counts', {}).get('total') and 'total' in universe.get('counts', {}):
            require(copies[parent_id][0] == 'excluded', f'{universe["id"]}: excluded subtree has nonexcluded parent')
    core = data['core_roadmap']
    core_ids = [leaf['id'] for leaf in core['leaves']]
    require(len(core_ids) == len(set(core_ids)), 'Duplicate core objective ID')
    tally = Counter(leaf['status'] for leaf in core['leaves'])
    require(core['total'] == len(core['leaves']), 'Core editorial total drift')
    for status in ('proved', 'open'):
        require(core[status] == tally[status], f'Core {status} count drift')
    require(core['total'] == core['proved'] + core['open'], 'Unexpected core status')
    for field in ('global_geometric_total', 'global_eliminated_total', 'global_remaining_total'):
        require(data[field] is None, f'{field}: no reviewed exhaustive disjoint global partition in this schema')
    return len(universes)


if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('inventory.json')
    try:
        n = validate(json.loads(path.read_text()))
    except (ValueError, KeyError, TypeError) as exc:
        sys.exit(f'FAIL: {exc}')
    print(f'PASS: {n} separately scoped universes; local counts, nesting, record histories and editorial ledger consistent; global totals null.')
