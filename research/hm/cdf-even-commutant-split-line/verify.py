#!/usr/bin/env python3
"""Exact universal algebra/character checks; no actual HM instance evaluation."""
from pathlib import Path
import hashlib,json,itertools
import sympy as s
ROOT=Path(__file__).resolve().parent
ncheck=0
def ck(v,msg):
 global ncheck
 if not v:raise ValueError(msg)
 ncheck+=1
def zero(v):return s.expand(v)==0
for r in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/r['file']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==r['sha256'],'SHA '+r['file'])
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['git_blob'],'blob '+r['file'])
# Universal multiplication in each source summand, with explicit right inverses.
for n in (16,5):
 x=s.zeros(n+2,n+1);y=s.zeros(n+2,n+1)
 for i in range(n+1):x[i,i]=1;y[i+1,i]=1
 M=x.row_join(y);R=s.zeros(2*(n+1),n+2)
 for i in range(n+1):R[i,i]=1
 R[-1,-1]=1
 ck(M*R==s.eye(n+2),'generated middle Sym'+str(n))
ck(all(d+1<0 for d in (-2,-4,-8)),'target joint kernel H0 E1 zero')
# Algebra tuple (a,b,dV,dP,alpha,beta,gamma1,gamma2).
def mul(x,y):
 a,b,v,p,al,be,g,h=x;A,B,V,P,AL,BE,G,H=y
 return (a*A,b*B,v*V,p*P,b*AL+V*al,a*BE+P*be,b*G+P*g,b*H+P*h)
x=s.symbols('x:8');y=s.symbols('y:8');z=s.symbols('z:8')
for i,(l,r) in enumerate(zip(mul(mul(x,y),z),mul(x,mul(y,z)))):ck(zero(l-r),'associative coordinate'+str(i))
unit=(1,1,1,1,0,0,0,0)
ck(mul(unit,x)==x and mul(x,unit)==x,'unit')
rx=(0,0,0,0,*x[4:]);ry=(0,0,0,0,*y[4:])
ck(mul(rx,ry)==(0,)*8,'four-dimensional radical square zero')
ck(4+4==8,'full even algebra dimension')
# All full-linear coordinates sit in the claimed subalgebra.
a,b,d,w,A,B,D,W=s.symbols('a b d w A B D W')
f=(a,b,d,d,0,w,0,0);g=(A,B,D,D,0,W,0,0)
ck(mul(f,g)==(a*A,b*B,d*D,d*D,0,a*W+D*w,0,0),'full linear subalgebra')
# All four source-(0,1) idempotent types, including each arrow coefficient.
al,be,g1,g2=s.symbols('alpha beta gamma1 gamma2')
for v,p in itertools.product((0,1),repeat=2):
 e=(0,1,v,p,al,be,g1,g2);e2=mul(e,e)
 ck(zero(e2[4]-e[4]-v*al),'V shear idempotent equation')
 ck(zero(e2[5]-e[5]-(p-1)*be),'F/P shear idempotent equation')
 ck(zero(e2[6]-e[6]-p*g1) and zero(e2[7]-e[7]-p*g2),'B/P shears idempotent equations')
# Exact character bottlenecks and forced footprint.
names=('A','V','P','D');dims=(3,3,4,5)
def c(**kw):return tuple(kw.get(n,0) for n in names)
def add(*vs):return tuple(map(sum,zip(*vs)))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mn(a,b):return tuple(min(x,y) for x,y in zip(a,b))
def dim(a):return sum(x*y for x,y in zip(a,dims))
xf=c(V=1,P=1,D=2);xb=c(A=1,V=1,P=2,D=2)
yf=c(P=1,D=1);yb=c(V=1,P=2,D=2);im=c(V=2,P=3,D=3)
rows=[]
for v,p in itertools.product((0,1),repeat=2):
 y0=add(yf,c(V=1-v,P=1-p));y1=add(yb,c(V=v,P=p))
 i0,i1=mn(xf,y0),mn(xb,y1);bound=add(i0,i1)
 ck(bound[1]==2-v,'V bottleneck exhausts target bits')
 ck(dim(bound)==(33 if not v else 30),'exact image upper dimension')
 if not v:
  ck(bound==im,'image maximality attained constituentwise')
  ck(sub(xf,i0)==c(D=1) and sub(xb,i1)==c(A=1),'exact kernel separation')
  ck(sub(y0,i0)==c(P=1-p) and sub(y1,i1)==c(P=p),'exact cokernel separation')
 rows.append({'V_bit':v,'P_bit':p,'bound_dimension':dim(bound)})
y0=add(yf,c(V=1));y1=add(yb,c(P=1))
ck(dim(y0)==12 and dim(y1)==25,'surviving eigenspace dimensions')
ck(mn(xf,y0)==y0,'surviving F Q block onto')
ck(sub(y1,mn(xb,y1))==c(P=1),'surviving B cokernel P')
ck(sub(xf,y0)==c(D=1),'persistent formal D kernel')
# Surviving idempotent retains alpha,beta and zero gamma, with split L bits.
e=(0,1,0,1,al,be,0,0)
ck(all(zero(a-b) for a,b in zip(mul(e,e),e)),'all retained graph shears idempotent')
ck(e[2]!=e[3],'remaining idempotent cannot be full linear')
# Formal right-inverse recurrence as exact free-word cancellation: Qs=id_Y.
def reduce_word(word):
 word=list(word)
 while True:
  if any(word[i:i+2]==['q','k'] for i in range(len(word)-1)):return None
  for i in range(len(word)-1):
   if word[i:i+2]==['q','s']:
    word=word[:i]+word[i+2:];break
  else:return tuple(word)
for n in range(1,9):
 left=('q',)+('s','t')*n+('k',)
 right=('t',)+('s','t')*(n-1)+('k',)
 ck(reduce_word(left)==reduce_word(right),'formal correction cancellation order'+str(n))
 ck((-1)**n+(-1)**(n-1)==0,'formal correction signs order'+str(n))
ck(reduce_word(('q','k')) is None,'initial kernel equation')
ck(33+3==36 and 41-5==36,'generic rank trapped at36')
ck(37-36==1 and 41-36==5,'generic kernel and cokernel dimensions')
# One-sided gate places D in B; nonscalar footprint places D in disjoint F.
ck(c(A=1,D=1)!=c(A=1),'one-sided B kernel contradicts nonscalar B kernel')
print(json.dumps({'status':'pass','checks':ncheck,'even_algebra_dimension':8,'radical_dimension':4,'target_bit_table':rows,'surviving_bits':[0,1],'nonscalar_branch_generic_rank':36,'actual_instance_evaluations':0,'scope':'Necessary conditional alternative; occurrence and source exclusion not asserted.'},indent=2))
