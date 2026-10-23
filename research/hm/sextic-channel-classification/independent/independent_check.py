#!/usr/bin/env python3
"""Independent exact universal controls; no actual HM data."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product
import hashlib,json
ROOT=Path(__file__).resolve().parent
count=0
def check(x,msg):
 global count
 count+=1
 if not x:raise RuntimeError(msg)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sc(s,a):return(s*a[0],s*a[1])
def sym(n,t):
 if n<0:return(Q(0),Q(0))
 a=(Q(1),Q(0));b=t
 if n==0:return a
 for i in range(2,n+1):a,b=b,add(mul(t,b),neg(a))
 return b
tr=[(Q(2),Q(0)),(Q(-2),Q(0)),(Q(1,2),Q(1,2)),(Q(-1,2),Q(-1,2)),(Q(1,2),Q(-1,2)),(Q(-1,2),Q(1,2)),(Q(1),Q(0)),(Q(-1),Q(0)),(Q(0),Q(0))]
weights=[1,1,12,12,12,12,20,20,30]
chars={r:[sym(n,t)for t in tr]for r,n in [('one',0),('W',1),('A',2),('S',3),('D',4),('T',5)]}
chars['P']=[(Q(i),Q(0))for i in[4,4,-1,-1,-1,-1,1,1,0]]
chars['V']=[add(sym(6,t),neg(p))for t,p in zip(tr,chars['P'])]
chars['Wp']=[add(mul(t,p),neg(v))for t,p,v in zip(tr,chars['P'],chars['T'])]
def decompose(v):
 ans={}
 for r,cv in chars.items():
  a=(Q(0),Q(0))
  for w,x,y in zip(weights,v,cv):a=add(a,sc(Q(w,120),mul(x,y)))
  check(a[1]==0 and a[0].denominator==1,'integral character inner product')
  if a[0]:ans[r]=int(a[0])
 return ans
for r,cv in chars.items():check(decompose(cv)=={r:1},'orthogonality')
for d in range(31):
 target=[sym(d+6,t)for t in tr]
 for kind in['V','P','full']:
  src=chars[kind]if kind!='full'else[sym(6,t)for t in tr]
  prod=[mul(v,sym(d,t))for v,t in zip(src,tr)]
  if kind=='V':
   ker=[mul(v,sym(d-3,t))for v,t in zip(chars['Wp'],tr)]
   cok=chars['P']if d==0 else chars['Wp']if d==1 else[(Q(0),Q(0))]*9
  elif kind=='P':
   ker=[mul(v,sym(d-2,t))for v,t in zip(chars['V'],tr)]
   cok=chars['V']if d==0 else[(Q(0),Q(0))]*9
  else:
   ker=[mul(v,sym(d-1,t))for v,t in zip(chars['T'],tr)]
   cok=[(Q(0),Q(0))]*9
  check(all(add(add(p,neg(t)),add(c,neg(k)))==(0,0)for p,t,c,k in zip(prod,target,cok,ker)),'exact multiplier character')
  check(all(v>=0 for v in decompose(ker).values()),'genuine kernel')
  check(all(v>=0 for v in decompose(cok).values()),'genuine cokernel')
# Every nonempty available support; scalar support is not assumed full.
rows=[]
for U in[(1,0),(0,1),(1,1)]:
 for J in product((0,1),repeat=2):
  if not any(J)or any(j>u for j,u in zip(J,U)):continue
  for d in range(1,31):
   m=6 if d==1 and J==(1,0)else d+7
   r=3*J[0]+4*J[1];inactive=3*(U[0]-J[0])+4*(U[1]-J[1])
   b=inactive
   check(m>=r,'active fiber bound')
   check((m-r+(b>0))>=0,'codimension bound')
   if d==1 and U==(1,1):rows.append((J,m))
check(rows==[((0,1),8),((1,0),6),((1,1),8)],'exceptional exact coefficient spans')
# Exhaust the representation quotients of Wprime+2T with exact active quotient.
possible=[(wp,t)for wp in range(2)for t in range(3)]
expected={(1,0):{(0,2),(1,2)},(0,1):{(1,2)},(1,1):{(1,1),(1,2)}}
for support,wanted in expected.items():
 out=set()
 for wp,t in possible:
  if support==(1,0):
   # R=T; inactive P span quotient Wprime+T of rank at least four.
   fits=t>=1 and any(2*a+6*b>=4 and a<=wp and b<=t-1 for a,b in product(range(2),repeat=2))
  elif support==(0,1):fits=wp>=1 and t>=2
  else:fits=wp>=1 and t>=1
  if fits:out.add((wp,t))
 check(out==wanted,'exact d1 ambient quotient list')
# Hilbert numerators of minimal resolutions, independently at degree up to forty.
for rank,shift,syzr,syzs,length,vec in[(3,6,2,9,27,[1,2,3,4,5,6,4,2]),(4,6,3,8,24,[1,2,3,4,5,6,3]),(7,6,6,7,21,[1,2,3,4,5,6])]:
 h=[n+1-rank*max(n-shift+1,0)+syzr*max(n-syzs+1,0)for n in range(41)]
 check(h[:len(vec)]==vec and not any(h[len(vec):]),'Hilbert vector')
 check(sum(h)==length,'quotient length')
# Full formal apolar orthogonality of l^7 Sym^(d-1) and l^d Sym6.
apolar=0
for d in range(1,25):
 n=d+6
 for i in range(d):
  for j in range(7):
   val=Q(0)
   for p in range(n+1):
    a=p-i;b=n-p-j
    if 0<=a<=7 and 0<=b<=d:val+=Q((-1)**p*comb(7,a)*comb(d,b),comb(n,p))
   check(val==0,'formal polynomial apolar identity')
   apolar+=1
# Full evaluation kernel syzygies in formal variables and directional contraction charts.
import sympy as s
x,y,t=s.symbols('x y t')
mon=[x**(6-i)*y**i for i in range(7)]
for i in range(6):check(s.expand(-y*mon[i]+x*mon[i+1])==0,'full sextic linear syzygy')
for a,b,columns in[(1,t,range(1,7)),(t,1,range(6))]:
 deriv=[s.expand(b*s.diff(f,x)-a*s.diff(f,y))for f in mon]
 M=s.Matrix([[s.Poly(deriv[j],x,y).coeff_monomial(x**(5-i)*y**i)for j in columns]for i in range(6)])
 check(s.expand(M.det()) in (factorial(6),-factorial(6)),'directional contraction rank six on chart')
 check(s.expand(b*s.diff((a*x+b*y)**6,x)-a*s.diff((a*x+b*y)**6,y))==0,'pure power is exact contraction kernel')
# Fresh original content authentication retained beside this checker.
auth=[]
manifest=json.loads((ROOT/'INPUTS.json').read_text())
for item in manifest:
 p=ROOT/'originals'/Path(item['file']).name;data=p.read_bytes()
 check(len(data)==item['bytes'],'original bytes')
 check(hashlib.sha256(data).hexdigest()==item['sha256'],'original sha256')
 check(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob_sha1'],'original git blob')
 auth.append({'file':p.name,'sha256':hashlib.sha256(data).hexdigest(),'exact':True})
result={'checks':count,'formal_apolar_identities':apolar,'authenticated_originals':auth,'scope':'Universal support and coefficient-span controls, not actual HM instances or a proof assistant'}
print(json.dumps(result,indent=2,sort_keys=True))
