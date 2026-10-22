"""Exact full-form assembly of supported W actions, with the trace term retained.
Every coefficient is symbolic. No source/frame instance is selected.
"""
from universal_source_balance_helpers import *

def positive_wedge_matrix(polar):
    rf={(i,):polar[i] for i in range(3)}
    return s.Matrix.hstack(*[getp([wedge(rf,{(i,):s.eye(6)[2*i+j,c] for i in range(3)}) for j in range(2)]) for c in range(6)])

def supported_w_precontraction(K,polar,TW,F):
    """Return the entire VVW three-form before the final i_x.

    TW is the two-dimensional W action, not its determinant adjoint.
    The latter is tr(TW) I-TW.  No closedness assumption on F is used.
    """
    E=positive_wedge_matrix(polar)
    A=K*E+E*up*adj6(K)*low
    B=E*up*adj6(K)*low
    YY=s.Matrix.hstack(getY(F,(3,)),getY(F,(4,)))
    out=[{},{}]
    for j in range(2):
        Y=sum((TW[j,i]*YY[:,i] for i in range(2)),s.zeros(6,1))
        out=adds(out,putp(A*Y-s.trace(TW)*B*YY[:,j],(3+j,)))
    return out

def supported_w_action(K,polar,TW,F):
    return [contract(coords,f) for f in supported_w_precontraction(K,polar,TW,F)]
