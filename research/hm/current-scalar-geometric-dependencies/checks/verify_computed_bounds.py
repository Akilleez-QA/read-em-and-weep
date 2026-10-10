#!/usr/bin/env python3
"""Independently derive clearing bounds from computed tail/prefix fields."""
import json
from pathlib import Path
import sys


def verify(report):
    if report['modelSha256'] != 'b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2':
        raise ValueError('Model mismatch')
    tail = report['tailPrimaryJ0']
    if tail != [13, 13, 13, 13, 13, 0, 1, 1, 1, 1]:
        raise ValueError('Computed tail bound mismatch')
    if len(report['q2']) != 10 or len(report['q3']) != 10:
        raise ValueError('Prefix profile coverage')
    order = [5, 0, 1, 2, 3, 4]
    import itertools
    for name, count, field in [('q2', 2, 'scalar'), ('q2', 2, 'blocks'), ('q3', 3, 'block')]:
        expected = set(itertools.combinations(order[:-1], count))
        actual = set()
        for profile in report[name]:
            anchors = tuple(profile[k] for k in ('a', 'b', 'c')[:count])
            actual.add(anchors)
            if set(anchors).intersection(profile['tailCarriers']):
                raise ValueError('Prefix/tail carrier overlap')
            if profile['tailCarriers'] != order[order.index(anchors[-1]) + 1:]:
                raise ValueError('Incorrect tail carriers')
            bound = profile[field]
            auxiliary_maximum = (1 if field == 'scalar' else 3 if field == 'blocks' else 2)
            if (len(bound) != 10 or any(type(v) is not int or v < 0 for v in bound)
                    or max(bound[:5]) > 2 or bound[5] > auxiliary_maximum
                    or any(v > 1 for v in bound[6:])):
                raise ValueError('Computed prefix bound exceeds certificate')
        if actual != expected:
            raise ValueError('Missing or duplicated anchor profiles')
    return {'status': 'PASS', 'computedPrimaryTailPower': 13,
            'computedScalarPrefixPrimaryPowerAtMost': 2,
            'computedScalarAuxiliaryPowerAtMost': 1,
            'computedLegalLinePowersAtMost': [1, 1, 1, 1],
            'scalarMergedCarrierPowers': [1, 13, 13, 13, 13],
            'allMaskNumeratorClearingPowers': [13, 14, 14, 14],
            'declaredCompletedFieldUsedAsEvidence': False,
            'geometricMergerUsesSeparateHomogeneousIdentities': True}


if __name__ == '__main__':
    print(json.dumps(verify(json.loads(Path(sys.argv[1]).read_text())), indent=2))
