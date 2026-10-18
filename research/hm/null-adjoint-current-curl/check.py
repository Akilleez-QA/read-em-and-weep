"""Universal free-word identities only. No physical source imports or matrix values."""
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import json, hashlib

ROOT=Path(__file__).resolve().parent
PINS={'branches.json': '335c9568efc9d15d0f94833e6d6635768724cab106b2e9e8ee5e83250e89cb9f', 'inputs/compiler.py.txt': '28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386', 'inputs/raw_engine.py.txt': 'c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9', 'dependencies/source-adjoint-proof.md': '106648cb80212191cc6fe85098a24271069f8f2e7f625daae29c9f5a114d2922', 'dependencies/source-adjoint-review.md': '0259d8c855dc3d21f45212912f4ec526f7893c1da6a0e3065e69b99ef3713d46'}
for name,digest in PINS.items():
    if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
        raise RuntimeError('pinned input mismatch: '+name)

INVERSE={'A':'Ai','Ai':'A','B':'Bi','Bi':'B'}
def reduce_word(w):
    out=[]
    for t in w:
        if out and INVERSE.get(t)==out[-1]:out.pop()
        else:out.append(t)
    return tuple(out)
def clean(d):return {w:c for w,c in d.items() if c}
def add(*ps):
    d=defaultdict(Q)
    for p in ps:
        for w,c in p.items():d[w]+=c
    return clean(d)
def scale(p,c):return clean({w:c*v for w,v in p.items()})
def mul(*ps):
    out={():Q(1)}
    for p in ps:
        d=defaultdict(Q)
        for w,c in out.items():
            for v,e in p.items():d[reduce_word(w+v)]+=c*e
        out=clean(d)
    return out
def atom(s):return {(s,):Q(1)}
def comm(p,q):return add(mul(p,q),scale(mul(q,p),-1))
def der_atom(t,i):
    if t in ('Ai','Bi'):
        x=t[0];return scale(mul(atom(t),atom(x+i),atom(t)),-1)
    if t[0] in 'AB' and all(c in 'ab' for c in t[1:]):
        return atom(t[0]+''.join(sorted(t[1:]+i)))
    if t=='C':return atom('C'+i)
    raise ValueError(t)
def der(p,i):
    out={}
    for w,c in p.items():
        for j,t in enumerate(w):
            out=add(out,scale(mul({w[:j]:Q(1)},der_atom(t,i),{w[j+1:]:Q(1)}),c))
    return out
def trace(p):
    # Cyclic rotation may expose a cancelling inverse pair at the boundary.
    d=defaultdict(Q)
    for w,c in p.items():
        while w:
            v=min((reduce_word(w[i:]+w[:i]) for i in range(len(w))),key=lambda x:(len(x),x))
            if len(v)==len(w):
                w=v;break
            w=v
        d[w]+=c
    return clean(d)
checks=[]
def eq(name,p,q):
    if add(p,scale(q,-1)):raise RuntimeError(name+' failed')
    checks.append(name)
def neq(name,p,q):
    if not add(p,scale(q,-1)):raise RuntimeError(name+' mutation survived')
    checks.append(name)
A,Ai,B,Bi,C=map(atom,['A','Ai','B','Bi','C'])
L={i:mul(Ai,atom('A'+i)) for i in 'ab'}
U={i:mul(Ai,Bi,atom('B'+i),A) for i in 'ab'}
T={i:add(L[i],U[i]) for i in 'ab'}
La,Lb,Ua,Ub=L['a'],L['b'],U['a'],U['b']
cL=add(der(Lb,'a'),scale(der(La,'b'),-1))
cU=add(der(Ub,'a'),scale(der(Ua,'b'),-1))
BL=comm(La,Lb);BU=comm(Ua,Ub)
M=add(comm(La,Ub),comm(Ua,Lb))
eq('Maurer-Cartan L',cL,scale(BL,-1))
eq('transported U curl',cU,scale(add(BU,M),-1))
eq('total current curl',add(cL,cU),scale(comm(T['a'],T['b']),-1))
eq('product transition current',mul(Ai,Bi,der(mul(B,A),'a')),T['a'])
kij=scale(BL,Q(1,4));kik=scale(comm(T['a'],T['b']),Q(1,4))
source_k=scale(add(mul(der(Ai,'a'),der(A,'b')),scale(mul(der(Ai,'b'),der(A,'a')),-1)),Q(-1,4))
eq('literal source k',source_k,kij)
eq('k difference curl',cU,scale(add(kik,scale(kij,-1)),-4))
# The scalar coefficient of each independent endpoint is checked separately.
oldjk=scale(trace(add(der(mul(C,Lb),'a'),scale(der(mul(C,La),'b'),-1))),Q(-1,2))
oldij=scale(trace(add(der(mul(C,Ub),'a'),scale(der(mul(C,Ua),'b'),-1))),Q(1,2))
KderL=trace(add(mul(atom('Ca'),Lb),scale(mul(atom('Cb'),La),-1)))
KderU=trace(add(mul(atom('Ca'),Ub),scale(mul(atom('Cb'),Ua),-1)))
newjk=add(scale(KderL,Q(-1,2)),scale(trace(mul(C,kij)),2))
newij=add(scale(KderU,Q(1,2)),scale(trace(mul(C,add(kij,scale(kik,-1)))),2))
eq('jk complete weighted adjoint',oldjk,newjk)
eq('ij complete weighted adjoint',oldij,newij)
Da=add(atom('Ca'),comm(La,C));Db=add(atom('Cb'),comm(Lb,C))
covij=scale(trace(add(mul(Da,Ub),scale(mul(Db,Ua),-1),scale(mul(C,BU),-1))),Q(1,2))
eq('cyclic covariant dual form',newij,covij)
neq('reject naive MC for U',cU,scale(BU,-1))
neq('reject dropped dual derivative jk',oldjk,scale(trace(mul(C,kij)),2))
neq('reject dropped dual derivative ij',oldij,scale(trace(mul(C,add(kij,scale(kik,-1)))),2))
neq('reject wrong ij endpoint sign',oldij,scale(newij,-1))
# The mixed transport correction survives ordinary cyclic trace with arbitrary C.
neq('mixed trace family really survives',trace(mul(C,M)),{})
branches=json.loads(Path(__file__).with_name('branches.json').read_text())
expected=[]
for pair,other in [([0,1],[2,3]),([2,3],[0,1])]:
    a,b=pair
    for axis,current,edge,num in [(a,['L',b],'jk',1),(b,['L',a],'jk',-1),(b,['U',a],'ij',1),(a,['U',b],'ij',-1)]:
        expected.append(dict(pair=pair,scalar_pair=other,axis=axis,current=current,edge=edge,coefficient=[num,2]))
if branches!=expected:raise RuntimeError('eight source branches mismatch')
checks.append('eight source branch signs and endpoints')
print(json.dumps({'status':'PASS','checks':checks,'check_count':len(checks),'scope':'universal free differential words, formal cyclic trace, source branch metadata; no matrix/source/owner/jet evaluation'},indent=2))
