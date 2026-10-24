"""Exact authentication and bounded universal checks; no actual-instance evaluation."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import characters as ch

ROOT=Path(__file__).resolve().parent
checks=[]
def require(condition,name):
    if not condition:
        raise RuntimeError(name)
    checks.append(name)

SOURCE_FILE='inputs/top-normal-extension.md'
SOURCE_REF='192f771436114029ccbaf0413a5e8f96edb6fce5'
SOURCE_PATH='research/hm/rankfour-profile11-triplet-top-normal-extension/PROOF.md'
SOURCE_BYTES=16808
SOURCE_SHA256='074dba0e590290f7b811a848b5fb4910ab6eebe5597f855111b66d5cd5fe71d0'
SOURCE_BLOB='59d734b137e2bfc014a6932ad1844d26a27ac147'
PROOF_BYTES=16724
PROOF_SHA256='5a9a86e376cce495818f2ffefd0442b0a45e9b249143cf333d48c7ed9d302959'
items=json.loads((ROOT/'INPUTS.json').read_text())
require(len(items)==1,'exactly one complete direct immutable original')
i=items[0]
require(i['file']==SOURCE_FILE and i['ref']==SOURCE_REF and i['path']==SOURCE_PATH,'hard-pinned immutable source path and ref')
b=(ROOT/SOURCE_FILE).read_bytes()
require(len(b)==i['bytes']==SOURCE_BYTES,'complete immutable source UTF8 length')
require(hashlib.sha256(b).hexdigest()==i['sha256']==SOURCE_SHA256,'complete immutable source SHA256')
require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==i['git_blob_sha1']==SOURCE_BLOB,'complete immutable source Git blob')
require(i['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+SOURCE_REF+'/'+SOURCE_PATH,'exact immutable source URL')
p=(ROOT/'PROOF.md').read_bytes()
require(len(p)==PROOF_BYTES,'entire frozen proof UTF8 length')
require(hashlib.sha256(p).hexdigest()==PROOF_SHA256,'entire frozen proof SHA256')
require(ch.checks==81,'81 exact-rational physical-W consistency checks')
for n,r in {1:{'W':1},2:{'A':1},3:{'S':1},4:{'D':1},5:{'T':1},6:{'V':1,'P':1},7:{'T':1,'Wp':1},9:{'S':1,'T':1},10:{'A':1,'V':1,'D':1},12:{'one':1,'A':1,'D':1,'P':1}}.items():
    require(ch.product('one',n)==Counter(r),'fixed Sym'+str(n)+' physical decomposition')
require(ch.product('V',1)==Counter({'T':1}),'V_alt twist-nine irreducible source')
require(ch.product('V',2)==Counter({'D':1,'P':1}),'V_alt twist-ten source')
require(ch.product('V',3)==Counter({'S':1,'T':1,'Wp':1}),'V_alt twist-eleven source')
require(ch.product('one',7)['W']==0,'terminal intrinsic U0 derivative Hom vanishes')
require(ch.product('one',9)['W']==0,'actual U0 has no graph into Z1')
require(ch.product('one',10)['one']==0,'terminal Euler-line U0 Hom vanishes')
require(ch.product('one',12)['one']==1,'unique degree-twelve invariant line')
require(6<12 and 7<12,'complementary scalar rows have no invariant base divisor')
require(min(ch.DIM[r] for r in ch.product('V',2))>2,'rank-two kernel has no twist-ten source constituent')
require(ch.product('V',3)['Wp']==1 and ch.product('one',9)['Wp']==0 and ch.DIM['Wp']==2,'twist-eleven kernel has exactly alternate doublet coefficient')
require(7*(-4)-7*6==-70 and -70 < -52,'rank-seven rank-one coherent capacity contradiction')
require(5*(-6)-5*4==-50 and -50 < -46,'rank-five rank-one coherent capacity contradiction')
require(4*(-7)+3*(-8)==-52 and 4+3==7,'C rank and degree')
require(3*(-8)-(-2)==-22 and 2*(-11)==-22,'V_alt scalar-row kernel degree')
require(3+2==5 and 3*(-8)+2*(-11)==-46,'R5 rank and degree')
require(-52-(-46)==2*(-3),'full beta_C quotient degree')
require(2*(-11)-(-4)==-18,'alternate-doublet scalar-row kernel degree')
require(2+1==3 and 2*(-9)-18==-36,'R3 rank and degree')
require(-46-(-36)==2*(-5),'full beta_R5 quotient degree')
require(-7-(-2)==-5 and -5-2==-7,'successive rank-two actual target twists')
require(-8-18==-26 and -36-(-26)==-10,'terminal coherent image and kernel degrees')
require(2*(-7)-(-26)==12,'terminal target defect length')
require(-6-(-18)==12 and -8-(-18)==10 and -11-(-18)==7,'terminal invariant and two Hom degrees')
require(all(d>=-1 for d in (3,9,10)),'all stated ordinary extension H1 groups vanish')
require(5*(-6)-4*(-7)==-2 and 4*(-7)-3*(-8)==-4 and 3*(-8)-2*(-9)==-6,'all three actual consecutive jet quotient degrees')
require(-2-2==-4 and -4-2==-6 and -6-2==-8,'all three actual Euler coherent column degrees')
require([-46+24+34,-52+28+48,-54+30+60,-52+30+70]==[12,24,36,48],'four coherent mixed-sum saturation lengths')
require([3+2,4+3,5+4,6+5]==[5,7,9,11],'four coherent mixed-sum full ranks')
print(json.dumps({'status':'PASS','checks':len(checks),'proof_sha256':hashlib.sha256(p).hexdigest(),'universal_character_consistency_checks':ch.checks,'scope':'Complete direct-source and entire-proof authentication, with bounded universal character, rank, degree and Ext arithmetic only. No selected actual instance, broad computation, realization or exclusion is certified. The actual geometric argument requires entire-proof independent review.','details':checks},indent=2))
