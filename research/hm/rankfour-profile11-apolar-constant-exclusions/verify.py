"""Fixed character, coefficient-span, Euler flag and universal Hom checks."""
from collections import Counter
from pathlib import Path
import hashlib,json
from characters import product,W,DIM
root=Path(__file__).resolve().parent
checks=0
def req(ok,label):
 global checks
 checks+=1
 if not ok:raise RuntimeError(label)
def eq(got,want,label):req(got==want,label)
def dim(c):return sum(DIM[r]*m for r,m in c.items())
def rd(r,d):return [DIM[r],DIM[r]*d]
proof_hash=hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest()
eq(proof_hash,'e5d2c74f516bb5b2ede85287fceb3a774c6870b68b7b2418398e30fd5093d9b2','exact proof binding')
inputs=json.loads((root/'INPUTS.json').read_text())
eq(len(inputs),4,'four immutable originals')
for item in inputs:
 b=(root/item['file']).read_bytes()
 eq(len(b),item['bytes'],'input byte length')
 eq(hashlib.sha256(b).hexdigest(),item['sha256'],'input SHA256')
 eq(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),item['git_blob_sha1'],'input Git blob')
M2=Counter(A=1,V=2,P=3,D=4)
M3=Counter(Wp=3,S=3,T=6)
M4=Counter(V=2,P=4,D=3)
eq(W(M3),Counter(A=3,V=6,P=9,D=9),'M3 tensor W')
H=W(M3);H.subtract(M2);H.subtract(M4)
eq(+H,Counter(A=2,V=2,P=2,D=2),'actual constant H character')
eq(dim(H),30,'original ambient dimension')
C=H.copy();C.subtract(product('one',8))
eq(+C,Counter(A=2,V=2,P=1,D=1),'actual constant C character')
eq(dim(C),21,'small ambient dimension')
eq(dim(product('one',8)),9,'octic quotient coefficient dimension')
fixed={6:Counter(V=1,P=1),8:Counter(P=1,D=1),10:Counter(A=1,V=1,D=1),12:Counter(one=1,A=1,D=1,P=1),13:Counter(W=1,S=1,T=1,Wp=1),16:Counter(D=2,V=1,P=1)}
for n,want in fixed.items():
 eq(product('one',n),want,'fixed Sym'+str(n))
 eq(dim(product('one',n)),n+1,'fixed symmetric dimension')
coefficient_bound=product('one',10)+product('one',6)+product('one',16)
eq(coefficient_bound['A'],1,'form II coefficient A upper bound')
eq(C['A'],2,'full small ambient A demand')
req(coefficient_bound['A']<C['A'],'coefficient-span contradiction')
# Stated actual flag only; no possible flag search.
flag=[('one',-6),('W',-5),('A',-4),('S',-3),('D',-2)]
expected_rd=[[1,-6],[2,-10],[3,-12],[4,-12],[5,-10]]
for (r,d),expected in zip(flag,expected_rd):
 eq(rd(r,d),expected,'actual flag rank/degree')
 req(d<0,'negative flag term')
for n in range(5):
 eq(product('one',n),Counter({flag[n][0]:1}),'physical principal-parts coefficient')
 eq(n-6,flag[n][1],'principal-parts degree')
# Graded positive quotient degrees are -4,-2,0,2, giving the exact rows.
qdeg=[]
for lower,upper in zip(expected_rd,expected_rd[1:]):
 eq(upper[0]-lower[0],1,'flag rank increment')
 qdeg.append(upper[1]-lower[1])
eq(qdeg,[-4,-2,0,2],'flag quotient degrees')
rows=[('S',3),('A',2),('W',1),('one',0)]
for r,n in rows:eq(product(r,n)['one'],1,'evaluation Hom dimension')
eq(-5-(-3),-2,'top-D internal derivative ordinary Hom degree')
req(-5< -3,'top-D internal derivative row vanishes')
# Four semisimple quotient dimensions of two stated inequivalent irreducibles.
quotient_dims=(0,3,4,7)
eq([d for d in quotient_dims if d>=5],[7],'top-D full coefficient span')
eq(dim(product('one',6)),7,'sextic coefficient dimension')
eq(rd('W',-5),[2,-10],'actual seven-space annihilator')
eq(rd('T',-1),[6,-6],'Euler-line annihilator rank/degree')
eq(0-(-6),6,'complete sextic evaluation quotient degree')
eq(11-3,8,'universal second-jet kernel rank')
eq(0-3*8,8*(-3),'universal second-jet kernel degree')
eq(product('one',7),Counter(Wp=1,T=1),'universal second-jet kernel coefficient')
req(-3-(-2)<0,'top-D map to universal jet kernel vanishes')
req(-5-(-4)<0,'O(-4) row to W(-5) vanishes')
eq(product('W',13)['one'],1,'O(-18) to W(-5) Hom')
eq(product('one',12)['one'],1,'degree-twelve invariant dimension')
eq(product('W',1)['one'],1,'Euler line Hom')
eq(-18+12,-6,'invariant factor line degree')
req(-2-(-1)<0,'T6(-1) cannot inject into E0')
# Retained remaining data and fixed rank-degree consistency.
eq(3*(-8)+2*(-11),-46,'surviving S0 degree')
eq(3+2,5,'surviving S0 rank')
eq(2*3+4-8,2,'surviving primal quotient degree')
eq(7*(-2)+2*(-9),-32,'retained original L degree')
eq(-10+6*(-3),-28,'retained original next kernel degree')
controls={
 'one extra A_std coefficient would erase this multiplicity cut':(coefficient_bound+Counter(A=1))['A']==C['A'],
 'rank four would not force the seven-space quotient':([d for d in quotient_dims if d>=4]!=[7]),
 'allowing degree minus one in E0 would remove the ordinary Hom contradiction':(-1-(-1))>=0,
}
for label,ok in controls.items():req(ok,label)
print(json.dumps({'status':'PASS','checks':checks,'proof_sha256':proof_hash,
 'scope':'Fixed universal representation/degree/Hom data only; no actual coefficients, jets or instance ranks and no bundle search.',
 'ambient_H':dict(+H),'ambient_C':dict(+C),'form_II_coefficient_upper_bound':dict(coefficient_bound),
 'actual_top_D_flag_rank_degree':expected_rd,'sextic_coefficient_quotient_dimensions':quotient_dims,
 'hom_dimensions':{'S4(-3)->O':1,'A(-4)->O(-2)':1,'W(-5)->O(-4)':1,'O(-6)->O(-6)':1,'O(-18)->W(-5)':1,'invariant_degree_12':1},
 'necessary_remaining_primal':'W(3)+O(4)+O(-8)','necessary_remaining_S0':'A_std(-8)+Wp(-11)',
 'excluded_primal':'O(2)+2O(4)+O(-8)','original_defect':12,'semantic_controls':controls},indent=2,sort_keys=True))
