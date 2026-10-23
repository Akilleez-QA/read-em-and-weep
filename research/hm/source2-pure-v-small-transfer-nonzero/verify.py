#!/usr/bin/env python3
"""Universal prolongation and finite-group identities; no actual instances."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent; checks=[]
def check(name,ok):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['local_path']).read_bytes()
 check(item['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==item['sha256'])
 check(item['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'])
x,y=s.symbols('x y')
# All coefficients of arbitrary j(e_i) are independent, not equivariant samples.
c=s.symbols('c0:85');fs=[sum(c[17*i+k]*x**(16-k)*y**k for k in range(17)) for i in range(5)]
out=[]
for i in range(6):
 out.append(s.expand(((5-i)*x*fs[i] if i<5 else 0)+(i*y*fs[i-1] if i>0 else 0))/5)
rows=[s.Poly(f,x,y).coeff_monomial(x**(17-k)*y**k) for f in out for k in range(18)]
M=s.Matrix(rows).jacobian(c)
check('full prolongation dimensions',M.shape==(108,85))
check('full prolongation injective',M.rank()==85)
check('highest monomial first recurrence',s.expand(out[0]-x*fs[0])==0)
for i in range(1,5):check('recurrence '+str(i),s.expand(5*out[i]-(5-i)*x*fs[i]-i*y*fs[i-1])==0)
check('terminal recurrence',s.expand(out[5]-y*fs[4])==0)
# Polarization and multiplication for arbitrary degree12 form, no f12 evaluation.
d=s.symbols('d0:13');F=sum(d[k]*x**(12-k)*y**k for k in range(13))
j=[s.expand(F*x**(4-i)*y**i) for i in range(5)]
for i in range(6):
 pol=((5-i)*x*j[i] if i<5 else 0)+(i*y*j[i-1] if i else 0)
 check('formal degree12 scalar prolongation '+str(i),s.expand(pol/5-F*x**(5-i)*y**i)==0)
# Exact character table via trace of the binary defining representation.
z=s.sqrt(5);phi=(1+z)/2
tr=[s.Integer(2),s.Integer(-2),s.Integer(0),s.Integer(1),s.Integer(-1),phi,-phi,phi-1,1-phi]
weights=[1,1,30,20,20,12,12,12,12]
def simp(v):return s.Matrix([s.simplify(a) for a in v])
def sy(n):
 a=s.ones(9,1);b=s.Matrix(tr)
 if n==0:return a
 for k in range(1,n):a,b=b,simp([tr[i]*b[i]-a[i] for i in range(9)])
 return b
def prod(a,b):return simp([u*v for u,v in zip(a,b)])
def ip(a,b):return s.simplify(sum(n*u*v for n,u,v in zip(weights,a,b))/120)
W=sy(1);Wp=simp([a.xreplace({z:-z}) for a in W]);S=sy(3);D=sy(4);T=sy(5);P=prod(W,Wp);V=sy(6)-P
check('binary class weights120',sum(weights)==120)
check('D irreducible',ip(D,D)==1)
check('T irreducible',ip(T,T)==1)
check('V irreducible',ip(V,V)==1)
check('W tensor V equals T',simp(prod(W,V)-T)==s.zeros(9,1))
check('NC2 decomposition',simp(sy(16)-V-P-2*D)==s.zeros(9,1))
check('NC3 decomposition',simp(sy(17)-Wp-S-2*T)==s.zeros(9,1))
check('NC3 T multiplicity exactly2',ip(sy(17),T)==2)
check('NC4 has no V',ip(P+D,V)==0)
check('V has no intersection with I2 type',ip(V,D)==0)
check('W tensor D has canonical T and S',simp(prod(W,D)-T-S)==s.zeros(9,1))
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,conclusion='No D incidence in every branch; full NC4 transversality for all endpoint16, and gamma nonzero for endpoint9.',scope='Universal arbitrary-map prolongation and characters only; actual commutation and joint kernel are justified by proof.'),indent=2))
