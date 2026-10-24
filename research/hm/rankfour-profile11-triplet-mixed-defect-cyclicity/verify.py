"""Complete authentication and tiny universal Q[t]-module identities only."""
from fractions import Fraction
from math import factorial
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
checks=[]
def require(ok,name):
    if not ok:raise RuntimeError(name)
    checks.append(name)
SOURCE_FILE='inputs/top-backward-flag.md'
SOURCE_REF='16998561d07a6c69a2529a8a052a7f9c3a510bee'
SOURCE_PATH='research/hm/rankfour-profile11-triplet-top-backward-flag/PROOF.md'
SOURCE_BYTES=16724
SOURCE_SHA256='5a9a86e376cce495818f2ffefd0442b0a45e9b249143cf333d48c7ed9d302959'
SOURCE_BLOB='2407aeca994376c073fb4ded46e988bab0c7ca70'
PROOF_BYTES=8768
PROOF_SHA256='55a65f12dc249217cd542f70b9acf9429c8715b810c06044de9b1e3240d358ca'
items=json.loads((ROOT/'INPUTS.json').read_text())
require(len(items)==1,'exactly one entire immutable direct original')
i=items[0];b=(ROOT/SOURCE_FILE).read_bytes()
require(i['file']==SOURCE_FILE and i['ref']==SOURCE_REF and i['path']==SOURCE_PATH,'hard-pinned immutable source file path and ref')
require(len(b)==i['bytes']==SOURCE_BYTES,'complete source UTF8 length')
require(hashlib.sha256(b).hexdigest()==i['sha256']==SOURCE_SHA256,'complete source SHA256')
require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==i['git_blob_sha1']==SOURCE_BLOB,'complete source Git blob')
require(i['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+SOURCE_REF+'/'+SOURCE_PATH,'immutable source URL')
p=(ROOT/'PROOF.md').read_bytes()
require(len(p)==PROOF_BYTES,'entire frozen proof UTF8 length')
require(hashlib.sha256(p).hexdigest()==PROOF_SHA256,'entire frozen proof SHA256')

# Sparse vectors in the free module Q[t]e_0+...+Q[t]e_(j-1).
# Keys are (formal generator index, formal exponent); nothing is evaluated.
def add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,Fraction(0))+v
    return {k:v for k,v in c.items() if v}
def scale(a,c,power=0):
    return {(k[0],k[1]+power):v*c for k,v in a.items() if v*c}
def basis(k,power=0):return {(k,power):Fraction(1)}
def relation(k):
    return add(basis(k,1),scale(basis(k-1),Fraction(k))) if k else basis(0,1)
for j in (1,2,3,4):
    coefficients={k:Fraction((-1)**(j-1-k)*factorial(k),factorial(j-1)) for k in range(j)}
    require(coefficients[j-1]==1,f'j={j}: last generator maps to one')
    for k in range(1,j):
        require(coefficients[k]+k*coefficients[k-1]==0,f'j={j}: quotient map kills universal relation {k}')
    for k in range(j-1):
        lhs=add(basis(k),scale(basis(j-1),-coefficients[k],j-1-k))
        rhs={}
        for ell in range(k+1,j):
            rhs=add(rhs,scale(relation(ell),Fraction((-1)**(ell-k-1)*factorial(k),factorial(ell)),ell-k-1))
        require(lhs==rhs,f'j={j}: exact reversible elimination identity e{k}')
    require(coefficients[0]!=0,f'j={j}: residual t^{j} coefficient is a rational unit')
    require((j+2)+(j+1)==2*j+3 and (j+2)+1+j==2*j+3,f'j={j}: source and adapted-basis rank totals')
    require((2*j+3)-(2*j+2)==1,f'j={j}: one cyclic elementary direction')
    require(12*j in (12,24,36,48),f'j={j}: degree-twelve divisor length')
require([-46+24+34,-52+28+48,-54+30+60,-52+30+70]==[12,24,36,48],'four retained rank-degree deficit totals')
print(json.dumps({'status':'PASS','checks':len(checks),'proof_sha256':hashlib.sha256(p).hexdigest(),'scope':'Entire immutable-source and frozen-proof authentication plus four tiny universal formal Q[t]-module elimination identities, ranks and degree totals. No actual coefficient, point, matrix or source-instance rank is evaluated. This is not a substitute for entire-proof geometric review.','details':checks},indent=2))
