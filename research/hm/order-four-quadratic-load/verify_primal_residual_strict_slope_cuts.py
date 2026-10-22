#!/usr/bin/env python3
"""Bounded abstract section constraints on actual residual quotients."""
from pathlib import Path
from itertools import product
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={
'PRIMAL-EQUALITY-HAS-SIX-RESIDUAL-QUOTIENT-PARAMETER-SPACES.md':'de06847ba55aae35effb6ad394de4792b5c8813d48dbee35b4c1bed79935afa6',
'primal-equality-six-residual-quotients.json':'56174a13450e9b9e40ca7ab69ca52445cd9dabbbac5ad782ce4845405ac8570e',
'equality-gauss-rational-normal-subbundles.json':'c1930c3f8977515f75fc9359866dd9a143e2101322a3fd80a352a8357d15377f',
'NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md':'53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
names=['one','W','Wp','A','V','P','S','D','T'];dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]))
edges=[('one','W'),('W','A'),('A','S'),('S','D'),('D','T'),('T','V'),('T','P'),('P','Wp')]
def tensorW(v):
 out={n:0 for n in names}
 for a,b in edges:out[a]+=v.get(b,0);out[b]+=v.get(a,0)
 return {n:m for n,m in out.items()if m}
def add(*vs):return {n:sum(v.get(n,0)for v in vs)for n in names if sum(v.get(n,0)for v in vs)}
def sub(v,w):return {n:v.get(n,0)-w.get(n,0)for n in names if v.get(n,0)!=w.get(n,0)}
sym=[{'one':1},{'W':1}]
for t in range(2,9):sym.append(sub(tensorW(sym[-1]),sym[-2]))
assert sym[7]=={'Wp':1,'T':1} and sym[3]=={'S':1}
assert add(sym[7],sym[3])=={'Wp':1,'S':1,'T':1}
assert tensorW({'D':1})=={'S':1,'T':1}
assert sym[5]=={'T':1} and sym[4]=={'D':1}
prior=json.loads((ROOT/'primal-equality-six-residual-quotients.json').read_text())
records={r['type']:r for r in prior['records']};assert set(records)==set(range(1,7))
# Z6 source index zero is Wp O(-3); neither quotient row has this channel.
assert records[6]['residual_blocks'][0]==[-3,'Wp']
assert all(c['source_index']!=0 for c in records[6]['Hom_channels'])
assert sym[5].get('Wp',0)==0
# Z3 source zero is D O(-2); its sole channel is the alpha upper row.
assert records[3]['residual_blocks'][0]==[-2,'D']
assert [(c['target_degree'],c['source_index'])for c in records[3]['Hom_channels']if c['source_index']==0]==[(2,0)]
def small_h0(bs,r):
 out={}
 for degree,rep in bs:
  t=degree+r
  if t<0:continue
  assert t in [0,1]
  out=add(out,{rep:1}if t==0 else tensorW({rep:1}))
 return out
survivors=[]
conditions=[
 ('alpha != 0 and (a,b) != (0,0)',lambda alpha,beta,a,b:alpha and(a or b),4),
 ('alpha*a != 0',lambda alpha,beta,a:alpha and a,3),
 ('alpha != 0 and (a,b) != (0,0)',lambda alpha,beta,a,b:alpha and(a or b),4),
 ('alpha*b != 0',lambda alpha,beta,b:alpha and b,3),
 ('a != 0 and (alpha,beta) != (0,0)',lambda alpha,beta,a:a and(alpha or beta),3),
]
for typ,(description,predicate,nvars)in enumerate(conditions,1):
 bs=records[typ]['residual_blocks'];z2=small_h0(bs,2);z3=small_h0(bs,3)
 if typ in [1,3]:
  assert z2=={'D':1} and z3=={'S':1,'T':1}
  # Full Sym4 evaluation and its degree-one multiplication are surjective.
  n2=sub(z2,sym[4]);n3=sub(z3,sym[5])
 elif typ in [2,4]:
  assert z2=={} and z3=={'T':1};n2={};n3=sub(z3,sym[5])
 else:assert z2==z3=={};n2=n3={}
 assert n2=={} and n3==({'S':1}if typ in [1,3]else{})
 supports=[s for s in product([False,True],repeat=nvars)if predicate(*s)];assert supports
 survivors.append({'type':typ,'necessary_scalar_condition':description,'admissible_zero_nonzero_support_count':len(supports),'H0_N_twist2':n2,'H0_N_twist3':n3})
assert small_h0(records[6]['residual_blocks'],3)=={'Wp':1}
old_Z3=lambda alpha,beta,a,b:(a or b)and(alpha or(a and beta))
removed=[s for s in product([False,True],repeat=4)if old_Z3(*s)and not conditions[2][1](*s)]
assert removed==[(False,True,True,False),(False,True,True,True)]
assert len(prior['labels'])==3
out={'scope':'Necessary strict-slope refinement: six residual types become five, Z3 loses its alpha=0 stratum, no quotient label excluded, no quotient connection asserted.','source_hashes':PINNED,'labels':prior['labels'],'excluded_residual_types':[6],'excluded_parameter_stratum':{'type':3,'condition':'alpha=0 and a*beta!=0'},'surviving_type_count':5,'surviving_types':survivors,'excluded_label_count':0}
(ROOT/'primal-residual-strict-slope-cuts.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: Z6 excluded; Z3 requires alpha!=0; five necessary residual types remain; zero quotient-label exclusions.')
