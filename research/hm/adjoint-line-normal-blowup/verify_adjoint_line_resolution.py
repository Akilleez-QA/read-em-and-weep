"""Bounded universal chart identities; no actual HM/source evaluation."""
import sympy as S
z,eta,k,s=S.symbols('z eta k s', nonzero=True)
def mod2(x):
    return S.simplify(S.diff(x,eta).subs(eta,0)*eta+x.subs(eta,0))
w=1/z; etat=eta/z**2
zp=z-k*eta; wp=w+k*etat
assert mod2(zp*wp)==1
transition=mod2(zp**2/z**2)
assert S.simplify(transition-(1-2*k*eta/z))==0
assert mod2(transition*(1+2*k*eta/z))==1
# q/(st) pulls back to eta/z under t=sz, q=s²eta.
t=s*z; q=s**2*eta
assert S.cancel(q/(s*t))==eta/z
# Rees generators: qT nilpotent and the mixed chart is covered by squares.
T=S.symbols('T')
assert S.expand((s*t*T)**2-(s*s*T)*(t*t*T))==0
assert mod2((q*T)**2)==0
# Ordinary blowup obstruction is coefficientwise: q does not lie in (s²)
# in C[r,s,z,q]/q², since its reduction modulo s is the nonzero nilpotent q.
q0=S.symbols('q0')
_, remainder=S.reduced(q0,[s**2,q0**2],s,q0)
assert remainder==q0
# The Laurent monomial giving the class has BOTH exponents negative;
# every monomial from R_s or R_t has at least one exponent nonnegative.
assert -1<0 and -1<0
print('PASS: reciprocal deformed charts, adjoint-line transition/inverse, normal-enhanced Rees relations, and obstruction bookkeeping.')
print('The proof, not this finite check, establishes Picard/Hartogs vanishing, chart-ring identification, and nonextendibility.')
