"""Independent exact audit over Q; run with Python and SymPy. No network."""
import sympy as sp
from itertools import product

A, B, D, E, U, V, W = sp.symbols('A B D E U V W')
coords = (A, B, D, E, U, V, W)
q = 4*A*E - B*D + U*V + U*W + V*W
k = A*D**2 + B**2*E - 4*A*E*(U+V+W) - U*V*W
assert sp.hessian(q, coords).det() == 32

# The homogeneous Segre identities, checked independently of the supplied script.
a = sp.symbols('a1:5'); b = sp.symbols('b1:5')
z = [sp.prod(a[j] if e == 0 else b[j] for j,e in enumerate(bits))
     for bits in product((0,1), repeat=4)]
f = (z[0], z[1]+z[2]+z[4]+z[8], z[7]+z[11]+z[13]+z[14],
     z[15], z[3]+z[12], z[5]+z[10], z[6]+z[9])
segre = dict(zip(coords,f))
assert sp.expand(q.subs(segre)) == 0
assert sp.expand(k.subs(segre)) == 0

# Affine quotient normal form. Capital X,Y,Z are the squares x^2,y^2,z^2.
s, X, Y, Z, T = sp.symbols('s X Y Z T')
change = {A:1, B:s, U:(s*s+X-Y-Z)/8,
          V:(s*s-X+Y-Z)/8, W:(s*s-X-Y+Z)/8,
          D:(s**3-s*(X+Y+Z)+2*T)/16}
change[E] = sp.expand((B*D-U*V-U*W-V*W).subs(change)/4)
assert sp.expand(q.subs(change)) == 0
assert sp.expand(k.subs(change)-(T*T-X*Y*Z)/64) == 0
inverse = {s:B, X:B*B-4*(V+W), Y:B*B-4*(U+W),
           Z:B*B-4*(U+V), T:B**3-4*B*(U+V+W)+8*D}
for variable in (B,D,U,V,W):
    assert sp.expand(change[variable].subs(inverse, simultaneous=True)-variable)==0

# Hadamard coordinates and invariance under the three double transpositions.
x,y,z0 = sp.symbols('x y z')
t = [(s+x+y+z0)/4, (s+x-y-z0)/4,
     (s-x+y-z0)/4, (s-x-y+z0)/4]
e3 = sum(sp.prod(t[j] for j in range(4) if j != i) for i in range(4))
assert sp.expand(e3-(s**3-s*(x*x+y*y+z0*z0)+2*x*y*z0)/16)==0

# Three singular Veronese surfaces, with distinguished coordinate U, V, or W.
r,h,v = sp.symbols('r h v')
veronese = {A:r*r, B:2*r*h, D:2*h*v, E:v*v,
            U:h*h-2*r*v, V:2*r*v, W:2*r*v}
assert sp.expand(q.subs(veronese)) == 0
assert sp.expand(k.subs(veronese)) == 0
J = sp.Matrix([[sp.diff(p,c) for c in coords] for p in (q,k)])
for i in range(7):
    for j in range(i+1,7):
        minor = J[:,[i,j]].det()
        assert sp.expand(minor.subs(veronese)) == 0

# Global complete-intersection and invariant-ring Hilbert functions agree.
def choose(n,r):
    return 0 if n<r else sp.binomial(n,r)
for n in range(80):
    ci = choose(n+6,6)-choose(n+4,6)-choose(n+3,6)+choose(n+1,6)
    invariant = ((n+1)**4+3*(n+1)**2)//4
    assert ci == invariant

print('PASS: Hessian determinant 32; homogeneous quadratic/cubic identities.')
print('PASS: A=1 image equation is exactly (T^2-XYZ)/64 after eliminating E.')
print('PASS: displayed coordinate changes are polynomial inverses over Q.')
print('PASS: Veronese parametrization lies in the Jacobian singular scheme.')
print('PASS: invariant and complete-intersection Hilbert functions, degrees 0..79.')
print('NOTE: mathematical proofs of all-degree equality, exact scheme image,')
print('quotient structure, singular scheme, fiber lengths and Chern classes')
print('are in image_geometry.md; finite computations do not replace them.')
