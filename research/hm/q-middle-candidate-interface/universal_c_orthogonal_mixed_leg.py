"""A literal positive-linear mixed leg orthogonal to every actual C source.

The single leg is not claimed to be the required G-equivariant external
(a,h)-family. All physical outputs and source-projection shifts are retained.
"""
from universal_physical_mixed_leg_foundation import *

Yraw0=s.Matrix([-x,-z,0,0,-z,0]);Yraw1=s.zeros(6,1)
zeta=s.Matrix([0,x/(2*FC),0])
Y0=s.Matrix([-x/2,-z,0,0,-z,0])
Y1=s.Matrix([0,0,0,FB*x/(2*FC),0,0])
Yraw=mixed(Yraw0,Yraw1)
Yleg=mixed(Y0,Y1)
Yspin=s.Matrix([-2*z,0,0,0])
YB=s.Matrix([[0,2*u*z]])


Zcoeff=s.Matrix([0,0,0,0,2*u,0])
Zleg=vww_leg(Zcoeff)
ZA=YB
ZC=s.Matrix([[0,0,2*FD*u*u/3]])


def square_action(leg,eta,phi=1):
    return sc(phi*scalar_pairing(leg,eta),leg)

def symmetric_cross(left,right,eta,phi=1):
    return adds(sc(phi*scalar_pairing(right,eta),left),
                sc(phi*scalar_pairing(left,eta),right))
