"""Independent full representation identities, never an actual source test."""
import runpy,contextlib,io,sympy as s
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):T0=runpy.run_path(str(Path(__file__).resolve().parent/'verify_universal_monad_clifford_homotopy.py'))
globals().update({k:v for k,v in T0.items() if not k.startswith('__')})
G=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,1]])
K=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,-1,0,0],[0,0,1,0]])
mm=Ms[0].row_join(Ms[1]).row_join(Ms[2])
jj=s.Matrix.vstack(2*M1,2*M0,M2)/3
Pi=s.eye(6)-jj*mm
ext=s.eye(6)[:4,:]*Pi
assert K*ext==Pi
coeff=s.symbols('r0:16');R4=s.Matrix(4,4,coeff)
d0,d1,d2=s.symbols('d0 d1 d2');phi=d0*u*u+d1*u*w+d2*w*w
RR=phi*K*R4*ext
J6=s.kronecker_product(s.eye(3),J)
RV=-J6.inv()*RR.T*J6

def adds(*Fs):return [add(*(F[j] for F in Fs)) for j in range(2)]
def getp(F):return s.Matrix([F[j].get(I,0)*sgn for I,sgn in [((1,2),1),((0,2),-1),((0,1),1)] for j in range(2)])
def putp(p):return [{I:sgn*p[2*i+j] for i,(I,sgn) in enumerate([((1,2),1),((0,2),-1),((0,1),1)])} for j in range(2)]
def getY(F,e):return s.Matrix([F[j].get((i,e),0) for i in range(3) for j in range(2)])
def putY(Y,e):return [{(i,e):Y[2*i+j] for i in range(3)} for j in range(2)]
def R2(F,aa=RR,bb=RV):
    out=putp(aa*getp(F))
    for e in [3,4]:out=adds(out,putY(bb*getY(F,e),e))
    return out

def T(F):
    out=R2(F)
    for coord,i in [(u,3),(w,4)]:
        der=R2(F,RR.diff(coord),RV.diff(coord))
        out=adds(out,[scale(-s.Rational(1,2),wedge({(i,):1},contract(coords,der[j]))) for j in range(2)])
    return out
# Use arbitrary constant three-forms to obtain universal K inputs.
from itertools import combinations
basis=list(combinations(range(5),3))
fcs=s.symbols('f0:20');gcs=s.symbols('g0:20')
f=[contract(coords,dict(zip(basis,fcs[10*i:10*i+10]))) for i in range(2)]
g=[contract(coords,dict(zip(basis,gcs[10*i:10*i+10]))) for i in range(2)]
Tf=T(f);Tg=T(g)
for F in [Tf,Tg]:
 for component in F:eq(contract(coords,component),{})
eq(add(pair(Tf,g),pair(f,Tg)),{})
for F in T(B(p)):eq(F,{})
print('Independent PASS: general End(S4) quadratic lift is K-valued, skew, and annihilates B; 16 operator and3 quadratic coefficients remain symbolic.')

# Exact common Cartan projection, including its sign and factor.
Iv=s.zeros(3)
for i,(I,sgn) in enumerate([((1,2),1),((0,2),-1),((0,1),1)]):
    cv=contract([x,y,z,0,0],{I:sgn})
    for j in range(3):Iv[j,i]=cv.get((j,),0)
Jactual=ext*s.kronecker_product(G.inv()*Iv,s.eye(2))*K
ad=s.zeros(3)
for i,Mi in enumerate(Ms):
    comm=M*Mi-Mi*M
    ad[:,i]=s.Matrix([comm[0,1],comm[1,0],comm[0,0]])
Rho=ext*(s.kronecker_product(ad,s.eye(2))+s.kronecker_product(s.eye(3),M))*K
assert all(s.expand(v)==0 for v in Jactual+s.Rational(2,3)*Rho)
print('Independent PASS: common projected contraction is exactly -(2/3) rho^3(M_v).')

# Independently reconstruct BOTH complete binary identities. No scalar solve,
# coefficient assignment, source matrix, differential rank or orbit scan.
from math import comb
ss,tt,uu,ww,hh,kk,ll=s.symbols('S T u w h k ell')
e=s.symbols('e0:7');b=s.symbols('b0:4');zz=s.symbols('z0:3')
sext=sum(e[i]*ss**(6-i)*tt**i for i in range(7))
cub=sum(b[i]*ss**(3-i)*tt**i for i in range(4))
quad=sum(zz[i]*ss**(2-i)*tt**i for i in range(3))
lin=-ww*ss+uu*tt
HD=kk*uu**2-2*hh*uu*ww-ll*ww**2
Db=lambda F:s.expand((hh*ss+ll*tt)*s.diff(F,ss)+(kk*ss-hh*tt)*s.diff(F,tt))
Nb=lambda F:s.expand(-2*lin*(uu*s.diff(F,ss)+ww*s.diff(F,tt)))
Cm=lambda F:s.expand(Db(Nb(F))-Nb(Db(F)))
Pl=lambda F:s.expand(Db(Nb(F))+Nb(Db(F)))
Jb=lambda F:s.expand(sum((-1)**i*comb(3,i)*s.diff(sext,ss,3-i,tt,i)*s.diff(F,ss,i,tt,3-i) for i in range(4)))
Dl=Db(lin)
Pm=Cm(quad)+2*HD*quad
Pp=s.expand(Pl(quad)-4*Dl*(uu*s.diff(quad,ss)+ww*s.diff(quad,tt))-2*HD*quad)
assert s.expand(Cm(lin*quad)-lin*Pm)==0
assert s.expand(Pl(lin*quad)-lin*Pp)==0
combination=s.expand(3*Db(Nb(cub))-Nb(Db(cub)))
assert s.expand(s.Rational(3,2)*Dl*cub+(ss*s.diff(combination,uu)+tt*s.diff(combination,ww))/24)==0
p=-lin*quad
ZK=Jb(Dl*quad)
YM=[];YP=[]
for coord,mult in [(uu,-tt),(ww,ss)]:
    dm=lambda F:s.expand(s.diff(Cm(F),coord)-Cm(s.diff(F,coord)))
    dp=lambda F:s.expand(s.diff(Pl(F),coord)-Pl(s.diff(F,coord)))
    YM.append(s.expand(Cm(Jb(mult*quad))-Jb(mult*Pm)+(Jb(dm(p))-dm(Jb(p)))/2))
    YP.append(s.expand(-Pl(Jb(mult*quad))-Jb(mult*Pp)+(Jb(dp(p))+dp(Jb(p)))/2))
assert s.expand(uu*YM[0]+ww*YM[1])==0
assert s.expand(uu*YP[0]+ww*YP[1])==0
# Verify the two full components directly, avoiding any coordinate division.
assert s.expand(36*ww*ZK+2*YM[0]+YP[0])==0
assert s.expand(-36*uu*ZK+2*YM[1]+YP[1])==0
print('Independent PASS: full reverse-source cubic identity and both components of 36 ZK+2 Zcomm+Zplus=0.')
print('All representation coefficients remain symbolic; no actual source or rank is evaluated.')
