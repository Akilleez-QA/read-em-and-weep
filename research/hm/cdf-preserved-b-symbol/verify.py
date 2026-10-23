#!/usr/bin/env python3
"""Bounded universal algebra only. Never imports or evaluates HM instance data."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=0
def check(p,msg):
 global checks
 if not p: raise ValueError(msg)
 checks+=1
for name,pin in json.loads((ROOT/'INPUTS.json').read_text()).items():
 b=(ROOT/'inputs'/name).read_bytes()
 check(hashlib.sha256(b).hexdigest()==pin['sha256'],'sha256 '+name)
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob'],'git blob '+name)
names=['one','W','A','S','D','T','V','P','Wp']; dims=[1,2,3,4,5,6,3,4,2]
def c(**kw):return tuple(kw.get(n,0) for n in names)
def add(*xs):return tuple(map(sum,zip(*xs)))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,n):return tuple(x*n for x in a)
def dim(a):return sum(x*y for x,y in zip(a,dims))
rules=[c(W=1),c(one=1,A=1),c(W=1,S=1),c(A=1,D=1),c(S=1,T=1),c(D=1,V=1,P=1),c(T=1),c(T=1,Wp=1),c(P=1)]
def w(a):return tuple(sum(a[i]*rules[i][j] for i in range(9)) for j in range(9))
def a(a):return sub(w(w(a)),a)
check(a(c(A=1))==c(one=1,A=1,D=1),'A tensor A')
check(a(c(D=1))==c(A=1,D=1,V=1,P=1),'A tensor D')
check(a(c(A=1))[names.index('D')]==1,'unique alpha A')
check(a(c(D=1))[names.index('D')]==1,'unique alpha D')
check(a(c(D=1))[names.index('P')]==1,'unique gamma')
xf=c(V=1,P=1,D=2); xb=c(A=1,V=1,P=2,D=2)
yb=c(V=1,P=2,D=2); yf=c(P=1,D=1); yl=c(V=1,P=1)
k=c(A=1,D=1); cok=c(P=1)
check(sub(add(xf,xb),k)==sub(add(yf,yb,yl),cok),'global cohomology Euler')
for d in [0,1]:
 kb=c(A=1,D=d); im=sub(xb,kb); cs=sub(yb,im)
 check(cs==c(D=d),'exhaust internal cokernel possibilities')
 check(dim(im)==21-5*d,'derived internal image dimension')
check(sub(yb,sub(xb,k))==c(D=1),'internal cokernel D')
check(sub(add(yf,yl),sub(xf,c(D=1)))==c(P=1),'quotient cohomology')
check(dim(sub(xb,k))==16,'conditional image dimension 16')
check(dim(xf)==17 and dim(xb)==24,'source dimensions')
x,y=s.symbols('x y'); av=s.symbols('a0:3'); bv=s.symbols('b0:3'); hv=s.symbols('h0:5')
f=sum(av[i]*x**(2-i)*y**i for i in range(3))
g=sum(bv[i]*x**(2-i)*y**i for i in range(3))
h=sum(hv[i]*x**(4-i)*y**i for i in range(5))
def tau(f,h):return s.diff(f,x)*s.diff(h,y)-s.diff(f,y)*s.diff(h,x)
expr=s.expand(f*tau(f,h))
check(expr!=0,'universal composed family nonzero')
check(s.expand((f+g)*tau(f+g,h)-expr-g*tau(g,h)-f*tau(g,h)-g*tau(f,h))==0,'polarization')
check(s.expand(x**2*tau(x**2,x**3*y))==2*x**6,'universal highest weight coefficient')
check(s.Poly(expr,x,y).total_degree()==6,'binary degree six')
check(all(sum(mon[:3])==2 and sum(mon[3:])==1 for mon in s.Poly(expr,*av,*hv).monoms()),'quadratic parameter and linear D input')
# Euler relation for the standard sl2 raising derivation on binary polynomials.
raising=lambda p:s.expand(x*s.diff(p,y))
check(s.expand(raising(tau(f,h))-tau(raising(f),h)-tau(f,raising(h)))==0,'transvectant sl2 naturality')
check(s.expand(raising(f*tau(f,h))-raising(f)*tau(f,h)-f*tau(raising(f),h)-f*tau(f,raising(h)))==0,'composite sl2 naturality')
# Synthetic deformation block identity: Q maps correction u to -alpha*k;
# quotient differential gamma then gives second class -gamma*alpha*k.
al,ga,kk=s.symbols('alpha gamma k'); u=-al*kk
check(s.expand(ga*u+ga*al*kk)==0,'signed second transfer identity')
check(s.expand(ga*al*kk)!=0,'nonzero factors cannot be dropped')
H=s.symbols('H');check(s.series((1-H)**-3,H,0,3).removeO()==1+3*H+6*H**2,'Chern quotient')
# Negative regression: A alone in the internal kernel is the onto case,
# not the actual nonzero-second-compatible case.
check(sub(yb,sub(xb,c(A=1)))==c(),'onto branch has no obstruction target')
check(c(A=1)!=k,'do not discard forced D kernel')
check(a(c(D=1))[names.index('P')]!=0,'do not erase nonzero projected composition')
print(json.dumps({'status':'pass','checks':checks,'scope':'universal representation and polynomial identities only','actual_instance_evaluations':0},indent=2))
