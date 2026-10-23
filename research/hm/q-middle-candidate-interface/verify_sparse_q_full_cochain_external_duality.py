"""All-free external Fischer/negative-dual compatibility, no source solve.

Two physical scales times100 independent two-form cochain coefficients,
20 arbitrary eta coefficients and6 external quadratic coefficients remain
formal. The production right-endpoint routine is executed without any
geometric/source constructor, on the larger unrestricted cochain domain.
"""
from itertools import combinations
from universal_sparse_q_orthogonal_c_source_adapter import *

def main():
    record={'divided_left':{}};pairs=list(combinations(range(5),2))
    for j,c in enumerate(COLUMNS):
        terms={}
        for powers,tag in ((CW,5),(INV,6)):
            forms=[]
            for a in range(2):forms.append({I:power(var(tag),1+20*j+10*a+i) for i,I in enumerate(pairs)})
            terms[powers]=forms
        record['divided_left'][c]=pack_scaled(terms)
    eta=[{I:power(var(7),1+10*a+i) for i,I in enumerate(pairs)} for a in range(2)]
    mon=(power(var(10),2),mul(var(10),var(11)),mul(var(10),var(12)),power(var(11),2),mul(var(11),var(12)),power(var(12),2))
    external=add(*(mul(power(var(8),i+1),p) for i,p in enumerate(mon)))
    full=transform_tensors(record,lambda p:mul(external,p))
    right=lambda r:QOrthogonalSourceMap.divided_right_pairing(None,r,eta)
    plain=right(record);actual=right(full)
    assert actual==transform_tensors(plain,lambda p:mul(external,p))
    assert transform_tensors(actual,lapD)==right(transform_tensors(full,lapD))
    assert transform_tensors(actual,projectD)==right(transform_tensors(full,projectD))
    assert any(lapD(unpack_poly(p)) for p in tensor_polys(actual))
    assert all(not lapD(unpack_poly(p)) for p in tensor_polys(transform_tensors(actual,projectD)))
    print('PASS: both physical divided-arrow scales, all200 free cochain coefficients, all20 free eta coefficients and all6 external quadratic coefficients commute with fixed negative-dual pairing, external Laplacian and whole-cochain Fischer projection.',flush=True)
    print('PASS: nonzero right-endpoint trace retained before projection; no source constructor, source solve, coefficient values, point or rank test.',flush=True)
if __name__=='__main__':main()
