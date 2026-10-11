"""Exact first-jet reconstruction and quadratic certificate over the rationals.

Coefficient maps are supplied data. Laurent tensors use sparse dictionaries
(symmetric slot, z/X/Y/W exponents). Run with Python assertions enabled.
"""
if not __debug__:
    raise RuntimeError('Run without -O: exact checks use assertions.')

from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
import hashlib, json
import sympy as s

ROOT=Path(__file__).resolve().parent
R=ROOT/'data'
OUT=ROOT/'build'
OUT.mkdir(exist_ok=True)
F=json.loads((R/'order_1.json').read_text())
SND=json.loads((R/'order_2.json').read_text())
REPORT={}
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():
   out[k]=out.get(k,Q(0))+v
   if not out[k]: del out[k]
 return out
def scale(p,v):return {k:a*v for k,a in p.items() if a*v}
def pmul(p,q):
 out={}
 for e,a in p.items():
  for f,b in q.items():
   g=tuple(i+j for i,j in zip(e,f));out[g]=out.get(g,Q(0))+a*b
   if not out[g]:del out[g]
 return out
def mon(e,c=1):return {tuple(e):Q(c)}
def pshift(p,e,c=1):return pmul(p,mon(e,c))
def ppow(p,n):
 q=mon((0,0,0,0))
 for _ in range(n):q=pmul(q,p)
 return q
one=mon((0,0,0,0)); z=mon((1,0,0,0)); X=mon((0,1,0,0));Y=mon((0,0,1,0));W=mon((0,0,0,1))
S=add(ppow(X,2),ppow(Y,2)); xy=pmul(X,Y); aa=add(ppow(X,3),ppow(Y,3)); sig=ppow(W,6)
g=add(S,scale(pmul(z,ppow(W,2)),-1));gi=pshift(g,(-1,0,0,0))
C=add(ppow(S,2),pmul(pmul(z,S),ppow(W,2)),pmul(ppow(z,2),ppow(W,4)))
r=[scale(aa,-1),sig,scale(g,-1),xy];ri=[scale(aa,-1),ppow(S,3),scale(gi,-1),xy]
def vmul(v,p,target=None):
 out={}
 for (ch,e),a in v.items():
  for f,b in p.items():
   k=(ch if target is None else target,tuple(i+j for i,j in zip(e,f)))
   out[k]=out.get(k,Q(0))+a*b
   if not out[k]:del out[k]
 return out
def vshift(v,e,c=1):return vmul(v,mon(e,c))
def slot(v,ch):return {k:a for k,a in v.items() if k[0]==ch}
def project(v):return {k:a for k,a in v.items() if all(t<0 for t in k[1][1:])}
TB={(0,0):ppow(z,3),(1,1):one,(1,2):pmul(z,C),(2,2):ppow(z,4),(3,3):ppow(z,3)}
def trans(v,kind):
 out={}
 for (ch,e),a in v.items():
  if kind=='U':
   for (i,j),p in TB.items():
    if ch==j:out=add(out,vmul({(i,e):a},pshift(p,(-1,0,0,0))))
  else:
   for (i,j),p in TB.items():
    if ch[0]!=j:continue
    for (l,k),q in TB.items():
     if ch[1]==k:out=add(out,vmul({(tuple(sorted((i,l))),e):a},pshift(pmul(p,q),(-4,0,0,0))))
 return out
def invU(v):
 out={}
 for ch,d in [(0,2),(2,3),(3,2)]:out=add(out,vshift(slot(v,ch),(-d,0,0,0)))
 out=add(out,vshift(slot(v,1),(1,0,0,0)),scale(vmul(slot(v,2),pshift(C,(-2,0,0,0)),1),-1))
 return project(out)
def rel(v,rr):
 out={}
 for i in range(4):
  for j,p in enumerate(rr):out=add(out,vmul(slot(v,i),p,tuple(sorted((i,j)))))
 return out
def ca(*cs):
 out={}
 for c in cs:
  for k,v in c.items():out[k]=add(out.get(k,{}),v)
 return {k:v for k,v in out.items() if v}
