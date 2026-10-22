"""Universal Cartan–Koszul identities, with NO actual source specialization.

All binary sextic/cubic/quadratic, base-coordinate and Hamiltonian coefficients
are independent symbols. The only matrices below encode universal Clifford
and representation tensors. No actual monad matrix, rank, or source scan occurs.
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


# Every coefficient below is universal, not an actual-source specialization.
R=s.Matrix(4,4,s.symbols('R0:16'))
coeff=s.symbols('quartic0:5')
four=sum(coeff[i]*u**(4-i)*w**i for i in range(5))
Sfour=four*R
zeta=s.symbols('free3form0:20')
free3=[dict(zip(combinations(range(5),3),zeta[10*i:10*i+10])) for i in range(2)]
eta=[contract(coords,F) for F in free3]

def higher_lift(Sop,degree,F):
    out=[{},{}]
    for wi,i in [(u,3),(w,4)]:
        ER=E_R(Sop.diff(wi)/degree,F)
        out=adds(out,[contract(coords,wedge({(i,):1},f)) for f in ER])
    return out

TF= higher_lift(Sfour,4,eta)
for f in TF:eq(contract(coords,f),{})
eqvec(higher_lift(Sfour,4,B(p)),[{},{}])
TA=higher_lift(Sfour,4,A(p))
zero_matrix(getp(TA)-Kinc*Sfour*extract*getp(A(p)))
# This covers all 80 independent quartic operator coefficients by linearity.
print('PASS: full 80-coefficient quartic Cartan lift is polynomial, K-valued, and kills B.')

ff=s.symbols('factor0:3');gg=s.symbols('symbol0:3')
factor=ff[0]*u*u+ff[1]*u*w+ff[2]*w*w
scalar=gg[0]*u*u+gg[1]*u*w+gg[2]*w*w
Squad=scalar*R
mixed=adds(higher_lift(factor*Squad,4,eta),sc(-factor,higher_lift(Squad,2,eta)))
PB=factor.diff(u)*Squad.diff(w)-factor.diff(w)*Squad.diff(u)
jw=contract(coords,omega)
vertical=[wedge(jw,contract(coords,F)) for F in E_R(PB,eta)]
eqvec(mixed,sc(s.Rational(1,8),vertical))
zero_matrix(getp(mixed))
assert any(s.expand(F)!=0 for component in mixed for F in component.values())
print('PASS: exact product anomaly equals (1/8) j wedge i_x E_{ {f,S} }, including sign.')

# The common image is j wedge ker(i_x), and is annihilated by every such anomaly.
# Check all 16 free Cartan endomorphism coefficients, both U components,
# and every independent coefficient of an arbitrary H-valued one-form.
onecoef=s.symbols('oneform0:10')
one=[dict(zip([(i,) for i in range(5)],onecoef[5*j:5*j+5])) for j in range(2)]
jone=[wedge(jw,F) for F in one]
kill=[wedge(jw,contract(coords,F)) for F in E_R(R,jone)]
eqvec(kill,[{},{}])
for F in vertical:
    eq(contract(coords,F),{})
# Every image factor contains j, so its determinant pairing is zero.
# Universal exterior identity, not a selected point or an evaluated source.
assert wedge(jw,jw)=={}
print('PASS: each vertical anomaly kills the entire common j-wedge image; all mutual products vanish.')

# General degree product coefficient identity, checked symbolically.
deg,other=s.symbols('d e',nonzero=True)
f,fi,ss,si=s.symbols('f f_i S S_i')
assert s.simplify((fi*ss+f*si)/(deg+other)-f*si/deg-
                 (fi*ss-other*f*si/deg)/(deg+other))==0
print('PASS: arbitrary positive-degree multiplication rule retains both Leibniz terms.')
print('No actual source values, monad matrices, ranks, selected points, or scans were used.')
