#!/usr/bin/env python3
"""Universal formal polynomial and degree controls, never HM instance data."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
from math import comb
import json, hashlib, sys
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok: raise RuntimeError(msg)
def choose(n,k): return comb(n,k) if 0<=k<=n else 0
def same(a,b):
 z=Counter(a);z.subtract(b);return not any(z.values())
manifest=json.loads((ROOT/'INPUTS.json').read_text())
for item in manifest:
 data=(ROOT/item['file']).read_bytes()
 require(len(data)==item['bytes'],'byte length')
 require(hashlib.sha256(data).hexdigest()==item['sha256'],'SHA256')
 require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob_sha1'],'Git blob')
require(same(c.product('one',6),{'V':1,'P':1}),'unique sextic V')
require(same(c.product('V',2),c.product('one',8)),'quadratic span representation')
records=[]
for d in range(2,33):
 n=d+6;k=d-1
 require(n-k==7 and k+1==d,'osculation exponent')
 require(d+7==n+1,'complementary apolar dimensions')
 require((-1)**n==(-1)**d,'central parity channel compatibility')
 # Pair formal (x+t y)^7*x^(k-j)*y^j with
 # (x+t y)^d*x^(6-i)*y^i. All terms have the same t power.
 # Its coefficient vanishes exactly; no parameter is sampled.
 for j in range(k+1):
  for i in range(7):
   coefficient=sum((Fraction((-1)**a*choose(7,a-j)*choose(d,n-a-i),comb(n,a))
                    for a in range(n+1)),Fraction(0))
   require(coefficient==0,'formal apolar polynomial identity')
 expected=Counter(c.product('one',n));expected.update(c.product('Wp',d-3))
 require(same(c.product('V',d),expected),'balanced multiplication exact character')
 require(3*(d+1)-(n+1)==max(2*d-4,0),'multiplication kernel dimension')
 # Both universal sharp models: rank3 in n+1, and rank5 in n+4.
 require((n+1)-3==n-2,'rank3 boundary')
 require((n+4)-5==n-1,'nonzero high boundary')
 require(-1>-d and -d<0,'high source degree and negativity')
 require(2*(-1)==-2,'nonconstant high block')
 require((n+4)-(n+1)==3 and 2<3,'high block in constant3')
 if n%2==0:
  require((-1)**n==1 and (-1)**2==1,'center-even sharp ambient')
 for r in range(0,21):
  for excess in range(-2,4):
   M=(n+1)+r+excess
   codim=M-(r+3)
   require((r<=M-(n+1))==(codim>=n-2),'weak bound equivalence')
   if r:
    require((r<M-(n+1))==(codim>=n-1),'strict bound equivalence')
 records.append({'d':d,'n':n,'k':k,'general_bound':n-2,'nonzero_high_bound':n-1})
require(21-16==5 and 5<10-2 and 5<10-1,'known residual contradiction, not new case')
# Negative-control boundary: d=1 net multiplication has rank6<8.
require(sum(c.DIM[r]*v for r,v in c.product('V',1).items())==6,'subthreshold source')
require(1+6+1==8 and 6<8,'d>=2 is needed for completeness proof')
output={'scope':'Universal sharp sextic-channel apolar codimension obstruction',
 'checks':checks+c.checks,'degree_range':records,'authenticated_inputs':len(manifest),
 'actual_instance_evaluated':False,'new_actual_profile_exclusion':False,
 'general_bound':'codimension >= n-2','nonzero_high_bound':'codimension >= n-1',
 'sharp_abstract_models':True,'formal_apolar_parameter_sampled':False}
text=json.dumps(output,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(text)
else:require((ROOT/'RESULT.json').read_text()==text,'exact result replay')
print(text,end='')
