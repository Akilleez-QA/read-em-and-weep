"""Small abstract Koszul cochain test; no physical source inputs."""
from itertools import combinations, product
import json
import sympy as s

# X=P1xP1; F=O(-2,-2); four chart denominator sections
# d_(a,b)=Z_a^2 W_b^2, so every L_v=O(2,2).
vertices=list(product((0,1), repeat=2))
def basis(q):
    deg=2*(q+1)-2
    return [(I,(a,b)) for I in combinations(range(4),q+1)
            for a,b in product(range(deg+1),repeat=2)]
bases=[basis(q) for q in range(4)]
def differential(q):
    target={x:i for i,x in enumerate(bases[q+1])}
    D=s.zeros(len(bases[q+1]),len(bases[q]))
    for col,(I,ex) in enumerate(bases[q]):
        for v in range(4):
            if v in I: continue
            J=tuple(sorted(I+(v,)))
            k=J.index(v)
            a,b=vertices[v]
            row=target[(J,(ex[0]+2*a,ex[1]+2*b))]
            D[row,col]=(-1)**k
    return D
Ds=[differential(q) for q in range(3)]
assert Ds[1]*Ds[0]==s.zeros(len(bases[2]),len(bases[0]))
assert Ds[2]*Ds[1]==s.zeros(len(bases[3]),len(bases[1]))
ranks=[D.rank() for D in Ds]
cohom=[len(bases[0])-ranks[0]]+[len(bases[q])-ranks[q-1]-(ranks[q] if q<3 else 0) for q in range(1,4)]
assert cohom==[0,0,1,0],cohom
# Exact dual factorization from closedness on V0.
eta=s.Matrix([((i*7)%11)-5 for i in range(len(bases[2]))])
e=Ds[1].T*eta
assert Ds[0].T*e==s.zeros(len(bases[0]),1)
assert all((e.T*k)[0]==0 for k in Ds[1].nullspace())
# A tempting numerator truncation of V0 preserves D1D0=0 but destroys H1.
D0clip=Ds[0][:,1:]
assert Ds[1]*D0clip==s.zeros(len(bases[2]),len(bases[0])-1)
clip_h1=len(bases[1])-ranks[1]-D0clip.rank()
assert clip_h1==1
# All old gauge tests can pass while the omitted primitive boundary obstructs eta.
z=Ds[0][:,0]
# The four columns have disjoint monomial supports, so z itself separates them.
bad_e=z
assert D0clip.T*bad_e==s.zeros(3,1)
assert (bad_e.T*z)[0]!=0
assert Ds[1]*z==s.zeros(len(bases[2]),1)
result={'dimensions':[len(b) for b in bases], 'ranks':ranks,'cohomology_dimensions':cohom,
        'clipped_H1':clip_h1,'omitted_boundary_pairing':int((bad_e.T*z)[0]),
        'physical_source_evaluated':False}
print(json.dumps(result,indent=2))
