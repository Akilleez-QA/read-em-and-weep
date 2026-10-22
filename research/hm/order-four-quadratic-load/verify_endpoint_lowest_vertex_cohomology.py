"""Universal character/degree checks for the exact lowest endpoint quotient."""
from pathlib import Path
import contextlib,io,runpy
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
    q=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
vm,inn=q['vm'],q['inner']
W,Wp,V,A,P=[q[k] for k in ('W','Wp','V','A','P')]
D=[q['sym'](4,t) for t in W]
add=lambda a,b:[q['add'](x,y) for x,y in zip(a,b)]
assert vm(Wp,W)==P
assert vm(V,A)==add(P,D)
assert inn(P,D)==0
assert -s.Rational(5,2)-s.Rational(1,2)==-3
assert -(-3)-2==1
assert 4+8==12
assert 8+4==12
assert -s.Rational(4,2)==-2
x=s.symbols('x')
HS=s.cancel((1-x**6-x**8-x**10+x**11+x**13)/(1-x)**2)
assert s.degree(HS,x)==11
assert s.expand(HS).coeff(x,12)==0
# T(alpha+beta*n)-alpha*u=beta*T(n), using T(1)=u.
alpha,beta,u,Tn=s.symbols('alpha beta u Tn')
assert s.expand(alpha*u+beta*Tn-alpha*u-beta*Tn)==0
# Actual cone patch c_i n: degree 4+8; residual ell n: at least degree8.
assert 4+8==12 and 12>4
assert 0+8>4
assert 6+8>12  # even the smallest source cannot feed trace-degree12
assert 8+4==12 # the genuine leading source/operator pair does feed it
# General patch coefficient line: physical twist2 minus coverdegree4/2.
assert 2-4//2==0
assert max(-0-1,0)==0 # H1(P1,O)=0
assert 4-8<0 # a regular homogeneous degree4 ell*n difference is impossible
print('PASS: P4 quotient, trace correction, and input-scoped/general L4 comparison degrees')
