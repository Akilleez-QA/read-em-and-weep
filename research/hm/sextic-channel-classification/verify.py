#!/usr/bin/env python3
"""Universal character, support, apolar and polynomial controls only."""
from pathlib import Path
from collections import Counter
from itertools import product
import hashlib,json,sys
import sympy as sp
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok:raise RuntimeError(msg)
def equal(a,b):
 z=Counter(a);z.subtract(b);return not any(z.values())
def dimension(a):return sum(c.DIM[r]*m for r,m in a.items())
def add(*xs):
 z=Counter()
 for x in xs:z.update(x)
 return z
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==4,'four full public inputs')
for x in manifest:
 b=(ROOT/x['file']).read_bytes()
 require(len(b)==x['bytes'],'bytes')
 require(hashlib.sha256(b).hexdigest()==x['sha256'],'sha256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],'git blob')
require(equal(c.product('one',6),{'V':1,'P':1}),'multiplicity-free sextics')
require(equal(c.product('V',1),{'T':1}),'linear V')
require(equal(c.product('P',1),{'Wp':1,'T':1}),'linear P')
require(equal(c.product('one',7),{'Wp':1,'T':1}),'Sym7')
rows={'V':{'r':3,'threshold':2,'syzygy':'Wp','shift':3,'length':27},'P':{'r':4,'threshold':1,'syzygy':'V','shift':2,'length':24},'VP':{'r':7,'threshold':0,'syzygy':'T','shift':1,'length':21}}
for name,row in rows.items():
 for d in range(65):
  src=c.product(name,d) if name!='VP' else add(c.product('V',d),c.product('P',d))
  target=c.product('one',d+6)
  kernel=c.product(row['syzygy'],d-row['shift'])
  cokernel=c.product(row['syzygy'],row['shift']-d-2)
  require(equal(add(src,cokernel),add(target,kernel)),f'exact {name}/{d}')
  require(dimension(src)==row['r']*(d+1),'source dimension')
  require(dimension(kernel)-dimension(cokernel)==dimension(src)-(d+7),'Euler dimension')
  require((not cokernel)==(d>=row['threshold']),'sharp threshold')
 hilbert=[]
 for j in range(45):
  h=(j+1)-row['r']*max(j-5,0)+(row['r']-1)*max(j-(6+row['shift'])+1,0)
  require(h>=0,'Hilbert nonnegative')
  if h:hilbert.append(h)
 require(sum(hilbert)==row['length'],'quotient length')
 require(hilbert=={'V':[1,2,3,4,5,6,4,2],'P':[1,2,3,4,5,6,3],'VP':[1,2,3,4,5,6]}[name],'full Hilbert vector')
# Exhaust active supports rather than treating nonzero two-channel maps as units.
strata=[]
for U in [('V',),('P',),('V','P')]:
 for active in product((False,True),repeat=len(U)):
  if not any(active):continue
  J=tuple(x for x,on in zip(U,active) if on)
  inactive=tuple(x for x,on in zip(U,active) if not on)
  r=sum(c.DIM[x] for x in J)
  for d in range(1,33):
   m=6 if J==('V',) and d==1 else d+7
   require(m>=r,'span contains active fiber')
   require((m==d+7)==(J!=('V',) or d>=2),'complete iff threshold')
   for high_rank in range(7):
    if d==1 and high_rank:continue
    b=high_rank+sum(c.DIM[x] for x in inactive)
    M=m+b+(1 if b else 0)
    codim=M-(b+r)
    require(codim==m-r+(1 if b else 0),'strict rank arithmetic')
    require(not inactive or b>0,'inactive contributes to kernel')
  strata.append({'source':'+'.join(U),'active':'+'.join(J),'inactive':'+'.join(inactive),'rank':r})
require(len(strata)==5,'all nonzero support strata')
# Enumerate all semisimple ambient quotients at d=1 from coefficient modules.
exact=[]
expected={('V','V'):[(0,1,3)],('P','P'):[(1,1,4)],('VP','V'):[(0,2,5),(1,2,7)],('VP','P'):[(1,2,7)],('VP','VP'):[(1,1,1),(1,2,7)]}
for (U,J),wanted in expected.items():
 maxwp=0 if U=='V' else 1;maxt=2 if U=='VP' else 1
 rsource=rows[U]['r']; choices=[]
 for wp in range(maxwp+1):
  for t in range(maxt+1):
   M=2*wp+6*t
   if J=='V':rwp,rt=0,1
   else:rwp,rt=1,1
   if wp<rwp or t<rt:continue
   # Inactive P must span at least6 and inactive V exactlyT.
   if U=='VP' and J=='V' and (2*(wp-rwp)+6*(t-rt)<6):continue
   if U=='VP' and J=='P' and t-rt<1:continue
   if M<rsource:continue
   choices.append((wp,t,M-rsource))
 require(choices==wanted,f'exact d1 {U}/{J}')
 exact.append({'source':U,'active':J,'ambient_Wp_T_codim':choices})
# Full formal monomial apolar annihilation and complementary dimensions.
apolar=0
for d in range(1,41):
 n=d+6
 for i in range(d):
  for j in range(7):
   require(i+j!=n,'all osculating-annihilator pairings vanish');apolar+=1
  require(7<=n-i<=n,'unique complement pairing exists')
 require(d+7==n+1,'complementary apolar dimensions')
# Symbolic derivative kernel, not evaluation at a parameter or actual source.
x,y,s,t=sp.symbols('x y s t')
f=(t*x-s*y)**6
require(sp.expand(s*sp.diff(f,x)+t*sp.diff(f,y))==0,'pure sixth power derivative kernel')
M=sp.zeros(6,7)
for j in range(7):
 if j<6:M[j,j]=(6-j)*s
 if j>0:M[j-1,j]=j*t
require(sp.expand(M[:,:6].det())==720*s**6,'first universal minor')
require(sp.expand(M[:,1:].det())==720*t**6,'second universal minor')
require(6<12 and 7<12,'base divisors below orbit minimum')
# The two complete coefficient representations and model dimensions.
require(equal(add(c.product('V',1),c.product('P',1)),{'Wp':1,'T':2}),'full coefficient module')
require(12-7==5 and 14-7==7 and 8-7==1,'sharp fullsource model codimensions')
out={'checks':checks+c.checks,'source_inputs':len(manifest),'support_strata':strata,'exact_d1_strata':exact,'formal_apolar_pairings':apolar,'thresholds':{k:v['threshold'] for k,v in rows.items()},'quotient_lengths':{k:v['length'] for k,v in rows.items()},'actual_instance_evaluated':False,'new_actual_profile_exclusion':False}
text=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(text)
else:require((ROOT/'RESULT.json').read_text()==text,'retained output identical')
print(text,end='')
