"""Tiny occurrence-vector checks only; no physical source objects or evaluation."""
import json

def d(v):
    rows = [v[:i] + (0,) + v[i:] for i in range(len(v)+1)]
    return tuple(max(r[i] for r in rows) for i in range(len(v)+1))

def h(v):
    return (v[0]+4,) + v[1:]

def require(actual, expected):
    if actual != expected:
        raise ValueError((actual, expected))

N = ((35,24,5), (12,12,3))
primitive = (h(d(N[0])), d(N[1]))
require(primitive, ((39,35,24,5),(12,12,12,3)))
E = ((27,24,5), (9,10,3))
selected = (h(d(h(d(E[0])))), d(d(E[1])))
require(selected, ((35,31,27,24,5),(9,10,10,10,3)))
for c,l in (primitive,selected):
    if max(c)>54 or max(l)>29:
        raise ValueError('Fixed comparison weights do not clear the bound')
if d((3,7)) != (3,7,7):
    raise ValueError('Omitted-slot ownership rule changed')
print(json.dumps({'status':'pass','primitive':primitive,'selected':selected,
                  'scope':'integer occurrence vectors only'},sort_keys=True))
