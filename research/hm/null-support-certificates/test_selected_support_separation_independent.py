"""Independent metadata-only support proof; no physical coefficients or expansion."""
import json,itertools,functools,hashlib,unittest
from pathlib import Path
from fractions import Fraction
p=str(Path(__file__).parent)+'/'
raw=open(p+'selected-full-owner-kernel-lowering.json','rb').read(); a=json.loads(raw); nodes=a['dag']
# Enumerate vertices of the metadata bounded simplex, not composition summands.
def vertices(lo,hi,total):
 ans=set()
 for free in range(len(lo)):
  other=[i for i in range(len(lo)) if i!=free]
  for bits in itertools.product((0,1),repeat=len(other)):
   v=[0]*len(lo)
   for i,b in zip(other,bits):v[i]=(lo,hi)[b][i]
   v[free]=total-sum(v)
   if lo[free]<=v[free]<=hi[free]:ans.add(tuple(v))
 assert ans
 return ans
@functools.lru_cache(None)
def bound(i,w):
 op,*args=nodes[i]
 if op=='rational':return (0,0) if args[0] else None
 if op=='coordinate':return (w[args[0]],)*2
 if op=='add':
  b=[bound(j,w) for j in args];b=[q for q in b if q is not None]
  return (min(q[0] for q in b),max(q[1] for q in b)) if b else None
 if op=='multiply':
  b=[bound(j,w) for j in args]
  return None if None in b else tuple(sum(q[k] for q in b) for k in (0,1))
 if op=='power':
  j,e=args
  if e==0:return (0,0)
  b=bound(j,w)
  if b is None:return None
  assert e>=0 or nodes[j][0]=='coordinate'
  return tuple(sorted(e*t for t in b))
 assert op=='bounded_composition_sum'
 d,body=args;N=d['dimension'];L=d['total'];T=d['threshold'];j=d['chosen']
 lo=[T if k==j else 0 for k in range(N)];hi=[T-1 if k<j else L for k in range(N)]
 for power in body['powers']:
  b=bound(power['base'],w)
  if b is None:
   # All zero bases in this artifact must be literal, and 0^0 stays one.
   assert nodes[power['base']][0]=='rational' and nodes[power['base']][1]==0
   e=power['exponent'];assert e['constant']==0 and sorted(e['coefficients'])==[0]*(N-1)+[1]
   hi[e['coefficients'].index(1)]=0
 vs=vertices(lo,hi,L);results=[]
 for v in vs:
  val=[0,0]
  for power in body['powers']:
   e=power['exponent'];ex=e['constant']+sum(x*y for x,y in zip(v,e['coefficients']));assert ex>=0
   b=bound(power['base'],w)
   if b is None:assert ex==0;continue
   for k in (0,1):val[k]+=ex*b[k]
  results.append(val)
 return min(v[0] for v in results),max(v[1] for v in results)
class IndependentSeparation(unittest.TestCase):
 def test_all_eight_complete_numerator_functionals_vanish(self):
  self.assertEqual(hashlib.sha256(raw).hexdigest(),'d07117856027c371cc3dd7c3dca21fc95fd34c32d8b84dbb6fa9693f416f506f')
  for t in a['terms']:
   w=(1,0,1,1) if t['edge']==[1,2] else (0,-1,0,1)
   for kind in ('A','B'):
    b=bound(t[kind]['root'],w);d=t['coordinate'];kappa=(-1,-2,-2,-2)
    target=sum(x*y for x,y in zip(w,kappa))+(w[d] if kind=='B' else 0)
    M=[(0,0,-2,-2)[i]+sum(5250+70+(3 if a['owners'][o][3]&(1<<i) else 1) for o in t['edge']) for i in range(4)]
    low=[int(kind=='B' and i==d) for i in range(4)]
    max_a=sum(w[i]*(M[i] if w[i]>0 else low[i]) for i in range(4))
    necessary=target-b[1]
    assert necessary>max_a

if __name__=='__main__':unittest.main()
