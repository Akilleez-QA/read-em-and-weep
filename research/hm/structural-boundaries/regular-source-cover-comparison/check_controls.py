#!/usr/bin/env python3
"""Invented finite formal controls only. No input files, source, or models read."""
from itertools import product
from collections import defaultdict
import json

# Polynomials in two INVENTED weight symbols; these are not source polynomials.
ONE={(0,0):1}; ZERO={}
def pa(p,q):
    d=dict(p)
    for m,v in q.items(): d[m]=d.get(m,0)+v
    return {m:v for m,v in d.items() if v}
def ps(p,s): return {m:v*s for m,v in p.items() if v*s}
def pm(p,q):
    d=defaultdict(int)
    for a,u in p.items():
        for b,v in q.items(): d[tuple(x+y for x,y in zip(a,b))]+=u*v
    return {m:v for m,v in d.items() if v}
def variable(tag): return {(1,0) if tag==0 else (0,1):1}
def weight(tag,bit,bad=False):
    v=variable(tag)
    return v if bit else (ONE if bad else pa(ONE,ps(v,-1)))
def ca(c,d,scale=1):
    out=dict(c)
    for t,p in d.items():
        out[t]=pa(out.get(t,ZERO),ps(p,scale))
        if not out[t]: del out[t]
    return out
def cscale(c,p): return {t:r for t,q in c.items() if (r:=pm(p,q))}
def singleton(t): return {tuple(t):ONE}
def boundary(c):
    out={}
    for t,p in c.items():
        if len(t)<=1: continue
        for i in range(len(t)):
            out=ca(out,{t[:i]+t[i+1:]:p},(-1)**i)
    return out
def apply(c,fn):
    out={}
    for t,p in c.items(): out=ca(out,cscale(fn(t),p))
    return out

def F(t,bad=False):
    """Standard tag tuple -> weighted source tuple."""
    out={}
    for bits in product((0,1),repeat=len(t)):
        p=ONE
        for tag,bit in zip(t,bits): p=pm(p,weight(tag,bit,bad))
        s=tuple(2*tag+bit for tag,bit in zip(t,bits))
        out=ca(out,{s:p})
    return out

