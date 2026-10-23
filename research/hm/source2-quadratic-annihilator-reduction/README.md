# Every non-V radical direction: quadratic-annihilated endpoint reduction

This extends PR957 to the unique exceptional mixed direction without an
exceptional extension splitting. For every non-V radical image I, the actual
embedded NC/I has endpoint spaces(V+D,0), so every negative quadratic kills
its initial V+D even if its first arrows are nonzero.

If the radical line is Q-compatible, restriction rank8 gives24-to-20
obstruction cancellation. Rank3 gives a permanent D plus active24-to-25 and
forces rank at most36 throughout the original41-to-37 affine family Q+Sym²W.
No existence, rank selection, source/pair cut, or wider quadric claim follows.

Read PROOF.md and the four immutable original inputs in INPUTS.json.
Reproduce using Python3 and SymPy (verified with SymPy1.14.0):

    python verify.py
    python -O verify.py

Both produce RESULT.json. Tests deliberately include nonzero first arrows
whose second composites vanish, distinguishing this theorem from zero-arrow
arguments. They are synthetic controls, not actual HM computations.
