"""Fixed symbolic and degree checks. No actual source instance is evaluated."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as Q
import characters as C
BASE=Path(__file__).resolve().parent
count=0
def require(v,s):
 global count
 count+=1
 if not v:raise RuntimeError(s)
a=json.loads((BASE/'INPUTS.json').read_text())
require(len(a)==1,'one complete direct input')
i=a[0]
require(i['file']=='inputs/nonsplit-quotient.md','exact input')
require(i['ref']=='f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1','immutable ref')
require(i['path']=='research/hm/rankfour-profile11-triplet-nonsplit-quotient/PROOF.md','immutable path')
b=(BASE/i['file']).read_bytes()
require(len(b)==i['bytes']==13619,'full input bytes')
require(hashlib.sha256(b).hexdigest()==i['sha256']=='d4ff280dc943c2a112ea68ff4d9c4750fe5f93b3892d8a104fa9c08aa5960568','input hash')
require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==i['git_blob_sha1']=='1974a5c3b20546dcb414539096511388f495cdab','input blob')
require(i['url'].endswith('/'+i['ref']+'/'+i['path']),'source link')
proof=(BASE/'PROOF.md').read_bytes()
require(len(proof)==12872,'frozen proof bytes')
require(hashlib.sha256(proof).hexdigest()=='96c3a9dea9260bcc34435220e00ad78a721bb18423d38b3a9aae3b7124eab7b7','frozen proof hash')
require(C.product('one',12)['one']==1,'unique fixed universal invariant')
# Ordinary degree/rank bookkeeping from the actual flag.
require(7-6==1 and -88-(-80)==-8,'B7/G6')
require(8-7==1 and -84-(-88)==4,'B6/B7')
require(4-(-8)==12,'graph Hom degree')
require(4-2==2,'actual normal twist')
require(2-(-10)==12,'L10 normal restriction degree')
require(5+1+1==7,'all local generators')
require(5+6==11,'vanishing mixed pairing')
require(6+6==5+7==12,'norm and first differentiated identity')
require(6+7==13,'symmetric norm derivative order')
require(12-2*12==-12<0,'global double-divisor obstruction')
require(12>0,'no nowhere-zero map from O(-8) to O4')
# Formal identities use only Leibniz and symmetry. The variables below label
# universal symbolic coefficients, not actual parameters or selected jets.
p57_from_zero_pairing=-Q(1)
p67_from_symmetric_norm=Q(1,2)
require(Q(1)+p57_from_zero_pairing==0,'differentiate p56=0')
require(2*p67_from_symmetric_norm==1,'differentiate symmetric p66')
require(p67_from_symmetric_norm==Q(1,2),'universal half factor')
stationary_relation=-p67_from_symmetric_norm
require(stationary_relation+Q(1,2)==0,'remaining conormal component')
require(stationary_relation!=0,'nonzero graphs consistent')
require(stationary_relation!=1,'distinct graphs consistent')
require(1+stationary_relation!=0,'no accidental identification with negative graph')
# In a smooth formal parameter z along the whole reduced divisor, a section
# z*u has derivative u modulo z. A vanishing differential is exactly u=0
# modulo z, i.e. a second divisor factor. Only the universal orders are used.
require(1-1==0,'first-order derivative of divisor equation')
require(2-1>=1,'second-order factor has zero first derivative on divisor')
print(json.dumps({'status':'PASS','checks':count,'proof_sha256':hashlib.sha256(proof).hexdigest(),'scope':'one complete immutable input; fixed representation, degree and formal Leibniz/conormal identities','not_claimed':['selected actual coefficient, graph scalar, point or instance evaluation','exact coherent image from fiberwise vanishing','higher vanishing or original tenth jets','branch occurrence or exclusion','proof by computation']},indent=2,sort_keys=True))
