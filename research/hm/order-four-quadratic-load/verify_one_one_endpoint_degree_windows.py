#!/usr/bin/env python3
"""Bounded universal characters only; no actual coefficients, points or ranks."""
import contextlib,io,runpy
from pathlib import Path
from functools import lru_cache
from itertools import combinations_with_replacement
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
names=('one','W','Wp','A','V','P','S','D','T'); reps=[r[n] for n in names]
def dec(ch):
 a=[r['inner'](ch,R) for R in reps]
 assert all(y==0 and x.denominator==1 for x,y in a)
 return tuple(int(x) for x,y in a)
zero=(0,)*9
unit=lambda i:tuple(int(i==j)for j in range(9))
def add(*xs):return tuple(map(sum,zip(*xs)))
def neg(x):return tuple(-v for v in x)
def eff(x):return min(x)>=0
@lru_cache(None)
def tensor(i,j):return dec(r['vmul'](reps[i],reps[j]))
def mul(x,y):return tuple(sum(x[i]*y[j]*tensor(i,j)[k]for i in range(9)for j in range(9)if x[i] and y[j])for k in range(9))
@lru_cache(None)
def sym(n):return dec([r['sym'](n,w)for w in r['W']])
@lru_cache(None)
def chi_line(d):return sym(d)if d>=0 else zero if d==-1 else neg(sym(-d-2))
@lru_cache(None)
def block(e,i,t):return mul(unit(i),chi_line(e+t))
def chi(X,t):return add(zero,*[block(e,i,t)for e,i in X])
def h0(X,t):return chi(tuple((e,i)for e,i in X if e+t>=0),t)
def dim(x):return sum(x[i]*int(reps[i][0][0])for i in range(9))
M2=(0,0,0,1,2,3,0,4,0); M3=(0,0,3,0,0,0,3,0,6)
def dual(t):return add(mul(M3,chi_line(t-1)),neg(mul(M2,chi_line(t))))
allowed=[]
for j in range(2,43):
 for i,R in enumerate(reps):
  if R[1][0]!=(-1)**j*R[0][0]:continue
  if eff(add(M2,neg(mul(unit(i),sym(j-2))))):allowed.append((j,names[i]))
