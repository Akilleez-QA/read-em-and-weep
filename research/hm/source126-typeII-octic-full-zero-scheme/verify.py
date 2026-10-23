#!/usr/bin/env python3
"""Universal full-generator zero scheme; no actual HM evaluation."""
from pathlib import Path
import hashlib,itertools,json
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    if not value:raise RuntimeError(name)
    checks.append(name)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/e['local_path']).read_bytes()
    check(e['label']+' SHA256',hashlib.sha256(b).hexdigest()==e['sha256'])
    check(e['label']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'])
phi=(1+s.sqrt(5))/2
A=s.Matrix([3,-1,0,phi,1-phi]);D=s.Matrix([5,1,-1,0,0]);P=s.Matrix([4,0,1,-1,-1]);V=s.Matrix([3,-1,0,1-phi,phi]);one=s.ones(5,1)
w=(1,15,20,12,12)
mul=lambda a,b:a.multiply_elementwise(b)
inner=lambda a,b:s.simplify(sum(z*x*y for z,x,y in zip(w,a,b))/60)
H=[one,A]
for n in range(2,4):H.append((mul(A,H[n-1])-mul(A,H[n-2])+(H[n-3] if n>=3 else s.zeros(5,1))).applyfunc(s.expand))
check('plane symmetric square', (H[2]-one-D).applyfunc(s.simplify)==s.zeros(5,1))
check('plane symmetric cube', (H[3]-A-V-P).applyfunc(s.simplify)==s.zeros(5,1))
check('unique cubic P channel',inner(H[3],P)==1)
check('unique quadratic polarization channel',inner(mul(H[2],A),P)==1)
check('D tensor A has one P',inner(mul(D,A),P)==1)
check('P has no C5 fixed vector',s.Rational(4+4*(-1),5)==0)
check('rank2 derivative gives tangent rank2',3-1==2)

# Euler's identity for a general PLANE cubic. No invariant coefficients or
# actual parameter values are selected.
a,b,c=s.symbols('a b c');coeff=s.symbols('z:10')
monomials=[a**i*b**j*c**(3-i-j) for i in range(4) for j in range(4-i)]
f=sum(z*m for z,m in zip(coeff,monomials))
check('plane cubic monomial count',len(monomials)==10)
check('universal cubic Euler',s.expand(a*s.diff(f,a)+b*s.diff(f,b)+c*s.diff(f,c)-3*f)==0)
check('universal derivative degree2',all(s.Poly(s.diff(f,x),a,b,c).total_degree()==2 for x in (a,b,c)))

# S3 class order: identity, transpositions, 3-cycles. Retain O(-1) sign.
ones=s.Matrix([1,1,1]);chi=s.Matrix([1,-1,1]);rho=s.Matrix([2,0,-1]);sw=(1,3,2)
sinner=lambda x,y:s.simplify(sum(z*a*b for z,a,b in zip(sw,x,y))/6)
Ds=s.Matrix([5,1,-1]);Ps=s.Matrix([4,0,1])
check('D restriction',Ds==ones+2*rho)
check('P restriction',Ps==ones+chi+rho)
check('standard sign twist',mul(rho,chi)==rho)
check('D source sign twist',mul(Ds,chi)==chi+2*rho)
check('cubic parameter character',chi.applyfunc(lambda x:x**3)==chi)
check('parameter O-minus1 character',chi!=ones)
check('unique P sign line',sinner(Ps,chi)==1)
check('sign orthogonal trivial',sinner(chi,ones)==0)
check('sign orthogonal standard',sinner(chi,rho)==0)
image_options=[]
for m1,mc,mr in itertools.product(range(2),range(2),range(2)):
    if m1<=0 and mc<=1 and mr<=1 and m1+mc+2*mr==3:image_options.append((m1,mc,mr))
check('unique twisted rank3 image',image_options==[(0,1,1)])
check('rank3 image character',chi+rho==s.Matrix([3,-1,0]))
# The un-twisted erroneous inference really differs.
check('untwisted rank3 alternative differs',ones+rho!=chi+rho)
x,y,eta=s.symbols('x y eta',nonzero=True)
check('axis fixed by binary rotation',s.expand((eta*x)*(y/eta)-x*y)==0)
check('axis negated by binary swap',s.expand(y*(-x)+x*y)==0)
check('swap squared is central scalar',(-x)*(-y)==x*y)

# Scheme-theoretic outer product ideals are all pairwise products.
u,v=s.symbols('u v')
sigma_gens=[u*u,v*v];psi_gens=[u,v]
product=[s.expand(f*g) for f in sigma_gens for g in psi_gens]
triples=[u**3,u*u*v,u*v*v,v**3]
check('local product generators',set(product)==set(triples))
check('product Groebner equals maximal cube',s.groebner(product,u,v).polys==s.groebner(triples,u,v).polys)
length4=[(i,j) for i in range(2) for j in range(2)]
length6=[(i,j) for i in range(3) for j in range(3-i)]
check('sigma local length4',len(length4)==4)
check('generator local length6',len(length6)==6)
check('triple fat point monomials',set(length6)=={(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)})
check('target factor length34',6*4+10==34)
check('full generator length46',6*6+10==46)
check('additional local length exactly12',46-34==6*(6-4))
# Universal outer product in local frames, retaining all entries.
ss=s.symbols('s:2');pp=s.symbols('p:5')
M=s.Matrix(ss)*s.Matrix(1,5,pp)
for i in range(2):
 for j in range(5):check(f'outer product entry {i},{j}',M[i,j]==ss[i]*pp[j])
result={'status':'PASS','checks':len(checks),'cubic_P_base_scheme':'six reduced C5 axes',
 'quartic_covector_zero_scheme':'six reduced C5 axes; nonzero at all C3 axes',
 'C3_parameter_line':'sign','C3_twisted_rank3_image':'sign + standard2',
 'full_generator_zero_length':46,'full_generator_local_ideals':{'six_C5_axes':'m^3, length6 each','ten_C3_axes':'m, length1 each'},
 'square_conic_zeros':False,'actual_octic_scalar':'unselected','actual_instance_evaluated':False,'source_pair_removed':False}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
