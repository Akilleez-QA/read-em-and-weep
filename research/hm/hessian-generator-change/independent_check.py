import sympy as S
A,B=S.symbols('a b')
c=S.symbols('c0:4'); e=S.symbols('e0:6'); d=S.symbols('d0:3')
f=sum(c[i]*A**(3-i)*B**i for i in range(4))
g=sum(e[i]*A**(5-i)*B**i for i in range(6))
h=sum(d[i]*A**(2-i)*B**i for i in range(3)); gp=g+h*f
H=lambda p:S.hessian(p,(A,B))
mx=lambda U,V:U[0,0]*V[1,1]+U[1,1]*V[0,0]-2*U[0,1]*V[0,1]
J=lambda p,r:S.diff(p,A)*S.diff(r,B)-S.diff(p,B)*S.diff(r,A)
k=J(f,h)/15; K=S.diff(k,A)/3; L=S.diff(k,B)/3
F=S.Matrix([S.diff(f,A)/3,S.diff(f,B)/3]); G=S.Matrix([S.diff(g,A)/5,S.diff(g,B)/5])
gamma=-mx(H(f),H(h))/144
alpha=-F[0]*L+F[1]*K
beta=-(G[0]+h*F[0])*L+(G[1]+h*F[1])*K
t=mx(H(f),H(g))/240; ss=-H(f).det()/36; r=H(g).det()/400
tp=mx(H(f),H(gp))/240; rp=H(gp).det()/400
checks={
'euler first':S.diff(gp,A)/5-G[0]-h*F[0]+B*k,
'euler second':S.diff(gp,B)/5-G[1]-h*F[1]-A*k,
'diagonal':alpha+tp-t+h*ss-f*gamma,
'lower-left':2*beta+k*k+rp-r-2*h*t+h*h*ss-2*gp*gamma,
'linear decomposition':A*K+B*L-k}
for name,p in checks.items():
    assert S.expand(p)==0,name
    print(name+': PASS')
x,y,z,ka,kb=S.symbols('x y z ka kb'); q=x*z-y*y
C=S.Matrix([[x,y],[y,z]]); vec=S.Matrix([-y*ka-z*kb,x*ka+y*kb])
assert (C*vec-q*S.Matrix([-kb,ka])).applyfunc(S.expand)==S.zeros(2,1)
print('coarse identity: PASS')
