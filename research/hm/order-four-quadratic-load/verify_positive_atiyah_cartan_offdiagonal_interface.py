#!/usr/bin/env python3
"""Complete universal positive-H tensors, never an actual-source instance."""
import sympy as s,runpy,contextlib,io
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    E=runpy.run_path(str(Path(__file__).with_name('verify_universal_monad_clifford_homotopy.py')))
globals().update({k:v for k,v in E.items() if not k.startswith('__')})
def zm(A):
    assert A.applyfunc(s.expand)==s.zeros(*A.shape),A
G=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,1]])
K=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,-1,0,0],[0,0,1,0]])
c=M0.row_join(M1).row_join(M2)
j=s.Matrix.vstack(2*M1,2*M0,M2)/3
Pi=s.eye(6)-j*c;ex=s.eye(6)[:4,:]*Pi
J4=K.T*s.kronecker_product(G,J)*K
AA,BB,CC,DD,FF=s.symbols('H_A H_B H_C H_D H_F')
H=s.Matrix([[AA,BB,CC],[DD,AA,FF],[2*FF,2*CC,-2*AA]])
zm(H*G-G*H.T);assert s.trace(H)==0
HH=s.kronecker_product(-H.T,s.eye(2))
CH=ex*HH*K
zm(CH.T*J4-J4*CH);assert s.trace(CH)==0
zm(CH*CH-s.trace(H*H)*s.eye(4)/6)
zm(c*HH*j)
spin=c*HH*K
zm(spin-s.Matrix([[-CC,-3*AA,-3*FF,-DD],[-BB,3*CC,-3*AA,FF]]))
# Each free coefficient has an explicit nonzero detection, not a source rank.
assert [spin[1,0],spin[0,3],spin[0,0],spin[1,3],spin[0,1]]==[-BB,-DD,-CC,FF,-3*AA]
dPi=HH*Pi-Pi*HH
zm(Pi*dPi*Pi);zm((s.eye(6)-Pi)*dPi*(s.eye(6)-Pi))
HH5=s.zeros(5);HH5[:3,:3]=H
MH=sum(((s.Matrix([[x,y,z]])*H)[i]*Ms[i] for i in range(3)),s.zeros(2))
rh=HH5*r
hphys=s.expand((s.Matrix(1,5,coords)*rh)[0])
zm(M*MH+MH*M-2*theta*hphys*s.eye(2))
# Full natural coefficient derivatives, not fixed-wedge differentiation.
BH=[contract(coords,action(HH5,F)) for F in Bcoef(p)]
Carr=[contract(coords,action(HH5,F)) for F in C]
eq(pair(B(p),BH),{})
# Exact whole four-form identity for B*delta_H C, with all eight cs free.
pw=u*K*s.Matrix(cs[:4])+w*K*s.Matrix(cs[4:])
KH=-c*HH*pw
scalar=(p.T*J*KH)[0]
eq(pair(B(p),Carr),scale(scalar,ixOmega))
# Differentiated isotropy is retained rather than setting either term zero.
eq(add(pair(B(p),Carr),pair(BH,Cx)),{})
# Universal h-gradient identity for all ten independent coefficient symbols.
Ph=hphys*D-rh*ell
zm(s.Matrix(1,5,coords)*Ph);assert s.trace(Ph)==0
assert action(Ph,ixOmega)=={}
rhf={(i,):rh[i] for i in range(5)}
lhs=add(scale(hphys,contract(coords,action(D,Z))),scale(-1,action(Ph,contract(coords,Z))))
eq(lhs,contract(coords,wedge(rhf,contract(list(ell),Z))))
for jj in range(2):
    Lv={(i,):(Ms[i]*p)[jj] for i in range(3)}
    eq(contract(coords,wedge(rhf,contract(list(ell),Bcoef(p)[jj]))),
       contract(coords,wedge(wedge(Lv,rhf),t)))
    rc=wedge(rhf,contract(list(ell),C[jj]))
    assert set(rc).issubset({(0,1,2)})
# Exact derivative sign in the free noncommutative coefficient algebra.
U0,Up,m,ep=s.symbols('U Uprime d_M e_H',commutative=False)
derivative=Up*m+U0*ep-ep*U0-m*Up
right_diff=Up*m-m*Up
comm=ep*U0-U0*ep
assert s.expand(derivative-(right_diff-comm))==0
print('PASS: full five-symbol Cartan Clifford square and off-diagonal spin tensor.')
print('PASS: moving-projector diagonal vanishing and all five off-diagonal detections.')
print('PASS: physical Clifford anticommutator and complete eight-symbol derivative pairing.')
print('PASS: full ten-symbol h-gradient identity and both residual column types.')
print('PASS: literal natural-derivative commutator sign.')
print('No actual source coefficient, monad instance, rank, or scan was evaluated.')
