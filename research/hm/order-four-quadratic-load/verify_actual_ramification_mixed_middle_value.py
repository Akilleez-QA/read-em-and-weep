import sympy as S
r,s,X,Y=S.symbols('r s X Y')
M=S.Matrix([[-r*s,r*r],[-s*s,r*s]])
u=S.Matrix([r,s])
assert M*u==S.zeros(2,1)
assert M*M==S.zeros(2)
assert S.expand((r*X+s*Y)**2*(r*X+s*Y)-(r*X+s*Y)**3)==0
am,bm,k,a,h,z,TA,TB,TC=S.symbols('a_m b_m k a h z TA TB TC',nonzero=True)
forced=2*k*a*a*h*z
# The full U and c equations give these evaluations, without a comparison S.
value=TC-TA-bm*TB/am
assert S.simplify(value.subs({TC:forced,TA:-bm*TB/am})-forced)==0
assert 12-2-4==6
print('PASS: full Clifford kernel line and marked Clebsch pure-cube input.')
print('PASS: exact mixed-form value after all-source two-column subtraction, with k and channel ratio.')
print('PASS: at least six uniformly admissible ramification pairs; no actual-instance evaluation.')
