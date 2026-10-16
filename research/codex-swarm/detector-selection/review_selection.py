"""Independent constant-arrow reconstruction; no producer imports or physical input."""
import hashlib,itertools,json,subprocess,sys
from pathlib import Path
P=101
HERE=Path(__file__).resolve().parent

def need(c,m):
 if not c:raise ValueError(m)
def digest(v):return hashlib.sha256(json.dumps(v,separators=(',',':'),sort_keys=True).encode()).hexdigest()
def auth(commit,path,blob):
 raw=subprocess.check_output(['git','show',commit+':'+path])
 need(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==blob,'source blob');return raw
PIN='f968b53943ba2312f09fbc3e8f9d462e86bcaa34'
auth(PIN,'research/hm/d8-small-certificates/p4/check_hm_p4_all_twists.js','7adc1d6a733636204b1dd613870c168717be6277')
old=json.loads(auth(PIN,'research/hm/d8-small-certificates/p4/certificate.json','304d031083bb2a19fb9bc012cfd338bbe0129980'))
R=[5,15,10,2]
wp=lambda i:((i+2)%5,(i+3)%5)
wm=lambda i:((i+1)%5,(i+4)%5)
def eps(t):return 0 if len(set(t))<5 else (-1)**sum(t[i]>t[j] for i in range(5) for j in range(i+1,5))
gamma=[[[eps((k,*(wp(a) if r<5 or r>=10 else wm(a)),*(wp(r) if r<5 else wm(r-5) if r<10 else wm(r-10)))) for k in range(5)] for a in range(5)] for r in range(15)]
d=[[],[],[]]
for a in range(5):
 for r in range(15):
  for k in range(5):
   if gamma[r][a][k]:d[0].append((r,a,k,gamma[r][a][k]))
for i in range(5):
 for col,h,(p,q) in [(i,0,wp(i)),(i+5,1,wm(i)),(i+10,0,wm(i)),(i+10,1,wp(i))]:
  d[1]+=[(5*h+q,col,p,1),(5*h+p,col,q,-1)]
for b in range(2):
 for k in range(5):d[2].append((b,5*b+k,k,1))
def basis(r,t):
 deg=r+t
 if deg<0:return []
 mons=sorted(m for m in itertools.product(range(deg+1),repeat=5) if sum(m)==deg)
 return [(u,u+r,a,b,*m) for u in range(4) if 0<=u+r<4 for a in range(R[u+r]) for b in range(R[u]) for m in mons]
def matrix(r,t):
 src,dst=basis(r,t),basis(r+1,t);idx={x:i for i,x in enumerate(dst)};cols=[]
 for u,v,a,b,*m in src:
  col={}
  def emit(uu,vv,aa,bb,k,z):
   mm=m[:];mm[k]+=1;i=idx[(uu,vv,aa,bb,*mm)];col[i]=col.get(i,0)+z
  if v<3:
   for rr,cc,k,z in d[v]:
    if cc==a:emit(u,v+1,rr,b,k,z)
  if u>0:
   for rr,cc,k,z in d[u-1]:
    if rr==b:emit(u-1,v,a,cc,k,z*(1 if r%2 else -1))
  cols.append(sorted((i,z) for i,z in col.items() if z))
 return {'rows':len(dst),'columns':len(src),'data':cols}
def image(M,col):
 out={}
 for j,z in col:
  for i,w in M['data'][j]:out[i]=out.get(i,0)+z*w
 return {i:z for i,z in out.items() if z}
class Span:
 def __init__(self):self.v={};self.updates=0
 def add(self,col):
  q={i:z%P for i,z in col if z%P}
  while q:
   j=max(q) # deliberately opposite pivot order from producer
   if j not in self.v:
    a=pow(q[j],P-2,P);self.v[j]={i:z*a%P for i,z in q.items()};return True
   a=q[j]
   for i,z in self.v[j].items():
    self.updates+=1;need(self.updates<=20_000_000,'review update cap')
    q[i]=(q.get(i,0)-a*z)%P
    if not q[i]:del q[i]
  return False

