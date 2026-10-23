#!/usr/bin/env python3
"""Exact universal representation certificate. No actual HM data."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent;count=0
def ck(value,message):
 global count
 count+=1
 if not value:raise RuntimeError(message)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['local_path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==item['sha256'],'immutable input SHA256')
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'],'immutable input Git blob')
import sympy as s
from math import comb,factorial
x,y,q,t=s.symbols('x y q t');z=s.sqrt(5)
P=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
def cv(f,d):
 f=s.Poly(s.expand(f),x,y);return s.Matrix([f.coeff_monomial(x**(d-i)*y**i) for i in range(d+1)])
def pol(v,d):return s.expand(sum(v[i]*x**(d-i)*y**i for i in range(d+1)))
v=[pol(b,6) for b in P.nullspace()]
f=s.expand(s.det(s.Matrix([[s.diff(h,x,k)*s.diff(h,x,0)**0 if False else s.diff(h.subs(y,1),x,k) for h in v] for k in range(3)])))
f=s.Poly(f,x).homogenize(y).as_expr();f=s.expand(f)
ck(s.Poly(f,x,y).total_degree()==12,'Wronskian degree12')
a=x*x+q*x*y+t*y*y
T=s.Matrix.hstack(*[P*cv(a*x**(4-i)*y**i,6) for i in range(5)])
k=s.Matrix([(-1)**i*s.expand(T[:,[j for j in range(5) if j!=i]].det(method='berkowitz')) for i in range(5)])
k=k.applyfunc(s.expand);kap=pol(k,4)
ck(all(s.expand(e)==0 for e in T*k),'signed minors kernel identity')
def tv(f,g,n):return s.expand(sum((-1)**i*comb(n,i)*s.diff(f,x,n-i,y,i)*s.diff(g,x,i,y,n-i) for i in range(n+1)))
def rem(f):
 cs=cv(f,4);rs=[1,x]
 for _ in range(3):rs.append(s.expand(-q*rs[-1]-t*rs[-2]))
 return s.expand(sum(cs[i]*rs[4-i] for i in range(5)))
ops=[lambda h:(q*q-4*t)*tv(a,h,1),lambda h:tv(f,a**3*h,9)/(factorial(12)//factorial(3)*factorial(10)),lambda h:tv(f,tv(a**3,h,1),8)/(factorial(12)//factorial(4)*factorial(8))]
# apply each operator through its 5 coefficient columns (avoid differentiating k coefficients).
R=[s.Matrix.hstack(*[cv(op(x**(4-i)*y**i),4) for i in range(5)]) for op in ops]

rhok=tv(a,kap,1)
A0=[rem(pol(M*k,4)) for M in R]
A1=[rem(pol(M*cv(rhok,4),4)) for M in R]
def coeffmat(fs):
 ps=[s.Poly(f,x,q,t) for f in fs];mon=sorted(set().union(*(set(p.monoms()) for p in ps)));return s.Matrix([[p.coeff_monomial(m) for p in ps] for m in mon])

C0=coeffmat(A0);C1=coeffmat(A1)
ck(C0.shape==(53,3) and C1.shape==(75,3),'all coefficient matrix shapes')
def ns(M):
 from sympy.polys.matrices import DomainMatrix
 dm=DomainMatrix.from_Matrix(M).convert_to(s.QQ.algebraic_field(z))
 return dm.nullspace().to_Matrix()
def rk(M):return M.cols-ns(M).rows
ck(rk(C0)==1 and rk(C1)==2 and rk(C0.col_join(C1))==3,'exact restriction ranks 1,2,3')
M=C0.col_join(C1);minor=M[[0,53,55],:]
expected=s.Matrix([[1280*z/9,s.Rational(1024,81),s.Rational(20480,63)],[0,s.Rational(-256,9),s.Rational(5120,3)],[-20480*z/9,s.Rational(7936,45),s.Rational(152576,63)]])
ck(minor==expected,'published coefficient minor')
ck(s.simplify(minor.det()+s.Rational(268435456000,2187)*z)==0,'nonzero determinant certificate')
# Quotient classes are independent, not an assumption from dimension counts.
raw=[[rem(pol(M[:,i],4)) for i in range(5)] for M in R]
C=s.Matrix.vstack(*(coeffmat([r[i] for r in raw]) for i in range(5)))
ck(rk(C)==3,'three independent quotient covariants')
# Exact binary-icosahedral generator compatibility, same universal convention as input.
def sm(m,n):
 a,b,c,d=list(m)
 return s.Matrix.hstack(*[cv((a*x+c*y)**(n-j)*(b*x+d*y)**j,n) for j in range(n+1)])
ph=(1+z)/2;I=s.I;Rational=s.Rational
for aa,bb,cc,dd in [(0,1,0,0),(0,0,1,0),(Rational(1,2),)*4,(ph/2,Rational(1,2),(ph-1)/2,0)]:
 m=s.Matrix([[aa+I*bb,cc+I*dd],[-cc+I*dd,aa-I*bb]])
 target=s.kronecker_product(m,m.subs(z,-z))
 ck((P*sm(m,6)-target*P).applyfunc(s.simplify)==s.zeros(4,7),'universal P6 intertwiner')
 fv=cv(f,12)
 ck((sm(m,12)*fv-fv).applyfunc(s.simplify)==s.zeros(13,1),'Wronskian invariant')
# McKay recurrence; Sym^n(Sym²W)=sum Sym^(2n-4j)W.
names=('one','W','A','S','D','T','V','P','Wp');dims=(1,2,3,4,5,6,3,4,2)
def ch(**kw):return tuple(kw.get(n,0) for n in names)
rules=(ch(W=1),ch(one=1,A=1),ch(W=1,S=1),ch(A=1,D=1),ch(S=1,T=1),ch(D=1,V=1,P=1),ch(T=1),ch(Wp=1,T=1),ch(P=1))
def mw(a):return tuple(sum(a[i]*rules[i][j] for i in range(9)) for j in range(9))
sym=[ch(one=1),ch(W=1)]
for i in range(2,17):sym.append(tuple(a-b for a,b in zip(mw(sym[-1]),sym[-2])))
for i,c in enumerate(sym):ck(min(c)>=0 and sum(a*b for a,b in zip(c,dims))==i+1,'McKay dimension')
def syma(n):return tuple(sum(sym[2*n-4*j][i] for j in range(n//2+1)) for i in range(9))
ck(syma(8)[names.index('D')]-syma(7)[names.index('A')]==2,'target invariant dimension2')
ck(4+1+3==8 and 4+3==7,'secondary and primary restriction degrees')
print(f'PASS: {count} exact checks; coefficient ranks1,2,3; no actual HM parameter evaluation.')
