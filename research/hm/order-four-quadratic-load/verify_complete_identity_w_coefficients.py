from universal_complete_identity_w_coefficients import *
FB,FC,FD=s.symbols('FB FC FD',nonzero=True)
f=s.Matrix([[0,0,FC,0],[-9*FB*FC/FD,0,0,0],[0,0,0,FD],[0,FB,0,0]])
q=s.symbols('q0:5');H0=op4(sum(c*m for c,m in zip(q,mon(4))))
g12=marked_twelve(f)
assert s.Poly(g12,S,T).coeff_monomial(S**6*T**6)==s.Rational(11,15)
print('PASS: marked invariant degree12 has fixed nonzero middle coefficient11/15.',flush=True)
rq,rh=build_complete_identity_w_coefficients(f,H0)
print('Constructed',len(rq),'Rq generators and',len(rh),'Rh coefficients.',flush=True)
for name,K in rq+rh:
 for e in K:
  for powers,c in s.Poly(s.expand(e),h,k,l,u,w).terms():
   if c:assert sum(powers[:3])==2 and sum(powers[3:])==2,(name,powers)
print('PASS: all97 coefficients have the required D²/base² degrees.',flush=True)
for name,K in rq:
 for e in K:
  for powers,c in s.Poly(s.expand(e),*q).terms():
   if c:assert sum(powers)==1,(name,powers)
for name,K in rh:
 assert not (set().union(*(e.free_symbols for e in K))&set(q))
for degree,target,order,kind in [(8,4,8,'D5'),(8,6,7,'P4'),(10,2,10,'V'),(10,4,9,'D5'),(10,6,8,'A')]:
 zs=s.symbols('bridge'+str(degree)+'_'+str(target)+'_0:'+str(degree+1))
 p0=sum(c*m for c,m in zip(zs,mon(degree)))
 out=tv(g12,p0,order)
 assert s.expand(out)!=0
 if kind in ('A','P4'):
  R=op6(out);val=2 if kind=='A' else 12
  zero_matrix(negative_casimir(f,R)-val*R)
 print('PASS: complete marked bridge',degree,'to',target,'has type',kind,flush=True)
cs=s.symbols('sextic0:7');pp=sum(c*m for c,m in zip(cs,mon(6)))
assert s.expand(sextic(op6(pp))-pp)==0
# Exact G-character identities; all representations are symbolic.
phi=(1+s.sqrt(5))/2;sizes=[1,15,20,12,12]
C={'1':s.ones(5,1),'A':s.Matrix([3,-1,0,phi,1-phi]),'V':s.Matrix([3,-1,0,1-phi,phi]),'P4':s.Matrix([4,0,1,-1,-1]),'D5':s.Matrix([5,1,-1,0,0])}
inner=lambda a,b:s.simplify(sum(n*x*y for n,x,y in zip(sizes,a,b))/60)
mul=lambda a,b:a.multiply_elementwise(b)
even=[C['1'],C['V']]
for i in range(1,6):even.append((mul(C['V']-C['1'],even[i])-even[i-1]).applyfunc(s.simplify))
assert even[2]==C['D5'] and even[3]==C['A']+C['P4']
assert even[4]==C['P4']+C['D5'] and even[5]==C['A']+C['V']+C['D5']
assert inner(even[6],C['1'])==1
N=mul(C['1']+C['D5'],C['A'])
end6=2*C['1']+C['A']+4*C['V']+C['P4']+3*C['D5']
assert inner(mul(C['D5'],N),end6)==54 and inner(N,end6)==10
for degree,target,kind in [(8,4,'D5'),(8,6,'P4'),(10,2,'V'),(10,4,'D5'),(10,6,'A')]:
 assert inner(even[degree//2],even[target//2])==1
 assert inner(even[degree//2],C[kind])==inner(even[target//2],C[kind])==1
print('PASS: all five bridge Hom spaces are one-dimensional; full identity-W coefficient target is54+10.')
print('No actual source values, instance ranks, middle-presentation independence, or solution claim.')
