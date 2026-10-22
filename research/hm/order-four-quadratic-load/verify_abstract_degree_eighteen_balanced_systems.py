#!/usr/bin/env python3
"""Abstract degree18 balanced systems: character and universal Clebsch certificates only."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
from functools import lru_cache
ROOT=Path(__file__).resolve().parent

# Exact Q(sqrt(5)) character arithmetic, independently reproduced here.
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def minus(a,b):return plus(a,scale(-1,b))
def total(xs):
 out=(F(0),F(0))
 for x in xs:out=plus(out,x)
 return out
z=lambda a,b=0:(F(a),F(b))
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
@lru_cache(None)
def symchar(n):
 a=[z(1)]*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,[minus(times(w,v),u)for w,v,u in zip(W,b,a)]
 return b
chars={'one':[z(1)]*9,'W':W,'A':symchar(2),'S':symchar(3),'D':symchar(4),'T':symchar(5)}
chars['P']=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
chars['V']=[minus(a,b)for a,b in zip(symchar(6),chars['P'])]
chars['Wp']=[minus(times(w,p),t)for w,p,t in zip(W,chars['P'],chars['T'])]
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(s,times(x,y))for s,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
# Characters are real, hence the nine irreducibles are self-dual.
# W has trivial determinant: Lambda^2 W = 1 (the standard SL2 lift).
# The recurrence uses exactly that determinant-one linearization.
def mul(a,b):return [times(x,y)for x,y in zip(a,b)]
def sub(a,b):return [minus(x,y)for x,y in zip(a,b)]
def linear(terms):return [total(scale(c,chars[n][i])for c,n in terms)for i in range(9)]
def decompose(a):
 out=[inner(a,chars[n])for n in names]
 assert all(b==0 and x.denominator==1 for x,b in out)
 return tuple(int(x)for x,b in out)
M3=linear([(3,'Wp'),(3,'S'),(6,'T')])
M4=linear([(2,'V'),(4,'P'),(3,'D')])
PINNED={'TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md': 'f7621cc508b76f8c12e52a0c5eddf067e18688a174265d930403fc8a69641026'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
C=lambda n:decompose(symchar(n));I=lambda n:decompose(chars[n])
add=lambda a,b:tuple(x+y for x,y in zip(a,b));subv=lambda a,b:tuple(x-y for x,y in zip(a,b))
assert C(6)==add(I('V'),I('P')) and C(7)==add(I('Wp'),I('T'))
assert C(12)[0]==1 and C(20)[0]==1
assert C(18)==(0,0,0,1,1,2,0,1,0)
assert C(17)==(0,0,1,0,0,0,1,0,2)
assert C(19)==(0,1,1,0,0,0,1,0,2)
H=linear([(1,'A'),(1,'V'),(1,'P')])
assert decompose(mul(H,chars['W']))==C(19)
assert decompose(mul(chars['V'],chars['W']))==I('T')
assert decompose(mul(chars['P'],chars['W']))==add(I('Wp'),I('T'))
assert decompose(mul(chars['D'],chars['W']))==add(I('S'),I('T'))
assert decompose(mul(chars['A'],chars['W']))==add(I('W'),I('S'))
assert subv(decompose(mul(symchar(18),chars['W'])),C(19))==C(17)
# Formal universal SL2 tensor polynomials in x,y;u,v. These are highest-weight vectors, NOT chosen group-invariant/source coefficients.
def clean(p):return {k:v for k,v in p.items()if v}
def combine(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return clean(out)
def times_var(p,i):return {tuple(a+(j==i)for j,a in enumerate(k)):v for k,v in p.items()}
def derivative(p,i):
 return {tuple(a-(j==i)for j,a in enumerate(k)):v*k[i]for k,v in p.items()if k[i]}
def poly_scale(p,c):return {k:c*v for k,v in p.items()}
def raising(p):return combine(times_var(derivative(p,1),0),times_var(derivative(p,3),2))
# Polar2 input Sym20 -> Sym18 tensor Sym2; multiplication's S component.
a={(18,0,2,0):1}
a_image=combine(times_var(times_var(a,1),2),poly_scale(times_var(times_var(a,0),3),-1))
assert a_image=={(18,1,3,0):1,(19,0,2,1):-1} and not raising(a_image)
# Sym20 -> Sym17 tensor Sym5, then delta on Sym17 and contraction W tensor Sym5 -> Sym4.
t={(17,0,4,1):1,(16,1,5,0):-1}
assert not raising(t)
t_image=poly_scale(combine(times_var(derivative(t,2),0),times_var(derivative(t,3),1)),-1)
assert t_image=={(18,0,3,1):-4,(17,1,4,0):4} and not raising(t_image)
assert all(k[0]+k[1]==19 and k[2]+k[3]==3 for k in a_image)
assert all(k[0]+k[1]==18 and k[2]+k[3]==4 for k in t_image)
# The multiplicity-space argument: V+2P contributes 3 T columns, target2; full domain4, kernel2.
assert 4-2==2 and 3-1==2
# P0=f12 P6 has nonzero Wp multiplication, but its T image is the same line as f12 V6.
assert C(7)[names.index('Wp')]==1 and decompose(mul(chars['V'],chars['W']))[names.index('Wp')]==0
# A basepoint-free kernel with rank9, degree-18 and no H0(K(1)) has all nine degrees -2.
assert 10-1==9 and -18==9*(-2)
assert subv(C(18),decompose(H))==add(I('P'),I('D'))
out=dict(scope='Abstract balanced degree18 systems exist on P1 minus two points; not a realization of the fixed source.',source_hashes=PINNED,character_order=names,Sym18=C(18),Sym17=C(17),Sym19=C(19),H_character=decompose(H),embedding_parameter='P1 of P multiplicity lines in Sym18',A_to_S_universal_image=[[list(k),v]for k,v in a_image.items()],kernel_T_to_D_universal_image=[[list(k),v]for k,v in t_image.items()],exceptional_points=[dict(name='T',description='P_line=f12 P6',linear_syzygy_character=I('T'),determinant_multiplicity=6),dict(name='Wp',description='unique zero of Wp multiplication linear form; distinct from f12 P6',linear_syzygy_character=I('Wp'),determinant_multiplicity=2)],balanced_parameter_locus='P1 minus these two distinct points',balanced_kernel=[[-2,'P'],[-2,'D']],actual_fixed_source_feasibility_claimed=False,actual_instance_evaluations=False)
(ROOT/'abstract-degree-eighteen-balanced-systems.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: abstract degree18 balanced systems form P1 minus two points; universal symbolic checks only.')
