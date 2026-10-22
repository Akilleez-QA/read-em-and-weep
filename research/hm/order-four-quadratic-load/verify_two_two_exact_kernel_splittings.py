"""Exhaust negative-kernel splittings using exact cohomology characters."""
from pathlib import Path
import runpy,io,contextlib,json
from functools import lru_cache
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):r=runpy.run_path(str(ROOT/'verify_two_two_symmetric_quotient_constraints.py'))
reps=r['reps'];names=tuple(reps);hc,va,vs,vm,sym=[r[k] for k in ('hc','va','vs','vm','sym')]
mult=r['r']['multiplicity'];zero=(0,)*9
def vec(c):return tuple(mult(c,reps[n]) for n in names)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def positive(a):return min(a)>=0
@lru_cache(None)
def solve_kernel(B,side):
 ch2=r['chiE2'] if side=='E' else r['chiQ2']
 ch3=r['chiE3'] if side=='E' else r['chiQ3']
 H=vec(va(hc(B,2,True),vs(-1,ch2)))
 C=vec(va(ch3,vs(-1,hc(B,3,True))))
 cap=vec(hc(B,1));hd=sum(x*r['dimension'](reps[n]) for x,n in zip(H,names))
 allowed=[]
 for j in range(4,hd+4):
  for n,R in reps.items():
   if R[1][0]!=(-1)**j*R[0][0]:continue
   c=vec(vm(R,sym(j-4)))
   if positive(sub(H,c)):
    c3=vec(vm(R,sym(j-5))) if j>=5 else zero
    allowed.append((j,n,c,c3))
 @lru_cache(None)
 def solve(i,left):
  if i==len(allowed):return ((),) if left==zero else ()
  j,n,c,c3=allowed[i];bound=min(x//y for x,y in zip(left,c) if y)
  out=[]
  for k in range(bound+1):
   rest=tuple(x-k*y for x,y in zip(left,c))
   out.extend((k,)+s for s in solve(i+1,rest))
  return tuple(out)
 out=[]
 for counts in solve(0,H):
  top=C
  for k,(_,_,_,c3) in zip(counts,allowed):top=add(top,tuple(k*x for x in c3))
  if not positive(top) or not positive(sub(cap,top)):continue
  if any(k and reps[n][1][0]!=-reps[n][0][0] for k,n in zip(top,names)):continue
  blocks=[(3,n,k) for k,n in zip(top,names) if k]+[(j,n,k) for k,(j,n,_,_) in zip(counts,allowed) if k]
  assert sum(k*r['dimension'](reps[n]) for j,n,k in blocks)==(14 if side=='E' else 10)
  assert -sum(j*k*r['dimension'](reps[n]) for j,n,k in blocks)==-54-r['degree'](B)
  out.append(blocks)
 return out
pairs=sorted({(x['A'],x['B']) for x in r['records']})
checked=[]
for A,B in pairs:
 ka,kb=solve_kernel(A,'E'),solve_kernel(B,'Q')
 checked.append(dict(A=A,B=B,K_splittings=ka,L_splittings=kb))
passed=[x for x in checked if x['K_splittings'] and x['L_splittings']]
print('Exact negative-kernel splitting pairs:',len(passed),'of',len(pairs))
for x in checked:
 if not x['K_splittings'] or not x['L_splittings']:print('EXCLUDED',x['A'],x['B'])
print('Kernel splitting counts:',[(len(x['K_splittings']),len(x['L_splittings'])) for x in passed])
(ROOT/'two-two-exact-kernel-splittings.json').write_text(json.dumps(checked,indent=2)+'\n')
# Every exact sequence also imposes a genuine six-term cohomology sequence
# at every twist. At the character level, its first two unknown map images
# must be genuine; Euler exactness supplies the remaining image automatically.
Es={co:E for co,E,R in r['Es']};Qs={p:Q for p,Q,R in r['Qs']}
@lru_cache(None)
def kernel_h0(K,t):return hc(tuple((-j,n) for j,n,c in K for _ in range(c)),t)
@lru_cache(None)
def cv(F,t,euler=False):return vec(hc(F,t,euler))
@lru_cache(None)
def exact_compatible(K,F,C):
 KB=tuple((-j,n) for j,n,c in K for _ in range(c))
 for t in range(-30,35):
  hF,hK,hC=cv(F,t),cv(KB,t),cv(C,t)
  image=sub(hF,hK)
  if not positive(image) or not positive(sub(hC,image)):return False
  h1F=sub(hF,cv(F,t,True));h1C=sub(hC,cv(C,t,True))
  if not positive(sub(h1F,h1C)):return False
 return True

surviving=[]
for x in r['records']:
 A,B=x['A'],x['B']
 ks=[K for K in solve_kernel(A,'E') if exact_compatible(tuple(K),Es[x['E']],A)]
 ls=[L for L in solve_kernel(B,'Q') if exact_compatible(tuple(L),Qs[x['Q']],B)]
 if ks and ls:surviving.append(dict(x,K_splittings=ks,L_splittings=ls))
assert len(surviving)==1880
assert len({(x['A'],x['B']) for x in surviving})==34
print('After exact six-term cohomology compatibility:',len(surviving),'records;',len({(x['A'],x['B']) for x in surviving}),'pairs')
(ROOT/'two-two-exact-kernel-compatible-records.json').write_text(json.dumps(surviving,indent=2)+'\n')
