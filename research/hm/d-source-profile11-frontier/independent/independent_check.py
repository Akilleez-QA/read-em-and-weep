from pathlib import Path
import json,hashlib
from functools import lru_cache
from collections import Counter
ROOT=Path(__file__).parent
exec((ROOT/'character_base.py').read_text())
product=lru_cache(None)(product)
PACK=ROOT.parent
DIM={r:int(c[0][0]) for r,c in chars.items()}
auth=[]
for m in json.loads((ROOT/'FETCH.json').read_text()):
 p=ROOT/m['local']; b=p.read_bytes()
 def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 if blob(b)!=m['actual_blob'] and b.endswith(b'\n') and blob(b[:-1])==m['actual_blob']:b=b[:-1];p.write_bytes(b)
 need(blob(b)==m['actual_blob']==m['git_blob_sha1']);need(hashlib.sha256(b).hexdigest()==m['sha256']);need(len(b)==m['bytes']);need(b==(PACK/m['file']).read_bytes());auth.append({k:v for k,v in m.items() if k!='content'})
rows=json.loads((ROOT/'originals/1.txt').read_text());need(len(rows)==159)
E=[[-2,'D'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-8,'one']]
def h1(B,t):
 o=Counter()
 for e,r in B:o.update(product(r,-e-t-2))
 return o
def diff(a,b):
 o=Counter(a);o.subtract(b);return dict(sorted((r,n) for r,n in o.items() if n))
def neg(a):return {r:n for r,n in a.items() if n<0}
def shape(A):return sorted(map(tuple,A))
def deg(A):return sum(e*DIM[r] for e,r in A)
known=[([[-8,'one'],[4,'one'],[6,'one']],'shape_1135'),([[-8,'one'],[5,'W']],'shape_1135'),([[-8,'one'],[4,'one'],[8,'one']],'shape_1142'),([[-8,'one'],[4,'one'],[10,'one']],'shape_1142'),([[-8,'one'],[2,'one'],[16,'one']],'shape_1145')]
need(deg(E)==-54);need(sum(DIM[r] for e,r in E)==17);need(chi(E,4)==Counter(V=3,P=3,D=2))
summary={k:[] for k in ['incompatible_D','cubic_1140','dual_capacity','shape_1135','shape_1142','shape_1145','remaining']}; records=[]
author=json.loads((PACK/'RESULT.json').read_text())
for i,x in enumerate(rows):
 A,B=x['A'],x['B'];fail=[]
 for u in range(-10,11):
  for label,a,b in [('H1(E(u))-H1(A(u))',h1(E,u),h1(A,u)),('H1(E(-u))-H0(B(u))',h1(E,-u),h0(B,u))]:
   n=neg(diff(a,b))
   if n:fail.append(dict(condition=label,twist=u,negative_multiplicities=n))
 need((not fail)==([1,1,1,0,0,1,0,0] in x['compatible_E_types']))
 need(deg(A)==x['a'] and deg(B)==x['b']);need(x['defect']==-6-deg(A)-deg(B))
 cubic=diff(h0(A,3),Counter(Wp=1,T=2));lam=sorted([e for e,r in B for _ in range(DIM[r])],reverse=True);need(len(lam)==3)
 caps=[]
 for twos in range(6):
  q=[2]*twos+[1]*(10-2*twos)
  cap=sum(sum(lam[:rank])-2*(j+1)*rank for j,rank in enumerate(q))
  h=10-twos;need(cap==h*lam[0]-h*(h+1)+twos*lam[1]-twos*(twos+1));caps.append(cap)
 caps.reverse();ell=-54-deg(B)
 s='incompatible_D' if fail else 'cubic_1140' if neg(cubic) else 'dual_capacity' if ell>max(caps) else next((label for a,label in known if shape(a)==shape(A)),'remaining')
 summary[s].append(i)
 a=author['records'][i]
 need(a['index']==i);need(a['source_failures']==fail);need(a['cubic_character']==cubic);need(a['cubic_negative']==neg(cubic));need(a['capacities']==caps);need(a['capacity_max']==max(caps));need(a['dual_kernel_degree']==ell);need(a['partition']==s)
 records.append(dict(index=i,stage=s,cubic=cubic,capacities=caps,degree_L=ell))
need(summary==author['summary']);need([len(v) for v in summary.values()]==[57,32,62,2,2,1,3]);need(summary['remaining']==[32,50,52])
# Independent character inner products compared with production McKay recurrence.
import importlib.util
spec=importlib.util.spec_from_file_location('author_character',PACK/'characters.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
for r in chars:
 for n in range(41):need(product(r,n)==c.product(r,n))
print(json.dumps(dict(checks=checks,summary=summary,records=records,authenticated_inputs=auth),indent=2,sort_keys=True))
