"""Universal free-bicubic identities and product-line cohomology only."""
import sympy as s
r0,r1,w0,w1=s.symbols('r0 r1 w0 w1')
c=s.symbols('c0:16')
F=sum(c[4*i+j]*r0**i*r1**(3-i)*w0**j*w1**(3-j) for i in range(4) for j in range(4))
r=s.Matrix([r0,r1])
row=s.Matrix([[-r1,r0]])
M=r*row
assert M*r==s.zeros(2,1)
assert M*M==s.zeros(2,2)
polar=s.Matrix([[s.diff(F,r0)/3,s.diff(F,r1)/3]])
assert s.expand((polar*r)[0]-F)==0
assert s.expand(row.col_join(polar).det()+F)==0

def p1(n):
    return (max(n+1,0),max(-n-1,0))
def hh(a,b):
    x,y=p1(a); z,t=p1(b)
    return (x*z,x*t+y*z,y*t)
assert hh(-1,3)==(0,0,0)
assert hh(-4,0)==(0,3,0)
assert hh(2,3)==(12,0,0)
assert hh(4,2)==(15,0,0)
source=2*hh(2,3)[0]+3*hh(4,2)[0]
target=6*hh(4,3)[0]
line=hh(5,3)[0]
curve=hh(4,6)[0]-hh(1,3)[0]
assert (source,target,line,curve)==(69,120,24,27)
assert target-source==line+curve==51
print('PASS: free bicubic Euler/null-Clifford identities and cohomology dimensions 69 -> 120 -> 51.')

print('Equivariant splitting and actual support identification are proved in the note, not inferred from this arithmetic check.')
