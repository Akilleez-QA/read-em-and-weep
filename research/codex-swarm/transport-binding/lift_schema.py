"""Shared typed closed-resolution lift; no source values or residual lowering."""

def source_components():
    return [
        {'id': 'baseline', 'op': 'tracefree', 'input': 'M0_0', 'gerbe': 'complete', 'legacy_scalar_correction': False},
        {'id': 'Fk12', 'op': 'scalar_times_row_end', 'scalar': 'F34', 'matrix': 'k12_ik'},
        {'id': 'Fk34', 'op': 'scalar_times_row_end', 'scalar': 'F12', 'matrix': 'k34_ik'},
        {'id': 'E12', 'op': 'directional', 'pair': [0, 1], 'input': {'op': 'scalar_solver', 'pair': [2, 3], 'input': 'F34'}},
        {'id': 'E34', 'op': 'directional', 'pair': [2, 3], 'input': {'op': 'scalar_solver', 'pair': [0, 1], 'input': 'F12'}},
    ]

def closed_lift_schema():
    nodes = [{'id': 'J0', 'cech_degree': 2, 'internal_degree': 0, 'coefficient': 1,
              'op': 'row_residual_inclusion', 'input': 'Rsharp', 'leading_owner': 'o0',
              'block': [1, 1], 'left': 'Iphys_o0', 'transpose_input': True, 'right': 'Pphys_o0'}]
    for s, sign in ((1, 1), (2, -1), (3, 1)):
        nodes.append({'id': 'J'+str(s), 'cech_degree': 2+s, 'internal_degree': -s,
                      'coefficient': sign, 'op': 'end_homotopy', 'homotopy_input_degree': 1-s,
                      'input': {'op': 'cech', 'input': 'J'+str(s-1)},
                      'leading_owner_rule': 'first vertex before any subsequent face deletion'})
    return {'schema': 'closed-resolution-lift-v1',
            'total_differential': 'D=delta_Cech+(-1)^cech_degree*d_End',
            'homotopy': 'H_r(F)=H_K F+(-1)^r E_K F H_K',
            'HK_blocks': [{'source': 1, 'target': 0, 'name': 'H0', 'shape': [5, 15]},
                          {'source': 2, 'target': 1, 'name': 'H1', 'shape': [15, 10]},
                          {'source': 3, 'target': 2, 'name': 'eta', 'shape': [10, 2]}],
            'EK': {'nonzero_block': [1, 1], 'formula': 'Iphys Pphys', 'shape': [15, 15]},
            'cech_frame': 'original fixed resolution frames; restrictions only; no extra row-End conjugation',
            'nodes': nodes,
            'closure_equations': ['d_End J0=0', 'delta J0-d_End J1=0', 'delta J1+d_End J2=0',
                                  'delta J2-d_End J3=0', 'delta J3=0'],
            'scalar_test_component': 'J2', 'top_component_required': 'J3'}
