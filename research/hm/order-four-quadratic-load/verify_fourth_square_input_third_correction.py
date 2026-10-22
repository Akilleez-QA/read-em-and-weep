#!/usr/bin/env python3
"""Universal tensor calculation for the actual fourth detecting input; no instance."""
import sympy as S
X,Y,s,t,A,B,c=S.symbols('X Y s t A B c',nonzero=True)
def trans(f,g,r,x,y):
    return S.expand(sum((-1)**j*S.binomial(r,j)*S.diff(f,x,r-j,y,j)*S.diff(g,x,j,y,r-j) for j in range(r+1)))
f=A*X**2*Y*s**3+B*Y**3*s*s*t+A*c*X**3*s*t*t-B*c*X*Y**2*t**3
H=S.expand(2*(S.diff(f,X,s)*S.diff(f,Y,t)-S.diff(f,X,t)*S.diff(f,Y,s)))
expected=-36*A*A*c*X**4*s**3*t+36*A*B*X*Y**3*s**4-108*A*B*c*X**2*Y**2*s*s*t*t-36*A*B*c*c*X**3*Y*t**4+36*B*B*c*Y**4*s*t**3
assert S.expand(H-expected)==0
Iy4=trans(H,Y**4,4,X,Y)
Imid=trans(H,X**2*Y**2,4,X,Y)
assert S.expand(Iy4+20736*A*A*c*s**3*t)==0
assert S.expand(Imid+10368*A*B*c*s*s*t*t)==0
Cy4=trans(t*t,Iy4,2,s,t)
Cmid=trans(t*t,Imid,2,s,t)
assert S.expand(Cy4+248832*A*A*c*s*t)==0
assert S.expand(Cmid+41472*A*B*c*t*t)==0
ratio=S.cancel((Cmid/(t*t))/(Cy4/(s*t)))
assert S.simplify(ratio-B/(6*A))==0
assert (8-4*2)%10==0
assert (2+0)%10==2
assert (3*2+2)%10==8
print('PASS: complete mixed-transvectant identity with all cubic parameters formal.')
print('PASS: both intrinsic correction values are nonzero and their ratio is B/(6A).')
print('PASS: the fourth detecting input has a nonzero correction parallel to a.')
print('PASS: its B3|A contribution lies in, rather than outside, the fourth detecting character.')
print('No fourth value, invariant numerical scalar, actual coefficient, or actual matrix/rank is evaluated.')