def cm(c,fn):return {k:q for k,v in c.items() if (q:=fn(v))}
def delta(c,degree):
 out={}
 for ij in combinations(range(3),degree+2):
  q=add(*(scale(c.get(ij[:i]+ij[i+1:],{}),(-1)**i) for i in range(len(ij))))
  if q:out[ij]=q
 return out
def K(c):
 out={}
 for ij,v in c.items():
  for (ch,e),a in v.items():
   piv=next((i for i in range(3) if e[i+1]>=0),None)
   if piv is not None and piv in ij:
    k=tuple(i for i in ij if i!=piv)
    out[k]=add(out.get(k,{}),{(ch,e):a*((-1)**ij.index(piv))})
 return {k:v for k,v in out.items() if v}
TOP=(0,1,2)
def lift(x):
 xi=invU(x)
 assert project(trans(xi,'U'))==x
 xh=K({TOP:add(trans(xi,'U'),scale(x,-1))})
 assert delta(xh,1)=={TOP:add(trans(xi,'U'),scale(x,-1))}
 e0=K({TOP:rel(x,r)});ei=K({TOP:rel(xi,ri)})
 assert delta(e0,1)=={TOP:rel(x,r)}
 assert delta(ei,1)=={TOP:rel(xi,ri)}
 mix=ca(cm(ei,lambda v:trans(v,'W')),cm(e0,lambda v:scale(v,-1)),cm(xh,lambda v:scale(rel(v,r),-1)))
 eh=K(mix);assert delta(eh,0)==mix
 return e0,ei,eh
def bracket(p,q,chart):
 omega={(1,2):xy,(1,3):g if chart==0 else gi,(2,3):sig if chart==0 else ppow(S,3)}
 out={}
 for ((i,j),e),a in p.items():
  for ((k,l),f),b in q.items():
   ee=tuple(x+y for x,y in zip(e,f))
   for out1,out2,arg1,arg2 in [(i,l,j,k),(j,l,i,k),(i,k,j,l),(j,k,i,l)]:
    if arg1==arg2:continue
    form=omega.get(tuple(sorted((arg1,arg2))),{})
    out=add(out,vmul({(tuple(sorted((out1,out2))),ee):a*b*(1 if arg1<arg2 else -1)},form))
 return out
def divide(v):
 u=vmul(slot(v,(1,1)),mon((0,0,0,-6)),1)
 for j in (0,2,3):
  a=add(slot(v,tuple(sorted((1,j)))),scale(vmul(slot(u,1),r[j],tuple(sorted((1,j)))),-1))
  u=add(u,vmul(a,mon((0,0,0,-6)),j))
 assert rel(u,r)==v
 return u
def split(v):
 f={};inf={}
 for ch,d in [(0,2),(2,3),(3,2)]:
  for (c,e),a in slot(v,ch).items():
   if e[0]>=0:f[(ch,e)]=-a
   else:inf[(ch,(e[0]-d,*e[1:]))]=a
 residual=add(v,scale(project(trans(inf,'U')),-1))
 for (ch,e),a in slot(residual,1).items():
  if e[0]>=0:f[(1,e)]=-a
  else:inf[(1,(e[0]+1,*e[1:]))]=a
 assert project(add(trans(inf,'U'),scale(f,-1)))==v
 return f,inf
def obstruction(et):
 e0,ei,eh=et
 q0=scale(bracket(e0.get((0,1),{}),e0.get((1,2),{}),0),Q(1,2))
 qi=scale(bracket(ei.get((0,1),{}),ei.get((1,2),{}),1),Q(1,2))
 qh={}
 for i,j in combinations(range(3),2):
  q=scale(add(bracket(eh.get((i,),{}),trans(ei.get((i,j),{}),'W'),0),scale(bracket(e0.get((i,j),{}),eh.get((j,),{}),0),-1)),Q(1,2))
  if q:qh[(i,j)]=q
 defect=add(trans(qi,'W'),scale(q0,-1),scale(delta(qh,1).get(TOP,{}),-1));u=divide(defect)
 v0,vi=split(project(u));vh=K({TOP:add(trans(vi,'U'),scale(v0,-1),scale(u,-1))})
 assert add(trans(vi,'U'),scale(v0,-1),scale(delta(vh,1).get(TOP,{}),-1))==u
 c0=add(q0,scale(rel(v0,r),-1));ci=add(qi,scale(rel(vi,ri),-1))
 ch=ca(qh,cm(vh,lambda v:scale(rel(v,r),-1)))
 assert add(trans(ci,'W'),scale(c0,-1),scale(delta(ch,1).get(TOP,{}),-1))=={}
 obs=project(c0);assert project(trans(project(ci),'W'))==obs
 return obs
