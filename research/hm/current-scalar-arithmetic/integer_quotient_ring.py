#!/usr/bin/env python3
"""Import-safe exact signed-integer arithmetic in Z[v,w,z]/(v6,w37,z22)."""
V,W,Z=6,37,22
RV,RW,QZ=11,73,803
LEGAL=tuple(r+RV*w+QZ*z for z in range(Z)for w in range(W)for r in range(V))
OP={'mul':0,'sparse':0,'packed':0,'monomial':0,'maxNonzeros':0,'maxCoefficientBits':0,'maxPackedDigitBits':0,'nonnegativePackedProducts':0}
def valid(q):return isinstance(q,int)and q>=0 and q%RV<V and(q//RV)%RW<W and q//QZ<Z
class Poly:
 __slots__=('p',)
 def __init__(self,p):
  assert all(valid(q)and isinstance(c,int)and c for q,c in p.items())
  self.p=p
  OP['maxNonzeros']=max(OP['maxNonzeros'],len(p))
  OP['maxCoefficientBits']=max(OP['maxCoefficientBits'],max((abs(c).bit_length()for c in p.values()),default=0))
ZERO=Poly({});ONE=Poly({0:1})
def make(p):return ZERO if not p else ONE if p=={0:1}else Poly(p)
def split_pack(A,width):
 n=max(A.p)+1;plus=bytearray(width*n);minus=bytearray(width*n)
 for q,c in A.p.items():
  target=plus if c>0 else minus
  target[width*q:width*(q+1)]=abs(c).to_bytes(width,'little')
 return int.from_bytes(plus,'little'),int.from_bytes(minus,'little')
def packed_mul(A,B):
 if not A.p or not B.p:return ZERO
 bound=min(len(A.p),len(B.p))*max(abs(c)for c in A.p.values())*max(abs(c)for c in B.p.values())
 width=(bound.bit_length()+7)//8;assert width>0 and (1<<(8*width))>bound
 assert width<=512,'Dynamic exact packed digit guard exceeded4096bits'
 OP['maxPackedDigitBits']=max(OP['maxPackedDigitBits'],8*width)
 ap,an=split_pack(A,width);bp,bn=split_pack(B,width)
 def prod(a,b):
  if not a or not b:return 0
  OP['nonnegativePackedProducts']+=1;return a*b
 plus=prod(ap,bp)+prod(an,bn);minus=prod(ap,bn)+prod(an,bp)
 n=max(A.p)+max(B.p)+1
 pos=plus.to_bytes(width*n,'little');neg=minus.to_bytes(width*n,'little');C={}
 for q in LEGAL:
  if q>=n:break
  k=width*q;c=int.from_bytes(pos[k:k+width],'little')-int.from_bytes(neg[k:k+width],'little')
  if c:C[q]=c
 return make(C)
def sparse_mul(A,B):
 C={}
 for q,a in A.p.items():
  for t,b in B.p.items():
   k=q+t
   if valid(k):C[k]=C.get(k,0)+a*b
 return make({q:c for q,c in C.items()if c})
def mul(A,B):
 OP['mul']+=1
 if not A.p or not B.p:return ZERO
 if A is ONE:return B
 if B is ONE:return A
 if len(A.p)==1 or len(B.p)==1:
  OP['monomial']+=1
  if len(A.p)>1:A,B=B,A
  q,c=next(iter(A.p.items()));return make({q+t:c*b for t,b in B.p.items()if valid(q+t)})
 if len(A.p)*len(B.p)<=4096:OP['sparse']+=1;return sparse_mul(A,B)
 OP['packed']+=1;return packed_mul(A,B)
def power(A,e):
 assert isinstance(e,int)and e>=0
 B=ONE
 while e:
  if e%2:B=mul(B,A)
  e//=2
  if e:A=mul(A,A)
 return B
def add_shift(C,A,c,du,dt):
 assert isinstance(c,int)and du>=0 and dt>=0
 if not c or du>=V or dt>=W:return
 for q,a in A.p.items():
  r=q%RV;w=(q//RV)%RW
  if r+du<V and w+dt<W:
   k=q+du+RV*dt;value=C.get(k,0)+c*a
   if value:C[k]=value
   else:C.pop(k,None)
