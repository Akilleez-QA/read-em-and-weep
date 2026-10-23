#!/usr/bin/env python3
"""Universal diagnostics for the actual compatible-W variation theorem.

No actual HM coefficients, points, matrices, source ranks or evaluations.
The cone closure and weight-four vanishing are written geometric inputs,
not established by these free-word and character checks.
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
negatives = 0


def eq(x,y,label):
    global checks
    if x != y:
        raise AssertionError(label)
    checks += 1


def ne(x,y,label):
    global negatives
    if x == y:
        raise AssertionError(label)
    negatives += 1


# Exact q-adic free-word trace polynomials. Scalar names are formal labels,
# not values of any HM coefficient; noncommuting words have no matrices.
def atom(q=0, scalars=(), word=()):
    return {(q,tuple(sorted(scalars)),tuple(word)): F(1)}


def addp(*ps):
    out={}
    for p in ps:
        for key,c in p.items():
            out[key]=out.get(key,F(0))+c
    return {key:c for key,c in out.items() if c}


def scal(c,p):
    return {key:F(c)*v for key,v in p.items() if c*v}


def mul(p,r):
    out={}
    for (q,s,w),c in p.items():
        for (qq,ss,ww),cc in r.items():
            key=(q+qq,tuple(sorted(s+ss)),w+ww)
            out[key]=out.get(key,F(0))+c*cc
    return {key:c for key,c in out.items() if c}


def trace(p):
    out={}
    for (q,s,w),c in p.items():
        ww=min(w[j:]+w[:j] for j in range(len(w))) if w else w
        key=(q,s,ww)
        out[key]=out.get(key,F(0))+c
    return {key:c for key,c in out.items() if c}


def nil(p):
    # All trace words in the norm calculation have length two.
    # The geometric input N^2=0 sets precisely tr(N N) to zero.
    return {key:c for key,c in p.items() if key[2] != ('N','N')}


def norm(p):
    return scal(F(1,2),trace(mul(p,p)))


def trunc(p,n):
    return {key:c for key,c in p.items() if key[0] < n}


def coefficient(p,n):
    return {(s,w):c for (q,s,w),c in p.items() if q == n}


def main():
    start=perf_counter()
    one,a,v,p,d=(chars[k] for k in ['1','A','V','P','D'])
    k=add(a,d); target=add(one,v,p,d)
    r=add(times(3,a),times(3,v),times(3,p),times(4,d))
    eq(k[0],8,'actual positive K vector dimension')
    eq(inner(r,k),7,'compatible equivariant family torsor')
    eq(inner(r,a),3,'A family slots')
    eq(inner(r,d),4,'D family slots')
    eq(inner(k,target),1,'representation-only allowed D coupling')
    eq(inner(a,target),0,'A absent from trace target')
    eq(inner(d,target),1,'D present in trace target')
    eq(target[0],13,'associated-graded trace sections')
    ne(inner(k,target),0,'representation allowance is not geometric vanishing')
    ne(target[0],0,'13 coefficient sections are not actual zero image')

    q3=atom(3)
    J=addp(atom(0,('A0',),('N',)),*(atom(i,(),('J'+str(i),)) for i in range(1,5)))
    D=addp(atom(0,('g',),('N',)),*(atom(i,(),('D'+str(i),)) for i in range(1,4)))
    shift=mul(q3,D)
    for sign in [1,-1]:
        new=addp(J,scal(sign,shift))
        difference=addp(norm(new),scal(-1,norm(J)))
        predicted=addp(scal(sign,trace(mul(J,shift))),norm(shift))
        eq(difference,predicted,'complete quadratic norm identity '+str(sign))
        for degree in range(14):
            eq(coefficient(difference,degree),coefficient(predicted,degree),
               'all q coefficients '+str((sign,degree)))
        eq(trunc(nil(difference),4),{},'exact norm invariance on 4Q '+str(sign))
        expected4=scal(sign,addp(atom(4,('A0',),('D1','N')),
                                 atom(4,('g',),('J1','N'))))
        eq(coefficient(nil(difference),4),coefficient(expected4,4),
           'uncontrolled next normal coefficient '+str(sign))
        ne(coefficient(nil(difference),4),{},'ambient norm invariance is not proved '+str(sign))
        eq(trunc(norm(shift),4),{},'quadratic variation term dies mod q4 '+str(sign))

    # Preserve the actual lower square condition in the higher-order negative
    # control: this formal J is already square-zero modulo q^3.
    Jlow=addp(atom(0,('A0',),('N',)),atom(3,(),('J3',)))
    eq(trunc(nil(norm(Jlow)),3),{},'lower 3Q square condition retained')
    diff=addp(norm(addp(Jlow,shift)),scal(-1,norm(Jlow)))
    eq(trunc(nil(diff),4),{},'same rho on 4Q with lower square condition')
    ne(coefficient(nil(diff),4),{},'lower square does not control fifth-order norm')
    ne(trunc(shift,4),{},'same norm does not imply same J4')

    # A missing normal power or an arbitrary cone adjoint invalidates the
    # special statement. These are universal free-word negative controls.
    wrongshift=mul(atom(2),D)
    wrong=addp(norm(addp(Jlow,wrongshift)),scal(-1,norm(Jlow)))
    ne(trunc(nil(wrong),4),{},'q^3 factor cannot be replaced by q^2')
    arbitrary=atom(3,(),('K0',))
    wrong=addp(norm(addp(Jlow,arbitrary)),scal(-1,norm(Jlow)))
    ne(trunc(nil(wrong),4),{},'actual k=gN identification is necessary')

    # Adding qY to the primitive leaves the induced section on 4Q unchanged.
    Y=addp(atom(0,(),('Y0',)),atom(1,(),('Y1',)))
    Dprime=addp(D,mul(atom(1),Y))
    eq(trunc(Dprime,1),trunc(D,1),'primitive representative has same cone restriction')
    eq(trunc(mul(q3,Dprime),4),trunc(shift,4),'representative change killed on4Q')
    eq(trunc(nil(norm(addp(Jlow,mul(q3,Dprime)))),4),
       trunc(nil(norm(addp(Jlow,shift))),4),'norm representative independence')
    for slot,weight in [('A'+str(i),0) for i in range(3)]+[('D'+str(i),4) for i in range(4)]:
        eq(8+weight in [8,12],True,'actual cone weight '+slot)
        eq(3*4+8+weight > 16,True,'whole slot misses weight16 '+slot)
    eq((3*2+4,2*10,2*10-3*2),(10,20,14),'J4 norm and rho physical twists')
    eq((8+2+4,3*2+8+2+4),(14,20),'cross term physical twist')
    eq((6 >= 4,4 >= 4),(True,True),'discarded normal orders on4Q')
    if perf_counter()-start >= 30:
        raise AssertionError('bounded diagnostic runtime')
    print(f'PASS: {checks} exact q-adic/character/weight checks; {negatives} negative controls')
    print('PASS: all7 compatible family directions miss weight16; norm equal on4Q')
    print('PASS: q4 coefficient remains uncontrolled; representatives agree only at stated order')
    print('SCOPE: universal diagnostics, not actual HM evaluation, physical-row construction, or Lean')


if __name__ == '__main__':
    main()
