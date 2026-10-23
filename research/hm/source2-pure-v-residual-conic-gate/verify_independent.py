import sympy as s
x,y,u,v=s.symbols('x y u v')
def tr(a,b,k):
 return s.expand(sum((-1)**i*s.binomial(k,i)*s.diff(a,x,k-i,y,i)*s.diff(b,x,i,y,k-i) for i in range(k+1)))
def delta(f):
 g=s.Poly(s.expand(f.subs({x:x+u,y:y+v},simultaneous=True)),u,v)
 return [g.coeff_monomial(u**(2-j)*v**j) for j in range(3)]
def C(a):return s.expand(sum(tr(x**(2-j)*y**j,a[j],2) for j in range(3)))
def cv(f,d):return s.Matrix([s.expand(f).coeff(x,d-i).coeff(y,i) for i in range(d+1)])
f=sum(s.Symbol('f'+str(i))*x**(6-i)*y**i for i in range(7));c=sum(s.Symbol('c'+str(i))*x**(3-i)*y**i for i in range(4));a=sum(s.Symbol('a'+str(i))*x**(2-i)*y**i for i in range(3))
checks={
 'cubic descendant identity':s.expand(C([c*g for g in delta(f)])-tr(c,f,2))==0,
 'Spencer factor minus twelve':s.expand(x*tr(y*c,f,3)-y*tr(x*c,f,3)+12*tr(c,f,2))==0,
 'diagonal factor three hundred sixty':s.expand(tr(a*a,f,3)-6*tr(a,tr(a,f,2),1))==0}
rels=[]
for z in [x,y]:
 for i in range(9):
  d=delta(x**(8-i)*y**i)
  rels.append(s.Matrix.vstack(*[cv(z*g,7) for g in d]))
Rel=s.Matrix.hstack(*rels)
CM=s.Matrix.hstack(*[cv(tr(x**(2-j)*y**j,x**(7-i)*y**i,2),5) for j in range(3) for i in range(8)])
checks.update({'relations rank eighteen':Rel.rank()==18,'quotient rank six':CM.rank()==6,'C annihilates exact relations':CM*Rel==s.zeros(6,18)})
for k,v in checks.items():
 if not v:raise RuntimeError(k)
print(checks)
