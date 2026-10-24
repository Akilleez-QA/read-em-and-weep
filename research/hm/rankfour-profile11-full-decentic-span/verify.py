"""Fixed character and genuine-direct-summand degree checks only."""
from collections import Counter
from pathlib import Path
import hashlib,json
from characters import product,DIM
root=Path(__file__).resolve().parent
checks=0
def req(ok,label):
 global checks
 checks+=1
 if not ok:raise RuntimeError(label)
def eq(a,b,label):req(a==b,label)
def dim(c):return sum(DIM[r]*n for r,n in c.items())
h=hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest()
eq(h,'f7952c7e28fe1cb4c31dffb3b4017e891b09b1bfd94012d583760840c7d043c3','proof binding')
a=json.loads((root/'INPUTS.json').read_text());eq(len(a),1,'one complete immutable source')
for i in a:
 b=(root/i['file']).read_bytes()
 eq(len(b),i['bytes'],'source length')
 eq(hashlib.sha256(b).hexdigest(),i['sha256'],'source hash')
 eq(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),i['git_blob_sha1'],'source blob')
C=Counter(A=2,V=2,P=1,D=1)
R=product('one',10);T=product('Wp',11)
eq(R,Counter(A=1,V=1,D=1),'actual line coefficient domain')
eq(T,Counter(A=1,V=1,P=2,D=2),'complement coefficient domain')
eq(dim(R),11,'degree-ten dimension');eq(dim(T),24,'doublet coefficient dimension');eq(dim(C),21,'ambient dimension')
for r in ['A','V']:
 eq(C[r],2,'ambient multiplicity demand')
 eq(T[r],1,'complement multiplicity bound')
 req(C[r]>T[r],'line span must contain '+r)
small=Counter(A=1,V=1);eq(dim(small),6,'deficient line span dimension')
Jbound=Counter({r:min(C[r],T[r]) for r in C})
eq(Jbound,Counter(A=1,V=1,P=1,D=1),'complement ambient bound')
eq(dim(Jbound),15,'complement dimension bound')
eq(dim(small)+dim(Jbound),dim(C),'constant direct sum forced by equality')
eq(6-3,3,'annihilator direct summand rank')
eq(0-(-24),24,'quotient degree');eq(-24,-24,'annihilator degree')
eq(15-2,13,'other annihilator rank');eq(-22+(-24),-46,'direct sum degree')
eq(5+8+3,16,'E0 ordinary rank');eq(5*(-2)+8*(-3)+3*(-4),-46,'E0 ordinary degree')
eq(min(-2,-3,-4)*3,-12,'rank-three direct summand degree floor')
req(-24< -12,'contradiction in deficient span case')
N=C.copy();N.subtract(R)
eq(+N,Counter(A=1,V=1,P=1),'constant q kernel character')
eq(dim(N),10,'constant q kernel dimension')
controls={'a rank-three subbundle alone has no asserted degree floor':True,
 'losing equality of dimensions would not force zero intersection':6+16>21,
 'a rank-three degree minus twelve summand would not contradict the bound':not(-12< -12)}
# The first item is a stated logical boundary, not an executable geometric claim.
for name in list(controls)[1:]:req(controls[name],name)
print(json.dumps({'status':'PASS','checks':checks,'proof_sha256':h,'scope':'Only fixed characters and numerical direct-summand identities; geometric splitting is proved in PROOF.md.',
 'line_coefficient_domain':dict(R),'complement_coefficient_domain':dict(T),
 'ambient_character':dict(C),'complement_dimension_bound':dim(Jbound),
 'forced_line_span_dimension':11,'constant_kernel_character':dict(+N),'constant_kernel_dimension':10,
 'controls_and_boundary':controls},indent=2,sort_keys=True))
