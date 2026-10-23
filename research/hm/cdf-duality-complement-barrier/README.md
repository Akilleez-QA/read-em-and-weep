# Duality does not force complementary c-d-f preservation

PROOF.md identifies the actual P4 and P1 dual windows, states the exact necessary transpose condition, and constructs a universal equivariant Laurent counterfamily. It respects endpoint/kernel/cokernel characters and the scalar compatible-algebra conclusion, but does not claim actual HM realization or all negative-multiplication/Bockstein relations.

Reproduce with Python 3 and SymPy:

    python verify.py
    python -O verify.py

Both runs pass46 checks. Every matrix and parameter in the checker belongs to the explicit universal synthetic counterfamily or the standard universal sl2 trace calculation. No actual HM/source data are evaluated.
