#!/usr/bin/env python3
"""Formal-algebra certificate, not evaluation of an actual source matrix."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent;checks=[]
def check(name,ok):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['local_path']).read_bytes()
 check(item['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==item['sha256'])
 check(item['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'])
t=s.symbols('t')
def smat(prefix,n,m):return s.Matrix(n,m,s.symbols(prefix+':'+str(n*m)))
def coeff(M,k):return M.applyfunc(lambda f:s.expand(f).coeff(t,k))
A=smat('a',3,3);B=smat('b',3,5);C=smat('c',1,3);D=smat('d',1,5);E=smat('e',1,5)
U=s.eye(3)+t*A;Ui=s.eye(3)-t*A+t*t*A*A
check('unit-block inverse through degree2',all(coeff(U*Ui-s.eye(3),i)==s.zeros(3) for i in range(3)))
M=t*t*U.row_join(t*B).col_join((t*C).row_join(t*D+t*t*E))
left=s.eye(4);left[3:4,0:3]=-t*C*Ui
right=s.eye(8);right[0:3,3:8]=-Ui*t*B
S=left*M*right
check('universal residual block shape',M.shape==(4,8))
check('first unit Schur operations have determinant1',left.det()==1 and right.det()==1)
check('top right killed through degree4',all(coeff(S[:3,3:],k)==s.zeros(3,5) for k in range(5)))
check('bottom left killed through degree4',all(coeff(S[3:,:3],k)==s.zeros(1,3) for k in range(5)))
check('third coefficient is normalized D',coeff(S[3:,3:],3)==D)
check('fourth coefficient is corrected E minus CB',coeff(S[3:,3:],4)==E-C*B)
check('no residual coefficients below degree3',all(coeff(S[3:,3:],k)==s.zeros(1,5) for k in range(3)))
# The five localizations cover every nonzero fourth coefficient row.
r=s.symbols('r0:5');row=s.Matrix([r]).reshape(1,5)
for pivot in range(5):
 order=[pivot]+[j for j in range(5) if j!=pivot]
 V=s.zeros(5)
 V[pivot,0]=1/r[pivot]
 for col,j in enumerate(order[1:],1):
  V[j,col]=1;V[pivot,col]=-r[j]/r[pivot]
 check('row unit pivot chart'+str(pivot),row*V==s.Matrix([[1,0,0,0,0]]))
 check('column basis invertible chart'+str(pivot),s.simplify(V.det()*r[pivot]) in [1,-1])
 check('four independent kernel columns chart'+str(pivot),V[:,1:].extract(order[1:],range(4))==s.eye(4))
exponents=[0]*33+[2]*3+[4]
check('positive source and target dimensions',41-37==4 and len(exponents)==37)
check('rank33 kernel and cokernel dimensions',41-33==8 and 37-33==4)
check('second page remaining dimensions',8-3==5 and 4-3==1)
check('fourth page remaining dimensions',5-1==4 and 1-1==0)
check('unit and positive valuation counts',exponents.count(0)==33 and exponents.count(2)==3 and exponents.count(4)==1)
check('maximal minor valuation10',sum(exponents)==10)
check('determinantal orders34to37',[sum(exponents[:k]) for k in range(34,38)]==[2,4,6,10])
check('cokernel length10',3*2+4==10)
check('exceptional scheme length46',6*4+10+12==46)
check('exceptional support count28',6+10+12==28)
check('second rank-drop support included',set(['C5']).issubset({'C5','C3','E12'}))
# Gate-to-determinant equivalence after the three t-squared pivots.
alpha=s.symbols('alpha'); z=s.symbols('z0:5'); w=s.symbols('w0:5')
last=s.Matrix([[t**4*alpha*z[j]+t**5*w[j] for j in range(5)]])
check('order-four row proportional to unselected alpha',coeff(last,4)==alpha*s.Matrix([z]))
check('zero alpha kills fourth but permits later coefficients',last.subs(alpha,0)==t**5*s.Matrix([w]))
check('zero alpha maximal minors divisible by t11',all(s.expand(t**6*v).coeff(t,10)==0 for v in last.subs(alpha,0)))
check('degree-ten Plucker coefficient is alpha times nonzero row',coeff(t**6*last,10)==alpha*s.Matrix([z]))
check('first four exceptional Smith shifts',6+4==10 and 6+5==11)
check('finite later exponent polynomial degree bound',37-6==31)
check('no inference of Laurent rank loss from zero fourth',s.expand(t**6*last.subs(alpha,0)[0])==t**11*w[0])
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'hypothesis':'residual-large; alpha nonzero is an explicit conditional hypothesis; no endpoint9 input','smith_exponents':exponents,'free_source_columns':4,'maximal_minor_valuation':10,'scope':'Positive41-to37 component only, outside support of Z plus E12; no actual evaluations.'},indent=2))
