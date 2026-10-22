"""Exact universal character checks; no actual-instance coefficients or ranks."""
from pathlib import Path
import runpy, contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
 b=runpy.run_path(str(Path(__file__).with_name('verify_extremal_31_rank_one_ten_quotients.py')))
r,va,vs,vm,sy,eu,se,ef,mu,dim=[b[x] for x in ['r','va','vs','vm','sy','eu','se','ef','mu','dim']]
z=b['b']['zero']; U=b['U']
def chi(blocks,t):return va(*[vm(r[R],eu(n+t)) for R,n in blocks])
def sub(a,c):return va(a,vs(-1,c))
def low_blocks(M, target):
 return [(R,j) for j in range(target,dim(M)+5) for R in r
         if ef(sub(M,vm(r[R],sy(j-5)))) and mu(r[R],se(j-target))]
E4=va(vs(3,r['V']),vs(3,r['P']),vs(2,r['D']))
for key,rep,blocks in b['b']['profiles']:
 assert va(*[vm(C,eu(4-j)) for j,C in blocks])==E4
B=b['base'][3]; A0=list(B)+[('one',-10)]; A1=[('one',2),('one',2),('one',-12)]
assert b['margin'](11,B)==va(r['Wp'],vs(2,r['S']),r['T'])
assert sub(U,chi(A0,3))==va(vs(-1,r['Wp']),r['T'])
assert sub(sub(U,chi(A0,3)),chi(A1,3))==z
assert low_blocks(vs(2,r['S']),14)==[]
for B in (b['base'][4],b['base'][6]):
 A0=list(B)+[('one',-10)]; D=[(R,n-2) for R,n in B]; A1=D+[('one',-12)]
 assert b['margin'](11,B)==va(r['Wp'],vs(2,r['S']),vs(2,r['T']))
 assert sub(U,chi(A0,3))==sub(r['T'],r['S'])
 assert chi(D,3)==va(r['Wp'],vs(2,r['T']))
 assert chi([(R,n-1) for R,n in B],0)==va(r['S'],r['T'])
 assert all(mu(vm(r['W'],vm(r[R],se(n+13))),r['one'])==0 for R,n in D)
 assert sub(sub(U,chi(A0,3)),chi(A1,3))==vs(-1,r['S'])
 kp4=va(E4,vs(-1,chi(A0,4)),vs(-1,chi(A1,4)),vs(-1,eu(-10)))
 R=sub(kp4,vm(r['T'],sy(1)))
 assert R==va(vs(-1,r['A']),r['V'],r['P']) and not ef(R)
assert low_blocks(va(vs(2,r['S']),r['T']),14)==[('one',14)]
assert vm(r['W'],sy(8))==va(r['Wp'],r['S'],vs(2,r['T']))
assert list(sy(9))==va(r['S'],r['T'])
assert vm(r['T'],r['W'])==va(r['V'],r['P'],r['D'])
assert all(mu(r['Wp'],sy(n))==0 for n in range(7))
# Defect12 alternative in D=O2+O4.
A0=[('one',4),('one',6),('one',-10)]
A1=[('one',4),('one',-10),('one',-12)]
assert sub(sub(U,chi(A0,3)),chi(A1,3))==va(vs(2,r['T']),vs(-1,r['S']))
# The independent e9 lower-line exclusion.
assert b['margin'](9,b['base'][0])==r['T']
assert list(sy(5))==r['T'] and mu(sy(4),r['one'])==0
# Three additional e9 cases: exact source/kernel characters and low-block obstruction.
for i in (1,2,5):
 B=b['base'][i]; A0=list(B)+[('one',-8)]
 A1=[(R,n-2) for R,n in B]+[('one',-10)]
 Y3=va(U,vs(-1,chi(A0,3)),vs(-1,eu(-7)))
 assert Y3==(va(r['Wp'],r['T']) if i==2 else va(r['S'],r['T']))
 K23=va(U,vs(-1,chi(A0,3)),vs(-1,chi(A1,3)))
 assert K23==(vs(-1,r['S']) if i==2 else z)
 M=va(r['W'],r['S'],r['T']) if i==2 else va(r['W'],r['S'])
 assert low_blocks(M,12)==[]
assert vm(r['W'],sy(4))==va(r['S'],r['T'])
assert mu(sy(7),r['Wp'])==1
print('PASS: all three e11 shapes and four e9 shapes excluded by the accompanying Gauss argument.')
print('Three e9 necessary shapes remain; no complete plateau exclusion or improved rank bound claimed.')
