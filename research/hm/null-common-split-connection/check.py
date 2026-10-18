#!/usr/bin/env python3
"""Static bytes and invented free-word/exponent controls. No production import."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
checks = []
def need(ok, name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

def add(*ps):
    out = {}
    for p in ps:
        for w, c in p.items():
            out[w] = out.get(w, 0) + c
    return {w:c for w,c in out.items() if c}
def scale(c, p): return {w:c*v for w,v in p.items() if c*v}
def mul(*ps):
    out = {():1}
    for p in ps:
        n = {}
        for a,x in out.items():
            for b,y in p.items(): n[a+b] = n.get(a+b,0) + x*y
        out = {w:c for w,c in n.items() if c}
    return out
def atom(s): return {(s,):1}
def neg(p): return scale(-1,p)
def comm(a,b): return add(mul(a,b),neg(mul(b,a)))
def deriv(p, rules):
    out = {}
    for w,c in p.items():
        for i,a in enumerate(w):
            out = add(out,scale(c,mul({w[:i]:1}, rules.get(a,{}), {w[i+1:]:1})))
    return out

pins = json.loads((ROOT/'pins.json').read_text())
for entry in pins['files']:
    need(hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest()==entry['sha256'], 'hash:'+entry['path'])
raw=(ROOT/'inputs/raw_engine.py.txt').read_text()
need(hashlib.sha256(raw.encode()).hexdigest()=='c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9','frozen-raw-source')
tree=ast.parse(raw)
cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='PhysicalModel')
blocks=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='blocks')
need(blocks.lineno==140 and blocks.end_lineno==155,'blocks-exact-lines')
# All arithmetic below is on integer exponents or invented free symbols.
weights=(-1,1,3,5)
local=((0,)*5,(-2,)*5+(0,-2)+(2,)*8,(0,)*8+(2,)*2,(0,)*2)
common=tuple(tuple(x+k for x in a) for k,a in zip(weights,local))
need(common==((-1,)*5,(-1,)*5+(1,-1)+(3,)*8,(3,)*8+(5,)*2,(5,)*2),'actual-common-frame-exponents')
need(common[0]==common[1][:5] and common[1][7:]==common[2][:8] and common[2][8:]==common[3],'three-differential-and-homotopy-pairs')
need(common[1][5:7]==(1,-1),'distinct-cohomology-weights')
# -D(U S)S^-1Q contributes minus column exponent times rho.
need(tuple(-x for x in common[1])==(1,)*5+(-1,1)+(-3,)*8,'Gamma0-column-rho')
need(tuple(-x for x in common[2])==(-3,)*8+(-5,)*2,'Gamma1-column-rho')
# alpha-rho: numerator after multiplication by 2x(x^2-1)/(m y).
# 2-(x^2+1)=-(x^2-1), represented by constant and x^2 coefficients.
need((2-1,-1)==(1,-1),'beta-minus-my-over-2x')
need(weights[0+2]-weights[0]==4 and weights[1+2]-weights[1]==4,'weight-gap-four')
need(2*(-2)==-4,'J2-scalar-connection-minus-four-beta')

G,H,D,j,L,Dp,Lp=map(atom,('G','H','delta','j','L','delta_prime','L_prime'))
C=comm(D,G)
J1=mul(H,D,j)
J2=neg(mul(H,D,J1))
rules={'H':neg(comm(G,H)),'j':neg(mul(G,j))}
J1p=add(neg(mul(G,J1)),neg(mul(H,C,j)))
J2p=add(neg(mul(G,J2)),mul(H,C,J1),mul(H,D,H,C,j))
need(deriv(J1,rules)==J1p,'J1-derivative')
need(deriv(J2,rules)==J2p,'J2-derivative')
need(deriv(mul(L,J2),dict(rules,L=Lp))==add(mul(add(Lp,neg(mul(L,G))),J2),mul(L,H,C,J1),mul(L,H,D,H,C,j)),'selected-derivative')
Ceff=add(C,neg(Dp))
need(deriv(J2,dict(rules,delta=Dp))==add(neg(mul(G,J2)),mul(H,Ceff,J1),mul(H,D,H,Ceff,j)),'moving-restrictions')
# First face changes the leading owner; later faces retain it.
Gi,Gj,X=map(atom,('G_i','G_j','X'))
need(add(mul(Gj,X),neg(mul(Gi,X)))==mul(add(Gj,neg(Gi)),X),'positive-first-face')
need(add(mul(Gi,X),neg(mul(Gi,X)))=={},'later-faces-cancel')
# Algebraic compatibility after Pi delta = delta Pi and delta T = T Delta.
outer,inner,TaLE,R=map(atom,('outer_boundary','inner_boundary','Ta_plus_LE','R_conn'))
need(add(outer,neg(inner),R,inner)==add(outer,R),'old-K-compatibility')
need(add(outer,neg(inner),R)!=add(outer,R),'old-K-naive-substitution-rejected')
# Independent diagnostic mutations must disagree with exact product derivative.
mutations={
 'opposite-exterior-G':add(mul(G,J2),mul(H,C,J1),mul(H,D,H,C,j)),
 'negative-first-C':add(neg(mul(G,J2)),neg(mul(H,C,J1)),mul(H,D,H,C,j)),
 'negative-second-C':add(neg(mul(G,J2)),mul(H,C,J1),neg(mul(H,D,H,C,j))),
 'missing-selector-G':add(mul(L,H,C,J1),mul(L,H,D,H,C,j)),
}
for name,value in mutations.items():
    target=mul(L,J2p) if name=='missing-selector-G' else deriv(J2,rules)
    need(value!=target,'reject:'+name)
need(local[0]!=common[0] and local[3]!=common[3],'reject:raw-local-shortcut')
need(common[1][5:7]!=(1,1),'reject:equal-cohomology-weights')
print(json.dumps({'status':'PASS','scope':'static text, integer exponents, invented noncommutative words only','checks':checks,'count':len(checks)},indent=2))
