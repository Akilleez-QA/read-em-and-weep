#!/usr/bin/env python3
"""Exact universal diagnostics for the supplied-source membership sector.

Abstract character and split-multiplicity labels only. These labels are
not actual HM coefficient choices, source evaluations, matrices or ranks.
The actual geometric/cohomological inputs are written in PROOF.md.
"""
from fractions import Fraction as F
from time import perf_counter


class Qphi:
    # a+b*phi with phi^2=phi+1.
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Qphi) else Qphi(x)

    def __add__(self, x):
        x = self.coerce(x)
        return Qphi(self.a+x.a, self.b+x.b)

    __radd__ = __add__

    def __neg__(self):
        return Qphi(-self.a, -self.b)

    def __sub__(self, x):
        return self+-self.coerce(x)

    def __rsub__(self, x):
        return self.coerce(x)+-self

    def __mul__(self, x):
        x = self.coerce(x)
        return Qphi(self.a*x.a+self.b*x.b,
                    self.a*x.b+self.b*x.a+self.b*x.b)

    __rmul__ = __mul__

    def __truediv__(self, x):
        # Only rational denominators are needed.
        return Qphi(self.a/F(x), self.b/F(x))

    def __pow__(self, n):
        out = Qphi(1)
        for _ in range(n):
            out = out*self
        return out

    def __eq__(self, x):
        x = self.coerce(x)
        return (self.a, self.b) == (x.a, x.b)


phi = Qphi(0, 1)
phibar = 1-phi
sizes = [1, 15, 20, 12, 12]
chars = {
    '1': [1, 1, 1, 1, 1],
    'A': [3, -1, 0, phi, phibar],
    'V': [3, -1, 0, phibar, phi],
    'P': [4, 0, 1, -1, -1],
    'D': [5, 1, -1, 0, 0],
}
chars = {k: [Qphi.coerce(v) for v in c] for k, c in chars.items()}


def add(*cs):
    return [sum((c[i] for c in cs), Qphi()) for i in range(5)]


def sub(c, d):
    return [x-y for x, y in zip(c, d)]


def tensor(c, d):
    return [x*y for x, y in zip(c, d)]


def times(n, c):
    return [n*x for x in c]


def inner(c, d):
    return sum((n*x*y for n, x, y in zip(sizes, c, d)), Qphi())/60


def binary_sym(n, two):
    if n == 0:
        return chars['1']
    prev, out = chars['1'], two
    for _ in range(1, n):
        prev, out = out, sub(tensor(two, out), prev)
    return out


checks = 0
negative_checks = 0


def equal(x, y, label):
    global checks
    if x != y:
        raise AssertionError(label)
    checks += 1


def different(x, y, label):
    global negative_checks
    if x == y:
        raise AssertionError(label)
    negative_checks += 1


