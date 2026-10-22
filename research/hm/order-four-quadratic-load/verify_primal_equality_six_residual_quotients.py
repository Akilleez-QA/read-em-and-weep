#!/usr/bin/env python3
"""Exact representation and integer enumeration; no actual-instance evaluations."""
from pathlib import Path
from itertools import product
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={
'EQUALITY-GAUSS-ENVELOPES-FORCE-RATIONAL-NORMAL-SUBBUNDLES.md':'cc64326df0b4c5d3b35a195a994f1faf397cac88ec377d608aac56b29f4fb9db',
'equality-gauss-rational-normal-subbundles.json':'c1930c3f8977515f75fc9359866dd9a143e2101322a3fd80a352a8357d15377f',
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
'NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md':'53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
names=['one','W','Wp','A','V','P','S','D','T'];dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]))
edges=[('one','W'),('W','A'),('A','S'),('S','D'),('D','T'),('T','V'),('T','P'),('P','Wp')]
def tensorW(v):
 out={n:0 for n in names}
 for a,b in edges:out[a]+=v.get(b,0);out[b]+=v.get(a,0)
 return out
sym=[{'one':1},{'W':1}]
for t in range(2,13):
 v=tensorW(sym[-1]);sym.append({n:v[n]-sym[-2].get(n,0) for n in names if v[n]!=sym[-2].get(n,0)})
expected_sym={1:{'W':1},4:{'D':1},5:{'T':1},6:{'V':1,'P':1},7:{'Wp':1,'T':1},8:{'P':1,'D':1},10:{'A':1,'V':1,'D':1},11:{'W':1,'S':1,'T':1},12:{'one':1,'A':1,'P':1,'D':1}}
for t,v in expected_sym.items():assert sym[t]==v
assert all(sum(dims[n]*m for n,m in v.items())==i+1 for i,v in enumerate(sym))
base=[(-3,'Wp'),(-3,'T'),(-4,'V'),(-4,'P'),(-5,'Wp'),(-8,'one'),(-9,'W'),(-10,'one')]
alltypes=[];retained=[]
for a,d,g,h in product(range(2),repeat=4):
 for b,c,e,f in product(range(4),repeat=4):
  if a+d+g+h!=1 or b+c+d+e+f+2*g+h!=3 or c+g+h<1:continue
  coeff=(a,b,c,d,e,f,g,h);R2={'V':c+g+h-1,'P':d+e+g+h,'D':f+g}
  bs=[(-2,n)for n,m in R2.items()for _ in range(m)]+[x for m,x in zip(coeff,base)for _ in range(m)]
  assert sum(dims[n]for t,n in bs)==17 and sum(t*dims[n]for t,n in bs)==-54
  alltypes.append(coeff)
  if R2['V']!=0 or R2['P']!=1 or R2['D']not in [1,2]:continue
  residual=bs.copy();residual.remove((-2,'P'));residual.remove((-2,'D'))
  assert sum(dims[n]for t,n in residual)==8 and sum(t*dims[n]for t,n in residual)==-36
  retained.append((coeff,residual))
assert len(alltypes)==28 and len(retained)==6
Z=[
 [(-2,'D'),(-8,'one'),(-8,'one'),(-10,'one')],
 [(-3,'T'),(-8,'one'),(-10,'one')],
 [(-2,'D'),(-8,'one'),(-9,'W')],
 [(-3,'T'),(-9,'W')],
 [(-4,'V'),(-4,'P'),(-8,'one')],
 [(-3,'Wp'),(-4,'V'),(-5,'Wp'),(-8,'one')],
]
assert {tuple(sorted(bs))for c,bs in retained}=={tuple(sorted(bs))for bs in Z}
# Every input irrep is self-dual. Hom_G(R O(e),O(t)) is its multiplicity
# in Sym^(t-e) W; repeated copies are kept as distinct source blocks.
hom=[]
for bs in Z:
 channels=[]
 for target in [2,-8]:
  for i,(degree,rep)in enumerate(bs):
   m=target-degree
   mult=sym[m].get(rep,0)if 0<=m<len(sym)else 0
   assert mult in [0,1]
   if mult:channels.append({'target_degree':target,'source_index':i,'source_degree':degree,'source_rep':rep,'polynomial_degree':m})
 hom.append(channels)
expected=[[(2,0),(2,3),(-8,1),(-8,2)],[(2,0),(2,2),(-8,1)],[(2,0),(2,2),(-8,1),(-8,2)],[(2,0),(2,1),(-8,1)],[(2,0),(2,1),(-8,2)],[(2,1),(2,2),(-8,3)]]
assert [[(c['target_degree'],c['source_index'])for c in cs]for cs in hom]==expected
assert list(map(len,hom))==[4,3,4,3,3,3]
for cs in hom:
 for c in cs:assert c['polynomial_degree']<12 or (c['polynomial_degree']==12 and c['source_rep']=='one')
# Conditions refer only to zero/nonzero support, not evaluated coefficients.
conditions=[
 ('alpha != 0 and (a,b) != (0,0)',lambda alpha,beta,a,b:alpha and (a or b),4),
 ('alpha*a != 0',lambda alpha,beta,a:alpha and a,3),
 ('(a,b) != (0,0) and (alpha != 0 or a*beta != 0)',lambda alpha,beta,a,b:(a or b)and(alpha or(a and beta)),4),
 ('alpha*b != 0',lambda alpha,beta,b:alpha and b,3),
 ('a != 0 and (alpha,beta) != (0,0)',lambda alpha,beta,a:a and(alpha or beta),3),
 ('a != 0 and (alpha,beta) != (0,0)',lambda alpha,beta,a:a and(alpha or beta),3),
]
records=[]
for i,(bs,channels,(description,predicate,nvars))in enumerate(zip(Z,hom,conditions),1):
 supports=[x for x in product([False,True],repeat=nvars)if predicate(*x)]
 assert supports
 coeff=next(c for c,r in retained if sorted(r)==sorted(bs))
 records.append({'type':i,'E_parameter_tuple':coeff,'residual_blocks':bs,'rank':8,'degree':-36,'Hom_dimension':len(channels),'Hom_channels':channels,'surjectivity_condition':description,'admissible_zero_nonzero_support_count':len(supports)})
foundation=json.loads((ROOT/'equality-gauss-rational-normal-subbundles.json').read_text())
labels=sorted(r['id']for r in foundation['records']if r['side']=='A')
assert labels==sorted(['G3.11.942927348917','G3.12.8e9af2d08af9','G3.21.45ca6278cbfc'])
for r in foundation['records']:
 if r['side']=='A':
  assert r['target_degrees_descending']==[6,2,-8]
  assert all(f['heights'][0]==8 for f in r['flags']if not f['height_excluded_by_central_twist_one_vanishing'])
out={'scope':'Six necessary residual bundle types and exact ordinary equivariant quotient-map parameter spaces; no descended connection or realization; zero label exclusions.','source_hashes':PINNED,'labels':labels,'starting_E_type_count':28,'remaining_E_type_count':6,'records':records,'excluded_label_count':0}
(ROOT/'primal-equality-six-residual-quotients.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 28->6 formal E types; residual ranks8/degrees-36; Hom dimensions4/3/4/3/3/3; six nonempty surjection loci; zero label exclusions.')
