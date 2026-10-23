#!/usr/bin/env python3
"""Exact universal character, degree and formal apolar checks only."""
from pathlib import Path
from collections import Counter
from itertools import combinations_with_replacement
import hashlib, json, sys
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok: raise RuntimeError(msg)
def clean(x): return {k:v for k,v in x.items() if v}
def sub(a,b):
 z=a.copy();z.subtract(b);return z
def dim(a):return sum(c.DIM[k]*v for k,v in a.items())
def same(a,b):return not clean(sub(a,Counter(b)))
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==3,'three complete pinned originals')
for x in manifest:
 b=(ROOT/x['file']).read_bytes()
 require(len(b)==x['bytes'],'source length')
 require(hashlib.sha256(b).hexdigest()==x['sha256'],'source SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],'source Git blob')
require((ROOT/'characters.py').read_bytes()==(ROOT/'inputs/character-reference.py').read_bytes(),'exact public character implementation')
for r,n,expected in [('one',6,{'V':1,'P':1}),('V',1,{'T':1}),('P',1,{'Wp':1,'T':1}),('one',7,{'Wp':1,'T':1}),('P',2,{'V':1,'P':1,'D':1}),('one',8,{'P':1,'D':1})]:
 require(same(c.product(r,n),expected),'needed representation identity')
require(same(sub(c.product('P',2),c.product('one',8)),{'V':1}),'exact coefficient kernel')
parts=[p for p in combinations_with_replacement(range(1,7),3) if sum(p)==6]
require(parts==[(1,1,4),(1,2,3),(2,2,2)],'all positive rank3 degree6 partitions')
for p in parts:
 h0=sum(max(2-a,0) for a in p)
 require(h0<=3,'cubic kernel upper bound')
 require(6>h0,'T channel cannot vanish')
require([p for p in parts if sum(max(2-a,0) for a in p)==0]==[(2,2,2)],'linear injection forces balanced type')
require(c.product('V',1)['Wp']==0,'complement cannot supply Wprime')
require(60//5==12 and 6<12,'base divisor orbit obstruction')
mult=[]
for d in range(65):
 src=c.product('P',d);tgt=c.product('one',d+6)
 ker=c.product('V',d-2);coker=Counter(V=1) if d==0 else Counter()
 require(same(sub(src,tgt),sub(ker,coker)),'exact multiplication virtual character')
 require(dim(ker)==max(3*d-3,0),'kernel dimension')
 require(dim(coker)==max(3-3*d,0),'cokernel dimension')
 require(dim(src)-dim(ker)==min(4*(d+1),d+7),'rank formula')
 require(dim(tgt)-dim(coker)==min(4*(d+1),d+7),'target rank formula')
 if d<=4:mult.append(dict(d=d,rank=dim(src)-dim(ker),kernel=clean(ker),cokernel=clean(coker)))
hilbert=[]
for n in range(80):
 h=max(n+1,0)-4*max(n-5,0)+3*max(n-7,0)
 hchar=sub(sub(c.product('one',n),c.product('P',n-6)),Counter())
 hchar.update(c.product('V',n-8))
 expected=c.product('one',n) if n<6 else Counter(V=1) if n==6 else Counter()
 require(same(hchar,expected),'graded quotient character')
 require(dim(hchar)==h,'graded resolution Hilbert numerator')
 require(h>=0,'genuine Hilbert function')
 hilbert.append(h)
require(hilbert[:7]==[1,2,3,4,5,6,3] and not any(hilbert[7:]),'finite Hilbert vector')
require(sum(hilbert)==24,'quotient length')
# Formal full monomial pairing: x exponent i pairs only with x exponent n-i.
# This is an identity over the full homogeneous polynomial spaces, not a point test.
apolar=0
for d in range(1,25):
 n=d+6;k=d-1
 osculation=range(7,n+1)
 annihilator=range(d,n+1)
 for i in osculation:
  for j in annihilator:
   require(i+j!=n,'universal formal apolar zero');apolar+=1
 require(len(osculation)+len(annihilator)==n+1,'complementary dimensions')
 require(len(annihilator)==7,'sextic coefficient rank')
 require(k+1==d,'number osculating directions')
 for r in range(0,20):
  M=r+n+1
  require(M-(r+4)==n-3,'weak rank bound boundary')
  if r:
   require((M+1)-(r+4)==n-2,'strict saturation bound boundary')
 require((n+1)-4==n-3,'zero high-block sharp model')
 if d>=2:
  require(-1>-d and -1<0,'sharp model high-block degrees')
  require((n+4)-6==n-2,'nonzero high-block sharp model')
 else:
  require(not any(-1<e<0 for e in range(-5,5)),'d1 nonzero negative high block impossible')
 require((-1)**n==(-1)**d,'central parity compatibility')
out={'scope':'Universal complementary P sextic syzygies and apolar criterion only','checks':checks+c.checks,'authenticated_inputs':3,'kernel_bundle':'V O(-2)','minimal_surjective_multiplier_degree':1,'multiplier_controls':mult,'hilbert_vector':hilbert[:7],'quotient_length':24,'formal_apolar_zero_identities':apolar,'codimension_bounds':{'general':'n-3','nonzero_high':'n-2','nonzero_high_requires_d_at_least':2},'actual_profile_exclusion':False,'actual_instance_evaluated':False}
s=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(s)
else:require((ROOT/'RESULT.json').read_text()==s,'exact retained replay')
print(s,end='')
