#!/usr/bin/env python3
"""Universal identities only. All A,B,c,L,k remain indeterminates.
No actual coefficient assignment, actual-instance matrix/rank evaluation,
source instance, local-model experiment, or scan is used.
"""
import sympy as S
X,Y,z,w,A,B,c,L,k=S.symbols('X Y z w A B c L k',nonzero=True)
def tau(f,g):return S.expand(S.diff(f,X,2)*S.diff(g,Y,2)-2*S.diff(f,X,Y)*S.diff(g,X,Y)+S.diff(f,Y,2)*S.diff(g,X,2))
def detH(f):return tau(f,f)/2
f=A*X**2*Y+B*Y**3*z+A*c*X**3*z*z-B*c*X*Y**2*z**3
g=-L/(2*A*c)*(B*X*Y**4/z**3+A*X**3*Y**2/z**4)
h=X**2*Y**2
a=z*z
u=-2*k*A/B*X**4*z*z-2*k*A/(B*c)*X**3*Y-2*k/c*X*Y**3*z
nX4=(X**2*(-4*A*z+B*c*c*z**6)+2*B*c*X*Y*z**4-3*B*Y**2*z*z)/L
rr=S.symbols('rr')
nh=S.expand(S.cancel(S.rem(rr*rr*nX4.subs({X:1,Y:rr}),f.subs({X:1,Y:rr}),rr)).subs(rr,Y/X)*X*X)
mh=S.cancel((h*S.diff(f,z)-nh*g)/f)
assert not S.denom(mh).has(X,Y)
vH=L*X/(8*c*z**4)
def calc_error(f,g,a,u,vH,coord):
    H=k*a*h
    ap=S.diff(a,coord)
    def D(F):return S.expand(2*a*S.diff(F,coord)+ap*(X*S.diff(F,X)+Y*S.diff(F,Y))/2)
    Lambda=2*k*a*ap*h-u
    # Recover n_h by the exact restriction identity already proved in x,
    # transporting by its true O(6) factor on the y chart.
    n=nh if coord==z else S.expand((nh/z**6).subs(z,-1/w))
    m=S.cancel((H*D(f)-2*k*a*a*n*g)/f)
    cc=-2*k*a*a*n
    bb=Lambda/2-m
    dd=S.cancel(((Lambda-m)*g-H*D(g))/f)
    assert not S.denom(dd).has(X,Y)
    # Exact two rows of the section-line operator equation.
    assert S.cancel(H*D(f)+bb*f+cc*g-Lambda*f/2)==0
    assert S.cancel(H*D(g)+dd*f-bb*g-Lambda*g/2)==0
    t11=tau(f,g)/112+vH*f
    t12=-detH(f)/20
    t21=detH(g)/144+2*vH*g
    error=(tau(H,D(f*g))/462+tau(cc,g*g)/198+tau(dd,f*f)/550-tau(Lambda,f*g)/462
           +H*D(t11)+(2*H*ap-Lambda)*t11+cc*t21-dd*t12)
    return S.expand(error),[S.factor(t) for t in (m,cc,bb,dd)]
ex,conn=calc_error(f,g,a,u,vH,z)




fy=S.expand((f/z**3).subs(z,-1/w));gy=S.expand((g*z**5).subs(z,-1/w))
uy=S.expand((u/z**2).subs(z,-1/w));vy=S.expand((vH*z**5).subs(z,-1/w))
ey,_=calc_error(fy,gy,S.Integer(1),uy,vy,w)

assert S.expand(ey-ex.subs(z,-1/w))==0
print('PASS: full absolute error has exact oriented two-chart coefficient covariance.')
# Verify the actual regular target transitions in the intrinsic double-cubic coordinate.
px=L/(2*A*c)*X*Y/z**4-L/(2*A)*X**2/z**2+L*B/A**2*Y**2/z
py=-L/(2*A*c*c)*Y**2/w**2+L/(B*c*c)*X**2/w
gx=S.expand(g+px*f);gyreg=S.expand(gy+py*fy)
vx=S.expand(vH+tau(f,px)/16);vyreg=S.expand(vy+tau(fy,py)/16)
exreg,_=calc_error(f,gx,a,u,vx,z)
eyreg,_=calc_error(fy,gyreg,S.Integer(1),uy,vyreg,w)
for ff,gg,ggp,ee,eep,var in [(f,g,gx,ex,exreg,z),(fy,gy,gyreg,ey,eyreg,w)]:
    difference=S.cancel((eep*gg**2-ee*ggp**2)/ff**2)
    assert not S.denom(difference).has(X,Y)
    print('PASS: double-cubic source-change divisibility in chart',var)
    assert all(t.as_powers_dict().get(var,0)>=0 for t in S.Add.make_args(S.expand(eep)))
    print('PASS: absolute error polynomial is regular in chart',var)



