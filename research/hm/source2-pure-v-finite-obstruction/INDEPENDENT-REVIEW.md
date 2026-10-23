# Independent review: finite global corrected-lift criterion

## Conclusion and binding

The theorem is sound under its retained actual-source hypotheses. The review binds to `PROOF.md` SHA256 `d1f96ad68df6781474e0aa247625b08de8cfc06e2af854418cbd32ce52469140` and `verify.py` SHA256 `ebcc295dd16ffb45dc1d1c8825ac090122c84f4917820e6198d72701340ea89f`.

The result is a finite conditional criterion, not an evaluation of any actual obstruction or a determination of which generic rank occurs. The sixth target has dimension three; the first equivariant kappa ambiguity is at original order nine. The comparison and stopping rule concern the original 37-by41 positive component only.

## Actual correction and gauge audit

The starting maps are actual original corrections: `qx0=i_P`, with `x0=s`, and `qxi=-T x_(i-1)`. Their initial existence is supplied by the pinned quotient-third construction. The radical identity gives `j4 T x_(n-1)=L j2 x_(n-1)`, so the order-n quotient representative lands in J before any passage to generic fibers. Correction changes contribute earlier, vanishing page symbols or the existing second image B. Since B is injective as a sheaf, no additional A source sheaf survives. This does not describe extra A kernels after specialization.

For a zero class, the injective kernel map `(m,kappa)` identifies its source bundle with the kernel sheaf. Its inverse there yields a unique global decomposition `C_n=m g_n+kappa c_n`; no local rational inverse or gluing obstruction is introduced. The dimensions of Hom spaces are not being used to infer this existence.

The essential simultaneous update is correct. The actual first A correction satisfies both `q u_A=-T a_A` and `j2 u_A=-mu m`, the latter by applying h. Adding `a_A g_n/mu` to `x_(n-2)` and `u_A g_n/mu` to `x_(n-1)` preserves the earlier equation and changes the next equation by exactly the matching `-T a_A g_n/mu`. Its radical image becomes `kappa c_n`. There is no assertion that this raw remainder is zero. The identity `L kappa=0`, together with `ker j4=im q`, is sufficient for the next correction through a fixed equivariant inverse of q. All degrees match, and the previous radical image is unchanged because `j2 a_A=0`.

Substituting `p=L_a d` gives the original string `d,-x0(Ld),...,-x_(n-1)(Ld)`. Cancellation proves the minus sign and the one-order shift in the comparison. Generic surjectivity of L and torsion-freeness of J prove that its original obstruction is identically zero exactly when s_n is zero globally. They are not used to identify special fiber pages.

## Finite stopping rule

With the known 33 unit and three order-two factors, a first nonzero s_n supplies precisely the final exponent n+1. If all classes through s23 vanish, the global string extends through x23 and cancels original coefficients through order24. Any remaining finite exponent would be at least25, forcing every nonzero maximal minor to have order at least31. The authenticated degree bound30 excludes this. Rank36 still follows from the already established lower pivots; it is not an assumption that an infinite recursion has converged.

Conversely, generic rank36 makes every successive original obstruction generically zero. The comparison and torsion-freeness then give global zero quotient classes, and the gauge induction constructs the finite certificate. Thus the stated equivalence, including its global direction, is justified. No square-conic base-change lifting or full-adjoint conclusion is used.

## Independent character check and production replay

Independently computed symmetric-power characters on the five A5 conjugacy classes, with class sizes 1,15,20,12,12, reproduce all twenty-one retained rows. This calculation uses the determinant-one three-dimensional character and pairs with P and D; it is separate from the production binary-icosahedral implementation and its Newton check. In particular, the original-sixth lift, m-gauge, kappa-gauge and target dimensions are 5,2,0,3. The kappa term is `Hom_G(P,Sym^(n-5) A)`, first nonzero at quotient n=8.

The production verifier was read, then executed normally and with Python optimization. Both 46-check outputs agree byte-for-byte with each other and with `RESULT.json`. The retained gate table agrees with the independent calculation. Reproduction commands are `python verify.py` and `python -O verify.py`. The symbolic bookkeeping checks supplement, rather than replace, the actual-map and sheaf argument audited above.

## Immediate-input authentication

Each of the following exact public commit/path resources was freshly fetched during this review. Its content agrees byte-for-byte with the retained input, including both the manifest SHA256 and Git blob hash:

| Input | Commit | Git blob |
|---|---|---|
| 1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| 1025 | `09f1377f83b027ca27eea0b3a9f40a1b92c6c466` | `d036adcf5bc2bfc53e07cd752ff180c5993251f7` |
| 1103 | `0c2da01cfa9440d25b38360a5742ee8b32f20d0f` | `d19ae749f54ec46eb667ffd70bc54868b595a227` |
| 1104 | `287a94911cdfec629529490e5c1642ddbe610b31` | `cf560b059d337f64a79a3f39ee7a962c27143843` |

The exact paths and SHA256 values are in `INPUTS.json`. Authentication covers these four immediate inputs, not a fresh recursive reproof of their geometric ancestry. No actual source coefficients, parameter values, directions, jets or source-instance ranks were evaluated.
