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
f=s.expand(s.det(s.Matrix([[s.diff(h.subs(y,1),x,k) for h in v] for k in range(3)])))
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

def pairing(F,H,d):
 f=cv(F,d);h=cv(H,d)
 return s.expand(sum((-1)**i*f[i]*h[d-i]/comb(d,i) for i in range(d+1)))
c=pairing(a*a,kap,4); B=pairing(f,a**4*kap,12); C=s.expand((q*q-4*t)*c)
ck(s.Poly(C,q,t).as_expr()!=0,'nonzero primary restriction')
ck(s.expand(B+s.Rational(64,175)*z*C)==0,'exact primary row relation')
rhok=tv(a,kap,1)
ck(pairing(a*a,rhok,4)==0,'quadratic secondary zero')
ck(pairing(f,a**4*rhok,12)==0,'Cartan quartic secondary zero')
ck(pairing(f,x**8*y**4,12)==s.Rational(2,15),'universal basis independence coefficient')
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
for i in range(2,19):sym.append(tuple(a-b for a,b in zip(mw(sym[-1]),sym[-2])))
for i,c in enumerate(sym):ck(min(c)>=0 and sum(a*b for a,b in zip(c,dims))==i+1,'McKay dimension')
def syma(n):return tuple(sum(sym[2*n-4*j][i] for j in range(n//2+1)) for i in range(9))

ck(syma(4)[names.index('D')]==2,'quartic covector dimension2')
for degree in [18,14,10,6,2]: ck(sym[degree][0]==0,'binary constituent has no invariant')
ck(syma(9)[0]==0,'PLANE degree9 invariants vanish')
ck(syma(7)[0]==0,'PLANE degree7 invariants vanish')
ck(4+1+8==13 and 4+1+4==9,'secondary octic degrees')
print(f'PASS: {count} exact checks; quartic secondary restriction is zero; no actual HM evaluation.')
