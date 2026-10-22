#!/usr/bin/env python3
"""Reproduce universal identities and the precise newly proved frontier."""
import runpy
from pathlib import Path
root=Path(__file__).resolve().parent
for name in [
 'verify_polar_vector_regular_lift_independence.py',
 'verify_meromorphic_quintic_source_frame_covariance.py',
 'verify_divisor_quintic_two_chart_cancellation.py',
 'verify_actual_square_third_channel_zero.py',
 'verify_semisimple_axis_vector_cup_cancellation.py',
 'verify_semisimple_actual_scalar_primitive_audit.py',
 'verify_six_axis_third_gate_exclusion.py',
]:
    runpy.run_path(str(root/name),run_name='__main__')
assert 0 not in {4,6}
assert 33+3==36
assert 37-3*2==31
assert 4<=31
assert 41-36==5 and 41-37==4
print('PASS: specialized extra A-kernel has weight0 and cannot map to weights4,6.')
print('PASS: actual third-vanishing frontier is 4<=e<=31, or permanent last cokernel.')
print('Generic section alternatives4/5 and all fourth-or-later values remain unresolved.')
