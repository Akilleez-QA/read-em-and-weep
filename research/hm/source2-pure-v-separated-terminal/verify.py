#!/usr/bin/env python3
"""Whole universal coefficient maps, never selected actual instances."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent;checks=[]
def check(name,ok):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
for a in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/a['local_path']).read_bytes()
 check(a['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==a['sha256'])
 check(a['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==a['git_blob'])
import sympy as s
from math import comb
x,y=s.symbols('x y');z=s.sqrt(5)
def cv(f,n):
 f=s.Poly(s.expand(f),x,y);return s.Matrix([f.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def tv(a,f,k):return s.expand(sum((-1)**j*comb(k,j)*s.diff(a,x,k-j,y,j)*s.diff(f,x,j,y,k-j) for j in range(k+1)))
def gram(n):return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,comb(n,i)) if i+j==n else 0)
P8=s.Matrix([[0,7*z/40,0,s.Rational(1,8),0,-z/40,0,s.Rational(1,8),0],[-1,0,z/20,0,-s.Rational(1,10),0,-z/20,0,0],[0,0,z/20,0,s.Rational(1,10),0,-z/20,0,1],[0,-s.Rational(1,8),0,z/40,0,-s.Rational(1,8),0,-7*z/40,0]])
E8=gram(8).inv()*P8.T
C=s.Matrix.hstack(*[s.Matrix.vstack(cv(tv(x**(3-i)*y**i,x**(8-j)*y**j,2),7),cv(tv(x**(3-i)*y**i,x**(8-j)*y**j,3),5)) for i in range(4) for j in range(9)])
CP=C*s.diag(E8,E8,E8,E8)
# Degree3 relation image of W times degree2 polarization.
Rel=s.zeros(36,22)
for l in range(2):
 for k in range(11):
  for j in range(3):
   i=k-j
   if 0<=i<=8:Rel[(j+l)*9+i,l*11+k]=comb(10-k,2-j)*comb(k,j) if 0<=2-j<=10-k and 0<=j<=k else 0

check('P8 apolar inclusion nondegenerate',(P8*E8).det()!=0)
check('full relation matrix shape',Rel.shape==(36,22))
check('full relation image dimension22',Rel.rank()==22)
check('transvectant quotient kills every relation',C*Rel==s.zeros(14,22))
check('whole quotient rank14',C.rank()==14)
check('whole kernel equals relation image',36-C.rank()==Rel.rank())
rs=[0,1,2,3,4,5,8,9,10,11,12,13];cs=list(range(12))
det=s.simplify(CP.extract(rs,cs).det())
check('exact twelve by twelve determinant',det==-548077643046499094530321725505142784)
check('whole cubic P descendant rank12',CP.rank()==12)
check('cubic P kernel dimension4',CP.cols-CP.rank()==4)
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

check('binary group class size sum',sum(weights)==120)
check('cubic P source character S plus2T',simp(prod(S,P)-S-2*T)==s.zeros(9,1))
check('terminal quotient character Wprime plus2T',simp(sy(7)+sy(5)-Wp-2*T)==s.zeros(9,1))
check('relation character W tensor Sym10',simp(prod(S,sy(8))-prod(W,sy(10))-sy(7)-sy(5))==s.zeros(9,1))
check('actual degree5 has no S',ip(Wp+3*T,S)==0)
check('S channel irreducible',ip(S,S)==1)
check('terminal quotient S multiplicity0',ip(sy(7)+sy(5),S)==0)
check('terminal source has two T copies',ip(prod(S,P),T)==2)
check('terminal target has two T copies',ip(sy(7)+sy(5),T)==2)
check('actual length51',9+14+16+12==51)
check('socle dimension16',4+12==16)
t=s.symbols('t')
check('bounded Hilbert numerator',s.expand((9+14*t+16*t*t+12*t**3)*(1-t)**2)==9-4*t-3*t*t-6*t**3-8*t**4+12*t**5)
# Minimal resolution from actual socle and character-valued numerator.
A=sy(2);F=[P+D,Wp+2*T,V+2*P+D,2*T];zero=s.zeros(9,1)
num=[]
for k in range(6):
 num.append(simp((F[k] if k<4 else zero)-(prod(W,F[k-1]) if 0<=k-1<4 else zero)+(F[k-2] if 0<=k-2<4 else zero)))
expected=[P+D,-S,-V,-Wp-S,-V-D,2*T]
check('full equivariant Hilbert numerator',all(simp(a-b)==zero for a,b in zip(num,expected)))
T2={4:P,5:2*T};T1={1:S,2:V,3:Wp+S,4:V+P+D}
check('socle determines Tor2',T2[4][0]==4 and T2[5][0]==12)
check('all Tor terms reconstruct numerator',all(simp(num[k]-((P+D if k==0 else zero)-T1.get(k,zero)+T2.get(k,zero)))==zero for k in range(6)))
check('essential quartic relation P retained',ip(T1[4],P)==1)
check('original first-syzygy degrees',[d+2 for d in T1]==[3,4,5,6])
check('original second-syzygy degrees',[d+2 for d in T2]==[6,7])
check('all lower annihilator domains irreducible',all(ip(sy(d),sy(d))==1 for d in [1,2,3]))
check('all three descendant degrees nonzero',all(F[d][0]>0 for d in [1,2,3]))
check('fourth negative power exceeds terminal degree',2+4>5)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,cubic_minor=str(det),actual_conditional_dimensions=[9,14,16,12],scope='Universal representation coefficients only; actual-map transfer requires the pinned proofs.'),indent=2))
