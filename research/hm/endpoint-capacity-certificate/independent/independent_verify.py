"""Independent exact synthetic oracle. Usage: python independent_verify.py PACKET_DIR"""
import copy
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys
p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / 'endpoint-capacity-certificate'
spec = importlib.util.spec_from_file_location('reviewed_capacity', p / 'capacity.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
counts = {}
def check(ok, label):
    if not ok: raise RuntimeError(label)
    counts[label] = counts.get(label, 0) + 1
def reject(f):
    try: f()
    except ValueError: return True
    return False
def original(n, x, y, h):
    k = n-h
    return h*x+k*y-h*(h+1)-k*(k+1)
def exhaustive(n,x,y):
    vals = [(original(n,x,y,h),h) for h in range((n+1)//2,n+1)]
    best = max(v for v,h in vals)
    return best, [h for v,h in vals if v == best]
for n in range(1,36):
    for y in range(-17,18):
        for gap in range(61):
            x=y+gap; c=m.solve(n,x,y); best, hs=exhaustive(n,x,y)
            check((c['maximum'],c['heights']) == (best,hs) and m.verify(c), 'synthetic_exhaustive')
            for t in (x-hs[0]-1,x-hs[0],x-hs[-1]):
                f=m.equality_filter(c,best,t,actual_top_flags_proved=True)
                check(f['surviving_heights']==[h for h in hs if x-2*h<=t-h] and f['unfiltered_capacity']==best,'equality_boundaries')
            check(reject(lambda: m.equality_filter(c,best-1,x-n-100,actual_top_flags_proved=True)), 'strict_inequality_not_filtered')
# Acceptance soundness and completeness: supply independently formed certificates
# for EVERY singleton and pair, not just mutations of the solver's answer.
for n in range(1,13):
    for y in (-9,0,7):
        for gap in range(29):
            x=y+gap; best, hs=exhaustive(n,x,y); dom=range((n+1)//2,n+1)
            for size in (1,2):
                for choice in itertools.combinations(dom,size):
                    h=choice[0]
                    c=dict(rank=n,lambda1=x,lambda2=y,maximum=original(n,x,y,h),heights=list(choice),square_distance=(4*h-(x-y+2*n))**2)
                    check((not reject(lambda: m.verify(c))) == (list(choice)==hs),'certificate_acceptance_exhaustive')
# A separate discrete derivative binary search oracle, valid at arbitrary size.
def binary_oracle(n,x,y):
    lo=(n+1)//2; hi=n
    while lo<hi:
        h=(lo+hi)//2
        if original(n,x,y,h+1)>original(n,x,y,h): lo=h+1
        else: hi=h
    hs=[lo]
    if lo<n and original(n,x,y,lo+1)==original(n,x,y,lo): hs.append(lo+1)
    return original(n,x,y,lo),hs
for n in (10**80,10**80+1,10**80+2):
    for gap in (0,1,2,3,4,2*n-3,2*n-2,2*n-1,2*n,2*n+1,10**120):
        for y in (-10**150,0,10**150):
            c=m.solve(n,y+gap,y)
            check((c['maximum'],c['heights'])==binary_oracle(n,y+gap,y) and m.verify(c),'huge_binary_oracle')
base=m.solve(6,2,0)
for key in ('rank','lambda1','lambda2','maximum','square_distance'):
    for val in (True,False,1.0,'1',None,[],{}):
        c=copy.deepcopy(base); c[key]=val
        check(reject(lambda: m.verify(c)),'malformed_scalars')
for val in (None,(),{},[True],[3.0],[3,4,5],[],[4,3],[3,3],[-1],[100]):
    c=copy.deepcopy(base); c['heights']=val
    check(reject(lambda: m.verify(c)),'malformed_heights')
for flag in (False,None,0,1,'true',[],{}):
    check(reject(lambda: m.equality_filter(base,base['maximum'],0,actual_top_flags_proved=flag)),'flag_gate')
for deg in (base['maximum']-1,base['maximum']+1,True,False,1.0,None):
    check(reject(lambda: m.equality_filter(base,deg,0,actual_top_flags_proved=True)),'degree_gate')
for args in ((0,0,0),(-1,0,0),(1,-1,0),(True,1,0),(2,False,0),(2,1,0.0)):
    check(reject(lambda: m.solve(*args)),'invalid_domain')
print(json.dumps({'status':'PASS','checks':counts,'total':sum(counts.values()),'scope':'Synthetic arithmetic only; no new actual-profile exclusion.','capacity_sha256':hashlib.sha256((p/'capacity.py').read_bytes()).hexdigest()},indent=2,sort_keys=True))
