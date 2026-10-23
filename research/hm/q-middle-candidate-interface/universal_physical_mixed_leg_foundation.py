"""Minimal public physical foundation for C-orthogonal mixed legs.

Only universal_source_balance_helpers.py is imported. This module contains
fixed-frame cubic marking, mixed exterior contraction, the actual Cartan
D5/C splitting, and pairings/partners. It imports no diagnostic candidate,
source filter, family solve, or coefficient-specialization script.
"""
import sympy as s
from universal_source_balance_helpers import (
    x,y,z,u,w,coords,tau,omega,ixOmega,J,Ms,M,spin,cliff,Kinc,extract,
    up,low,A,B,putp,getp,adds,sc,add,scale,wedge,contract,pair,eq,eqvec)

S,T=s.symbols('mixed_binary_S mixed_binary_T')
FB,FC,FD=s.symbols('mixed_FB mixed_FC mixed_FD',nonzero=True)
f=s.Matrix([[0,0,FC,0],[-9*FB*FC/FD,0,0,0],
            [0,0,0,FD],[0,FB,0,0]])
Pstd=s.diag(1,s.Rational(1,3),-s.Rational(1,3),-1)
Cinc=Kinc*Pstd
N0,N1=s.symbols('cross_negative_N0 cross_negative_N1')

def mon(d): return [S**(d-i)*T**i for i in range(d+1)]
def coeff(p,d): return s.Matrix([s.Poly(s.expand(p),S,T).coeff_monomial(m) for m in mon(d)])
def poly(v,d): return s.expand(sum(a*b for a,b in zip(v,mon(d))))
def mark(p,marking=f): return poly(marking*coeff(p,3),3)

def mixed(d0,d1):
    """Complete physical i_x of VVW primitives, retaining VV and VW."""
    return adds(*[[contract(coords,wedge(ff,{(3+r,):1})) for ff in putp(d)]
                  for r,d in enumerate((d0,d1))])


def C_column(zsource,marking=f):
    c0=-Cinc*coeff(mark(T*zsource,marking),3)
    c1=Cinc*coeff(mark(S*zsource,marking),3)
    return mixed(c0,c1),(c0,c1)


def cartan_pair_split(marking=f):
    """D5 inclusion, multiplication, C inclusion, and regular C inverse.

    For b=(b0,b1) in Sym^3(W) tensor W, F=N0 b0+N1 b1,
    D(F)=(d_N0 F,d_N1 F)/4, z=(d_N0 b1-d_N1 b0)/4.
    Then b=D(F)+(-N1 z,N0 z), literally.
    """
    negmon=lambda d:[N0**(d-j)*N1**j for j in range(d+1)]
    nc=lambda p,d:s.Matrix([s.Poly(s.expand(p),N0,N1).coeff_monomial(m) for m in negmon(d)])
    np=lambda v,d:sum(c*m for c,m in zip(v,negmon(d)))
    D=s.Matrix.hstack(*[(marking*nc(s.diff(F,N0)/4,3)).col_join(marking*nc(s.diff(F,N1)/4,3)) for F in negmon(4)])
    C=s.Matrix.hstack(*[(-marking*nc(N1*z,3)).col_join(marking*nc(N0*z,3)) for z in negmon(2)])
    Mu=s.zeros(5,8);Zeta=s.zeros(3,8)
    for j in range(8):
        b0=np(marking.inv()*s.eye(8)[:4,j],3)
        b1=np(marking.inv()*s.eye(8)[4:,j],3)
        Mu[:,j]=nc(N0*b0+N1*b1,4)
        Zeta[:,j]=nc((s.diff(b1,N0)-s.diff(b0,N1))/4,2)
    return D,Mu,C,Zeta



def vww_leg(G):
    return [contract(coords,wedge({(i,):G[2*i+a] for i in range(3)},omega))
            for a in range(2)]


def scalar_pairing(left,right):
    value=s.cancel(pair(left,right).get((1,2,3,4),0)/x)
    eq(pair(left,right),scale(value,ixOmega))
    return s.expand(value)


