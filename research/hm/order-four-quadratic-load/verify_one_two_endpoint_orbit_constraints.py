#!/usr/bin/env python3
"""Universal bounded characters and integer flags only; no map instances."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import runpy, contextlib, io, json, hashlib
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    r=runpy.run_path(str(ROOT/'verify_equivariant_splitting_gauss_persistence.py'))
names=tuple(r['reps']); reps=r['reps']; zero=(0,)*len(names)
def decomp(ch):
    out=tuple(r['inner'](ch,reps[n]) for n in names)
    assert all(b==0 and a.denominator==1 for a,b in out)
    return tuple(int(a) for a,b in out)
def add(*xs):return tuple(map(sum,zip(*xs))) if xs else zero
def neg(x):return tuple(-a for a in x)
def eff(x):return min(x)>=0
def dim(n):return int(reps[n][0][0])
def degree(B):return sum(e*dim(n) for e,n in B)
@lru_cache(None)
def prod(n,d):return decomp(r['vm'](reps[n],r['sym'](d)))
@lru_cache(None)
def hc(B,t=0,euler=False):
    return add(*(prod(n,e+t) if e+t>=0 else neg(prod(n,-e-t-2)) if euler and e+t<=-2 else zero for e,n in B))
@lru_cache(None)
def chiQ(t):
    def line(d):return r['sym'](d) if d>=0 else r['vs'](-1,r['sym'](-d-2)) if d<=-2 else r['vs'](0,r['one'])
    return decomp(r['va'](r['vm'](r['M3'],line(t-1)),r['vs'](-1,r['vm'](r['M2'],line(t)))))
def hom(e,n,f,m):return f>=e and prod(m,f-e)[names.index(n)]>0
# For rank seven and deg M >= -44, sum (j-3)dim R <=23, hence j<=26.
blocks=tuple((j,n) for j in range(3,27) for n in names
             if reps[n][1][0]==(-1)**j*dim(n))
@lru_cache(None)
def endpoint_shapes(excess):
    def rec(rank,exc,start):
        if rank==0:
            if exc==0:yield ()
            return
        for i in range(start,len(blocks)):
            j,n=blocks[i]; d=dim(n); x=(j-3)*d
            if d<=rank and x<=exc:
                for rest in rec(rank-d,exc-x,i):yield ((-j,n),)+rest
    return tuple(rec(7,excess,0))
@lru_cache(None)
def torsion(s,k,t):
    if not s:return zero
    return add(hc(((k,'one'),),t,True),neg(hc(((k-s,'one'),),t,True)))
def rank_one_possible(deg,c):
    # deg=7*last-42-sum(i*delta_i), 0<=last<=c<=4 here.
    lo=(deg+42+6)//7
    if c<lo:return False
    budget_max=7*c-42-deg
    sem={12*x+20*y+30*z for x in range(budget_max//12+1)
         for y in range(budget_max//20+1) for z in range(budget_max//30+1)
         if 12*x+20*y+30*z<=budget_max}
    for last in range(lo,c+1):
        if last%2 or c-last not in sem:continue
        budget=7*last-42-deg
        sums={0}
        for weight in range(1,7):
            sums={u+weight*v for u in sums for v in sem if u+weight*v<=budget}
        if budget in sums:return True
    return False
source=ROOT/'one-two-finite-quotient-pairs.json'
old=json.loads(source.read_text()); assert len(old['pairs'])==25
records=[]; stage_counts=[]; rank_one_rejections=[]
for i,pair in enumerate(old['pairs']):
    A=tuple(map(tuple,pair['A'])); B=tuple(map(tuple,pair['B'])); a=degree(A)
    assert -4<=a<=6 and degree(B)==-6-a
    for s in (0,12,20):
        if s>14-2*a:continue
        deg=-36+2*a+s; candidates=endpoint_shapes(-deg-21); pre=post=0
        for M in candidates:
            assert sum(dim(n) for e,n in M)==7 and degree(M)==deg
            d=-max(e for e,n in M)
            if not eff(add(hc(B,d-4),neg(hc(M,d)))):continue
            # The exact Euler recurrence makes twists 0,1 sufficient;
            # check 0..26 redundantly across the entire proven block window.
            ks=(0,) if s==0 else range(0,10 if s==12 else 6,2)
            good_k=[k for k in ks if all(add(hc(M,t,True),neg(chiQ(t)),hc(B,t,True),hc(B,t-2,True))==torsion(s,k,t) for t in range(27))]
            if not good_k:continue
            pre+=1
            targets=[(e-4,n) for e,n in B if any(hom(f,m,e-4,n) for f,m in M)]
            capacity=sum(dim(n) for e,n in targets)
            if capacity<=1:
                assert capacity==0 or targets[0][1]=='one'
                if not targets or not rank_one_possible(deg,targets[0][0]):
                    rank_one_rejections.append(dict(pair_id=i,s=s,M=M,targets=targets))
                    continue
            post+=1
            records.append(dict(pair_id=i,A=A,B=B,s=s,M=M,torsion_k=good_k,E_ids=pair['E_ids']))
        stage_counts.append(dict(pair_id=i,s=s,all_M=len(candidates),after_character_and_top=pre,after_rank_one=post))
pre_ids=sorted({x['pair_id'] for x in stage_counts if x['after_character_and_top']})
ids=sorted({x['pair_id'] for x in records})
assert pre_ids==[0,2,4,5,6,7,8,9,12,14,20,21,23,24]
assert ids==[0,2,4,6,7,8,12,14,20,21]
assert not any(x['s']==20 and x['after_character_and_top'] for x in stage_counts)
# Standalone envelope certificate for old pair18.
B=tuple(map(tuple,old['pairs'][18]['B']))
C=add(hc(B,-1),neg(chiQ(3)),hc(B,3,True),hc(B,1,True))
expected=tuple({'W':2,'Wp':1,'T':-1}.get(n,0) for n in names)
assert C==expected
out=dict(scope='Necessary overlist only; no realizability or global rank improvement.',
 inputs={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ('one-two-finite-quotient-pairs.json','verify_equivariant_splitting_gauss_persistence.py','verify_negative_vertex_scalar.py')},
 input_pair_count=25,character_top_pair_count=14,remaining_pair_count=10,
 remaining_pair_ids=ids,records=records,stage_counts=stage_counts,rank_one_rejections=rank_one_rejections)
(ROOT/'one-two-endpoint-orbit-constraints.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 25 -> 14 by endpoint characters/top slope -> 10 by backward rank-one flags.')
print('PASS: every second-dual twenty-defect branch excluded; remaining pair IDs:',ids)
print('Remaining endpoint records:',len(records),'by defect:',dict(Counter(x['s'] for x in records)))
print('Inherited compatible pair/E records:',sum(len(old['pairs'][i]['E_ids']) for i in ids))
print('No actual coefficients, points, instance matrices, rank evaluations or scans.')
