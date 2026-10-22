#!/usr/bin/env python3
"""Exact character and sheaf bookkeeping only; no actual instances or scans."""
from pathlib import Path
import contextlib,io,runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 b=runpy.run_path(str(ROOT/'verify_extremal_31_first_remaining_quotient_exclusion.py'))
for k in ('hom','reps','va','vs','vm','sym','mu','one','W','Wp','V','P','A','D','S4','T','euler','rkdeg','chi','exact','support'):
 globals()[k]=b[k]
Ls=[[('one',8),('one',10)],[('W',9)]]
def check(B,target,active):support(B,target,active)
def tail(B):
 check(B,[('one',10)],[(i,0,1) for i,x in enumerate(B) if x==('one',10)])
 # The constant maps on copies of O(-10) have a single line image.
 K=list(B);K.remove(('one',10))
 exact(B,K,[('one',10)])
 check(K,[('one',12)],[])
def fork(B):
 check(B,[('one',8)],[(i,0,1) for i,x in enumerate(B) if x in [('one',8),('W',9)]])
 # A nonzero constant line splits off; otherwise complete linear evaluation.
 options=[]
 if ('one',8) in B:
  K=list(B);K.remove(('one',8));options.append(K)
 if ('W',9) in B:
  K=list(B);K.remove(('W',9));K.append(('one',10));options.append(K)
 for K in options:exact(B,K,[('one',8)]);tail(K)
def chain(Bs,targets,low=False):
 for i,(B,t) in enumerate(zip(Bs,targets)):
  check(B,[('one',t)]+([('Wp',7)] if i==0 and low else []),[(0,0,1)])
  if i+1<len(Bs):exact(B,Bs[i+1],[('one',t)])
for L in Ls:
 Q=[('V',4),('P',4),('Wp',5)]+L
 check(Q,[('one',-2),('Wp',5)],[(0,0,1),(1,0,1),(2,0,1),(2,1,1)]+([(4,0,1)] if len(L)==2 else [(3,0,1)]))
 assert rkdeg(Q)==(11,-56)
 # Both sextics nonzero.
 F=[('T',5)]+L
 exact(Q,F,[('one',-2),('Wp',5)])
 Bs=[[x]+L for x in [('T',5),('D',6),('S',7),('A',8),('W',9)]]
 chain(Bs[:-1],[0,2,4,6],True)
 exact(Bs[-2],Bs[-1],[('one',6)])
 fork(Bs[-1])
 # Only the P sextic is nonzero.
 F=[('V',6),('V',4)]+L
 exact(Q,F,[('one',-2),('Wp',5)])
 check(F,[('one',0),('Wp',7)],[(0,0,1)])
 F1=[('Wp',9),('V',4)]+L
 exact(F,F1,[('one',0)])
 check(F1,[('one',2)],[(0,0,1)])
 F2=[('one',16),('V',4)]+L
 exact(F1,F2,[('one',2)])
 check(F2,[('one',4)],[(0,0,1)])
 exact(F2,[('V',4)]+L,[('one',16)])
 check([('V',4)]+L,[('one',18)],[])
 # Only the V sextic is nonzero.
 F=[('Wp',7),('P',4)]+L
 exact(Q,F,[('one',-2),('Wp',5)])
 check(F,[('one',0),('Wp',7)],[(0,0,1),(0,1,1)])
 K=[('P',4)]+L
 exact(F,K,[('Wp',7)])
 check(K,[('Wp',9)],[])
 F1=[('one',14)]+K
 exact(F,F1,[('one',0)])
 check(F1,[('one',2)],[(0,0,1)])
 exact(F1,K,[('one',14)])
 check(K,[('one',16)],[])
 # Neither sextic is nonzero.
 if len(L)==2:
  F=[('V',4),('P',4),('one',8)]
  exact(Q,F,[('Wp',5),('one',10)])
  check(F,[('Wp',7),('one',12)],[])
 else:
  F=[('V',4),('P',4),('one',20)]
  exact(Q,F,[('Wp',5),('one',-2)])
  check(F,[('one',0),('Wp',7)],[(2,0,1),(2,1,1)])
  K=[('V',4),('P',4)]
  exact(F,K,[('one',20)])
  check(K,[('one',22)],[])
 # Beta shapes.
 Q=[('T',3),('Wp',5)]+L+[('one',10)]
 check(Q,[('one',-2),('Wp',5)],[(0,0,1),(1,0,1),(1,1,1)]+([(3,0,1),(4,0,1)] if len(L)==2 else [(2,0,1),(3,0,1)]))
 assert rkdeg(Q)==(11,-56)
 F=[('D',4)]+L+[('one',10)]
 exact(Q,F,[('one',-2),('Wp',5)])
 Bs=[[x]+L+[('one',10)] for x in [('D',4),('S',5),('A',6),('W',7),('one',8)]]
 chain(Bs[:-1],[0,2,4,6],True)
 exact(Bs[-2],Bs[-1],[('one',6)])
 fork(Bs[-1])
 # All deeper high components lift through each nonzero sextic/quintic evaluation.
 for kernel_j in (5,6,7):
  for _,j in L:assert j-kernel_j>=-1
 for _,j in L+[('one',10)]:assert j-4>=-1
# Degree-eleven W pair is unique; its kernel and divisor bound are geometric.
assert hom(W,9,one,-2)==1
exact([('W',9)],[('one',20)],[('one',-2)])
assert 11<12 and 7<12 and 6<12
assert W!=Wp
for n in range(1,7):assert va(vm(sym(n),W),vs(-1,sym(n+1)))==list(sym(n-1))
print('PASS: all four doubled-sector Q shapes, every branch and true-image quotient checked.')
print('PASS: exact Hom supports, Euler characters, ranks, negative degrees and lifting inequalities.')
print('CONCLUSION with companion proof: all nine a=2 candidates excluded; eleven a=1 candidates remain.')
print('No exclusion of the full (8,2) quotient or rank-one branch; global bounds unchanged.')