def matrix(d,prefix):
 shape=d[prefix+'_shape'];out=s.zeros(*shape)
 for i,j,v in d[prefix+'_sparse']:out[i,j]=s.Rational(v)
 return out
dweights=[3,0,2,2]
kernel1=None
for k,data,dp,sb,tb in [(1,F,'D','source_basis','target_basis'),(2,SND,'D2','D2_source_basis','D2_target_basis')]:
 basis=data[sb]; cols=[j for j,(ch,e,p) in enumerate(basis) if 2*e-p[0]-p[1]-2==k-4+dweights[ch]]
 D=matrix(data,dp);B=D[:,cols];ns=B.nullspace();H=s.Matrix.hstack(*ns) if ns else s.zeros(len(cols),0)
 item={'selected_source_indices':cols,'source_dimension':len(cols),'D_rank':B.rank(),'kernel_dimension':H.cols}
 if k==1:
  E=matrix(F,'Ev');EK=E[:,cols]*H;nk=EK.nullspace();kernel1=H*s.Matrix.hstack(*nk)
  item['evaluation_rank']=EK.rank();item['fixed_beta_kernel_dimension']=kernel1.cols
  item['fixed_beta_kernel_vectors']=[[[cols[i],str(v)] for i,v in enumerate(kernel1[:,j]) if v] for j in range(kernel1.cols)]
  source1=cols
 else:
  target=data[tb];rows=[i for i,(ch,e,p) in enumerate(target) if 2*e+p[0]+p[1]==k-4+dweights[ch[0]]+dweights[ch[1]]]
  assert all(not D[i,j] for i in range(D.rows) if i not in rows for j in cols)
  DH=D[rows,cols];ls=DH.T.nullspace();assert len(ls)==1
  detector=ls[0];item['target_dimension']=len(rows);item['obstruction_dimension']=1
  item['obstruction_detector']=[[rows[i],str(v)] for i,v in enumerate(detector) if v]
  target2={((ch[0],ch[1]),(e,*p)):i for i,(ch,e,p) in enumerate(target)}
  D2rows=rows
 REPORT[str(k)]=item
def src1(coeffs):
 out={}
 for j,a in coeffs:
  ch,e,p=F['source_basis'][j];v={(ch,(e,*[-v-1 for v in p])):Q(a)}
  if ch==2:
   extra=project(vmul(v,pshift(C,(-3,0,0,0)),1))
   v=add(v,{k:a for k,a in extra.items() if k[1][0]>=0})
  out=add(out,v)
 return out
origin=lift(src1([(j,v) for j,_,v in F['preimage_x_sparse']]))
vY=REPORT['1']['fixed_beta_kernel_vectors'][0];vX=REPORT['1']['fixed_beta_kernel_vectors'][1]
dirs=[lift(src1(vX)),lift(src1(vY))]
for e in [(-2,1,0,0),(-2,0,1,0)]:dirs.append(({}, {}, {(i,):{((1,1),e):Q(1)} for i in range(3)}))
def evaluate(pt):
 et=tuple(ca(origin[k],*(cm(dirs[j][k],lambda v:scale(v,pt[j])) for j in range(4))) for k in range(3))
 obs=obstruction(et)
 # Reconstructing forced coordinates is necessary before extracting independent slots.
 red=dict(obs)
 for src,tgt,mulc,threshold in [((0,2),(0,1),1,0),((2,2),(1,2),2,1),((2,3),(1,3),1,0)]:
  forced=project(vmul(slot(obs,src),pshift(C,(-3,0,0,0),mulc),tgt))
  red=add(red,scale({k:a for k,a in forced.items() if k[1][0]>=threshold},-1))
 assert all(k in target2 for k in red)
 vec=s.zeros(len(SND['D2_target_basis']),1)
 for k,a in red.items():vec[target2[k]]=a
 assert all(not vec[i] for i in range(vec.rows) if i not in D2rows)
 value=(detector.T*vec[D2rows,:])[0]
 return value, vec[D2rows,:]
