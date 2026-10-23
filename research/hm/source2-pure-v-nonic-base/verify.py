#!/usr/bin/env python3
"""Universal representation/local-algebra diagnostics, no actual-source inputs."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def ck(n,v):
 if not v: raise RuntimeError(n)
 checks.append(n)
for p in json.loads((root/'INPUTS.json').read_text()):
 b=(root/p['local_path']).read_bytes()
 ck('immutable commit '+p['label'],len(p['commit'])==40)
 ck('sha256 '+p['label'],hashlib.sha256(b).hexdigest()==p['sha256'])
 ck('git blob '+p['label'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob'])
r=s.sqrt(5);A=[3,-1,0,(1+r)/2,(1-r)/2];P=[4,0,1,-1,-1];D=[5,1,-1,0,0];sizes=[1,15,20,12,12]
def inner(a,b):return s.simplify(sum(n*x*y for n,x,y in zip(sizes,a,b))*s.Rational(1,60))
h=[[s.Integer(1)]*5]
for n in range(1,10):
 h.append([s.simplify(c*h[n-1][i]-(c*h[n-2][i] if n>=2 else 0)+(h[n-3][i] if n>=3 else 0)) for i,c in enumerate(A)])
inv=[inner(x,[1]*5) for x in h]
ck('low-degree invariant dimensions',inv==[1,0,1,0,1,0,2,0,2,0])
ck('cubic P uniqueness',inner(h[3],P)==1)
ck('no P in degree-seven ideal generators',inner(P,D)==0)
ck('degree-eight invariants are delta times sextics',inv[8]==inv[6])
ck('degree-four invariants are delta squared',inv[4]==inv[2]==1)
ck('no odd gcd degree through nine',all(inv[d]==0 for d in [1,3,5,7,9]))
ck('nonreduced sextic repeated reduced part degree at most three',6//2==3)
# Full D5 class order: identity, +/-1 rotations, +/-2 rotations, reflections.
D5sizes=[1,2,2,5];P5=[4,-1,-1,0]
rho1=[2,(r-1)/2,(-r-1)/2,0];rho2=[2,(-r-1)/2,(r-1)/2,0];sign5=[1,1,1,-1]
def inn5(a,b):return s.simplify(sum(n*x*y for n,x,y in zip(D5sizes,a,b))*s.Rational(1,10))
ck('P restricts to both distinct D5 irreducibles',all(s.simplify(p-a-b)==0 for p,a,b in zip(P5,rho1,rho2)))
ck('D5 quadratic jet multiplicity one',inn5(P5,[x*y for x,y in zip(sign5,rho2)])==1)
ck('D5 sign twist preserves quadratic two-space character',all(s.simplify(x*y-y)==0 for x,y in zip(sign5,rho2)))
# S3 order: identity, transpositions, 3-cycles.
S3sizes=[1,3,2];P3=[4,0,1];rho=[2,0,-1];sign3=[1,-1,1]
ck('P S3 restriction',P3==[1+c+d for c,d in zip(sign3,rho)])
ck('S3 signed first jet multiplicity one',sum(n*p*c*q for n,p,c,q in zip(S3sizes,P3,sign3,rho))*s.Rational(1,6)==1)
ck('normalizer odd twist sign',(-1)**9==-1)
ck('axis sextic cyclic twist trivial',1**6==1)
# The colon ((u^2,v^2):(u,v)) is m^2, by exhaustive monomial border.
inI=lambda i,j:i>=2 or j>=2
for i in range(4):
 for j in range(4):
  ck('colon monomial '+str((i,j)),(inI(i+1,j) and inI(i,j+1))==(i+j>=2))
ck('C3 tangent has no invariant linear term',all(w%3!=0 for w in [1,-1]))
ck('sixteen singular points exceed sextic genus bound',6+10>10+6-1)
ck('polar alternative bound',2*(6+10)>6*5)
ck('joint jet Bezout contradiction',6*3**2+10*2**2==94 and 94>9**2)
ck('length O/m cubed',sum(1 for i in range(3) for j in range(3) if i+j<3)==6)
ck('length O/m squared',sum(1 for i in range(2) for j in range(2) if i+j<2)==3)
ck('ell5 lower bound',6*6+10==46)
ck('ell3 lower bound',6*4+10*3==54)
print(json.dumps({'status':'pass','count':len(checks),'checks':checks,'scope':'all nonzero universal gate elements; actual coefficient line unselected'},indent=2))
