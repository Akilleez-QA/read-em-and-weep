# The unmultiplied first-normal matrix cannot extend square-zero across the third neighborhood

## Inputs and scope

Retain the full actual filtered harmonic frame of PR692 at 858f96ba1539afb1293f31239b8761af08e46f60, with regular trace-free weighted matrices and even binary degrees. A matrix of weight d has diagonal, upper and lower degrees d,d−2,d+2. Thus regular matrices have order at least −2. The actual first-normal matrix is Ns=H(n_full)+qH(T_full) modulo q², with orders at least eight and four. Its leading terms are n8=u[[fg,−f²],[g²,−fg]] and T4, with degrees f=3,g=5, a regular pair, and u nonzero. It is square-zero modulo q².

Use the [scalar-slope theorem, PR729](https://github.com/Akilleez-QA/read-em-and-weep/blob/c384ae419983a5031af19c37674df020de1aa5da/research/hm/firstnormal-scalar-slope/PROOF.md): the leading degree-eight second-square scalar d2 of n8+qT4 has nonzero image in (S/(f))8 for every regular pair. That theorem derives its nonzero image independently of the choice of nilpotent T4. Its hypotheses are the same regular-pair and first-normal hypotheses used here; the present proof uses its nonvanishing conclusion without repeating its formal harmonic calculation.

The ambient third-neighborhood algebra is the regular completed coefficient algebra modulo (q³), with q the fixed quadric equation; square-zero means the matrix square vanishes in that quotient, entry by entry. This is extension of a fixed class modulo (q²), not an assertion about a chosen representative outside these quotients. A trace-free lift always exists as a matrix: lift the upper/lower entries and one diagonal entry harmonically, and take the other diagonal entry to be its negative. The question is whether any such lift has square zero. The difference of any two such regular trace-free lifts is q²H(K) modulo q³; regularity in this actual frame forces the entry degree bounds above, hence ord K≥−2.

Pinned frame dependency:
https://github.com/Akilleez-QA/read-em-and-weep/blob/858f96ba1539afb1293f31239b8761af08e46f60/research/hm/vertex-scalar-filtration/PROOF.md

The scalar-slope dependency is fixed at commit c384ae419983a5031af19c37674df020de1aa5da.

## Claim

There is no regular trace-free extension of this fixed Ns to the third neighborhood that remains square-zero. This is a local obstruction at the generic vertex in the actual frame. It is not a statement about a different first-normal matrix, a change of frame allowing poles, or the multiplied J3.

## Filtered proof

Every regular trace-free extension has the form

 Nhat=H(n_full)+qH(T_full)+q²H(K) modulo q³,

with K of weighted order at least −2. Its square coefficient at q² is

 D_full+tr(n_full K),

where

 D_full=sc(T_full²+B1(n_full,T_full)+B1(T_full,n_full)+B2(n_full,n_full))

has order at least eight. The second expression uses ordinary multiplication because a q² factor is already present. At weight six the entire equation is therefore

 tr(n8 K_(−2))=0.

The only regular weight−2 entry is a constant lower entry c; the diagonal and upper entries have negative degrees and vanish. Thus this equation is −u f² c=0. The domain property and nonzero u,f force c=0, hence K_(−2)=0.

At weight eight, all higher filtered terms of n_full multiplying K_(−2) disappear, and the equation reduces to

 d2+tr(n8 K0)=0.

A regular weight-zero trace-free matrix has constant diagonal x, zero upper entry, and quadratic lower entry z. Consequently

 tr(n8 K0)=u(2fgx−f²z) in (f²S2+kfg) subset fS5.

Reduction modulo f would give [d2]=0, contrary to the scalar-slope theorem. Therefore no such regular K exists.

The proof uses neither actual coefficients nor actual point/derivative/rank evaluations. It retains the higher filtered actual data and excludes their contribution by order, rather than replacing the actual pair by a homogeneous model.

## Why this does not contradict J3

The multiplied leading matrix P=a²h n8 has weight twelve. Its second-normal correction R has weight four, and the relevant trace map from weight-four matrices to S12 is surjective. Thus the multiplication by the quartic source changes the regularity/degree budget and allows its q² square equation to be solved, as previously established. The nonextendibility of Ns does not exclude the already-existing multiplied J3. It identifies the local root of the nonzero scalar slope rather than deciding the actual fourth-square class.
