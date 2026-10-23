"""Exact physical Fischer split on positive cubics, retaining theta."""
import sympy as s
from universal_laurent_lex_module import sparse_add,sparse_multiply

def positive_cubic_fischer(poly,variables,x,y,z,theta):
    ids=[variables.index(v) for v in (x,y,z)];ti=variables.index(theta);quotient={}
    for mm,c in poly.items():
        a,b,d=(mm[i] for i in ids);assert a+b+d==3 and min(a,b,d)>=0
        for shift,factor in [((-1,-1,0),4*a*b),((0,0,-2),d*(d-1))]:
            if not factor:continue
            nn=list(mm)
            for i,k in zip(ids,shift):nn[i]+=k
            nn[ti]+=1;nn=tuple(nn)
            quotient[nn]=quotient.get(nn,s.S.Zero)+c*s.Rational(factor,10)
    quotient={m:c for m,c in quotient.items() if c}
    q={}
    for pp in [(1,1,0),(0,0,2)]:
        nn=[0]*len(variables)
        for i,k in zip(ids,pp):nn[i]=k
        nn[ti]=-1;q[tuple(nn)]=s.S.One
    harmonic=sparse_add(poly,sparse_multiply(q,quotient),-1)
    assert sparse_add(harmonic,sparse_multiply(q,quotient))==poly
    return quotient,harmonic

if __name__=='__main__':
    from universal_laurent_lex_module import sparse_laurent,sparse_expression
    from universal_sparse_double_fischer_rows import parameter_harmonic_sparse
    x,y,z,h,k,l,theta=s.symbols('x y z h k l theta')
    vm=[x**a*y**b*z**(3-a-b) for a in range(4) for b in range(4-a)]
    dm=[h*h,h*k,h*l,k*k,k*l,l*l];c=s.symbols('v0:60')
    e=sum(c[6*i+j]*v*d for i,v in enumerate(vm) for j,d in enumerate(dm))
    vv=[x,y,z,h,k,l,theta]+list(c);pp=sparse_laurent(e,vv)
    quotient,harmonic=positive_cubic_fischer(pp,vv,x,y,z,theta)
    rq=sparse_expression(quotient,vv);hh=sparse_expression(harmonic,vv)
    lap=lambda e:s.expand(theta*(4*s.diff(e,x,y)+s.diff(e,z,2)))
    assert s.expand(rq-lap(e)/10)==0 and lap(hh)==0
    assert s.expand(e-(x*y+z*z)*rq/theta-hh)==0
    _,again=positive_cubic_fischer(harmonic,vv,x,y,z,theta);assert again==harmonic
    dq,dh=positive_cubic_fischer(parameter_harmonic_sparse(pp,vv,h,k,l),vv,x,y,z,theta)
    assert dq==parameter_harmonic_sparse(quotient,vv,h,k,l)
    assert dh==parameter_harmonic_sparse(harmonic,vv,h,k,l)
    print('PASS all60 free cubic/parameter-quadratic coefficients: physical normalization, exact reconstruction, harmonicity, idempotence and commuting parameter projection.')
