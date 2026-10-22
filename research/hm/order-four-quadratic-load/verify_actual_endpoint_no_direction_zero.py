"""Universal polynomial identities; no selected HM input or instance rank."""
import sympy as s
x,y,z=s.symbols('x y z')
a=s.Matrix([x,y,z]); S=a*a.T-(x*x+y*y+z*z)*s.eye(3)/3
assert s.trace(S)==0
# These identities prove S=0 forces all coordinates zero over C.
assert s.expand(x*(S[0,0]-S[1,1])+y*S[0,1])==x**3
assert s.expand(y*(S[1,1]-S[2,2])+z*S[1,2])==y**3
assert s.expand(z*(S[2,2]-S[0,0])+x*S[0,2])==z**3
print('PASS: the harmonic quadratic tensor has no nonzero zero direction.')
print('Combined with the proved actual nonzero family and irreducibility, every full endpoint fiber is nonzero.')
print('No individual-input rank, nonsquare secant, or fourth value is asserted.')
