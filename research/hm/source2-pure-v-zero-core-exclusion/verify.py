"""Verify universal polynomial identities and pinned public inputs only."""
from pathlib import Path
from math import comb
import hashlib
import json
import sympy as s

root=Path(__file__).resolve().parent
checks=[]
def ck(name,condition):
    if not bool(condition):
        raise RuntimeError(name)
    checks.append(name)

for row in json.loads((root/'INPUTS.json').read_text()):
    data=(root/row['local_path']).read_bytes()
    ck(row['label']+' SHA-256',hashlib.sha256(data).hexdigest()==row['sha256'])
    ck(row['label']+' Git blob',hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==row['git_blob'])

x,y,X,Y=s.symbols('x y X Y')
def tv2(a,g):
    return s.expand(s.diff(a,x,2)*s.diff(g,y,2)-2*s.diff(a,x,y)*s.diff(g,x,y)+s.diff(a,y,2)*s.diff(g,x,2))
def vec(f,n):
    p=s.Poly(s.expand(f),x,y)
    return s.Matrix([p.coeff_monomial(x**(n-j)*y**j) for j in range(n+1)])
def vec24(f):
    p=s.Poly(s.expand(f),X,Y,x,y)
    return s.Matrix([p.coeff_monomial(X**(2-i)*Y**i*x**(4-j)*y**j) for i in range(3) for j in range(5)])

# All 15 source coefficients and all 3 quadratic-argument coefficients.
M=s.Matrix.hstack(*[
    s.Matrix.vstack(*[
        vec(tv2(x**(2-i)*y**i,x**(6-k-j)*y**(k+j)),4)
        for k in range(3)])
    for i in range(3) for j in range(5)])
ck('full universal map has shape15x15',M.shape==(15,15))
determinant=M.det()
ck('full coefficient determinant',determinant==5222734824996864)
ck('determinant prime factorization',determinant==2**25*3**3*7**8)
ck('universal Hom map rank15',M.rank()==15)
G2=s.Matrix([[0,0,1],[0,-s.Rational(1,2),0],[1,0,0]])
L=s.kronecker_product(G2.inv(),s.eye(5))*M
ck('apolar Gram determinant',G2.det()==s.Rational(1,2))

# Simultaneous sl2 action on both tensor factors, not a group-point sample.
def sl2(n):
    e=s.zeros(n+1);f=s.zeros(n+1);h=s.zeros(n+1)
    for j in range(n+1):
        h[j,j]=n-2*j
        if j>0:e[j-1,j]=j
        if j<n:f[j+1,j]=n-j
    return e,f,h
E2,F2,H2=sl2(2);E4,F4,H4=sl2(4)
E=s.kronecker_product(E2,s.eye(5))+s.kronecker_product(s.eye(3),E4)
F=s.kronecker_product(F2,s.eye(5))+s.kronecker_product(s.eye(3),F4)
H=s.kronecker_product(H2,s.eye(5))+s.kronecker_product(s.eye(3),H4)
for label,Z in [('raising',E),('lowering',F),('weight',H)]:
    ck('recoupling commutes with '+label,L*Z==Z*L)

highest=[(6,4,X**2*x**4),(4,28,(X*y-Y*x)*X*x**3),(2,84,(X*y-Y*x)**2*x**2)]
all_columns=[]
for degree,scalar,poly in highest:
    v=vec24(poly)
    ck(f'Sym{degree} highest weight',E*v==s.zeros(15,1) and H*v==degree*v)
    ck(f'Sym{degree} highest recoupling scalar',L*v==scalar*v)
    columns=[]
    for j in range(degree+1):
        ck(f'Sym{degree} descendant{j} scalar',L*v==scalar*v)
        columns.append(v);all_columns.append(v)
        v=F*v
    ck(f'Sym{degree} full lowering span',s.Matrix.hstack(*columns).rank()==degree+1)
    ck(f'Sym{degree} lowering terminates',v==s.zeros(15,1))
ck('three full summands span all15 coefficients',s.Matrix.hstack(*all_columns).rank()==15)
z=s.symbols('z')
ck('whole recoupling characteristic polynomial',s.Poly(L.charpoly(z).as_expr(),z)==s.Poly((z-4)**7*(z-28)**5*(z-84)**3,z))

# Independent exact finite-group character identities.
r5=s.sqrt(5);phi=(1+r5)/2
traces=[2,-2,0,1,-1,phi,-phi,phi-1,1-phi]
class_sizes=[1,1,30,20,20,12,12,12,12]
def sy(n):
    a=s.ones(9,1);b=s.Matrix(traces)
    for _ in range(n):
        a,b=b,s.Matrix([s.simplify(traces[i]*b[i]-a[i]) for i in range(9)])
    return a

def mul(a,b):return s.Matrix([s.simplify(c*d) for c,d in zip(a,b)])
def ip(a,b):return s.simplify(sum(w*c*d for w,c,d in zip(class_sizes,a,b))/120)
W=sy(1);Wp=W.applyfunc(lambda c:c.xreplace({r5:-r5}));P=mul(W,Wp)
A=sy(2);S=sy(3);D=sy(4);T=sy(5);V=sy(6)-P
NC2=V+P+2*D;N8=A+V+P+D;NR=NC2+N8;J2=NR+P;target=mul(A,D)
ck('target is exactly A+V+P+D',target==N8)
ck('quartic finite-group irreducibility',ip(D,D)==1)
ck('sextic restricted representation is V+P',sy(6)==V+P)
ck('actual NC2 is Sym16',sy(16)==NC2)
ck('actual NC3 is Wprime+S+2T',sy(17)==Wp+S+2*T)
ck('actual separated degree2 is P+D',sy(8)==P+D)
ck('actual M2 dimension41',(NR+P+D)[0]==41)
ck('actual NR2 dimension32',NR[0]==32)
ck('actual J2 dimension36',J2[0]==36)
ck('universal target dimension15',target[0]==15)
ck('common residual kernel character is NC2',NR-target==NC2)
ck('full common kernel character is NC2+P',J2-target==NC2+P)
ck('common kernel dimension21',(J2-target)[0]==21)
ck('Ph has zero intersection with NC2 after nonzero projection',P[0]==4 and NC2[0]+P[0]==21)
ck('correction source is V+P+D',mul(A,P)==V+P+D)
ck('correction dimension12',mul(A,P)[0]==12)
ck('kernel decomposition dimensions9+12',21==(P+D)[0]+mul(A,P)[0])
ck('kernel decomposition characters',NC2+P==P+D+mul(A,P))
ck('actual QNC2 quotient character',NC2-D==V+P+D)
ck('QK dimension16',21-D[0]==16)
ck('QNC2 plus I4 dimension16',(NC2-D)[0]+P[0]==16)
ck('QNC2 plus I4 endpoint character',NC2-D+P==P+mul(A,P))
ck('canonical terminal dimension6',T[0]==6)
ck('separated terminal dimension12',(2*T)[0]==12)
ck('terminal dimensions are contradictory',T[0]!=(2*T)[0])

print(json.dumps({
    'status':'PASS','count':len(checks),'checks':checks,
    'universal_map_shape':[15,15],'universal_rank':15,
    'universal_determinant':str(determinant),
    'apolar_channel_scalars':{'Sym6':4,'Sym4':28,'Sym2':84},
    'under_hNC4_zero':{'NR_common_kernel':17,'J2_common_kernel':21},
    'contradictory_terminal_dimensions_under_R_zero':[6,12],
    'scope':'Entire universal representation identities; actual-map transport is proved in PROOF.md; no actual source coefficients or instance ranks are evaluated.'
},indent=2))
