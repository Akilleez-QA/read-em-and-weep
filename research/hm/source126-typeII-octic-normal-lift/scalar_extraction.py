"""Pure symbolic quotient-gauge extractor; no data fetch or HM evaluation.

Inputs are already dehomogenized 5x5 polynomial matrices on a=x^2+b*x*y+c*y^2.
The caller must supply a fixed nonzero generator R and a candidate lift L.
Returns a scalar only after verifying the entire quotient identity QL=alpha QR.
This module neither constructs nor evaluates an actual internal symbol.
"""
import sympy as s

def quotient_remainder(b,c):
    return s.Matrix([[-b**3+2*b*c,b*b-c,-b,1,0],
                     [-b*b*c+c*c,b*c,-c,0,1]])

def extract_scalar(L,R,b,c):
    if L.shape!=(5,5) or R.shape!=(5,5):
        raise ValueError('Expected two polynomial 5x5 matrices')
    Q=quotient_remainder(b,c)
    T=(Q*R).applyfunc(s.expand);S=(Q*L).applyfunc(s.expand)
    pivot=None
    for i in range(2):
        for j in range(5):
            p=s.Poly(T[i,j],b,c)
            for powers,gamma in p.terms():
                if gamma!=0:
                    pivot=(i,j,powers,gamma)
                    break
            if pivot is not None:break
        if pivot is not None:break
    if pivot is None:raise ValueError('Generator has zero quotient')
    i,j,powers,gamma=pivot
    alpha=s.cancel(s.Poly(S[i,j],b,c).coeff_monomial(powers)/gamma)
    if alpha.has(b,c):raise ValueError('Ratio is not a constant scalar')
    if (S-alpha*T).applyfunc(s.simplify)!=s.zeros(2,5):
        raise ValueError('Candidate quotient is not in the generator line')
    return alpha,{'entry':(i,j),'monomial':powers,'denominator':gamma}
