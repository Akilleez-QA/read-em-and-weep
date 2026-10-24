#!/usr/bin/env python3
"""Bounded exact pins, fixed characters and formal differential identities only."""
from pathlib import Path
from collections import Counter
import hashlib
import json
from characters import (SIZES, IRREPS, DIMENSIONS, sym_character, tensor,
                        character_sum, inner, decompose_even)

ROOT=Path(__file__).resolve().parent
CHECKS=0

def require(condition,label):
    global CHECKS
    CHECKS+=1
    if not condition:
        raise RuntimeError(label)

PROOF_SHA='40a89cf37dffe2fc58a4d7dc78953f241efcc1d984131501376966dc91f7926b'
PROOF_BYTES=16557
PINS=[('inputs/nine-jets.md', '66a6bfe8dd424da58f3d775be1818d1f4f71eff1', 'research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md', 12744, '44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a', '916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6'), ('inputs/defect-capacity.md', 'ca235151d5d93bbead2beffa7640fbd0741aec43', 'research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md', 16069, '135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f', '175af94697c44f3140bb2c1d04978931c255b3fe'), ('inputs/deep-images.md', '95af2c0fa1e3cce92496a44ef9023708735e1ec7', 'research/hm/rankfour-profile11-triplet-deep-images/PROOF.md', 12085, '09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26', '9cf95f42505f37900f5a24c25cff07acca1b499f')]

proof=(ROOT/'PROOF.md').read_bytes()
require(len(proof)==PROOF_BYTES,'complete frozen proof length')
require(hashlib.sha256(proof).hexdigest()==PROOF_SHA,'complete frozen proof SHA256')
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==len(PINS)==3,'three complete immutable direct sources')
for rec,pin in zip(manifest,PINS):
    file,ref,path,length,sha,blob=pin
    data=(ROOT/file).read_bytes()
    require(rec['file']==file and rec['ref']==ref and rec['path']==path,
            'immutable commit and path')
    require(rec['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,
            'exact immutable source URL')
    require(rec['bytes']==len(data)==length,'complete source byte length')
    require(rec['sha256']==hashlib.sha256(data).hexdigest()==sha,'complete source SHA256')
    actual_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(rec['git_blob_sha1']==actual_blob==blob,'complete source Git blob')

# One fixed five-class character table, not a search over representations.
require(sum(SIZES)==60,'projective group order')
require(sum(d*d for d in DIMENSIONS.values())==60,'fixed irreducible dimension sum')
for name,x in IRREPS.items():
    require(x[0]==(DIMENSIONS[name],0),'fixed irreducible dimension')
    for other,y in IRREPS.items():
        require(inner(x,y)==int(name==other),'fixed table orthogonality')
require(sym_character(2)==IRREPS['A'],'physical Sym2 is A')
s8=sym_character(8);s10=sym_character(10);s12=sym_character(12)
require(decompose_even(s8)=={'P':1,'D':1},'fixed Sym8=P+D')
require(decompose_even(s10)=={'A':1,'V':1,'D':1},'fixed Sym10=A+V+D')
require(inner(s8,IRREPS['one'])==0,'Sym8 has no invariants')
require(inner(s10,IRREPS['one'])==0,'Sym10 has no invariants')
require(inner(s12,IRREPS['one'])==1,'Sym12 has exactly one invariant')
require(inner(tensor(s10,sym_character(2)),IRREPS['one'])==1,
        'one invariant in the B7 complete section source')
require(inner(tensor(IRREPS['P'],s10),IRREPS['one'])==0,
        'no invariant in the B7 section target')
require(tensor(sym_character(9),sym_character(1))==character_sum(s10,s8),
        'fixed Clebsch-Gordan character equality')
require(inner(tensor(sym_character(9),sym_character(1)),IRREPS['one'])==0,
        'no invariant in the B8 complete section source')
require(all(DIMENSIONS[r]>2 for r in decompose_even(s10)),
        'Sym10 has no nonzero subrepresentation of dimension at most two')

# Universal ranks/degrees of the two exact complete-system comparisons.
require(11-4==7 and 11*(-8)==-88,'B7 comparison rank and degree')
require(10-4==6 and 10*(-9)==-90,'B8 comparison rank and degree')
require(10-8==2 and 2<12,'saturation defect bound below invariant divisor minimum')
require((18-8,10-8)==(10,2),'diagonal quotient bidegree')
require(10+2==12 and (10+8,2+8)==(18,10),'Cartan input and biform bidegrees')
require(12+10-2*2==18,'second transvectant target degree')
require(3+3+5==11==10+1,'complete degree-ten coefficient dimension')
require(16-2*7==2 and 2-(-10)==12,'normal derivative degree twelve')
require(6*2==12,'six order-five subgroups give the twelve-point orbit')

# Formal chain-rule verification of the homogeneous second transvectant.
# A term (power,derivative,coefficient) denotes t^power times f^(derivative)
# or g^(derivative). These are formal symbols, never evaluated forms.
m,n=12,10
fxx=[(0,2,1)]
fxy=[(0,1,m-1),(1,2,-1)]
fyy=[(0,0,m*(m-1)),(1,1,-2*(m-1)),(2,2,1)]
gxx=[(0,2,1)]
gxy=[(0,1,n-1),(1,2,-1)]
gyy=[(0,0,n*(n-1)),(1,1,-2*(n-1)),(2,2,1)]
formal=Counter()
for left,right,scale in ((fxx,gyy,1),(fxy,gxy,-2),(fyy,gxx,1)):
    for power_f,df,cf in left:
        for power_g,dg,cg in right:
            formal[(power_f+power_g,df,dg)]+=scale*cf*cg
formal={key:value for key,value in formal.items() if value!=0}
require(formal=={(0,0,2):132,(0,1,1):-198,(0,2,0):90},
        'formal ODE coefficients and cancellation of coordinate powers')
require(m*(m-1)==132!=0,'nonzero formal leading differential coefficient')
require(2*(m-1)*(n-1)==198 and n*(n-1)==90,'remaining formal coefficients')

# The fixed complete Veronese flag only; not actual-instance jet evaluation.
for j in range(11):
    require((j+1)+(10-j)==11,'universal complete jet and kernel ranks')
    require((j+1)*(j-10)==-(j+1)*(10-j),'universal complete jet degree')
require(11*(10-10)==0,'last complete jet bundle is constant')

print(json.dumps({
    'status':'PASS','checks':CHECKS,'proof_sha256':PROOF_SHA,
    'scope':'three complete source pins; fixed small characters; universal degree bookkeeping; formal second-transvectant ODE identity',
    'not_claimed':['evaluation of any actual coefficient, point, jet, tensor or matrix',
                   'geometric proof by computation','resolution of delta or e9',
                   'original tenth-jet separation','branch realization or exclusion']
},sort_keys=True,indent=2))
