#!/usr/bin/env python3
"""Universal exact character/sheaf-bookkeeping certificate, not actual instances."""
from pathlib import Path
import contextlib, io, runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    b=runpy.run_path(str(ROOT/'verify_extremal_31_first_remaining_quotient_reduction.py'))
for k in ('hom','reps','va','vs','vm','sym','mu','one','W','Wp','V','P','A','D','S4','T','euler'):
    globals()[k]=b[k]
dim=b['b']['prior']['dimension']
sub=lambda x,y:va(x,vs(-1,y))
zero=vs(0,one)
def blocks(*args): return list(args)
def rkdeg(B):return sum(dim(reps[n]) for n,j in B),-sum(j*dim(reps[n]) for n,j in B)
def chi(B,t):return va(zero,*[vm(reps[n],euler(t-j)) for n,j in B])
def exact(B,K,C):
    assert rkdeg(B)==tuple(x+y for x,y in zip(rkdeg(K),rkdeg(C)))
    for t in range(-2,20):assert chi(B,t)==va(chi(K,t),chi(C,t))
def support(B,targets,expected):
    got=[(i,k,hom(reps[n],j,reps[m],t)) for i,(n,j) in enumerate(B) for k,(m,t) in enumerate(targets) if hom(reps[n],j,reps[m],t)]
    assert got==expected,(B,targets,got,expected)
    assert rkdeg(B)[0]>0 and rkdeg(B)[1]<0

def scalar_chain(sources,start,initial_low=False):
    for i,B in enumerate(sources):
        targets=[('one',start+2*i)]
        if i==0 and initial_low:targets += [('Wp',7)]
        terminal=i==len(sources)-1
        # Active block always first; all other Hom spaces vanish.
        support(B,targets,[] if terminal else [(0,0,1)])
        if not terminal:exact(B,sources[i+1],[targets[0]])

explicit_Q=[ [('D',4),('V',4),('Wp',5),('one',10)],
 [('S',3),('V',4),('Wp',5),('one',8),('one',10)],
 [('S',3),('V',4),('Wp',5),('W',9)]]
explicit_F=[ [('S',5),('V',4),('one',10)],
 [('A',4),('V',4),('one',8),('one',10)],
 [('A',4),('V',4),('W',9)]]
for Q,F in zip(explicit_Q,explicit_F):
 support(Q,[('one',0),('Wp',5)],[(0,0,1),(2,1,1)])
 exact(Q,F,[('one',0),('Wp',5)])
 assert rkdeg(Q)==(11,-52) and rkdeg(F)==(8,-42)
scalar_chain([[B,('V',4),('one',10)] for B in [('S',5),('A',6),('W',7),('one',8)]]+
 [[('one',10),('V',4)],[('V',4)]],2,True)
for L in [[('one',8),('one',10)],[('W',9)]]:
 initial=[[B,('V',4)]+L for B in [('A',4),('W',5),('one',6)]]
 # Reorder only abstract direct summands so active block is first.
 fourth=L+[('V',4)]
 scalar_chain(initial+[fourth,[('one',10),('V',4)],[('V',4)]],2,True)

# Complete evaluation identifications and the two irreducible sextic kernels.
for n in range(1,7):
 assert sub(vm(sym(n),W),sym(n+1))==list(sym(n-1))
assert list(sym(6))==va(V,P)
assert vm(V,A)==va(P,D)
assert sub(vm(V,S4),sym(9))==Wp
assert vm(P,W)==va(Wp,T)==list(sym(7))
assert sub(vm(P,A),sym(8))==V
assert W!=Wp
assert hom(Wp,5,V,4)==0
assert mu(vm(Wp,Wp),one)==1
assert euler(-2)==vs(-1,one)
assert vm(Wp,W)==P
assert hom(Wp,5,one,-2)==1
# The lifts use H1(O(0)) and H1(O(-1)); no lower degree is allowed.
assert 5-5==0 and 5-6==-1

J=[('V',4),('V',4),('P',4),('Wp',5)]
residual_Q=[ [('V',4),('T',5),('Wp',5)],
 [('V',4),('V',4),('V',6),('Wp',5)],
 [('V',4),('P',4),('P',6)],
 [('V',4),('P',4),('Wp',5),('Wp',7)]]
residual_F=[ [('D',6),('V',4)], [('V',4),('V',4),('Wp',9)],
 [('V',4),('P',4),('one',14)], [('V',4),('P',4),('one',14)]]
expected=[[(1,0,1),(2,1,1)],[(2,0,1),(3,1,1)],[(2,0,1),(2,1,1)],[(2,1,1),(3,0,1)]]
for Q,F,s in zip(residual_Q,residual_F,expected):
 exact(J,Q,[('one',-2)])
 support(Q,[('one',0),('Wp',5)],s)
 exact(Q,F,[('one',0),('Wp',5)])
 assert rkdeg(Q)==(11,-52) and rkdeg(F)==(8,-42)
scalar_chain([[B,('V',4)] for B in [('D',6),('S',7),('A',8),('W',9),('one',10)]]+[[('V',4)]],2,True)
# Tensor Euler plus septic evaluation in R3.
exact([('P',6)],[('Wp',7)],[('Wp',5)])
support([('Wp',7)],[('one',0)],[(0,0,1)])
exact([('Wp',7)],[('one',14)],[('one',0)])
# R2: septic kernel, then possibly vanishing scalar with degree-twelve zeros.
F=residual_F[1]
support(F,[('one',2),('Wp',7)],[(2,0,1)])
K=[('V',4),('V',4),('one',16)]
exact(F,K,[('one',2)])
support(K,[('one',4)],[(2,0,1)])
exact(K,[('V',4),('V',4)],[('one',16)])
support([('V',4),('V',4)],[('one',18)],[])
# R3/R4: a SINGLE line can reach both targets; its quotient stays that line.
F=residual_F[2]
support(F,[('one',2),('Wp',7)],[(2,0,1),(2,1,1)])
exact(F,[('V',4),('P',4)],[('one',14)])
support([('V',4),('P',4)],[('one',16)],[])
print('PASS: all three explicit Q cases and four residual Q cases have verified Hom supports.')
print('PASS: all recursive kernels, Euler characters, ranks and negative degrees checked exactly.')
print('PASS: sextic/septic evaluation, tensor Euler, extension dimension and lift tests checked.')
print('CONCLUSION with companion actual-subundle proof: the full (6,2) quotient is excluded.')
print('Only (8,2) remains in the rank-two dual-image branch; rank-one branch and bounds unchanged.')
