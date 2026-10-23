#!/usr/bin/env python3
"""Small fixed representation identities and exact catalog checks; no instance evaluation."""
from characters import *
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent/'audit-inputs'
for name,sha in [('one-one-endpoint-necessary-pairs.json','fe0afa410d89340d3082dc814277f89fbb582c19'),('rank-three-quotient-frontier-144.json','8b5971092f9ef762584912609fd5e9301c4e271d')]:
 b=(p/name).read_bytes()
 assert hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==sha
c=json.loads((p/'one-one-endpoint-necessary-pairs.json').read_text())[113]
assert c['A']==[[-10,'one'],[2,'one'],[16,'one']]
assert c['B']==[[-18,'one'],[-4,'one'],[8,'one']] and c['defect']==0
assert len(c['compatible_E_types'])==10
assert all(a==d==g==0 and h==1 and b+cc+e+f==2 for a,b,cc,d,e,f,g,h in c['compatible_E_types'])
assert [0,1,1,0,0,0,0,1] in c['compatible_E_types']
ls=json.loads((p/'rank-three-quotient-frontier-144.json').read_text())['cases']
assert [r['source_index'] for r in ls if r['id']=='G3.11.ad509d55173f']==[113]
assert sym(6)==rep('V+P') and sym(7)==rep('Wp+T') and sym(8)==rep('P+D')
assert sym(18)==rep('A+V+2P+D') and sym(19)==rep('W+Wp+S+2T')
assert vm(chars['T'],chars['A'])==rep('Wp+S+2T')
assert vm(chars['V'],chars['W'])==chars['T']
def hom(a,b):
 j,R=a;n,U=b
 return 0 if j<n else inner(chars[R],vm(chars[U],sym(j-n)))[0]
ks=[[(4,'P'),(7,'W')],[(3,'Wp'),(5,'Wp'),(7,'W')],[(4,'P'),(6,'one'),(8,'one')],[(3,'Wp'),(5,'Wp'),(6,'one'),(8,'one')]]
for row in ks:
 rank=degree=0;h1=chi=ZERO
 for j,R in row:
  dim=chars[R][0][0];rank+=dim;degree-=j*dim
  if j>=4:h1=va(h1,vm(chars[R],sym(j-4)))
  if j==3:chi=va(chi,chars[R])
  elif j>=5:chi=vs(chi,vm(chars[R],sym(j-5)))
  for target in [(5,'T'),(6,'V'),(12,'one')]:assert hom((j,R),target)==0
 assert (rank,degree)==(6,-30) and h1==rep('A+P+D') and chi==vk(-1,rep('W+S'))
for target in [(3,'T'),(4,'V'),(10,'one')]:assert hom((4,'one'),target)==0
assert -14+18==4 and -14+6==-8
assert 6+3+1==10 and -18-12-10==-40
assert 30-9==21 and 10+40-21==29 and 29-24<12
assert -40+24==-16 and 14+24==38 and 38-18==20
assert len({(-8)%10,8%10,(-4)%10})==3
M2=rep('A+2V+3P+4D');M3=rep('3Wp+3S+6T')
assert vs(vm(M3,sym(2)),vm(M2,sym(3)))==vs(chars['T'],rep('2W+S'))
assert vs(M2,va(sym(16),sym(18)))==chars['D']
chiR=va(vs(chars['T'],rep('2W+S')),va(sym(13),sym(15)))
assert chiR==vs(rep('Wp+S+4T'),chars['W'])
assert vs(chiR,vm(chars['D'],chars['W']))==vs(rep('Wp+3T'),chars['W'])
assert va(chiR,chars['W'])==rep('Wp+S+4T')
assert vm(rep('2Wp+T'),chars['A'])==rep('Wp+S+4T')
assert sym(9)==rep('S+T') and inner(sym(9),chars['Wp'])==q(0)
print('PASS: pinned catalog hashes; all ten original tuples; exact bc source; four kernel characters; every changed internal Hom; intersection Hom; defect budget; dual cohomology and strict-top contradiction.')
print('Only fixed abstract character arithmetic and catalog reads. No selected actual source data or large computation.')
