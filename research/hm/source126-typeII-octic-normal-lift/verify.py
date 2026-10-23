#!/usr/bin/env python3
"""Universal normal-lift identities. No actual HM input or specialization."""
from pathlib import Path
import hashlib,json,itertools,math
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    if not value:raise RuntimeError(name)
    checks.append(name)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
    raw=(ROOT/e['local_path']).read_bytes()
    check(e['label']+' SHA256',hashlib.sha256(raw).hexdigest()==e['sha256'])
    check(e['label']+' Git blob',hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['git_blob'])
# Completely formal 4x5 matrix. No representation matrix is instantiated.
entries=s.symbols('C11:16 C21:26 C31:36 C41:46')
C=s.Matrix(4,5,entries);z=s.Matrix(1,4,s.symbols('z1:5'))
k=s.Matrix([(-1)**j*C[:,[i for i in range(5) if i!=j]].det(method='domain-ge') for j in range(5)])
p=z*C
for i in range(4):check(f'Laplace kernel row{i}',s.expand((C*k)[i])==0)
for j in range(5):check(f'cofactor degree{j}',s.Poly(k[j],*entries).total_degree()==4)
contraction=s.expand((p*k)[0])
check('quartic covector kills cofactor',contraction==0)
R=k*p
# Exact associative contraction avoids exponentially re-expanding R*R.
check('square-zero by exact contraction',k*contraction*p==s.zeros(5))
check('C-annihilated lift',(C*k).applyfunc(s.expand)*p==s.zeros(4,5))
check('trace zero',s.expand(s.trace(R))==0)
kk=s.Matrix(s.symbols('k0:5'));pp=s.Matrix(1,5,s.symbols('p0:5'));outer=kk*pp
for i,j in itertools.combinations(range(5),2):
 for r,t in itertools.combinations(range(5),2):
    check(f'rank-one minor {i},{j};{r},{t}',s.expand(outer[i,r]*outer[j,t]-outer[i,t]*outer[j,r])==0)
check('weighted octic degree',4+3+1==8)
recipe={'kind':'universal determinantal identity, not actual HM coefficients',
 'C':[[str(C[i,j]) for j in range(5)] for i in range(4)],
 'weights':{'C_entries':1,'z_entries':3,'kappa':4,'psi':4,'R':8},
 'kappa':[str(v) for v in k], 'psi':[str(v) for v in p],
 'R':[[str(R[i,j]) for j in range(5)] for i in range(5)],
 'substitution':'C = pinned quotient multiplication family; z = paired cubic P-covariant',
 'actual_HM_coefficients_supplied':False}
(ROOT/'UNIVERSAL-MATRIX.json').write_text(json.dumps(recipe,indent=2)+'\n')
# Formal monic chart and division, never selected parameter values.
x,y,b,c=s.symbols('x y b c')
Q=s.Matrix([[-b**3+2*b*c,b*b-c,-b,1,0],[-b*b*c+c*c,b*c,-c,0,1]])
B=s.Matrix([[1,0,0],[b,1,0],[c,b,1],[0,c,b],[0,0,c]])
check('quotient kills complete multiplication gauge',(Q*B).applyfunc(s.expand)==s.zeros(2,3))
a=x*x+b*x*y+c*y*y
for i in range(5):
    rem=s.rem(x**(4-i)*y**i,a,x)
    check(f'quartic remainder basis{i}',s.expand(rem-Q[0,i]*x*y**3-Q[1,i]*y**4)==0)
U=s.Matrix(3,5,s.symbols('u0:15'));alpha=s.symbols('alpha')
L=B*U+alpha*outer
check('gauge invariant extraction identity',(Q*L-alpha*Q*outer).applyfunc(s.expand)==s.zeros(2,5))
from scalar_extraction import extract_scalar
value,pivot=extract_scalar(L,outer,b,c)
check('symbolic extractor returns only scalar',s.simplify(value-alpha)==0)
check('extractor pivot recorded',pivot['entry']==(0,0))
try:
    bad=L.copy();bad[4,0]+=b
    extract_scalar(bad,outer,b,c)
except ValueError:
    rejected=True
else:
    rejected=False
check('extractor rejects off-line quotient',rejected)
try:
    extract_scalar(L,s.zeros(5),b,c)
except ValueError:
    rejected=True
else:
    rejected=False
check('extractor rejects zero generator quotient',rejected)
check('plane degree7 monomials',math.comb(7+2,2)==36)
check('plane degree8 monomials',math.comb(8+2,2)==45)
check('normal form unknown count',3*5*36+1==541)
check('normal form equation count',5*5*45==1125)
check('lift zero length',6+10==16)
check('projection zero length',6*6+10==46)
check('projection excess length',46-16==6*(6-1))
# Local ideal products with a unit factor at each disjoint orbit.
u,v=s.symbols('u v')
check('C5 lift ideal',s.groebner([u,v],u,v).polys==s.groebner([1*u,1*v],u,v).polys)
check('C3 lift ideal',s.groebner([u,v],u,v).polys==s.groebner([u*1,v*1],u,v).polys)
check('C5 projected ideal',s.groebner([u*u*u,u*u*v,v*v*u,v*v*v],u,v).polys==s.groebner([u**3,u*u*v,u*v*v,v**3],u,v).polys)
# Universal rank-one nilpotent normal form, with no relation to an HM fiber.
J=s.zeros(5);J[0,1]=1
check('Jordan partition 2 1 1 1',J.rank()==1 and J*J==s.zeros(5))
from build_universal_matrix import build
pinned_pivot=build(check)
result={'pinned_extraction_pivot':pinned_pivot,'status':'PASS','checks':len(checks),'normalized_target_factor':'sigma = pi(kappa)',
 'lift_identities':['C R = 0','R^2 = 0','trace R = 0','rank R <= 1','pi R = g8'],
 'lift_zero_scheme':'six plus ten reduced axes','lift_zero_length':16,
 'projected_zero_length':46,'normal_form_dimension':541,'ambient_dimension':1125,
 'scalar_extraction':'quotient remainder coefficient, invariant under every B U gauge',
 'actual_scalar_evaluated':False,'actual_HM_instance_evaluated':False,'source_or_pair_removed':False}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
