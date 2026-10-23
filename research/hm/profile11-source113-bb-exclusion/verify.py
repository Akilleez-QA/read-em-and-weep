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
assert [0,2,0,0,0,0,0,1] in c['compatible_E_types'] and len(c['compatible_E_types'])==10
assert 4+12+1==17 and -8-36-10==-54
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
expected=[{((8,'A'),(5,'T'))},{((10,'one'),(5,'T'))},{((9,'W'),(5,'T'))},{((18,'one'),(5,'T'))},{((10,'one'),(5,'T'))}]
for row,support in zip(ks,expected):
 actual=set()
 for a in row:
  for b in [(5,'T'),(12,'one')]:
   h=hom(a,b)
   assert h in (0,1)
   if h:actual.add((a,b))
 assert actual==support
assert hom((4,'V'),(5,'T'))==0 and hom((4,'V'),(12,'one'))==0
for n in [6,8,14,18]:assert inner(sym(n),chars['one'])==q(0)
assert inner(sym(13),chars['T'])==q(1) and inner(sym(1),chars['T'])==q(0)
assert vm(chars['P'],chars['W'])==rep('Wp+T')
assert vm(chars['P'],chars['A'])==rep('V+P+D')
assert vm(chars['T'],chars['W'])==rep('V+P+D')
assert vm(chars['T'],chars['A'])==rep('Wp+S+2T')
assert vm(chars['A'],chars['W'])==rep('W+S')
assert vm(chars['Wp'],sym(3))==rep('V+D')
assert vm(chars['Wp'],sym(2))==chars['T']
# Character of M from J and exact raw image; splitting C + L(-1).
def polar(J):
 c0=vs(sym(18),chars['P']);c1=sym(19)
 for j,R in J:
  c0=vs(c0,vm(chars[R],sym(j-4)))
  c1=vs(c1,vm(chars[R],sym(j-5)))
 return c0,vs(c1,vm(c0,chars['W']))
assert polar([(9,'W')])==(chars['A'],vs(rep('Wp+T'),chars['S']))
assert polar([(8,'A')])==(ZERO,rep('Wp+T'))
assert polar([(18,'one')])==(ZERO,chars['T'])
# Every source-dependent Hom used in the two final branch arguments.
for target in [(2,'P'),(3,'T'),(10,'one')]:assert hom((2,'V'),target)==0
assert hom((-2,'P'),(-4,'one'))==0 # P O(2) -> O(4)
assert hom((4,'A'),(-4,'one'))==0 # A O(-4) -> O(4)
assert hom((4,'A'),(8,'one'))==0
assert hom((4,'A'),(3,'T'))==0
assert hom((5,'W'),(3,'T'))==0
assert hom((-3,'Wp'),(-4,'one'))==0 # Wp O(3) -> O(4)
for R in ['W','Wp']:assert hom((3,R),(3,'T'))==0
assert hom((14,'one'),(-4,'one'))==0
assert hom((14,'one'),(8,'one'))==0
# Degree/HN bounds and residual saturation budget.
assert -8+18==10 and 10-8==2 and 10-14==-4
assert -8-18==-26 and -8-12==-20
assert 4*(-2)+4*(-3)==-20 and 4*(-2)+7*(-3)==-29
assert -20-18==-38 and -18-(-8)==-10 and 3*(-4)==-12
assert 17-6==11 and -54-(-38)==-16 and 30-8==22
assert 11+16-22==5 and 5<12
# Universal dual degree38 obstruction, with exact original B.
M2=rep('A+2V+3P+4D');M3=rep('3Wp+3S+6T')
assert vs(vm(M3,sym(2)),vm(M2,sym(3)))==vs(chars['T'],rep('2W+S'))
assert vs(M2,va(sym(16),sym(18)))==chars['D']
chiR=va(vs(chars['T'],rep('2W+S')),va(sym(13),sym(15)))
assert chiR==vs(rep('Wp+S+4T'),chars['W'])
assert vs(chiR,vm(chars['D'],chars['W']))==vs(rep('Wp+3T'),chars['W'])
assert va(chiR,chars['W'])==rep('Wp+S+4T')
assert vm(rep('2Wp+T'),chars['A'])==rep('Wp+S+4T')
assert sym(9)==rep('S+T') and inner(sym(9),chars['Wp'])==q(0)
print('PASS: four pinned original hashes; exact bb source; thirteen kernel candidates; five exact kernels; every internal Hom; three polar characters; final-span Hom tests; HN and saturation budgets; dual strict-top contradiction.')
print('Fixed abstract representation arithmetic and catalog reads only. No selected actual coefficient, parameter, point, derivative, matrix, rank, model or scan.')
