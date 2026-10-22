"""Bounded free-symbol identities; no selected regular pair or source."""
import sympy as s
F1,F2,L,L1,D,D1=s.symbols('F1 F2 L L1 D D1')
left=(-42*F1*L*D1+56*F2*L*D+112*F1*L1*D)/462
left-=(-32*F1*L*D1-32*F1*L1*D+72*F2*L*D)/352
assert s.expand(left-D*(F1*L1/3-F2*L/12))==0
t,a,p,q=s.symbols('t a p q')
F=a*(t**3+p*t+q)
Q=3*s.diff(F,t,2)**2-8*s.diff(F,t)*s.diff(F,t,3)
assert s.expand(Q+12*a*a*(3*t*t+4*p))==0
assert s.expand((t**3+p*t+q)-(t*(3*t*t+4*p)/3-p*t/3+q))==0
print('PASS: source restriction; arbitrary depressed-cubic Q; exact division identity.')
