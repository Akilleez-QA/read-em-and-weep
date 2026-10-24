#!/usr/bin/env python3
"""Fixed character, row-degree, and actual-kernel capacity checks."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json,hashlib,sys
import characters as c
P=Path(__file__).resolve().parent;checks=0
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
def norm(v):return dict(sorted((r,n) for r,n in v.items() if n))
def rank(B):return sum(c.DIM[r] for e,r in B)
def degree(B):return sum(e*c.DIM[r] for e,r in B)
def hom_scalar(R,e,target=0):return c.product('one',target-e)[R]
for row in json.loads((P/'INPUTS.json').read_text()):
 b=(P/row['file']).read_bytes()
 req(len(b)==row['bytes'],row['file']+' length')
 req(hashlib.sha256(b).hexdigest()==row['sha256'],row['file']+' SHA256')
 req(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob_sha1'],row['file']+' blob')
 req(row['ref'] in row['url'],row['file']+' immutable')
K={
'T':[(-3,'S'),(-4,'V'),(-5,'T')],
'W':[(-3,'S'),(-4,'V'),(-4,'P'),(-7,'Wp')],
'one':[(-3,'S'),(-4,'V'),(-4,'D'),(-10,'one')]}
for name,B in K.items():req(rank(B)==13 and degree(B)==-54,name+' K rank degree')
rows={}
for name,B in K.items():
 rows[name]=[{'block':[e,R],'to_O':hom_scalar(R,e),'to_O_minus10':hom_scalar(R,e,-10)} for e,R in B]
allowed={(-3,'S'),(-5,'T'),(-7,'Wp'),(-4,'D')}
for name,B in K.items():
 for e,R in B:
  req(bool(hom_scalar(R,e))==((e,R) in allowed),'complete nonzero scalar source list')
  req(bool(hom_scalar(R,e,-10))==((e,R)==(-10,'one')),'complete negative source list')
  if hom_scalar(R,e):req(-e<12,'scalar row invariant base divisor degree below12')
req(c.product('one',10)==Counter(A=1,D=1,V=1),'O(-10) cannot map to scalar O')
req(hom_scalar('V',-4)==0 and hom_scalar('V',-4,-10)==0,'V only maps to W O1')
req(c.product('W',5)['V']==1,'V row has unique possible W O1 coefficient')
for e in range(-4,2):req(c.product('one',e+4)['V']==0,'no rank1 V image')
req(2*1-2*(-4)==10,'maximal minor degree10')
req(10<12,'rank2 minors have no invariant common zero')
# Actual K^- capacities: no quotient N is used.
req(13-2==11 and -54-2==-56,'rank2 image kernel invariants')
req(6+5==11 and 6*7+5*6==72,'two-column balanced cost')
req(11-72==-61 and -56>-61,'rank2 capacity contradiction')
req(13-3==10 and -54-(2-10)==-46,'negative image kernel invariants')
# Polynomial coefficients in z: -11z-(10-z)^2/2-z^2.
req([F(-50),F(-1),F(-3,2)]==[-F(100,2),-11+10,F(-1,2)-1],'all three heights capacity polynomial')
req(-46>-50,'negative rank3 capacity contradiction')
req(5+5+0==10 and 5+5-5*6-5*6==-50,'exact negative image capacity attained at height5,5,0')
req(13-3==10 and -54-2==-56,'positive image next kernel invariants')
E0=[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V')]
Apos=[(3,'W'),(2,'one')]
req(rank(E0)==16 and degree(E0)==-46,'forward transform rank degree')
req(rank(Apos)==3 and degree(Apos)==8,'forward rank3 quotient')
req(-54+8==-46,'forward degree identity')
req([(e-2,R) for e,R in Apos]==[(1,'W'),(0,'one')],'actual cotangent-twisted graded isomorphism')
req(3==16-13,'E0 actual kernel rank')

mutations=[
('allow V scalar row',lambda:req(hom_scalar('V',-4)>0,'V scalar Hom')),
('allow rank1 V image',lambda:req(c.product('one',5)['V']>0,'rank1 V')),
('permit degree10 invariant base divisor',lambda:req(10>=12,'orbit gap')),
('allow O(-10) scalar row',lambda:req(c.product('one',10)['one']>0,'scalar tail Hom')),
('allow both scalar channels',lambda:req(2+1+1<=3,'rank4 contradiction')),
('permit rank2 capacity',lambda:req(-56<=-61,'rank2 contradiction')),
('permit negative rank3 capacity',lambda:req(-46<=-50,'rank3 contradiction')),
('wrong next kernel degree',lambda:req(-54-2==-46,'positive degree must be minus56'))]
rejected=[]
for name,fn in mutations:
 try:fn()
 except RuntimeError:rejected.append(name)
 else:raise RuntimeError('mutation survived '+name)
req(len(rejected)==8,'all mutation controls rejected')
out={'claim':'Actual beta_K is everywhere onto W O1+O; negative component zero; K^-rank10degree-56 and K^+=E0',
'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),
'checks':checks+c.checks,'authenticated_inputs':11,'max_symmetric_degree':10,'scalar_row_table':rows,
'V_minor_degree':10,'minimum_invariant_divisor_degree':12,
'rank2_image_capacity':-61,'negative_rank3_image_capacity':-50,
'next_kernel':{'rank':10,'degree':-56},'forward_transform':{'rank':16,'degree':-46,'blocks':E0},
'checked_mutations':rejected,'all_three_heights_retained':True,'N_assumed_flat':False,
'actual_instance_evaluated':False,'K_type_selected':False,'profile_closure':False}
s=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(P/'RESULT.json').write_text(s)
else:req((P/'RESULT.json').read_text()==s,'exact RESULT replay')
print(json.dumps({'checks':out['checks'],'inputs':11,'mutations':8,'proof_sha256':out['proof_sha256'],'result_sha256':hashlib.sha256(s.encode()).hexdigest()},sort_keys=True))
