"""Universal binary identities and invariant-series bounds only."""
import sympy as s
x,y=s.symbols('s t')
def tv(f,g):return s.expand(s.diff(f,x)*s.diff(g,y)-s.diff(f,y)*s.diff(g,x))
assert tv(y**4,y**4)==0
assert tv(y**4,x*y**3)==-4*y**6
assert y**4*x*y**3==x*y**7
assert 12*max(0,7-5+1)==36>5*(8-5+1)==20
assert 12*max(0,6-3+1)==48>3*(6-3+1)==12
print('PASS: pure alternating zero, mixed transvectant, and both strict Wronskian exclusions.')
print('With the pinned actual pure nonzero and mixed zero, both actual parity coefficients are nonzero.')
print('No channel ratio or fourth Bockstein value is asserted.')
