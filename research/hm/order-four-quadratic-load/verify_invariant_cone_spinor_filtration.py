#!/usr/bin/env python3
"""Universal spinor, Hilbert and character identities; no actual bundle coefficients."""
from pathlib import Path
import runpy
import sympy as s
r=runpy.run_path(str(Path(__file__).with_name('verify_twist_five_global_cohomology.py')))
q=r['r']; va,vm,vs=r['va'],r['vm'],r['vs']
z=q['z']; inn=q['inner']; fc=r['fc']
def chif(t):
    ans=vs(0,q['one'])
    for i,c in fc.items():
        if t+i>=0: ans=va(ans,vm(c,q['ambient_sym'](t+i)))
    return ans
for t,expected in [(0,va(q['A'],q['Wp'])),(1,va(q['P'],q['W'],q['S'])),(2,va(q['one'],q['A'],q['T']))]:
    assert vs(-1,chif(t))==expected
assert va(q['P'],vs(-1,chif(3)))==q['W']
assert inn(q['Wp'],va(q['P'],q['W'],q['S']))==z(0)
assert vm(q['V'],q['W'])==q['T']
assert va(q['ambient_sym'](2),vs(-1,q['one']))==va(q['A'],q['D'],q['T'])
assert inn(q['A'],q['V'])==z(0) and inn(q['Wp'],q['W'])==z(0)
a,b,u,v,A,C,D,t=s.symbols('a b u v A C D t')
M=s.Matrix([[D,C],[-A,-D]])
assert s.expand(M.det())==A*C-D**2
assert (s.Matrix([[a,b]])*M).subs({A:a*a,C:b*b,D:a*b})==s.zeros(1,2)
O=lambda t:s.prod(t+i for i in range(1,5))/24
F=lambda t:15*O(t)-10*O(t+1)+2*O(t+2)-5*O(t-1)
S=lambda t:(t+1)*(t+2)*(t+3)/3
E=s.expand(F(t+2)-F(t))
assert s.expand(E-(s.Rational(2,3)*t**3+6*t**2+s.Rational(31,3)*t-5))==0
assert s.expand(S(t)+S(t+2)-E)==9*t+27
for h0E,h1E in [(2,7),(5,10)]:
    assert int(S(2))-(h0E-2)+h1E==27
# Universal tracefree centralizer, not an actual HM matrix evaluation.
x,y,z0=s.symbols('x y z0')
N=s.Matrix([[0,1],[0,0]]); B=s.Matrix([[x,y],[z0,-x]])
assert N*B-B*N==s.Matrix([[z0,-2*x],[0,-z0]])
print('PASS: spinor relations, primary representations, forced 8+6 multiples, defect 9t+27 and h0=27, universal nilpotent centralizer.')
