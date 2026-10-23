# Zero endpoint-core homotopy exclusion

Under the actual source2 nonzero pure-V compatible-radical hypotheses,
the condition h|NC4=0 forces the canonical fourth gate R to be nonzero.
Equivalently a zero fourth gate requires the nonzero D row on NC4/I4.

The new coefficient certificate proves the full universal map
Sym2 W tensor Sym4 W -> Hom(Sym2 W,Sym4 W),
u -> (b -> C2(bu)), invertible. Its determinant in the stated monomial
bases is 5222734824996864, and its apolar recoupling scalars on
Sym6, Sym4, Sym2 are 4, 28, 84.

PROOF.md supplies actual-map transport, common-kernel identification,
and the contradiction between the forced six-dimensional terminal image
and the separated twelve-dimensional generated terminal.

Reproduce the 80 checks using Python 3 and SymPy:

    python verify.py
    python -O verify.py

Both print JSON matching RESULT.json. INPUTS.json pins nine complete public proofs,
whose bytes are retained in inputs/. No historical executable is run.
No actual source coefficient, direction, jet, matrix or instance rank
is evaluated. The theorem does not exclude source2 or select a surviving
mechanism or gate coefficient.
