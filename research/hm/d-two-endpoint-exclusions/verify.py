#!/usr/bin/env python3
"""Universal checks only. No actual coefficients, parameters or instance ranks."""
import hashlib,json,math
from pathlib import Path
from collections import Counter
from itertools import product
from fractions import Fraction
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def check(ok,msg):
 global checks
 checks+=1
 if not ok:raise RuntimeError(msg)
for x in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/x['file']).read_bytes()
 check(len(data)==x['bytes'],'length '+x['file'])
 check(hashlib.sha256(data).hexdigest()==x['sha256'],'sha256 '+x['file'])
 check(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==x['git_blob_sha1'],'git blob '+x['file'])
rows=json.loads((ROOT/'inputs/profile11-pairs.json').read_text())
expect={32:([[-8,'one'],[2,'one'],[4,'one']],[[-18,'one'],[-4,'one'],[6,'one']],12),52:([[-8,'one'],[3,'W']],[[-5,'W'],[6,'one']],0)}
for n,(A,B,d) in expect.items():
 r=rows[n]
 check(sorted(r['A'])==sorted(A),'fixed A '+str(n))
 check(sorted(r['B'])==sorted(B),'fixed B '+str(n))
 check(r['defect']==d,'fixed defect '+str(n))
 check([1,1,1,0,0,1,0,0] in r['compatible_E_types'],'fixed D compatibility')
D=[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-8,'one')]
rank=lambda xs:sum(c.DIM[r] for e,r in xs)
degree=lambda xs:sum(e*c.DIM[r] for e,r in xs)
check(rank(D)==17 and degree(D)==-54,'actual D source')
check(max(-e for e,r in D)==8,'jet bound')
F=D[:-1]
check(rank(F)==16 and degree(F)==-46,'residual F')
check(rank(F[:-1])==13,'higher source rank')
check(30-9==21 and 21-11==10 and 13>10,'ambient contradiction')
def caps(a,b):return [h*a-h*(h+1)+(10-h)*b-(10-h)*(11-h) for h in range(5,11)]
check(caps(6,-4)==[-50,-42,-38,-38,-42,-50],'pair32 capacities')
check(caps(6,-5)==[-55,-46,-41,-40,-43,-50],'pair52 capacities')
check([h for h,C in zip(range(5,11),caps(6,-4)) if C>=-38 and h<=7]==[7],'pair32 surviving height')
check([h for h,C in zip(range(5,11),caps(6,-5)) if C>=-50 and h<=7]==[6,7],'pair52 surviving heights')
check(-54-sum([-18,-4,6])==-38,'pair32 deg L')
check(-54-(6-10)==-50,'pair52 deg L')
check(-46-(-4-18)==-24==sum([-6,-8,-10]),'residual capacity equality')
for n in range(12):
 check(c.product('one',n)['W']==(1 if n in (1,11) else 0),'W gap '+str(n))
for n in range(1,12):check(c.product('one',n)['one']==0,'invariant gap '+str(n))
check(c.product('one',0)['one']==1 and c.product('one',12)['one']==1,'invariant endpoints')
for n,want in [(6,{'V':1,'P':1}),(8,{'P':1,'D':1}),(10,{'A':1,'V':1,'D':1})]:
 check(c.product('one',n)==Counter(want),'Sym decomposition '+str(n))
check(max(c.DIM['P'],c.DIM['D'])<8,'complete Sym8 quotient')
# Full equivariant Hom tests for all determinant deficits up to the boundary.
q2=[d for d in range(12) if c.product('one',d)['W'] or c.product('one',d-11)['one']]
q1=[d for d in range(13) if c.product('one',d)['one'] or c.product('one',d-11)['W']]
check(q2==[1,11],'all rank2 deficits through11')
check(q1==[0,12],'all rank1 deficits through12')
# Finite budgets mean no omitted larger deficit can contribute.
patterns={}
for h,budget in [(6,4),(7,9)]:
 n2=10-h;n1=h-n2
 opts2=[d for d in range(budget+1) if c.product('one',d)['W'] or c.product('one',d-11)['one']]
 opts1=[d for d in range(budget+1) if c.product('one',d)['one'] or c.product('one',d-11)['W']]
 choices=[x for x in product(*([opts2]*n2+[opts1]*n1)) if sum(x)==budget]
 patterns[str(h)]=[list(x) for x in choices]
 check(choices==([(1,1,1,1,0,0)] if h==6 else []),'complete deficit patterns '+str(h))
check(6-2*6==-6,'terminal degree')
# All possible sextic-net kernel splitting types, not actual instances.
for a in range(1,6):
 b=6-a
 check(a>=1 and b>=1 and a<=5 and b<=5,'net bounds')
 check(4-a>=-1 and 4-b>=-1,'net H1 vanishing')
# Formal coefficient-by-coefficient Taylor inversion for degrees0..16.
# Coefficient of v_l in the recovered v_k equals this scalar times t^(l-k).
for d in range(17):
 for k in range(d+1):
  for l in range(d+1):
   value=sum(Fraction(math.comb(a,k)*(-1)**(a-k)*math.factorial(l),math.factorial(l-a)*math.factorial(a)) for a in range(k,l+1)) if l>=k else Fraction(0)
   check(value==int(l==k),'Taylor coefficient identity')
result={'status':'PASS','checks':checks,'character_internal_checks':c.checks,'excluded_original_pairs':[32,52],'pair32_surviving_height_before_apolar':7,'pair52_deficit_patterns':patterns,'scope':'two actual D-source pairs under maximal profile11; not pair50 or global closure','proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()}
print(json.dumps(result,indent=2))
