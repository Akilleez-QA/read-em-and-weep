# Source2 has an exact projected residual Gauss flag

## Result

For stable ID **G3.21.d610e381ed75**, source index2, the actual saturated projected residual of PR751 has the exact backward Gauss flag

    R=O(-18)+A_std O(-6),
    R^-=W O(-7),
    R^{--}=O(-8),
    R^{---}=0.

Its ranks are (4,2,1,0), its degrees are (-36,-14,-8,0), and its consecutive quotient bundles are

    O(-18)+O(-4),  O(-6),  O(-8).

In particular the previously known inclusion S=W O(-7) subset R^- is equality. This is a condition on the actual projected source, not just a formal splitting. It selects no parameter in the abstract degree-eighteen family and excludes no quotient label.

## 1. A constant-projection kernel lemma

Let F be a saturated subbundle of a constant bundle H tensor O, and let V be a constant subspace. Suppose D=F intersect (V tensor O) is a subbundle and the image C=F/D is saturated in the genuine constant quotient (H/V) tensor O. All Gauss kernels below use these constant connections.

If C^-=0, then

    F^-=D^-.                                           (1)

Indeed projection commutes with the constant connection. Therefore it maps local sections of F^- into C^-, so F^- lies in D. For a section of D, its derivative lies in V tensor Omega. Such a derivative lies in F tensor Omega exactly when it lies in D tensor Omega, because D=F intersect V tensor O. Consequently the derivative-kernel condition inside F agrees with the derivative-kernel condition inside D. This proves equality as sheaves, not just equality of generic ranks.

A negative saturated line C in a constant bundle has C^-=0. Its second fundamental form cannot vanish identically, since that would make it a horizontal constant line subbundle of degree0. A nonzero morphism from a line to a vector bundle has zero sheaf kernel.

## 2. Apply the actual constant projection, not a connection on a complement

PR751, commite21d50b6bd7d124dc419beeb8c27fa3b9ef3e169, proves all of the following for the same actual source:

    R subset Hbar tensor O is saturated;
    V1=Sym8 W=P+D is an actual invariant constant subspace of Hbar;
    D=R intersect (V1 tensor O)=A0=A_std O(-6);
    0 -> R/A0=O(-18) -> (Hbar/V1) tensor O -> (P+D)O2 -> 0.

Thus C=R/A0 is a negative saturated line in the genuine constant quotient. It has zero backward kernel. Formula (1) gives

    R^-=A0^-.

This uses only the published actual intersection and saturation. There is no projection onto an arbitrary bundle complement, and no assumption that a connection descends to an abstract residual.

## 3. The complete degree-eight osculating flag

The same theorem identifies A0 as the actual second osculating bundle of the complete degree-eight line in V1=Sym8 W. Write

    U_j=Sym^j W O(j-8),   with fiber l^(8-j) Sym^j W.

For j=0,1,2, differentiation has a nonzero rank-one leading symbol from U_j into (U_(j+1)/U_j) tensor Omega; its kernel is U_(j-1), with U_(-1)=0. To check this directly, use l=x+t y and the local section l^(8-j)y^j. Its derivative modulo U_j is

    (8-j) l^(7-j)y^(j+1).

The coefficient 8-j is respectively8,7,6, hence nonzero in characteristic zero. The lower-j osculating fibers give exactly the kernel. Therefore

    A0^-=U2^-=U1=W O(-7),
    U1^-=U0=O(-8),
    U0^-=0.

Together with Section2 this proves the exact residual flag. The universal evaluation quotients U2/U1=O(-4) and U1/U0=O(-6), together with R/U2=O(-18), give the asserted consecutive quotient splittings; R/U1=O(-18)+O(-4) is also the actual quotient already proved in PR738.

## Scope and reproduction

This supersedes the tentative longer rank-one alternative argument. The orbit-size bound on a derivative zero divisor and a subsequent terminal-kernel contradiction are unnecessary after the actual constant-span intersection of PR751. No extra claim about either of those proposed intermediate arguments is needed.

Run `python3 verify_two_one_index_two_exact_residual_gauss_flag.py` to generate `two-one-index-two-exact-residual-gauss-flag.json`. The small standalone checker pins the published prerequisite and stable baseline row, verifies the universal nonzero symbols and all flag ranks, degrees and quotient degrees. The proof supplies the constant-projection lemma and its actual geometric hypotheses.

No selected actual coefficients or points, actual-instance matrices/ranks, parameter evaluation, scan, spike or consumed experiment is used. No previous frozen file, label count or abstract-feasibility claim is changed.
