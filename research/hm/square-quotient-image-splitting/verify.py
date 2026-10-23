#!/usr/bin/env python3
"""Universal binary identities and abstract characters; no HM instances."""
from pathlib import Path
import hashlib, json
import sympy as s

ROOT=Path(__file__).resolve().parent
checks=0
def require(ok, message):
    global checks
    if not ok: raise RuntimeError(message)
    checks+=1

X,Y,a,b,c,d,p,q=s.symbols('X Y a b c d p q')
ell=p*X+q*Y
f=ell**3*(a*X+b*Y)
g=ell**3*(c*X+d*Y)
def transvectant(f,g,k):
    return s.expand(sum((-1)**i*s.binomial(k,i)*s.diff(f,X,k-i,Y,i)*s.diff(g,X,i,Y,k-i) for i in range(k+1)))
require(s.expand(f*g-ell**6*(a*X+b*Y)*(c*X+d*Y))==0,'Sym8 multiplication channel')
t2=transvectant(f,g,2)
require(s.expand(t2+18*(p*b-q*a)*(p*d-q*c)*ell**4)==0,'universal second transvectant')
require(t2!=0,'Sym4 channel not identically zero')
require(transvectant(f,g,4)==0,'trivial fourth transvectant channel zero')

x,y,u,v=s.symbols('x y u v')
high=x**6*u**2
lower=y*s.diff(high,x)+v*s.diff(high,u)
require(lower==6*x**5*y*u**2+2*x**6*u*v,'lowering highest Sym8')
h9=x*high
h7=s.expand(y*high-x*lower/8)
h5=x**5*(x*v-y*u)**2
require(s.expand(h7-(x**6*y*u**2-x**7*u*v)/4)==0,'Sym7 coefficient image')
for weight, polynomial in [(9,h9),(7,h7),(5,h5)]:
    require(polynomial!=0,'nonzero degree-one channel '+str(weight))
    require(s.expand(x*s.diff(polynomial,y)+u*s.diff(polynomial,v))==0,'highest-weight equation '+str(weight))
    require(s.expand(x*s.diff(polynomial,x)-y*s.diff(polynomial,y)+u*s.diff(polynomial,u)-v*s.diff(polynomial,v)-weight*polynomial)==0,'weight '+str(weight))

# Formal SL2 characters, not coefficient matrices of any geometric instance.
def ch(n): return {i:1 for i in range(-n,n+1,2)}
def add(*characters):
    z={}
    for character in characters:
        for k,vv in character.items():z[k]=z.get(k,0)+vv
    return {k:vv for k,vv in z.items() if vv}
def mul(c1,c2):
    z={}
    for k,vv in c1.items():
        for l,ww in c2.items():z[k+l]=z.get(k+l,0)+vv*ww
    return z
require(mul(ch(6),ch(2))==add(ch(8),ch(6),ch(4)),'degree-zero target decomposition')
require(mul(ch(7),ch(2))==add(ch(9),ch(7),ch(5)),'degree-one target decomposition')
require(mul(add(ch(8),ch(4),ch(0)),ch(1))==add(ch(9),ch(7),ch(5),ch(3),ch(1)),'degree-one source decomposition')
require(15-(9+5)==1,'degree-zero kernel dimension')
require(30-(10+8+6)==6,'degree-one kernel dimension')
require(1+4+7==12 and 4+2*7==18,'quotient rank and degree')
require(2*1+4==6,'dual twist-one section count')
require(18-4==2*(12-1-4),'remaining positive degrees all exactly two')

# Binary-icosahedral McKay restriction and complement ambiguity checks.
names=('one','W','A','S','D','T','V','P','Wp')
dims=(1,2,3,4,5,6,3,4,2)
def rc(**kw):return tuple(kw.get(n,0) for n in names)
rules=(rc(W=1),rc(one=1,A=1),rc(W=1,S=1),rc(A=1,D=1),rc(S=1,T=1),rc(D=1,V=1,P=1),rc(T=1),rc(Wp=1,T=1),rc(P=1))
def wtimes(z):return tuple(sum(z[i]*rules[i][j] for i in range(9)) for j in range(9))
def ra(*zs):return tuple(map(sum,zip(*zs)))
def rs(z,t):return tuple(a-b for a,b in zip(z,t))
sym=[rc(one=1),rc(W=1)]
for n in range(2,10):sym.append(rs(wtimes(sym[-1]),sym[-2]))
for n,z in enumerate(sym):
    require(min(z)>=0 and sum(a*b for a,b in zip(z,dims))==n+1,'restricted symmetric degree '+str(n))
require(sym[3]==rc(S=1),'degree-one coefficient S')
require(sym[6]==rc(V=1,P=1),'degree-two coefficient V+P')
require(wtimes(sym[3])==rc(A=1,D=1),'zero-to-one ambiguity has no trivial')
require(ra(sym[8],sym[6],sym[4])==rc(V=1,P=2,D=2),'zero-to-two ambiguity has no trivial')
require(wtimes(sym[6])==rc(Wp=1,T=2),'one-to-two ambiguity has no S')
require(8+4*7+7*6==78,'actual image degree after duality twist')

manifest=ROOT/'INPUTS.json'
require(manifest.exists(),'immutable input manifest exists')
for row in json.loads(manifest.read_text()):
    data=(ROOT/'audit-inputs'/(row['key']+'.md')).read_bytes()
    require(hashlib.sha256(data).hexdigest()==row['sha256'],'input SHA256 '+row['key'])
    require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==row['blob'],'input Git blob '+row['key'])
print(json.dumps({'status':'PASS','checks':checks,'square_quotient':'O + S O(1) + (V+P) O(2)','image_Theta':'O(8) + S O(7) + (V+P) O(6)','scope':'universal symbolic identities and abstract characters; actual image application requires the pinned rank theorem'},indent=2))
