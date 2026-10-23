"""Pinned representation matrix, with every plane coordinate left formal.
Never imports or runs the historical input script; reads only its P6 literal.
"""
from pathlib import Path
import json
import sympy as s
from math import comb
ROOT=Path(__file__).resolve().parent

def build(check):
    r=s.sqrt(5)
    line='P6=s.Matrix([[r,0,1,0,-r/3,0,5],[0,r/3,0,-1,0,-r,0],[0,-r,0,-1,0,r/3,0],[5,0,-r/3,0,1,0,r]])'
    check('pinned P6 literal retained',line in (ROOT/'inputs/universal-symbols.md').read_text().splitlines())
    P=s.Matrix([[r,0,1,0,-r/3,0,5],[0,r/3,0,-1,0,-r,0],[0,-r,0,-1,0,r/3,0],[5,0,-r/3,0,1,0,r]])
    x,y,p,q,t=s.symbols('x y p q t')
    a=p*x*x+q*x*y+t*y*y
    cv=lambda f:s.Matrix([s.Poly(s.expand(f),x,y).coeff_monomial(x**(6-i)*y**i) for i in range(7)])
    C=s.Matrix.hstack(*[P*cv(a*x**(4-i)*y**i) for i in range(5)])
    cubic=P*cv(a**3)
    J=s.zeros(7)
    for i in range(7):J[i,6-i]=s.Rational((-1)**i,comb(6,i))
    dual=(P*J.inv()*P.T).applyfunc(s.simplify)
    check('quotient apolar form nondegenerate',s.simplify(dual.det())!=0)
    G=dual.inv().applyfunc(s.simplify)
    check('quotient pairing symmetric',G==G.T)
    check('quotient pairing inverse',(G*dual).applyfunc(s.simplify)==s.eye(4))
    k=s.Matrix([(-1)**j*s.expand(C[:,[i for i in range(5) if i!=j]].det(method='berkowitz')) for j in range(5)])
    psi=(cubic.T*G*C).applyfunc(s.expand)
    R=(k*psi).applyfunc(s.expand)
    for i,v in enumerate(C*k):check(f'pinned cofactor identity{i}',s.expand(v)==0)
    check('pinned quartic naturality',s.expand((psi*k)[0])==0)
    check('pinned cubic nonzero',any(v!=0 for v in cubic))
    check('pinned octic nonzero',any(v!=0 for v in R))
    check('explicit q8 extraction denominator',s.Poly(R[0,0],p,q,t).coeff_monomial(q**8)==-s.Rational(1,27))
    gauge=s.symbols('g0:36')
    monomials=[p**i*q**j*t**(7-i-j) for i in range(8) for j in range(8-i)]
    check('q8 functional kills entire degree7 gauge',s.Poly(p*sum(g*m for g,m in zip(gauge,monomials)),p,q,t).coeff_monomial(q**8)==0)
    for i,v in enumerate(R):check(f'pinned homogeneous octic{i}',v==0 or s.Poly(v,p,q,t).total_degree()==8 and all(sum(m)==8 for m in s.Poly(v,p,q,t).monoms()))
    from scalar_extraction import quotient_remainder,extract_scalar
    # Dehomogenization p=1 is the formal coordinate chart, not a selected
    # point. q and t remain algebraically independent throughout.
    chart=R.subs(p,1);Q=quotient_remainder(q,t)
    quotient=(Q*chart).applyfunc(s.expand)
    check('pinned quotient generator nonzero',any(v!=0 for v in quotient))
    alpha=s.symbols('alpha')
    B=s.Matrix([[1,0,0],[q,1,0],[t,q,1],[0,t,q],[0,0,t]])
    U=s.Matrix(3,5,s.symbols('u0:15'))
    value,pivot=extract_scalar(alpha*chart+B*U,chart,q,t)
    check('pinned gauge extraction certificate',s.simplify(value-alpha)==0)
    def coefficients(expr):
        return [{'powers':list(m),'coefficient':str(s.simplify(v))} for m,v in s.Poly(expr,p,q,t).terms() if v!=0]
    data={'kind':'authenticated universal representation matrix; no HM instance data',
      'plane_coordinates':['p','q','t'],'coefficient_field':'Q(sqrt(5))',
      'P6':[[str(v) for v in P.row(i)] for i in range(4)],
      'quotient_pairing':[[str(v) for v in G.row(i)] for i in range(4)],
      'dual_pairing_determinant':str(s.simplify(dual.det())),
      'kappa':[coefficients(v) for v in k],
      'psi':[coefficients(v) for v in psi],
      'R':[[coefficients(R[i,j]) for j in range(5)] for i in range(5)],
      'extraction_pivot':{'entry':list(pivot['entry']),'monomial_q_t':list(pivot['monomial']),'denominator':str(pivot['denominator'])},
      'actual_internal_symbol_supplied':False,'actual_scalar_evaluated':False}
    (ROOT/'PINNED-OCTIC-MATRIX.json').write_text(json.dumps(data,indent=2)+'\n')
    return data['extraction_pivot']
