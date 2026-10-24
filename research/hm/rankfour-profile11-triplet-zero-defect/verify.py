#!/usr/bin/env python3
"""Fixed universal characters and one symbolic identity, never a height scan."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib, json
from characters import product, tr, chars, q, plus, times, minus, scale
ROOT=Path(__file__).resolve().parent
checks=0
def check(got,want,label):
 global checks
 checks+=1
 if got!=want: raise RuntimeError((label,got,want))
check(dict(product('A',4)),{'A':1,'D':1,'V':1,'P':1},'untwisted gate character')
check(dict(product('A',5)),{'Wp':1,'S':1,'T':2},'twist-one gate character')
for x,a in zip(tr,chars['A']):
 x2=minus(times(x,x),q(2))
 x3=minus(times(times(x,x),x),scale(3,x))
 a2=minus(times(x2,x2),q(1))
 a3=minus(times(x3,x3),q(1))
 wedge2=scale(F(1,2),minus(times(a,a),a2))
 wedge3=scale(F(1,6),plus(minus(times(times(a,a),a),scale(3,times(a,a2))),scale(2,a3)))
 check(wedge2,a,'exterior square trace')
 check(wedge3,q(1),'determinant trace')
# Substitute h1=9-x-y, h2=x, h3=y and expand both formulas exactly.
def padd(*ps):
 out=Counter()
 for p in ps:out.update(p)
 return {m:c for m,c in out.items() if c}
def pscale(k,p):return {m:k*c for m,c in p.items() if k*c}
def pmul(p,r):
 out=Counter()
 for (a,b),c in p.items():
  for (d,e),f in r.items():out[a+d,b+e]+=c*f
 return {m:c for m,c in out.items() if c}
one={(0,0):1};x={(1,0):1};y={(0,1):1}
hs=[padd(pscale(9,one),pscale(-1,x),pscale(-1,y)),x,y]
capacity=padd(*(padd(pscale(l,h),pscale(-1,pmul(h,padd(h,one)))) for l,h in zip((6,-6,-6),hs)))
squares=padd(pscale(-30,one),*(pscale(-1,pmul(padd(h,pscale(-c,one)),padd(h,pscale(-c,one)))) for h,c in zip(hs,(7,1,1))))
check(capacity,squares,'all-height quadratic polynomial identity')
check(sum((7,1,1)),9,'unique equality center on rank plane')
check(6*7-6-6-(7*8+1*2+1*2),-30,'exact equality value')
check(-54-(-12-12),-30,'defect12 endpoint degree')
check(4-8-8,-12,'rank-three first-piece bound')
check(4+2*(-8),-12,'mixed exterior-power degree')
check(3*(-8),-24,'triplet determinant degree')
check(product('A',0).get('one',0),0,'no determinant map to A(-12)')
check(dict(product('one',-12)),{},'no determinant map to O(-24)')
check(-54-(-12),-42,'zero-defect L degree')
# Mutation: replacing the irreducible A coefficient by one scalar summand
# changes the decisive determinant Hom from zero to one.
check(product('one',0).get('one',0),1,'semantic determinant-target mutation')
inputs=[
 ('inputs/top-four.md','56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0','51d43f891d940ff1dd250747ac450db28057ac54'),
 ('inputs/low-top.md','c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af','6565110a12173fb6ff27838d294489ec1ad53941')]
for path,sha,blob in inputs:
 b=(ROOT/path).read_bytes()
 check(hashlib.sha256(b).hexdigest(),sha,path+' SHA256')
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),blob,path+' git blob')
print(json.dumps({'status':'PASS','checks':checks,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'scope':'Fixed universal character, exterior-power, symbolic-degree and pinned-input checks only; actual geometry remains conditional.'},sort_keys=True,indent=2))
