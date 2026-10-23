"""Whole universal representation and projection identities; no source data."""
from pathlib import Path
from math import comb
import hashlib
import json
import sympy as s

root=Path(__file__).resolve().parent
checks=[]
def ck(name,condition):
    if not bool(condition):raise RuntimeError(name)
    checks.append(name)
for row in json.loads((root/'INPUTS.json').read_text()):
    data=(root/row['local_path']).read_bytes()
    ck(row['label']+' SHA256',hashlib.sha256(data).hexdigest()==row['sha256'])
    ck(row['label']+' Git blob',hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==row['git_blob'])

# Reconstruct the complete universal D18 row. No historical program is run.
x,y=s.symbols('x y');z=s.sqrt(5)
def vec(f,n):
    p=s.Poly(s.expand(f),x,y)
    return s.Matrix([p.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def tv(f,g,k):
    return s.expand(sum((-1)**j*comb(k,j)*s.diff(f,x,k-j,y,j)*s.diff(g,x,j,y,k-j) for j in range(k+1)))
def gram(n):
    return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,comb(n,i)) if i+j==n else 0)
f12=-2*x**12-s.Rational(44,5)*z*x**10*y**2+66*x**8*y**4+s.Rational(88,5)*z*x**6*y**6+66*x**4*y**8-s.Rational(44,5)*z*x**2*y**10-2*y**12
f20=tv(f12,f12,2)
E=s.Matrix.hstack(*[vec(tv(f20,x**(4-i)*y**i,3),18) for i in range(5)])
projection=E.T*gram(18)
M=s.Matrix.vstack(*[projection*s.Matrix.hstack(*[vec(x**(2-k)*y**k*x**(16-i)*y**i,18) for i in range(17)]) for k in range(3)])
I=s.Matrix.hstack(*[vec(f12*x**(4-i)*y**i,16) for i in range(5)])
ck('D18 complete inclusion shape',E.shape==(19,5))
ck('D18 inclusion rank5',E.rank()==5)
ck('whole NC common map shape',M.shape==(15,17))
ck('whole NC common map rank12',M.rank()==12)
ck('all embedded I2 coefficients killed',M*I==s.zeros(15,5))
ck('actual polynomial I2 model has rank5',I.rank()==5)
ck('whole common-kernel equality',17-M.rank()==I.rank())
rows=[0,1,2,3,4,5,6,7,8,9,13,14]
minor=s.simplify(M.extract(rows,list(range(12))).det())
expected=-s.Rational(18181172528241933728741524320484149524538009158867979010156234925375606868884195114084653614308612112384,364138898268600625)*z
ck('exact full-coefficient12minor from1113',minor==expected)

# Exact finite-group representation identities.
f=(1+z)/2;tr=[2,-2,0,1,-1,f,-f,f-1,1-f];weights=[1,1,30,20,20,12,12,12,12]
def sy(n):
    a=s.ones(9,1);b=s.Matrix(tr)
    for _ in range(n):a,b=b,s.Matrix([s.simplify(tr[i]*b[i]-a[i]) for i in range(9)])
    return a

def mul(a,b):return s.Matrix([s.simplify(c*d) for c,d in zip(a,b)])
def ip(a,b):return s.simplify(sum(w*c*d for w,c,d in zip(weights,a,b))/120)
W=sy(1);Wp=W.applyfunc(lambda a:a.xreplace({z:-z}));P=mul(W,Wp);A=sy(2);D=sy(4);V=sy(6)-P;T=sy(5)
NC=V+P+2*D;N8=A+V+P+D;NR=NC+N8;J=NR+P;target=mul(A,D)
KR=NR-target;K=J-target;correction=mul(A,P)
ck('NC2 exact polynomial character',sy(16)==NC)
ck('Sym18 complete character',sy(18)==A+V+2*P+D)
ck('unique D18',ip(D,sy(18))==1)
ck('target all four channels',target==N8)
ck('NC nonzero row fills V+P+D',NC-D==V+P+D)
ck('canonical A is remaining channel',target-(NC-D)==A)
ck('NR dimension32',NR[0]==32)
ck('J dimension36',J[0]==36)
ck('common target dimension15',target[0]==15)
ck('residual common kernel dimension17',KR[0]==17)
ck('full common kernel dimension21',K[0]==21)
ck('residual kernel character',KR==V+P+2*D)
ck('residual kernel quotient character',KR-D==V+P+D)
ck('full kernel split by separated Ph',K==KR+P)
ck('correction input three channels',correction==V+P+D)
ck('correction input dimension12',correction[0]==12)
ck('full correction decomposition character',K==D+P+correction)
ck('residual normalized decomposition character',KR==D+correction)
ck('unique residual P',ip(P,KR)==1)
ck('unique residual V',ip(V,KR)==1)
ck('V inverse ambiguity absent',ip(V,A+D)==0)
ck('P inverse ambiguity absent',ip(P,A+D)==0)
ck('D inverse ambiguity one I2 row',ip(D,A+D)==1)
ck('defect has only one P channel',ip(P,correction)==1 and ip(P,V)==0 and ip(P,D)==0)
ck('canonical quotient onto N8 subspace',KR-D==N8-A)
ck('generated endpoint character',P+correction==V+2*P+D)
ck('separated generated endpoint dimension16',(P+correction)[0]==16)
ck('terminal two T dimension12',(2*T)[0]==12)

