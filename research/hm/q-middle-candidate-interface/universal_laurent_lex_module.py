"""Sparse rational-Laurent scalar extension of a certified fixed lex normal form.
Only declared frame units may have negative powers. No coefficient-field
specialization or recursive multivariate remainder is used.
"""
import sympy as s
from universal_cached_lex_module import CachedLexModule

def sparse_laurent(expression,variables,units=()):
    variables=tuple(variables);index={v:i for i,v in enumerate(variables)};allowed=set(units);out={}
    for term in s.Add.make_args(s.expand(expression)):
        scalar,mon=term.as_coeff_Mul()
        if not scalar.is_Rational:raise ValueError('Non-rational scalar')
        powers=[0]*len(variables)
        for base,power in mon.as_powers_dict().items():
            if base==1:continue
            if base not in index or not power.is_Integer:raise ValueError('Not a Laurent monomial: '+str(term))
            if power<0 and base not in allowed:raise ValueError('Undeclared denominator: '+str(base))
            powers[index[base]]=int(power)
        key=tuple(powers);out[key]=out.get(key,s.S.Zero)+scalar
    return {m:c for m,c in out.items() if c}

def sparse_expression(poly,variables):
    return s.Add(*(c*s.Mul(*(v**e for v,e in zip(variables,m) if e)) for m,c in poly.items()))

def sparse_add(a,b,scale=1):
    out=dict(a)
    for m,c in b.items():
        value=out.get(m,s.S.Zero)+scale*c
        if value:out[m]=value
        elif m in out:del out[m]
    return out

def sparse_multiply(a,b):
    out={}
    for m,c in a.items():
        for n,d in b.items():
            key=tuple(x+y for x,y in zip(m,n));out[key]=out.get(key,s.S.Zero)+c*d
    return {m:c for m,c in out.items() if c}

class LaurentLexModule:
    def __init__(self,divisor,coefficient_symbols,units):
        self.normal=CachedLexModule(divisor);self.gens=divisor.gens
        self.coefficients=tuple(coefficient_symbols);self.units=tuple(units)
        if set(self.gens)&set(self.coefficients):raise ValueError('Disjoint geometric/coefficient symbols required')
        if not set(self.units)<=set(self.coefficients):raise ValueError('Units must be coefficient symbols')
        self.variables=self.gens+self.coefficients;self.n=len(self.gens);self.cache={}
        self.divisor=sparse_laurent(divisor.as_expr(),self.variables,self.units)
    def basis(self,powers):
        if powers not in self.cache:
            q,r=self.normal.basis(powers)
            self.cache[powers]=(sparse_laurent(q,self.variables,self.units),sparse_laurent(r,self.variables,self.units))
        return self.cache[powers]
    def reduce_sparse(self,p):
        q={};r={};zero=(0,)*self.n
        for m,c in p.items():
            bq,br=self.basis(m[:self.n]);shift=zero+m[self.n:]
            for source,target in [(bq,q),(br,r)]:
                for n,d in source.items():
                    key=tuple(a+b for a,b in zip(n,shift));target[key]=target.get(key,s.S.Zero)+c*d
        q={m:c for m,c in q.items() if c};r={m:c for m,c in r.items() if c}
        assert sparse_add(sparse_multiply(q,self.divisor),r)==p
        lt=self.normal.leading
        assert all(not all(a>=b for a,b in zip(m[:self.n],lt)) for m in r)
        return q,r
    def reduce_expression(self,expression):
        p=sparse_laurent(expression,self.variables,self.units);q,r=self.reduce_sparse(p)
        return sparse_expression(q,self.variables),sparse_expression(r,self.variables)
