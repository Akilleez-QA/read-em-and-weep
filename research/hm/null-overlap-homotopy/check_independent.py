#!/usr/bin/env python3
"""Independent formal typed-operator rewrites; no geometric data or imports."""
from collections import defaultdict
import json
checks=[]
def check(condition,name):
    if not condition: raise RuntimeError(name)
    checks.append(name)
def add(*polys):
    out=defaultdict(int)
    for p in polys:
        for w,c in p.items(): out[w]+=c
    return {w:c for w,c in out.items() if c}
def neg(p):return {w:-c for w,c in p.items()}
deg={'L':0,'H':-1,'R':-1,'J':-1,'j':0,'d':1,'c':0,'D':0,'P':0}
def normalize(poly):
    done={}
    pending=dict(poly)
    while pending:
        word,c=pending.popitem()
        replacements=None
        for k,t in enumerate(word):
            if t=='P' and sum(deg[a] for a in word[k+1:])!=0:
                replacements={};break
        if replacements is None:
            for k in range(len(word)-1):
                a,b=word[k:k+2]
                if (a,b) in [('L','d'),('d','j')]: replacements={};break
                if (a,b)==('H','d'): replacements={():1,('P',):-1,('d','H'):-1};break
                if (a,b)==('d','J'): replacements={('c','j'):1,('j','D'):-1};break
                if (a,b)==('c','d'): replacements={('d','c'):1};break
                if (a,b)==('L','c'): replacements={('c','L'):1};break
        if replacements is None:done=add(done,{word:c});continue
        if replacements:
            pending=add(pending,{word[:k]+w+word[k+2:]:c*v for w,v in replacements.items()})
    return done
# Substitute C-C0=dR+Rd into both overlap families, without deleting any term.
start={tuple(w.split()):1 for w in ['L H d R J','L H R d J','L H c H d R j','L H c H R d j']}
expected={tuple(w.split()):v for w,v in [('L R J',1),('L H R c j',1),('L H c R j',1),('c L H R j',-1),('L H R j D',-1)]}
check(normalize(start)==expected,'full-four-term-contraction-rewrite')
for word in expected:
    wrong=dict(expected);wrong.pop(word)
    check(bool(add(normalize(start),neg(wrong))),'omission-detected-'+''.join(word))
wrong=dict(expected);wrong[('L','H','R','j','D')]=1
check(normalize(start)!=wrong,'nonclosed-sign-flip-detected')
# Connection differences cancel owner-independent representation anomalies.
check(add({('Gamma_j',):1,('anomaly',):-1},{('Gamma_i',):-1,('anomaly',):1})=={('Gamma_j',):1,('Gamma_i',):-1},'common-anomaly-cancels')
# Edge-only pole envelope; none assigned to a single connection coefficient.
bounds={'Aedge':(5,1),'Xi':(11,4),'Q':(21,9),'QZ':(40,16),'QDeltaZ':(48,20)}
check(tuple(a+b for a,b in zip((5,1),(6,3)))==bounds['Xi'],'Xi-envelope')
check(tuple(a+b+c for a,b,c in zip((6,3),bounds['Xi'],(4,2)))==bounds['Q'],'Q-envelope')
check(tuple(a+b for a,b in zip(bounds['Q'],(19,7)))==bounds['QZ'],'QZ-envelope')
check(tuple(a+b for a,b in zip(bounds['Q'],(27,11)))==bounds['QDeltaZ'],'QDeltaZ-envelope')
check(all(x<=y for x,y in zip(bounds['QDeltaZ'],(54,29))),'ordinary-weight-dominates')
print(json.dumps({'status':'pass','scope':'formal operator rewrite and conditional envelope arithmetic only','checks':checks},indent=2))
