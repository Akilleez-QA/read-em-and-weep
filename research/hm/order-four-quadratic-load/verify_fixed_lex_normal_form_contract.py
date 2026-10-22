"""Regression contract for quotient certificates; no geometric instance data.
Run: python verify_fixed_lex_normal_form_contract.py (SymPy).
"""
import sympy as s
from itertools import product
x,y,h,c=s.symbols('x y h c')
F=x*(y+1)
G=s.groebner([F],x,y,order='lex',domain=s.QQ)
def nf(p):
    return G.reduce(s.expand(p))[1]
a,b=x*y**2,x*y
old_a=s.div(a,F,x,y)[1]
old_b=s.div(b,F,x,y)[1]
old_sum=s.div(a+b,F,x,y)[1]
assert s.expand(old_a+old_b-old_sum)!=0
assert nf(a)==x and nf(b)==-x and nf(a+b)==0
samples=[x**i*y**j for i,j in product(range(5),repeat=2)]
for p in samples:
    q,r=G.reduce(p)
    assert s.expand(p-q[0]*F-r)==0
    # LM(F)=xy in lex x>y: no remainder term is divisible by xy.
    assert all(not(i>=1 and j>=1) for (i,j),coef in s.Poly(r,x,y).terms() if coef)
    for z in samples:
        assert nf(p+z)==s.expand(nf(p)+nf(z))
        assert nf(3*p-2*z)==s.expand(3*nf(p)-2*nf(z))
# Parameters are coefficients, not geometric variables; F is independent of them.
Gp=s.groebner([F],x,y,order='lex',domain=s.QQ.poly_ring(h,c))
P=h*a+c*b+h*c*(x**3*y**3+y**2)
R=Gp.reduce(s.expand(P))[1]
for powers in [(1,0),(0,1),(1,1)]:
    i,j=powers
    lhs=s.expand(R).coeff(h,i).coeff(c,j)
    rhs=nf(s.expand(P).coeff(h,i).coeff(c,j))
    assert s.expand(lhs-rhs)==0
print('PASS: nonadditive recursive-remainder counterexample reproduced')
print('PASS: 25 reconstruction/standard-monomial tests; 625 additivity and 625 rational-linearity tests')
print('PASS: 3 parameter-coefficient extraction tests over QQ[h,c], fixed lex x>y')
print('Scope: regression contract only; not certification of any geometric exclusion.')
