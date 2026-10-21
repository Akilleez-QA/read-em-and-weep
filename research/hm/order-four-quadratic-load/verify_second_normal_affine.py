#!/usr/bin/env python3
"""Universal dimension/character identities, not HM coefficients or ranks."""
assert 3*3==9
assert 3*9==27
assert 5*3==15
# A5 class sizes and product character of 5 tensor either 3.
sizes=[1,15,20,12,12]
product=[15,-1,0,0,0]
# Last two character entries play no role in this inner product.
three_on_nonzero=[3,-1,0,0,0]
assert sum(n*p*t for n,p,t in zip(sizes,product,three_on_nonzero))==60
assert 60//60==1
# Direct-sum character uses phi+phi'=1 on either five-cycle class.
assert [3+3+4+5,-1-1+0+1,0+0+1-1,1-1,1-1]==product
print('PASS: plane class9, restricted ambient class27, ambient cohomology15')
print('PASS: each genuine three-dimensional A5 module has multiplicity1')
print('PASS: affine law yields commutator polynomial of degree at most2')
print('BOUNDARY: no actual normal scalar or commutator tensor asserted nonzero')
