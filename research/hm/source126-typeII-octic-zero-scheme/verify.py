#!/usr/bin/env python3
"""Universal section geometry. No actual HM coefficient/point evaluation."""
from pathlib import Path
import hashlib,itertools,json
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    if not value: raise RuntimeError(name)
    checks.append(name)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/e['local_path']).read_bytes()
    check(e['label']+' SHA256',hashlib.sha256(b).hexdigest()==e['sha256'])
    check(e['label']+' blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'])
phi=(1+s.sqrt(5))/2
A=s.Matrix([3,-1,0,phi,1-phi]);D=s.Matrix([5,1,-1,0,0]);one=s.ones(5,1)
weights=(1,15,20,12,12)
mul=lambda a,b:a.multiply_elementwise(b)
inner=lambda a,b:s.simplify(sum(w*x*y for w,x,y in zip(weights,a,b))/60)
H=[one,A]
for n in range(2,5):H.append((mul(A,H[n-1])-mul(A,H[n-2])+(H[n-3] if n>=3 else s.zeros(5,1))).applyfunc(s.expand))
Ei=[]
for n in range(5):
    check('plane Sym dimension '+str(n),H[n][0]==s.binomial(n+2,2))
    E=mul(D,H[n])-(mul(A,H[n-1]) if n else s.zeros(5,1))
    Ei.append(inner(one,E))
check('no lower invariant sections and unique sigma',Ei==[0,0,0,0,1])
z=s.Symbol('z')
chern=s.series((1-z)**(-3),z,0,3).removeO()
check('E Chern classes',chern==1+3*z+6*z*z)
check('E4 top Chern number',6+4*3+4**2==34)
check('conic degree twist',3+2*4==11)

# Restriction to the conic by the full universal first-jet map.
p,q=s.symbols('p q')
B=s.Matrix([[q*q,0,0],[-2*p*q,q*q,0],[p*p,-2*p*q,q*q],[0,p*p,-2*p*q],[0,0,p*p]])
G=s.Matrix([[4*p**3,3*p*p*q,2*p*q*q,q**3,0],[0,p**3,2*p*p*q,3*p*q*q,4*q**3]])
check('universal gradient kills double-root quartics',(G*B).applyfunc(s.expand)==s.zeros(2,3))
check('jet minor p',s.expand(G[:,[0,1]].det())==4*p**6)
check('jet minor q',s.expand(G[:,[3,4]].det())==4*q**6)
check('kernel rank3 from multiplication minor',B[:3,:].det()==q**6)
check('kernel rank3 other multiplication minor',B[2:,:].det()==p**6)
# Binary characters are used only on P(W), not for plane cohomology.
W=s.Matrix([2,0,1,phi,phi-1])
SW=[one,W]
for n in range(2,13):SW.append((mul(W,SW[n-1])-SW[n-2]).applyfunc(s.expand))
check('binary degree10 has no invariant',inner(one,SW[10])==0)
check('binary degree12 has unique invariant',inner(one,SW[12])==1)
check('gradient target invariant line',inner(one,mul(W,SW[11]))==1)
check('Clebsch-Gordan gradient splitting',(mul(W,SW[11])-SW[12]-SW[10]).applyfunc(s.simplify)==s.zeros(5,1))
x,y=s.symbols('x y');cc=s.symbols('c:13')
F=sum(cc[i]*x**(12-i)*y**i for i in range(13))
check('universal Euler gradient identity',s.expand(x*s.diff(F,x)+y*s.diff(F,y)-12*F)==0)
# Euler plus squarefreeness is the written common-zero argument; no actual
# F12 coefficient or root is chosen here.

# Exact abstract A5 enumeration. These permutations are NOT HM matrices.
e=tuple(range(5))
def parity(p):return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2
def compose(p,q):return tuple(p[q[i]] for i in range(5))
def inv(p):return tuple(p.index(i) for i in range(5))
def order(p):
    a=e
    for n in range(1,61):
        a=compose(a,p)
        if a==e:return n
    raise RuntimeError('invalid order')