# The ACTUAL scalar inverse, checked via formal socle identities.
e=S.symbols('e',nonzero=True)
QX4=e*(-B/(2*A)*X*Y*z**2-B/(2*A*c)*Y**2)
QX3Y=e*(X**2*z+B/A*Y**2*z**2)/4
QXY3=e*(-A/B*X**2+Y**2*z)/4
Qh=-e*X*Y*z/2
Qu=S.expand(-2*k*A/B*z*z*QX4-2*k*A/(B*c)*QX3Y-2*k/c*z*QXY3)
assert S.expand(Qu-k*a*(2*a*S.diff(Qh,z)-2*S.diff(a,z)*Qh))==0
print('PASS: actual O(2) coefficient-line Lie derivative and socle inverse.')

# Explicit absolute numerator, not merely a vector-cochain shadow.
P=(6*A**3*X**8*c**2*z**4+12*A**3*X**7*Y*c*z**2+6*A**3*X**6*Y**2
   -18*A**2*B*X**6*Y**2*c**2*z**5-2*A**2*B*X**5*Y**3*c*z**3+21*A**2*B*X**4*Y**4*z
   +18*A*B**2*X**4*Y**4*c**2*z**6-32*A*B**2*X**3*Y**5*c*z**4+24*A*B**2*X**2*Y**6*z**2
   +4*B**3*X**2*Y**6*c**2*z**7-18*B**3*X*Y**7*c*z**5+9*B**3*Y**8*z**3)
assert S.expand(ex+L*k*P/(30*A*B*c*c*z**4))==0
assert S.expand(vx-7*B*L*c*X*z/(8*A))==0
assert S.expand(vyreg-7*L*Y*w/(8*c*c))==0
print('PASS: unique actual Hessian primitive and displayed absolute numerator.')

# Independently verify the harmonic Euler-Gram conversion on COMPLETE
# abstract monomial bases, not on any actual cubic/quintic instance.
from functools import lru_cache
x0,y0,z0=S.symbols('x0 y0 z0')
q=x0*z0-y0*y0
lap=lambda pp:S.diff(pp,x0,z0)-S.diff(pp,y0,2)/4
@lru_cache(None)
def lift_mon(i,j):
    m=(i+j)//2; parity=i%2
    pp=x0**((i-parity)//2)*y0**parity*z0**((j-parity)//2)
    out=pp; coeff=S.Integer(1); derivative=pp
    for j0 in range(1,m//2+1):
        derivative=lap(derivative)
        coeff=-coeff/(j0*(S.Rational(2*m+1,2)-j0))
        out+=coeff*q**j0*derivative
    return S.expand(out)
def lift(pp):
    return S.expand(sum(coeff*lift_mon(i,j) for (i,j),coeff in S.Poly(pp,X,Y).terms()))
count=0
for pdeg,qdeg in [(3,3),(3,5),(5,5)]:
    for i in range(pdeg+1):
        for j in range(qdeg+1):
            ff=X**i*Y**(pdeg-i);gg=X**j*Y**(qdeg-j)
            f1,f2=lift(S.diff(ff,X)/pdeg),lift(S.diff(ff,Y)/pdeg)
            g1,g2=lift(S.diff(gg,X)/qdeg),lift(S.diff(gg,Y)/qdeg)
            gram=x0*f1*g1+y0*(f1*g2+f2*g1)+z0*f2*g2
            correction=tau(ff,gg)/(2*pdeg*qdeg*(pdeg+qdeg-1))
            diff=S.expand(gram-lift(ff*gg)-q*lift(correction))
            assert S.reduced(diff,[q*q],x0,y0,z0)[1]==0
            count+=1
assert count==76
assert S.Rational(1,210)+S.Rational(1,240)==S.Rational(1,112)
assert -S.Rational(1,45)-S.Rational(1,36)==-S.Rational(1,20)
assert S.Rational(1,225)+S.Rational(1,400)==S.Rational(1,144)
print('PASS: all 76 harmonic Euler-Gram basis identities and Hessian conversion.')
print('No fourth Bockstein value is asserted.')

# Full tangent equation, independently retaining both operator end actions.
H=k*a*h; ap=S.diff(a,z)
D=lambda pp:S.expand(2*a*S.diff(pp,z)+ap*(X*S.diff(pp,X)+Y*S.diff(pp,Y))/2)
Lam=2*k*a*ap*h-u
m,cc,bb,dd=conn
T=tau(f,g)/112+vH*f
T12=-detH(f)/20
T21=detH(g)/144+2*vH*g
E12=S.expand(-tau(H,D(f*f))/270-2*tau(bb,f*f)/270-2*tau(cc,f*g)/126+tau(Lam,f*f)/270
    +H*D(T12)+u*T12+2*bb*T12-2*cc*T)
E21=S.expand(tau(H,D(g*g))/702+2*tau(dd,f*g)/910-2*tau(bb,g*g)/702-tau(Lam,g*g)/702
    +H*D(T21)+u*T21+2*dd*T-2*bb*T21)
assert S.expand(2*f*g*ex+g*g*E12-f*f*E21)==0
assert not S.denom(S.cancel(E12/f)).has(X,Y)
assert not S.denom(S.cancel(E21/g)).has(X,Y)
print('PASS: full absolute error is tangent with both exact regular-pair divisibilities.')
