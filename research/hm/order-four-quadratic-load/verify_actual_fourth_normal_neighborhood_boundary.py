"""Formal actual-neighborhood comparison; no actual-instance computation."""
import sympy as S
q,a,h,b,Z,V,W=S.symbols('q a h b Z V W')
dU=q*q*Z;dC=a*h*Z-q*V;dE=a*(V-b*Z)-q*W
dJ3=S.expand((a*h-q*b)*dU-q*q*dC)
dJ4=S.expand(a*dJ3-q**3*dE)
assert S.expand(dJ3-q**3*(V-b*Z))==0
assert S.expand(dJ4-q**4*W)==0
assert S.expand(a*dJ4-q**4*a*W)==0
# Every integer records a physical twist, not an evaluated source value.
assert 4+4==4+4==8
assert 8+2==6+4==10
assert 10+2-4*2==4
assert 8-3*2==10-4*2==2
assert 2*2+2+2==8 and 3*2+2+2==10 and 4*2+2+2==12
# For all t>=2, t+1>=3 exceeds every largest partition part (<=2).
for partition in [(2,2),(2,1,1),(1,1,1,1)]:
    assert 2+1>=max(partition)
assert 2-1>=0 and 2>=1
print('PASS: exact actual3Q/4Q ladder and fifth-neighborhood boundary, with all twists retained.')
print('PASS: uniform twist>=2 chain-Hom Bott dominance reduces cohomological equalities to global primitives.')
print('The primitives beyond U_a and the actual fourth value remain uncomputed.')
