"""Universal representation/sheaf identities, never an actual-instance computation."""
from pathlib import Path
import runpy,contextlib,io
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):b=runpy.run_path(str(ROOT/'verify_extremal_31_doubled_gauss_exclusion.py'))
globals().update({k:b[k] for k in ('hom','reps','va','vs','vm','sym','mu','one','W','Wp','V','P','A','D','S4','T','euler','rkdeg','chi','exact','support')})
# New evaluations
exact([('T',3)],[('V',4),('Wp',5)],[('one',-4)])
exact([('P',4)],[('Wp',5),('one',10)],[('one',-4)])
assert vm(V,W)==T and vm(Wp,W)==P
assert hom(T,3,one,-4)==1
assert hom(P,4,one,-4)==1
assert hom(W,9,one,-4)==1 and hom(one,8,one,-4)==1
assert hom(W,9,one,8)==1
# J low supports
for L in [[('one',8),('one',10)],[('W',9)]]:
 for B in [[('V',4),('P',4),('P',4)]+L,[('T',3),('P',4)]+L+[('one',10)]]:
  assert rkdeg(B)==(13,-62)
 # No-P low branch quotient and next supports.
for Q in [[('V',4),('P',4),('P',4)],[('T',3),('P',4),('one',10)]]:
 assert all(hom(reps[n],j,W,11)==0 for n,j in Q)
# K high low supports for no leading T/P high after low scalar elimination.
Q=[('T',3),('P',4),('one',10)]
assert all(hom(reps[n],j,Wp,5)==0 for n,j in Q)
# L high degree thirteen equals invariant degree twelve times complete linear pair.
assert hom(W,9,one,8)==hom(W,9,one,-4)==1
assert hom(one,8,one,-4)==1
assert hom(one,10,Wp,3)==hom(W,9,Wp,3)==hom(one,10,W,9)==1
assert hom(one,8,Wp,3)==0
# septic factoring octic
assert hom(P,4,Wp,3)==1
# Extension obstructions, checked in the equivariant category.
def ext(C,j,B,k):
 return 0 if k-j-2<0 else mu(vm(C,vm(B,sym(k-j-2))),one)
assert ext(P,4,one,10)==0
assert ext(T,3,Wp,5)==0
assert ext(Wp,3,Wp,5)==1
assert ext(one,8,one,10)==1
assert ext(W,9,one,10)==0
assert ext(Wp,5,V,4)==0 and ext(one,10,Wp,5)==0
assert ext(Wp,3,V,2)==0
assert hom(Wp,3,V,2)==0
# Every later high/low graph removal has the stated vanishing obstruction.
for n,j in [('P',4),('one',8),('one',10),('W',9)]:
 assert ext(reps[n],j,V,4)==0
 assert ext(reps[n],j,Wp,5)==0
for n,j in [('V',4),('P',4),('one',8),('one',10),('W',9)]:
 assert ext(reps[n],j,P,4)==0
for n,j in [('P',4),('one',8),('one',10),('W',9)]:
 assert ext(reps[n],j,T,3)==0
# All six source rows, counted with the two L choices.
Ls=[[('one',8),('one',10)],[('W',9)]]
KI=[('Wp',3),('V',4),('P',4),('P',4),('one',8)]
rows=[KI]
for L in Ls:
 JA=[('V',4),('P',4),('P',4)]+L
 JB=[('T',3),('P',4)]+L+[('one',10)]
 QA=[('V',4),('P',4),('Wp',5)]+L
 QB=[('T',3),('Wp',5)]+L+[('one',10)]
 Ks=[
  [('Wp',3),('T',3),('P',4)]+L,
  [('P',2),('P',4),('P',4)]+L,
  [('V',2),('Wp',3),('V',4),('P',4)]+L,
  [('V',2),('Wp',3),('T',3)]+L+[('one',10)],
  [('V',2),('P',2),('P',4)]+L+[('one',10)]]
 rows+=Ks
 exact(KI,JA,[('one',-4)])
 exact(Ks[0],JA,[('one',-4)])
 exact(Ks[0],JB,[('one',-4)])
 exact(Ks[1],JA,[('one',-4)])
 exact(Ks[2],JA,[('one',-4)])
 exact(Ks[3],JB,[('one',-4)])
 exact(Ks[4],JB,[('one',-4)])
 exact(JA,QA,[('Wp',3)])
 exact(JB,QB,[('Wp',3)])
 exact(KI,QA,[('one',-4),('Wp',3)])
 exact(Ks[2],QA,[('one',-4),('Wp',3)])
 exact(Ks[3],QB,[('one',-4),('Wp',3)])
 # The generic-rank-two W low branch has actual quotient W(-9).
 if L==[('W',9)]:
  qa=[('V',4),('P',4),('P',4)]
  qb=[('T',3),('P',4),('one',10)]
  exact(JA,qa,[('W',9)])
  exact(JB,qb,[('W',9)])
 # Zero leading high maps retain O(-8), not its saturated image O(4).
 exact(Ks[0],[('T',3),('P',4),('one',10)],[('Wp',3),('one',8)])
exact(KI,[('V',4),('P',4),('P',4)],[('Wp',3),('one',8)])
assert len(rows)==11
for K in rows:assert rkdeg(K)==(14,-58)
# Both degree-minus-two high components are forced and have no low Hom.
for C in (V,P):assert hom(C,2,one,-4)==1 and hom(C,2,Wp,3)==0
# The high cores used in the common lemma have no other low components.
assert hom(T,3,Wp,3)==0
assert hom(Wp,3,Wp,3)==1
assert hom(P,4,Wp,3)==1
# The nonsplit combined V/Wp high kernel is tensor Euler.
exact([('V',2),('Wp',3)],[('P',4)],[('one',-4)])
exact([('P',4)],[('Wp',5)],[('Wp',3)])
print('PASS: eleven single-Wprime source cases and all stated quotient identities.')
print('PASS: low-zero scalar branches, extension spaces, and rank-three contradictions.')
print('Conclusion with the companion proof: the full (8,2) rank-two quotient is excluded.')
print('The rank-one dual-image branch and global bounds remain unchanged.')
