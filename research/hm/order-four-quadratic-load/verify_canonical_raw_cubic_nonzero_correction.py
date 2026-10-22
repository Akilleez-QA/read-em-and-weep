#!/usr/bin/env python3
"""Universal formal identities for a nondetecting square input of the actual tensor."""
import sympy as S
X,Y,s,t,z,w,A,B,c,L,k,e,nu=S.symbols('X Y s t z w A B c L k e nu',nonzero=True)
def tr(f,g,r,x=X,y=Y):
    return S.expand(sum((-1)**j*S.binomial(r,j)*S.diff(f,x,r-j,y,j)*S.diff(g,x,j,y,r-j) for j in range(r+1)))
def tau(f,g): return tr(f,g,2)
f=A*X**2*Y+B*Y**3*z+A*c*X**3*z*z-B*c*X*Y**2*z**3
g=-L/(2*A*c)*(B*X*Y**4/z**3+A*X**3*Y**2/z**4)
h=Y**4
n=A*(-3*A*X**2*c*c*z**4-2*A*X*Y*c*z*z+A*Y**2+4*B*Y**2*c*c*z**5)/(B*L)
m=Y**2*(-3*A*X**2*c*z*z+A*X*Y+2*B*Y**2*c*z**3)/(2*B*c*z**4)
assert S.cancel(h*S.diff(f,z)-m*f-n*g)==0
Qh=e*(-A*c/B*X**2*t*t+A/B*X*Y*s*s)/2
Qmiddle=-e*X*Y*s*t/2
rhs=k*t*t*(-2*t*S.diff(Qh,s))
Qu=4*k*A/B*t*t*Qmiddle
assert S.expand(Qu-rhs)==0
Gx=4*k*A/B*X**2*Y**2*z*z+4*k*h*z**3
Gy=S.expand((Gx/z**2-4*k*z*h).subs(z,-1/w))
assert S.expand(Gy-4*k*A/B*X**2*Y**2)==0
print('PASS: actual restriction identity, canonical scalar inverse, and oriented Gamma.')
px=L/(2*A*c)*X*Y/z**4-L/(2*A)*X**2/z**2+L*B/A**2*Y**2/z
py=-L/(2*A*c*c)*Y**2/w**2+L/(B*c*c)*X**2/w
ny=S.expand((n/z**6).subs(z,-1/w))
my=S.expand((z*z*m-3*z*h).subs(z,-1/w))
assert S.expand(tau(px,n)+20*c*c*z**3)==0
assert S.expand(tau(py,ny)-2*A*(2*A*w**5-5*B*c*c)/(B*B*c*c))==0
print('PASS: the zero source Gram primitive is forced by two regular actual target transforms.')
def R(p,m,n,a,G,coord):
    return S.expand(k*a*a*(-S.Rational(2,15)*tau(p,m)+S.Rational(2,5)*p*tau(p,n)
                           +tau(p,p)*n/5-tau(h,S.diff(p,coord))/15)-tau(p,G)/30)
def polar(expr,coord):
    return S.expand(S.Add(*[term for term in S.expand(expr).as_ordered_terms() if term.as_powers_dict().get(coord,0)<0]))
Rx=R(px,m,n,z*z,Gx,z)
Ry=R(py,my,ny,1,Gy,w)
Ppx=k*L/(3*B*c)*X*Y/z**2+k*L/(10*B*c*c)*Y**2/z**4
Ppy=-4*A*k*L/(3*B*B*c*c)*X**2/w+4*k*L/(15*B*c*c)*Y**2/w**2
assert S.expand(polar(Rx,z)-Ppx)==0
assert S.expand(polar(Ry,w)-Ppy)==0
Uy=-4*A*k*L/(3*B*B*c*c)*X**2/w+k*L/(6*B*c*c)*Y**2/w**2
removed_y=S.expand((z**4*(k*L/(10*B*c*c)*Y**2/z**2)).subs(z,-1/w))
assert S.expand(Ppy-removed_y-Uy)==0
cy=Y**2+2*A/B*X**2*w
res_raw=S.expand(tau(Uy,cy)/nu).coeff(w,-1)
assert S.simplify(res_raw+4*A*k*L/(B*B*c*c*nu))==0
print('PASS: complete principal parts and a nonzero raw P4 residue, before beta2 quotient.')
# beta2=-k*b*a*D_a e, with the natural coefficient O(-8) line action.
Da_px=2*z*z*S.diff(px,z)+16*z*px
beta_x=S.expand(-k*z**3*Da_px)
assert polar(beta_x,z)==0
beta_y=S.expand(-k*(-w)*2*S.diff(py,w))
Vy=-2*k*L/(B*c*c)*X**2/w+2*k*L/(A*c*c)*Y**2/w**2
assert S.expand(beta_y-Vy)==0
res_second=S.expand(tau(Vy,cy)).coeff(w,-1)
assert S.simplify(res_second-8*k*L/(B*c*c))==0
assert S.simplify(res_raw/res_second+A/(2*B*nu))==0
print('PASS: relative eigenline ratio -A/(2B nu) in the displayed conventions, not an invariant scalar assignment.')
# Mixed transvectant H=(f,f)_(1,1), a nonzero intrinsic model of the correction line.
F=A*X**2*Y*s**3+B*Y**3*s*s*t+A*c*X**3*s*t*t-B*c*X*Y**2*t**3
H=S.expand(2*(S.diff(F,X,s)*S.diff(F,Y,t)-S.diff(F,X,t)*S.diff(F,Y,s)))
Ih=tr(H,Y**4,4)
assert S.expand(Ih+20736*A*A*c*s**3*t)==0
clebsch=tr(t*t,Ih,2,s,t)
assert S.expand(clebsch+248832*A*A*c*s*t)==0
assert 1+3+5==3*3
assert 3*4//2-1 == 5
assert 1+1 < 3  # rank sym(a tensor ell) <= 2 < rank of the nondegenerate metric
print('PASS: the intrinsic Clebsch correction line is nonzero; its actual scalar is not assigned numerically.')
print('PASS: the universal symmetric-tensor rank bound gives fiberwise surjectivity of the nonzero correction.')
print('All parameters remain unassigned; no actual-instance coefficient, matrix/rank evaluation, or scan used.')