evaluations={}
def scalar(pt):
 value,vector=evaluate(pt)
 evaluations[tuple(pt)]=vector
 return value
origin_value=scalar([0]*4);assert origin_value==0
linear=[];diagonal=[];cross={}
for j in range(4):
 p=[0]*4;p[j]=1;vp=scalar(p);p[j]=-1;vm=scalar(p)
 linear.append(s.factor((vp-vm)/2));diagonal.append(s.factor((vp+vm)/2-origin_value))
for j,k in combinations(range(4),2):
 p=[0]*4;p[j]=p[k]=1
 cross[f'{j},{k}']=s.factor(scalar(p)-origin_value-linear[j]-linear[k]-diagonal[j]-diagonal[k])
params=s.symbols('a b c d')
polynomial=origin_value+sum(linear[j]*params[j]+diagonal[j]*params[j]**2 for j in range(4))+sum(v*params[int(k.split(',')[0])]*params[int(k.split(',')[1])] for k,v in cross.items())
for pt in [[2,-1,3,-2],[-3,2,1,4],[1,1,1,1]]:assert scalar(pt)==polynomial.subs(dict(zip(params,pt)))
REPORT['quadratic']={'coordinates':['a nu_X','b nu_Y','c z^-2 X E0^2','d z^-2 Y E0^2'],'constant':str(origin_value),'linear':list(map(str,linear)),'squares':list(map(str,diagonal)),'mixed':{k:str(v) for k,v in cross.items()},'obstruction_polynomial':str(s.factor(polynomial)),'interpolation_validation_points':[[2,-1,3,-2],[-3,2,1,4],[1,1,1,1]],'degree_bound':2}
def ser(v):return [[list(ch) if isinstance(ch,tuple) else ch,list(e),str(c)] for (ch,e),c in sorted(v.items())]
def cser(c):return [{'open':list(k),'terms':ser(v)} for k,v in sorted(c.items())]
REPORT['representatives']={'origin':[cser(c) for c in origin],'directions':[[cser(c) for c in d] for d in dirs]}
REPORT['input_hashes']={n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['order_1.json','order_2.json']}
(OUT/'early_parameters.json').write_text(json.dumps(REPORT,indent=2)+'\n')
print('First-order fixed-beta differences: 2 H2(U) + 2 H1(W) = 4.')
print('Second-order homogeneous kernel: 0 H2(U) + 1 H1(W) = 1.')
print('Homogeneous order-two obstruction quotient dimension:',REPORT['2']['obstruction_dimension'])
print('Normalized detector equation:',s.factor(polynomial),'= 0')
print('Three off-grid polynomial identity checks: PASS')

# The degree bound is structural: two brackets, followed only by rational linear maps.
# Reconstruct every vector coefficient, then give an explicit polynomial preimage.
def vector(pt):
 return evaluations[tuple(pt)]
zero=(0,0,0,0);v0=vector(zero);linear_vectors=[];square_vectors=[]
for j in range(4):
 plus=[0]*4;minus=[0]*4;plus[j]=1;minus[j]=-1
 linear_vectors.append((vector(plus)-vector(minus))/2)
 square_vectors.append((vector(plus)+vector(minus))/2-v0)
obs=v0.copy()
for j in range(4):obs+=linear_vectors[j]*params[j]+square_vectors[j]*params[j]**2
for j,k in combinations(range(4),2):
 pt=[0]*4;pt[j]=pt[k]=1
 cross_vector=vector(pt)-v0-linear_vectors[j]-linear_vectors[k]-square_vectors[j]-square_vectors[k]
 obs+=cross_vector*params[j]*params[k]
