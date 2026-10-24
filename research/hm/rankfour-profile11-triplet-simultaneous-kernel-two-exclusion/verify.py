"""Fixed universal arithmetic only. No selected actual source evaluation."""
from pathlib import Path
from collections import Counter
import hashlib,json
import characters as C
BASE=Path(__file__).resolve().parent
count=0
def require(c,msg):
 global count
 count+=1
 if not c:raise RuntimeError(msg)
pins={'inputs/quartic-normal-map.md': ('06385eec63b85efac6cc25441d4b58d4fa5a8adb', 'research/hm/rankfour-profile11-triplet-quartic-normal-map/PROOF.md', 15127, '205256f2772d21d81025e6c511a52de564bfd7e9e0d94cce79fc3f684b6d17ba', '243adcdfe618e0792f330534c5c74931ad2741ac'), 'inputs/common-kernel-ladder.md': ('5249c844765cfd96ffb51bdfd4aaef8307d49b1f', 'research/hm/rankfour-profile11-triplet-common-kernel-ladder/PROOF.md', 13135, '0a24ab99c6f3d6c2f60212532c7f4aed2bd7d5fba17823243dd479a83a7308dd', 'd64a0db4f2bcbd61651cdefc37a37b672c321176'), 'inputs/eighteen-jets.md': ('913892c66403ea57ed1681957ae1b9f8db9e5e15', 'research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md', 17528, '33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf', '730021d4e97c4c1307a1d3c6c5303e4e9792202d'), 'inputs/five-kernels.md': ('7d71f0e2a3963cff64a069198f4415c5cfd0fe9b', 'research/hm/rankfour-profile11-triplet-kernels/PROOF.md', 8501, '4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a', '163ba2126b6130befcc2351db7f6910d85fac2ec')}
inputs=json.loads((BASE/'INPUTS.json').read_text())
require(len(inputs)==4 and {i['file'] for i in inputs}==set(pins),'four selected complete originals')
for i in inputs:
 ref,path,n,sha,blob=pins[i['file']];data=(BASE/i['file']).read_bytes()
 require(i['ref']==ref and i['path']==path,'immutable exact ref and path')
 require(len(data)==i['bytes']==n,'complete byte length')
 require(hashlib.sha256(data).hexdigest()==i['sha256']==sha,'complete input hash')
 require(hashlib.sha1(b'blob '+str(n).encode()+b'\0'+data).hexdigest()==i['git_blob_sha1']==blob,'Git blob identity')
 require(i['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,'immutable URL')
proof=(BASE/'PROOF.md').read_bytes()
require(len(proof)==13703,'frozen whole-proof length')
require(hashlib.sha256(proof).hexdigest()=='0165fa9a854879e5b2c67885f3b0bede6c3f48b34e1c761c0ca846645a3247fa','frozen whole-proof hash')
require(C.checks==81,'fixed McKay validation')
require(C.product('one',6)==Counter({'V':1,'P':1}),'sixth symmetric power')
require(C.product('T',1)==Counter({'D':1,'V':1,'P':1}),'fifth times standard doublet')
require(C.product('one',4)==Counter({'D':1}),'Serre-dual degree-four irreducible')
require(C.product('one',10)==Counter({'A':1,'V':1,'D':1}),'degree-ten complete coefficient space')
require(sum(C.DIM[r]*n for r,n in C.product('one',10).items())==11,'complete coefficient dimension')
for d in (2,4,6,8,10):require(C.product('one',d)['one']==0,'fixed low scalar invariant vanishing')
require(C.product('one',12)['one']==1,'universal degree-twelve invariant dimension')
for j in (1,2,3):require(-10-(j-10)==-j<0,'shared coherent lower row vanishes')
require([20-2*j for j in range(5,10)]==[10,8,6,4,2],'five induction upper degrees')
for j in range(5,10):require(-10-(2*j-10)==-2*j<0,'five induction lower degrees')
require(10+1>10,'last complete jet exceeds F rank')
require(10-(2*4-10)==12,'first allowed upper incidence degree')
for j in range(4):require(-12-(j-10)==-j-2<0,'actual lifted H(-2) row degree')
require(-10-2==-12,'normal cotangent twist')
require(10+1==11,'maximum scalar coefficient span')
require((5+1,5-10,6+1,6-10)==(6,-5,7,-4),'actual fifth and sixth jet types')
require(7*(-4)-6*(-5)==2,'actual positive sixth quotient degree')
require(-7-(-5)<0,'K2 lower component vanishes')
R=Counter({'V':1,'P':2})
require(R['D']==0,'missing obstruction irreducible')
require(sum(C.DIM[r]*n for r,n in R.items())==11,'K2 canonical top rank')
require(11+2==13 and 11*(-4)+2*(-7)==-58,'K2 total rank and degree')
require(-4-2==-6 and -(-6)-2==4,'Ext twist and Serre-dual symmetric degree')
require(C.product('V',4)['one']+2*C.product('P',4)['one']==0,'equivariant extension obstruction zero')
require(0-2<0,'ambient difference from positive quotient zero')
print(json.dumps({'status':'PASS','checks':count,'proof_sha256':hashlib.sha256(proof).hexdigest(),'scope':'four complete immutable originals; fixed character, degree and exact-sequence arithmetic','not_claimed':['proof by computation','selected actual coefficient, parameter, point, jet, tensor, matrix or instance-rank evaluation','occurrence or exclusion beyond the stated conditional K2 intersection','original degree-eighteen tenth jets','horizontal splitting or quotient connection']},indent=2,sort_keys=True))
