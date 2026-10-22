#!/usr/bin/env python3
"""Universal character/splitting certificate, never actual coefficient or map tests."""
from pathlib import Path
from itertools import product
import contextlib, io, runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    b=runpy.run_path(str(ROOT/'verify_extremal_31_five_quotient_section_envelopes.py'))
for k in ('va','vs','vm','sym','reps','effective','euler','sections','vec','mu','profiles'):
    globals()[k]=b[k]
zero=vs(0,reps['one'])
sub=lambda x,y:va(x,vs(-1,y))
one,W,Wp,A,V,P,D,S4,T=[reps[n] for n in ('one','W','Wp','A','V','P','D','S','T')]
def hom(C,j,B,t):return mu(vm(C,vm(B,sections(j-t))),one)
chi3=sub(T,S4)
chi4=va(vs(-1,A),vs(2,V),vs(2,P),D)
assert sub(b['U'],va(sym(9),Wp))==chi3
assert va(sym(7),sym(5))==va(Wp,vs(2,T))
for _,_,blocks in profiles:
    assert sub(va(*[vm(C,euler(4-j)) for j,C in blocks]),va(sym(10),vm(Wp,W)))==chi4
# Rank 14, degree -54, and all degrees <=-2 give j<=28.
odd={'W','Wp','S','T'}
allowed=[]
for j in range(5,29):
    for name,C in reps.items():
        if (j%2==1)!=(name in odd):continue
        h=vm(C,sym(j-5))
        if effective(sub(va(Wp,T,S4),h)):allowed.append((j,name,h))
assert [(j,n) for j,n,h in allowed]==[(5,'Wp'),(5,'S'),(5,'T'),(6,'V'),(6,'P'),(6,'D'),(7,'Wp'),(8,'one'),(8,'V'),(9,'W'),(9,'Wp'),(10,'one'),(12,'one'),(14,'one')]
def tails(rem,start=0,blocks=()):
    if rem==zero:
        yield blocks
        return
    for i in range(start,len(allowed)):
        j,name,h=allowed[i]
        if effective(sub(rem,h)):
            yield from tails(sub(rem,h),i,blocks+((j,name),))
all_positive=[]; low_survivors=[]
for a,t in product(range(2),range(1,3)):
    X=va(vs(a,Wp),vs(t,T))
    for tail in tails(sub(X,chi3)):
        for v,s in product(range(2),repeat=2):
            R2=va(vs(v,V),vs(s,P))
            R3=sub(X,vm(R2,W))
            if not effective(R3):continue
            R4=va(chi4,vs(-1,vm(R2,A)),vs(-1,vm(R3,W)),*[vs(-1,vm(reps[n],euler(4-j))) for j,n in tail])
            if not effective(R4):continue
            blocks=[(2,R2),(3,R3),(4,R4)]+[(j,reps[n]) for j,n in tail]
            dim=b['prior']['dimension']
            assert sum(dim(C) for j,C in blocks)==14
            assert sum(j*dim(C) for j,C in blocks)==54
            record=(a,t,v,s,tail)
            all_positive.append(record)
            if any(hom(C,j,Wp,5) for j,C in blocks):
                low_survivors.append(record)
                assert [(j,n) for j,n in tail if hom(reps[n],j,Wp,5)]==[(5,'Wp')]
                assert hom(Wp,5,one,-4)==0
                if t==1:
                    assert R4==va(R2,V)
                else:
                    assert R4==sub(R2,P)
expected=[(1,1,v,s,((5,'Wp'),(8,'one'))) for v,s in ((0,0),(0,1),(1,0))]
expected += [(1,2,v,1,tail) for tail in (((5,'Wp'),(8,'one'),(10,'one')),((5,'Wp'),(9,'W'))) for v in (0,1)]
assert len(all_positive)==13
assert sorted(low_survivors)==sorted(expected)
# Evaluation lemmas: invariant gcd degrees 6 or 7 are below minimum orbit 12.
assert vm(V,A)==va(P,D)
assert sub(vm(V,S4),sym(9))==Wp
assert vm(P,W)==va(Wp,T)==list(sym(7))
assert sub(vm(P,A),sym(8))==V
assert Wp!=W
# Nontrivial extensions: Euler sequences, and the no-lift argument.
assert hom(Wp,3,V,2)==0
assert hom(Wp,3,one,-4)==1
assert mu(vm(Wp,Wp),one)==1
assert vm(Wp,W)==P
assert hom(V,4,one,-4)==0
assert list(sym(6))==va(V,P)
assert list(sym(5))==T
# Universal final kernel shapes, repeated V coefficients are left explicit.
actual_kernels=[[(4,va(vs(2,V),P)),(8,one)],
                [(3,T),(4,V),(8,one),(10,one)],
                [(3,T),(4,V),(9,W)]]
for blocks in actual_kernels:
    assert all(hom(C,j,Wp,7)==0 for j,C in blocks)
assert vm(Wp,S4)==va(V,D)
assert vm(Wp,A)==T
# Obstruction line degrees for every lifted remaining high map.
for kernel_j,source_js in [(4,(4,8)),(4,(3,8,9,10)),(3,(4,8,9,10))]:
    assert all(j-kernel_j>=-1 for j in source_js)
# The two exceptional extensions are governed by H1(O(-2)) of dimension 1.
assert euler(-2)==vs(-1,one)
print('PASS: complete degree-28 tail exhaustion gives 13 genuine K splittings.')
print('PASS: six have no low map; the remaining seven are exactly families A/B/C.')
print('PASS: Euler/evaluation/extension characters and all required lifts checked.')
print('PASS: all three possible actual K2 shapes have no map to Wprime O(-7).')
print('CONCLUSION with companion sheaf proof: (n,e)=(8,4) is excluded.')
print('SF >= 3 and positive-square rank >= 27 remain unchanged.')
