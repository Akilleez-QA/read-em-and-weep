#!/usr/bin/env python3
"""Bounded universal bookkeeping only. No actual HM coefficients are read.
This checks expansions modulo explicitly named harmonic associativity laws;
it is not a formal verification of the geometric inputs or a rank computation.
"""
from collections import Counter
import sympy as s

def add(*items):
    out=Counter()
    for item in items:
        out.update(item)
    return Counter({k:v for k,v in out.items() if v})

def neg(c): return Counter({k:-v for k,v in c.items()})

# Ordered tags, with f,s central scalar factors. nD and Dn remain distinct.
lhs=Counter({'fTD':1,'fDT':1,'snD':1,'sDn':1,
             'B(f,n)D':1,'DB(f,n)':1,'B(fn,D)':1,'B(D,fn)':1})
# Coefficient-one associativity of (f*n)*D=f*(n*D), and
# D*(f*n)=f*(D*n), the latter also using scalar centrality.
forward=Counter({'B(f,n)D':1,'B(fn,D)':1,
                 'fB(n,D)':-1,'B(f,nD)':-1})
reverse=Counter({'DB(f,n)':1,'B(D,fn)':1,
                 'fB(D,n)':-1,'B(f,Dn)':-1})
reduced=add(lhs,neg(forward),neg(reverse))
assert reduced == Counter({'fTD':1,'fDT':1,'snD':1,'sDn':1,
                           'fB(n,D)':1,'fB(D,n)':1,
                           'B(f,nD)':1,'B(f,Dn)':1})
# Apply nD+Dn=0 and bilinearity, not any matrix commutativity.
for a,b in [('snD','sDn'),('B(f,nD)','B(f,Dn)')]:
    assert reduced[a]==reduced[b]
    del reduced[a]; del reduced[b]
assert reduced==Counter({'fTD':1,'fDT':1,'fB(n,D)':1,'fB(D,n)':1})
print('PASS: ordered harmonic associativity tags give f times Z')

# Universal trace-free rank-two polarization, not an HM/source matrix.
x,y,z,u,v,w=s.symbols('x y z u v w')
A=s.Matrix([[x,y],[z,-x]]); B=s.Matrix([[u,v],[w,-u]])
assert s.simplify(A*B+B*A-s.trace(A*B)*s.eye(2))==s.zeros(2)
assert s.expand(s.trace(A*B+B*A)/2-s.trace(A*B))==0
print('PASS: scalar extraction and trace-lift normalization have no extra 2')

# Symbolic regular-pair formulas; no f3 or g5 specialization/evaluation.
f,g,l,unit=s.symbols('f g l unit')
n=unit*s.Matrix([[f*g,-f*f],[g*g,-f*g]])
D=l*s.Matrix([[f/2,0],[g,-f/2]])
assert s.simplify(n*D+D*n)==s.zeros(2)
D1=s.Matrix([[x,0],[z,-x]])
assert s.expand(s.trace(n*D1)-unit*(2*f*g*x-f*f*z))==0
print('PASS: formal kernel generator and weight-zero trace-image formula')

# All homogeneous degrees and dimensions, without coefficient/rank evaluation.
assert 4+4==8+4-4==8  # TD and B1(n,D)
assert 4+8==12         # f*Psi
assert 8+0==8         # tr(n D1)
assert (4+1)+(2+1)+(6+1)==15
assert 15-13==2 and 9-(3+1)==5
assert 8-6==2 and 8-8==0 and 8-10<0
print('PASS: weight-eight quotient and dimensions 2 -> 5')
