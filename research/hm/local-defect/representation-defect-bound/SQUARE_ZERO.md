Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Square-zero isolated self-dual defects have length at most five times rank

## Universal theorem

Under the hypotheses of PROOF.md, if m²Q=0 then

    length_R(Q)≤5 rank_R(M).

This bound requires no nontrivial group action and follows already from the scalar part of the generator bound. In particular a rank-two isolated self-dual reflexive module has no square-zero defect of length greater than ten.

## Proof with all Koszul ranks specified

Let n=dim_C Q, b=dim_C mQ, and

    a=dim_C(Q/soc(Q)),   soc(Q)={q : mq=0}.

The square-zero hypothesis gives mQ⊂soc(Q), so b≤n−a. Choose four regular parameters and write d_i for the differential

    Q⊗Λ^i W → Q⊗Λ^{i−1} W

in their Koszul complex, with r_i=rank_C d_i. In degree four, d₄(q⊗vol) records all four parameter products of q. Its kernel is soc(Q)⊗Λ⁴W. Thus r₄=a.

Since multiplication kills soc(Q), d₃ factors through (Q/soc(Q))⊗Λ³W, a vector space of dimension 4a. Its image lies in mQ⊗Λ²W, a space of dimension 6b. Consequently

    r₃≤4a,   r₃≤6b≤6(n−a).                 (1)

Koszul homology computes Tor with the residue field. Therefore

    β₄(Q)=n−a,
    β₃(Q)=4n−r₃−a,
    β₃(Q)−2β₄(Q)=2n−r₃+a.

The scalar necessary rank inequality from PROOF.md is r≥β₃−2β₄. Hence

    r₃−a≥2n−r.                              (2)

Combining (2) with the first bound in (1) gives

    a≥(2n−r)/3.

Combining it with the second gives

    a≤(4n+r)/7.

The compatibility of these inequalities implies

    7(2n−r)≤3(4n+r),
    2n≤10r,
    n≤5r.

All inequalities are valid also when 2n−r≤0, or Q=0; no positivity division was used.

## Equality rigidity and combination with representation imbalance

If n=5r, every inequality above is an equality:

    a=3r, b=2r, r₃=12r,
    soc(Q)=mQ,
    β₃(Q)−2β₄(Q)=r.

Thus d₃ induces an isomorphism

    (Q/soc(Q))⊗Λ³W → mQ⊗Λ²W.

In the equivariant setting this is an isomorphism of representations as well. Moreover PROOF.md forces a_H(Tor₁(D(Q),k))=0 at equality.

More generally set e=a_H(Tor₁(D(Q),k)). The strengthened rank bound gives r−e≥2n−r₃+a. Repeating the same calculation with r replaced by r−e yields

    n≤5(r−e), or equivalently r≥n/5+e.

This is a necessary condition for square-zero defects, not a realization assertion.

## Conditional canonical consequence

If the separately audited canonical rank-two arguments exclude all positive local defect lengths 1 through 10 under the same equivariance hypotheses, then every nonzero canonical defect must satisfy

    m²Q≠0.

Indeed square-zero defects have length at most ten by the theorem. Equivalently the Loewy length must be at least three. The universal bound here is proved independently of the low-length exclusions; this note does not audit those external exclusions or change a global numerical bound by itself.

No physical source-model matrix, operation, input, rank instance, jet, or residue was evaluated. The proof uses only universal local algebra and finite-dimensional rank inequalities.
