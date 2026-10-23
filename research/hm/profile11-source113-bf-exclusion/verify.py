#!/usr/bin/env python3
"""Fixed 13-candidate abstract character audit, not an actual instance computation."""
from characters import *
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent/'audit-inputs'
for name,sha in [('one-one-endpoint-necessary-pairs.json','fe0afa410d89340d3082dc814277f89fbb582c19'),('rank-three-quotient-frontier-144.json','8b5971092f9ef762584912609fd5e9301c4e271d'),('ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md','b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3'),('NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md','d7506dae49b4be43230450c4132bd5db91f137ef')]:
 b=(p/name).read_bytes();assert hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==sha
c=json.loads((p/'one-one-endpoint-necessary-pairs.json').read_text())[113]
assert c['A']==[[-10,'one'],[2,'one'],[16,'one']]
assert c['B']==[[-18,'one'],[-4,'one'],[8,'one']] and c['defect']==0
assert [0,1,0,0,0,1,0,1] in c['compatible_E_types'] and len(c['compatible_E_types'])==10
assert 4+5+6+1+1==17 and -8-10-18-8-10==-54
ls=json.loads((p/'rank-three-quotient-frontier-144.json').read_text())['cases']
assert [r['source_index'] for r in ls if r['id']=='G3.11.ad509d55173f']==[113]
def hom(a,b):
 j,R=a;n,U=b
 return 0 if j<n else inner(chars[R],vm(chars[U],sym(j-n)))[0]
def invariants(row):
 rank=degree=0;h1=chi=ZERO
 for j,R in row:
  dim=chars[R][0][0];rank+=dim;degree-=j*dim
  if j>=4:h1=va(h1,vm(chars[R],sym(j-4)))
  if j==3:chi=va(chi,chars[R])
  elif j>=5:chi=vs(chi,vm(chars[R],sym(j-5)))
 return rank,degree,h1,chi
candidates=[[(8,'A')],[(8,'V')]]
for j,k in [(3,18),(5,14),(7,10),(9,6)]:
 for R in ['W','Wp']:candidates.append([(j,R),(k,'one')])
for ns in [(6,6,12),(6,8,10),(8,8,8)]:candidates.append([(j,'one') for j in ns])
assert len(candidates)==13
ks=[[(8,'A')],[(7,'W'),(10,'one')],[(9,'W'),(6,'one')],[(3,'Wp'),(18,'one')],[(6,'one'),(8,'one'),(10,'one')]]
found=[]
for row in candidates:
 r,d,h,c0=invariants(row);assert(r,d)==(3,-24)
 if h==rep('A+V+P+D') and c0==vk(-1,rep('W+S+T')):found.append(row)
assert set(map(tuple,found))==set(map(tuple,ks))
expected=[{((8,'A'),(4,'D')),((8,'A'),(5,'T'))},
 {((7,'W'),(4,'D')),((10,'one'),(5,'T')),((10,'one'),(10,'one'))},
 {((9,'W'),(4,'D')),((9,'W'),(5,'T'))},
 {((18,'one'),(4,'D')),((18,'one'),(5,'T'))},
 {((8,'one'),(4,'D')),((10,'one'),(5,'T')),((10,'one'),(10,'one'))}]
for row,support in zip(ks,expected):
 actual=set()
 for a in row:
  for b in [(4,'D'),(5,'T'),(10,'one'),(12,'one')]:
   h=hom(a,b);assert h in(0,1)
   if h:actual.add((a,b))
 assert actual==support,(row,actual)
for b in [(4,'D'),(5,'T'),(10,'one'),(12,'one')]:assert hom((4,'V'),b)==0
# Universal factor maps for the two rank-dropping D channels.
assert hom((8,'A'),(7,'W'))==1 and hom((7,'W'),(4,'D'))==1
assert hom((9,'W'),(8,'one'))==1 and hom((8,'one'),(4,'D'))==1
# Invariant exclusions and uniqueness of residual covariants.
assert sym(10)==rep("A+V+D")
for n in [6,8,10,14,18]:assert inner(sym(n),chars['one'])==q(0)
assert inner(sym(14),chars['D'])==q(1) and inner(sym(2),chars['D'])==q(0)
assert inner(sym(13),chars['T'])==q(1) and inner(sym(1),chars['T'])==q(0)
assert vm(chars['P'],chars['W'])==rep('Wp+T')
assert vm(chars['P'],chars['A'])==rep('V+P+D')
assert vm(chars['T'],chars['W'])==rep('V+P+D')
assert vm(chars['T'],chars['A'])==rep('Wp+S+2T')
assert vm(chars['D'],chars['W'])==rep('S+T')
assert vm(chars['Wp'],sym(3))==rep('V+D')
assert vm(chars['Wp'],sym(2))==chars['T']
# First-polar characters from each declared saturated internal image.
def polar(J):
 c0=vs(sym(18),chars['P']);c1=sym(19)
 for j,R in J:
  c0=vs(c0,vm(chars[R],sym(j-4)))
  c1=vs(c1,vm(chars[R],sym(j-5)))
 return c0,vs(c1,vm(c0,chars['W']))