obs=obs.applyfunc(s.expand)
for pt in [(2,-1,3,-2),(-3,2,1,4),(1,1,1,1)]:
 assert obs.subs(dict(zip(params,pt)))==vector(pt)
_,selected_rows=DH.T.rref();selected_rows=list(selected_rows)
minor=DH[selected_rows,:];assert minor.det()==1
preimage=(minor.inv()*obs[selected_rows,:]).applyfunc(s.expand)
assert (DH*preimage-obs).applyfunc(s.expand)==s.zeros(16,1)
assert s.expand((detector.T*obs)[0])==0
assert REPORT['1']['source_dimension']==22
assert REPORT['1']['D_rank']==19 and REPORT['1']['kernel_dimension']==3
assert REPORT['1']['evaluation_rank']==1 and REPORT['1']['fixed_beta_kernel_dimension']==2
assert REPORT['2']['source_dimension']==15 and REPORT['2']['D_rank']==15
assert REPORT['2']['kernel_dimension']==0 and REPORT['2']['target_dimension']==16
assert polynomial==0
# The affine origin satisfies the fixed positive first pairing in the supplied map.
x=s.zeros(len(F['source_basis']),1)
for i,j,value in F['preimage_x_sparse']:x[i,j]=s.Rational(value)
beta=s.zeros(*[F['Ev_shape'][0],1])
for i,j,value in F['target_b_sparse']:beta[i,j]=s.Rational(value)
assert matrix(F,'D')*x==s.zeros(F['D_shape'][0],1)
assert matrix(F,'Ev')*x==beta and beta!=s.zeros(beta.rows,1)
# The declared first-jet coordinates are frozen; basis changes are not silently allowed.
author=json.loads((R/'first_jet.json').read_text())
def norm(c):
 return {tuple(v['open']):{(tuple(ch) if isinstance(ch,list) else ch,tuple(e)):Q(a) for ch,e,a in v['terms']} for v in c}
for i,name in enumerate(['finite','infinity','mixed']):assert origin[i]==norm(author['origin'][name])
for i in range(4):
 for j,name in enumerate(['finite','infinity','mixed']):assert dirs[i][j]==norm(author['directions'][i][name])
# Check original-cover regularity, plane degrees and the prescribed secondary character.
pdegrees=[-3,0,-4,-4]
for triple in [origin,*dirs]:
 for chart,cochain in enumerate(triple):
  weights=[3,6,0,2] if chart==1 else [3,0,2,2]
  offset=-7 if chart==1 else -3
  for opened,tensor in cochain.items():
   for ((i,j),e),coef in tensor.items():
    assert all(e[t+1]>=0 for t in range(3) if t not in opened)
    assert chart==2 or (e[0]<=0 if chart==1 else e[0]>=0)
    assert sum(e[1:])==pdegrees[i]+pdegrees[j]+1
    assert 2*e[0]+e[1]+e[2]==offset+weights[i]+weights[j]
certificate={
 'coordinate_order':['a=nu_X','b=nu_Y','c=z^-2 X E0^2','d=z^-2 Y E0^2'],
 'degree_bound':2,'D2_hom':[[str(v) for v in DH.row(i)] for i in range(16)],
 'source_columns':REPORT['2']['selected_source_indices'],'target_rows':D2rows,
 'left_cokernel_detector':[str(v) for v in detector],
 'obstruction_vector':[str(v) for v in obs],
 'polynomial_preimage':[str(v) for v in preimage],
 'invertible_minor_rows':selected_rows,'minor_determinant':'1',
 'scalar_obstruction':'0','D2_times_preimage_equals_obstruction':True,
 'second_order_direction':'lambda*z^-1*E0^2',
 'parameter_divisions':False}
(OUT/'quadratic_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('First-jet representatives, cover regularity, grades and positive pairing: PASS')
print('Symbolic D2_hom * y(a,b,c,d) = obstruction(a,b,c,d): PASS')
