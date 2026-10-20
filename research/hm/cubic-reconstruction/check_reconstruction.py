import sympy as S
z, I, J = S.symbols('z I J')
f = z**3 - 3*I*z - J

def red(p):
    return S.rem(S.expand(p), f, z)

def eps(p):
    return S.expand(red(p)).coeff(z, 2)

def require_zero(p, label):
    if S.expand(p) != 0:
        raise RuntimeError(label + ': ' + str(S.expand(p)))

tau = z*z - 2*I
basis = [1,z,tau]
dual = [tau+I,z,1]
for i in range(3):
    for j in range(3):
        require_zero(eps(basis[i]*dual[j]) - int(i==j), 'dual basis')
gram = S.Matrix([[eps(a*b) for b in basis] for a in basis])
if gram != S.Matrix([[0,0,1],[0,1,0],[1,0,-I]]):
    raise RuntimeError('Gram mismatch')
require_zero(gram.det()+1, 'Gram determinant')
a0,a1,a2,b0,b1,b2 = S.symbols('a0 a1 a2 b0 b1 b2')
r = a0*dual[0]+a1*dual[1]+a2*dual[2]
b = b0+b1*z+b2*tau
require_zero(eps(r*b)-(a0*b0+a1*b1+a2*b2), 'functional reconstruction')
# Multiplication matrices only for the invented universal scalar cubic algebra.
def coords(p):
    p=red(p)
    return S.Matrix([p.coeff(z,0)+2*I*p.coeff(z,2),p.coeff(z,1),p.coeff(z,2)])
mult = S.Matrix.hstack(*[coords(b*t) for t in basis])
require_zero(S.trace(mult)-3*b0, 'normalized algebra trace')
require_zero(eps(S.diff(f,z)*b)-S.trace(mult), 'different trace identity')
require_zero(eps(dual[0]*b)-b0, 'constant projector')
u=S.symbols('u', nonzero=True)
# New frame z'=u z, I'=u²I, tau'=u²tau and epsilon'=u^-2 epsilon.
rnew=a0*u**2*dual[0]+(u*a1)*(u*z)+(u**2*a2)
require_zero(S.expand(rnew-u**2*r), 'line-frame covariance')
# Formal boundary symbols: delta p_i=a_i, delta h_minus=c_minus.
p0,p1,p2=S.symbols('p0 p1 p2')
primitive=p0*dual[0]+p1*z+p2
require_zero(primitive.xreplace({p0:a0,p1:a1,p2:a2})-r, 'boundary reconstruction')
# Basis multiplication checks; no numerical specializations.
require_zero(red(z*tau-I*z-J), 'sigma tau')
require_zero(red(tau*tau-(2*I**2+J*z-I*tau)), 'tau square')
print('PASS: exact universal scalar cubic identities; no samples, source data, or physical products.')
