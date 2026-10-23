#!/usr/bin/env python3
"""Fixed constituent bookkeeping only, not an actual multiplication evaluation."""
from pathlib import Path
import hashlib,json

def require(v,msg):
 if not v:raise RuntimeError(msg)
names=('A','V','P','D');dims=(3,3,4,5)
XF=(0,1,1,2);XB=(1,1,2,2)
YF=(0,0,1,1);YB=(0,1,2,2);YL=(0,1,1,0)
actual_kernel=(1,0,0,1);actual_image=(0,2,3,3);actual_coker=(0,0,1,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cap(a,b):return tuple(min(x,y) for x,y in zip(a,b))
def dim(a):return sum(x*y for x,y in zip(a,dims))
source=add(XF,XB);target=add(add(YF,YB),YL)
require(sub(source,actual_kernel)==actual_image,'imported kernel-image consistency')
require(sub(target,actual_image)==actual_coker,'imported image-cokernel consistency')
# TypeB: the graph of any equivariant shear has the same genuine character YL.
maxB_F=cap(XF,YF);maxB_B=cap(XB,add(YB,YL));maxB=add(maxB_F,maxB_B)
require(maxB[1]==1 and actual_image[1]==2,'V bottleneck')
require(dim(maxB)==30 and dim(actual_image)==33,'dimension cross-check')
# TypeF reaches both maximal block characters, since their sum is the full image.
maxF_F=cap(XF,add(YF,YL));maxF_B=cap(XB,YB)
require(add(maxF_F,maxF_B)==actual_image,'simultaneous saturation of bounds')
require(sub(XF,maxF_F)==(0,0,0,1),'F kernel D')
require(sub(XB,maxF_B)==(1,0,0,0),'B kernel A')
require(sub(add(YF,YL),maxF_F)==(0,0,1,0),'F cokernel P')
require(sub(YB,maxF_B)==(0,0,0,0),'B surjectivity')
require((dim(maxF_F),dim(maxF_B))==(12,21),'block dimensions')
require(YF[1]==0 and YL[1]==XF[1]==1,'F quotient V is forced')
root=Path(__file__).parent;man=root/'audit-inputs'/'manifest.json'
if man.exists():
 for e in json.loads(man.read_text()):
  b=(root/'audit-inputs'/e['name']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob'],'original blob '+e['name'])
 print('PASS: two original immutable inputs authenticate exactly.')
print('PASS: TypeB maximum has one V; actual invariant image has two V.')
print('PASS: TypeF images12/21, kernelsD/A, cokernelsP/0.')
print('BOUNDARY: no actual map or rank evaluated; theorem requires written equivariant/intertwining proof.')
