"""Independent finite bilinear control. Invented arrays only; no source reads."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import json
import resource

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('review_omega', HERE/'prepare_omega.py')
P=importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)
E=P.E

def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def bracket(a,b):
    ab,ba=mul(a,b),mul(b,a)
    return [[ab[i][j]-ba[i][j] for j in range(2)] for i in range(2)]

def main():
    resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
    resource.setrlimit(resource.RLIMIT_CPU,(15,15))
    basis=(((1,0),(0,-1)),((0,1),(0,0)),((0,0),(1,0)))
    signs=(1,-1,-1,1)
    total=0
    for jr in range(4):
        for hr in range(4):
            for jb in basis:
                for hb in basis:
                    m=E.Meter()
                    zero=lambda:[[E.Rat(m,0) for _ in range(2)] for _ in range(2)]
                    H,J=[zero() for _ in range(4)],[zero() for _ in range(4)]
                    H[hr]=[[E.Rat(m,v) for v in row] for row in hb]
                    J[jr]=[[E.Rat(m,v) for v in row] for row in jb]
                    omega,C,skew=P.omega_and_gram(H,J)
                    factor=F(signs[jr],8) if jr+hr==3 else F(0)
                    expected=[[factor*v for v in row] for row in bracket(jb,hb)]
                    actual=[[F(v.n,v.d) for v in row] for row in omega]
                    if actual!=expected:
                        raise RuntimeError('bilinear basis mismatch')
                    if (all(v.is_zero() for row in omega for v in row)
                        != all(v.is_zero() for v in skew)):
                        raise RuntimeError('three-skew equivalence mismatch')
                    total+=1
    print(json.dumps(dict(status='PASS',basis_pairs=total,actual_source_evaluated=False,
                         actual_source_reads=False,physical_entrypoint_invoked=False)))

if __name__=='__main__':
    main()