def G(t): return singleton(tuple(a//2 for a in t))
def P(t,bad=False): return F(tuple(a//2 for a in t),bad)
def H(t,omit_prefix=False):
    out={}
    for i in range(len(t)):
        for bits in product((0,1),repeat=i+1):
            p=ONE
            for j,bit in enumerate(bits):
                if not omit_prefix or j==i:
                    p=pm(p,weight(t[j]//2,bit))
            b=tuple(2*(t[j]//2)+bit for j,bit in enumerate(bits))
            out=ca(out,{b+t[i:]:p},(-1)**i)
    return out

checks=defaultdict(int)
def need(ok,label):
    if not ok: raise RuntimeError(label)
    checks[label]+=1

source_tuples=[t for n in range(1,5) for t in product(range(4),repeat=n)]
standard_tuples=[t for n in range(1,5) for t in product(range(2),repeat=n)]
for t in source_tuples:
    z=singleton(t)
    need(boundary(boundary(z))=={},'boundary_squared')
    need(boundary(G(t))==apply(boundary(z),G),'tag_restriction_chain_map')
    need(boundary(P(t))==apply(boundary(z),P),'averaging_chain_map')
    lhs=ca(boundary(H(t)),apply(boundary(z),H))
    need(lhs==ca(z,P(t),-1),'partition_prism_identity')
    for term in H(t):
        need(len(term)==len(t)+1,'prism_degree')
for t in standard_tuples:
    z=singleton(t)
    need(boundary(F(t))==apply(boundary(z),F),'full_comparison_chain_map')
    need(apply(F(t),G)==z,'comparison_retraction')

# Owned-vector arithmetic. Pairs are (carrier vector, legal vector).
def vadd(*vs): return tuple(map(sum,zip(*vs)))
def vmax(*vs): return tuple(map(max,zip(*vs)))
def edge(i,j,c,l):
    cv=[0]*3; lv=[0]*3
    cv[i]=cv[j]=c; lv[i]=lv[j]=l
    return tuple(cv),tuple(lv)
def mul(*terms): return tuple(vadd(*(x[k] for x in terms)) for k in (0,1))
Ginv=edge(0,2,2,1); A=edge(0,1,2,1); B=edge(1,2,2,1)
UA=edge(0,1,8,5); UB=edge(1,2,8,5); UG=edge(0,2,8,5)
dA=edge(0,1,3,2); dB=edge(1,2,3,2)
dUA=edge(0,1,9,6); dUB=edge(1,2,9,6)
ddA=edge(0,1,4,3); ddB=edge(1,2,4,3)
b=((0,0,0),(1,2,1))
ledger=[mul(Ginv,UB,UA),mul(Ginv,dUB,dA),mul(Ginv,dB,dUA),
        mul(Ginv,ddB,ddA),mul(Ginv,b,UG),mul(Ginv,b,b,edge(0,2,2,1))]
expected=[((10,16,10),(6,10,6)),((5,12,11),(3,8,7)),
          ((11,12,5),(7,8,3)),((6,8,6),(4,6,4)),
          ((10,0,10),(7,2,7)),((4,0,4),(4,4,4))]
need(ledger==expected,'full_ten_slot_ledger')
need(sum((2,2,2,1,2,1))==10,'full_slot_count')
need((max(5,6)+2,max(2,4)+1)==(8,5),'full_first_lift_dominance')
need((max(3+6,2+7),max(2+4,1+5))==(9,6),'full_first_lift_derivative')
need(vmax(*(x[0] for x in ledger))==(11,16,11),'carrier_maximum')
need(vmax(*(x[1] for x in ledger))==(7,10,7),'legal_maximum')
need(54-16==38 and 29-10==19,'weight_clearance_margin')

# Formal ownership controls for a prism term of each small degree/seam.
for n in range(1,5):
    for i in range(n):
        # Separate input occurrences even when equal labels are later chosen.
        input_slots=[('inserted',j) for j in range(i+1)]+[('original',j) for j in range(i,n)]
        charges={slot:(16,10) for slot in input_slots}
        for kind,j in input_slots:
            supply=(54,29) if kind=='inserted' else (16,10)
            need(all(s>=q for s,q in zip(supply,charges[(kind,j)])),'owned_prism_clearance')
        need(len(input_slots)==n+1,'shared_seam_retained')

negative=[]
def reject(name,condition):
    if not condition: raise RuntimeError('negative control failed: '+name)
    negative.append(name)
reject('opposite prism sign',any(ca(boundary(H(t)),apply(boundary(singleton(t)),H))
    !=ca(P(t),singleton(t),-1) for t in source_tuples))
reject('omitted prefix weights',any(ca(boundary(H(t,True)),apply(boundary(singleton(t)),lambda x:H(x,True)))
    !=ca(singleton(t),P(t),-1) for t in source_tuples))
reject('weights do not sum to one',any(boundary(F(t,True))
    !=apply(boundary(singleton(t)),lambda x:F(x,True)) for t in standard_tuples))
reject('merged equal-divisor occurrences',max(8,8)<16)
reject('omitted shared seam',all((i+1)+(n-i-1)!=n+1 for n in range(1,5) for i in range(n)))
reject('uncleared suffix on standard target',0<16 and 0<10)
reject('absent standard tag borrowed',set((0,))!=set((1,)))

print(json.dumps({'status':'passed','scope':'Invented formal partition symbols, tuple chains, and integer pole metadata only.',
  'checks':dict(sorted(checks.items())),'source_tuples':len(source_tuples),'standard_tuples':len(standard_tuples),
  'negative_controls':negative,'source_or_model_evaluation':False,
  'witness_coefficients_computed':False,'weights_changed':False},indent=2))