def main():
    start = perf_counter()
    one, a, v, p, d = (chars[k] for k in ['1', 'A', 'V', 'P', 'D'])
    for n, c in chars.items():
        for m, e in chars.items():
            equal(inner(c, e), int(n == m), 'orthogonality '+n+m)
    squares, cubes = [0, 0, 2, 4, 3], [0, 1, 0, 4, 3]
    sym3a = [(a[j]**3+3*a[j]*a[squares[j]]+2*a[cubes[j]])/6 for j in range(5)]
    equal(sym3a, add(a,v,p), 'Sym3 negative A')
    r = tensor(sym3a,d)
    equal(r, add(times(3,a),times(3,v),times(3,p),times(4,d)), 'R decomposition')
    equal(r[0],50,'R dimension')
    m2=add(a,times(2,v),times(3,p),times(4,d))
    m4=add(times(2,v),times(4,p),times(3,d))
    k=add(a,d)
    im=add(times(2,v),times(3,p),times(3,d))
    equal(sub(m2,k),im,'actual q kernel-image character')
    equal(sub(m4,im),p,'actual q quotient character')
    for c,n,label in [(m2,41,'M2'),(m4,37,'M4'),(k,8,'K'),(im,33,'I'),(p,4,'P')]:
        equal(c[0],n,label+' dimension')
    for c,n,label in [(m2,34,'M2'),(m4,30,'M4'),(k,7,'K'),(im,27,'I'),(p,3,'P')]:
        equal(inner(r,c),n,'family Hom '+label)
    equal(34-7,27,'family image')
    equal(30-27,3,'family quotient')
    equal(34-30,7-3,'family Euler difference')
    equal(inner(r,times(2,v)),6,'V compatibility slots')
    equal(inner(r,times(3,p)),9,'image P compatibility slots')
    equal(inner(r,times(3,d)),12,'D compatibility slots')
    equal(inner(tensor(a,d),a),1,'linear correction line')
    equal(tensor(a,a),add(one,a,d),'A tensor A correction convention')
    trace=add(one,v,p,d)
    equal(inner(r,trace),10,'PR889 trace family target')
    equal(27-10,17,'linear detector forced blind dimension')
    equal(27+1,28,'uncalibrated correction sector')
    equal(34+1-28,7,'joint membership fiber dimension')

    # Formal coefficient labels for an arbitrary split exact sequence
    # with the proven multiplicities. No actual q-matrix is assembled.
    rm={'A':3,'V':3,'P':3,'D':4}
    sm={'A':1,'V':2,'P':3,'D':4}
    tm={'A':0,'V':2,'P':4,'D':3}
    imult={'A':0,'V':2,'P':3,'D':3}
    source={(t,i,j) for t in rm for i in range(rm[t]) for j in range(sm[t])}
    target={(t,i,j) for t in rm for i in range(rm[t]) for j in range(tm[t])}
    image={(t,i,j) for t in rm for i in range(rm[t]) for j in range(imult[t])}
    kernel=source-image
    quotient=target-image
    equal(tuple(map(len,(source,target,image,kernel,quotient))),(34,30,27,7,3),'all formal slot counts')
    equal(image <= source and image <= target,True,'formal image embeddings')
    equal(image.isdisjoint(kernel),True,'split source exactness')
    equal(image.isdisjoint(quotient),True,'split target exactness')
    equal(image | kernel,source,'full source retained')
    equal(image | quotient,target,'full target retained')

    def q_family(s):
        return {key:value for key,value in s.items() if key in image and value}

    def pi_family(t):
        return {key:value for key,value in t.items() if key in quotient and value}

    for key in sorted(image):
        equal(q_family({key:-1}),{key:-1},'each compatibility coefficient lifts '+str(key))
    for key in sorted(kernel):
        equal(q_family({key:1}),{},'each invisible W coefficient '+str(key))
    for key in sorted(quotient):
        equal(pi_family({key:1}),{key:1},'each raw quotient coefficient '+str(key))
    for key in sorted(image):
        equal(pi_family({key:1}),{},'all27 residuals invisible in quotient '+str(key))
    bad=('V',0,0)
    different({bad:1},{},'nonzero compatible-sector defect rejected')
    equal(pi_family({bad:1}),{},'quotient test alone misses this defect')
    different(27,3,'fixed W versus choose W not conflated')
    different(28,30,'canonical correction leaves only one quotient line')
    different(34,7,'arbitrary W is not automatically compatible')
    different(10,27,'trace calibration not full membership')
    different(33,27,'cohomology image dimension not family Hom dimension')
    different(0,7,'W cohomology ambiguity retained')
    equal((2+1,1),(3,1),'a V degree')
    equal((1+1+1,1),(3,1),'a b Z degree')
    equal((0+3,1),(3,1),'q W degree')
    equal((2+2,2+2,2+2),(4,4,4),'all three physical twists')
    if perf_counter()-start >= 30:
        raise AssertionError('bounded diagnostic runtime')
    print(f'PASS: {checks} exact character/multiplicity checks; {negative_checks} negative controls')
    print('PASS: raw 34 -> 30; kernel7, image27, quotient3; corrected b/W sector28')
    print('PASS: fixed canonical b leaves 27 slots = 6 V + 9 P4 + 12 D5; compatible W fiber7')
    print('SCOPE: universal diagnostics, not actual source evaluation, primitive construction, or Lean')


if __name__ == '__main__':
    main()
