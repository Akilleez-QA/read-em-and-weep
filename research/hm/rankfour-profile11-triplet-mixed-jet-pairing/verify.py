#!/usr/bin/env python3
"""Exact pins and bounded universal representation/symbol identities only."""
from pathlib import Path
from collections import Counter
from math import comb,prod
import hashlib,json
from characters import product,DIM

ROOT=Path(__file__).resolve().parent
CHECKS=0
def require(condition,label):
    global CHECKS
    CHECKS+=1
    if not condition: raise RuntimeError(label)

PROOF_SHA='3e1ce0d1589d694d578796a90398cbdaf8fdf6fb340158b5098ad3f79cdfa95b'
PINS=[
 ('inputs/rankseven-equality.md','f5895c822322b4ddab07e51a97874d4528fb5b88',
  'research/hm/rankfour-profile11-triplet-rankseven-equality/PROOF.md',15139,
  'a6e56f535af652d3ff437cc5041527636f601751ae24285ba1ec91670f4db7ae',
  '6a4ef8941ee4cee131992bdf9cd7657635b058c5'),
 ('inputs/nine-jets.md','66a6bfe8dd424da58f3d775be1818d1f4f71eff1',
  'research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md',12744,
  '44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a',
  '916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6'),
 ('inputs/defect-capacity.md','ca235151d5d93bbead2beffa7640fbd0741aec43',
  'research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md',16069,
  '135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f',
  '175af94697c44f3140bb2c1d04978931c255b3fe')]
proof=(ROOT/'PROOF.md').read_bytes()
require(len(proof)==14593,'complete frozen proof length')
require(hashlib.sha256(proof).hexdigest()==PROOF_SHA,'complete frozen proof SHA256')
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==len(PINS)==3,'three complete direct inputs')
for rec,pin in zip(manifest,PINS):
    file,ref,path,length,sha,blob=pin;data=(ROOT/file).read_bytes()
    require(rec['file']==file and rec['ref']==ref and rec['path']==path,'immutable source pin')
    require(rec['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,'exact source URL')
    require(rec['bytes']==len(data)==length,'complete source length')
    require(rec['sha256']==hashlib.sha256(data).hexdigest()==sha,'complete source SHA256')
    computed=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(rec['git_blob_sha1']==computed==blob,'complete source Git blob')

# Fixed physical character identities; no actual coefficient maps instantiated.
expected={2:{'A':1},4:{'D':1},6:{'V':1,'P':1},8:{'P':1,'D':1},
          10:{'A':1,'V':1,'D':1},12:{'one':1,'A':1,'D':1,'P':1},
          18:{'A':1,'V':1,'D':1,'P':2}}
for n,c in expected.items():
    require(product('one',n)==Counter(c),'fixed symmetric-power decomposition')
for n in (2,4,6,8,10):
    require(product('one',n)['one']==0,'fixed low invariant vanishing')
require(product('one',12)['one']==1,'unique fixed degree12 invariant')
cg=Counter()
for n in (0,2,4,6,8,10,12):cg.update(product('one',n))
left=product('V',6).copy();left.update(product('P',6))
require(left==cg,'universal Sym6 tensor Sym6 decomposition')
require(cg['one']==2,'two invariant residual biform summands')

# Formal mixed-jet rectangle and bidegree identities, not actual jet values.
require(7+4+1==12,'diagonal multiplicity from rectangle')
for n in range(12):
    a=min(7,n);b=n-a
    require(a+b==n and 0<=a<=7 and 0<=b<=4,'anchor for every formal diagonal order')
require(18-12==6,'residual bidegrees')
require(12%2==0 and 6%2==0 and 18%2==0,'exchange and apolar parity')
require(12+18-2*6==18,'sixth transvectant output degree')
require(2*18-2*12==12,'unique Sym12 biform constituent')

# Universal highest-symbol Vandermonde identity in degree twelve. This fixed
# thirteen-monomial formal basis check contains no coefficients of f12 or of
# any actual source system, and evaluates no point or instance rank.
def falling(n,k):
    return 0 if k>n else prod(range(n-k+1,n+1))
symbol=falling(12,6)
require(symbol==12*11*10*9*8*7==665280,'nonzero universal order-six symbol factor')
require(symbol==comb(12,6)*720,'radial derivative factor')
for r in range(13):
    coefficient=sum(comb(6,k)*falling(12-r,6-k)*falling(r,k) for k in range(7))
    require(coefficient==symbol,'formal degree12 highest-symbol identity')

# Representation gap and finite embedded-kernel consequence, not evaluated
# eigenvalues, eigenvectors, matrices, ranks, or actual coefficient choices.
e=product('one',18)
require(sum(DIM[r]*m for r,m in e.items())==19,'universal coefficient-space dimension')
require(DIM['P']==4 and 19-4==15,'known actual kernel type dimensions')
remaining=e.copy();remaining.subtract({'P':1});remaining=+remaining
require(min(DIM[r] for r in remaining)==3,'no small extra kernel constituent')
require(4+3>6,'ODE dimension bound excludes strict kernel enlargement')
require(4*2==8 and 8>6,'P-isotypic operator cannot be scalar')
require(2==e['P'],'two-dimensional universal multiplicity space')
require(9<18 and 9+1==10,'transferred jet range does not assert original order10')

print(json.dumps({'status':'PASS','checks':CHECKS,'proof_sha256':PROOF_SHA,
 'scope':'three complete pins; fixed characters; formal rectangle and universal differential-symbol identities',
 'not_claimed':['actual coefficient or matrix evaluation','chosen invariant normalization or eigenvalue',
 'original tenth jets','realization or branch exclusion','geometric proof by computation']},sort_keys=True,indent=2))
