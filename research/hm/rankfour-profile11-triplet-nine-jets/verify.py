#!/usr/bin/env python3
"""Fixed universal degree identities and exact-byte pins, not actual jet tests."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib
import json
from characters import product

ROOT=Path(__file__).resolve().parent
CHECKS=0
def require(condition,label):
    global CHECKS
    CHECKS+=1
    if not condition:
        raise RuntimeError(label)

PROOF_SHA='44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a'
PINS=[
 ('inputs/twelve-orientation.md','8ca4ccd046248752714a84dfb05aae42a6433f55',
  'research/hm/rankfour-profile11-triplet-twelve-orientation/PROOF.md',12396,
  'a9b56b6f84c9a11dedb94639bf16ab5c1065e21a91d067c52f75435d4b014da2',
  'e698ba5aa8caf0ffdc0aa28baec9d0ba8f036eda'),
 ('inputs/projected-ranktwo.md','b2d020a32a3ac5aaf5f264e33e2f930c16195c34',
  'research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md',15271,
  '7f1567617b78898bcd218107de5bac5a71342a4cb34411862f7342d13699c4bd',
  '99a5a0257b0d683b04c5d190333d868c5b0d194d'),
 ('inputs/deep-images.md','95af2c0fa1e3cce92496a44ef9023708735e1ec7',
  'research/hm/rankfour-profile11-triplet-deep-images/PROOF.md',12085,
  '09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26',
  '9cf95f42505f37900f5a24c25cff07acca1b499f')]
proof=(ROOT/'PROOF.md').read_bytes()
require(len(proof)==12744,'complete frozen proof length')
require(hashlib.sha256(proof).hexdigest()==PROOF_SHA,'complete frozen proof SHA256')
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==len(PINS)==3,'three complete direct sources')
for rec,pin in zip(manifest,PINS):
    file,ref,path,length,sha,blob=pin
    data=(ROOT/file).read_bytes()
    require(rec['file']==file and rec['ref']==ref and rec['path']==path,'immutable source pin')
    require(rec['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,'exact source URL')
    require(rec['bytes']==len(data)==length,'complete source byte length')
    require(rec['sha256']==hashlib.sha256(data).hexdigest()==sha,'complete source SHA256')
    computed=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(rec['git_blob_sha1']==computed==blob,'complete source Git blob')

# Coefficient-level verification of the universal polynomial identity.
# (14-j)(3-j)=42-17j+j^2; (j+1)(18-j)=18+17j-j^2.
require(tuple(a+b for a,b in zip((42,-17,1),(18,17,-1)))==(60,0,0),
        'constant capacity budget sixty')
require(15-(3+1)==11 and -(3+1)*(18-3)==-60,'actual starting rank and degree')
require(18-2*3==12 and 16-2*3==10,'starting adjacent normal degrees')
require(min((12,20,30,60))==12,'minimum invariant orbit size')

# Exactly the six displayed universal induction stages, not a search over
# source-instance candidates or an evaluation of an actual differential map.
stages=[]
for j in range(3,9):
    n=14-j; degree=-(j+1)*(18-j); a=16-2*j
    require(n*a-n*(n-1)-degree==60,'rank-one capacity slack at fixed stage')
    require(Fraction(60,n)<12,'coherent defect below minimum invariant divisor')
    require(degree-a==-(j+2)*(17-j),'actual backward degree recurrence')
    require((j+2)*((j+1)-18)==degree-a,'intrinsic next source degree agrees')
    require(15-(n-1)==j+2,'next annihilator rank agrees')
    stages.append({'j':j,'annihilator_rank':n,'annihilator_degree':degree,
                   'normal_line_degree':a})
require([x['normal_line_degree'] for x in stages]==[10,8,6,4,2,0],
        'six forced full coherent normal lines')
require(10*(9-18)==-90 and 14-9==5,'original ninth-jet and annihilator degrees')

# Endpoint: only the arithmetic bounds and the equality flag are checked.
require(16-2*9==-2,'next normal degree')
require(5*(-2)-5*4-(-90)==60,'endpoint capacity budget')
require(Fraction(60,5)==12,'endpoint reaches twelve exactly')
require(5*(-14)-5*4==-90,'positive endpoint is capacity equality')
quotients=[-14,-16,-18,-20,-22]
require(sum(quotients)==-90,'five actual quotient degrees sum correctly')
require(all(quotients[i+1]==quotients[i]-2 for i in range(4)),
        'consecutive coherent quotient degrees')
for k in range(5):
    rank=k+1; degree=sum(quotients[4-k:])
    require(degree==rank*(k-22),'auxiliary intrinsic source degree')
    require(rank==5-(4-k),'auxiliary rank agreement')
require(product('one',4)==Counter({'D':1}),'fixed Sym4=D identity')
require(9-18<0,'original T9 has no constant sections')

print(json.dumps({'status':'PASS','checks':CHECKS,'proof_sha256':PROOF_SHA,
 'scope':'three complete source pins; six fixed universal degree stages; endpoint equality arithmetic',
 'not_claimed':['evaluation of any actual jet or coefficient','geometric proof by computation',
 'global original tenth-jet separation','endpoint realization or exclusion']},sort_keys=True,indent=2))
