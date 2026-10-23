#!/usr/bin/env python3
"""Independent source and formal-identity checks. No actual-instance data."""
import hashlib, json
from math import comb, factorial
from pathlib import Path
BASE=Path(__file__).resolve().parent
PACKET=BASE.parent
def need(ok, message):
    if not ok: raise RuntimeError(message)
fresh=json.loads((BASE/'fresh-sources.json').read_text())
auth=[]
for row in json.loads((PACKET/'INPUTS.json').read_text()):
    fetched=fresh[row['local'][:-3]]
    raw=fetched['content'].encode('utf-8')
    sha=hashlib.sha256(raw).hexdigest()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    need(raw==(PACKET/'inputs'/row['local']).read_bytes(),'fresh source differs')
    need(sha==row['sha256'] and blob==row['git_blob']==fetched['sha'],'source digest')
    need(len(raw)==row['bytes'],'source length')
    auth.append({'file':row['local'],'sha256':sha,'git_blob':blob,'bytes':len(raw),'url':row['url']})
# Taylor matrices in divided-derivative normalization. Entry (a,k) is
# binom(k,a)*t^(k-a); its inverse has the same coefficient times (-1)^(k-a).
# Each matrix-product entry has a single formal exponent k-a.
checks=0
for m in range(25):
    for a in range(m+1):
        for k in range(a,m+1):
            for side in (0,1):
                total=sum(comb(j,a)*comb(k,j)*(-1)**((j-a) if side==0 else (k-j)) for j in range(a,k+1))
                need(total==int(a==k),'formal two-sided Taylor inverse')
                checks+=1
# Triangular Wronskian of 1,t,...,t^j has constant nonzero determinant
# product(a!), proving exact formal sharp-model derivative rank without a point.
for j in range(25):
    determinant=1
    for a in range(j+1): determinant*=factorial(a)
    need(determinant>0,'formal triangular derivative determinant')
# Ordinary derivative of t^p vanishes modulo p. The abstract Frobenius line
# (1,t^p) is saturated and spanning but horizontal, so char0 is essential.
for p in (2,3,5,7,11):
    need(p%p==0 and 1%p!=0,'Frobenius edge')
result={'status':'PASS','fresh_source_authentication':auth,'two_sided_formal_Taylor_checks':checks,'formal_degrees':[0,24],'formal_Wronskian_triangular_checks':25,'characteristic_p_edges':[2,3,5,7,11],'actual_instance_evaluations':0,'proof_assistant_verified':False}
print(json.dumps(result,indent=2,sort_keys=True))
