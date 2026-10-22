"""Universal representation and tensor identities; no HM-instance input."""
import sympy as s
phi=(1+s.sqrt(5))/2
sizes=[1,15,20,12,12]
one=[1]*5
A=[3,-1,0,phi,1-phi]
V=[3,-1,0,1-phi,phi]
P=[4,0,1,-1,-1]
D=[5,1,-1,0,0]
def add(*rows): return [s.simplify(sum(v)) for v in zip(*rows)]
def mul(x,y): return [s.simplify(a*b) for a,b in zip(x,y)]
def ip(x,y): return s.simplify(s.Rational(1,60)*sum(n*a*b for n,a,b in zip(sizes,x,y)))
assert mul(A,A)==add(one,A,D)
assert mul(V,D)==add(A,V,P,D)
assert mul(P,D)==add(A,V,P,D,D)
assert mul(D,D)==add(one,A,V,P,P,D,D)
C=add(V,P,P,P,D,D)
Sym2A=add(one,D)
assert ip(D,mul(C,Sym2A))==13
assert ip(mul(A,A),C)==2
assert ip(D,C)==2
assert ip(mul(A,A),P)==0
assert ip(D,mul(P,Sym2A))==2
assert ip(D,P)==0
x,y,u,v,w,gamma=s.symbols('x y u v w gamma')
S=s.Matrix([[x,u,v],[u,y,w],[v,w,-x-y]])
I=s.eye(3)
result=s.zeros(3)
for j in range(3):
    e=I[:,j]; b=gamma*S*e
    sym=(e*b.T+b*e.T)/2
    result+=sym-s.trace(sym)*I/3
assert s.simplify(result-gamma*S)==s.zeros(3)
print('PASS: lower-family restriction/trace dimensions 13 -> 11 + 2.')
print('PASS: endpoint P4 restriction is an isomorphism on two channels.')
print('PASS: exact symbolic trace of every factoring family is gamma*T(S_h).')
print('No actual endpoint or fourth-obstruction value is evaluated.')
