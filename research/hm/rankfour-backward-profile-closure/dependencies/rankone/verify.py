#!/usr/bin/env python3
"""Conditional rank-one-image exclusion by universal abstract bundle tests."""
from pathlib import Path
import importlib.util,json,hashlib
ROOT=Path(__file__).resolve().parent
p=ROOT/'dependency'/'verify.py'
if hashlib.sha256(p.read_bytes()).hexdigest()!='8bfaf601c8817fb0ab3af19a5aff734efdad09a318491c1bec7d8430818cb0f6':raise RuntimeError('Dependency checker hash')
s=importlib.util.spec_from_file_location('c',p);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
checks=0
def require(test,why):
 global checks
 checks+=1
 if not test:raise RuntimeError(why)
require(hashlib.sha256((ROOT/'dependency'/'PROOF.md').read_bytes()).hexdigest()=='f6f807996ccca5b05233af8964bbbaa4f3913f79e4955ea2b4906462db3f2751','Dependency proof hash')
old=c.derive();require(old==json.loads((ROOT/'dependency'/'RESULT.json').read_text()),'Retained full lower-image replay')
require([e for e in range(10)if c.image_eligible(e,0)]==[9],'Complete rank-one image degree domain')
require(c.cooccur_image(((9,0),))==['D'],'Actual rank-one source forced D')
J=((9,0),);lo,domain=c.N_domain(J)
other=tuple(sorted(bs for d in range(6,19,2) for bs in c.split_by_ordinary_degrees(3,d,6)))
require(lo==-6 and domain==other and len(domain)==53,'Complete independent rank-three domain')
ledger=c.first_ledger();require(ledger==c.second_ledger(),'Complete defect ledger')
records=[];low=[];high=[]
for N in domain:
 B=tuple(sorted(N+c.C(J)));d=c.degree_of(B);m=c.margin(J,N);targets=c.target_types(N)
 require(c.rank_of(N)==3 and c.degree_of(N)==d+8,'Actual rank/degree kernel')
 require(min(e for e,i in N)>=-6 and max(e for e,i in N)<=6,'Ordinary slope window')
 require(c.ext_character(J,N)==c.ZERO,'Ordinary extension vanishes')
 require(c.class_decompose(c.class_chi(N,3))==c.chi(N,3),'Independent class Euler')
 passed=c.genuine(m)and bool(targets)
 rec={'kernel':c.shape(N),'c3':d,'margin':c.pretty(m),'dual_targets':targets,'passes':passed}
 records.append(rec)
 if not passed:continue
 rows=[r for r in ledger if r[3][2]==d];require(bool(rows),'Actual degree rows exist')
 if d in(-2,0):
  require(all(r[2][0]==r[2][1]==0 for r in rows),'Only lower defects vanish in low cases')
  a=-24 if d==-2 else -30;require(all(r[0]==a for r in rows),'Forced lower endpoint degree')
  dom=c.split_by_blocks(5,a,-4);require(dom==c.split_by_ordinary_degrees(5,a,-4),'Two endpoint enumerations')
  survivors=[]
  for ep in dom:
   for t in(3,4):
    require(c.class_decompose(c.class_chi(ep,t))==c.chi(ep,t),'Endpoint class crosscheck')
    require(c.class_decompose(c.bottom_B_class(B,t))==c.bottom_B(B,t),'Target class crosscheck')
   if all(c.chi(ep,t)==c.bottom_B(B,t)for t in(3,4)):survivors.append(ep)
  require(not survivors,'No low endpoint survives both twists')
  low.append(dict(rec,endpoint_degree=a,endpoint_domain=len(dom),survivors=0,defect_rows=[c.ledger_row(r)for r in rows]))
 else:
  require(d>0 and all(r[2][2]==0 for r in rows),'Third defect zero only in high cases')
  dual=c.dual(B);eul=c.sub(c.Qstar(4),c.chi(dual,2));target=c.h0(dual,0)
  require(c.class_decompose(c.cadd(c.class_Qstar(4),c.cmul(c.class_chi(dual,2),-1)))==eul,'Independent upper Euler')
  require(c.class_decompose(c.class_h0(dual,0))==target,'Independent upper target')
  require(eul[8]==1 and target[8]==0,'Physical V top-section obstruction')
  high.append(dict(rec,upper_euler=c.pretty(eul),upper_target=c.pretty(target),V_margin=eul[8]-target[8],defect_rows=[c.ledger_row(r)for r in rows]))
require(len(low)==7 and len(high)==9,'Complete sixteen-case exclusion')
require(sum(r['passes']for r in records)==16,'Finite filtered domain')
# Nonvacuous controls: the same top-section test must not claim an A obstruction in every case.
require(any(r['upper_euler'].get('A',0)<=r['upper_target'].get('A',0)for r in high),'Physical marking matters')
print(json.dumps({'claim':'Rank-one restricted dual cubic image excluded under retained actual premises.','actual_instances_evaluated':False,'new_checks':checks,'dependency_checks':old['checks'],'raw_domain':records,'low_exclusions':low,'upper_exclusions':high,'counts':[53,16,7,9],'complete_profile_claim':False},sort_keys=True,indent=2))
