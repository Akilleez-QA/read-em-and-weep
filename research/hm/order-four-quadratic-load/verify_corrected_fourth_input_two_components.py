"""Aggregate exact checks for the two canonical lower-source components."""
from pathlib import Path
import runpy
root=Path(__file__).resolve().parent
for name in ('verify_corrected_square_source_reduced_cubic.py','verify_endpoint_two_tensor_reconstruction.py'):
 runpy.run_path(str(root/name),run_name='__main__')
print('PASS: both actual corrected lower-source involution components are nonzero, with gamma, nu and c_eta retained.')
print('No actual next ambient division or fourth Bockstein value is supplied.')
