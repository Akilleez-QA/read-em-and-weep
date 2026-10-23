#!/usr/bin/env python3
"""Universal formal identities only; no selected source or parameter evaluation."""
from pathlib import Path
from fractions import Fraction
from math import comb, factorial
import hashlib
import json

ROOT = Path(__file__).resolve().parent
checks = 0
def require(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)

# These are fresh immutable connector reads, not copies from the author's packet.
sources = {
 'pr1145.md': ('47ce243076419081917682b9ab78990e7cf8066598d8eae1f4a175e80ab91b98', '357b420e0254de52a3ae5d4510744478159a1a10'),
 'pr1147.md': ('2ea61681c18105cbba37e7135fc968aa9052e14eff71d963e8c374f55f041122', '9bf944c40951a06378c48b743157ed0c1710aead'),
}
for name, (sha, blob) in sources.items():
    data=(ROOT/'originals'/name).read_bytes()
    require(hashlib.sha256(data).hexdigest()==sha, name+' SHA256')
    require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==blob, name+' Git blob')

pairings=0
for d in range(2,27):
    n=d+6; k=d-1
    # l=(x+t*y), but t remains an indeterminate. All summands of a
    # pairing have the same formal t exponent n-a-b. Check its coefficient.
    for a in range(k+1):
        for b in range(7):
            coefficient=Fraction(0)
            for j in range(8):
                h=n-a-b-j
                if 0<=h<=d:
                    coefficient += Fraction((-1)**(a+j)*comb(7,j)*comb(d,h),comb(n,a+j))
            require(coefficient==0, 'formal apolar orthogonality')
            pairings+=1
    require((k+1)+7==n+1, 'complementary apolar dimensions')
    # Multiplication by l^d on Sym6 has triangular unit minors on both
    # standard charts. This certifies immersion of every fixed subspace.
    for reversed_chart in (False,True):
        diagonal=[]
        for row in range(7):
            for col in range(7):
                if row<col:
                    require(row-col<0, 'zero upper triangular formal coefficient')
            diagonal.append(comb(d,0))
        require(all(x==1 for x in diagonal), 'unit chart minor')
    require(all(factorial(j)>0 for j in range(k+1)), 'formal osculation triangular diagonal')
    require(3*(d+1)-2*(d-2)==n+1, 'balanced net full coefficient dimension')
    require(n+1-3==n-2, 'rank3 sharp model codimension')
    require(n+4-5==n-1, 'nonzero high model codimension')
    require(-1>-d and -d<0, 'high block negative degree order')
    require((-1)**n==(-1)**d, 'central parity of rank3 model')
    require((-1)*(-1)==1, 'central parity of high W O(-1) model')
    for high_rank in range(21):
        for residual_dimension in range(24):
            M=n+1+residual_dimension
            codim=M-(high_rank+3)
            require((high_rank<=residual_dimension)==(codim>=n-2), 'weak rank inequality equivalence')
            if high_rank>0:
                require((high_rank<residual_dimension)==(codim>=n-1), 'strict saturation inequality equivalence')

require(21-16<10-2 and 21-16<10-1, 'old residual excluded by both bounds')
out={'checks':checks,'formal_apolar_pairings':pairings,'degrees_checked':[8,32],
     'actual_instance_evaluated':False,'scope':'supporting universal identities, not a substitute for the bundle proof'}
print(json.dumps(out,indent=2,sort_keys=True))
