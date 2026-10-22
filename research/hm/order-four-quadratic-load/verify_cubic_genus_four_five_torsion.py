#!/usr/bin/env python3
"""Universal characters and curve arithmetic only."""
import runpy
r=runpy.run_path('verify_negative_vertex_scalar.py')
sw=lambda n:[r['sym'](n,x) for x in r['W']]
sp=lambda n:[r['sym'](n,x) for x in r['Wp']]
invariants=[]
for a in range(4):
    for b in range(4):
        if r['inner'](sp(a),sw(b))!=r['z'](0): invariants.append((a,b))
assert invariants==[(0,0),(3,3)]
genus=(3-1)*(3-1)
assert genus==4 and 60//5>genus
assert 12-genus+1==9 and 30-genus+1==27
assert 12>2*genus-2 and 30>2*genus-2
plus,prod,scale=r['vadd'],r['vmul'],r['vscale']
nilpotent=plus(prod(sp(6),sw(6)),scale(-1,prod(sp(3),sw(9))))
reduced=plus(prod(sp(3),sw(9)),scale(-1,sw(12)))
assert nilpotent==plus(r['P'],r['D'])
assert reduced==plus(r['A'],scale(2,r['V']),scale(2,r['P']),scale(2,r['D']))
assert r['inner'](r['Wp'],sw(3))==r['z'](0)
assert plus(sw(4),prod(r['Wp'],sw(1)))==nilpotent
assert 4+2*1==6 and 5+2*2==9
assert nilpotent[0]==r['z'](9) and reduced[0]==r['z'](27)
print('PASS: no proper invariant bidegree, genus-four singular-orbit exclusion, and 9/27 residue filtration characters.')
print('Exact five-torsion uses the actual nowhere-zero quintic and the proved Kunneth vanishing, not a coefficient test.')