print('Q* allowed negative blocks:',allowed)
J=max(j for j,n in allowed); print('Maximum j:',J)
def candidates(degree,lo):
 upper=degree-2*lo
 for es in combinations_with_replacement(range(lo+(lo%2),upper+1,2),3):
  if sum(es)==degree:yield tuple((e,0)for e in es)
 for i in (1,2):
  for e in range(lo+int(lo%2==0),upper+1,2):
   f=degree-2*e
   if f>=lo and f%2==0:yield ((e,i),(f,0))
 if degree%6==0 and degree//3>=lo:
  for i in (3,4):yield ((degree//3,i),)
# Top L <= -2 gives b>=-34; transpose and independently proved a>=-4 give b<=-2.
Bs={}
for b in range(-34,-1,2):
 Bs[b]=[X for X in candidates(b,-J) if eff(add(chi(X,1),neg(dual(1)))) and eff(add(h0(X,0),chi(X,2),neg(dual(2))))]
print('B survivors by degree:',[(b,len(xs))for b,xs in Bs.items()])
Bs={b:[X for X in xs if max(e for e,i in X)<=8]for b,xs in Bs.items()}
print('B survivors with transpose upper bound 8:',[(b,len(xs))for b,xs in Bs.items()])
print('Lowest B:',next((b,[(tuple((e,names[i])for e,i in X))for X in xs])for b,xs in Bs.items()if xs))
def h1(X,t):return add(h0(X,t),neg(chi(X,t)))
Bs={b:[X for X in xs if eff(add(M2,neg(h1(X,0))))]for b,xs in Bs.items()}
print('B survivors with H1 quotient:',[(b,len(xs))for b,xs in Bs.items()])
print('Lowest B:',next((b,[(tuple((e,names[i])for e,i in X))for X in xs])for b,xs in Bs.items()if xs))
chiE3=(0,0,1,0,0,0,0,0,2)
As={a:[X for X in candidates(a,-10) if eff(add(chi(X,2),unit(4))) and eff(add(h0(X,1),chi(X,3),neg(chiE3))) and eff(add((0,0,1,0,0,0,0,0,3),neg(h1(X,1))))] for a in range(-4,25,2)}
def ordinary(X):return sorted(e for e,i in X for _ in range(int(reps[i][0][0])))
def equiv_nonzero(X,Y):
 return all(any(e<=f and mul(mul(unit(i),unit(j)),sym(f-e))[0]>0 for f,j in Y)for e,i in X)
def dualtwist(X):return tuple((-e-2,i)for e,i in X)
pairs=[]
for a,axs in As.items():
 for b,bxs in Bs.items():
  t=-6-a-b
  if t not in (0,12,20,24):continue
  for X in axs:
   for Y in bxs:
    Z=dualtwist(Y)
    if any(e>f for e,f in zip(ordinary(X),ordinary(Z))):continue
    if not equiv_nonzero(X,Z) or not equiv_nonzero(Y,dualtwist(X)):continue
    if t==0 and sorted(X)!=sorted(Z):continue
    pairs.append((a,b,t,X,Y))
print('Pair count:',len(pairs))
print('Degree triples:',sorted(set((a,b,t)for a,b,t,X,Y in pairs)))
print('Pair count by defect:',{t:sum(p[2]==t for p in pairs)for t in (0,12,20,24)})
M4=(0,0,0,0,2,4,0,3,0)
pairs=[p for p in pairs if eff(add(M2,neg(h0(p[3],0)))) and eff(add(M4,neg(h0(p[4],0)))) and eff(add((0,0,1,0,0,0,0,0,3),neg(h0(p[4],-1))))]
print('Full incidence survivors:',len(pairs))
print('Degree triples:',sorted(set((a,b,t)for a,b,t,X,Y in pairs)))
print('Pair count by defect:',{t:sum(p[2]==t for p in pairs)for t in (0,12,20,24)})
with contextlib.redirect_stdout(io.StringIO()):
 er=runpy.run_path(str(Path(__file__).with_name('verify_equivariant_splitting_gauss_persistence.py')))
Es=[]
for coeff,R2,blocks in er['profiles']:
 X=tuple((-j,i)for j,R in blocks for i,n in enumerate(dec(R)) for _ in range(n))
 Es.append((coeff,X))
compatible=[]
for p in pairs:
 a,b,t,X,Y=p
 ok=[]
 for coeff,E in Es:
  if all(eff(add(h1(E,u),neg(h1(X,u)))) and eff(add(h1(E,-u),neg(h0(Y,u)))) for u in range(-10,11)):
   ok.append(coeff)
 if ok:compatible.append((p,ok))
print('28-type compatible:',len(compatible))
print('Degree triples:',sorted(set(p[:3]for p,ok in compatible)))
print('Pair count by defect:',{t:sum(p[2]==t for p,ok in compatible)for t in (0,12,20,24)})
print('b=-32 certificates:')
for X in candidates(-32,-30):
 if max(e for e,i in X)>8 or dim(h0(X,0))<8:continue
 envs=[add(chi(X,1),neg(dual(1))),add(h0(X,0),chi(X,2),neg(dual(2)))]
 print(X,[(k+1,names[i],v)for k,C in enumerate(envs)for i,v in enumerate(C)if v<0])
assert J==30
assert not Bs[-34] and not Bs[-32]
assert len(compatible)==159
assert {t:sum(p[2]==t for p,ok in compatible)for t in (0,12,20,24)}=={0:80,12:61,20:5,24:13}
import json
out=[dict(a=p[0],b=p[1],defect=p[2],A=[(e,names[i])for e,i in p[3]],B=[(e,names[i])for e,i in p[4]],compatible_E_types=ok)for p,ok in compatible]
Path(__file__).with_name('one-one-endpoint-necessary-pairs.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS: endpoint-safe -4<=a<=24, -30<=b<=-2, t in {0,12,20,24}; 159 necessary pairs, 25 degree triples. No realizability or rank-four assertion.')
assert len(allowed)==38
bad32=[X for X in candidates(-32,-30) if max(e for e,i in X)<=8 and dim(h0(X,0))>=8]
assert [tuple(e for e,i in X)for X in bad32]==[(-30,-10,8),(-28,-12,8),(-26,-14,8),(-24,-16,8),(-22,-18,8),(-20,-20,8)]
assert [add(chi(X,1),neg(dual(1)))[2]for X in bad32]==[-2,-1,-1,-1,-1,-2]
triples=set(p[:3]for p,ok in compatible)
assert len(triples)==25
assert triples=={(a,-6-a,0)for a in (-4,-2,0,2,4,6,8,10,12,14,16,18,22,24)}|{(a,-18-a,12)for a in (-4,-2,0,2,4,6,10,12)}|{(-2,-24,20),(2,-28,20),(-2,-28,24)}
assert min(p[0]for p,ok in compatible)==-4 and max(p[0]for p,ok in compatible)==24
assert min(p[1]for p,ok in compatible)==-30 and max(p[1]for p,ok in compatible)==-2
