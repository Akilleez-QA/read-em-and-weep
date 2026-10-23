#!/usr/bin/env python3
"""Bounded checks of authenticated inputs and universal bookkeeping only.

This does not evaluate actual HM/source data or prove the geometric inputs.
It checks no actual map, matrix, point, derivative, parameter or instance rank.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def bottleneck(x, y):
    return tuple(min(a, b) for a, b in zip(x, y))


def main():
    manifest = json.loads((ROOT / 'audit-inputs/manifest.json').read_text())
    require(len(manifest) == 6, 'Expected six original inputs')
    for item in manifest:
        data = (ROOT / 'audit-inputs' / item['name']).read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        require(blob == item['blob'], 'Input authentication: ' + item['name'])

    # Ordered irreducible multiplicities A,V,P,D, never actual map entries.
    XF, XB = (0, 1, 1, 2), (1, 1, 2, 2)
    YF, YB, YL = (0, 0, 1, 1), (0, 1, 2, 2), (0, 1, 1, 0)
    image = (0, 2, 3, 3)
    require(sub(add(XF, XB), image) == (1, 0, 0, 1), 'Global kernel')
    require(sub(add(add(YF, YB), YL), image) == (0, 0, 1, 0), 'Global cokernel')
    typeB = add(bottleneck(XF, YF), bottleneck(XB, add(YB, YL)))
    require(typeB[1] == 1 and image[1] == 2, 'Type B V contradiction')
    typeF_F = bottleneck(XF, add(YF, YL))
    typeF_B = bottleneck(XB, YB)
    require(add(typeF_F, typeF_B) == image, 'Type F all bounds saturated')
    require(typeF_B == YB, 'Type F onto B target')
    require(sub(XB, typeF_B) == (1, 0, 0, 0), 'Unique A kernel')

    # In the universal algebra, p=(0,1,d,w) is idempotent iff
    # d*d=d and d*w=w. Over C the first gives d in {0,1};
    # at d=0 the second gives w=0, at d=1 it gives no condition.
    # Coefficients of d(d-1), rather than a numerical search for roots.
    polynomial = [0, 0, 0]
    for i, x in enumerate([0, 1]):
        for j, y in enumerate([-1, 1]):
            polynomial[i+j] += x*y
    require(polynomial == [0, -1, 1], 'Idempotent scalar factorization')
    require(0 - 1 == -1 and 1 - 1 == 0, 'Radical idempotent equation')

    # Polynomial identity for the finite Neumann inverse, with one formal
    # endomorphism symbol E. The leftover is a multiple of t^(n+1).
    for n in range(1, 8):
        inv = [(-1) ** j for j in range(n + 1)]
        product = [0] * (n + 2)
        for j, coefficient in enumerate(inv):
            product[j] += coefficient
            product[j + 1] += coefficient
        require(product[0] == 1 and all(c == 0 for c in product[1:n+1]), 'Formal inverse')
        require(product[n+1] == (-1)**n, 'Formal inverse remainder')

    print('PASS: six exact originals; constituent bottlenecks; universal idempotent and formal-inverse bookkeeping.')
    print('Scope: no actual-instance evaluation; this bounded verifier is not a proof assistant or a replacement for mathematical review.')


if __name__ == '__main__':
    main()
