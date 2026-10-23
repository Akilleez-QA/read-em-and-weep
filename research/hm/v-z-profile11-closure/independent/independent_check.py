from pathlib import Path
import json,hashlib
from functools import lru_cache
from collections import Counter
ROOT=Path(__file__).parent
exec((ROOT/'character_base.py').read_text())
product=lru_cache(None)(product)
DIM={r:int(c[0][0]) for r,c in chars.items()}
auth=[]
for m in json.loads((ROOT/'FETCH.json').read_text()):
 p=ROOT/'originals'/m['name'];raw=p.read_bytes()
 def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 if blob(raw)!=m['git_blob'] and raw.endswith(b'\n') and blob(raw[:-1])==m['git_blob']:raw=raw[:-1];p.write_bytes(raw)
 need(blob(raw)==m['git_blob']);auth.append(dict(m,sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
(ROOT/'AUTHENTICATION.json').write_text(json.dumps(auth,indent=2)+'\n')
rows=json.loads((ROOT/'originals/profile11-pairs.json').read_text());need(len(rows)==159)
def h1(B,t):
 z=Counter()
 for e,r in B:z.update(product(r,-e-t-2))
 return z
def le(a,b):return all(a[r]<=b[r] for r in chars)
def deg(B):return sum(e*DIM[r] for e,r in B)
result={}
for name,tuple_,E in [('V',[1,1,2,0,0,0,0,0],[[-2,'V'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-4,'V']]),('Z',[1,2,1,0,0,0,0,0],[[-3,'Wp'],[-3,'T'],[-3,'T'],[-4,'V']])]:
 need(sum(DIM[r] for e,r in E)==17);need(deg(E)==-54)
 need(chi(E,4)==Counter(V=3,P=3,D=2));need(h0(E,3)==Counter(Wp=1,T=2))
 compatible=[];cubic=[];quartic=[];capacity=[];records=[];rejected=[]
 for i,row in enumerate(rows):
  A,B=row['A'],row['B'];need(deg(A)==row['a']);need(deg(B)==row['b']);need(row['defect']==-6-deg(A)-deg(B))
  witnesses=[]
  for u in range(-10,11):
   for label,a,b in [('H1E-H1A',h1(E,u),h1(A,u)),('H1Edual-H0B',h1(E,-u),h0(B,u))]:
    neg={r:a[r]-b[r] for r in chars if a[r]<b[r]}
    if neg:witnesses.append(dict(twist=u,condition=label,negative=neg))
  need((not witnesses)==(tuple_ in row['compatible_E_types']))
  if witnesses:rejected.append(dict(index=i,witnesses=witnesses));continue
  compatible.append(i)
  if not le(Counter(Wp=1,T=2),h0(A,3)):cubic.append(i);continue
  envelope=h0(A,2);envelope.update(chi(A,4));envelope.subtract(chi(E,4))
  neg={r:envelope[r] for r in chars if envelope[r]<0}
  if neg:quartic.append(i);records.append(dict(index=i,kind='quartic',negative=neg));continue
  lam=sorted([e for e,r in B for _ in range(DIM[r])],reverse=True);need(len(lam)==3)
  caps=[]
  for twos in range(6):
   q=[2]*twos+[1]*(10-2*twos)
   cap=sum(sum(lam[:r])-2*(j+1)*r for j,r in enumerate(q))
   h=10-twos;need(cap==h*lam[0]-h*(h+1)+(10-h)*lam[1]-(10-h)*(11-h));caps.append(cap)
  ell=-54-deg(B);need(ell>max(caps));capacity.append(i)
  records.append(dict(index=i,kind='capacity',ordinary_B=lam,degree_L=ell,caps_h10_to5=caps,max_capacity=max(caps),gap=ell-max(caps)))
 need(len(compatible)==34);need(len(cubic)==16);need(len(quartic)==7);need(len(capacity)==11)
 need(set(cubic)|set(quartic)|set(capacity)==set(compatible));need(len(cubic+quartic+capacity)==len(set(compatible)))
 result[name]=dict(tuple=tuple_,compatible=compatible,cubic=cubic,quartic=quartic,capacity=capacity,records=records,incompatible_witnesses=rejected)
# Cross-check closed class-character formulas against independent McKay production ring, not closure output.
import importlib.util
spec=importlib.util.spec_from_file_location('prod',ROOT/'originals/characters.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
for r in chars:
 for n in range(41):need(product(r,n)==c.product(r,n))
print(json.dumps(dict(checks=checks,sources=result),indent=2))
