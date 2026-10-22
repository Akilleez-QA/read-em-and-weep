import runpy,sympy as S
from pathlib import Path
n=runpy.run_path(str(Path(__file__).with_name('verify_nonzero_endpoint_explicit_serre_residue.py')))
X,Y,s,t,A,B,c,e,k=[n[v] for v in ('X','Y','s','t','A','B','c','e','k')]
Q=n['Q'];pair=n['pair']
f=A*X**2*Y*s**3+B*Y**3*s*s*t+A*c*X**3*s*t*t-B*c*X*Y*Y*t**3
# Unnormalized product transvectants; conventions absorbed by calibration.
def tv(p,q,r,j):
 return S.expand(sum((-1)**(i+l)*S.binomial(r,i)*S.binomial(j,l)*S.diff(p,X,r-i,Y,i,s,j-l,t,l)*S.diff(q,X,i,Y,r-i,s,l,t,j-l) for i in range(r+1) for l in range(j+1)))
def project(p):
 return S.factor(S.expand(p-sum(pair(p,Q[4-i])/pair(Q[i],Q[4-i])*Q[i] for i in range(5))))
H=tv(f,f,1,1)
vals={}
for label,h in [('X4',X**4),('XY3',X*Y**3),('X2Y2',X*X*Y*Y)]:
 U=project(tv(h*t**4,S.expand(f*f),4,4));V=project(tv(h*t**4,H,3,3))
 vals[label]=(U,V)
 print(label,'U=',U,'V=',V,flush=True)

def zero(q):assert S.cancel(q)==0,S.factor(q)
# Exact invariant Gram identity, not an instance rank evaluation.
for i in range(5):
 for j in range(5):
  expected=3*e**2*S.Rational(1,8)*(-1)**i/S.binomial(4,i) if i+j==4 else 0
  zero(pair(Q[i],Q[j])-expected)
for pairval in vals.values():
 for v in pairval:
  for qi in Q:zero(pair(v,qi))
O1=B*t*(2*A*X**2*s-B*Y**2*t)
O2=A**2*X*(c*X*t*t+2*Y*s*s)
O3=A*s*(A*X*X*s+2*B*Y*Y*t)
for v,expected in zip(vals['X4'],[-552960*O1,-995328*O1]):zero(v-expected)
for v,expected in zip(vals['XY3'],[-3870720*O2,-248832*O2]):zero(v-expected)
for v,expected in zip(vals['X2Y2'],[2764800*O3,497664*O3]):zero(v-expected)
# Independence of two universal tensor maps: exact symbolic coefficient determinant.
det=(-552960)*(-248832)-(-995328)*(-3870720)
assert det==-3715041853440 and det!=0
# Representation arithmetic: multiplicity of P4 in D5 tensor Sym^2(A) is two.
sizes=[1,15,20,12,12];d5=[5,1,-1,0,0];p4=[4,0,1,-1,-1];sym2a=[6,2,0,1,1]
assert sum(a*b*c*d for a,b,c,d in zip(sizes,d5,p4,sym2a))==120
assert sum(a*b*c*d for a,b,c,d in zip(sizes,d5,p4,sym2a))//60==2
cU=k*e/(7464960*A*B*c)
cV=-k*e/(13436928*A*B*c)
value=lambda label:S.factor(cU*vals[label][0]+cV*vals[label][1])
zero(value('X4'))
zero(value('XY3')+k*e*A/(B*c)*(X*Y*s*s+c*X*X*t*t/2))
result=k*e/(3*B*c)*s*(A*X*X*s+2*B*Y*Y*t)
zero(value('X2Y2')-result)
for qi in Q:zero(pair(result,qi))
assert S.Poly(result,X,Y,s,t).coeff_monomial(X*X*s*s).is_nonzero
print('PASS: invariant Gram identity and all orthogonal projections.')
print('PASS: independent universal tensor maps, determinant',det,'and complete quadratic-family multiplicity two.')
print('PASS: both actual K-input calibration identities.')
print('RESULT: normalized X2Y2 endpoint residue =',S.factor(result))
print('Actual residue is c_eta times this expression, c_eta nonzero and unknown. No fourth value.')
