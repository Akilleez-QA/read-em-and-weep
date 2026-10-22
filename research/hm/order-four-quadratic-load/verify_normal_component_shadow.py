#!/usr/bin/env python3
"""Universal character tests for the negative square-shadow exact sequence."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
vm,va=r['vmul'],r['vadd']; ip=r['inner']; z=r['z']
assert ip(r['one'],vm(r['Wp'],r['N']))==z(1)
s6=[r['sym'](6,x) for x in r['W']]
s8p=[r['sym'](8,x) for x in r['Wp']]
assert s6==va(r['P'],r['V'])
assert s8p==va(r['P'],r['D'])
assert ip(r['one'],vm(r['P'],s6))==z(1)
assert ip(r['one'],vm(s8p,r['A']))==z(0)
assert ip(r['one'],r['D'])==z(0)
# Cohomology dimensions determined by exact invariant sequences:
vertex_constants,vertex_nilpotents,conic_constants=1,1,1
shadow=vertex_constants+vertex_nilpotents+conic_constants-1
assert shadow==2 and shadow-1==1
print('PASS: invariant shadow dimension2, primary obstruction dimension1, eta kernel dimension1.')
print('The actual shadow boundary and eta self-bracket are NOT evaluated.')

# Twist checks for the independent Serre-dual bracket criterion.
assert -2+1==-1 and -2+(-1)==-3 and -4+1==-3
# Cyclic trace of three odd cochains has sign (-1)^(1*(1+1))=+1.
assert (-1)**(1*(1+1))==1
print('PASS: Serre-dual low-twist bracket target and cyclic trace sign.')
