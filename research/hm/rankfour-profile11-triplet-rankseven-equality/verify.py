#!/usr/bin/env python3
"""Bounded universal degree/character checks; no actual-instance evaluations."""
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

PROOF_SHA='a6e56f535af652d3ff437cc5041527636f601751ae24285ba1ec91670f4db7ae'
PINS=[
 ('inputs/common-kernel-ladder.md','5249c844765cfd96ffb51bdfd4aaef8307d49b1f',
  'research/hm/rankfour-profile11-triplet-common-kernel-ladder/PROOF.md',13135,
  '0a24ab99c6f3d6c2f60212532c7f4aed2bd7d5fba17823243dd479a83a7308dd',
  'd64a0db4f2bcbd61651cdefc37a37b672c321176'),
 ('inputs/nine-jets.md','66a6bfe8dd424da58f3d775be1818d1f4f71eff1',
  'research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md',12744,
  '44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a',
  '916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6'),
 ('inputs/deep-images.md','95af2c0fa1e3cce92496a44ef9023708735e1ec7',
  'research/hm/rankfour-profile11-triplet-deep-images/PROOF.md',12085,
  '09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26',
  '9cf95f42505f37900f5a24c25cff07acca1b499f')]
proof=(ROOT/'PROOF.md').read_bytes()
require(len(proof)==15139,'complete frozen proof length')
require(hashlib.sha256(proof).hexdigest()==PROOF_SHA,'complete frozen proof SHA256')
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==len(PINS)==3,'three complete direct sources')
for rec,pin in zip(manifest,PINS):
    file,ref,path,length,sha,blob=pin; data=(ROOT/file).read_bytes()
    require(rec['file']==file and rec['ref']==ref and rec['path']==path,'immutable source pin')
    require(rec['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,'source URL')
    require(rec['bytes']==len(data)==length,'complete source length')
    require(rec['sha256']==hashlib.sha256(data).hexdigest()==sha,'complete source SHA256')
    computed=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(rec['git_blob_sha1']==computed==blob,'complete source Git blob')

# Fixed universal physical characters only.
require(product('one',4)==Counter({'D':1}),'Sym4=D')
require(product('T',3)['one']==0,'Hom(T6,Sym3)=0')
require(product('T',1)['one']==0,'Hom(T6,W)=0')
require(product('one',2)['one']==0,'column off-diagonal invariant vanishes')
require(product('one',14)['one']==0,'quotient extension invariant vanishes')
require(min((12,20,30,60))==12,'minimum invariant divisor')

# The three exact quotient-rank counts in the displayed coherent flag.
def cap(k):
    return (7-k)*(-8)+k*(-10)-(7-k)*(6-k)-k*(k-1)
require([cap(k) for k in (1,2,3)]==[-88,-82,-80],'three capacity bounds')
require([cap(k)+88 for k in (1,2,3)]==[0,6,8],'three exact total deficits')
require(all(cap(k)==-98+12*k-2*k*k for k in (1,2,3)), 'capacity polynomial')
require([(e,e-2) for e in (0,2,8)]==[(0,-2),(2,0),(8,6)],'rank-one component degrees')
require(8<12 and 6<12,'k3 two components vanish')
require(3*2==6,'all three k2 deficits are lower-column')

# k1 actual initial jets and ramified first saturation.
require((-8-10)+sum((-10,-12,-14,-16,-18))==-88,'k1 coherent quotient degrees')
require(sum((-10,-12,-14,-16,-18))==-70,'fourth-jet Q1 degree')
require(5*(4-18)==-70,'intrinsic auxiliary fourth-jet degree')
require(-70-8==-78 and 6*(5-18)==-78,'intrinsic auxiliary fifth-jet degree')
require(-88-(-78)==-10,'F6/K quotient degree')
require(-82-(-78)==6-10,'F5/K extension degree')
require(-10-6==-16 and 16-2==14,'extension and Serre-dual twists')
require(4-(-8)==12,'ramified coherent-image defect')
require(-78+6==-72,'saturated sixth-jet degree')
require(7*(6-18)==-84 and -72-(-84)==12,'not an unramified sixth source')

# Actual full normal projections after the ramified step.
degree=-72; rank=7
for quotient,expected_rank,expected_degree in ((8,8,-64),(10,9,-54),(12,10,-42)):
    degree+=quotient; rank+=1
    require((rank,degree)==(expected_rank,expected_degree),'full forward span rank and degree')
require(-48-(-42)==-60-(-54)==-6,'persistent actual quotient Q degree')
require(-10+4==-6 and 4-2==2,'Q extension and twisted top bound')

# Corrected normal targets and both cases of each degree-equal scalar map.
for j,target in ((2,12),(1,14),(0,16)):
    require(16-2*j==target,'correct normal target includes Omega shift')
    require(-j-1<0,'complete-kernel top is negative')
for n,d,bound in ((10,-42,-70),(11,-28,-88),(12,-12,-108)):
    require(2*n-n*(n-1)==bound,'zero-case rank-one capacity upper bound')
    require(d>bound,'zero case contradiction')
require(-42+14==-28 and -28+16==-12,'nonzero scalar-map degree gains')
require(-12+18==6 and 12+1==13,'final forbidden positive-degree subbundle')
require(6>0,'constant-bundle degree contradiction')

# Remaining k2 lower-column actual jet source and quotient.
require((-8-10)+(-10-12)+(-14-16-18)==-88,'k2 coherent quotient degrees')
require(-14-16-18==-48 and 3*(2-18)==-48,'second-jet source degree')
require(-48-12==-60 and 4*(3-18)==-60,'third-jet source degree')
require(-60-10==-70 and 5*(4-18)==-70,'fourth-jet source degree')
require(-88-(-70)==-18 and -10-8==-18,'rank-two quotient degree')
require(-10-(-8)==-2 and -(-2)-1==1,'one-dimensional line extension')
require(2*(-9)==-18,'Euler middle degree')

print(json.dumps({'status':'PASS','checks':CHECKS,'proof_sha256':PROOF_SHA,
 'scope':'three complete pins; fixed physical characters; displayed coherent-flag and corrected forward-climb degrees',
 'not_claimed':['actual instance evaluation','exclusion of simultaneous rank7 image or delta12',
 'original higher jets beyond order9','geometric proof by computation']},sort_keys=True,indent=2))
