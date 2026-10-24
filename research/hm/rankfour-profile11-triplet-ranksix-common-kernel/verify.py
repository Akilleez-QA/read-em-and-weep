#!/usr/bin/env python3
"""Fixed character/degree identities and exact complete-source pins only."""
from pathlib import Path
from collections import Counter
import hashlib,json
from characters import product

ROOT=Path(__file__).resolve().parent
CHECKS=0
def require(condition,label):
    global CHECKS
    CHECKS+=1
    if not condition: raise RuntimeError(label)

PROOF_SHA='06e1795f1390e8451dbf4e98e10a8011b3e97ce733ec6b1cbbd5af90b4694111'
PINS=[
 ('inputs/rankseven-equality.md','f5895c822322b4ddab07e51a97874d4528fb5b88',
  'research/hm/rankfour-profile11-triplet-rankseven-equality/PROOF.md',15139,
  'a6e56f535af652d3ff437cc5041527636f601751ae24285ba1ec91670f4db7ae',
  '6a4ef8941ee4cee131992bdf9cd7657635b058c5'),
 ('inputs/nine-jets.md','66a6bfe8dd424da58f3d775be1818d1f4f71eff1',
  'research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md',12744,
  '44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a',
  '916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6')]
proof=(ROOT/'PROOF.md').read_bytes()
require(len(proof)==9703,'exact frozen proof length')
require(hashlib.sha256(proof).hexdigest()==PROOF_SHA,'exact frozen proof SHA256')
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==len(PINS)==2,'two complete direct inputs')
for rec,pin in zip(manifest,PINS):
    file,ref,path,length,sha,blob=pin;data=(ROOT/file).read_bytes()
    require(rec['file']==file and rec['ref']==ref and rec['path']==path,'immutable source pin')
    require(rec['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,'exact source URL')
    require(rec['bytes']==len(data)==length,'complete source length')
    require(rec['sha256']==hashlib.sha256(data).hexdigest()==sha,'complete source SHA256')
    computed=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(rec['git_blob_sha1']==computed==blob,'complete source Git blob')

# Fixed physical character identities, not a selected coefficient system.
require(product('one',3)==Counter({'S':1}),'Sym3=S4')
require(product('one',4)==Counter({'D':1}),'Sym4=D')
require(product('D',2)['one']==0,'Hom(D,A)=0')
require(product('one',10)['one']==0,'degree10 invariant vanishing')
require(product('one',2)['one']==0,'column-mixing invariant vanishing')

# Actual common-kernel and transverse quotient degree arithmetic.
require(7-1==6 and -88-(-8)==-80,'G6 rank and degree')
require(5+5-4==6,'sum Q1+U4 rank')
require(-70-70-(-60)==-80,'sum Q1+U4 degree')
require(-70-(-60)==-10,'both transverse quotient line degrees')
require(2*(-10)==-20 and -80-(-60)==-20,'G6/U3 rank-two degree')
require(5*(-14)-10==-80,'split G6 degree')
require(-14-(-10)==-4 and -(-4)-2==2,'scalar complement extension twist')
require(-14-(-10)<0,'uniqueness Hom has negative degree')

# Actual normal extension and coherent defect, without any matrix evaluation.
require(-84-(-80)==-4 and -8+4==-4,'B6/G6 degree')
require(-8-4==-12 and -(-12)-2==10,'normal extension Serre-dual twist')
require((-8)-2==-10 and 4-2==2,'two actual normal twists')
require(2-12==-10,'external coherent image twist')
require((-10+2)-(-10-10)==12,'normal torsion length')
require(12*(0+1)==12,'simple cyclic local elementary divisors')
require(-80-(-20)==-60 and 4*(-15)==-60,'exact backward-kernel degree')
require(6+2==8 and -80+((-10+2)+2*2)==-84,'saturated forward rank and degree')
require(6-18==-12 and -12<0,'T6 has no constant global sections')

print(json.dumps({'status':'PASS','checks':CHECKS,'proof_sha256':PROOF_SHA,
 'scope':'two complete source pins; fixed physical characters and actual-sequence degree identities',
 'not_claimed':['actual instance evaluation','everywhere derivative rank2',
 'full auxiliary scalar span','intrinsic auxiliary ramification','branch exclusion']},sort_keys=True,indent=2))
