#!/usr/bin/env python3
"""Independent typed integration audit, not a geometric theorem prover."""
from pathlib import Path
import copy,hashlib,itertools,json,sys
HERE=Path(__file__).resolve().parent
PACKET=Path(sys.argv[1]) if len(sys.argv)>1 else HERE.parent
n=0
def check(x,label):
 global n
 n+=1
 if not x: raise ValueError(label)
def read(p):return json.loads(p.read_text())
rows=read(PACKET/'inputs/profile11-pairs.json')
c=read(PACKET/'COVERAGE.json')
m=read(PACKET/'INPUTS.json')
# Derive the four sources directly from PR1123's reduced equations.
derived=[]
for b,c0,e,f in itertools.product(range(4),repeat=4):
 if b>=1 and c0>=1 and b+c0+e+f==3:
  derived.append((1,b,c0,0,e,f,0,0))
types={'D':(1,1,1,0,0,1,0,0),'P':(1,1,1,0,1,0,0,0),
       'V':(1,1,2,0,0,0,0,0),'Z':(1,2,1,0,0,0,0,0)}
check(set(derived)==set(types.values()),'four-source equations')
check(len(rows)==159,'fixed historical list, not regenerated')
dims={'one':1,'W':2,'Wp':2,'Wprime':2,"W'":2,'A':3,'V':3,'S':4,'P':4,'D':5,'T':6}
for i,r in enumerate(rows):
 for side,degree in [('A','a'),('B','b')]:
  check(sum(dims[z] for e,z in r[side])==3,f'{i} {side} rank')
  check(sum(e*dims[z] for e,z in r[side])==r[degree],f'{i} {side} degree')
 check(-6-r['a']-r['b']==r['defect'],f'{i} signed defect')
 check(r['defect'] in [0,12,20,24],f'{i} allowed defect')
for x in m:
 b=(PACKET/x['file']).read_bytes();fresh=(HERE/'public'/Path(x['file']).name).read_bytes()
 check(b==fresh,'fresh independent public bytes '+x['file'])
 check(hashlib.sha256(b).hexdigest()==x['sha256'],'SHA256')
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],'blob')
 check(len(b)==x['bytes'],'bytes')
 check(len(x['ref'])==40 and set(x['ref'])<=set('0123456789abcdef'),'immutable SHA')
 check(x['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+x['ref']+'/'+x['path'],'public exact URL')
check(len(m)==16,'all direct inputs')
groups={}
for s in types:
 wanted=[i for i,r in enumerate(rows) if list(types[s]) in r['compatible_E_types']]
 if s=='P':g=read(PACKET/'inputs/p-RESULT.json')['partition']
 elif s=='D':
  allg=read(PACKET/'inputs/d-RESULT.json')['summary']
  check(allg['incompatible_D']==[i for i in range(159) if i not in wanted],'D complement')
  g={k:v for k,v in allg.items() if k!='incompatible_D'}
 else:g=read(PACKET/'inputs/vz-RESULT.json')['sources'][s]['partition']
 groups[s]=(g,wanted)
def partition(g,w):
 flat=sum(g.values(),[])
 check(len(flat)==len(set(flat)),'disjoint records')
 check(sorted(flat)==w,'all and only compatible records')
for g,w in groups.values():partition(g,w)
check(groups['D'][0]['remaining']==[32,50,52],'ordered D frontier')
expected={str(i):{k:rows[i][k] for k in ['A','B','defect']} for i in [32,50,52]}
def contract(x):
 check(x['profile']==[1,1] and x['maximal'] is True,'maximal11')
 check(x['actual'] is True and x['conditional_necessity'] is True,'actual conditional inputs')
 check(x['sources']==list(types),'exhaustive named sources')
 check(x['source_exclusions']=={'P':'p-PROOF.md','V':'vz-PROOF.md','Z':'vz-PROOF.md'},'source theorem matching')
 check(x['D_frontier']==[32,50,52],'exact ordered frontier')
 check(x['pairs']==expected,'ordered signatures with positive defect')
 check(x['pair_exclusions']=={'32':'two-PROOF.md','50':'last-PROOF.md','52':'two-PROOF.md'},'pair theorem matching')
 check(x['conclusion']=='no_actual_maximal_profile_11' and x['proof_assistant_verified'] is False,'scope')
contract(c)
mutations=0
def rejected(f):
 global mutations
 try:f()
 except (ValueError,KeyError):mutations+=1;return
 raise ValueError('invalid mutation accepted')
# Deletion of any member of any source partition is detected independently.
for g,w in groups.values():
 for name,indices in g.items():
  for idx in indices:
   a=copy.deepcopy(g);a[name].remove(idx);rejected(lambda:partition(a,w))
  if indices:
   a=copy.deepcopy(g);a[name].append(indices[0]);rejected(lambda:partition(a,w))
for source in types:
 a=copy.deepcopy(c);a['sources'].remove(source);rejected(lambda:contract(a))
for source in ['P','V','Z']:
 a=copy.deepcopy(c);del a['source_exclusions'][source];rejected(lambda:contract(a))
for idx in ['32','50','52']:
 a=copy.deepcopy(c);del a['pair_exclusions'][idx];rejected(lambda:contract(a))
 a=copy.deepcopy(c);a['pairs'][idx]['A'],a['pairs'][idx]['B']=a['pairs'][idx]['B'],a['pairs'][idx]['A'];rejected(lambda:contract(a))
 a=copy.deepcopy(c);a['pairs'][idx]['defect']+=12;rejected(lambda:contract(a))
for key,value in [('maximal',False),('actual',False),('conditional_necessity',False),('proof_assistant_verified',True),('conclusion','no_rank_three')]:
 a=copy.deepcopy(c);a[key]=value;rejected(lambda:contract(a))
a=copy.deepcopy(c);a['pairs']['32']=a['pairs']['50'];rejected(lambda:contract(a))
a=copy.deepcopy(c);a['pair_exclusions']['50']='two-PROOF.md';rejected(lambda:contract(a))
print(json.dumps({'checks':n,'mutations_rejected':mutations,'source_compatible_counts':{s:len(w) for s,(g,w) in groups.items()},'direct_public_inputs':len(m),'result':'PASS','boundary':'Conditional maximal profile11 integration only; no actual-instance evaluation or historical list generation.'},indent=2,sort_keys=True))
