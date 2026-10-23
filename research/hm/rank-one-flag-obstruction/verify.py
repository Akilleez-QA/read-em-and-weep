"""Universal orbit-degree and equivariant Euler controls. No actual instance data."""
import json,hashlib
from pathlib import Path
from collections import Counter
import characters as c
root=Path(__file__).parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok: raise RuntimeError(msg)
def clean(z): return {r:z[r] for r in c.NAMES if z[r]}
def chi(B,t=0):
 out=Counter()
 for e,R in B:
  out.update(c.product(R,e+t));out.subtract(c.product(R,-e-t-2))
 return out
def dim(z):return sum(c.DIM[r]*v for r,v in z.items())
for m in json.loads((root/'INPUTS.json').read_text()):
 data=(root/m['file']).read_bytes()
 require(len(data)==m['bytes'],'input length '+m['file'])
 require(hashlib.sha256(data).hexdigest()==m['sha256'],'input hash '+m['file'])
 require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==m['git_blob_sha1'],'input blob '+m['file'])
require(hashlib.sha256((root/'inputs/FROZEN-SCALAR-ENDPOINT-LEMMA.md').read_bytes()).hexdigest()=='d76c66aac6cf179ae06a03d311edffe819834db6aa6dee1f39d59cd76ed7d2af','frozen endpoint proof')
# Character checks independently at all nine exact conjugacy traces, through the
# largest symmetric degree used here. The underlying Q(sqrt5) operations are exact.
for n in range(91):
 z=c.product('one',n)
 require(dim(z)==n+1,'symmetric dimension')
 for i,x in enumerate(c.tr):
  value=c.q(0)
  for R,v in z.items():value=c.plus(value,c.scale(v,c.chars[R][i]))
  require(value==c.sy(n,x),'exact class character')
E=[(-2,'P'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-5,'Wp')]
require(sum(c.DIM[R] for e,R in E)==17,'E rank')
require(sum(e*c.DIM[R] for e,R in E)==-54,'E degree')
require(c.product('one',14)['one']==0,'D-source Hom obstruction')
# Every invariant effective divisor is a sum of orbits of sizes12,20,30,60.
# Generate their necessary degree superset only up to the proved total78.
semigroup=sorted({12*a+20*b+30*d+60*e for a in range(7) for b in range(4) for d in range(3) for e in range(2) if 12*a+20*b+30*d+60*e<=78})
require(semigroup[0:2]==[0,12],'minimum orbit degree')
def patterns(total,j=0):
 if j==13:
  if total==0:yield ()
  return
 weight=13-j
 for delta in semigroup:
  if weight*delta<=total:
   for tail in patterns(total-weight*delta,j+1):yield (delta,)+tail
expected={3:[{'one':1,'A':2,'V':-1,'P':-1}]*3+[{'one':1,'A':1,'P':-1},{'A':1,'V':-1}],5:[{'one':2,'A':2,'P':-2},{'one':1,'A':1,'P':-1}]}
results={}
for r in (3,5):
 A=[(-r,'Wp'),(16,'one')]
 env=c.h0(A,2);env.update(chi(A,4));env.subtract({'V':3,'P':3,'D':2})
 require(env['V']==-1,'cubic-zero envelope')
 pats=sorted(patterns(84-2*r),reverse=True)
 require(len(pats)==(5 if r==3 else 2),'complete degree pattern count')
 rows=[]
 for n,ds in enumerate(pats):
  require(sum((13-j)*d for j,d in enumerate(ds))==84-2*r,'weighted defect')
  require(all(d==0 for d in ds[:7]),'first seven divisors vanish')
  bs=[14]
  for d in ds:bs.append(bs[-1]-2-d)
  require(len(bs)==14 and sum(bs)==-70+2*r,'complete flag degree and length')
  require(all(b%2==0 for b in bs),'central parity')
  residual=chi(E);residual.subtract(chi(A));residual.subtract(chi([(b,'one') for b in bs]))
  require(clean(residual)==expected[r][n],'exact residual')
  require(dim(residual)==0,'ordinary Euler equality')
  require(bool(clean(residual)),'equivariant Euler contradiction')
  # A zero equality would remain zero at every twist; all listed obstructions
  # are already certified at twist0, not by a positivity test.
  rows.append({'delta':{str(j):d for j,d in enumerate(ds) if d},'degrees':bs,'euler_residual':clean(residual)})
 q=c.product('one',10).copy();q.update(chi(A,10));q.subtract(chi(E,10))
 for i in range(7):q.update(c.product('one',24-2*i))
 require(q['one']==(0 if r==3 else -1),'F7 envelope crosscheck')
 results[str(r)]={'total_defect':84-2*r,'cubic_zero_envelope':clean(env),'F7_envelope':clean(q),'patterns':rows}
print(json.dumps({'status':'PASS','explicit_checks':checks,'character_module_checks':c.checks,'scope':'Both targets excluded, all four actual sources, k=1; no full profile closure.','results':results},indent=2,sort_keys=True))
