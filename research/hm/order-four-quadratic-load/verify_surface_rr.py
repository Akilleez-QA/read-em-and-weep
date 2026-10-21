"""Exact formal RR certificate; no HM coefficients or selected evaluations.
Run: python verify_surface_rr.py
Polynomials are truncated in h at degree four, over rational coefficients.
"""
from fractions import Fraction as Q
from math import factorial, comb

def add(*ps):
    return [sum((p[i] for p in ps), Q(0)) for i in range(5)]
def scale(p,a): return [a*x for x in p]
def mul(p,q):
    return [sum((p[j]*q[i-j] for j in range(i+1)),Q(0)) for i in range(5)]
def exp(a): return [Q(a**i,factorial(i)) for i in range(5)]
def rr(p): return mul(p,[Q(1),Q(5,2),Q(35,12),Q(25,12),Q(1)])[4]

E=[Q(2),Q(5),Q(5,2),Q(-25,6),Q(-175,24)]
OX=add(exp(0),scale(exp(-5),-3),mul(E,exp(-10)))
assert OX == [0,0,Q(15),Q(-50),Q(325,4)]
for n in range(-20,21):
    value=rr(mul(OX,exp(n)))
    assert value == Q(15*n*n-25*n,2)
    # Independent K-class expression from the exact sequence.
    ambient=Q(comb(n+4,4)) if n>=0 else Q((n+4)*(n+3)*(n+2)*(n+1),24)
    line=Q((n-1)*(n-2)*(n-3)*(n-4),24)
    assert value == ambient-3*line+rr(mul(E,exp(n-10)))
    section=value-rr(mul(OX,exp(n-1)))
    assert section == 15*n-20
assert rr(OX)==0
print('PASS: ch(O_X)=15h^2-50h^3+(325/4)h^4')
print('PASS: chi(O_X(n))=(15n^2-25n)/2 for formal degree-two polynomial')
print('PASS: 41 exact twist checks and independent K-class identities')
print('PASS: sectional polynomial 15n-20, arithmetic genus 21; chi(O_X)=0')
print('Scope: certifies arithmetic under the stated resolution, not its geometric hypotheses.')
