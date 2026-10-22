"""Universal character obstruction for the actual degree-zero quotient.

No selected HM coefficients or actual multiplication matrix/rank are used.
The actual target character is a proved source input; this checks its
comparison with the universal tensor-product source, not that source proof.
"""
from fractions import Fraction as F

# Exact arithmetic in Q(sqrt(5)); nine binary-A5 conjugacy classes.
def z(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def seq_sum(xs):
    out=z(0)
    for x in xs: out=add(out,x)
    return out
phi=z(F(1,2),F(1,2)); phip=z(F(1,2),F(-1,2))
tr=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n,x):
    if n==0: return z(1)
    a,b=z(1),x
    for _ in range(2,n+1): a,b=b,sub(mul(x,b),a)
    return b
def inner(a,b): return scale(F(1,120),seq_sum(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
def vadd(*args): return [seq_sum(v) for v in zip(*args)]
def vmul(a,b): return [mul(x,y) for x,y in zip(a,b)]
def vscale(k,a): return [scale(k,x) for x in a]
W=tr; A=[sym(2,x) for x in tr]; S=[sym(3,x) for x in tr]
T=[sym(5,x) for x in tr]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=[sub(sym(6,x),p) for x,p in zip(tr,P)]
Wp=[sub(mul(w,p),t) for w,p,t in zip(W,P,T)]
for chi in (W,Wp,A,V,S,T): assert inner(chi,chi)==z(1)
assert inner(A,V)==z(0)
source = vmul(vmul(A,V),T)
target = vadd(vscale(3,Wp),vscale(3,S),vscale(6,T))
expected_source = vadd(vscale(2,W),vscale(2,Wp),vscale(4,S),vscale(5,T))
assert source == expected_source
assert source[0] == target[0] == z(54)
forced_kernel = vadd(vscale(2,W),S)
forced_cokernel = vadd(Wp,T)
assert forced_kernel[0] == forced_cokernel[0] == z(8)
assert vadd(source,vscale(-1,target)) == vadd(forced_kernel,vscale(-1,forced_cokernel))
for chi,mult in [(W,2),(Wp,2),(S,4),(T,5)]:
    assert inner(chi,source) == z(mult)
print('PASS: A tensor V tensor Sym5W = 2W + 2Wprime + 4Sym3W + 5Sym5W.')
print('PASS: target 3Wprime + 3Sym3W + 6Sym5W forces kernel 2W+Sym3W and cokernel Wprime+Sym5W.')
print('PASS: both forced dimensions are eight; the degree-zero quotient cannot be trivial.')
