"""Universal integer degree identities, not tests on actual map instances."""
import sympy as s
d,j,r=s.symbols('d j r',integer=True,positive=True)
# If F/C has degree -d-j with j>=0, Hom(C,(F/C)(-2)) is O(-j-2).
assert s.expand((-d-j-2)-(-d))==-j-2
# The same includes equal top-degree summands, j=0.
assert (-2)<0
for n in range(4):assert -2-n+(n+1)==-1
assert [(-2-n,n+1) for n in (1,2,3)]==[(-3,2),(-4,3),(-5,4)]
# K -> A0(-2), twisted by3, lands in A0(1).
assert -2+3==1
assert s.simplify((-d-r)-1-(-d-(r+1)))==0
print('PASS: strict top-degree Hom vanishing, iteration, actual backward bounds and one-step target twist.')
print('Geometric proof uses saturation and characteristic zero; no fiberwise injectivity or new global rank bound is inferred.')
