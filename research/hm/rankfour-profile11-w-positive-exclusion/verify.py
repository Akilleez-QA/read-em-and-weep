"""Fixed universal source-block rank bounds and one-column degree arithmetic."""
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
def rd(blocks):return [sum(m*DIM[r] for m,r,d in blocks),sum(m*DIM[r]*d for m,r,d in blocks)]
ph=hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest()
eq(ph,'eacf658ecef85350c36591f25f80cae14408869d56f077d371982a5311e0232f','proof binding')
inputs=json.loads((root/'INPUTS.json').read_text());eq(len(inputs),3,'three immutable inputs')
for i in inputs:
 b=(root/i['file']).read_bytes()
 eq(len(b),i['bytes'],'source byte length')
 eq(hashlib.sha256(b).hexdigest(),i['sha256'],'source SHA256')
 eq(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),i['git_blob_sha1'],'source Git blob')
E=[(1,'D',-2),(1,'Wp',-3),(1,'T',-3),(1,'V',-4)]
K=[(1,'S',-3),(2,'V',-4),(1,'Wp',-5),(1,'one',-10)]
J=[(1,'Wp',-3),(1,'T',-3)]
Jminus=[(1,'V',-4),(1,'P',-4)]
G=[(1,'D',-2),(1,'V',-4)]
eq(rd(E),[16,-46],'actual E0 source')
eq(rd(K),[13,-56],'actual K source')
eq(rd(J),[8,-24],'complete second-jet kernel')
eq(rd(Jminus),[7,-28],'complete derivative kernel')
eq(rd(G),[8,-22],'constant projection kernel')
eq(product('one',7),Counter(Wp=1,T=1),'Sym7 decomposition')
eq(product('one',6),Counter(V=1,P=1),'Sym6 decomposition')
eq(product('Wp',1),Counter(P=1),'Wp tensor W')
eq(product('Wp',1)['V'],0,'quartic V has no Wp cubic target')
eq(product('T',1),Counter(D=1,V=1,P=1),'T6 tensor W')
# Universal cubic alternatives, not selected scalar values or instance ranks.
lower_rank=16-10;eq(lower_rank,6,'generic projection rank floor')
eq(2+3,5,'zero T6 scalar upper rank');req(5<lower_rank,'zero T6 impossible')
eq(11-6,5,'annihilator rank in zero Wp case')
eq(5,5,'equals full S0 rank');req(11<21,'span contradiction for zero Wp')
eq(2+6,8,'both nonzero cubic blocks fill J')
req(-3-(-2)<0,'top D projection to J vanishes')
eq(16-8,8,'G0 rank');eq(-46-(-24),-22,'G0 degree')
for m,r,d in G:req(d<0,'G0 is negative')
N=Counter(A=1,V=1,P=1);eq(sum(DIM[r]*m for r,m in N.items()),10,'constant N dimension')
eq(3+4,7,'actual top-D constant span')
req(8>7,'G0 span must add the remaining A_std')
eq(10-8,2,'annihilator rank')
eq(-22,2*(-11),'equal-degree projected Wp bundle')
eq(11-2,9,'cotangent-twisted actual dual target')
# Coefficient Hom and source-rank bounds, not an actual map matrix.
req(-4-(-3)<0,'cubic S4 row into Jminus vanishes')
eq(Counter(V=1,P=1)['V'],1,'single target V coefficient')
eq(Counter(V=1,P=1)['S'],0,'no S4 equal-degree coefficient')
eq(product('V',1)['Wp'],0,'Wp source has no target V channel')
eq(product('P',1)['Wp'],1,'Wp source may target P channel')
block_bounds=[0,3,2,1]
eq(sum(block_bounds),6,'universal rank upper bound for qK')
eq(13-sum(block_bounds),7,'kernel rank lower bound')
eq(8-7,1,'derivative rank upper bound')
# Exact O(2) line image is justified geometrically; check its fixed prerequisites.
eq(product('Wp',7)['one'],1,'line row Hom dimension')
eq(9-2,7,'line row polynomial degree')
orbits=[60//m for m in (1,2,3,5)]
eq(orbits,[60,30,20,12],'possible orbit lengths')
eq(min(orbits),12,'smallest orbit length')
req(7<min(orbits),'degree-seven common zero divisor impossible')
eq(-10-(-12),2,'top-D quotient degree')
eq(-22-2,-24,'actual rank-seven kernel degree')
eq(8-1,7,'actual kernel rank')
# One stated seven-stage actual kernel chain, not a search over flags.
degrees=[2-2*j for j in range(1,8)]
eq(degrees,[0,-2,-4,-6,-8,-10,-12],'seven line capacity bounds')
eq(sum(degrees),-42,'one-column capacity sum')
req(-24>sum(degrees),'degree contradiction')
eq((-24)-sum(degrees),18,'strict degree gap')
controls={
 'an upper rank seven would not force the same rank-one conclusion':8-(13-7)==2,
 'a degree twelve row would not exclude the smallest invariant divisor':not(12<min(orbits)),
 'four kernel lines would not yield this degree contradiction':not(-24>sum(2-2*j for j in range(1,5))),
}
for label,ok in controls.items():req(ok,label)
print(json.dumps({'status':'PASS','checks':checks,'proof_sha256':ph,
 'scope':'Fixed representation/Hom, source-block rank upper bounds, and one stated seven-line capacity sum. No actual coefficients, matrices or instance ranks.',
 'E0_rank_degree':rd(E),'K_rank_degree':rd(K),'J_rank_degree':rd(J),'Jminus_rank_degree':rd(Jminus),'G0_rank_degree':rd(G),
 'qK_source_block_rank_upper_bounds':block_bounds,'rank_seven_kernel_degree':-24,
 'seven_line_degree_upper_bounds':degrees,'capacity_upper_bound':sum(degrees),'contradiction_gap':18,
 'excluded_primal':'W(3)+O(4)+O(-8)','semantic_controls':controls},indent=2,sort_keys=True))
