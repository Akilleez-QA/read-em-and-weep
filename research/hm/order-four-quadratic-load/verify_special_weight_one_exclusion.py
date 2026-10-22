#!/usr/bin/env python3
"""Independent universal weights/polarization/trace check, no actual coefficients."""
from fractions import Fraction
from math import comb
mod=5
wX,wY=1,4
wt=lambda a,b:(a*wX+b*wY)%mod
assert wt(4,0)==4 and wt(3,1)==2
# O(-3) weight3 calibrates t,w, so O(1) weight-1.
assert (3+wX)%mod==4 and (3+wY)%mod==2
assert [(-(a+2))%mod for a in [12,14,18]]==[1,4,0]
assert wt(7,1)==wt(2,6)==1
source=[(4,0),(2,2),(1,3),(0,4)]
# Polynomial function weights for S=x²z,G=xz²−tau y³,J=xyz,K=xy².
fun=[(-4)%mod,(-8)%mod,(-1-4)%mod,(-2)%mod]
assert fun==[1,2,0,3]
assert [(2+wt(*ab))%mod for ab in source]==fun
coef_7_1=Fraction(2*comb(4,0)*comb(4,1),comb(8,1))
coef_GK=Fraction(2*comb(4,2)*comb(4,4),comb(8,6))
coef_J2=Fraction(comb(4,3)**2,comb(8,6))
assert (coef_7_1,coef_GK,coef_J2)==(1,Fraction(3,7),Fraction(4,7))
assert coef_GK+coef_J2==1
# On z=0: G=-tau y³, K=xy², J=0, q0=rho x².
shadow_trace=(1,5)
q0_trace=(2,0)
forbidden=tuple(a+b for a,b in zip(shadow_trace,q0_trace))
assert forbidden==(3,5)
allowed={(4,4),(2,6),(0,8)}
assert forbidden not in allowed
assert 12*(7-3)==48>20==4*(8-3)
print('PASS: source boundary weight1 conflicts with scalar a14 weight4 and a18 weight0; a12 weight1 survives.')
print('PASS: wedge weights, Cartan coefficients3/7 and4/7, forbidden x³y⁵ trace, Wronskian48>20.')
print('No actual coefficients, selected matrices, evaluated ranks, or local-model experiment computed.')
