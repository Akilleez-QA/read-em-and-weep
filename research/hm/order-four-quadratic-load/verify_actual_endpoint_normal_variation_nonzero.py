"""Aggregate actual endpoint checks; all source parameters stay formal."""
import runpy
from pathlib import Path
import sympy as S
root=Path(__file__).resolve().parent
for name in ('verify_two_endpoint_input_cone_operators.py','verify_endpoint_lowest_vertex_cohomology.py','verify_homogeneous_endpoint_secondary_square_cancellation.py','verify_homogeneous_endpoint_secondary_xy3_nonvanishing.py'):
 runpy.run_path(str(root/name))
X,Y,s,t,A,B,c=S.symbols('X Y s t A B c',nonzero=True)
f=A*X**2*Y*s**3+B*Y**3*s*s*t+A*c*X**3*s*t*t-B*c*X*Y*Y*t**3
H=S.expand(2*(S.diff(f,X,s)*S.diff(f,Y,t)-S.diff(f,X,t)*S.diff(f,Y,s)))
def tv(p,q,r,x,y):
 return S.expand(sum((-1)**j*S.binomial(r,j)*S.diff(p,x,r-j,y,j)*S.diff(q,x,j,y,r-j) for j in range(r+1)))
IX4=tv(H,X**4,4,X,Y);IXY3=tv(H,X*Y**3,4,X,Y)
assert S.expand(IX4-20736*B**2*c*s*t**3)==0
assert S.expand(IXY3-5184*A*B*c*c*t**4)==0
assert tv(t*t,IX4,2,s,t)==0
assert tv(t*t,IXY3,2,s,t)==0
print('PASS: both actual source lines are canonical K inputs, with exact nonzero source-identification constants.')
print('PASS: actual lower endpoint variation has zero mixed-input value and nonzero pure-input value, up to its common nonzero normal scale.')
print('The one-dimensional normal-direction map therefore has zero kernel. No fourth value is asserted.')
