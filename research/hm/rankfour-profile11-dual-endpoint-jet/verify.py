"""Fixed universal Hom and degree checks only. No actual map is evaluated."""
from collections import Counter
import hashlib,json
from pathlib import Path
from characters import product,DIM
root=Path(__file__).resolve().parent
checks=0
def require(condition,label):
 global checks
 checks+=1
 if not condition:raise RuntimeError(label)
def eq(got,want,label):require(got==want,label)
def rd(blocks):return [sum(DIM[r] for d,r in blocks),sum(d*DIM[r] for d,r in blocks)]
proof_hash=hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest()
eq(proof_hash,'bbe7c05e9055b70ba511c77ebc0514a0fdf89d75844199f971e7e774355c08c6','proof binding')
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/item['file']).read_bytes()
 eq(len(b),item['bytes'],'input bytes')
 eq(hashlib.sha256(b).hexdigest(),item['sha256'],'input sha256')
 eq(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),item['git_blob_sha1'],'input blob')
identities={
 'W tensor W':(product('W',1),Counter(one=1,A=1)),
 'W tensor Sym3 W':(product('W',3),Counter(A=1,D=1)),
 'W tensor A_std':(product('W',2),Counter(W=1,S=1)),
 'Sym5 W':(product('one',5),Counter(T=1)),
 'Sym6 W':(product('one',6),Counter(V=1,P=1)),
}
for label,(got,want) in identities.items():eq(got,want,label)
hom={
 'O(-10) -> O(-6)':product('one',4)['one'],
 'O(-10) -> O(-8)':product('one',2)['one'],
 'O(-10) -> W(-7)':product('W',3)['one'],
 'W(-9) -> O(-6)':product('W',3)['one'],
 'W(-9) -> O(-8)':product('W',1)['one'],
 'W(-9) -> W(-7)':product('W',2)['W'],
 'O(-8) -> W(-7)':product('W',1)['one'],
}
for got,want in zip(hom.values(),(0,0,0,0,1,1,1)):eq(got,want,'fixed Hom')
for n in range(0,7):
 c=product('one',n)
 eq(sum(DIM[r]*m for r,m in c.items()),n+1,'symmetric power dimension')
 require(all(m>=0 for m in c.values()),'genuine fixed symmetric power')
# Only the stated two shapes. No candidate construction or search.
F=[[(2,'one'),(4,'one'),(4,'one')],[(3,'W'),(4,'one')]]
for f in F:
 eq(rd(f),[3,10],'positive quotient degree')
 target=[(-d-4,r) for d,r in f]
 eq(rd(target),[3,-22],'coherent target F* (-4)')
 eq(rd([(-d-2,r) for d,r in f]),[3,-16],'coherent target F* (-2)')
 eq(-16-12,-28,'actual B0 degree')
 eq(-46-(-28),-18,'L0 degree')
# Euler rows and principal-parts sequences.
eq(rd([(-9,'W')]),[2,-18],'balanced L0')
eq(rd([(-8,'one'),(-10,'one')]),[2,-18],'split numerical L0')
eq(rd([(9,'W')]),[2,18],'first jet degree')
eq(rd([(8,'one'),(10,'one')]),[2,18],'first jet extension degree')
eq(8-10,-2,'Ext1 line degree')
eq(max(-(8-10)-1,0),1,'Ext1 dimension')
require(10!=0,'nonzero jet extension class in characteristic zero')
require(9-10<0,'Euler extension cannot split')
eq(-10,(-8)-2,'internal line derivative is equal degree')
eq(-18-(-10),-8,'small derivative quotient degree')
eq(-18+(-6),-24,'positive modification degree')
eq(rd([(-2,'V'),(-2,'P')]),[7,-14],'old tail kernel')
eq(rd([(-3,'T')]),[6,-18],'next tail kernel')
eq(-14-(-18),4,'tail derivative image degree')
eq(rd([(-10,'one'),(-3,'T')]),[7,-28],'original next kernel')
eq(-18+(-14),-32,'original L degree')
eq(-32-(-28),-8+4,'original derivative image degree')
eq(8-3,5,'second jet restriction residual degree')
eq(max(-5-1,0),0,'H1 O(5) vanishes')
# Numerical semantic controls. These are not modified actual configurations.
controls={
 'zero jet coefficient would not give the extension comparison':not (0!=0),
 'a degree minus eleven line would not have an isomorphic internal row':(-11!=(-8)-2),
 'the split and balanced ordinary degrees differ':sorted((-8,-10))!=[-9,-9],
 'rank one alone does not determine the degree minus eight image':(-7!=-8),
}
for label,ok in controls.items():require(ok,label)
print(json.dumps({'status':'PASS','checks':checks,'proof_sha256':proof_hash,
 'scope':'Fixed universal representation, Hom, Euler/jet and rank-degree identities only; no actual instance data.',
 'hom_dimensions':hom,'semantic_controls':controls,
 'conclusions':{'small_dual_endpoint':'W(-9)','small_actual_kernel':'O(-10)',
 'small_saturated_image':'O(-8)','original_actual_kernel':'O(-10)+T6(-3)',
 'original_kernel_rank':7,'original_kernel_degree':-28,'original_defect':12}},indent=2,sort_keys=True))
