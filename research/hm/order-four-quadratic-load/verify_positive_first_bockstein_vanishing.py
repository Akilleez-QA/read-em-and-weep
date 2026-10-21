#!/usr/bin/env python3
"""Universal bookkeeping and formal pencil identity; no actual matrix evaluation."""
from pathlib import Path
import runpy
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs=r['vadd'],r['vscale']
s=va(r['one'],r['A'],r['V'],r['D'])
t=va(r['A'],vs(2,r['V']),vs(3,r['P']),vs(4,r['D']))
c=va(t,vs(-1,s),r['one'])
assert s[0]==r['z'](12) and t[0]==r['z'](41)
assert c==va(r['V'],vs(3,r['P']),vs(3,r['D']))
assert r['inner'](c,r['A'])==r['z'](0)
assert r['inner'](s,r['A'])==r['inner'](t,r['A'])==r['z'](1)
# Formal expansion: M0 k0=0, M1 k0=M0 kz implies
# (M0+t M1)(k0-t kz)=-t^2 M1 kz.
terms={(0,'M0k0'):1,(1,'M1k0'):1,(1,'M0kz'):-1,(2,'M1kz'):-1}
terms.pop((0,'M0k0'))
terms[(1,'M0kz')]+=terms.pop((1,'M1k0'))
terms={k:v for k,v in terms.items() if v}
assert terms=={(2,'M1kz'):-1}
print('PASS: the unique A maps isomorphically once the invariant-only lower kernel is known.')
print('PASS: formal first correction cancels beta1; the residual is the stated second obstruction.')
print('No assertion about the rank or nonvanishing of beta2.')
