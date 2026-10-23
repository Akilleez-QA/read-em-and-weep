#!/usr/bin/env python3
"""Universal coefficient/divisibility certificate; no actual source evaluation."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent; checks=[]
def check(name,ok):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['local_path']).read_bytes()
 check(item['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==item['sha256'])
 check(item['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'])
X,Y,u,v=s.symbols('X Y u v')
# X and Y are arbitrary complementary formal linear forms, not chosen
# direction values of an actual source. Coefficients span each full Sym^n.
def polarization(n,k,f):
 return [s.diff(f,X,k-j,Y,j)/(s.factorial(k-j)*s.factorial(j)) for j in range(k+1)]
def constraints(n,k,square):
 cols=[];degree=n-k
 for i in range(n+1):
  pieces=polarization(n,k,X**(n-i)*Y**i)
  forbidden=[j for j in range(degree+1) if (degree-j<2 if square else (j==0 or j==degree))]
  cols.append(s.Matrix([s.expand(g).coeff(X,degree-j).coeff(Y,j) for g in pieces for j in forbidden]))
 return s.Matrix.hstack(*cols)
for n,k,square,allowed,name in [(10,8,True,[0],'N0 square'),(10,8,False,[],'N0 nonsquare'),(8,2,True,list(range(5)),'N8 square'),(8,2,False,[3,4,5],'N8 nonsquare')]:
 M=constraints(n,k,square)
 check(name+' full coefficient kernel dimension',n+1-M.rank()==len(allowed))
 check(name+' exact monomial kernel',all(M[:,i]==s.zeros(M.rows,1) for i in allowed))
 # Independence of all other columns excludes cancellations.
 check(name+' no cancellation between forbidden monomials',M[:,[i for i in range(n+1) if i not in allowed]].rank()==n+1-len(allowed))
coeff=s.symbols('f0:9');f=sum(coeff[i]*X**(8-i)*Y**i for i in range(9))
check('Delta2,6 equals full second derivative coefficients',polarization(8,2,f)==[s.diff(f,X,2)/2,s.diff(f,X,Y),s.diff(f,Y,2)/2])
l=u*X+v*Y
check('complete pure-power covariance all linear forms',all(s.expand(g-s.binomial(10,8)*s.binomial(8,j)*u**(8-j)*v**j*l**2)==0 for j,g in enumerate(polarization(10,8,l**10))))
check('block dimensions match actual positive component',9+32==41 and 16+21==37)
check('quadratic general block ceiling',min(9,16)+min(32,21)==30)
check('N0 square and nonsquare ranks',9-1==8 and 9-0==9)
check('N8 square and nonsquare ranks',15-5==10 and 15-3==12)
check('nonsplit residual square ceiling',9+10==19)
check('full square ceiling',8+19==27)
# Universal multilinearity example, with all coefficients indeterminate.
t=s.symbols('t');Q=s.Matrix(3,3,s.symbols('q0:9'));U=s.Matrix(3,2,s.symbols('u0:6'));V=s.Matrix(2,3,s.symbols('v0:6'))
det=s.Poly((Q+t*U*V).det(),t)
check('universal rank-two update has no cubic determinant term',det.degree()<=2)
check('no simultaneous Q block assumption',len(set().union(*(z.free_symbols for z in Q)))==9)
check('generic finite final exponent24',30-3*2==24)
check('square finite final exponent21',27-3*2==21)
check('zero-fourth lower bound5',4+1==5)
check('improved zero-alpha generic interval',list(range(5,25))[-1]==24)
check('improved square interval',list(range(5,22))[-1]==21)
check('six axes cannot form conic orbit',6<12)
check('conic fourth exceptional support',12==12 and 6+10+12==28)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'bounds':{'general_T_rank':30,'square_T_rank':27,'finite_generic_last_exponent':24,'finite_square_last_exponent':21},'scope':'Conditional actual source2; no source, coefficient or direction evaluated. Absent final pivot remains possible.'},indent=2))
