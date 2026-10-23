"""Exact sparse coefficient arithmetic for the two independent quadratic gates.

No curve division, specialization or geometric denominator is introduced.
The physical scale theta cancels in the physical harmonic projector.
"""
import sympy as s
from universal_laurent_lex_module import sparse_laurent, sparse_expression

def _project(poly,indices,pair,lap):
    """Project homogeneous quadratic monomials, over the unchanged coefficient ring."""
    out={}; indices=tuple(indices)
    assert sum(lap)==6
    def add(m,c):
        value=out.get(m,s.S.Zero)+c
        if value: out[m]=value
        elif m in out: del out[m]
    for mon,c in poly.items():
        powers=tuple(mon[i] for i in indices)
        assert sum(powers)==2 and min(powers)>=0
        add(mon,c)
        if powers in pair:
            scale=-s.Rational(lap[pair.index(powers)],6)*c
            for target in pair:
                new=list(mon)
                for i,power in zip(indices,target):new[i]=power
                add(tuple(new),scale)
    return out

def physical_harmonic_sparse(poly,variables,x,y,z):
    """1-(xy+z²)(4∂xy+∂z²)/6 on positive degree two."""
    return _project(poly,[variables.index(v) for v in (x,y,z)],
                    ((1,1,0),(0,0,2)),(4,2))

def parameter_harmonic_sparse(poly,variables,h,k,l):
    """1-(h²+kl)(∂h²+4∂kl)/6 on parameter degree two."""
    return _project(poly,[variables.index(v) for v in (h,k,l)],
                    ((2,0,0),(0,1,1)),(2,4))

def physical_trace_quotient_sparse(poly,variables,x,y,z,theta):
    """Delta_q/6 on positive degree two, retaining the physical theta factor."""
    ids=[variables.index(v) for v in (x,y,z)]; ti=variables.index(theta)
    out={}; weights={(1,1,0):4,(0,0,2):2}
    for mon,c in poly.items():
        powers=tuple(mon[i] for i in ids)
        assert sum(powers)==2
        if powers not in weights:continue
        new=list(mon)
        for i in ids:new[i]=0
        new[ti]+=1;key=tuple(new)
        out[key]=out.get(key,s.S.Zero)+s.Rational(weights[powers],6)*c
    return {m:c for m,c in out.items() if c}

def affine_coefficient_rows(poly,actual,parameters):
    """Complete coefficient equations, with no actual coefficient assignment."""
    n=len(actual);rows={}
    for mon,c in poly.items():
        op=mon[n:]
        assert len(op)==len(parameters) and sum(op)<=1 and min(op,default=0)>=0
        value=s.S.One if not sum(op) else parameters[op.index(1)]
        key=mon[:n]
        rows[key]=rows.get(key,s.S.Zero)+c*value
    return {m:s.expand(c) for m,c in rows.items() if s.expand(c)!=0}

if __name__=='__main__':
    x,y,z,h,k,l=s.symbols('x y z h k l')
    theta=s.symbols('theta',nonzero=True)
    c=s.symbols('free0:36')
    vm=[x*x,x*y,x*z,y*y,y*z,z*z]
    dm=[h*h,h*k,h*l,k*k,k*l,l*l]
    p=sum(c[6*i+j]*v*d for i,v in enumerate(vm) for j,d in enumerate(dm))
    variables=[x,y,z,h,k,l]+list(c)
    raw=sparse_laurent(p,variables)
    vproj=physical_harmonic_sparse(raw,variables,x,y,z)
    both=parameter_harmonic_sparse(vproj,variables,h,k,l)
    other=physical_harmonic_sparse(parameter_harmonic_sparse(raw,variables,h,k,l),variables,x,y,z)
    assert both==other
    q=(x*y+z*z)/theta
    lapq=lambda e:theta*(4*s.diff(e,x,y)+s.diff(e,z,2))
    lapd=lambda e:s.diff(e,h,2)+4*s.diff(e,k,l)
    direct=p-q*lapq(p)/6
    direct=s.expand(direct-(h*h+k*l)*lapd(direct)/6)
    assert s.expand(sparse_expression(both,variables)-direct)==0
    assert parameter_harmonic_sparse(both,variables,h,k,l)==both
    assert physical_harmonic_sparse(both,variables,x,y,z)==both
    rows=affine_coefficient_rows(both,variables[:6],list(c))
    assert s.expand(sum(value*s.Mul(*(v**e for v,e in zip(variables[:6],m)))
                        for m,value in rows.items())-direct)==0
    print('PASS: all36 free coefficients; commuting physical/parameter Fischer projections, exact reconstruction, idempotence and affine extraction.')
