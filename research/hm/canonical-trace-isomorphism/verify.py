"""Bounded formal-jet identities only: no forms, points, or instances selected."""
import sympy as sp
F,F1,F2,G,G1,G2,L,L1,u=sp.symbols('F F1 F2 G G1 G2 L L1 u')
def tau(d,e,P,P1,P2,R,R1,R2):
    return d*(d-1)*P*R2-2*(d-1)*(e-1)*P1*R1+e*(e-1)*P2*R
Hf=6*F*F2-4*F1**2
Hg=20*G*G2-16*G1**2
x=u*tau(3,5,F,F1,F2,G,G1,G2)/112
y=-u*Hf/20
z=u*Hg/144
FG=(F*G,F1*G+F*G1,F2*G+2*F1*G1+F*G2)
Fsq=(F**2,2*F*F1,2*F1**2+2*F*F2)
Gsq=(G**2,2*G*G1,2*G1**2+2*G*G2)
LF=(L*F,L1*F+L*F1,2*L1*F1+L*F2)
LG=(L*G,L1*G+L*G1,2*L1*G1+L*G2)
C=u**2*(tau(8,8,*FG,*FG)/1470-tau(6,10,*Fsq,*Gsq)/1350)
assert sp.expand(u*(2*F*G*x+G**2*y-F**2*z)+C)==0
b=u*(tau(8,4,*FG,*LF)/462-tau(6,6,*Fsq,*LG)/550)
Psi=L*(F*x+G*y)+b
expected=u*F*(L*(F*G2/sp.Integer(40)-F2*G/sp.Integer(12))+L1*(-F*G1/sp.Integer(5)+F1*G/sp.Integer(3)))
assert sp.expand(Psi-expected)==0
# Determinant-one covariance follows analytically from contraction by epsilon;
# this script checks only the two displayed differential identities.
print('PASS: canonical nilpotence and exact obstruction formula, universal jets only.')
