#!/usr/bin/env python3
"""Exact marked scalar consequences, with no actual source specialization."""
import sympy as s

r,chi,g,rho,theta,Cap,Kcup,Cres=s.symbols(
    'r chi g_L rho_C theta C_ap K_cup C_res', nonzero=True)
nu,ell,ss,tt=s.symbols('nu ell s t', nonzero=True)
def zero(x):
    assert s.cancel(x)==0, s.factor(x)
kap=-chi*r/g
ratio=2*rho*g/(theta*chi*r)
zero(ratio+2*rho/(theta*kap))
cplus=Cap*r/(2*Kcup)
k=theta*Cap*chi/(4*Cres*Kcup*g)
zero(cplus/k-ratio.subs(rho,Cres*r**2))
zero(-cplus/k+ratio.subs(rho,Cres*r**2))
qchange={chi:chi/nu,Cap:nu*Cap,Kcup:nu**2*Kcup}
zero(kap.subs(qchange,simultaneous=True)-kap/nu)
zero(cplus.subs(qchange,simultaneous=True)-cplus/nu)
zero(k.subs(qchange,simultaneous=True)-k/nu**2)
zero(ratio.subs(qchange,simultaneous=True)-nu*ratio)
serre={rho:rho/ell**2,theta:theta/ell**2,Cres:Cres/ell**2}
zero(ratio.subs(serre,simultaneous=True)-ratio)
zero(k.subs(serre,simultaneous=True)-k)
channels={chi:ss**2*chi,g:ss**3*g/tt,r:ss*r/tt}
zero(kap.subs(channels,simultaneous=True)-kap)
zero(ratio.subs(channels,simultaneous=True)-ratio)
zero(kap.subs(r,-r)+kap)
zero(ratio.subs(r,-r)+ratio)
zero(cplus.subs(r,-r)+cplus)
zero(k.subs(r,-r)-k)
print('PASS: exact positive-endpoint and bracket-normalized signs.')
print('PASS: normal-root comparison and fixed-boundary k normalization.')
print('PASS: physical q0, Serre marking, channel marking, and endpoint exchange.')
print('All source coefficients and normalization constants remain unassigned.')
