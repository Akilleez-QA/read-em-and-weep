"""A fixed field-linear bicubic normal form, cached on geometric monomials.

Only divisor/frame units belong to the base field. Arbitrary H, D, source,
or operator coefficients stay symbolic scalar extensions. No recursive
multivariate Poly.div/rem is used. Each cache entry has independent sparse
and SymPy lex certificates, so coefficient extraction always commutes.
"""
import sympy as s
from verify_true_lex_curve_normal_form_audit import explicit_lex_division

class CachedLexModule:
    def __init__(self, divisor):
        if not isinstance(divisor,s.Poly) or not divisor.domain.is_Field:
            raise TypeError('Supply a nonzero Poly over an exact coefficient field')
        if divisor.is_zero: raise ZeroDivisionError('zero divisor')
        self.divisor=divisor
        self.gens=divisor.gens
        self.field=divisor.domain
        self.leading=divisor.monoms(order='lex')[0]
        self.cache={}

    def basis(self,powers):
        powers=tuple(powers)
        if powers not in self.cache:
            mon=s.Poly.from_dict({powers:self.field.one},self.gens,domain=self.field)
            q,r=explicit_lex_division(mon,self.divisor)
            qq,rr=s.reduced(mon,[self.divisor],*self.gens,domain=self.field,order='lex')
            sq=qq[0] if qq else s.Poly(0,*self.gens,domain=self.field)
            assert q==sq and r==rr
            assert mon==q*self.divisor+r
            assert all(not all(a>=b for a,b in zip(mm,self.leading)) for mm,c in r.terms() if c)
            self.cache[powers]=(q.as_expr(),r.as_expr())
        return self.cache[powers]

    def reduce_expression(self,expression,*,check_reconstruction=True):
        # EX is only a scalar-extension container, never a division domain.
        p=s.Poly(s.expand(expression),*self.gens,domain=s.EX)
        q,r=s.S.Zero,s.S.Zero
        for powers,coefficient in p.terms():
            bq,br=self.basis(powers)
            q+=coefficient*bq;r+=coefficient*br
        q,r=s.expand(q),s.expand(r)
        if check_reconstruction:
            assert s.expand(expression-q*self.divisor.as_expr()-r)==0
        rp=s.Poly(r,*self.gens,domain=s.EX)
        assert all(not all(a>=b for a,b in zip(mm,self.leading)) for mm,c in rp.terms() if c)
        return q,r
