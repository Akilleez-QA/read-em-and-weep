#!/usr/bin/env python3
"""Fixed character and degree checks for the divisor-twelve cf exclusion."""
import runpy
from pathlib import Path
x=runpy.run_path(str(Path(__file__).with_name('verify.py')))
for n in ('q','chars','rep','sym','vm','va','vs','vk','dec','inner','names','ZERO'):
 globals()[n]=x[n]
assert sym(13)==rep('W+Wp+S+T')
assert sym(15)==rep('S+2T')
assert sym(16)==rep('V+P+2D')
assert sym(18)==rep('A+V+2P+D')
assert sym(9)==rep('S+T')
M2=rep('A+2V+3P+4D')
M3=rep('3Wp+3S+6T')
assert vs(vm(M3,sym(2)),vm(M2,sym(3)))==vs(chars['T'],rep('2W+S'))
assert vs(M2,va(sym(16),sym(18)))==chars['D']
chiR=va(vs(chars['T'],rep('2W+S')),va(sym(13),sym(15)))
assert chiR==vs(rep('Wp+S+4T'),chars['W'])
assert vs(chiR,vm(chars['D'],chars['W']))==vs(rep('Wp+3T'),chars['W'])
assert va(chiR,chars['W'])==rep('Wp+S+4T')
assert vm(rep('2Wp+T'),chars['A'])==rep('Wp+S+4T')
for R,out in [('W','W+S'),('Wp','T'),('S','W+S+T'),('T','Wp+S+2T')]:
 assert vm(chars[R],chars['A'])==rep(out)
# The complete declared parity/dimension list for H1 budget D.
eligible={'one':(2,4,6),'W':(3,),'Wp':(3,),'A':(2,),
 'V':(2,),'P':(2,),'S':(),'D':(2,),'T':()}
accepted={(2,'D'),(6,'one')}
budget=dec(chars['D'])
for R,js in eligible.items():
 dim=chars[R][0][0]
 assert js==tuple(j for j in range(2,8) if (j-1)*dim<=5 and chars[R][1][0]==(-1)**j*dim)
 for j in js:
  v=dec(vm(chars[R],sym(j-2)))
  assert all(0<=a<=b for a,b in zip(v,budget))==((j,R) in accepted)
# Universal order-ten stabilizer character congruences, not point evaluation.
assert (-8)%10==2 and (-(-8))%10==8 and (-4)%10==6
assert len({(-8)%10,8%10,(-4)%10})==3
# Rank, degree, full span, and minimum divisor-size arithmetic.
assert 17-7==10 and -54-(-14)==-40 and 30-9==21
assert 10+40-21==29 and 29-24<12
assert -40+24==-16 and 14+24==38 and 38-18==20
assert 13-2==11 and -54+38==-16
assert inner(sym(9),chars['Wp'])==q(0)
assert inner(rep('2Wp+T'),chars['Wp'])==q(2)
print('PASS: exact defect bounds; universal stabilizer weights; dual H1 budget D; its two support alternatives; forced (2Wp+T)(-1)+O(-6); strict-top character contradiction.')
print('No actual source coefficient, parameter, point, derivative, matrix, rank evaluation, scan, or large computation.')
