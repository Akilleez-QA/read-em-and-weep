#!/usr/bin/env python3
"""Bounded exact diagnostics, not actual instance computations."""
import hashlib, itertools, json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
checks=0

def check(ok, label):
    global checks
    checks+=1
    if not ok:
        raise RuntimeError(label)

def add(*vs): return tuple(map(sum,zip(*vs)))
def sub(v,w): return tuple(a-b for a,b in zip(v,w))
def meet(v,w): return tuple(min(a,b) for a,b in zip(v,w))
def dim(v): return sum(a*b for a,b in zip(v,(3,3,4,5)))
# Coordinates A,V,P,D. Universal representation multiplicities only.
x=[(0,0,1,1),(1,1,1,1),(0,1,1,2)]
y=[(0,1,2,1),(0,1,1,1),(0,0,1,1)]
X=add(*x);Y=add(*y);K=(1,0,0,1);I=(0,2,3,3)
check(X==(1,2,3,4) and Y==(0,2,4,3),'total endpoint characters')
check(sub(X,K)==I and dim(I)==33,'actual imported image arithmetic')
records=[]
for mode,xx,yy in [('zero',x,y),('nonzero',[x[0],add(x[1],x[2])],[y[0],add(y[1],y[2])])]:
    for bits in itertools.product((0,1),repeat=len(xx)):
        if len(set(bits))==1: continue
        ix=[i for i,b in enumerate(bits) if b]; co=[i for i,b in enumerate(bits) if not b]
        bound=add(meet(add(*(xx[i] for i in ix)),add(*(yy[i] for i in ix))),meet(add(*(xx[i] for i in co)),add(*(yy[i] for i in co))))
        n8=mode=='zero' and (bits==(0,1,0) or bits==(1,0,1))
        check(bound==(I if n8 else (0,1,3,3)), 'all subset bounds')
        records.append(dict(mode=mode,bits=bits,bound=bound,dimension=dim(bound),exclusion='second Bockstein' if n8 else 'missing V'))
check(len(records)==8,'eight proper vertex subsets')
check(meet(x[1],y[1])==y[1] and sub(x[1],y[1])==(1,0,0,0),'N8 surjective block unique A')
check(x[0][0]==x[2][0]==0,'A is unique actual isotypical space')
U=(1,2,2,3);Z=(0,2,2,2)
check(dim(U)==32 and dim(Z)==24,'PR795 annihilator dimensions')
check(sub(U,K)==Z and dim(U)-dim(K)==dim(Z),'annihilator onto if entire J compatible')
# Triangular two-arrow algebra in pencil orientation: source d,target a.
def mul(v,w):
    a,d,b,c=v; A,D,B,C=w
    return (a*A,d*D,a*B+D*b,a*C+D*c)
def plus(v,w):return tuple(a+b for a,b in zip(v,w))
def minus(v,w):return tuple(a-b for a,b in zip(v,w))
one=(F(1),F(1),F(0),F(0));zero=(F(0),)*4
for a,d in itertools.product((F(0),F(1)),repeat=2):
    for b,c in itertools.product(map(F,(-2,-1,0,1,2)),repeat=2):
        e=(a,d,b,c); idem=mul(e,e)==e
        check(idem==((a+d-1)*b==0 and (a+d-1)*c==0),'idempotent equations')
        if not idem: continue
        diag=(a,d,F(0),F(0))
        shear=zero if a==d else (F(0),F(0),b/(d-a),c/(d-a))
        check(mul(plus(one,shear),minus(one,shear))==one,'radical unit inverse')
        check(mul(mul(plus(one,shear),diag),minus(one,shear))==e,'all radical shear orientation')
for b,c,B,C in itertools.product(map(F,(-1,0,1)),repeat=4):
    check(mul((0,0,b,c),(0,0,B,C))==zero,'square-zero two-arrow ideal')
# Cubic Hermite projector for two spectral values 0,1: f=3z²-2z³.
# Evaluate in exact triangular algebra; this does NOT instantiate actual maps.
for b,c in itertools.product(map(F,(-1,0,1)),repeat=2):
    h=(F(0),F(1),b,c);h2=mul(h,h);h3=mul(h2,h)
    f=tuple(3*a-2*b for a,b in zip(h2,h3))
    check(mul(f,f)==f and f not in (zero,one),'Hermite polynomial produces proper idempotent')
# Universal surjective block Q=[0 I], T=[B C], right inverse s=[0;I].
# For k=(h,0), correction u=(0,-Bh), second error=-CBh lies in im Q.
# Formal recurrence r1=-Bh, r_(n+1)=-C r_n checks each coefficient.
for B,C,h in itertools.product(map(F,(-1,0,1)),repeat=3):
    r=[F(0),-B*h]
    for n in range(2,6): r.append(-C*r[-1])
    check(r[1]+B*h==0,'surjective block first correction')
    for n in range(2,6):check(r[n]+C*r[n-1]==0,'formal block lift coefficient')
# Negative control: scalar plus a nonzero square-zero element remains nonscalar.
j=(F(0),F(0),F(1),F(0))
check(j!=zero and mul(j,j)==zero,'nonzero nilpotent is not ruled out')
for lam,b in itertools.product(map(F,(-1,0,1)),repeat=2):
    e=(lam,lam,b,F(0))
    check((mul(e,e)==e)==(b==0 and lam in (0,1)),'dual numbers have no proper idempotent')
manifest=json.loads((ROOT/'INPUTS.json').read_text())
for entry in manifest:
    data=(ROOT/entry['local_path']).read_bytes()
    check(hashlib.sha256(data).hexdigest()==entry['sha256'],'input SHA256 '+entry['local_path'])
    check(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==entry['git_blob'],'input Git blob '+entry['local_path'])
print(json.dumps({'checks':checks,'status':'pass','proper_subsets':records,'result':'D_Q=C1+J_Q, J_Q²=0, dim J_Q≤1; no source/pair cut'},indent=2))
