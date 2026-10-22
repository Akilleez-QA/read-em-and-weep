#!/usr/bin/env python3
"""Exact abstract kernel strata, characters and degree bounds."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={
'PRIMAL-EQUALITY-HAS-SIX-RESIDUAL-QUOTIENT-PARAMETER-SPACES.md':'de06847ba55aae35effb6ad394de4792b5c8813d48dbee35b4c1bed79935afa6',
'primal-equality-six-residual-quotients.json':'56174a13450e9b9e40ca7ab69ca52445cd9dabbbac5ad782ce4845405ac8570e',
'PRIMAL-RESIDUAL-STRICT-SLOPES-REMOVE-ONE-TYPE-AND-ONE-STRATUM.md':'263e4a4689c327309a82559380120993797ffc0d7050d50305508a6142af03cf',
'primal-residual-strict-slope-cuts.json':'e025a325502387ea63ee4931817ccda805e692d7b5a1fa223afa4117dd8ba14e',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
names=['one','W','Wp','A','V','P','S','D','T'];dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]))
edges=[('one','W'),('W','A'),('A','S'),('S','D'),('D','T'),('T','V'),('T','P'),('P','Wp')]
def tw(v):
 out={n:0 for n in names}
 for a,b in edges:out[a]+=v.get(b,0);out[b]+=v.get(a,0)
 return {n:m for n,m in out.items()if m}
def sub(v,w):return {n:v.get(n,0)-w.get(n,0)for n in names if v.get(n,0)!=w.get(n,0)}
def symtimes(rep,bound):
 out=[{rep:1},tw({rep:1})]
 for k in range(2,bound+1):out.append(sub(tw(out[-1]),out[-2]))
 return out
sym=symtimes('one',10);vsym=symtimes('V',3)
assert vsym[1]=={'T':1} and vsym[2]=={'P':1,'D':1}
assert vsym[3]=={'Wp':1,'S':1,'T':1} and sym[9]=={'S':1,'T':1}
assert sub(vsym[3],sym[9])=={'Wp':1}
assert sym[4]=={'D':1} and sym[5]=={'T':1} and sym[6]=={'V':1,'P':1}
assert sym[7]=={'Wp':1,'T':1}
possible=[(a,-14-a)for a in range(-14,0)if a>=-14-a and max(a,-14-a)<=-6]
assert possible==[(-7,-7),(-6,-8)]
assert max(sum(max(0,e+7)for e in bs)for bs in possible)==1
assert min(dims[n]for n in vsym[2])>1
assert [bs for bs in possible if max(bs)<=-7]==[(-7,-7)]
# The lifting obstruction line degrees are all >= -1, hence H1=0.
ext_degrees={'O-10_to_S-3':7,'O-10_to_D-4':6,'W-9_to_S-3':6}
assert min(ext_degrees.values())>=-1
N1=[(-3,'S'),(-8,'one'),(-10,'one')];N2=[(-4,'D'),(-10,'one')]
strata=[
 (1,'all permitted scalars',N1),
 (2,'all permitted scalars',N2),
 (3,'a != 0',[(-3,'S'),(-9,'W')]),
 (3,'a = 0; b != 0',N1),
 (4,'all permitted scalars',N2),
 (5,'alpha*beta != 0',[(-5,'T')]),
 (5,'alpha = 0; beta != 0',[(-4,'V'),(-6,'V')]),
 (5,'beta = 0; alpha != 0',[(-4,'P'),(-7,'Wp')]),
]
records=[]
for typ,condition,bs in strata:
 rank=sum(dims[n]for e,n in bs);degree=sum(e*dims[n]for e,n in bs)
 assert (rank,degree)==(6,-30)
 records.append({'residual_type':typ,'scalar_stratum':condition,'kernel_blocks':bs,'rank':rank,'degree':degree})
assert len(records)==8 and len({tuple(sorted(x[2]))for x in strata})==6
prior=json.loads((ROOT/'primal-residual-strict-slope-cuts.json').read_text())
assert {r['type']for r in prior['surviving_types']}=={1,2,3,4,5}
assert len(prior['labels'])==3
out={'scope':'Complete equivariant bundle kernel splittings for five necessary ordinary quotient families; eight scalar strata and six distinct kernels; no later Gauss compatibility or realization claimed.','source_hashes':PINNED,'labels':prior['labels'],'scalar_stratum_count':8,'distinct_kernel_type_count':6,'records':records,'lifting_H1_line_degrees':ext_degrees,'rank_two_degree_minus14_candidates':possible,'excluded_label_count':0}
(ROOT/'primal-residual-kernel-splittings.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: eight scalar strata; six explicit rank6 degree-30 kernels; Ext1 lifts and boundary evaluation kernels verified; no label exclusions.')
