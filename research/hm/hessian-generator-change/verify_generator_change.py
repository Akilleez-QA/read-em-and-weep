import sympy as s
a,b=s.symbols('a b'); c=s.symbols('c0:4'); d=s.symbols('d0:3')
f=sum(c[i]*a**(3-i)*b**i for i in range(4)); h=sum(d[i]*a**(2-i)*b**i for i in range(3))
J=lambda f,g:s.diff(f,a)*s.diff(g,b)-s.diff(f,b)*s.diff(g,a)
H=lambda f:s.hessian(f,(a,b))
mix=lambda U,V:U[0,0]*V[1,1]+U[1,1]*V[0,0]-2*U[0,1]*V[0,1]
k=J(f,h)/15
D=s.expand(-J(f,k)/9+mix(H(f),H(h*f))/240-h*H(f).det()/36)
assert s.expand(D+f*mix(H(f),H(h))/144)==0
print('PASS: universal diagonal generator-change identity; no global gluing or gauge sufficiency checked.')
