#!/usr/bin/env python3
"""Small universal checks only; no actual instances or quotient enumeration."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
import characters as c
P=Path(__file__).resolve().parent
checks=0

def require(ok,message):
 global checks
 checks+=1
 if not ok: raise RuntimeError(message)

def norm(x):return dict(sorted((k,v) for k,v in x.items() if v))
def rank(B):return sum(c.DIM[r] for e,r in B)
def degree(B):return sum(e*c.DIM[r] for e,r in B)
def hom_scalar(B,e):return sum(c.product('one',e-d)[r] for d,r in B)

for row in json.loads((P/'INPUTS.json').read_text()):
 b=(P/row['file']).read_bytes()
 require(len(b)==row['bytes'],row['file']+' length')
 require(hashlib.sha256(b).hexdigest()==row['sha256'],row['file']+' hash')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob_sha1'],row['file']+' blob')
 require(row['ref'] in row['url'],row['file']+' immutable URL')

sources={
'D':[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-8,'one')],
'P':[(-2,'P'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-5,'Wp')],
'V':[(-2,'V'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-4,'V')],
'Z':[(-3,'Wp'),(-3,'T'),(-3,'T'),(-4,'V')]}
for k,B in sources.items():
 require(rank(B)==17 and degree(B)==-54,k+' actual source rank degree')

# Complete fixed proper-block table, not a multiset/candidate search.
proper=('one','W','Wp','A','V')
parity={'one':0,'A':0,'V':0,'W':1,'Wp':1}
block_table=[]
visible=[]
for R in proper:
 for e in range(-8,3):
  if e%2!=parity[R]:continue
  v=c.product(R,e+3)
  block_table.append({'R':R,'e':e,'cubic':norm(v)})
  if v['Wp']:visible.append([R,e])
require(sorted(visible)==sorted([['Wp',-3],['V',0],['A',2]]),'complete Wp mechanism table')
for R in ('W','Wp'):
 for e in (-7,-5,-3,-1,1):
  require(c.product(R,e+3)['T']<=1,'remaining doublet supplies at most one T')
for e in (-8,-6,-4,-2,0,2):
 require(c.product('one',e+3)['T']==int(e==2),'scalar T iff degree2')

hom_table={}
for k,B in sources.items():
 hom_table[k]={str(e):hom_scalar(B,e) for e in (-8,-6,-4,-2)}
 require(hom_table[k]=={'-8':int(k=='D'),'-6':0,'-4':0,'-2':0},k+' scalar quotient Hom')

shape1=[(-3,'Wp'),(2,'one'),(2,'one')]
shape2=[(2,'A'),(-8,'one')]
for B in (shape1,shape2):require(rank(B)==4 and degree(B)==-2,'two necessary shapes rank degree')
require(c.h0(shape1,3)==Counter(Wp=1,T=2),'shape1 cubic')
require(c.h0(shape2,3)==Counter(Wp=1,S=1,T=2),'shape2 cubic H0')
# Quadratic identity verified by coefficients, rather than sampling heights.
require([F(-143,2),F(8),F(-3,2)]==[F(-365,6)-F(3,2)*F(64,9),F(8),F(-3,2)],'completed square coefficients')
require(F(-365,6)<-60 and F(-365,6)>-61,'integer cap at most minus61')
require(2*5+2*5-3*3-(5*6+5*6+3*4)==-61,'one explicit optimizer')
require(-54-degree(shape1)==-52 and -52>-61,'capacity contradiction')
require(5*6+4*5+4*5==70 and 3*3*4==36,'balanced quadratic minima')
require(4*0<16 and 2+13<16,'sign contradiction constants')

# D cubic kernel is the unique standard binary evaluation kernel.
require(c.product('D',1)==Counter(S=1,T=1),'unique S4 Euler kernel channel')
require(c.DIM['S']==4 and c.DIM['D']==5,'Euler kernel ranks')
require(-3*c.DIM['S']+2==-2*c.DIM['D'],'Euler sequence degrees')
require(c.product('A',0)['one']==0,'no O2 to A_std O2')
require(13*(-4)==-52,'uniform K degree')
Ep=[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V')]
require(rank(Ep)==16 and degree(Ep)==-46,'cancelled source')
require(c.h0(Ep,3)==c.product('A',5),'cancelled cubic source character')
R=c.h0(Ep,4);R.subtract(c.product('A',6))
require(norm(R)=={'A':1,'P':1,'V':2},'forced K coefficient')
target=c.product('A',4)
require(target==Counter(A=1,D=1,V=1,P=1),'actual derivative coefficient target')
require(R['V']==2 and target['V']==1,'strict-top V multiplicity contradiction')

# Genuine fail-closed controls: each mutation changes a necessary assertion.
mutations=[
 ('omit second T', lambda: require(c.h0([(-3,'Wp'),(0,'one'),(2,'one')],3)['T']>=2,'two T required')),
 ('omit Wp',lambda: require(c.h0([(-3,'W'),(2,'one'),(2,'one')],3)['Wp']>=1,'Wp required')),
 ('permit scalar minus6',lambda:require(hom_scalar(sources['D'],-6)>0,'scalar quotient absent')),
 ('replace physical V by A',lambda:require(norm(R)=={'A':3,'P':1},'physical marking fixed')),
 ('drop one forced V',lambda:require(norm(R)=={'A':1,'P':1,'V':1},'multiplicity retained')),
 ('change derivative twist',lambda:require(c.product('A',6)==target,'cotangent twist retained')),
 ('allow O2 to triplet O2',lambda:require(c.product('A',0)['one']>0,'scalar factor obstruction')),
 ('allow cap minus52',lambda:require(F(-365,6)>=-52,'capacity strict'))]
rejected=[]
for name,f in mutations:
 try:f()
 except RuntimeError:rejected.append(name)
 else:raise RuntimeError('Mutation survived: '+name)
require(len(rejected)==len(mutations),'all controls rejected')
out={'scope':'All-source actual maximal rank-four profile (1,1): max ordinary primal quotient degree >=3',
 'checks':checks+c.checks,'authenticated_inputs':8,'max_symmetric_degree':6,
 'proper_block_table':block_table,'Wp_mechanisms':visible,'source_scalar_Hom':hom_table,
 'shape1_capacity_upper_bound':-61,'shape1_endpoint_degree':-52,
 'shape2_forced_K':norm(R),'shape2_derivative_target':norm(target),'rejected_mutations':rejected,
 'global_candidate_enumeration':False,'actual_instance_evaluated':False,'profile_closure':False,'new_global_rank_bound':False}
s=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(P/'RESULT.json').write_text(s)
else:require((P/'RESULT.json').read_text()==s,'exact result replay')
print(json.dumps({'checks':out['checks'],'authenticated_inputs':8,'mutations_rejected':len(rejected),'result_sha256':hashlib.sha256(s.encode()).hexdigest()},sort_keys=True))
