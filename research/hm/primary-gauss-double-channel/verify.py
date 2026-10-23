#!/usr/bin/env python3
"""Fixed universal representation checks, with no actual-instance evaluation."""
from pathlib import Path
from collections import Counter
import hashlib,json,sys
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok: raise RuntimeError(msg)
for x in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/x['file']).read_bytes()
 require(len(b)==x['bytes'],x['file']+' length')
 require(hashlib.sha256(b).hexdigest()==x['sha256'],x['file']+' SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],x['file']+' git blob')
E={
'D':[[-2,'D'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-8,'one']],
'P':[[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']],
'V':[[-2,'V'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-4,'V']],
'Z':[[-3,'Wp'],[-3,'T'],[-3,'T'],[-4,'V']]}
expected={'D':Counter(Wp=1,S=1,T=2),'P':Counter(Wp=2,T=2),'V':Counter(Wp=1,T=2),'Z':Counter(Wp=1,T=2)}
for name,blocks in E.items():
 require(sum(c.DIM[r] for e,r in blocks)==17,name+' rank')
 require(sum(e*c.DIM[r] for e,r in blocks)==-54,name+' degree')
 require(c.h0(blocks,3)==expected[name],name+' cubic character')
for r,expected_prod in [('D',Counter(S=1,T=1)),('P',Counter(Wp=1,T=1)),('V',Counter(T=1))]:
 require(c.product(r,1)==expected_prod,r+' top product')
 require(c.product(r,1)['T']==1,r+' unique graph lift channel')
 require(c.DIM[r]-1<c.DIM['T'],r+' cannot kill T by kernel bound')
 require(c.h0(E[r],2)==Counter({r:1}),r+' strict top source')
minimal=Counter(Wp=1,T=2)
remainder={}
for name,char in expected.items():
 rem=char.copy(); rem.subtract(minimal)
 require(all(v>=0 for v in rem.values()),name+' genuine remainder')
 remainder[name]=dict(sorted((+rem).items()))
require(remainder=={'D':{'S':1},'P':{'Wp':1},'V':{},'Z':{}},'cubic kernel alternatives')
def condition(blocks,t_multiplicity):
 v=c.h0(blocks,3)
 return v['Wp']>=1 and v['T']>=t_multiplicity
examples=[
 ([[-8,'one'],[3,'Wp']],Counter(W=1,Wp=1,S=1,T=1)),
 ([[-3,'Wp'],[4,'one']],Counter(Wp=2,T=1)),
 ([[-3,'Wp'],[6,'one']],Counter(Wp=1,S=1,T=1)),
 ([[0,'V']],Counter(Wp=1,S=1,T=1)),
 ([[-3,'Wp'],[10,'one']],Counter(W=1,Wp=2,S=1,T=1))]
for blocks,char in examples:
 require(c.h0(blocks,3)==char,'new exact shape character')
 require(condition(blocks,1) and not condition(blocks,2),'new shape needs stronger multiplicity')
base=json.loads((ROOT/'inputs/frontier182.json').read_text())['cases']
require(len(base)==182,'fixed original182')
require(len({x['id'] for x in base})==182,'unique stable IDs')
require(Counter(x['profile'] for x in base)=={'11':159,'12':10,'21':13},'original profile totals')
cut=[];new=[];passed=[];max_degree=0
for x in base:
 require(sum(c.DIM[r] for e,r in x['A'])==3,x['id']+' rank3')
 max_degree=max(max_degree,max(e+3 for e,r in x['A']))
 v=c.h0(x['A'],3)
 if condition(x['A'],2):passed.append(x['id'])
 else:
  row=dict(x,H0_A3=dict(sorted(v.items())),missing={r:n-v[r] for r,n in minimal.items() if v[r]<n})
  cut.append(row)
  if condition(x['A'],1):new.append(row)
require(max_degree==31,'bounded symmetric degree31')
require(Counter(x['profile'] for x in cut)=={'11':39,'12':2,'21':4},'total strengthened historical cuts')
require(len(passed)==137,'single-criterion historical passes')
require(Counter(x['profile'] for x in new)=={'11':14,'12':1},'historical difference only')
indices={p:[x['source_index'] for x in new if x['profile']==p] for p in ('11','12','21')}
require(indices=={'11':[19,20,23,42,43,44,45,53,54,62,67,73,76,102],'12':[14],'21':[]},'exact historical new indices')
require(all(x['missing']=={'T':1} for x in new),'every extra cut lacks second T')
require({tuple(tuple(a) for a in x['A']) for x in new}=={tuple(tuple(a) for a in b) for b,v in examples},'exact five extra shapes')
# Negative controls distinguish multiplicities, vanishing twists, and block order.
require(not condition([[-3,'Wp'],[4,'one']],2),'one-T mutation fails')
require(condition([[-3,'Wp'],[-3,'T'],[-3,'T']],2),'two copies retained')
require(not condition([[-3,'T'],[-3,'T']],2),'missing Wp fails')
require(c.h0([[-4,'T']],3)==Counter(),'negative symmetric exponent omitted')
require(c.h0([[-3,'Wp'],[-3,'T'],[-3,'T']],3)==c.h0([[-3,'T'],[-3,'Wp'],[-3,'T']],3),'block order invariant')
out={'scope':'Uniform actual cubic coefficient visibility and kernel alternatives; fixed historical records only',
 'sources_authenticated':8,'checks':checks+c.checks,
 'required_cubic_character':dict(minimal),'source_cubic_characters':{k:dict(v) for k,v in expected.items()},
 'possible_nonzero_cubic_kernel':remainder,
 'original_by_profile':{'11':159,'12':10,'21':13},
 'excluded_by_profile':{'11':39,'12':2,'21':4},
 'additional_historical_vs_Wp_plus_T':{'11':14,'12':1,'21':0},
 'additional_historical_records':new,'all_rejected_historical_records':cut,'passes_condition_only':passed,
 'max_symmetric_degree':max_degree,'profile11_excluded':False,
 'complete_coverage_proof':False,'actual_instance_evaluated':False,'global_rank_three_exclusion':False}
result=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(result)
else:
 if (ROOT/'RESULT.json').read_text()!=result: raise RuntimeError('RESULT exact replay failed')
print(json.dumps({'checks':checks+c.checks,'additional_historical':len(new),'all_historical_cuts':len(cut),'exact_result_reproduced':'--write' not in sys.argv},sort_keys=True))
