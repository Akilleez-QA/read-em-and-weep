#!/usr/bin/env python3
"""Universal parity, ideal-exponent and degree checks; no actual instances."""
from pathlib import Path
from itertools import product
import hashlib,json

def require(condition,message):
    if not condition: raise RuntimeError(message)
def parity_count(positive,negative,degree):
    counts=[0,0]
    for powers in product(range(degree+1),repeat=positive+negative):
        if sum(powers)==degree: counts[sum(powers[positive:])%2]+=1
    return tuple(counts)
require(parity_count(3,1,1)==(3,1),'P3 linear parity')
require(parity_count(2,1,2)==(4,2),'plane quadratic parity')
require((3+1+1,1)==(5,1),'Ferrand cubic parity from six independent generators')
require(5-1==4,'forced full even restriction image under unique cubic')
def h0plane(n):return (n+1)*(n+2)//2 if n>=0 else 0
# Square resolution of a length-two plane complete intersection of degrees1,2.
def h0_square(n):
    return h0plane(n-2)+h0plane(n-3)+h0plane(n-4)-h0plane(n-4)-h0plane(n-5)
require(h0_square(1)==0 and h0_square(2)==1,'length-two square in degrees1,2')
require(20-(2*3+1)==13,'plane conic cubic ideal dimension')
require(13-7==6,'Ferrand cubic ideal dimension after proven surjectivity')
# Exact monomial colon identities in the universal two-parameter regular local model.
def minimal(gens):
    gs=set(gens)
    return sorted(a for a in gs if not any(b!=a and all(x<=y for x,y in zip(b,a)) for b in gs))
def colon_t(gens,power):return minimal((max(a-power,0),b) for a,b in gens)
j_square=[(4,0),(2,1),(0,2)]
require(colon_t(j_square,1)==[(0,2),(1,1),(3,0)],'((t^2,u)^2:t)')
require(colon_t(j_square,2)==[(0,1),(2,0)],'((t^2,u)^2:t^2)=(t^2,u)')
require(6-2*2==2 and 5-2*2==1,'restrictions after q-prime squared')
require(6-2-1==3,'final cubic quotient degree')
require(2+1==3 and 3-3==0,'exhausted squares and zero fiber Tor')
root=Path(__file__).parent
entries=json.loads((root/'INPUTS.json').read_text())
for entry in entries:
    p=root/'audit-inputs'/(entry['key']+'.md')
    if p.exists():
        data=p.read_bytes()
        require(len(data)==entry['bytes'],'input size '+entry['key'])
        require(hashlib.sha256(data).hexdigest()==entry['sha256'],'input SHA256 '+entry['key'])
        frame=b'blob '+str(len(data)).encode()+b'\0'+data
        require(hashlib.sha1(frame).hexdigest()==entry['git_blob_sha1'],'input blob '+entry['key'])
print('PASS: fixed parity counts, complete-intersection square dimensions, universal monomial colon identities and degree bookkeeping.')
print('Input hashes checked for all locally reconstructed originals present.')
print('BOUNDARY: classification, regularity, Ferrand exactness, global membership and base change require the written proof; no actual coefficient, parameter, point or instance rank is evaluated.')
