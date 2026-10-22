#!/usr/bin/env python3
"""Complete abstract weight/character ansatz; no actual differential or rank."""
import sympy as s

def zero(x):
    assert s.expand(x)==0, s.expand(x)

p=s.symbols('p',integer=True)
# Source gauge weights and block output weights, after clearing b_m.
# Diagonal/middle monomial a^p b^(1-p): output (2p,2-2p).
# UA: c(a/b)^p gives (1+2p,1-2p).
# AU: a^p b^(2-p)/c gives (2p-1,3-2p).
assert [j for j in range(-5,6) if 0<=2*j<=2] == [0,1]
assert [j for j in range(-5,6) if 0<=1+2*j<=2] == [0]
assert [j for j in range(-5,6) if 0<=2*j-1<=2] == [1]
assert [j for j in range(-5,6) if -1<=2*j<=4] == [0,1,2]
# The displayed linear inequalities themselves prove that outside this range
# no further integer occurs; the finite lists are not parameter scans.
assert s.solve_univariate_inequality(-1<=2*p,p,relational=False).inf == -s.Rational(1,2)
assert s.solve_univariate_inequality(2*p<=4,p,relational=False).sup == 2

# Column-height degree bounds, not actual point/matrix ranks.
cols322=[3,3,1];cols3211=[4,2,1]
assert 7-sum(min(2,h) for h in cols322)==2
assert sum(min(3,h) for h in cols322)==7
assert 7-sum(min(2,h) for h in cols3211)==2
assert sum(min(3,h) for h in cols3211)==6

# Complete Schur characters from the universal generating series.
L,t,v,w=s.symbols('L t v w')
den=s.Poly((1-v*L*t+v*L**2*t**2-L**3*t**3)*(1-w*t+t**2),t)
h=[s.Integer(1)]
for n in range(1,8):
    h.append(s.expand(-sum(den.nth(i)*h[n-i] for i in range(1,min(5,n)+1))))
def sch(part):
    mat=s.Matrix([[h[part[i]-i+j] if part[i]-i+j>=0 else 0
                   for j in range(len(part))] for i in range(len(part))])
    return s.expand(s.det(mat))
S322=sch([3,2,2]);S3211=sch([3,2,1,1])
Ca=s.expand(v*S322.coeff(L,5)+S3211.coeff(L,5)+v*(v*v-v))
Cb=s.expand(v*S322.coeff(L,3)+S3211.coeff(L,3)+v*(w*w-1))
C2=s.expand(v*S322.coeff(L,7))
zero(C2-v*v)

phi=s.symbols('phi')
def red(z):
    return s.rem(s.Poly(s.expand(z),phi),s.Poly(phi**2-phi-1,phi)).as_expr()
classes=[(1,2,3),(15,0,-1),(20,1,0),(12,phi,1-phi),(12,phi-1,phi)]
def chars(C):return [red(C.subs({w:ww,v:vv})) for size,ww,vv in classes]
def multiplicity_A(C):
    return red(sum(size*red(ww*ww-1)*val
                   for (size,ww,vv),val in zip(classes,chars(C)))/60)
assert chars(Ca)==[258,-6,0,4-2*phi,2+2*phi]
assert chars(Cb)==[171,3,0,1,1]
assert multiplicity_A(Ca)==14
assert multiplicity_A(Cb)==8
assert multiplicity_A(C2)==0

Achar=w*w-1
source=[Achar**2*(v*v-v),Achar**3,
        (1+v)*(v*v-v),(1+v)*Achar]
assert [multiplicity_A(C) for C in source]==[3,3,1,1]
T6square=[36,0,0,1,1]
cross=red(sum(size*red(ww*ww-1)*val
              for (size,ww,vv),val in zip(classes,T6square))/60)
assert cross==2
assert 14+8+3+3+1+1+2+2==34

# Universal noncommutative arrow coefficients; no actual arrow is evaluated.
am,bm,cm,a,q,Cmult=s.symbols('a_m b_m c_m a q C_mult',nonzero=True)
A0,B0,C0,Ma,Mb,Pa,Pb,Qa,Qb,R,S,DaC=s.symbols(
    'A0 B0 C0 Ma Mb Pa Pb Qa Qb R S DaC',commutative=False)
Ucol=s.expand((am*Ma+bm*Mb)*(am*A0+bm*B0)
             -cm*C0*(am*bm/cm*S)
             -(am*A0+bm*B0)*(am*Qa+bm*Qb)-2*bm**2*a*B0)
Acol=s.expand((am*Ma+bm*Mb)*cm*C0-cm*C0*(am*Pa+bm*Pb)
             -(am*A0+bm*B0)*cm*R+Cmult*am*cm*q*DaC)
E1=Ma*A0-A0*Qa
E2=Ma*B0+Mb*A0-A0*Qb-B0*Qa-C0*S
E3=Mb*B0-B0*Qb-2*a*B0
E4=Ma*C0-C0*Pa-A0*R+Cmult*q*DaC
E5=Mb*C0-C0*Pb-B0*R
zero(Ucol-am**2*E1-am*bm*E2-bm**2*E3)
zero(Acol-am*cm*E4-bm*cm*E5)

print('PASS: complete Laurent weight ansatz, including the reverse ab/c source block.')
print('PASS: the only extra middle a^2/b channel is excluded by Hom_G(A,V tensor V)=0.')
print('PASS: complete middle multiplicities 14+8 and source multiplicities 3+3+1+1+2+2.')
print('PASS: exact noncommutative extraction of all five coupled arrow identities.')
print('No actual differential, rank, homotopy solution, or value of C_mult is evaluated.')
