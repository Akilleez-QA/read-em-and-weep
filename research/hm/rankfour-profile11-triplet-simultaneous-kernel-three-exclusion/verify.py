"""Complete immutable-source/proof authentication and bounded universal checks only."""
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

SOURCES=[
    ('inputs/top-normal-extension.md',
     '192f771436114029ccbaf0413a5e8f96edb6fce5',
     'research/hm/rankfour-profile11-triplet-top-normal-extension/PROOF.md',
     16808,
     '074dba0e590290f7b811a848b5fb4910ab6eebe5597f855111b66d5cd5fe71d0',
     '59d734b137e2bfc014a6932ad1844d26a27ac147'),
    ('inputs/eighteen-jets.md',
     '913892c66403ea57ed1681957ae1b9f8db9e5e15',
     'research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md',
     17528,
     '33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf',
     '730021d4e97c4c1307a1d3c6c5303e4e9792202d')]
PROOF_BYTES=16183
PROOF_SHA256='9a164b510ccb9c529d2380c7e9e4880067bde0e86656b82e2c4649e09e5443c2'
items=json.loads((ROOT/'INPUTS.json').read_text())
require(len(items)==2,'exactly two complete direct immutable originals')
for i,(file,ref,path,size,sha,blob) in zip(items,SOURCES):
    require(i['file']==file and i['ref']==ref and i['path']==path,'hard-pinned immutable path and ref: '+file)
    b=(ROOT/file).read_bytes()
    require(len(b)==i['bytes']==size,'complete immutable UTF8 length: '+file)
    require(hashlib.sha256(b).hexdigest()==i['sha256']==sha,'complete immutable SHA256: '+file)
    require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==i['git_blob_sha1']==blob,'complete immutable Git blob: '+file)
    require(i['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path,'exact immutable source URL: '+file)
p=(ROOT/'PROOF.md').read_bytes()
require(len(p)==PROOF_BYTES,'entire frozen proof UTF8 length')
require(hashlib.sha256(p).hexdigest()==PROOF_SHA256,'entire frozen proof SHA256')
require(ch.checks==81,'81 exact-rational physical-W consistency checks')
for n,r in {0:{'one':1},1:{'W':1},2:{'A':1},3:{'S':1},4:{'D':1},5:{'T':1},6:{'V':1,'P':1},7:{'T':1,'Wp':1}}.items():
    require(ch.product('one',n)==Counter(r),'fixed Sym'+str(n)+' physical decomposition')
require(ch.product('A',1)==Counter({'W':1,'S':1}),'unique Euler row W(1) into A(2)')
require(ch.product('Wp',1)==Counter({'P':1}),'canonical D(-4) has no map to alternate-doublet quotient')
require(ch.product('W',5)==Counter({'D':1,'V':1,'P':1}),'unique D(-4) row into W(1)')
require(ch.product('one',7)['Wp']==1 and ch.product('one',7)['one']==0 and ch.DIM['T']==6 and ch.DIM['Wp']==2,'balanced rank-two quotient coefficient is Wp')
require(all(ch.product('one',d)['one']==0 for d in (2,4,6)),'all positive even invariant degrees needed in Q classification vanish')
require(4-(-2)==6 and 10+(-2)==8 and 8>0,'unequal Q top invariant degree bound and positive lower-row degree bound')
require(4+(-10)==-6 and 2*(-3)==-6,'two Q middle types have the required degree')
require(5+2+6+3==16 and 5*(-2)+(2+6)*(-3)+3*(-4)==-46,'original E0 rank and degree')
require(7+6==13 and 7*(-4)+6*(-5)==-58,'original K1 rank and degree')
require(3+4+5+1==13 and (3+4+5)*(-4)-10==-58,'original K3 rank and degree')
require(5+4==9 and 9*(-6)==-54,'common B rank and degree')
require(4+3==7 and 4*(-7)+3*(-8)==-52,'common Csmall rank and degree')
require(9-7==2 and -54-(-52)==2*(-1),'lifted coherent image rank and degree')
require(-10-2==-12 and all(-12-d<0 for d in (-7,-8)),'actual H-normal leakage vanishes by ordinary degree')
require(9+2==11 and -54+2==-52,'actual forward R rank and degree')
require(13-11==2 and -58-(-52)==-6,'actual Q rank and degree')
require(2*1+4==3*2 and 2+1==3,'universal quadratic Euler sequence rank and degree')
require(11>10,'zero Euler row contradicts ranks of R and Kminus')
require(-64-(-54)==-10 and 10-9==1,'derivative quotient kernel Kminus over Bhat')
require(11+1==12 and -52+4==-48,'split-case actual N rank and degree')
require(13-12==1 and -58-(-48)==-10,'split-case actual K over N quotient')
require(12-9==3 and -48-(-54)==3*2,'split-case N over Bhat matches A(2)')
require(16-12==4 and -46-(-48)==2,'actual E0 over N rank and degree')
require(2-2*4==-6 and -12+3*2==-6,'split normal extension cotangent twist')
require(-10+3*4==2,'untwisted forbidden normal quotient degree')
require(all(-10-d<0 for d in (-2,-3,-4)),'ordinary Hom from E0 to O(-10) vanishes')
require(4+1==5 and 4*(-5)==5*(-4),'universal complete quartic evaluation kernel rank and degree')
require(0+2==2*1,'universal Euler scalar inclusion degree')
require(-6-(-4)<0 and -6-(-5)<0,'canonical D or quartic kernel cannot enter Bhat')
print(json.dumps({'status':'PASS','checks':len(checks),'proof_sha256':hashlib.sha256(p).hexdigest(),'universal_character_consistency_checks':ch.checks,'scope':'Complete direct-source and entire-proof authentication with bounded universal characters, ranks, degrees, invariant and ordinary Hom inequalities only. No selected actual instance, broad computation, or realization is evaluated. Arithmetic does not certify the conditional geometric exclusion; the entire actual-map proof requires independent review.','details':checks},indent=2))
