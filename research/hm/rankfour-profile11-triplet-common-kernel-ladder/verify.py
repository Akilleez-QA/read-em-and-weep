#!/usr/bin/env python3
"""Bounded universal arithmetic and exact proof/source pins only."""
from pathlib import Path
import hashlib
import json
from characters import product,NAMES,DIM,chars,q

ROOT=Path(__file__).resolve().parent
CHECKS=0
def require(condition,label):
    global CHECKS
    CHECKS+=1
    if not condition: raise RuntimeError(label)

PROOF_SHA='0a24ab99c6f3d6c2f60212532c7f4aed2bd7d5fba17823243dd479a83a7308dd'
PINS=[
 ('inputs/nine-jets.md','66a6bfe8dd424da58f3d775be1818d1f4f71eff1',
  'research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md',12744,
  '44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a',
  '916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6'),
 ('inputs/twelve-orientation.md','8ca4ccd046248752714a84dfb05aae42a6433f55',
  'research/hm/rankfour-profile11-triplet-twelve-orientation/PROOF.md',12396,
  'a9b56b6f84c9a11dedb94639bf16ab5c1065e21a91d067c52f75435d4b014da2',
  'e698ba5aa8caf0ffdc0aa28baec9d0ba8f036eda')]
proof=(ROOT/'PROOF.md').read_bytes()
require(len(proof)==13135,'exact complete proof length')
require(hashlib.sha256(proof).hexdigest()==PROOF_SHA,'exact frozen proof SHA256')
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==len(PINS)==2,'two complete direct inputs')
for rec,pin in zip(manifest,PINS):
    file,ref,path,length,sha,blob=pin; data=(ROOT/file).read_bytes()
    require(rec['file']==file and rec['ref']==ref and rec['path']==path,'immutable source pin')
    require(rec['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,'source URL')
    require(rec['bytes']==len(data)==length,'complete source length')
    require(rec['sha256']==hashlib.sha256(data).hexdigest()==sha,'complete source SHA256')
    computed=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(rec['git_blob_sha1']==computed==blob,'complete source Git blob')

def capacity(n,a,b,k):
    return (n-k)*a+k*b-(n-k)*(n-k-1)-k*(k-1)

# Exactly three displayed common-kernel stages and their fixed arithmetic.
rank=10; degree=-64
for j,n,d in ((4,9,-74),(5,8,-82),(6,7,-88)):
    a=16-2*j; previous_normal=a+2
    require(rank-1==n and degree-previous_normal==d,'common-kernel rank and degree')
    require(-(j+1)*(18-j)-4==d,'actual B_j/F_j quotient degree')
    require((14-j)-1==n,'actual quotient rank')
    require(n*(-10)-n*(n-1)<d,'rank-one image contradicted')
    require(j-18<0 and -4<0,'both dual extension end terms have no H0')
    rank,degree=n,d
require([9*(-10)-9*8,8*(-10)-8*7,7*(-10)-7*6]==[-162,-136,-112],
        'three rank-one bounds')

# Fixed degree inequalities for precisely the permitted quotient-rank counts.
v4=[capacity(9,-2,-10,k) for k in range(1,5)]
require(v4==[-82,-78,-78,-82],'rank-nine upper polynomial values')
require(max(v4)==-78 and -78<-74,'rank-nine contradiction threshold')
require(all(capacity(9,-2,-10,k)==-90+10*k-2*k*k for k in range(1,5)),
        'rank-nine polynomial identity')
v5=[capacity(8,-6,-10,k) for k in range(1,5)]
require(v5==[-94,-88,-86,-88],'rank-eight upper polynomial values')
require(max(v5)==-86 and -86<-82,'rank-eight contradiction threshold')
require(all(capacity(8,-6,-10,k)==-104+12*k-2*k*k for k in range(1,5)),
        'rank-eight polynomial identity')
v6=[capacity(7,-10,-10,k) for k in range(1,4)]
require(v6==[-100,-92,-88],'rank-seven equal-top endpoint')
require([k for k in range(1,4) if capacity(7,-10,-10,k)==-88]==[3],
        'unique rank-seven equality count')
require(all(capacity(7,-10,-10,k)==-112+14*k-2*k*k for k in range(1,4)),
        'rank-seven polynomial identity')

# Physical universal character facts; no actual coefficient system is tested.
require(sorted(DIM[r] for r in NAMES if chars[r][1]==q(DIM[r]))==[1,3,3,4,5],
        'center-even irreducible dimensions')
require(product('one',14)['one']==0,'invariant degree14 vanishes')
require(product('one',0)['one']==1,'endpoint identity Hom does not vanish')
require(min((12,20,30,60))==12,'minimum invariant effective divisor')
require(14<20 and 14<2*12,'no degree14 invariant orbit combination')
require(4-(-8)==12 and 4-(-10)==14,'rank-seven top and cross-term degrees')
require(8-(-1)<12 and 6-(-5)<12,'strict degree ranges force earlier top lines')

# Embedded defect lengths, not values of the original delta or e9.
require((8+2)-(8-10)==12,'rank-nine normal defect')
require((6+2)-(6-10)==12,'rank-eight normal defect')
require((4+2)-(4-10)==12,'cyclic rank-seven normal defect')
require((4+2)-(-8-10)==24,'both-direction rank-seven normal defect')
require(2-12==-10 and 4-12==-8,'two actual D12 twists')
require(12*(1+1)==24,'both-direction local elementary divisor lengths')

print(json.dumps({'status':'PASS','checks':CHECKS,'proof_sha256':PROOF_SHA,
 'scope':'two complete immutable input pins; three fixed actual-ladder degree stages and universal characters',
 'not_claimed':['actual instance or jet evaluation','exclusion of either rank7 alternative',
 'identification of different local defects','geometric proof by computation']},sort_keys=True,indent=2))
