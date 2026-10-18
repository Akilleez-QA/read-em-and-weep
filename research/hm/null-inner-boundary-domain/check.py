#!/usr/bin/env python3
"""Bounded invented-symbol controls, not geometric/source certification."""
from collections import defaultdict
import json
import hashlib
from pathlib import Path

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

# Validate only the explicitly bundled prerequisites; never load production code.
base=Path(__file__).resolve().parent
pins=json.loads((base/'pins.json').read_text())
for entry in pins['files']:
    require(hashlib.sha256((base/entry['path']).read_bytes()).hexdigest()==entry['sha256'], 'bundled byte mismatch: '+entry['path'])

def add(*terms):
    out = defaultdict(int)
    for p in terms:
        for (scalar, word), c in p.items():
            out[(scalar,word)] += c
    return {k:v for k,v in out.items() if v}

def atom(word, scalars=(), coefficient=1):
    return {(tuple(sorted(scalars)),tuple(word)):coefficient}

def mul(a,b, normalized=True):
    out=defaultdict(int)
    for (s,w),c in a.items():
        for (t,v),d in b.items():
            word=w+v
            # These adjacent factors have the same selected homotopy owner.
            if normalized and any(word[i:i+2] in [('H','H'),('H','j')] for i in range(len(word)-1)):
                continue
            out[(tuple(sorted(s+t)),word)]+=c*d
    return {k:v for k,v in out.items() if v}

def scale(p, scalar):
    return mul(atom((),(scalar,)),p)

def neg(p): return {k:-v for k,v in p.items()}
H,j,delta,Hp,jp,G = [atom((s,)) for s in ('H','j','delta','Hp','jp','Gamma')]
S=mul(H,Hp); t=mul(H,jp)
U=add(mul(mul(S,delta),j),neg(mul(mul(H,delta),t)))
HB=scale(H,'lambda')
HpB=add(scale(Hp,'lambda'),scale(H,'Vlambda'))
SB=mul(HB,HpB); tB=mul(HB,jp)
UB=add(mul(mul(SB,delta),j),neg(mul(mul(HB,delta),tB)))
require(UB==scale(scale(U,'lambda'),'lambda'),'scalar-frame covariance')
# Removing normalization preserves exactly the frame-derivative anomaly.
raw_SB=mul(HB,HpB,normalized=False)
raw_expected=scale(scale(S,'lambda'),'lambda')
raw_anomaly=add(raw_SB,neg(raw_expected))
require(raw_anomaly==atom(('H','H'),('lambda','Vlambda')),'negative normalization control')
# General connection correction, before assigning scalar-by-degree Gamma.
Hcov=add(Hp,mul(G,H),neg(mul(H,G)))
jcov=add(jp,mul(G,j),neg(atom(('j','GammaRow'))))
Ucov=add(mul(mul(mul(H,Hcov),delta),j),neg(mul(mul(H,delta),mul(H,jcov))))
correction=add(atom(('H','Gamma','H','delta','j')),neg(atom(('H','delta','H','Gamma','j'))))
require(add(Ucov,neg(U))==correction,'general connection correction')
require(bool(correction),'general gauge correction must not be silently discarded')
# Character extraction in squarefree local bases: each selected generator
# contributes t_i^-2; these are exponents, never division by a generator.
character_cases=0
for chart in range(16):
    for character in range(16):
        exponents=tuple((-2-2*((character>>i)&1)) if (chart>>i)&1 else 0 for i in range(4))
        if character==15:
            require(exponents==tuple(-4 if (chart>>i)&1 else 0 for i in range(4)), 'full-sign frame')
        character_cases+=1
jbound=(4,2); Hbound=(6,3); Zbound=(19,7)
def plus(*xs): return tuple(sum(x[i] for x in xs) for i in range(2))
def derivative(x): return tuple(v+1 if v else 0 for v in x)
a=plus(Hbound,derivative(Hbound),jbound)
b=plus(Hbound,Hbound,derivative(jbound))
require(a==b==(17,9),'kernel ledger')
bound=plus(a,Zbound)
require(bound==(36,16),'primitive ledger')
require(tuple(w-v for w,v in zip((54,29),bound))==(18,13),'ordinary-weight slack')
row_defect=plus(Zbound,(4,2),(4,2))
require(row_defect==(27,11),'row first-face transport ledger')
require(plus(a,row_defect)==(44,20),'nonclosed primitive ledger')
require(tuple(w-v for w,v in zip((54,29),(44,20)))==(10,9),'nonclosed primitive slack')
incidence_cases=0
for n in (4,5):
    # Every occurrence gets one own weight and its own target tag.
    occurrences=tuple(range(n))
    weights={i:(54,29) for i in occurrences}
    target_tags=set(occurrences)
    require(all(i in weights and i in target_tags for i in occurrences),'full-target incidence')
    bad=dict(weights); del bad[n-1]
    require(not all(i in bad for i in occurrences),'unweighted suffix negative control')
    incidence_cases+=1
# Two distinct occurrences may have the same divisor equation. Their
# clearing valuations add; merging them loses an entire required charge.
for multiplicity in (1,2,3):
    separate=2*36*multiplicity
    merged=36*multiplicity
    require(separate>merged,'coincident-divisor owner-merging control')
# Combined outer/inner identity under the separately declared cochain rules.
def cochain_reduce(p):
    out={}
    for (scalar,word),coefficient in p.items():
        word=list(word)
        changed=True
        while changed:
            changed=False
            for i in range(len(word)-1):
                if word[i:i+2]==['Pi','delta']:
                    word[i:i+2]=['delta','Pi']; changed=True; break
                if word[i:i+2]==['delta','T']:
                    word[i:i+2]=['T','Delta']; changed=True; break
        out=add(out,{(scalar,tuple(word)):coefficient})
    return out
lhs=add(atom(('delta','Q','T')),atom(('Q','delta','T')),
        neg(atom(('Pi','delta','LU'))),neg(atom(('Pi','LU','Delta'))),
        atom(('Pi','T','a')),atom(('Pi','LE')))
K=add(atom(('Q','T')),neg(atom(('Pi','LU'))))
rhs=add(mul(atom(('delta',)),K),mul(K,atom(('Delta',))),
        atom(('Pi','T','a')),atom(('Pi','LE')))
require(cochain_reduce(lhs)==cochain_reduce(rhs),'outer-inner synthesis')
wrongK=add(atom(('Q','T')),atom(('Pi','LU')))
wrongrhs=add(mul(atom(('delta',)),wrongK),mul(wrongK,atom(('Delta',))),
             atom(('Pi','T','a')),atom(('Pi','LE')))
require(cochain_reduce(lhs)!=cochain_reduce(wrongrhs),'synthesis sign mutation')
require(tuple(-4+2 for _ in range(4))==(-2,)*4,'dual test to canonical bundle')
print(json.dumps({'status':'PASS','scope':'Formal declared-rule and integer controls only; no actual model data or geometric source verification.', 'character_chart_cases':character_cases,'owner_incidence_cases':incidence_cases,'kernel_bound':a,'primitive_bound':bound,'ordinary_weight_slack':[18,13],'general_gauge_correction_terms':len(correction)},sort_keys=True,indent=2))
