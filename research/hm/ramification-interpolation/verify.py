#!/usr/bin/env python3
"""Bounded universal checks. No actual bicubic coefficients or points."""
import sympy as s

def h0(a,b): return max(a+1,0)*max(b+1,0)
def h1(a,b): return max(-a-1,0)*max(b+1,0)+max(a+1,0)*max(-b-1,0)
def h2(a,b): return max(-a-1,0)*max(-b-1,0)
for n in range(2,21):
    assert h1(2,n-3)==0 and h2(0,n-6)==0
    kernel=2*h0(2,n-3)-h0(0,n-6)+h1(0,n-6)
    assert kernel==5*n-7
    assert h0(4,n)-kernel==12
assert [h1(0,n-6) for n in (2,3,4,5)]==[3,2,1,0]
assert h0(4,0)<12 and h0(4,1)<12
print('PASS: universal P1-product cohomology and exact interpolation dimensions')
# Cech Laurent representatives: H1 O(-4) has exponents -1,-2,-3.
# Multiplication by any degree-d homogeneous section has local exponents 0..d.
for d in (0,1,2):
    target=set(range(-(3-d),0))
    reached={i+j for i in (-1,-2,-3) for j in range(d+1) if i+j in target}
    assert reached==target
print('PASS: universal Cech multiplication fills each low-degree saturation deficit')


# All eight cubic coefficients are algebraically independent.
y,z=s.symbols('y z')
g=s.symbols('g0:4'); h=s.symbols('h0:4')
G=sum(g[i]*y**i for i in range(4)); H=sum(h[i]*y**i for i in range(4))
num=s.expand(G*H.subs(y,z)-H*G.subs(y,z))
B,rem=s.div(num,y-z,y)
assert s.expand(rem)==0
M=s.Matrix(3,3,lambda i,j:s.expand(B).coeff(y,i).coeff(z,j))
assert M==M.T
res=s.resultant(G,H,y)
# Convention-dependent sign fixed by using the affine denominator y-z.
assert s.expand(M.det()+res)==0
assert s.expand((y-z)*B-num)==0
# The identity itself proves scheme vanishing on either homogeneous chart:
# at a common root G=H=0, multiplication by y-z on polynomials in z is injective.
print('PASS: full free-coefficient binary-cubic Bezout identity, symmetry, determinant/resultant')

# A5 character arithmetic, retaining weighted target rather than permutation data.
r=s.sqrt(5); phi=(1+r)/2; psi=(1-r)/2
sizes=[1,15,20,12,12]
A=[3,-1,0,phi,psi]; V=[3,-1,0,psi,phi]
P=[4,0,1,-1,-1]; D=[5,1,-1,0,0]
for i in range(5): assert s.simplify(D[i]*A[i]-A[i]-V[i]-P[i]-D[i])==0
print('PASS: D tensor A = A + V + P + D; weighted quotient V + P + D')
print('No actual coefficients, ramification points, evaluation matrices, or actual-source ranks were used.')
