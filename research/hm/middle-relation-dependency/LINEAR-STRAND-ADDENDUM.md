# A bound on the remaining linear third syzygies

Use the notation of PROOF.md and the audited vector-relation calculation. Then

    a=0 implies d=0;
    a=15 implies d∈{0,5,10,15,20,25,30}.

This adds the finite upper bound d≤30 to the previously known nonnegative divisibility condition. No realization assertion is made.

Let E=R₂, viewed as a vector space of dimension ten, and let A=Tor₂^S(L,C)₃. The first relation map is S(−2)⊗E→S⊗U, whose degree-three kernel is precisely A⊂X⊗E. The minimal cubic relation generators are linearly independent modulo XR₂, so a degree-three syzygy cannot involve them with nonzero constant coefficients. Thus this description of A is valid even when a=15 and those cubic generators are present.

We claim

    Tor₃^S(L,C)₄ = ker[X⊗A → S₂⊗E],                 (1)

where the map is ordinary polynomial multiplication after the inclusion A⊂X⊗E.

To justify this carefully, let F• be the full minimal resolution. In internal degree four, the free module F₂ has contributions X⊗A from its degree-three generators, and constant coefficients on its degree-four generators B. The images of B form a basis of the quotient of degree-four syzygies by X times degree-three syzygies; this is precisely the minimal-generator property for the syzygy module im(F₂→F₁). Consequently, if an element of F₂,₄ maps to zero, its B-component vanishes. Its remaining component belongs to X⊗A. The differential of an element of A has entries only in the degree-two summand S(−2)⊗E of F₁: it cannot have scalar entries in the degree-three summand because the resolution is minimal. Thus the differential restricted to X⊗A is exactly the multiplication map in (1).

Finally F₃ has no generators in degrees below four, so F₃,₄ is its degree-four generator space, of dimension d. The next free module F₄ has no elements in degree four, by the same minimum-degree bound (its generator degrees are at least five). Exactness therefore identifies F₃,₄ with ker(F₂,₄→F₁,₄), proving (1).

If a=0, (1) gives d=0. If a=15, apply the universal module shadow inequality to the 15-dimensional subspace A⊂S₁⊗E, with dim S₁=5 and dim S₂=15:

    dim(XA) ≥ (15/5)·15=45.

The source X⊗A has dimension 75. Equation (1) gives

    d=75−dim(XA)≤30.

The previously audited nontrivial Heisenberg central character in internal degree four forces 5 to divide d. This proves the stated finite list.

Only minimal graded resolution theory and the universal polynomial-shadow inequality are used; no actual multiplication matrix, coefficient selection, or rank-instance evaluation is performed.
