"""Clean universal exterior, Euler and binary Clebsch definitions.
Only public verify_universal_monad_clifford_homotopy.py is imported.
No curve division, operator exclusions, or actual coefficients occur.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sympy as s
from math import comb

# Reuse the frozen, independently checked exterior algebra helpers, quietly.
with redirect_stdout(StringIO()):
    exec(Path(__file__).with_name('verify_universal_monad_clifford_homotopy.py').read_text())

# Complete universal Cartan projector and its induced alternating pairing.
G=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,1]])
Kinc=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,-1,0,0],[0,0,1,0]])
cliff=Ms[0].row_join(Ms[1]).row_join(Ms[2])
spin=s.Matrix.vstack(2*M1,2*M0,M2)/3
assert cliff*spin==s.eye(2)
Pi=s.eye(6)-spin*cliff
extract=s.eye(6)[:4,:]*Pi
assert Kinc*extract==Pi and Pi*Pi==Pi
up=s.kronecker_product(G,s.eye(2)); low=up.inv()
J4=Kinc.T*s.kronecker_product(G,J)*Kinc
assert J4.T==-J4 and J4.det()!=0

def getp(F,extra=()):
    return s.Matrix([F[j].get(tuple(sorted(I+extra)),0)*sgn
                     for I,sgn in [((1,2),1),((0,2),-1),((0,1),1)] for j in range(2)])
def putp(p,extra=()):
    return [{tuple(sorted(I+extra)):sgn*p[2*i+j]
             for i,(I,sgn) in enumerate([((1,2),1),((0,2),-1),((0,1),1)])} for j in range(2)]
def getY(F,extra):
    return s.Matrix([F[j].get((i,)+extra,0) for i in range(3) for j in range(2)])
def putY(Y,extra):
    return [{(i,)+extra:Y[2*i+j] for i in range(3)} for j in range(2)]
def adds(*Fs):return [add(*(F[j] for F in Fs)) for j in range(2)]
def sc(c,F):return [scale(c,f) for f in F]
def eqvec(F,G):
    for f,g in zip(F,G):eq(f,g)
def zero_matrix(M):assert M.applyfunc(s.expand)==s.zeros(*M.shape)
def embeddings(R):
    Radj=J4.inv()*R.T*J4
    return Kinc*R*extract,up*Kinc*Radj*extract*low

def E_R(R,F):
    Rp,RadjY=embeddings(R)
    out=putp(Rp*getp(F))
    for i in [3,4]:out=adds(out,putY(-RadjY*getY(F,(i,)),(i,)))
    return out

def F_R(R,F):
    Rp,RadjY=embeddings(R)
    out=[{},{}]
    for i in [3,4]:out=adds(out,putp(Rp*getp(F,(i,)),(i,)))
    return adds(out,putY(-RadjY*getY(F,(3,4)),(3,4)))



# Complete six-space, including BOTH Cartan-spin off-diagonal blocks.
J6=s.kronecker_product(G,J)
def adj6(R):return J6.inv()*R.T*J6
def fullE(R,F):
 out=putp(R*getp(F))
 for i in [3,4]:out=adds(out,putY(-up*adj6(R)*low*getY(F,(i,)),(i,)))
 return out

def fullF(R,F):
 out=[{},{}]
 for i in [3,4]:out=adds(out,putp(R*getp(F,(i,)),(i,)))
 return adds(out,putY(-up*adj6(R)*low*getY(F,(3,4)),(3,4)))

def fullT(R,degree,F):
 out=[{},{}]
 for wi,i in [(u,3),(w,4)]:
  out=adds(out,[contract(coords,wedge({(i,):1},ff)) for ff in fullE(R.diff(wi)/degree,F)])
 return out

ha,hb,hc,hd,hf=s.symbols('ha hb hc hd hf')
H3=s.Matrix([[ha,hb,hc],[hd,ha,hf],[2*hf,2*hc,-2*ha]])
H5=s.zeros(5);H5[:3,:3]=H3
HH=s.kronecker_product(-H3.T,s.eye(2))
rh=H5*r
jw=contract(coords,omega);jvec=s.Matrix([jw.get((i,),0) for i in range(5)])
Hb=(s.Matrix(1,5,coords)*D*jvec)[0];abase=Hb/2

# Arbitrary coefficient operator on VVW, with nontrivial W action.
def FW(K,F):
 out=[{},{}]
 for i in [3,4]:
  for j in [3,4]:out=adds(out,putp(D[j,i]*K*getp(F,(i,)),(j,)))
 return out

def FWadj(K,F):
 out=[{},{}]
 for i in [3,4]:
  for j in [3,4]:out=adds(out,putY(-D[j,i]*up*adj6(K)*low*getY(F,(i,)),(j,)))
 return out

def TP(K,F):
 out=[{},{}]
 for i in range(3):
  ffirst=FW(K,[wedge({(i,):1},ff) for ff in F])
  fsecond=[wedge({(i,):1},ff) for ff in FWadj(K,F)]
  out=adds(out,sc(abase*rh[i],[contract(coords,ff) for ff in adds(ffirst,sc(-1,fsecond))]))
 return out

S,T=s.symbols('bs bt')
mon=lambda n:[S**(n-j)*T**j for j in range(n+1)]
def coeff(p,n):return s.Matrix([s.Poly(s.expand(p),S,T).coeff_monomial(m) for m in mon(n)])
def tv(p,q,r):
 return s.expand(sum((-1)**j*s.binomial(r,j)*s.diff(p,S,r-j,T,j)*s.diff(q,S,j,T,r-j) for j in range(r+1)))
def rep(fun,n):return s.Matrix.hstack(*[coeff(fun(p),n) for p in mon(n)])
binary_E=rep(lambda p:S*s.diff(p,T),3);binary_F=rep(lambda p:T*s.diff(p,S),3);binary_H=rep(lambda p:S*s.diff(p,S)-T*s.diff(p,T),3)
E1=s.Matrix([[0,1],[0,0]]);F1=E1.T;H1=s.diag(1,-1);J1=s.Matrix([[0,1],[-1,0]])
J3=s.zeros(4)
for j in range(4):J3[j,3-j]=(-1)**j/s.binomial(3,j)
def simp(X):return X.applyfunc(s.factor)
def op4(p):return rep(lambda z:tv(p,z,2)/12,3)
def op6(p):return rep(lambda z:tv(p,z,3)/120,3)
g=s.symbols('g0:5');gen4=sum(c*m for c,m in zip(g,mon(4)));OG=op4(gen4)
# Extract the inverse using COMPLETE polynomial coefficients, not input values.
# The complete system assumes typed matrices; use the five triangular entries.
entries=[(0,2),(0,1),(0,0),(1,0),(2,0)]
GG=s.symbols('o0:5')
recovery=s.solve([OG[i,j]-v for (i,j),v in zip(entries,GG)],g,dict=True)[0]
def quartic(Q):
 vals=dict(zip(GG,[Q[i,j] for i,j in entries]))
 return s.expand(sum(recovery[c].subs(vals)*m for c,m in zip(g,mon(4))))
assert s.expand(quartic(OG)-gen4)==0

def mixed5(p):return s.Matrix.hstack(*[coeff(tv(p,z,1)/4,3) for z in mon(1)])

if __name__ == '__main__':
 R6=s.Matrix(6,6,s.symbols('test_six0:36'))
 zz2=s.symbols('test_form2_0:20'); zz3=s.symbols('test_form3_0:20')
 F2=[dict(zip(combinations(range(5),2),zz2[10*j:10*j+10])) for j in range(2)]
 F3=[dict(zip(combinations(range(5),3),zz3[10*j:10*j+10])) for j in range(2)]
 eq(pair(fullF(R6,F3),F2),scale(-1,pair(F3,fullE(R6,F2))))
 eq(pair(FW(R6,F3),F2),pair(F3,FWadj(R6,F2)))
 for i in [3,4]:
  eqvec(fullF(R6,[wedge({(i,):1},ff) for ff in F2]),[wedge({(i,):1},ff) for ff in fullE(R6,F2)])
 assert s.expand(quartic(op4(gen4))-gen4)==0
 print('PASS: all36-symbol determinant adjoints, wedge/Euler conventions and complete quartic Clebsch inversion.')
