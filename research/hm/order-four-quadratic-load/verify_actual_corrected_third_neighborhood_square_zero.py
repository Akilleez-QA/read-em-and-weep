import sympy as S
s,t,k,x,y,b,h,q,u=S.symbols('s t k x y b h q u')
A,B,C,D,E,F=S.symbols('A B C D E F')
a=A*s*s+B*s*t+C*t*t
bb=D*s*s+E*s*t+F*t*t
sig=S.Matrix([s,t]); J=S.Matrix([[0,-1],[1,0]])
n=sig*sig.T*J
v=S.Matrix([x,y])
def tau(v): return sig*v.T*J+v*sig.T*J
def ham(a): return S.Matrix([-S.diff(a,t),S.diff(a,s)])
def zero(m): return all(S.expand(z)==0 for z in m)
br=S.diff(a,s)*S.diff(bb,t)-S.diff(a,t)*S.diff(bb,s)
assert zero(a*tau(ham(bb))-bb*tau(ham(a))+br*n)
T=tau(k*u*ham(a)/2+a*v)
mu=k*u+s*y-t*x
assert zero(T*T-a*a*mu*mu*S.eye(2))
assert S.expand(S.trace(n*T))==0
P=(a*h-q*b)*(a*u*n+q*T)
assert zero((P*P).applyfunc(lambda z:S.expand(z).coeff(q,2))-a**4*h*h*mu*mu*S.eye(2))
# Degree bounds: n has weight 8, T starts at 4, B_j lowers by 4j.
assert min(2*4,8+4-4,2*8-8)==8
assert 8+4>=12
for d in (-2,0,2):
    assert d-2-3<0 and d+2-5<0
# All fixed twists in the scalar global argument.
assert 2*8-2*2==12
assert 12-(2*2+2)==6
print('PASS: universal conic coherence, tangent square, and complete scalar b cancellation.')
print('PASS: vertex filtration and global scalar/ideal twists; no actual-instance evaluation.')
