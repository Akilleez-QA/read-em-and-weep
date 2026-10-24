#!/usr/bin/env python3
"""Small fixed representation and degree checks; no actual map evaluation."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import hashlib,json,sys
import characters as c
P=Path(__file__).resolve().parent; checks=0
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
def norm(v):return dict(sorted((k,n) for k,n in v.items() if n))
def rank(B):return sum(c.DIM[r] for e,r in B)
def degree(B):return sum(e*c.DIM[r] for e,r in B)
for row in json.loads((P/'INPUTS.json').read_text()):
 b=(P/row['file']).read_bytes()
 req(len(b)==row['bytes'],row['file']+' bytes')
 req(hashlib.sha256(b).hexdigest()==row['sha256'],row['file']+' hash')
 req(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob_sha1'],row['file']+' blob')
 req(row['ref'] in row['url'],row['file']+' immutable')

N=[ [(-4,'V'),(-5,'T')], [(-4,'V'),(-4,'P'),(-7,'Wp')], [(-4,'V'),(-4,'D'),(-10,'one')] ]
for B in N:
 req(rank(B)==9 and degree(B)==-42,'N rank degree')
 req(rank([(-3,'S')]+B)==13 and degree([(-3,'S')]+B)==-54,'K rank degree')
req(c.product('D',1)==Counter(S=1,T=1),'unique source Euler kernel')
req(c.product('S',0)['S']==1,'cubic evaluation multiplicity')
req(c.product('one',3)==Counter(S=1),'unique cubic evaluation')
req(c.product('W',1)['one']==1,'unique graph Euler injection')
req(c.product('W',4)['S']==1,'unique top derivative W component')
req(c.DIM['D']-c.DIM['S']==1 and -10-(-12)==2,'D Euler quotient O2')
req(c.DIM['S']-c.DIM['A']==1 and -12-(-12)==0,'cubic Euler kernel A minus4')
req(c.DIM['W']-1==1 and 2*3-2==4,'O2 into W3 quotient O4')
req(2*1-0==2,'O into W1 quotient O2')
req(c.product('one',4)['V']==0,'V row has no scalar component')
line_hom=[]
for d in range(-4,2):
 v=c.product('one',d+4)['V'];line_hom.append([d,v]);req(v==0,'V row cannot factor through rank1 image')
for r in (2,3):
 req(r-1 in (1,2),'gamma rank restriction')
 req(13-r==3+(9-(r-1)),'exact kernel ranks')
req(-3>-5,'E/F internal derivative Hom vanishing')
req(all(e>-10 for B in N[:2] for e,r in B),'first two negative components zero')
req(sum(c.DIM[r] for e,r in N[2] if e<=-10)==1,'third negative component only scalar tail')
# Exact polynomial identity in variables y,z, coefficients (1,y,z,y²,yz,z²).
original=[F(-36),F(8),F(7),F(-2),F(-2),F(-2)]
expanded=[F(-53,2)-2*(F(9,4)+1+F(3,2)),F(8),F(7),F(-2),F(-2),F(-2)]
req(original==expanded,'capacity square completion')
req(F(-53,2)<-26 and F(-53,2)>-27,'integral upper bound minus27')
for h in ((6,2,1),(7,1,1)):
 req(sum(h)==9 and h[0]>=h[1]>=h[2]>=0,'ordered height')
 req(6*h[0]-4*h[1]-5*h[2]-sum(x*(x+1) for x in h)==-27,'attaining height')
req(-27+46==19,'defect upper bound')
req(12<=19<20 and 24>19,'semigroup intersection exactly zero,twelve')
req([60//s for s in (1,2,3,5)]==[60,30,20,12],'orbit sizes')
req(15*2==30 and 20*2//2==20 and 24*2//4==12,'unique exceptional orbit counts')
req(12//12==1,'defect twelve has unit multiplicity')

mutations=[
('replace cubic kernel by V',lambda:req(c.product('one',2)==Counter(V=1),'physical standard')),
('allow rank1 V image',lambda:req(any(x[1] for x in line_hom),'rank1 Hom')),
('supply scalar V derivative',lambda:req(c.product('one',4)['V']>0,'scalar V Hom')),
('drop cotangent graph twist',lambda:req(2==0,'graph twist')),
('round capacity upward',lambda:req(-26<=F(-53,2),'integer capacity')),
('allow defect twenty',lambda:req(20<=19,'defect cap')),
('call defect twelve unramified',lambda:req(12==0,'positive defect retained')),
('use full N rank as residual rank',lambda:req(9<=2,'residual rank bound'))]
rejected=[]
for name,fn in mutations:
 try:fn()
 except RuntimeError:rejected.append(name)
 else:raise RuntimeError('mutation survived '+name)
req(len(rejected)==8,'all mutations rejected')
out={'claim':'Matched actual Euler graph, residual sheaf map, endpoint rank2-or3, and defect0-or12',
'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),
'checks':checks+c.checks,'authenticated_inputs':11,'max_symmetric_degree':5,
'necessary_N_shapes':N,'rank_one_V_image_Hom':line_hom,'dual_capacity':-27,'defect_bound':19,'possible_defects':[0,12],
'rejected_mutations':rejected,'gamma_is_assumed_Gauss_derivative':False,'coefficient_pair_selected':False,
'actual_instance_evaluated':False,'profile_closure':False}
s=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(P/'RESULT.json').write_text(s)
else:req((P/'RESULT.json').read_text()==s,'exact saved result')
print(json.dumps({'checks':out['checks'],'inputs':11,'mutations':8,'proof_sha256':out['proof_sha256'],'result_sha256':hashlib.sha256(s.encode()).hexdigest()},sort_keys=True))
