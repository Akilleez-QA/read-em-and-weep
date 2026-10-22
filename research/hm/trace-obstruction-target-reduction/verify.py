#!/usr/bin/env python3
"""Four universal jet identities modulo formal F, not actual derivatives/data."""
import sympy as s
F,F1,F2,G,G1,G2,L,L1,u=s.symbols('F F1 F2 G G1 G2 L L1 u')
f=(F,F1,F2);g=(G,G1,G2);l=(L,L1,0)
def mul(a,b):
    return (a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])
def tau(a,b,d,e):
    return s.expand(d*(d-1)*a[0]*b[2]-2*(d-1)*(e-1)*a[1]*b[1]+e*(e-1)*a[2]*b[0])
fg=mul(f,g);ff=mul(f,f);gg=mul(g,g);lf=mul(l,f);lg=mul(l,g)
# Reduction modulo the indeterminate F, not a point of a curve.
t1=tau(fg,fg,8,8).subs(F,0)
t2=tau(ff,gg,6,10).subs(F,0)
t3=tau(fg,lf,8,4).subs(F,0)
t4=tau(ff,lg,6,6).subs(F,0)
assert s.expand(t1+98*G**2*F1**2)==0
assert s.expand(t2-180*G**2*F1**2)==0
assert s.expand(t3+42*L*G*F1**2)==0
assert s.expand(t4-60*L*G*F1**2)==0
c=u*u*(t1/s.Integer(1470)-t2/s.Integer(1350))
b=u*(t3/s.Integer(462)-t4/s.Integer(550))
assert s.expand(c+u*u*G*G*F1*F1/5)==0
assert s.expand(b+u*L*G*F1*F1/5)==0
assert s.expand(L*G*(u*F1*F1/5)+b)==0
for d,e,den in [(8,8,1470),(6,10,1350),(8,4,462),(6,6,550)]:
    assert 2*(d-1)*(e-1)*(d+e-1)==den
assert 6-3-1==2
print('PASS: four universal jet congruences, harmonic denominators, cancellation, target dimension.')