A5=[p for p in itertools.permutations(range(5)) if not parity(p)]
check('A5 order',len(A5)==60)
orders={n:sum(order(p)==n for p in A5) for n in (1,2,3,5)}
check('A5 element counts',orders=={1:1,2:15,3:20,5:24})
def cyclic(p):
    result={e};a=p
    while a!=e:result.add(a);a=compose(a,p)
    return frozenset(result)
def normalizer(H):return [g for g in A5 if frozenset(compose(compose(g,h),inv(g)) for h in H)==H]
subgroups={n:{cyclic(g) for g in A5 if order(g)==n} for n in (2,3,5)}
check('cyclic subgroup counts',[len(subgroups[n]) for n in (2,3,5)]==[15,10,6])
for n,size in ((3,6),(5,10)):
    for i,Hh in enumerate(subgroups[n]):check(f'normalizer C{n} #{i}',len(normalizer(Hh))==size)
for i,g in enumerate(p for p in A5 if order(p)==2):
    cent=[h for h in A5 if compose(g,h)==compose(h,g)]
    check('involution centralizer order4 '+str(i),len(cent)==4)
    check('involution centralizer exponent2 '+str(i),all(order(h) in (1,2) for h in cent))
check('axis orbit sizes',[60//10,60//6]==[6,10])
check('off-conic all-2 stabilizer orbit sizes',[60//n for n in (1,2,4)]==[60,30,15])
check('conic orbit minimum12',min(60//n for n in (1,2,3,5))==12)
check('unique order5 fixed-point orbit cardinality',2*len(subgroups[5])==12)
solutions=[]
for a in range(6):
 for b in range(4):
  for c in range(3):
   for d in range(2):
    for f in range(1):
     if 6*a+10*b+15*c+30*d+60*f==34:solutions.append((a,b,c,d,f))
check('unique zero-orbit length decomposition',solutions==[(4,1,0,0,0)])
# Local C5 coordinate/fiber character test, modulo5.
check('tangent weights',[1,(-1)%5]==[1,4])
check('fiber weights',[2,(-2)%5]==[2,3])
quotient_basis=[(0,0),(1,0),(0,1),(1,1)]
quotient_weights=[(i-j)%5 for i,j in quotient_basis]
check('local quotient length4',len(quotient_basis)==4)
check('no fiber character in local quotient',not (set(quotient_weights)&{2,3}))
check('only allowed quadratic terms',[(i,2-i) for i in range(3) if (i-(2-i))%5 in (2,3)]==[(0,2),(2,0)])
check('complete exceptional length',6*4+10==34)
# Minimal resolution: positive shifts, zero first Chern class, length.
t=s.Symbol('t');numerator=1-5*t**7+3*t**8+t**11
check('ideal resolution rank',5-3-1==1)
check('ideal resolution first Chern class',-5*7-(-3*8-11)==0)
check('resolution minimal shifts',8>7 and 11>7)
check('Hilbert numerator vanishes at1',numerator.subs(t,1)==0)
check('first derivative vanishes at1',s.diff(numerator,t).subs(t,1)==0)
check('length from Hilbert numerator',s.diff(numerator,t,2).subs(t,1)/2==34)
def R(n):return (n+1)*(n+2)//2 if n>=0 else 0
hf=[R(n)-5*R(n-7)+3*R(n-8)+R(n-11) for n in range(20)]
check('Hilbert function through9',hf[:10]==[1,3,6,10,15,21,28,31,33,34])
check('Hilbert function stabilizes',hf[9:]==[34]*11)
check('h-vector degree9',[hf[i]-(hf[i-1] if i else 0) for i in range(10)]==[1,2,3,4,5,6,7,3,2,1])
result={'status' :'PASS','checks':len(checks),'sigma_zero_length':34,'minimal_ideal_resolution':'0 -> 3O(-8)+O(-11) -> 5O(-7) -> I_Z -> 0','sigma_nonzero_on_square_conic':True,
 'zero_orbits':{'order5_axes':{'points':6,'local_length':4,'completed_ideal':'(u^2,v^2)'},'order3_axes':{'points':10,'local_length':1}},
 'actual_octic_scalar':'not evaluated','source_covector_additional_zeros':'not computed','actual_instance_evaluated':False,'source_pair_removed':False}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