# Full universal linear algebra of normalization. These 48 formal entries
# describe an ARBITRARY linear leakage E12 -> P4, not an actual HM map.
leak=s.Matrix(4,12,lambda i,j:s.Symbol(f'h_{i}_{j}'))
incI=s.Matrix.vstack(s.eye(5),s.zeros(16,5))
sigma=s.Matrix.vstack(s.zeros(5,4),s.eye(4),s.zeros(12,4))
k=s.Matrix.vstack(s.zeros(9,12),s.eye(12))
e=s.Matrix.hstack(s.zeros(4,5),s.eye(4),leak)
r=s.eye(21)-sigma*e
kt=r*k
quotient=s.Matrix.hstack(s.zeros(12,9),s.eye(12))
section=s.Matrix.hstack(incI,kt)
left=s.Matrix.vstack(s.Matrix.hstack(s.eye(5),s.zeros(5,16)),quotient)
ck('projection kills leakage exactly',e*r==s.zeros(4,21))
ck('projection idempotent',r*r==r)
ck('projection kills Ph section',r*sigma==s.zeros(21,4))
ck('projection fixes I2',r*incI==incI)
ck('section of quotient has full left inverse',left*section==s.eye(17))
ck('projection equals residual section times left inverse',section*left==r)
ck('normalized correction exact formula',kt==k-sigma*leak)
ck('normalized correction quotient isomorphism',quotient*kt==s.eye(12))
ck('normalized complement intersects I2 trivially',left*s.Matrix.hstack(incI,kt)==s.eye(17))

# F4=I4 plus T_A P_h coordinates. Q kills I2, maps Ph to I4,
# and maps the original correction to the raw quadratic descendants.
Q=s.Matrix.vstack(s.Matrix.hstack(s.zeros(4,5),s.eye(4),s.zeros(4,12)),s.Matrix.hstack(s.zeros(12,9),s.eye(12)))
incI4=s.Matrix.vstack(s.eye(4),s.zeros(12,4))
raw=s.Matrix.vstack(s.zeros(4,12),s.eye(12))
e4=s.Matrix.hstack(s.zeros(12,4),s.eye(12))
defect=Q*sigma*e*k
ck('Q kills I2',Q*incI==s.zeros(16,5))
ck('Q maps Ph to I4',Q*sigma==incI4)
ck('Q original correction equals raw descendants',Q*k==raw)
ck('normalization defect lives in I4',defect==incI4*leak)
ck('full exact Q defect',Q*kt==raw-defect)
ck('projected Q ignores Ph subtraction',e4*Q*r==e4*Q)
ck('forced separated cross-block isomorphism',e4*Q*kt==s.eye(12))
ck('I4 and Q residual correction are complementary',s.Matrix.hstack(incI4,Q*kt).det()==1)

# An arbitrary I2-valued change of right inverse. Equivariance further
# restricts it to the D channel, verified above by exact characters.
gauge=s.Matrix(5,12,lambda i,j:s.Symbol(f'g_{i}_{j}'))
kp=k+incI*gauge
ktp=r*kp
ck('normalization retains only I2 gauge',ktp-kt==incI*gauge)
ck('quotient section independent of inverse',quotient*ktp==quotient*kt)
ck('defect independent of inverse',Q*sigma*e*kp==defect)
ck('Q normalized image independent of inverse',Q*ktp==Q*kt)

print(json.dumps({
    'status':'PASS','count':len(checks),'checks':checks,
    'universal_NC_rank':12,'universal_NC_kernel':5,
    'NC_coefficient_minor':str(minor),
    'all_mechanisms_common_ranks':{'NR2':15,'J2':15},
    'all_mechanisms_common_kernel_dimensions':{'NR2':17,'J2':21},
    'separated_R0_normalized_complement_dimension':12,
    'formal_normalization_leakage_shape':[4,12],
    'defect_retained':True,
    'scope':'Whole universal coefficient and abstract projection identities only; actual transport is the written proof; no actual source or instance values.'
},indent=2))
