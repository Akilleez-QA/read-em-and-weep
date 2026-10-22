"""Bounded universal symbolic check; no actual HM instance is selected."""
import sympy as S
s,t,A,B,C,u,k,v1,v2,h,b,x,y,z,r,j,l=S.symbols('s t A B C u k v1 v2 h b x y z r j l')
a=A*s*s+B*s*t+C*t*t
rho=S.Matrix([s,t]); J=S.Matrix([[0,1],[-1,0]])
N=u*rho*rho.T*J
w=k*u*S.Matrix([-S.diff(a,t),S.diff(a,s)])/2+a*S.Matrix([v1,v2])
T=rho*w.T*J+w*rho.T*J
I=S.eye(2)
def zero(M):
    assert all(S.expand(e)==0 for e in M)
zero(N*N)
assert S.expand(S.trace(N*T))==0
c=S.expand((T*T)[0,0]); zero(T*T-c*I)
for e in list(N)+list(T):
    assert all(sum(m)>=2 for m,coef in S.Poly(S.expand(e),s,t).terms() if coef !=0)
assert all(sum(m)>=4 for m,coef in S.Poly(c,s,t).terms() if coef!=0)
L0=a*a*h*N; L1=a*(h*T-b*N); L2=S.Matrix([[x,y],[z,-x]])
K=S.Matrix([[r,j],[l,-r]])
zero(L1*L1-a*a*h*h*c*I)
zero(L0*L2+L2*L0-a*a*h*S.trace(N*L2)*I)
chi=S.trace(L1*L2)
# The residual is exactly the q^2 relation times -a*b.
assert S.expand(chi-a*h*(S.trace(T*L2)+b*c)+a*b*(S.trace(N*L2)+h*c))==0
square=a*a*chi+a*S.trace(L0*K)
expected=a**3*h*(S.trace(T*L2)+b*c+S.trace(N*K))
assert S.expand(square-expected+a**3*b*(S.trace(N*L2)+h*c))==0
# Retain h's normal derivative in the source product.
q,h1=S.symbols('q h1')
product=(a*(h+q*h1)-q*b)*(a*N+q*T)
zero(product.diff(q).subs(q,0)-a*(h*T-(b-a*h1)*N))
print('PASS: universal conic fourth-square coefficient identities and I-adic bounds')
