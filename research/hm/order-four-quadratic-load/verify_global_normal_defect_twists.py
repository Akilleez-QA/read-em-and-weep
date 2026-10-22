#!/usr/bin/env python3
"""Line-factor bookkeeping, not a substitute for the global sheaf proof."""
canonical_X=-3
det_G=2
normal_equation=2
# Ext^2(O_2Z,O_X)=omega_2Z tensor omega_X^{-1}.
M_relative_to_omega=-canonical_X-det_G
assert M_relative_to_omega==1
normal_relative_to_omega=M_relative_to_omega-normal_equation
assert normal_relative_to_omega==-1
for t in range(-8,9):
    # Duality pairs omega_2Z(t-1) with O_2Z(1-t).
    assert (normal_relative_to_omega+t)+(1-t)==0
print('PASS: M=omega_2Z(1); first-normal defect=omega_2Z(-1).')
print('PASS: its twist-t H1 is dual to H0(O_2Z(1-t)).')
print('No negative-twist vanishing or operator-obstruction identification is asserted.')
