# c-d-f one-sided preserved B gate

Read PROOF.md for the new conditional mathematical deduction. Run:

    python verify.py
    python -O verify.py

Requires Python 3 and SymPy. Both runs pass 35 bounded checks. No actual HM instance data are evaluated. The checker supports, but does not formalize in a proof assistant, the geometric reasoning.

Inputs are exact original bytes authenticated by Git blob and SHA256. PR935 is pinned at a7707ba3e25592023eb69cc15686aa4ee1fdcb7c, research/hm/profile11-source127-cdf-bockstein-rigidity/PROOF.md; the exact blob 187fe2a8c1499e11afdb5002091aa3c144e1b4a3 is decisive.

Status: one-sided Q preservation remains unproved/unrefuted. There is no source-pair removal.
