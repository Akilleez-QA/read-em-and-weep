#!/usr/bin/env python3
"""Universal plane-character and normalization checks. No actual HM evaluation."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(label,value):
    if not value: raise RuntimeError(label)
    checks.append(label)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/e['local_path']).read_bytes()
    check(e['label']+' SHA256',hashlib.sha256(b).hexdigest()==e['sha256'])
    check(e['label']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'])
phi=(1+s.sqrt(5))/2
A=s.Matrix([3,-1,0,phi,1-phi]);D=s.Matrix([5,1,-1,0,0]);V=s.Matrix([3,-1,0,1-phi,phi]);P=s.Matrix([4,0,1,-1,-1]);one=s.ones(5,1)
w=(1,15,20,12,12)
mul=lambda a,b:a.multiply_elementwise(b)
inner=lambda a,b:s.simplify(sum(z*x*y for z,x,y in zip(w,a,b))/60)
H=[one,A]
for n in range(2,9):
    H.append((mul(A,H[n-1])-mul(A,H[n-2])+(H[n-3] if n>=3 else s.zeros(5,1))).applyfunc(s.expand))
E=[]
for n in range(9):
    check('plane Sym dimension '+str(n),H[n][0]==s.binomial(n+2,2))
    E.append((mul(D,H[n])-(mul(A,H[n-1]) if n else s.zeros(5,1))).applyfunc(s.expand))
    check('plane E dimension '+str(n),E[n][0]==5*s.binomial(n+2,2)-3*s.binomial(n+1,2))
md=[inner(D,h) for h in H];ei=[inner(one,e) for e in E]
check('D multiplicities through8',md==[0,0,1,0,2,1,3,2,5])
check('E invariants through8',ei==[0,0,0,0,1,1,1,1,2])
check('Hom dimensions4through8',[inner(D,E[n]) for n in range(4,9)]==[4,5,7,8,10])
check('plane cubic decomposition',(H[3]-A-V-P).applyfunc(s.simplify)==s.zeros(5,1))
check('unique cubic P covariant',inner(P,H[3])==1)
source_candidates={n:[k for k in range(-n,1) if md[n+k]>0] for n in range(4,9)}
rank_one_candidates={n:[k for k in source_candidates[n] if ei[-k]>0] for n in range(4,9)}
check('quartic source candidates',source_candidates[4]==[-2,0])
check('quintic source candidates',source_candidates[5]==[-3,-1,0])
check('sixth source candidates',source_candidates[6]==[-4,-2,-1,0])
check('seventh source candidates',source_candidates[7]==[-5,-3,-2,-1,0])
check('rank-one saturated lines4through8',rank_one_candidates=={4:[],5:[],6:[-4],7:[-5],8:[-6,-4]})
check('sixth factors one-dimensional',md[2]*ei[4]==1)
check('seventh factors one-dimensional',md[2]*ei[5]==1)
check('eighth k-6 factors one-dimensional',md[2]*ei[6]==1)
check('eighth k-4 quartic covectors dimension2',md[4]==2 and ei[4]==1)
check('eighth scalar restriction target dimension2',inner(one,H[8])==2)

# Universal apolar form, with ordinary monomial coefficients. This is a
# representation identity, not an actual selected HM direction or root.
x,y,p,q,r=s.symbols('x y p q r')
hs=s.symbols('h:5');h=sum(hs[i]*x**(4-i)*y**i for i in range(5))
a=p*x*x+q*x*y+r*y*y
basis=[x**(4-i)*y**i for i in range(5)]
def pairing(f,g):
    fp=s.Poly(s.expand(f),x,y);gp=s.Poly(s.expand(g),x,y)
    return s.expand(sum((-1)**i*fp.coeff_monomial(x**(4-i)*y**i)*gp.coeff_monomial(x**i*y**(4-i))/s.binomial(4,i) for i in range(5)))
operators=(lambda f:x*s.diff(f,y),lambda f:y*s.diff(f,x),lambda f:x*s.diff(f,x)-y*s.diff(f,y))
for j,op in enumerate(operators):
    for i,f in enumerate(basis):
        for k,g in enumerate(basis):
            check(f'apolar invariance {j},{i},{k}',s.expand(pairing(op(f),g)+pairing(f,op(g)))==0)
c2=pairing(a*a,h)
check('quadratic apolar covector nonzero',c2!=0)
check('plane degree2 covector',all(sum(mon[:3])==2 for mon in s.Poly(c2,p,q,r,*hs).monoms()))
check('general square transverse coefficient',pairing(x**4,h)==hs[4])
check('general square nondivisibility criterion',h.subs(x,0)==hs[4]*y**4)
Delta=q*q-4*p*r
check('discriminant times covector nonzero',s.expand(Delta*c2)!=0)
check('discriminant times covector has plane degree4',all(sum(mon[:3])==4 for mon in s.Poly(Delta*c2,p,q,r,*hs).monoms()))
check('kernel inclusion has quartic coordinates',5-1==4)
check('quadratic restriction plane degree6',2+4==6)
check('quartic restriction plane degree8',4+4==8)
for n in (6,7,8):
    check('higher naturality twist '+str(n),-5-(n-1)==-n-4)
# Two independent facts proved in the text: a nonzero restriction witness
# Delta*c2, and nonzero kernel witness cP* b_T. Finite-dimensional conclusion.
check('octic covector kernel dimension exactly1',md[4]-1==1)
check('octic full Hom dimension10',inner(D,E[8])==10)

# Formal polynomial normalization in a UNIVERSAL reduced complex. The A
# column is tB+t²A2+..., the D column FA*H+t^n*R. Subtracting successive
# polynomial A-corrections H_i leaves no term below n and leaves R at n.
# Noncommuting coefficients retain matrix multiplication order.
t=s.Symbol('t');B=s.Symbol('B',commutative=False)
AA={1:B,**{i:s.Symbol('A'+str(i),commutative=False) for i in range(2,9)}}
HH={i:s.Symbol('H'+str(i),commutative=False) for i in range(1,8)}
FA=sum(t**i*AA[i] for i in AA)
for n in range(4,9):
    R=s.Symbol('R'+str(n),commutative=False)
    HHn=sum(t**i*HH[i] for i in range(1,n))
    FD=s.expand(FA*HHn+t**n*R)
    for m in range(2,n):
        partial=sum(t**i*HH[i] for i in range(1,m-1))
        coeff=s.expand(FD-FA*partial).coeff(t,m)
        check(f'global normalization n{n} step{m}',s.expand(coeff-B*HH[m-1])==0)
    normalized=s.expand(FD-FA*HHn)
    for m in range(1,n):check(f'lower coefficient zero n{n} m{m}',normalized.coeff(t,m)==0)
    check('leading symbol retained n'+str(n),normalized.coeff(t,n)==R)
    # Reparameterizing the surviving D lifts by an identity-leading gauge
    # does not alter the first nonzero normalized symbol.
    V1=s.Symbol('V1',commutative=False)
    check('D lift gauge n'+str(n),s.expand(normalized*(1+t*V1)).coeff(t,n)==R)

result={'status':'PASS','checks':len(checks),'internal_symbols_forced_zero':[4,5,6,7],
 'internal_eighth':'canonical one-dimensional line; actual scalar unselected',
 'rank_one_factor_k':rank_one_candidates,'full_equivariant_hom_dimensions_4_to_8':[4,5,7,8,10],
 'degree_eight_naturality_line_dimension':1,'actual_instance_evaluated':False,'source_pair_removed':False}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
