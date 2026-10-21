"""Universal binary and jet identities; no actual HM coefficients or rank tests."""
from sympy import symbols, diff, expand, factorial, binomial, simplify
x,y,a,b,c,d,h = symbols('x y a b c d h')
ell=a*x+b*y
w=c*x+d*y
f=ell**4
g=ell**3*w
for n in (2,4):
    tv=sum((-1)**i*binomial(n,i)*diff(f,x,n-i,y,i)*diff(g,x,i,y,n-i) for i in range(n+1))
    assert expand(tv)==0
print('PASS: residual square products have zero second and fourth transvectants.')
assert expand(f*g-ell**7*w)==0
assert expand((f*g).subs({c:a,d:b})-ell**8)==0
print('PASS: Cartan multiplication and pure-eighth-power spanning identity.')
B=symbols('B0:8'); W0,W1=symbols('W0 W1')
series=sum(B[i]*h**i/factorial(i) for i in range(8))
F=expand(series*(W0+h*W1))
quot=expand((F-F.coeff(h,0)-h*F.coeff(h,1))/h**2)
expected=B[2]*W0/2+B[1]*W1+h*(B[3]*W0/6+B[2]*W1/2)
assert expand(quot-expected).coeff(h,0)==0
assert expand(quot-expected).coeff(h,1)==0
print('PASS: residual double-root quotient retains the second and third jets.')
# Numerical statements below are representation dimensions, not map ranks.
assert 3*3==1+3+5
assert 4*5//2==10
assert 2+4==6 and 4+8==12
allowed=[r for r in range(1,5) if (-1)**r==1]
assert allowed==[2,4]
assert [6-(2+r) for r in allowed]==[2,0]
print('PASS: character dimensions and determinant-parity alternatives are {2,4}.')
print('PASS: all checks are universal identities; no actual source evaluation was used.')