def unit_rank(M):
 # Independent exact integer row operations, full unit-pivot search.
 # A zero remaining matrix is a rational UPPER rank witness as well as lower.
 rows=[{} for _ in range(M['rows'])]
 for j,col in enumerate(M['data']):
  for i,z in col:rows[i][j]=z
 rank=0;updates=0;maxbits=0
 while any(rows):
  found=next(((i,j,z)for i,row in enumerate(rows)for j,z in row.items()if abs(z)==1),None)
  need(found is not None,'nonunit integer remainder: inconclusive')
  i,j,z=found;pivot={k:v*z for k,v in rows[i].items()};rows[i]={}
  for row in rows:
   factor=row.get(j,0)
   if not factor:continue
   for k,v in pivot.items():
    updates+=1;need(updates<=20_000_000,'integer update cap')
    value=row.get(k,0)-factor*v;maxbits=max(maxbits,abs(value).bit_length());need(maxbits<=256,'integer bit cap')
    if value:row[k]=value
    else:row.pop(k,None)
  rank+=1
 need(not any(rows),'nonzero integer remainder')
 return {'rank_Q':rank,'unit_pivots':rank,'remaining_nonzero_rows':0,'updates':updates,'max_bits':maxbits}

def verify(cert):
 need(cert['supertrace_orientation']=='c_(i,b)=-K_(15*b+i)','trace sign')
 I20=[(i,0)for i in range(5,11)]+[(i,1)for i in range(15)if i!=5]
 need(cert['I20']==[list(x)for x in I20],'I20 labels')
 base=basis(2,-2);E=matrix(2,-2);K={}
 for i,b in I20:
  vec={50+15*b+i:-1}
  for a in range(5):
   for k in range(5):
    if gamma[i][a][k]:vec[5*(5*b+k)+a]=-gamma[i][a][k]
  K[(i,b)]=sorted(vec.items());need(not image(E,K[(i,b)]),'integer base cycle')
 summary=[]
 for key,t,r,m in [('minus1',-1,240,10),('zero',0,848,2)]:
  B,C=matrix(1,t),matrix(2,t);b=basis(2,t);lookup={x:i for i,x in enumerate(b)};sel=cert['selected'][key]
  need(digest(B)==sel['matrix_digest'] and digest(C)==sel['outgoing_digest'],'matrix/basis binding')
  integral=unit_rank(B);need(integral['rank_Q']==r,'independent rational boundary rank')
  outgoing=unit_rank(C);need(outgoing['rank_Q']==C['rows'],'outgoing rank upper cohomology')
  need(B['rows']-outgoing['rank_Q']-r==m,'quotient dimension')
  need(all(not image(C,col) for col in B['data']),'integer square')
  space=Span()
  for col in B['data']:space.add(col)
  need(len(space.v)==r==sel['boundary_rank_mod101'],'boundary lower rank')
  labels=sel['labels'];need(len(labels)==m,'selection count')
  allowedmons=[(k,)for k in range(5)]if t==-1 else[(k,l)for k in range(5)for l in range(k,5)]
  seen=set()
  for label in labels:
   i,bidx=label['i'],label['b'];mon=tuple(label['base_monomial']);need((i,bidx)in K and mon in allowedmons,'label domain')
   need((i,bidx,mon)not in seen,'duplicate selection');seen.add((i,bidx,mon));col=[]
   for idx,z in K[(i,bidx)]:
    a=list(base[idx]);
    for k in mon:a[4+k]+=1
    col.append((lookup[tuple(a)],z))
   need(not image(C,col),'integer selected cycle');need(space.add(col),'selected dependent')
  need(len(space.v)==r+m==sel['augmented_rank_mod101'],'augmented lower rank')
  summary.append({'twist':t,'rank_B_mod101':r,'rank_aug_mod101':r+m,'integer_selected_cycles':m,'different_pivot_order':True,'updates':space.updates,'integer_unit_rank_certificate':integral,'outgoing_integer_unit_rank_certificate':outgoing,'quotient_dimension_Q':m})
 return summary
if __name__=='__main__':
 raw=(HERE/'selection.json').read_bytes();cert=json.loads(raw)
 result=verify(cert)
 print(json.dumps({'status':'independent_constant_selection_pass','selection_sha256':hashlib.sha256(raw).hexdigest(),'results':result,'rational_upper_source':'independently reconstructed exact integer unit-pivot reduction with zero remainder','physical_source_evaluated':False,'obstruction':'undecided'},indent=2,sort_keys=True))
