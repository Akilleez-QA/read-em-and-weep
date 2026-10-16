"""Independent symbolic jet audit; abstract model only, no physical sources."""
import runpy
from pathlib import Path
import sympy as s
m=runpy.run_path(str(Path(__file__).with_name('test_owned_denominator_complex.py')))
bases, Ds=m['bases'], m['Ds']
# Truncate at (x^2,y): each numerator keeps its constant and x coefficients.
def quotient(q):
    from itertools import combinations
    targets=[(I,(a,0)) for I in combinations(range(4),q+1) for a in range(2)]
    Q=s.zeros(len(targets),len(bases[q]))
    lookup={b:i for i,b in enumerate(targets)}
    for j,b in enumerate(bases[q]):
        if b in lookup: Q[lookup[b],j]=1
    return Q,targets
qs=[quotient(q) for q in range(3)]
# In this jet ring only d_0=1 survives; all other denominators vanish.
def jd(q):
    source,target=qs[q][1],qs[q+1][1]
    out=s.zeros(len(target),len(source)); lookup={b:i for i,b in enumerate(target)}
    for col,(I,ex) in enumerate(source):
        if 0 not in I:
            J=(0,)+I; out[lookup[(J,ex)],col]=1
    return out
JD0,JD1=jd(0),jd(1)
assert qs[1][0]*Ds[0]==JD0*qs[0][0]
assert qs[2][0]*Ds[1]==JD1*qs[1][0]
eta=s.zeros(len(bases[2]),1)
eta[bases[2].index(((0,1,2),(3,0)))]=1
e=Ds[1].T*eta
assert Ds[0].T*e==s.zeros(len(bases[0]),1)
eJ=s.zeros(len(qs[1][1]),1)
eJ[qs[1][1].index(((0,1),(1,0)))]=1
assert qs[1][0].T*eJ==e
assert JD0.T*eJ!=s.zeros(len(qs[0][1]),1)
assert qs[0][0].rank()==4 and qs[0][0].rows==8
# At order zero q0 is onto, but the same e does not factor through q1.
Qconstant=qs[1][0][::2,:]
w=s.zeros(len(bases[1]),1); w[bases[1].index(((0,1),(1,0)))]=1
assert Qconstant*w==s.zeros(Qconstant.rows,1)
assert (e.T*w)[0]==1
print('PASS: chain compatibility, global boundary annihilation, exact e factorization; missing q0 surjectivity prevents jet closedness.')
print('PASS: order-zero q0 is onto, but actual e factorization fails.')
