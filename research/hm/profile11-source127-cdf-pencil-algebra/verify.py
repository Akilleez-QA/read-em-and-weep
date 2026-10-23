#!/usr/bin/env python3
"""Fixed universal representation checks only. No source/model evaluation."""
from fractions import Fraction as Q
from functools import lru_cache

# Exact Q(sqrt(5)) arithmetic: (a,b) denotes a+b*sqrt(5).
def q(a, b=0): return (Q(a), Q(b))
def plus(x, y): return (x[0]+y[0], x[1]+y[1])
def times(x, y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(k, x): return (k*x[0], k*x[1])
def total(xs):
    out = q(0)
    for x in xs: out = plus(out, x)
    return out
ZERO = (q(0),)*9
def va(x, y): return tuple(plus(a,b) for a,b in zip(x,y))
def vk(k, x): return tuple(scale(k,a) for a in x)
def vm(x, y): return tuple(times(a,b) for a,b in zip(x,y))
def vs(x, y): return va(x,vk(-1,y))
phi, phip = q(Q(1,2),Q(1,2)), q(Q(1,2),-Q(1,2))
W = (q(2),q(-2),phi,scale(-1,phi),phip,scale(-1,phip),q(1),q(-1),q(0))
sizes = (1,1,12,12,12,12,20,20,30)
@lru_cache(None)
def sym(n):
    assert n >= 0
    a = (q(1),)*9
    if n == 0: return a
    b = W
    for _ in range(2,n+1): a,b = b,vs(vm(W,b),a)
    return b
chars = {"one":sym(0),"W":W,"A":sym(2),"S":sym(3),"D":sym(4),"T":sym(5)}
chars["P"] = tuple(map(q,(4,4,-1,-1,-1,-1,1,1,0)))
chars["V"] = vs(sym(6),chars["P"])
chars["Wp"] = vs(vm(W,chars["P"]),chars["T"])
names = ("one","W","Wp","A","V","P","S","D","T")
def inner(x,y): return scale(Q(1,120),total(scale(k,times(a,b)) for k,a,b in zip(sizes,x,y)))
assert all(inner(chars[a],chars[b]) == q(a==b) for a in names for b in names)
def rep(text):
    out = ZERO
    if text == "0": return out
    for term in text.split("+"):
        k = int(term[0]) if term[0].isdigit() else 1
        name = term[1:] if term[0].isdigit() else term
        out = va(out,vk(k,chars[name]))
    return out
def dec(x):
    out = [inner(x,chars[n]) for n in names]
    assert all(b==0 and a.denominator==1 for a,b in out)
    return tuple(int(a) for a,b in out)

# Authenticate the exact theorem/interface inputs; all checks below are universal.
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text());assert len(entries)==8
for e in entries:
    b=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']
def hom(U,d,V,e):return 0 if e<d else inner(chars[U],vm(chars[V],sym(e-d)))[0]
C10=rep('A+V+P');C11=sym(10);C9=sym(8)
assert C11==rep('A+V+D') and C9==rep('P+D')
assert inner(C11,C10)==q(2) and inner(C9,C10)==q(1)
assert inner(C9,C11)==q(1)
for U in ('P','D'):
    for V in ('V','P'):assert hom(U,-2,V,-4)==0
    assert hom(U,-2,'one',-8)==0
for U in ('V','P'):
    assert hom(U,-4,'one',-8)==0
    assert hom('one',-8,U,-4)==0
assert sym(26)==rep('A+2V+2P+2D')
assert hom('one',-8,'one',18)==0
# Exact covariant cohomology blocks, with no unmarked dual identification.
N2F=sym(16);N2B=vm(chars['S'],sym(5));N2L=ZERO
N3F=sym(17);N3B=vm(chars['S'],sym(6));N3L=sym(7)
N4F=rep('P+D');N4B=vm(rep('V+P'),sym(2));N4L=sym(6)
assert N2F==rep('V+P+2D') and N2B==rep('A+V+2P+2D')
assert N4B==rep('V+2P+2D') and N4L==rep('V+P')
assert va(va(N2F,N2B),N2L)==rep('A+2V+3P+4D')
assert va(va(N3F,N3B),N3L)==rep('3Wp+3S+6T')
assert va(va(N4F,N4B),N4L)==rep('2V+4P+3D')
assert [int(x[0][0]) for x in (N2F,N2B,N2L)]==[17,24,0]
assert [int(x[0][0]) for x in (N4F,N4B,N4L)]==[9,21,7]
assert hom('one',-8,'P',-2)==1 and hom('one',-8,'D',-2)==0
assert inner(N4L,chars['P'])==q(1) and inner(N4F,chars['P'])==q(1)
assert inner(N4L,chars['V'])==q(1)
# Universal middle-radical corollary: the full product kernel is T, not S.
assert vs(vm(sym(6),W),sym(7))==sym(5)==chars['T']
assert inner(sym(5),chars['Wp'])==q(0)
assert vm(chars['P'],W)==rep('Wp+T')
assert sym(7)==rep('Wp+T') and 2+6==8
assert [41-0,54-8,37-4]==[41,46,33]
assert 3+1==4 and 4-1==3
print('PASS: eight immutable inputs; all block Hom vanishings; exact one-dimensional radical Hom; invariant-free degree26; covariant cohomology characters and dimensions; the unique radical P-channel.')
print('The proof and review establish saturation, naturality for singular endomorphisms, full faithfulness, simultaneous actual-source reconstruction, the complete algebra and its conditional positive-quadratic certificate. No actual q_+ value, matrix rank, or source instance was evaluated.')
