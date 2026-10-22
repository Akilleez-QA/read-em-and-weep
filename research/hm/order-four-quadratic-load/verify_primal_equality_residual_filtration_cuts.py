#!/usr/bin/env python3
"""Bounded exact residual flags, no quotient connection or instance evaluation."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={
'PRIMAL-RESIDUAL-KERNELS-HAVE-SIX-EXPLICIT-SPLITTING-TYPES.md':'525fee7a0ebabf24196fa6602ec6ccd548ba79d15e9ce882a43b746b6d5ec431',
'primal-residual-kernel-splittings.json':'e896b04a1c0757973f34c7cd7a95eb9155bb7f81cf667ce75333ae3028cc4361',
'equality-gauss-rational-normal-subbundles.json':'c1930c3f8977515f75fc9359866dd9a143e2101322a3fd80a352a8357d15377f',
'NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md':'53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
names=['one','W','Wp','A','V','P','S','D','T'];dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]))
edges=[('one','W'),('W','A'),('A','S'),('S','D'),('D','T'),('T','V'),('T','P'),('P','Wp')]
def tw(v):
 out={n:0 for n in names}
 for a,b in edges:out[a]+=v.get(b,0);out[b]+=v.get(a,0)
 return {n:m for n,m in out.items()if m}
def sub(v,w):return {n:v.get(n,0)-w.get(n,0)for n in names if v.get(n,0)!=w.get(n,0)}
sym=[{'one':1},{'W':1}]
for t in range(2,6):sym.append(sub(tw(sym[-1]),sym[-2]))
assert sym[2]=={'A':1} and sym[4]=={'D':1}
assert all(sym[t].get(n,0)==0 for t in [2,4]for n in ['V','P'])
prior=json.loads((ROOT/'primal-residual-kernel-splittings.json').read_text())
unique=sorted({tuple(tuple(b)for b in r['kernel_blocks'])for r in prior['records']})
assert len(unique)==6
negative_allowed=[bs for bs in unique if any(e<=-10 for e,n in bs)]
N1=((-3,'S'),(-8,'one'),(-10,'one'));N2=((-4,'D'),(-10,'one'));N3=((-3,'S'),(-9,'W'));N4=((-5,'T'),)
assert set(negative_allowed)=={N1,N2}
# Standard symmetric powers through degree5 are irreducible here.
standard=['one','W','A','S','D','T'];assert all(sym[m]=={standard[m]:1}for m in range(6))
def inv(bs):return(sum(dims[n]for e,n in bs),sum(e*dims[n]for e,n in bs))
def step(bs,e,rep):
 bs=list(bs);bs.remove((e,rep));m=standard.index(rep)
 target=e+m
 if m:bs.append((e-1,standard[m-1]))
 return tuple(sorted(bs)),target
chains=[]
# Each step names one evaluated block; m=0 is a direct line projection.
specs=[
 ('length1_N1',N1,[(-3,'S'),(-4,'A'),(-5,'W'),(-6,'one'),(-8,'one'),(-10,'one')],1),
 ('length1_N2',N2,[(-4,'D'),(-5,'S'),(-6,'A'),(-7,'W'),(-8,'one'),(-10,'one')],1),
 ('length1_N3',N3,[(-3,'S'),(-4,'A'),(-5,'W'),(-6,'one'),(-9,'W'),(-10,'one')],1),
 ('length1_N4',N4,[(-5,'T'),(-6,'D'),(-7,'S'),(-8,'A'),(-9,'W'),(-10,'one')],1),
 ('length2_N1',N1,[(-3,'S'),(-4,'A'),(-5,'W'),(-6,'one'),(-8,'one')],2),
 ('length2_N2',N2,[(-4,'D'),(-5,'S'),(-6,'A'),(-7,'W'),(-8,'one')],2),
]
for label,bs,steps,length in specs:
 stages=[bs];arrows=[];assert inv(bs)==(6,-30)
 for j,(e,rep)in enumerate(steps,1):
  old=bs;targets=[]
  if length==2 and j==1:
   tmp=list(bs);tmp.remove((-10,'one'));bs=tuple(tmp);targets.append(-10)
  bs,target=step(bs,e,rep);targets.append(target)
  assert sorted(targets)==sorted(([0,-10]if length==2 and j==1 else[2-2*j]))
  ro,do=inv(old);rn,dn=inv(bs)
  assert ro-rn==len(targets) and do-dn==sum(targets)
  assert not bs or max(e for e,n in bs)<=-3-j
  arrows.append({'step':j,'target_line_degrees':targets,'evaluated_block':[e,rep]});stages.append(bs)
 assert not bs
 chains.append({'name':label,'stages':stages,'arrows':arrows})
assert len(chains)==6
foundation=json.loads((ROOT/'equality-gauss-rational-normal-subbundles.json').read_text())
labels=[]
for row in foundation['records']:
 if row['side']!='A':continue
 length=int(row['profile'][0]);kept=[f['heights']for f in row['flags']if not f['height_excluded_by_central_twist_one_vanishing']]
 assert kept==([[8,6,0]]if length==1 else[[8,5,1]])
 labels.append({'id':row['id'],'profile':row['profile'],'remaining_residual_types':[1,2,3,4,5]if length==1 else[1,2,3,4],'new_scalar_condition':'Z5: alpha*beta!=0'if length==1 else'Z3: a=0; all Z5 strata excluded','remaining_kernel_type_count':4 if length==1 else 2})
out={'scope':'Ordinary residual exact flags impose new scalar/type cuts, but exclude no quotient label and do not construct an ambient connection.','source_hashes':PINNED,'labels':labels,'explicit_compatible_residual_filtrations':chains,'excluded_label_count':0}
(ROOT/'primal-equality-residual-filtration-cuts.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: two length-one-profile Z5 boundary cuts; profile21 removes Z5 and Z3 a!=0; six ordinary filtered witnesses; zero label exclusions.')
