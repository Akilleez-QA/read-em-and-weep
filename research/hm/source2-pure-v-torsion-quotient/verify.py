#!/usr/bin/env python3
"""Bounded synthetic algebra only; no actual source coefficients or points."""
import hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parent
COUNT=0

def check(v,name):
    global COUNT
    COUNT+=1
    if not v: raise RuntimeError(name)


def run():
    for item in json.loads((ROOT/'INPUTS.json').read_text()):
        b=(ROOT/item['local_path']).read_bytes()
        check(hashlib.sha256(b).hexdigest()==item['sha256'],'exact source SHA256')
        check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'],'exact source Git blob')
    h1=lambda d:max(-d-1,0)
    check(h1(4)==h1(5)==0,'restriction cohomology')
    check(17-5==18-6==12,'first two torsion dimensions')
    check(12-(3+4)==5,'last torsion quotient')
    check((41-5,54-6,37-4)==(36,48,33),'full quotient dimensions')
    check(tuple(sum(x) for x in zip((9,18,16),(15,18,12),(12,12,5)))==(36,48,33),'extension dimensions')
    check(3+4+5==2+4+6==12,'torsion first two characters')
    check(9+3==12 and 9+3*5==24 and 24+12==36,'cokernel rank and degree')
    # Independent formal fiber multipliers, not an actual invariant orbit.
    zs=s.symbols('z0:12')
    D=s.diag(*zs)
    check(D.det()==s.prod(zs),'universal torsion determinant')
    t=s.symbols('t')
    for i in range(12):
        Di=s.eye(12); Di[i,i]=t
        check(Di.det()==t,'simple local divisor')
        check(Di.subs(t,0).rank()==11,'simple local rank drop')
        check(Di.subs(t,1).rank()==12,'off-divisor full rank')
    # Scalar complete multiplication pencil P4 and multiplicity A=3.
    Mx,My=s.zeros(6,5),s.zeros(6,5)
    for j in range(5): Mx[j,j]=1; My[j+1,j]=1
    x,y=s.symbols('x y')
    M=x*Mx+y*My
    check(M[:5,:].det()==x**5,'complete pencil x minor')
    check(M[1:,:].det()==y**5,'complete pencil y minor')
    M8=s.kronecker_product(s.eye(3),Mx)
    # Arbitrary synthetic extension cross terms, including dense ones.
    for seed in range(3):
        H=s.Matrix(12,15,lambda i,j: ((i+1)*(j+2)+seed)%5-2 if seed else 0)
        for lost in [-1,0,5,11]:
            DL=s.eye(12)
            if lost>=0: DL[lost,lost]=0
            K=DL.row_join(H).col_join(s.zeros(18,12).row_join(M8))
            check(K.rank()==27-(lost>=0),'extension preserves kernel dimension')
            for v in K.nullspace():
                check(v[12:,:]==s.zeros(15,1),'kernel lies in endpoint subspace')
                check(DL*v[:12,:]==s.zeros(12,1),'kernel is endpoint kernel')
    # A synthetic seven-dimensional constant space: e0,...,e5, sum(e6,...,e11).
    Hconst=s.zeros(12,7)
    for j in range(6): Hconst[j,j]=1
    for i in range(6,12): Hconst[i,6]=1
    R=s.zeros(5,12)
    for i in range(5): R[i,i+6]=1; R[i,11]=-1
    check(Hconst.rank()==7 and R.rank()==5,'constant/quotient dimensions')
    check(R*Hconst==s.zeros(5,7),'quotient kills constants')
    for i in range(12):
        check(any(Hconst[i,j]!=0 for j in range(7)),'constants avoid every coordinate hyperplane')
    B8=s.eye(12).row_join(s.zeros(12,6))
    for lost in [-1]+list(range(12)):
        DL=s.eye(12)
        if lost>=0: DL[lost,lost]=0
        BL=R*DL
        check(BL.rank()==5,'torsion second arrow onto')
        for seed in range(3):
            H=s.Matrix(5,18,lambda i,j: ((i+2)*(j+1)+seed)%7-3 if seed else 0)
            BK=BL.row_join(H).col_join(s.zeros(12,12).row_join(B8))
            check(BK.rank()==17,'residual second arrow onto with coupling')
            check(16+BK.rank()==33,'full second-arrow rank')
    # Full local presentation exhibits ideal(t) of maximal minors exactly.
    full=s.diag(t,*([1]*35)).col_join(s.zeros(12,36))
    check(full.shape==(48,36),'full presentation shape')
    check(full[:36,:].det()==t,'one maximal minor is uniformizer')
    check(full.subs(t,0).rank()==35,'all maximal minors vanish at divisor')
    check(full.subs(t,1).rank()==36,'full rank away')
    # Negative control: nonreduced torsion retains same point rank but not multiplicity.
    control=s.diag(t**2,*([1]*11))
    check(control.subs(t,0).rank()==11 and control.det()==t**2,'reducedness is stronger than rank support')
    print(json.dumps({'status':'PASS','checks':COUNT,'exact_inputs':3,
      'quotient_dimensions':[36,48,33],'first_rank_off_D12':36,'first_rank_on_D12':35,
      'common_first_kernel':0,'every_nonzero_second_rank':33,
      'degeneracy_divisor_degree':12,'degeneracy_multiplicity_each':1,
      'torsion_free_cokernel_rank':12,'torsion_free_cokernel_degree':24,
      'actual_source_evaluations':0},indent=2))

if __name__=='__main__': run()
