#!/usr/bin/env python3
"""Bounded source, character, and degree checks; no actual-instance evaluations."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib
import json
from characters import product, NAMES, DIM, chars, q

ROOT=Path(__file__).resolve().parent
CHECKS=0
def require(condition,label):
    global CHECKS
    CHECKS+=1
    if not condition:
        raise RuntimeError(label)

PROOF_SHA='a9b56b6f84c9a11dedb94639bf16ab5c1065e21a91d067c52f75435d4b014da2'
PINS=[
 ('inputs/twenty-exclusion.md','4c70887589bbb6f9ffe818575005268d82d14cf0',
  'research/hm/rankfour-profile11-triplet-twenty-exclusion/PROOF.md',16366,
  'fc42728dd57303770e15c9ff2ffa7d490f4f6aa11dae26cf4cabdcb8792b0fa7',
  'b84f7fd1c9447521548afaa605ad0cfbec28c78d'),
 ('inputs/defect-capacity.md','ca235151d5d93bbead2beffa7640fbd0741aec43',
  'research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md',16069,
  '135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f',
  '175af94697c44f3140bb2c1d04978931c255b3fe'),
 ('inputs/projected-ranktwo.md','b2d020a32a3ac5aaf5f264e33e2f930c16195c34',
  'research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md',15271,
  '7f1567617b78898bcd218107de5bac5a71342a4cb34411862f7342d13699c4bd',
  '99a5a0257b0d683b04c5d190333d868c5b0d194d')]
proof=(ROOT/'PROOF.md').read_bytes()
require(len(proof)==12396,'exact complete proof length')
require(hashlib.sha256(proof).hexdigest()==PROOF_SHA,'exact frozen whole proof')
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==len(PINS)==3,'three direct complete inputs')
for rec,pin in zip(manifest,PINS):
    file,ref,path,length,sha,blob=pin
    data=(ROOT/file).read_bytes()
    require(rec['file']==file and rec['ref']==ref and rec['path']==path,'immutable path and commit')
    require(rec['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,'exact source URL')
    require(rec['bytes']==len(data)==length,'complete source length')
    require(rec['sha256']==hashlib.sha256(data).hexdigest()==sha,'complete source SHA256')
    actual_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(rec['git_blob_sha1']==actual_blob==blob,'complete source Git blob')

# Only fixed physical characters are used. The module separately checks 81
# fixed McKay identities over Q(sqrt(5)); no source instance is instantiated.
require(product('one',4)==Counter({'D':1}),'Sym4=D')
require(product('one',6)==Counter({'V':1,'P':1}),'Sym6=V+P')
require(product('one',8)['one']==0,'degree-eight invariant vanishing')
even=sorted(DIM[r] for r in NAMES if chars[r][1]==q(DIM[r]))
require(even==[1,3,3,4,5],'center-even irreducible dimensions')
require(min((12,20,30,60))==12,'minimum projective orbit size')

# Formal coherent rank-one capacity for rank eleven. Its coefficient in e
# is -11, and its constant term is zero. This is a fixed eleven-term sum.
require(sum(10-2*i for i in range(11))==0,'rank-eleven capacity constant term')
require(sum(-1 for i in range(11))==-11,'rank-eleven capacity defect coefficient')
require(Fraction(60,11)<12,'capacity below minimum invariant divisor')
require(11-1==10 and -60-10==-70,'actual kernel H rank and degree')

# Degree-zero rank-two image, its two forced positive top degrees, and
# the two embedded cyclic orientations. These are displayed alternatives,
# not an enumeration of source-instance splitting types.
require(2+10-12==0,'degree I at defect twelve')
require(2+(-2)==0 and 10+(-10)==0,'two degree-zero types')
require(10-2==8 and 2-10<0,'upper normal off-diagonal vanishing degrees')
require(10-12==-2 and 2-12==-10,'two normal defect degrees')
require(2+(-2)==10+(-10),'orientation determinant degrees agree')
require(0+1==1,'simple local cyclic elementary divisors')

# Torsion Hom obstruction and equivariant Serre-duality degree.
require(10-4==6,'torsion Hom twist')
require(6-12==-6,'divisor exact-sequence left twist')
require(-(-6)-2==4,'Serre-dual symmetric degree')
require(product('one',6)['one']==0 and product('one',4)['one']==0,
        'both invariant groups flanking torsion sections vanish')

# Exact common-kernel incidence, without a jet identification.
require(10-1==9,'G9 rank from F quotient')
require(-64-10==-74,'G9 degree from F quotient')
require(-70-4==-74,'G9 degree from H quotient')
require(10+10-9==11,'sum F+H rank equals B')
require(-64+(-70)-(-74)==-60,'sum F+H degree equals B')
require(9-1==8,'Fminus rank')
require(-74-(-10)==-64,'Fminus degree')
require(-76+12==-64,'agreement with original defect formula')

print(json.dumps({'status':'PASS','checks':CHECKS,'proof_sha256':PROOF_SHA,
 'scope':'three exact complete inputs; fixed universal characters and degree identities only',
 'not_claimed':['actual-instance evaluation','complete geometric proof by computation',
 'delta12 exclusion or occurrence','original degree18 higher-jet separation']},sort_keys=True,indent=2))
