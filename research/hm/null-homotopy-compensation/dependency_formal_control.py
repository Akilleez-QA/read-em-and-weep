"""Free-word sign controls only. No physical data, matrices, or production imports."""
from collections import defaultdict

# a = target Cech differential; b = source scalar Cech differential;
# c = row Cech differential; F = differentiated prism; P = partition;
# U = coefficient derivative of P; T = degree-two transfer; Q = overlap map.
def reduce(poly):
    out = defaultdict(int)
    todo = list(poly.items())
    rules = {
        ('a','P'): [(1,('P','b'))],
        ('T','c'): [(1,('b','T'))],
        ('a','F'): [(1,('U',)),(-1,('F','b'))],
    }
    while todo:
        word, coeff = todo.pop()
        for i in range(len(word)-1):
            rhs = rules.get(word[i:i+2])
            if rhs is not None:
                for sign, part in rhs:
                    todo.append((word[:i]+part+word[i+2:], coeff*sign))
                break
        else:
            out[word] += coeff
    return {w:c for w,c in out.items() if c}

def diff(a,b):
    result = defaultdict(int, a)
    for w,c in b.items(): result[w] -= c
    return reduce(result)

def require(ok, message):
    if not ok: raise RuntimeError(message)

right = {('U','T'):1, ('P','b','Q'):-1, ('P','Q','c'):-1}
left = {('a','F','T'):1, ('a','P','Q'):-1,
        ('F','T','c'):1, ('P','Q','c'):-1}
require(not diff(left,right), 'Hom differential identity failed')
mutations = {
    'wrong K inner sign': {('a','F','T'):1,('a','P','Q'):1,('F','T','c'):1,('P','Q','c'):1},
    'wrong Hom differential sign': {('a','F','T'):1,('a','P','Q'):-1,('F','T','c'):-1,('P','Q','c'):1},
    'omit outer nonclosed term': {('a','F','T'):1,('a','P','Q'):-1,('P','Q','c'):-1},
    'omit inner nonclosed term': {('a','F','T'):1,('a','P','Q'):-1,('F','T','c'):1},
    'omit inner boundary': {('a','F','T'):1,('F','T','c'):1,('P','Q','c'):-1},
    'omit outer boundary': {('a','P','Q'):-1,('F','T','c'):1,('P','Q','c'):-1},
}
for name, mutation in mutations.items():
    residual = diff(mutation,right)
    require(bool(residual), 'undetected mutation: '+name)
    print(name+': '+str(sorted(residual.items())))
print('PASS: one operator identity; six omission/sign mutations distinguished')