assert polar([(7,'W')])==(rep('V+P'),ZERO)
assert polar([(8,'A')])==(ZERO,rep('Wp+T'))
assert polar([(7,'W'),(10,'one')])==(ZERO,rep('Wp+T'))
assert polar([(9,'W')])==(chars['A'],vs(rep('Wp+T'),chars['S']))
assert polar([(8,'one'),(10,'one')])==(chars['A'],vs(rep('Wp+T'),chars['S']))
assert polar([(18,'one')])==(ZERO,chars['T'])
# Constant seven-space residual quotient and horizontal O(-8).
for target in [(2,'D'),(3,'T'),(8,'one'),(10,'one')]:
 assert hom((5,'W'),target)==(1 if target==(2,'D') else 0)
assert vs(vm(chars['W'],chars['S']),chars['D'])==chars['A']
for target in [(10,'one'),(-2,'one'),(5,'T'),(12,'one')]:assert hom((8,'one'),target)==0
# C9 forbidden top representation and all actual lower-row vanishings.
for target in [(2,'P'),(2,'D'),(3,'T'),(8,'one'),(10,'one')]:assert hom((2,'V'),target)==0
assert {0,4,5,9}.isdisjoint({6,7})
assert 8*(-2)-(-18)==2
assert hom((-2,'P'),(-4,'one'))==0
for atom in [(4,'A'),(3,'W'),(6,'one')]:
 for target in [(-4,'one'),(8,'one')]:assert hom(atom,target)==0
assert hom((-3,'Wp'),(-4,'one'))==0
for R in ['W','Wp']:
 for target in [(2,'D'),(3,'T')]:assert hom((3,R),target)==0
for R in ['one','A','V']:
 for target in [(2,'D'),(3,'T'),(8,'one'),(10,'one')]:assert hom((2,R),target)==0
for target in [(-4,'one'),(8,'one')]:assert hom((14,'one'),target)==0
# Degree and full-span arithmetic for every surviving span.
assert -8+18==10 and 10-6==4 and 10-8==2 and 10-14==-4
assert 10-10==0 and 10-18==-8 and 10-10-8==-8 and 10-16==-6
assert 9*(-2)+2*(-3)==-24
assert -20-18==-38 and -18-(-8)==-10 and 3*(-4)==-12
for cdim in [8,12]:
 assert 17-(cdim-2)==19-cdim and -54-(-38)==-16
 assert ((19-cdim)+16)-(30-cdim)==5
assert 5<12
# Original degree38 dual obstruction.
M2=rep('A+2V+3P+4D');M3=rep('3Wp+3S+6T')
assert vs(vm(M3,sym(2)),vm(M2,sym(3)))==vs(chars['T'],rep('2W+S'))
assert vs(M2,va(sym(16),sym(18)))==chars['D']
chiR=va(vs(chars['T'],rep('2W+S')),va(sym(13),sym(15)))
assert chiR==vs(rep('Wp+S+4T'),chars['W'])
assert vs(chiR,vm(chars['D'],chars['W']))==vs(rep('Wp+3T'),chars['W'])
assert va(chiR,chars['W'])==rep('Wp+S+4T')
assert vm(rep('2Wp+T'),chars['A'])==rep('Wp+S+4T')
assert sym(9)==rep('S+T') and inner(sym(9),chars['Wp'])==q(0)
print('PASS: four original Git hashes; exact bf tuple; thirteen kernel candidates; complete five-kernel internal Hom support; rank-dropping factor channels; six polar characters; all changed span/lower-row Hom tests; uniform defect≤5; original dual strict-top contradiction.')
print('Fixed abstract character arithmetic and catalog reads only; no selected actual coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans or large computation.')
