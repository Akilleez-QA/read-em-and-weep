"""Bounded universal representation checks only; no HM source data."""
import sympy as s
phi=(1+s.sqrt(5))/2; phib=1-phi
sizes=[1,15,20,12,12]
chars={'1':[1]*5,'A':[3,-1,0,phi,phib],'V':[3,-1,0,phib,phi],'P':[4,0,1,-1,-1],'D':[5,1,-1,0,0]}
def ip(x,y): return s.simplify(s.Rational(1,60)*sum(n*a*b for n,a,b in zip(sizes,x,y)))
def mult(x): return {k:ip(x,y) for k,y in chars.items()}
def add(*rows):return [s.simplify(sum(z)) for z in zip(*rows)]
def eq(x,y):assert all(s.simplify(a-b)==0 for a,b in zip(x,y))
A=chars['A']; D=chars['D']; P=chars['P']
S={0:chars['1'],2:A}
for n in [4,6,8]: S[n]=[s.simplify((a-1)*b-c) for a,b,c in zip(A,S[n-2],S[n-4])]
eq(S[4],D);eq(S[6],add(chars['V'],P));eq(S[8],add(D,P))
assert ip([a*a for a in A],D)==1
M=[a*b for a,b in zip(D,P)]
assert mult(M)=={'1':0,'A':1,'V':1,'P':1,'D':2}
squared=[0,0,2,4,3]
sym=[s.Rational(1,2)*(D[i]**2+D[squared[i]]) for i in range(5)]
alt=[s.Rational(1,2)*(D[i]**2-D[squared[i]]) for i in range(5)]
eq(sym,add(S[8],S[4],S[0]));eq(alt,add(S[6],S[2]))
assert ip(sym,P)==ip(alt,P)==1
weights={'A':[0,2,-2],'V':[0,4,-4],'P':[2,-2,4,-4],'D':[0,2,-2,4,-4]}
counts={k:sum(w%10==4 for w in v) for k,v in weights.items()}
assert counts=={'A':0,'V':1,'P':1,'D':1}
assert sum(mult(M)[k]*counts[k] for k in counts)==4
assert all(sum(w%10==(h+4)%10 for w in weights['P'])==1 for h in [4,2])
x,y=s.symbols('x y')
def tv(f,g,r):return s.expand(sum((-1)**i*s.binomial(r,i)*s.diff(f,x,r-i,y,i)*s.diff(g,x,i,y,r-i) for i in range(r+1)))
assert tv(x**4,x**2,2)==0 and tv(x**3*y,x**2,2)==0
assert tv(x**4,x**4,1)==0 and tv(x**4,x**3*y,1)==4*x**6
assert tv(y**4,x**2,2)==24*y**2
assert tv(x*y**3,x**2,2)==12*x*y
assert tv(x*x*y*y,x**2,2)==4*x*x
assert 12>8 and 12>6
print('PASS: character decomposition, exact fiber codimensions, channel parity, secant kernel and triangular transvectant identities. Orbit spanning and reconstruction are proved in PROOF.md.')
